// Read-only pixel inspection: each mapped illustration must contain more than a blank cell.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),data=JSON.parse(fs.readFileSync(path.join(root,process.argv.includes('--partial')?'.work/previews/catalog-v2-preview.json':'data/catalog.json'),'utf8'));
(async()=>{
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage();await page.goto('about:blank');
 const cells=[];
 for(const b of data.boards.filter(b=>b.items.some(x=>data.entries.find(e=>e.id===x.entry_id).added_in==='27.0'))){
  const src='data:image/png;base64,'+fs.readFileSync(path.join(root,b.image)).toString('base64');
  const stats=await page.evaluate(async({src,columns,rows,count,xs,ys})=>{
   const img=new Image();img.src=src;await img.decode();
   const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.drawImage(img,0,0);
   const result=[];
   for(let i=0;i<count;i++){
    const col=i%columns,row=Math.floor(i/columns),x0=xs?xs[col]:col*img.width/columns,y0=ys?ys[row]:row*img.height/rows,cw=xs?xs[col+1]-xs[col]:img.width/columns,ch=ys?ys[row+1]-ys[row]:img.height/rows;const x=Math.floor(x0+cw*.08),y=Math.floor(y0+ch*.16),w=Math.floor(cw*.84),h=Math.floor(ch*.77),pixels=ctx.getImageData(x,y,w,h).data;
    let n=0,sum=0,sum2=0,dark=0;
    for(let j=0;j<pixels.length;j+=16){const v=pixels[j]*.2126+pixels[j+1]*.7152+pixels[j+2]*.0722;n++;sum+=v;sum2+=v*v;if(v<215)dark++;}
    const stdev=Math.sqrt(Math.max(0,sum2/n-(sum/n)**2));result.push({i,stdev:Number(stdev.toFixed(2)),darkFraction:Number((dark/n).toFixed(4)),suspect:stdev<8&&dark/n<.012});
   }
   return result;
  },{src,columns:b.columns,rows:b.rows,count:b.items.length,xs:b.column_boundaries,ys:b.row_boundaries});
  for(const x of stats)cells.push({board:b.id,entry:b.items[x.i].entry_id,name:b.items[x.i].name,...x});
 }
 await browser.close();
 const report={checked:cells.length,expected:data.entries.filter(e=>e.added_in==='27.0').length,suspect:cells.filter(c=>c.suspect),minimumVariance:Math.min(...cells.map(c=>c.stdev)),cells};
 fs.mkdirSync(path.join(root,'.work/verification/v27'),{recursive:true});fs.writeFileSync(path.join(root,'.work/verification/v27','image-cells.json'),JSON.stringify(report,null,2));assert.equal(report.checked,report.expected);assert.deepEqual(report.suspect,[]);console.log(JSON.stringify({checked:report.checked,expected:report.expected,suspect:report.suspect,minimumVariance:report.minimumVariance}));
})().catch(e=>{console.error(e);process.exitCode=1});
