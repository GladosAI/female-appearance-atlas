// Preserve the chosen PNG and use its alpha shape for theme-colored logo exports.
const fs=require('node:fs'),path=require('node:path'),os=require('node:os'),crypto=require('node:crypto');
let sharp;try{sharp=require('sharp')}catch{
 for(const base of [process.env.CODEX_NODE_MODULES,path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules')].filter(Boolean)){
  try{sharp=require(path.join(base,'sharp'));break}catch{}
 }
}
if(!sharp)throw Error('Brand exports require sharp. Install it locally or set CODEX_NODE_MODULES.');
const root=path.resolve(__dirname,'../..'),active=JSON.parse(fs.readFileSync(path.join(root,'assets/brand/active.json'),'utf8')),dir=path.join(root,active.directory),palettes=JSON.parse(fs.readFileSync(path.join(root,'tools/templates/theme_palettes.json'),'utf8'));
function ico(images){
 const header=Buffer.alloc(6+16*images.length);header.writeUInt16LE(1,2);header.writeUInt16LE(images.length,4);let offset=header.length;
 images.forEach(({size,buffer},i)=>{const at=6+16*i;header[at]=size===256?0:size;header[at+1]=size===256?0:size;header.writeUInt16LE(1,at+4);header.writeUInt16LE(32,at+6);header.writeUInt32LE(buffer.length,at+8);header.writeUInt32LE(offset,at+12);offset+=buffer.length});
 return Buffer.concat([header,...images.map(i=>i.buffer)]);
}
(async()=>{
 const original=fs.readFileSync(path.join(root,active.source)),metadata=await sharp(original).metadata();if(!metadata.hasAlpha)throw Error('The selected logo must retain transparency.');
 const embedded=(await sharp(original).resize(512,512).png().toBuffer()).toString('base64');
 const shape='<defs><filter id="beauty-profile-ink" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feFlood flood-color="currentColor" result="ink"/><feComposite in="ink" in2="SourceAlpha" operator="in"/></filter></defs><image x="2" y="2" width="60" height="60" filter="url(#beauty-profile-ink)" href="data:image/png;base64,'+embedded+'"/>';
 const light=palettes.find(p=>p.id==='light'),dark=palettes.find(p=>p.id==='dark');
 const svg=(p,tile=false,system=false)=>'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" color="'+p.colors.accent+'"><title>女性之美</title><desc>'+active.description+'</desc>'+(system?'<style>:root{color:'+light.colors.accent+'}.tile{fill:'+light.colors.soft+'}@media(prefers-color-scheme:dark){:root{color:'+dark.colors.accent+'}.tile{fill:'+dark.colors.soft+'}}</style>':'')+(tile?'<rect class="tile" width="64" height="64" rx="15" fill="'+p.colors.soft+'"/>':'')+shape+'</svg>\n';
 fs.writeFileSync(path.join(dir,'logo.svg'),svg(light));
 await sharp(Buffer.from(svg(light))).resize(512,512).png().toFile(path.join(dir,'logo.png'));
 for(const p of palettes)fs.writeFileSync(path.join(dir,'favicon-'+p.id+'.svg'),svg(p,true));
 fs.writeFileSync(path.join(dir,'favicon.svg'),svg(light,true,true));
 const fallback=Buffer.from(svg(light,true)),images=[];
 for(const size of [16,32,48,256])images.push({size,buffer:await sharp(fallback).resize(size,size).png().toBuffer()});
 fs.writeFileSync(path.join(dir,'favicon.ico'),ico(images));
 for(const size of [16,32,48])fs.writeFileSync(path.join(dir,'favicon-'+size+'.png'),images.find(i=>i.size===size).buffer);
 for(const [name,size]of [['apple-touch-icon.png',180],['icon-192.png',192],['icon-512.png',512]])await sharp(fallback).resize(size,size).flatten({background:light.colors.soft}).png().toFile(path.join(dir,name));
 const manifest={id:active.id,name:active.name,selected_concept:active.selected_concept,source:active.source,source_sha256:crypto.createHash('sha256').update(original).digest('hex'),svg_format:'SVG display file embeds the selected PNG alpha silhouette; it is not a traced path vector.',themes:palettes.map(p=>p.id),ico_sizes:images.map(i=>i.size)};
 fs.writeFileSync(path.join(dir,'release.json'),JSON.stringify(manifest,null,2)+'\n');
 const tiles=[];
 for(let i=0;i<palettes.length;i++){
  const p=palettes[i],image=await sharp(Buffer.from(svg(p))).resize(104,104).png().toBuffer(),face=await sharp(Buffer.from(svg(p,true))).resize(32,32).png().toBuffer();
  const background='<svg xmlns="http://www.w3.org/2000/svg" width="320" height="240"><rect width="320" height="240" fill="'+p.colors.bg+'"/><rect x="104" y="20" width="112" height="112" rx="24" fill="'+p.colors.soft+'"/><text x="160" y="171" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="22" font-weight="600" fill="'+p.colors.ink+'">女性之美</text><text x="160" y="198" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="'+p.colors.muted+'">'+p.name+'</text></svg>';
  tiles.push({input:await sharp(Buffer.from(background)).composite([{input:image,left:108,top:24},{input:face,left:144,top:205}]).png().toBuffer(),left:(i%2)*320,top:Math.floor(i/2)*240});
 }
 const out=path.join(root,'.work/verification/brand-release');fs.mkdirSync(out,{recursive:true});
 await sharp({create:{width:640,height:480,channels:4,background:'#fff'}}).composite(tiles).png().toFile(path.join(out,'approved-palettes.png'));
 const smalls=[];for(let i=0;i<3;i++)smalls.push({input:await sharp(images[i].buffer).resize(128,128,{kernel:'nearest'}).png().toBuffer(),left:16+i*160,top:16});
 await sharp({create:{width:480,height:160,channels:4,background:light.colors.bg}}).composite(smalls).png().toFile(path.join(out,'favicon-sizes.png'));
 console.log(JSON.stringify({passed:true,selected:active.id,theme_icons:palettes.length,source_sha256:manifest.source_sha256}));
})().catch(e=>{console.error(e);process.exitCode=1});
