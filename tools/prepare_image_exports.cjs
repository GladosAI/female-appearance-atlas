// Lossless browser-readable image sources for offline PNG export.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const sharp=require('sharp');
sharp.concurrency(1);
const root=path.resolve(__dirname,'..'),indexPath=path.join(root,'data/image-export-index.json');
const data=JSON.parse(fs.readFileSync(path.join(root,'data/catalog.json'),'utf8'));
const images=[...new Set(data.entries.flatMap(e=>['visual','wearing_visual','fullbody_visual'].map(k=>e[k]?.image).filter(Boolean)))];
const index=fs.existsSync(indexPath)?JSON.parse(fs.readFileSync(indexPath,'utf8')):{};
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
fs.mkdirSync(path.join(root,'images/export-data'),{recursive:true});
(async()=>{
 let cursor=0,done=0,generated=0;
 async function worker(){while(cursor<images.length){const image=images[cursor++],input=fs.readFileSync(path.join(root,image)),hash=digest(input),old=index[image];
  if(!(old?.source_sha256===hash&&old.mime==='image/webp'&&fs.existsSync(path.join(root,old.file)))){
   const output=await sharp(input,{limitInputPixels:false}).webp({lossless:true,effort:0}).toBuffer();
   const file='images/export-data/'+digest(Buffer.from(image)).slice(0,12)+'-'+hash.slice(0,12)+'.js';
   const dataUrl='data:image/webp;base64,'+output.toString('base64');
   fs.writeFileSync(path.join(root,file),'(globalThis.__atlasImageData ||= Object.create(null))['+JSON.stringify(image)+']='+JSON.stringify(dataUrl)+';\n');
   index[image]={source_sha256:hash,mime:'image/webp',file};generated++;
  }
  done++;if(done%50===0)console.log('Prepared '+done+'/'+images.length+' image sources');
 }}
 await Promise.all(Array.from({length:4},worker));
 fs.writeFileSync(indexPath,JSON.stringify(Object.fromEntries(images.map(k=>[k,index[k]])),null,2)+'\n');
 console.log(JSON.stringify({images:images.length,generated,lossless:true}));
})().catch(e=>{console.error(e);process.exitCode=1});
