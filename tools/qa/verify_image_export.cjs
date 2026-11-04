const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const sharp=require('./runtime.cjs').sharp;
const root=path.resolve(__dirname,'../..'),data=JSON.parse(fs.readFileSync(path.join(root,'data/catalog.json'),'utf8'));
const output=path.join(root,'.work/verification/image-export');fs.mkdirSync(output,{recursive:true});
(async()=>{
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 try{
  const context=await browser.newContext({acceptDownloads:true,viewport:{width:1280,height:900}}),p=await context.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));
  await p.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{write:async items=>{
   const item=items[0],blob=await item.getType('image/png'),bitmap=await createImageBitmap(blob),digest=await crypto.subtle.digest('SHA-256',await blob.arrayBuffer());
   window.copiedImage={types:item.types,width:bitmap.width,height:bitmap.height,hash:Array.from(new Uint8Array(digest)).map(x=>x.toString(16).padStart(2,'0')).join('')};bitmap.close();
  }}}));
  const url=pathToFileURL(path.join(root,'index.html')).href;
  async function open(e){await p.goto(url+'?section=all&q='+encodeURIComponent(e.id==='AH020'?'AH02':e.id));await p.locator(`[data-detail="${e.id}"]`).first().click();await p.locator('#detail-dialog').waitFor({state:'visible'})}
  async function checkDownload(e,kind,visual){
   const button=p.locator(`[data-image-export="download"][data-image-entry="${e.id}"][data-image-kind="${kind}"]`);
   const [download]=await Promise.all([p.waitForEvent('download'),button.click()]);assert(download.suggestedFilename().endsWith('.png'));assert(download.suggestedFilename().startsWith(e.id+'-'));
   const file=path.join(output,download.suggestedFilename());await download.saveAs(file);
   const m=await sharp(path.join(root,visual.image)).metadata(),r=visual.crop;
   const x=r?r.x*m.width/r.sheet_width:visual.column*m.width/visual.columns,y=r?r.y*m.height/r.sheet_height:visual.row*m.height/visual.rows;
   const w=r?r.width*m.width/r.sheet_width:m.width/visual.columns,h=r?r.height*m.height/r.sheet_height:m.height/visual.rows;
   const rect={left:Math.round(x),top:Math.round(y),width:Math.round(x+w)-Math.round(x),height:Math.round(y+h)-Math.round(y)};
   const actual=await sharp(file).metadata();assert.equal(actual.format,'png');assert.equal(actual.width,rect.width);assert.equal(actual.height,rect.height);
   const expectedPixels=await sharp(path.join(root,visual.image)).extract(rect).removeAlpha().raw().toBuffer(),actualPixels=await sharp(file).removeAlpha().raw().toBuffer();
   assert.deepEqual(actualPixels,expectedPixels,e.id+' '+kind+' must preserve source pixels');return file;
  }
  const ah=data.entries.find(e=>e.id==='AH020');await open(ah);
  assert.equal(await p.locator('#detail-dialog [data-image-export]').count(),2);
  const file=await checkDownload(ah,'auto',ah.visual);
  await p.locator('[data-image-export="copy"]').click();await p.waitForFunction(()=>window.copiedImage);
  const copied=await p.evaluate(()=>window.copiedImage);assert.deepEqual(copied.types,['image/png']);assert.equal(copied.width,256);assert.equal(copied.height,376);
  const crypto=require('node:crypto');assert.equal(copied.hash,crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'));
  assert((await p.locator('.image-export-status').innerText()).includes('图片已复制'));
  // The same-board cache and next-entry navigation still export the requested cell.
  const next=data.entries.find(e=>e.id==='AH021');await p.locator('#next-detail').click();assert((await p.locator('#detail-heading').innerText()).includes(next.id));await checkDownload(next,'auto',next.visual);
  const art=data.entries.find(e=>e.art_style_reference&&e.fullbody_visual);await open(art);assert.equal(await p.locator('#detail-dialog [data-image-export]').count(),4);
  await checkDownload(art,'fullbody',art.fullbody_visual);await checkDownload(art,'object',art.visual);
  const glasses=data.entries.find(e=>e.category==='eyewear'&&e.wearing_visual);await open(glasses);
  await checkDownload(glasses,'wearing',glasses.wearing_visual);await checkDownload(glasses,'object',glasses.visual);
  const legacy=data.entries.find(e=>e.visual&&!e.visual.crop&&!e.wearing_visual&&!e.fullbody_visual);assert(legacy);await open(legacy);await checkDownload(legacy,'auto',legacy.visual);
  for(const id of ['VD008','VH004','VS001','VC008','DF005','VX005','MV004','ZT004','NS008','SE003','MC003','MX012','SB006','FK008','GX002','GX006','GA001','GA008','GO002','GO008','GP001','GP008','MC013','MC017','MC023','MC028','MX016','MX018','MX022','MX027']){const entry=data.entries.find(e=>e.id===id);assert(entry);await open(entry);await checkDownload(entry,'auto',entry.visual)}
  await p.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{write:async()=>{throw new DOMException('Denied','NotAllowedError')}}}));
  await p.locator('[data-image-export="copy"]').click();await p.waitForFunction(()=>document.querySelector('.image-export-status').textContent.includes('允许剪贴板'));assert(await p.locator('[data-image-export="copy"]').isEnabled());
  await p.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:undefined}));await p.locator('[data-image-export="copy"]').click();assert((await p.locator('.image-export-status').innerText()).includes('不支持复制图片'));
  await open(ah);await p.screenshot({path:path.join(output,'desktop.png')});
  await p.setViewportSize({width:390,height:844});await open(glasses);assert(await p.locator('#detail-dialog').evaluate(e=>e.scrollWidth<=e.clientWidth+1));assert.equal(await p.locator('#detail-dialog [data-image-export]').count(),4);
  await p.screenshot({path:path.join(output,'mobile.png')});
  // The normal served-page path exports the same pixels without offline sidecars.
  const server=require('node:http').createServer((req,res)=>{let file;try{file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname))}catch{res.writeHead(400).end();return}
   if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return}if(!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404).end();return}
   res.setHeader('Content-Type',file.endsWith('.html')?'text/html;charset=utf-8':file.endsWith('.png')?'image/png':file.endsWith('.js')?'text/javascript':'application/octet-stream');fs.createReadStream(file).pipe(res);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  try{await p.setViewportSize({width:1280,height:900});await p.goto('http://127.0.0.1:'+server.address().port+'/index.html?section=all&q=AH020');await p.locator('[data-detail="AH020"]').first().click();await checkDownload(ah,'auto',ah.visual)}finally{await new Promise(resolve=>server.close(resolve))}
  assert.deepEqual(errors,[]);console.log(JSON.stringify({passed:true,local_file:true,http:true,png_pixels:'lossless source crops',clipboard:'PNG payload validated',views:'single, fullbody, portrait, wearing, object, legacy',failure_feedback:true,mobile:true}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
