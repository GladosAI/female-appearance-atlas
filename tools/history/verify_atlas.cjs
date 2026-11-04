const { chromium } = require('../qa/runtime.cjs').playwright;
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'verification');
fs.mkdirSync(out, {recursive:true});
const data = JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const report = {checks:[], errors:[], screenshots:[]};
function checked(label){report.checks.push(label);}
(async()=>{
  const browser = await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:1080},deviceScaleFactor:1});
  page.on('pageerror',e=>report.errors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text());});
  await page.goto(pathToFileURL(path.join(root,'index.html')).href);
  await page.waitForFunction(()=>document.querySelectorAll('#entry-grid .entry').length===72);
  await page.screenshot({path:path.join(out,'desktop.png'),fullPage:false});report.screenshots.push('desktop.png');
  assert.equal(await page.locator('#result-status').textContent(),'88 个结果 · 显示 72 个');
  await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .entry').count(),88);checked('All 88 illustrated cards render.');
  await page.locator('#all-mode').click();
  while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();
  assert.equal(await page.locator('#entry-grid .entry').count(),582);checked('All 582 entries render without duplication.');
  const ids = data.entries.map(e=>e.id);assert.equal(new Set(ids).size,582);
  assert.equal(new Set(data.entries.map(e=>e.name)).size,582);
  for(const c of data.categories){assert.equal(data.entries.filter(e=>e.category===c.id).length,c.count);}
  for(const e of data.entries){for(const id of e.related_reading)assert.ok(data.references.some(r=>r.id===id));if(e.visual)assert.ok(fs.existsSync(path.join(root,e.visual.image)));}
  for(const r of data.references){if(r.image)assert.ok(fs.existsSync(path.join(root,r.image)));}
  checked('Category counts, unique IDs, visual paths, and reference IDs are consistent.');
  await page.locator('#search').fill('羊腿袖');assert.equal(await page.locator('#entry-grid .entry').count(),1);assert.ok((await page.locator('#entry-grid').textContent()).includes('leg-of-mutton'));checked('Chinese terminology search finds the correct construction entry.');
  await page.locator('#clear-search').click();await page.locator('#search').fill('fishtail');assert.equal(await page.locator('#entry-grid .entry').count(),1);checked('English terminology search finds the correct braid.');
  await page.locator('#clear-search').click();await page.locator('[data-category="face"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),18);checked('Category filter displays all 18 face entries.');
  await page.locator('#entry-grid [data-detail]').first().click();await page.locator('#detail-dialog').waitFor({state:'visible'});await page.screenshot({path:path.join(out,'detail.png'),fullPage:false});report.screenshots.push('detail.png');
  await page.locator('#detail-dialog [data-save]').click();assert.equal(await page.locator('#top-saved-count').textContent(),'1');await page.keyboard.press('Escape');checked('Detail dialog, component selection, and Escape close work.');
  await page.locator('.nav [data-view="references"]').click();await page.locator('#museum-grid img').last().scrollIntoViewIfNeeded();await page.waitForFunction(()=>[...document.querySelectorAll('#museum-grid img')].every(i=>i.complete&&i.naturalWidth>0));
  await page.locator('#references-view').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'references.png'),fullPage:false});report.screenshots.push('references.png');checked('All six local museum reference photos load.');
  await page.locator('.nav [data-view="combinations"]').click();assert.equal(await page.locator('.combo').count(),24);await page.locator('[data-combo="0"]').click();assert.equal(await page.locator('#top-saved-count').textContent(),'7');checked('Combination selection adds its six distinct components.');
  await page.locator('.nav [data-view="card"]').click();await page.locator('#card-name').fill('QA character');await page.locator('#card-notes').fill('Persistent appearance selection');
  const downloadPromise=page.waitForEvent('download');await page.locator('#export-card').click();const download=await downloadPromise;await download.saveAs(path.join(out,'roundtrip-card.json'));
  const exported=JSON.parse(fs.readFileSync(path.join(out,'roundtrip-card.json'),'utf8'));assert.equal(exported.selected.length,7);assert.equal(exported.schema,'female-appearance-card/v1');
  await page.locator('#clear-card').click();assert.equal(await page.locator('#top-saved-count').textContent(),'0');await page.locator('#import-file').setInputFiles(path.join(out,'roundtrip-card.json'));await page.waitForFunction(()=>document.getElementById('top-saved-count').textContent==='7');
  await page.reload();await page.locator('.nav [data-view="card"]').click();assert.equal(await page.locator('#selected-grid .entry').count(),7);assert.equal(await page.locator('#card-name').inputValue(),'QA character');checked('Export/import round trip and browser reload persistence retain all selected components and notes.');
  // Remove QA data from the inspection browser only.
  await page.evaluate(()=>localStorage.removeItem('female-appearance-atlas-v1'));await page.reload();
  await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'dark.png'),fullPage:false});report.screenshots.push('dark.png');
  await page.emulateMedia({colorScheme:'light'});await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(out,'mobile.png'),fullPage:false});report.screenshots.push('mobile.png');
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);assert.equal(overflow,false);checked('390px mobile layout has no horizontal overflow; dark theme renders.');
  assert.equal(report.errors.length,0);checked('No browser runtime or resource errors.');
  await browser.close();
  report.passed=true;report.meta={entries:582,illustrations:88,categories:20,references:19,museumPhotos:6,combinations:24};
  fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
})().catch(e=>{report.passed=false;report.failure=e.stack;fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1;});
