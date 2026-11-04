// Read pixels without editing images; identify long grid rules for display crops.
const fs=require('node:fs'),path=require('node:path');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),boards=JSON.parse(fs.readFileSync(path.join(root,'source/extra-illustrations.json'),'utf8')).filter(b=>JSON.parse(fs.readFileSync(path.join(root,'source/image-jobs.json'),'utf8')).some(j=>j.edition===20&&j.id===b.id));
(async()=>{
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true}),page=await browser.newPage();const report=[];
 for(const board of boards){
  const src='data:image/png;base64,'+fs.readFileSync(path.join(root,board.image)).toString('base64');
  const grid=await page.evaluate(async src=>{
   const img=new Image();img.src=src;await img.decode();const canvas=document.createElement('canvas');canvas.width=img.width;canvas.height=img.height;const ctx=canvas.getContext('2d');ctx.drawImage(img,0,0);const pixels=ctx.getImageData(0,0,img.width,img.height).data;
   function axis(vertical){const size=vertical?img.width:img.height,other=vertical?img.height:img.width,bounds=[0],rules=[];
    for(let i=1;i<4;i++){const target=size*i/4,span=size/4*.30,candidates=[];
     for(let k=Math.floor(target-span);k<=Math.ceil(target+span);k++){let dark=0,total=0;for(let j=4;j<other-4;j++){const p=(vertical?j*img.width+k:k*img.width+j)*4;const v=pixels[p]*.2126+pixels[p+1]*.7152+pixels[p+2]*.0722;if(v<220)dark++;total++;}candidates.push({k,score:dark/total});}
     const max=Math.max(...candidates.map(x=>x.score));const peaks=candidates.filter(x=>x.score>=max-.025).sort((a,b)=>Math.abs(a.k-target)-Math.abs(b.k-target));const best=peaks[0];const pair=candidates.filter(x=>Math.abs(x.k-best.k)<=12&&x.score>=max-.07);const boundary=Math.round((Math.min(...pair.map(x=>x.k))+Math.max(...pair.map(x=>x.k)))/2);
     bounds.push(boundary);rules.push({target:Number(target.toFixed(2)),boundary,score:Number(max.toFixed(3))});
    }bounds.push(size);return {bounds,rules};}
   return {columns:axis(true),rows:axis(false),width:img.width,height:img.height};
  },src);report.push({id:board.id,image:board.image,...grid});
 }
 await browser.close();fs.writeFileSync(path.join(root,'.work/verification/v20/grid-boundaries.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
})().catch(e=>{console.error(e);process.exitCode=1});
