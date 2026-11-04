const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium}=require('../qa/runtime.cjs').playwright;
const root=path.resolve(__dirname,'..'),out=path.join(root,'verification-v13');
const data=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(out,'catalog-v12.json'),'utf8'));
const report={checks:[],errors:[],meta:data.meta};let browser;
(async()=>{
 assert.equal(data.meta.version,'13.0');assert.equal(data.entries.length,3693);assert.equal(data.categories.length,83);assert.equal(data.boards.length,262);assert.equal(data.meta.missing_image_count,0);assert.equal(data.meta.illustrated_count,3693);assert.equal(data.meta.new_count,32);assert.equal(data.meta.facial_count,492);assert.equal(data.meta.clothing_count,1679);
 const byId=new Map(data.entries.map(e=>[e.id,e]));assert.equal(byId.size,3693);assert.equal(new Set(data.entries.map(e=>e.name)).size,3693);
 for(const old of prior.entries){const e=byId.get(old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual);assert.equal(e.added_in,old.added_in);assert.deepEqual(e.keywords,old.keywords);}
 assert.deepEqual(data.references,prior.references);assert.deepEqual(data.combinations,prior.combinations);assert.deepEqual(data.style_families,prior.style_families);
 const additions=data.entries.filter(e=>e.added_in==='13.0');assert.equal(additions.length,32);
 for(const e of additions){assert.equal(e.age_context,'成年角色面部绘画参考');assert.equal(e.facial_reference,true);assert.ok(e.visual);}
 for(const [cat,n] of Object.entries({face_states:64,face_emotions:80,mouth_actions:48,face_hands:48,face_overlays:32,face_augments:32}))assert.equal(data.entries.filter(e=>e.category===cat).length,n);
 for(const e of data.entries)assert.ok(fs.existsSync(path.join(root,e.visual.image)));
 const boards=data.boards.filter(b=>b.items.some(x=>additions.some(e=>e.id===x.entry_id)));assert.equal(boards.length,2);
 for(const b of boards){assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.items.length,16);const png=fs.readFileSync(path.join(root,b.image));assert.equal(png.readUInt32BE(16),b.width);assert.equal(png.readUInt32BE(20),b.height);for(const x of b.items)assert.equal(x.name,byId.get(x.entry_id).name);}
 report.checks.push('All 3661 earlier names, IDs, image mappings, keywords and edition labels are preserved. All 32 adult additions have mapped, reviewed images.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,'index.html')).href;
 await page.goto(url+'?edition=3&section=clothing');assert.match(await page.locator('#result-status').textContent(),/^1679 /);assert.match(await page.locator('.edition').textContent(),/13$/);
 await page.locator('.jump [data-category="clothing_new"]').click();assert.match(await page.locator('#result-status').textContent(),/^32 /);assert.equal(await page.locator('#entry-grid .image-button').count(),32);
 const ids=await page.locator('#entry-grid .meta>span:first-child').allTextContents();assert.ok(additions.every(e=>ids.some(t=>t.startsWith(e.id))));
 await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'additions-desktop.png')});
 for(const [cat,dim,word,n] of [['face_states','眩晕与晕眩表演','眩晕',64],['face_emotions','困惑疑问与不解反应','困惑',80]]){
  await page.goto(url+'?section='+cat);while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),n);
  await page.locator('#dimension-filter').selectOption(dim);assert.equal(await page.locator('#entry-grid .image-button').count(),16);await page.locator('#search').fill(word);assert.equal(await page.locator('#entry-grid .entry').count(),16);
  await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,word+'-desktop.png')});
  await page.locator('#entry-grid [data-detail]').last().click();const heading=await page.locator('#detail-heading').textContent();await page.locator('#prev-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),heading);await page.keyboard.press('Escape');
 }
 await page.goto(url+'?section=facial');assert.match(await page.locator('#result-status').textContent(),/^492 /);
 for(const word of ['困惑','疑惑','不解','眩晕','晕眩','头晕','confused','dizziness']){await page.locator('#search').fill(word);assert.ok(await page.locator('#entry-grid .entry').count()>=16,word);assert.equal(await page.locator('#entry-grid .entry').count(),await page.locator('#entry-grid .image-button').count());}
 await page.locator('#search').fill('');while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),492);
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('facial');assert.equal(await page.locator('#board-list .board').count(),data.boards.filter(b=>b.items.some(x=>byId.get(x.entry_id).facial_reference)).length);
 for(const b of boards)assert.equal(await page.locator('[data-board="'+b.id+'"]').count(),1);
 const failed=await page.evaluate(async paths=>{const bad=[];await Promise.all(paths.map(p=>new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p})));return bad},boards.map(b=>b.image));assert.deepEqual(failed,[]);
 report.checks.push('Both new 16-entry subgroups, Chinese/English aliases, detail navigation, 32-entry latest scope and 492-entry facial gallery render correctly.');
 await page.goto(url+'?section=cosplay');assert.match(await page.locator('#result-status').textContent(),/^368 /);
 await page.locator('.nav [data-view="card"]').click();await page.locator('#clear-card').click();const roundtrip=path.join(root,'verification-v12/roundtrip.json');await page.locator('#import-file').setInputFiles(roundtrip);await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);assert.equal(await page.locator('#selected-grid .image-button').count(),6);
 await page.setViewportSize({width:390,height:844});
 for(const [cat,dim] of [['face_states','眩晕与晕眩表演'],['face_emotions','困惑疑问与不解反应']]){
  await page.goto(url+'?section='+cat);assert.equal(await page.locator('#mobile-category').inputValue(),cat);await page.locator('#dimension-filter').selectOption(dim);assert.equal(await page.locator('#entry-grid .image-button').count(),16);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,cat+'-mobile.png')});
 }
 await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'confusion-dark-mobile.png')});
 report.checks.push('Legacy clothing URL, cosplay scope and V12 appearance-card import remain compatible. Both new subgroups work on mobile and in dark mode without overflow.');
 assert.deepEqual(report.errors,[]);report.passed=true;await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,entries:data.entries.length}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
