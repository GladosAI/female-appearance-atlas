// Export actual corrected tiles, including offline lossless sidecars and WebP delivery.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL,fileURLToPath}=require('node:url');
const {launchBrowser,sharp}=require('./runtime.cjs');
const root=path.resolve(__dirname,'../..'),base=process.env.ATLAS_TEST_URL||pathToFileURL(path.join(root,'index.html')).href;
const read=async url=>url.protocol==='file:'?fs.readFileSync(fileURLToPath(url)):Buffer.from(await(await fetch(url)).arrayBuffer());
(async()=>{const data=JSON.parse((await read(new URL('data/catalog.json',base))).toString('utf8'));
 const browser=await launchBrowser();try{
 const page=await browser.newPage({acceptDownloads:true,viewport:{width:1280,height:900}}),errors=[];page.on('pageerror',error=>errors.push(error.message));
 const checked=[];
 const reviewed=new Map(),reviewRepresentatives=new Set();
 for(const file of fs.readdirSync(path.join(root,'source/quality-reviews')).filter(name=>name.endsWith('.json')).sort((a,b)=>a.localeCompare(b,'en',{numeric:true}))){
  const review=JSON.parse(fs.readFileSync(path.join(root,'source/quality-reviews',file),'utf8'));
  for(const record of review.records||[])if(record.field==='visual')reviewed.set(record.entry_id,record);
  for(const id of review.export_representatives||[])reviewRepresentatives.add(id);
 }
 const scenes=data.entries.filter(e=>e.scene_reference),representatives=[...new Set(scenes.map(e=>e.category))].map(category=>scenes.find(e=>e.category===category).id);
 for(const id of new Set(['HR025','HR045','HR053','FW046','SO075',
  'PO004','PO018','PO023','PO036','PO049','PO057',
  'HG001','HG013','HG017','HG029','HG033','HG045',...reviewRepresentatives,...representatives])){
  const entry=data.entries.find(e=>e.id===id),visual=entry.visual;
  if(reviewRepresentatives.has(id)){
   const approved=reviewed.get(id)?.visual_at_review;assert(approved,id+' requires a review snapshot');
   assert.equal(visual.board,approved.board,id+' reviewed board');
   assert.deepEqual(visual.crop,approved.crop,id+' approved crop geometry');
  }
  await page.goto(base+'?section='+entry.category+'&entry='+id);await page.locator('#detail-dialog').waitFor({state:'visible'});
  const kind=entry.wearing_visual?'object':'auto';
  const button=page.locator('#detail-dialog [data-image-export="download"][data-image-kind="'+kind+'"]').first();await button.waitFor();
  const event=page.waitForEvent('download');await button.click();const downloaded=fs.readFileSync(await(await event).path());
  const input=await read(new URL(visual.image,base)),size=await sharp(input).metadata();
  const left=Math.round(visual.column*size.width/visual.columns),top=Math.round(visual.row*size.height/visual.rows);
  const r=visual.crop||{x:left,y:top,width:Math.round((visual.column+1)*size.width/visual.columns)-left,height:Math.round((visual.row+1)*size.height/visual.rows)-top};
  const expected=await sharp(input).extract({left:r.x,top:r.y,width:r.width,height:r.height}).removeAlpha().raw().toBuffer();
  const result=await sharp(downloaded).removeAlpha().raw().toBuffer({resolveWithObject:true});
  assert.equal(result.info.width,r.width,id+' export width');assert.equal(result.info.height,r.height,id+' export height');
  assert.equal(result.data.length,expected.length);let difference=0;
  for(let i=0;i<expected.length;i++)difference+=Math.abs(expected[i]-result.data[i]);
  assert(difference/expected.length<1,id+' exported pixels must match the approved region');
  if(entry.wearing_visual)assert(await page.locator('#detail-dialog [data-image-kind="wearing"]').count()>0,'Keep the separate wearing illustration');
  checked.push({id,width:r.width,height:r.height,mean_pixel_difference:difference/expected.length});
 }
 await page.setViewportSize({width:390,height:844});assert(await page.locator('#detail-dialog').evaluate(e=>e.scrollWidth<=e.clientWidth+1));
 const output=path.join(root,'.work/qa');fs.mkdirSync(output,{recursive:true});await page.screenshot({path:path.join(output,'material-quality-mobile.png')});
 assert.deepEqual(errors,[]);console.log(JSON.stringify({passed:true,approved_crop_exports:checked,wearing_visuals_preserved:true,mobile:true}));
 }finally{await browser.close()}})().catch(error=>{console.error(error);process.exitCode=1});
