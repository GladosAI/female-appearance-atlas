const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium}=require('../qa/runtime.cjs').playwright;
const root=path.resolve(__dirname,'..'),out=path.join(root,'verification-v16');
const data=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(out,'catalog-v15.json'),'utf8'));
const report={checks:[],errors:[],meta:data.meta};let browser;
(async()=>{
 for(const [key,n] of Object.entries({entry_count:3981,category_count:88,board_count:280,clothing_count:1775,new_count:128,anthro_count:144,facial_count:588,hosiery_count:102,cosplay_count:368,hair_count:315,reference_count:78,missing_image_count:0,illustrated_count:3981}))assert.equal(data.meta[key],n,key);
 assert.equal(data.meta.version,'16.0');assert.equal(data.entries.length,3981);assert.equal(data.categories.length,88);assert.equal(data.boards.length,280);
 const byId=new Map(data.entries.map(e=>[e.id,e]));assert.equal(byId.size,3981);assert.equal(new Set(data.entries.map(e=>e.name)).size,3981);
 for(const old of prior.entries){const e=byId.get(old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual);assert.equal(e.added_in,old.added_in);assert.deepEqual(e.keywords,old.keywords);}
 assert.deepEqual(data.references.slice(0,prior.references.length),prior.references);assert.deepEqual(data.combinations,prior.combinations);assert.deepEqual(data.style_families,prior.style_families);
 const additions=data.entries.filter(e=>e.added_in==='16.0');assert.equal(additions.length,128);
 for(const cat of data.meta.anthro_categories)assert.equal(additions.filter(e=>e.category===cat).length,32);
 assert.equal(data.meta.anthro_levels.length,8);for(let n=1;n<=8;n++)assert.equal(additions.filter(e=>e.anthro_level===n).length,4);
 for(const e of additions){assert.equal(e.age_context,'成年女性幻想角色参考');assert.equal(e.anthro_reference,true);assert.ok(e.keywords.includes('福瑞'));assert.ok(e.visual.crop);const c=e.visual.crop;assert.ok(c.x>=0&&c.y>=0&&c.x+c.width<=c.sheet_width&&c.y+c.height<=c.sheet_height);}
 assert.equal(data.entries.filter(e=>e.anthro_reference&&e.added_in!=='16.0').length,16);
 assert.ok(data.entries.filter(e=>e.category==='cosplay_headgear'||e.category==='special_costumes').every(e=>!e.anthro_reference));
 for(const e of data.entries)assert.ok(fs.existsSync(path.join(root,e.visual.image)));
 const newIds=new Set(additions.map(e=>e.id)),boards=data.boards.filter(b=>b.items.some(x=>newIds.has(x.entry_id)));assert.equal(boards.length,8);
 for(const b of boards){assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.items.length,16);const png=fs.readFileSync(path.join(root,b.image));assert.equal(png.readUInt32BE(16),b.width);assert.equal(png.readUInt32BE(20),b.height);assert.equal(b.column_boundaries.length,5);assert.equal(b.row_boundaries.length,5);for(const x of b.items)assert.equal(x.name,byId.get(x.entry_id).name);}
 report.checks.push('All 3853 prior IDs, names, crops, keywords and edition labels are preserved. All 128 additions have reviewed images and individual display crops. Four categories contain 32 entries each; eight tiers contain four species each.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,'index.html')).href;
 await page.goto(url+'?edition=3&section=clothing');assert.match(await page.locator('#result-status').textContent(),/^1775 /);assert.match(await page.locator('.edition').textContent(),/16$/);
 await page.locator('.jump [data-category="clothing_new"]').click();assert.match(await page.locator('#result-status').textContent(),/^128 /);assert.equal(await page.locator('#entry-grid .image-button').count(),72);await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),128);
 await page.goto(url+'?section=anthro');assert.match(await page.locator('#result-status').textContent(),/^144 /);assert.match(await page.locator('#entry-grid .meta>span:first-child').first().textContent(),/^BL001/);
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),144);
 await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'anthro-desktop.png')});
 for(const q of ['福瑞','furry','kemono']){await page.locator('#search').fill(q);assert.match(await page.locator('#result-status').textContent(),/^128 /,q);}
 await page.goto(url+'?section=anthro_levels');for(let n=1;n<=8;n++){await page.locator('#search').fill('L'+n);assert.equal(await page.locator('#entry-grid .image-button').count(),4);const ids=await page.locator('#entry-grid .meta>span:first-child').allTextContents();assert.ok(ids.every(t=>byId.get(t.split(' ')[0]).anthro_level===n));}
 await page.locator('#search').fill('');await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'levels-desktop.png')});
 for(const cat of data.meta.anthro_categories){await page.goto(url+'?section='+cat);assert.equal(await page.locator('#entry-grid .image-button').count(),32);const dims=[...new Set(additions.filter(e=>e.category===cat).map(e=>e.dimension))];assert.equal(dims.length,2);for(const dim of dims){await page.locator('#dimension-filter').selectOption(dim);assert.equal(await page.locator('#entry-grid .image-button').count(),16);}await page.locator('#entry-grid [data-detail]').last().click();const title=await page.locator('#detail-heading').textContent();await page.locator('#prev-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),title);await page.keyboard.press('Escape');}
 await page.goto(url+'?section=anthro');await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('anthro');assert.equal(await page.locator('#board-list .board').count(),10);for(const b of boards)assert.equal(await page.locator('[data-board="'+b.id+'"]').count(),1);
 assert.equal(await page.locator('#board-list [data-board]').first().getAttribute('data-board'),'sheet-bl001-bl016');
 const failed=await page.evaluate(async paths=>{const bad=[];await Promise.all(paths.map(p=>new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p})));return bad},boards.map(b=>b.image));assert.deepEqual(failed,[]);
 report.checks.push('The 144-entry anthro overview, latest additions, L1–L8 searches, Chinese/English aliases, all eight subgroups, detail navigation and ten-board gallery render correctly. All eight new PNGs load.');
 await page.goto(url+'?section=facial');assert.match(await page.locator('#result-status').textContent(),/^588 /);
 await page.goto(url+'?section=socks');assert.match(await page.locator('#result-status').textContent(),/^102 /);await page.locator('#search').fill('20D');assert.equal(await page.locator('#entry-grid .image-button').count(),1);assert.match(await page.locator('#entry-grid .title-button').textContent(),/^20D/);
 await page.goto(url+'?section=cosplay');assert.match(await page.locator('#result-status').textContent(),/^368 /);await page.locator('.nav [data-view="card"]').click();await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(root,'verification-v12/roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);
 await page.setViewportSize({width:390,height:844});await page.goto(url+'?section=anthro');assert.equal(await page.locator('#mobile-category').inputValue(),'anthro');assert.match(await page.locator('#result-status').textContent(),/^144 /);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'anthro-mobile.png')});
 await page.locator('#mobile-category').selectOption('anthro_species');assert.match(await page.locator('#result-status').textContent(),/^32 /);await page.locator('#dimension-filter').selectOption('鳞羽水生昆虫与幻想拟人拓展');assert.equal(await page.locator('#entry-grid .image-button').count(),16);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.locator('#category-title').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'species-mobile.png')});await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'species-dark-mobile.png')});
 report.checks.push('Legacy clothing URL, face/hosiery/cosplay scopes, exact 20D search and old appearance-card import work. Anthro mobile categories, subgroups and dark mode have no horizontal overflow.');
 assert.deepEqual(report.errors,[]);report.passed=true;await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,entries:data.entries.length}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
