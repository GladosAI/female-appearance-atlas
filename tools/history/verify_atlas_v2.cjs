const {chromium}=require('../qa/runtime.cjs').playwright;
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..'),partial=process.argv.includes('--partial'),data=JSON.parse(fs.readFileSync(path.join(root,partial?'catalog-v2-preview.json':'catalog.json'),'utf8'));
const out=path.join(root,'verification-v2');fs.mkdirSync(out,{recursive:true});
const report={partial,checks:[],errors:[],meta:data.meta};
function checked(x){report.checks.push(x)}
let browser;
(async()=>{
 assert.equal(data.entries.length,1037);assert.equal(data.categories.length,33);
 assert.equal(new Set(data.entries.map(e=>e.id)).size,1037);assert.equal(new Set(data.entries.map(e=>e.name)).size,1037);
 if(!partial)assert.ok(data.entries.every(e=>e.visual));
 for(const c of data.categories)assert.equal(c.count,data.entries.filter(e=>e.category===c.id).length);
 for(const e of data.entries){e.related_reading.forEach(id=>assert.ok(data.references.some(r=>r.id===id)));if(e.visual)assert.ok(fs.existsSync(path.join(root,e.visual.image)));}
 checked('1037 unique entries, 33 categories, image mapping and related reading IDs are consistent.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 await page.goto(pathToFileURL(path.join(root,partial?'index-v2-preview.html':'index.html')).href);
 await page.waitForFunction(()=>document.querySelectorAll('#entry-grid .entry').length===72);
 assert.equal(await page.locator('#result-status').textContent(),'1037 个结果 · 显示 72 个');
 await page.screenshot({path:path.join(out,'desktop.png'),fullPage:false});
 await page.locator('[data-category="construction"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),52);
 await page.locator('#dimension-filter').selectOption({label:'袖型'});assert.equal(await page.locator('#entry-grid .entry').count(),20);checked('Category and construction subdimension filters show the expected 52 and 20 entries.');
 await page.locator('#entry-grid [data-detail]').first().click();const first=await page.locator('#detail-heading').textContent();await page.locator('#next-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('ArrowLeft');assert.equal(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('Escape');checked('Detail next/previous controls and arrow-key navigation work within the filtered set.');
 await page.locator('[data-category="all"]').click();await page.locator('#search').fill('羊腿袖');assert.equal(await page.locator('#entry-grid .entry').count(),1);await page.locator('#clear-search').click();await page.locator('#search').fill('fedora');assert.equal(await page.locator('#entry-grid .entry').count(),1);checked('Chinese and new English vocabulary searches work.');
 await page.locator('#clear-search').click();while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .entry').count(),1037);if(!partial)assert.equal(await page.locator('#entry-grid .image-button').count(),1037);checked('All 1037 cards render; final edition requires every card to have an image.');
 await page.locator('.nav [data-view="boards"]').click();assert.equal(await page.locator('#board-list .board').count(),data.boards.length);
 await page.locator('#board-category').selectOption('hats');const expected=data.boards.filter(b=>b.items.some(x=>data.entries.find(e=>e.id===x.entry_id).category==='hats')).length;assert.equal(await page.locator('#board-list .board').count(),expected);checked('Contact-sheet gallery supports the new category filter.');
 await page.locator('.nav [data-view="combinations"]').click();assert.equal(await page.locator('.combo').count(),32);await page.locator('[data-combo="0"]').click();await page.locator('.nav [data-view="card"]').click();assert.equal(await page.locator('#selected-grid .entry').count(),6);
 const wait=page.waitForEvent('download');await page.locator('#export-card').click();const dl=await wait;await dl.saveAs(path.join(out,'roundtrip.json'));const exported=JSON.parse(fs.readFileSync(path.join(out,'roundtrip.json'),'utf8'));assert.equal(exported.selected.length,6);await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(out,'roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);checked('32 combinations and external appearance-card export/import retain selected components.');
 // Check every source image directly in the rendering browser, including sheets not yet scrolled into view.
 if(!partial){const result=await page.evaluate(async paths=>{const failed=[];for(const p of paths){await new Promise(resolve=>{const i=new Image();i.onload=()=>resolve();i.onerror=()=>{failed.push(p);resolve()};i.src=p})}return failed},[...new Set(data.boards.map(b=>b.image).concat(data.references.filter(r=>r.image).map(r=>r.image)))]);assert.deepEqual(result,[]);checked('All contact sheets and six museum photographs load as image resources.');}
 await page.evaluate(()=>localStorage.removeItem('female-appearance-atlas-v1'));await page.reload();await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'dark.png'),fullPage:false});await page.emulateMedia({colorScheme:'light'});await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(out,'mobile.png'),fullPage:false});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth),false);checked('Dark and 390px mobile layouts render without horizontal overflow.');
 assert.deepEqual(report.errors,[]);checked('No runtime or resource errors.');report.passed=true;await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
