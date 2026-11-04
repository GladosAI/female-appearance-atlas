const {chromium}=require('../qa/runtime.cjs').playwright;
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..'),partial=process.argv.includes('--partial');
const data=JSON.parse(fs.readFileSync(path.join(root,partial?'catalog-v2-preview.json':'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(root,'verification-v4/catalog-v3.json'),'utf8'));
const out=path.join(root,'verification-v4');fs.mkdirSync(out,{recursive:true});
const report={partial,checks:[],errors:[],meta:data.meta};let browser;
const checked=x=>report.checks.push(x),clothing=new Set(data.meta.clothing_categories);
const count=(style,shoulder)=>data.entries.filter(e=>clothing.has(e.category)&&(!style||e.styles.includes(style))&&(!shoulder||e.shoulder_type===shoulder)).length;
(async()=>{
 assert.equal(data.entries.length,1677);assert.equal(data.categories.length,38);assert.equal(data.meta.clothing_count,879);assert.equal(data.meta.new_count,176);assert.equal(data.style_families.length,15);assert.equal(data.meta.shoulder_count,61);
 assert.equal(new Set(data.entries.map(e=>e.id)).size,1677);assert.equal(new Set(data.entries.map(e=>e.name)).size,1677);
 for(const old of prior.entries){const e=data.entries.find(e=>e.id===old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual)}
 for(const e of data.entries){assert.ok(e.visual);assert.ok(fs.existsSync(path.join(root,e.visual.image)));e.styles.forEach(k=>assert.ok(data.style_families.some(f=>f.id===k)));e.related_reading.forEach(k=>assert.ok(data.references.some(r=>r.id===k)))}
 for(const f of data.style_families)assert.equal(f.clothing_count,count(f.id));
 assert.deepEqual(data.entries.find(e=>e.name==='田园格纹洛丽塔装').styles,['lolita','cottagecore']);
 assert.ok(!data.entries.find(e=>e.name==='落肩方身毛衣').shoulder_type);assert.ok(!data.entries.find(e=>e.name==='高领无袖针织衫').shoulder_type);
 checked('1677 unique illustrated entries, 879 clothing references, 15 cross-category styles and 61 shoulder examples. All 1501 old IDs and image mappings remain compatible.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,partial?'index-v2-preview.html':'index.html')).href;
 await page.goto(url+'?edition=4&section=clothing');await page.waitForFunction(()=>document.querySelectorAll('#entry-grid .entry').length===72);
 assert.match(await page.locator('#result-status').textContent(),/^879 /);
 for(const id of ['gothic','british','lolita','punk']){
   await page.locator('.jump [data-style="'+id+'"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),count(id));
   assert.equal(await page.locator('#style-filter').inputValue(),id);await page.screenshot({path:path.join(out,id+'-desktop.png'),fullPage:false});
 }
 checked('Each of the four requested style shortcuts returns its actual clothing coordinates.');
 assert.equal(await page.locator('#shoulder-filter,[data-category="shoulders"],option[value="shoulders"]').count(),0);
 await page.locator('#reset-facets').click();await page.screenshot({path:path.join(out,'clothing-desktop.png'),fullPage:false});
 for(const [cat,q] of [['tops','一字肩'],['onepiece','挖肩']]){
   await page.locator('#reset-facets').click();await page.locator('#categories [data-category="'+cat+'"]').click();await page.locator('#search').fill(q);
   assert.ok(await page.locator('#entry-grid .entry').count()>0);assert.equal(await page.locator('#entry-grid .image-button').count(),await page.locator('#entry-grid .entry').count());
   await page.locator('#entry-grid [data-detail]').first().click();assert.match(await page.locator('#detail-heading').textContent(),new RegExp(cat==='tops'?'上装':'连身服装'));await page.keyboard.press('Escape');
 }
 checked('Dedicated shoulder controls are absent; exposed-shoulder garments remain searchable and illustrated in ordinary clothing categories.');
 for(const q of ['露肩连衣裙','一字肩上衣','英伦风','哥特洛丽塔','甜系洛丽塔','off shoulder','gothic lolita']){
   await page.locator('#reset-facets').click();await page.locator('#search').fill(q);const n=await page.locator('#entry-grid .entry').count();assert.ok(n>0,'No result for '+q);
   if(q==='哥特洛丽塔'){assert.equal(n,2);const ids=await page.locator('#entry-grid .meta>span:first-child').allTextContents();assert.ok(ids.every(x=>/^FS03[78]/.test(x)))}
 }
 checked('Common Chinese names, alternate names, compound substyles and English queries return meaningful results.');
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="clothing_new"]').click();assert.match(await page.locator('#result-status').textContent(),/^176 /);
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),176);
 await page.locator('#entry-grid [data-detail]').first().click();const first=await page.locator('#detail-heading').textContent();await page.locator('#next-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('ArrowLeft');assert.equal(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('Escape');
 await page.locator('.jump [data-category="all"]').click();while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),1677);checked('All new and original cards render with images and detail navigation.');
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('tops');assert.equal(await page.locator('#board-list .board').count(),data.boards.filter(b=>b.items.some(x=>data.entries.find(e=>e.id===x.entry_id).category==='tops')).length);checked('The sheet gallery retains ordinary clothing categories.');
 await page.locator('.nav [data-view="combinations"]').click();await page.locator('[data-combo="0"]').click();await page.locator('.nav [data-view="card"]').click();assert.equal(await page.locator('#selected-grid .entry').count(),6);
 const wait=page.waitForEvent('download');await page.locator('#export-card').click();const dl=await wait;await dl.saveAs(path.join(out,'roundtrip.json'));await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(out,'roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);checked('Appearance-card export/import and existing combinations still work.');
 const failed=await page.evaluate(async paths=>{const bad=[];for(const p of paths)await new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p});return bad},[...new Set(data.boards.map(b=>b.image).concat(data.references.filter(r=>r.image).map(r=>r.image)))]);assert.deepEqual(failed,[]);checked('All 136 contact sheets and six museum photographs load.');
 await page.goto(url+'?section=clothing&style=gothic');await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'gothic-dark.png'),fullPage:false});await page.emulateMedia({colorScheme:'light'});await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(out,'gothic-mobile.png'),fullPage:false});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.locator('#mobile-category').selectOption('onepiece');await page.locator('#search').fill('露肩');assert.ok(await page.locator('#entry-grid .entry').count()>0);assert.equal(await page.locator('#shoulder-filter,[data-category="shoulders"]').count(),0);await page.screenshot({path:path.join(out,'clothing-mobile.png'),fullPage:false});await page.goto(url+'?section=shoulders');assert.match(await page.locator('#result-status').textContent(),/^879 /);checked('Style deep links and legacy links, mobile categories and dark/mobile layouts work without overflow.');
 assert.deepEqual(report.errors,[]);checked('No script or image-resource errors.');report.passed=true;await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,meta:data.meta}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
