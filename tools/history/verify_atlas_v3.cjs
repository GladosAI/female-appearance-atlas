const {chromium}=require('../qa/runtime.cjs').playwright;
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..'),partial=process.argv.includes('--partial');
const data=JSON.parse(fs.readFileSync(path.join(root,partial?'catalog-v2-preview.json':'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(root,'verification-v3/catalog-v2.json'),'utf8'));
const out=path.join(root,'verification-v3');fs.mkdirSync(out,{recursive:true});
const report={partial,checks:[],errors:[],meta:data.meta};let browser;
const checked=x=>report.checks.push(x);
(async()=>{
 assert.equal(data.entries.length,1501);assert.equal(data.categories.length,37);assert.equal(data.meta.clothing_count,711);
 assert.equal(new Set(data.entries.map(e=>e.id)).size,1501);assert.equal(new Set(data.entries.map(e=>e.name)).size,1501);
 for(const old of prior.entries){const e=data.entries.find(e=>e.id===old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual)}
 const clothingIds=new Set(data.meta.clothing_categories),clothes=data.entries.filter(e=>clothingIds.has(e.category));assert.equal(clothes.length,711);
 const newItems=data.entries.filter(e=>!prior.entries.some(old=>old.id===e.id));assert.equal(newItems.length,464);assert.ok(newItems.every(e=>clothingIds.has(e.category)));
 if(!partial)assert.ok(data.entries.every(e=>e.visual));
 for(const c of data.categories)assert.equal(c.count,data.entries.filter(e=>e.category===c.id).length);
 for(const e of data.entries){e.related_reading.forEach(id=>assert.ok(data.references.some(r=>r.id===id)));if(e.visual)assert.ok(fs.existsSync(path.join(root,e.visual.image)))}
 checked('464 new clothing references; 711 clothing references; 1501 unique entries. All 1037 old IDs and illustration mappings remain compatible.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,partial?'index-v2-preview.html':'index.html')).href;
 await page.goto(url+'?edition=3&section=clothing');await page.waitForFunction(()=>document.querySelectorAll('#entry-grid .entry').length===72);
 assert.equal(await page.locator('#result-status').textContent(),'711 个结果 · 显示 72 个');
 await page.screenshot({path:path.join(out,'clothing-desktop.png'),fullPage:false});
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .entry').count(),711);
 const rendered=await page.locator('#entry-grid .meta .tag').allTextContents();assert.ok(rendered.every(name=>data.categories.some(c=>c.group==='clothing'&&c.name===name)));
 checked('Clothing URL, aggregate section and all 711 clothing cards render without appearance categories.');
 await page.locator('.jump [data-category="clothing_new"]').click();assert.match(await page.locator('#result-status').textContent(),/^464 /);assert.equal(await page.locator('#entry-grid .title-button').first().textContent(),'古巴领短衬衫');await page.screenshot({path:path.join(out,'new-clothing-desktop.png'),fullPage:false});checked('The new-clothing shortcut immediately shows the 464 added references.');
 await page.locator('.jump [data-category="tops"]').count().then(async n=>{if(n)await page.locator('.jump [data-category="tops"]').click();else await page.locator('#categories [data-category="tops"]').click()});
 await page.locator('#dimension-filter').selectOption({label:'衬衫与布帛上衣'});assert.equal(await page.locator('#entry-grid .entry').count(),16);
 await page.locator('#entry-grid [data-detail]').first().click();const first=await page.locator('#detail-heading').textContent();await page.locator('#next-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('ArrowLeft');assert.equal(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('Escape');
 await page.locator('.jump [data-category="clothing"]').click();await page.locator('#search').fill('半拉链针织衫');assert.equal(await page.locator('#entry-grid .entry').count(),1);await page.locator('#clear-search').click();await page.locator('#search').fill('piano recital');assert.equal(await page.locator('#entry-grid .entry').count(),1);await page.locator('#clear-search').click();
 checked('Clothing subdimensions, new Chinese/English searches and detail navigation work.');
 await page.locator('.jump [data-category="fantasy_outfits"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),64);
 await page.locator('#dimension-filter').selectOption({label:'魔法少女结构方案'});assert.equal(await page.locator('#entry-grid .entry').count(),16);
 await page.locator('.jump [data-category="layered_outfits"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),48);
 await page.locator('.jump [data-category="all"]').click();while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .entry').count(),1501);if(!partial)assert.equal(await page.locator('#entry-grid .image-button').count(),1501);
 checked('New fantasy, transformation and ensemble filters work; all 1501 final cards have images.');
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('clothing');const expected=data.boards.filter(b=>b.items.some(x=>clothingIds.has(data.entries.find(e=>e.id===x.entry_id).category))).length;assert.equal(await page.locator('#board-list .board').count(),expected);
 checked('Contact-sheet gallery supports the aggregate clothing section.');
 await page.locator('.nav [data-view="combinations"]').click();assert.equal(await page.locator('.combo').count(),32);await page.locator('[data-combo="0"]').click();await page.locator('.nav [data-view="card"]').click();assert.equal(await page.locator('#selected-grid .entry').count(),6);
 const wait=page.waitForEvent('download');await page.locator('#export-card').click();const dl=await wait;await dl.saveAs(path.join(out,'roundtrip.json'));await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(out,'roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);checked('Appearance-card export/import and original combinations still work.');
 if(!partial){const failed=await page.evaluate(async paths=>{const failed=[];for(const p of paths)await new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{failed.push(p);resolve()};i.src=p});return failed},[...new Set(data.boards.map(b=>b.image).concat(data.references.filter(r=>r.image).map(r=>r.image)))]);assert.deepEqual(failed,[]);checked('All 120 contact sheets and six museum photographs load.');}
 await page.goto(url+'?section=clothing');await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'clothing-dark.png'),fullPage:false});await page.emulateMedia({colorScheme:'light'});await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(out,'clothing-mobile.png'),fullPage:false});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.locator('#mobile-category').selectOption('stage_outfits');assert.equal(await page.locator('#entry-grid .entry').count(),32);await page.locator('#mobile-category').selectOption('clothing');assert.match(await page.locator('#result-status').textContent(),/^711 /);checked('Dark/mobile rendering and mobile clothing category navigation work.');
 assert.deepEqual(report.errors,[]);checked('No runtime or image-resource errors.');report.passed=true;await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,meta:data.meta}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
