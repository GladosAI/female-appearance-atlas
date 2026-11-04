const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium}=require('../qa/runtime.cjs').playwright;
const root=path.resolve(__dirname,'..'),out=path.join(root,'verification-v14'),partial=process.argv.includes('--partial');
const data=JSON.parse(fs.readFileSync(path.join(root,partial?'catalog-v2-preview.json':'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(out,'catalog-v13.json'),'utf8'));
const report={partial,checks:[],errors:[],meta:data.meta};let browser;
(async()=>{
 assert.equal(data.meta.version,'14.0');assert.equal(data.entries.length,3789);assert.equal(data.categories.length,84);assert.equal(data.boards.length,268);assert.equal(data.meta.missing_image_count,0);assert.equal(data.meta.illustrated_count,3789);assert.equal(data.meta.new_count,96);assert.equal(data.meta.hosiery_count,102);assert.equal(data.meta.clothing_count,1775);assert.equal(data.meta.facial_count,492);
 const byId=new Map(data.entries.map(e=>[e.id,e]));assert.equal(byId.size,3789);assert.equal(new Set(data.entries.map(e=>e.name)).size,3789);
 for(const old of prior.entries){const e=byId.get(old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual);assert.equal(e.added_in,old.added_in);assert.deepEqual(e.keywords,old.keywords);}
 assert.deepEqual(data.references.slice(0,prior.references.length),prior.references);assert.equal(data.references.length,74);assert.deepEqual(data.combinations,prior.combinations);assert.deepEqual(data.style_families,prior.style_families);
 const additions=data.entries.filter(e=>e.added_in==='14.0');assert.equal(additions.length,96);assert.equal(data.entries.filter(e=>e.hosiery_reference).length,102);
 for(const e of additions){assert.equal(e.category,'hosiery');assert.equal(e.age_context,'成年规格袜类产品参考');assert.equal(e.hosiery_reference,true);assert.ok(e.visual);}
 assert.deepEqual(additions.filter(e=>e.denier).map(e=>e.denier),[6,8,10,12,15,20,25,30,40,50,60,80,100,120,150,200]);
 for(const e of data.entries)assert.ok(fs.existsSync(path.join(root,e.visual.image)));
 const boards=data.boards.filter(b=>b.category==='hosiery');assert.equal(boards.length,6);
 for(const b of boards){if(!partial)assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.items.length,16);const png=fs.readFileSync(path.join(root,b.image));assert.equal(png.readUInt32BE(16),b.width);assert.equal(png.readUInt32BE(20),b.height);for(const x of b.items)assert.equal(x.name,byId.get(x.entry_id).name);}
 report.checks.push('All 3693 earlier IDs, names, image mappings, keywords and edition labels are unchanged. All 96 new products and six 16-cell groups are mapped; the 102-entry overview retains the six original sock types.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,partial?'index-v2-preview.html':'index.html')).href;
 await page.goto(url+'?edition=3&section=clothing');assert.match(await page.locator('#result-status').textContent(),/^1775 /);assert.match(await page.locator('.edition').textContent(),/14$/);
 await page.locator('.jump [data-category="socks"]').click();assert.match(await page.locator('#result-status').textContent(),/^102 /);assert.match(await page.locator('#entry-grid .meta>span:first-child').first().textContent(),/^SO001/);
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),102);
 await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'socks-desktop.png')});
 const dims=[...new Set(additions.map(e=>e.dimension))];assert.equal(dims.length,6);
 for(const dim of dims){await page.locator('#dimension-filter').selectOption(dim);assert.equal(await page.locator('#entry-grid .image-button').count(),16);}
 await page.locator('#dimension-filter').selectOption('all');
 for(const [q,n] of [['20D',20],['120D',120],['20 D',20],['20den',20],['20 denier',20],['20D丝袜',20],['6d',6],['200D',200]]){
  await page.locator('#search').fill(q);assert.equal(await page.locator('#entry-grid .entry').count(),1,q);assert.match(await page.locator('#entry-grid .title-button').textContent(),new RegExp('^'+n+'D'));
 }
 await page.locator('#search').fill('5D');assert.equal(await page.locator('#entry-grid .entry').count(),0);
 for(const q of ['吊带袜','自持袜','硅胶袜','四带','六带','八带','连裤袜','袜裤','踩脚','网袜','五趾','二趾','袜套','leggings','hold-ups','fishnet']){await page.locator('#search').fill(q);assert.ok(await page.locator('#entry-grid .entry').count()>0,q);assert.equal(await page.locator('#entry-grid .entry').count(),await page.locator('#entry-grid .image-button').count());}
 await page.locator('#search').fill('');await page.locator('#dimension-filter').selectOption('吊带袜与自持袜结构');await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'suspender-stayup-desktop.png')});
 await page.locator('#dimension-filter').selectOption('连裤袜与打底袜裤版型');await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'tights-desktop.png')});
 await page.locator('#entry-grid [data-detail]').last().click();const heading=await page.locator('#detail-heading').textContent();await page.locator('#prev-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),heading);await page.keyboard.press('Escape');
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="clothing_new"]').click();while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),96);
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('socks');assert.equal(await page.locator('#board-list .board').count(),data.boards.filter(b=>b.items.some(x=>byId.get(x.entry_id).hosiery_reference)).length);assert.equal(await page.locator('#board-list [data-board]').first().getAttribute('data-board'),'sheet-so001-so016');
 await page.locator('#board-category').selectOption('hosiery');assert.equal(await page.locator('#board-list .board').count(),6);
 const failed=await page.evaluate(async paths=>{const bad=[];await Promise.all(paths.map(p=>new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p})));return bad},boards.map(b=>b.image));assert.deepEqual(failed,[]);
 report.checks.push('All six subgroups, hosiery overview/gallery, suspension and tights names have pictures. D queries match exact values, including spaced English and Chinese queries; 20D excludes 120D.');
 for(const [scope,n] of [['facial',492],['cosplay',368],['hair',315],['hooded_cloaks',33]]){await page.goto(url+'?section='+scope);assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+n+' '));}
 await page.goto(url+'?section=clothing');await page.locator('#style-filter').selectOption('gothic');assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+data.style_families.find(f=>f.id==='gothic').clothing_count+' '));
 await page.locator('.nav [data-view="card"]').click();await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(root,'verification-v12/roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);
 await page.setViewportSize({width:390,height:844});await page.goto(url+'?section=socks');assert.equal(await page.locator('#mobile-category').inputValue(),'socks');assert.match(await page.locator('#result-status').textContent(),/^102 /);
 await page.locator('#dimension-filter').selectOption('丝袜D数与透感参考');assert.equal(await page.locator('#entry-grid .image-button').count(),16);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'denier-mobile.png')});
 await page.locator('#mobile-category').selectOption('hosiery');await page.locator('#dimension-filter').selectOption('连裤袜与打底袜裤版型');assert.equal(await page.locator('#entry-grid .image-button').count(),16);await page.emulateMedia({colorScheme:'dark'});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'tights-dark-mobile.png')});
 report.checks.push('Legacy clothing URL, prior topic scopes, style filters and appearance-card import remain compatible; hosiery mobile category and subgroup filters work without overflow in light and dark themes.');
 assert.deepEqual(report.errors,[]);report.passed=true;await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,entries:data.entries.length}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
