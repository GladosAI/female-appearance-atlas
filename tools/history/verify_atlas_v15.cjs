const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium}=require('../qa/runtime.cjs').playwright;
const root=path.resolve(__dirname,'..'),out=path.join(root,'verification-v15');
const data=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(out,'catalog-v14.json'),'utf8'));
const report={checks:[],errors:[],meta:data.meta};let browser;
(async()=>{
 assert.equal(data.meta.version,'15.0');assert.equal(data.entries.length,3853);assert.equal(data.categories.length,84);assert.equal(data.boards.length,272);assert.equal(data.meta.missing_image_count,0);assert.equal(data.meta.illustrated_count,3853);assert.equal(data.meta.new_count,64);assert.equal(data.meta.facial_count,556);assert.equal(data.meta.clothing_count,1775);assert.equal(data.meta.hosiery_count,102);
 const byId=new Map(data.entries.map(e=>[e.id,e]));assert.equal(byId.size,3853);assert.equal(new Set(data.entries.map(e=>e.name)).size,3853);
 for(const old of prior.entries){const e=byId.get(old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual);assert.equal(e.added_in,old.added_in);assert.deepEqual(e.keywords,old.keywords);}
 assert.deepEqual(data.references,prior.references);assert.deepEqual(data.combinations,prior.combinations);assert.deepEqual(data.style_families,prior.style_families);
 const additions=data.entries.filter(e=>e.added_in==='15.0');assert.equal(additions.length,64);
 for(const e of additions){assert.equal(e.age_context,'成年角色面部绘画参考');assert.equal(e.facial_reference,true);assert.ok(e.visual.crop);const c=e.visual.crop;assert.ok(c.x>=0&&c.y>=0&&c.x+c.width<=c.sheet_width&&c.y+c.height<=c.sheet_height);}
 for(const [cat,n] of Object.entries({face_states:80,face_emotions:128,mouth_actions:48,face_hands:48,face_overlays:32,face_augments:32}))assert.equal(data.entries.filter(e=>e.category===cat).length,n);
 assert.equal(additions.some(e=>(e.name+' '+e.keywords.join(' ')).includes('性需求')),false);
 for(const e of data.entries)assert.ok(fs.existsSync(path.join(root,e.visual.image)));
 const newIds=new Set(additions.map(e=>e.id)),boards=data.boards.filter(b=>b.items.some(x=>newIds.has(x.entry_id)));assert.equal(boards.length,4);
 for(const b of boards){assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.items.length,16);const png=fs.readFileSync(path.join(root,b.image));assert.equal(png.readUInt32BE(16),b.width);assert.equal(png.readUInt32BE(20),b.height);for(const x of b.items)assert.equal(x.name,byId.get(x.entry_id).name);}
 report.checks.push('All 3789 prior names, IDs, image crops, keywords and edition labels remain unchanged. All 64 additions have adult context, reviewed images and valid individual display crops.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,'index.html')).href;
 await page.goto(url+'?edition=3&section=clothing');assert.match(await page.locator('#result-status').textContent(),/^1775 /);assert.match(await page.locator('.edition').textContent(),/15$/);
 await page.locator('.jump [data-category="clothing_new"]').click();assert.equal(await page.locator('#entry-grid .image-button').count(),64);assert.match(await page.locator('#result-status').textContent(),/^64 /);
 const latest=await page.locator('#entry-grid .meta>span:first-child').allTextContents();assert.ok(additions.every(e=>latest.some(t=>t.startsWith(e.id))));
 for(const q of ['潮红','挑逗','魅惑','勾引']){await page.locator('#search').fill(q);assert.equal(await page.locator('#entry-grid .image-button').count(),16,q);}
 await page.locator('#search').fill('');await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'additions-desktop.png')});
 const topics=[['face_states','潮红位置与色感表现','潮红'],['face_emotions','挑逗逗趣与轻度调情','挑逗'],['face_emotions','魅惑目光与含蓄笑意','魅惑'],['face_emotions','含蓄勾引与暧昧邀约','勾引']];
 for(const [cat,dimension,q] of topics){
  await page.goto(url+'?section='+cat);await page.locator('#dimension-filter').selectOption(dimension);assert.equal(await page.locator('#entry-grid .image-button').count(),16);await page.locator('#search').fill(q);assert.equal(await page.locator('#entry-grid .entry').count(),16);
  await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,q+'-desktop.png')});
  await page.locator('#entry-grid [data-detail]').last().click();const title=await page.locator('#detail-heading').textContent();await page.locator('#prev-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),title);await page.keyboard.press('Escape');
 }
 await page.goto(url+'?section=facial');assert.match(await page.locator('#result-status').textContent(),/^556 /);while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),556);
 for(const q of ['潮红','挑逗','魅惑','勾引','blush','charming','flirty invitation']){await page.locator('#search').fill(q);assert.ok(await page.locator('#entry-grid .entry').count()>=16,q);}
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('facial');assert.equal(await page.locator('#board-list .board').count(),data.boards.filter(b=>b.items.some(x=>byId.get(x.entry_id).facial_reference)).length);for(const b of boards)assert.equal(await page.locator('[data-board="'+b.id+'"]').count(),1);
 const failed=await page.evaluate(async paths=>{const bad=[];await Promise.all(paths.map(p=>new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p})));return bad},boards.map(b=>b.image));assert.deepEqual(failed,[]);
 report.checks.push('All four 16-entry topics, Chinese/English aliases, latest scope, detail navigation and the 556-entry facial overview/gallery render their images correctly.');
 await page.goto(url+'?section=socks');assert.match(await page.locator('#result-status').textContent(),/^102 /);await page.locator('#search').fill('20D');assert.equal(await page.locator('#entry-grid .image-button').count(),1);assert.match(await page.locator('#entry-grid .title-button').textContent(),/^20D/);
 await page.goto(url+'?section=cosplay');assert.match(await page.locator('#result-status').textContent(),/^368 /);await page.locator('.nav [data-view="card"]').click();await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(root,'verification-v12/roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);
 await page.setViewportSize({width:390,height:844});await page.goto(url+'?section=facial');assert.equal(await page.locator('#mobile-category').inputValue(),'facial');assert.match(await page.locator('#result-status').textContent(),/^556 /);
 for(const [cat,dimension,q] of [topics[0],topics[2],topics[3]]){
  await page.locator('#mobile-category').selectOption(cat);await page.locator('#dimension-filter').selectOption(dimension);assert.equal(await page.locator('#entry-grid .image-button').count(),16);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,q+'-mobile.png')});
 }
 await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'inviting-dark-mobile.png')});
 report.checks.push('Legacy clothing URL, hosiery exact-D search, cosplay scope and old appearance-card import still work; facial mobile subgroups and dark mode have no horizontal overflow.');
 assert.deepEqual(report.errors,[]);report.passed=true;await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,entries:data.entries.length}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
