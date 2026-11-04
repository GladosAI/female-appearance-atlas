// Read pixels without editing images; identify long grid rules for display crops.
const fs=require('node:fs'),path=require('node:path');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),boards=JSON.parse(fs.readFileSync(path.join(root,'source/extra-illustrations.json'),'utf8')).filter(b=>JSON.parse(fs.readFileSync(path.join(root,'source/image-jobs.json'),'utf8')).some(j=>j.edition===30&&j.id===b.id));
(async()=>{
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true}),page=await browser.newPage();const report=[];
 for(const board of boards){
  const src='data:image/png;base64,'+fs.readFileSync(path.join(root,board.image)).toString('base64');
  const grid=await page.evaluate(async src=>{
   const img=new Image();img.src=src;await img.decode();const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;const ctx=canvas.getContext('2d');ctx.drawImage(img,0,0);const pixels=ctx.getImageData(0,0,img.width,img.height).data;
   function axis(vertical){const size=vertical?img.width:img.height,other=vertical?img.height:img.width,bounds=[0],rules=[];
    for(let i=1;i<4;i++){const target=size*i/4,span=size/4*.30,candidates=[];
     // Separators are darker than the paper and consistent along the axis.
     // Normalize darkness by luminance variation, allowing textured line colors.
     for(let k=Math.floor(target-span);k<=Math.ceil(target+span);k++){let sum=0,sum2=0,total=0,white=0;for(let j=4;j<other-4;j++){const p=(vertical?j*img.width+k:k*img.width+j)*4,r=pixels[p],g=pixels[p+1],b=pixels[p+2],v=r*.2126+g*.7152+b*.0722;sum+=v;sum2+=v*v;total++;if(v>235&&Math.max(r,g,b)-Math.min(r,g,b)<10)white++}const mean=sum/total,std=Math.sqrt(Math.max(0,sum2/total-mean*mean));candidates.push({k,white:white/total,score:(255-mean)/(std+5)/(1+Math.abs(k-target)/80)});}
     const whiteMax=Math.max(...candidates.map(x=>x.white)),light=whiteMax>.8;
     if(light)for(const c of candidates)c.score=c.white*12;
     const max=Math.max(...candidates.map(x=>x.score));const peaks=candidates.filter(x=>x.score>=max*.99).sort((a,b)=>Math.abs(a.k-target)-Math.abs(b.k-target));const boundary=peaks[0].k;
     bounds.push(boundary);rules.push({target:Number(target.toFixed(2)),boundary,score:Number(max.toFixed(3))});
    }bounds.push(size);return {bounds,rules};}
   return {columns:axis(true),rows:axis(false),width:img.width,height:img.height};
  },src);report.push({id:board.id,image:board.image,...grid});
 }
 await browser.close();fs.writeFileSync(path.join(root,'.work/verification/v30/grid-boundaries.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
})().catch(e=>{console.error(e);process.exitCode=1});
