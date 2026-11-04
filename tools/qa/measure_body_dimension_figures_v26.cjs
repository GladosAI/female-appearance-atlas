// Read-only native-pixel measurement. The PNGs are never modified or recoded.
const fs=require('node:fs'),path=require('node:path');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true}),page=await browser.newPage(),figures=[];
 const boards=read('source/extra-illustrations.json'),grids=read('.work/verification/v26/grid-boundaries.json');
 for(const grid of grids){const board=boards.find(b=>b.id===grid.id),src='data:image/png;base64,'+fs.readFileSync(path.join(root,board.image)).toString('base64');
  const bounds=await page.evaluate(async({src,xs,ys})=>{const img=new Image();img.src=src;await img.decode();const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;const ctx=canvas.getContext('2d');ctx.drawImage(img,0,0);const p=ctx.getImageData(0,0,img.width,img.height).data,out=[];
   for(let i=0;i<16;i++){const col=i%4,row=Math.floor(i/4),x0=xs[col],y0=ys[row],cw=xs[col+1]-x0,ch=ys[row+1]-y0;let minX=Infinity,minY=Infinity,maxX=0,maxY=0,n=0;
    for(let y=y0+5;y<y0+ch-5;y++)for(let x=x0+7;x<x0+cw-7;x++){if(y-y0<42&&x-x0<88)continue;const k=(y*img.width+x)*4,r=p[k],g=p[k+1],b=p[k+2],l=.2126*r+.7152*g+.0722*b,chroma=Math.max(r,g,b)-Math.min(r,g,b);if(!(l<150||(chroma<12&&l<205)))continue;minX=Math.min(minX,x);minY=Math.min(minY,y);maxX=Math.max(maxX,x);maxY=Math.max(maxY,y);n++}
    if(n<100)throw Error('Empty figure '+i);out.push({x:minX-1,y:minY-1,width:maxX-minX+3,height:maxY-minY+3,sheet_width:img.width,sheet_height:img.height,pixels:n});}
   return out;
  },{src,xs:grid.columns.bounds,ys:grid.rows.bounds});
  bounds.forEach((b,i)=>figures.push({id:board.items[i].entry_id,...b}));
 }
 await browser.close();fs.writeFileSync(path.join(root,'source/body-dimension-figures.json'),JSON.stringify(figures,null,2)+'\n');console.log(JSON.stringify(figures));
})().catch(e=>{console.error(e);process.exitCode=1});
