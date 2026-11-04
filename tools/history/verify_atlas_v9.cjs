const {chromium}=require('../qa/runtime.cjs').playwright;
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..'),partial=process.argv.includes('--partial');
const data=JSON.parse(fs.readFileSync(path.join(root,partial?'catalog-v2-preview.json':'catalog.json'),'utf8'));
const prior=JSON.parse(fs.readFileSync(path.join(root,'verification-v9/catalog-v8.json'),'utf8'));
const out=path.join(root,'verification-v9');fs.mkdirSync(out,{recursive:true});
const report={partial,checks:[],errors:[],meta:data.meta};let browser;
const checked=x=>report.checks.push(x),clothing=new Set(data.meta.clothing_categories);
const count=(style,shoulder)=>data.entries.filter(e=>clothing.has(e.category)&&(!style||e.styles.includes(style))&&(!shoulder||e.shoulder_type===shoulder)).length;
(async()=>{
 assert.equal(data.entries.length,2845);assert.equal(data.categories.length,61);assert.equal(data.meta.clothing_count,1615);assert.equal(data.meta.new_count,304);assert.equal(data.style_families.length,30);assert.equal(data.meta.shoulder_count,61);
 if(!partial){assert.equal(data.meta.illustrated_count,2845);assert.equal(data.meta.missing_image_count,0);assert.equal(data.boards.length,209);assert.equal(data.entries.filter(e=>e.added_in==='9.0').length,304);}
 assert.equal(new Set(data.entries.map(e=>e.id)).size,2845);assert.equal(new Set(data.entries.map(e=>e.name)).size,2845);
 for(const old of prior.entries){const e=data.entries.find(e=>e.id===old.id);assert.equal(e.name,old.name);assert.deepEqual(e.visual,old.visual)}
 for(const e of data.entries){if(!partial)assert.ok(e.visual);if(e.visual)assert.ok(fs.existsSync(path.join(root,e.visual.image)));e.styles.forEach(k=>assert.ok(data.style_families.some(f=>f.id===k)));e.related_reading.forEach(k=>assert.ok(data.references.some(r=>r.id===k)))}
 for(const f of data.style_families)assert.equal(f.clothing_count,count(f.id));
 if(!partial){const corrected=data.entries.filter(e=>e.visual.crop);assert.equal(corrected.length,16);for(const e of corrected){const r=e.visual.crop;assert.ok(r.x>=0&&r.y>=0&&r.width>0&&r.height>0&&r.x+r.width<=r.sheet_width&&r.y+r.height<=r.sheet_height);}}
 assert.deepEqual(data.entries.find(e=>e.name==='田园格纹洛丽塔装').styles,['lolita','cottagecore']);
 assert.ok(!data.entries.find(e=>e.name==='落肩方身毛衣').shoulder_type);assert.ok(!data.entries.find(e=>e.name==='高领无袖针织衫').shoulder_type);
 checked('2845 unique illustrated entries, 1615 clothing references, 30 cross-category styles and 61 retained shoulder references. All 2541 old IDs and image mappings remain compatible.');
 browser=await chromium.launch({...require('../qa/runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1080}});
 page.on('pageerror',e=>report.errors.push(e.message));page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const url=pathToFileURL(path.join(root,partial?'index-v2-preview.html':'index.html')).href;
 await page.goto(url+'?edition=9&section=clothing');await page.waitForFunction(()=>document.querySelectorAll('#entry-grid .entry').length===72);
 assert.match(await page.locator('#result-status').textContent(),/^1615 /);
 for(const id of ['gothic','british','lolita','punk','chinese','jirai','ryousangata']){
   await page.locator('.jump [data-style="'+id+'"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),Math.min(72,count(id)));assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+count(id)+' '));
   assert.equal(await page.locator('#style-filter').inputValue(),id);await page.screenshot({path:path.join(out,id+'-desktop.png'),fullPage:false});
 }
 checked('Each of the original style and new Chinese-style shortcuts returns its actual clothing coordinates.');
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

 const sizes={hats:56,bags:54,military_outfits:32,wizard_outfits:32,priestess_outfits:32,early20c_outfits:64,outerwear:110,special_costumes:96,hair_cut:52,hair_bangs:36,hair_tie:77,hair_surface:46,hair_details:40,hair_combinations:64,hair_accessories:64,earrings:16,pendants:16,studs:16,gloves:32,body_art:32,sleepwear:32,schoolwear:32,youthwear:64};
 for(const [cat,n] of Object.entries(sizes)){
   await page.locator('#reset-facets').click();await page.locator('#categories [data-category="'+cat+'"]').click();assert.equal(await page.locator('#entry-grid .entry').count(),Math.min(72,n));
   if(!partial)assert.equal(await page.locator('#entry-grid .image-button').count(),Math.min(72,n));
 }
 for(const [cat,word] of [['hats','棒球帽'],['hats','巫师帽'],['bags','背包'],['bags','口金'],['military_outfits','军装'],['military_outfits','作训服'],['wizard_outfits','巫师'],['wizard_outfits','女巫'],['priestess_outfits','巫女'],['priestess_outfits','千早'],['priestess_outfits','女祭司']]){
   await page.locator('#reset-facets').click();await page.locator('#categories [data-category="'+cat+'"]').click();await page.locator('#search').fill(word);assert.ok(await page.locator('#entry-grid .entry').count()>0,'Missing '+word);
 }
 checked('All five requested topics are illustrated and discoverable, including construction aliases and shrine/fantasy priestess distinctions.');
 for(const cat of ['early20c_outfits','hats','bags','military_outfits','wizard_outfits','priestess_outfits']){
  await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+cat+'"]').click();await page.screenshot({path:path.join(out,cat+'-desktop.png'),fullPage:false});
 }

 for(const family of data.style_families.filter(f=>['jirai','ryousangata','girly','french_girly','fairy_kei','decora','gyaru','hime_gyaru','visual_kei','grunge','yume_kawaii','yami_kawaii','tenshi','y2k'].includes(f.id))){
  await page.locator('#reset-facets').click();await page.locator('#style-filter').selectOption(family.id);assert.equal(await page.locator('#entry-grid .entry').count(),count(family.id));assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+count(family.id)+' '));
  assert.equal(await page.locator('#entry-grid .image-button').count(),count(family.id));
  await page.locator('#reset-facets').click();await page.locator('#search').fill(family.aliases[0]);assert.ok(await page.locator('#entry-grid .entry').count()>0,family.id+' alias');
 }
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="early20c_outfits"]').click();
 for(const decade of ['1900–1909年代欧美女装','1910–1919年代欧美女装','1920–1929年代欧美女装','1900–1920年代中国近代女装']){
  await page.locator('#dimension-filter').selectOption(decade);assert.equal(await page.locator('#entry-grid .entry').count(),16);assert.equal(await page.locator('#entry-grid .image-button').count(),16);
 }
 for(const q of ['爱德华时代','1900年代','1910年代','1920年代','文明新装','早期旗袍']){
  await page.locator('#reset-facets').click();await page.locator('.jump [data-category="early20c_outfits"]').click();await page.locator('#search').fill(q);assert.ok(await page.locator('#entry-grid .entry').count()>0,q);
 }
 checked('All 14 new styles, their common aliases, and four historical decade/region blocks return illustrated results.');

 assert.equal(data.meta.hair_count,315);assert.equal(data.meta.hooded_cloak_count,33);
 for(const [scope,n] of [['hair',315],['hooded_cloaks',33],['hair_combinations',64],['special_costumes',96]]){
  await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+scope+'"]').click();assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+n+' '));
  while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .image-button').count(),n);
  await page.screenshot({path:path.join(out,scope+'-desktop.png'),fullPage:false});
 }
 for(const [scope,words] of [['hooded_cloaks',['圆兜','尖兜','拉链','hooded cloak']],['special_costumes',['狐耳','南瓜','假面','人偶','云朵']],['hair',['V形缺口','刘海','loc','扎发','完整发型','鱼骨']]]){
  for(const word of words){await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+scope+'"]').click();await page.locator('#search').fill(word);assert.ok(await page.locator('#entry-grid .entry').count()>0,scope+' '+word);}
 }
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="special_costumes"]').click();
 for(const dim of ['兽耳兽角与动物拟态装扮','节庆童话与假面主题','非人幻想主题服装','机关道具与拟物装扮']){await page.locator('#dimension-filter').selectOption(dim);assert.equal(await page.locator('#entry-grid .image-button').count(),16);}
 checked('315 hair references, 64 complete hairstyles, 96 special costumes and 33 hooded cloaks are illustrated and searchable through dedicated scopes.');

 for(const [cat,n] of Object.entries({hair_accessories:64,earrings:16,pendants:16,studs:16,gloves:32,body_art:32,sleepwear:32,schoolwear:32,youthwear:64})){
  await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+cat+'"]').click();assert.equal(await page.locator('#entry-grid .image-button').count(),n);assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+n+' '));
  await page.screenshot({path:path.join(out,cat+'-desktop.png'),fullPage:false});
 }
 for(const [cat,words] of [['hair_accessories',['发箍','发卡','发簪','发圈']],['earrings',['耳夹','圈耳环']],['pendants',['吊坠','项链']],['studs',['耳钉','鼻钉','眉饰']],['gloves',['露指','连指','手套']],['body_art',['脸部彩绘','纹身','脸部纹身']],['sleepwear',['睡衣','睡裙','睡袍']],['schoolwear',['校服','水手领','运动']],['youthwear',['青少年','青春期','teen outfit']]]){
  for(const word of words){await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+cat+'"]').click();await page.locator('#search').fill(word);assert.ok(await page.locator('#entry-grid .entry').count()>0,cat+' '+word);}
 }
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="all"]').click();await page.locator('#search').fill('青春期');
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();assert.equal(await page.locator('#entry-grid .entry').count(),64);
 const ids=await page.locator('#entry-grid .meta>span:first-child').allTextContents();assert.ok(ids.every(x=>x.startsWith('YO')));
 for(const e of data.entries.filter(e=>['schoolwear','youthwear'].includes(e.category)))assert.equal(e.age_context,'13–17岁服装设计参考');
 for(const e of data.entries.filter(e=>['body_art','studs'].includes(e.category)))assert.equal(e.age_context,'成年角色装饰参考');
 checked('All nine requested categories have images and useful aliases; adolescent apparel queries remain scoped to everyday clothing.');

 for(const [cat,word,n] of [['earrings','耳夹',3],['studs','耳钉',11],['body_art','脸部彩绘',16],['body_art','纹身',16],['body_art','脸部纹身',4],['sleepwear','睡袍',6]]){
  await page.locator('#reset-facets').click();await page.locator('.jump [data-category="'+cat+'"]').click();await page.locator('#search').fill(word);assert.equal(await page.locator('#entry-grid .entry').count(),n,cat+' '+word);
 }
 checked('Specific earring, stud, face-paint, tattoo and robe searches avoid broad category-name false matches.');
 await page.locator('#reset-facets').click();await page.locator('.jump [data-category="clothing_new"]').click();assert.match(await page.locator('#result-status').textContent(),/^304 /);
 while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();if(!partial)assert.equal(await page.locator('#entry-grid .image-button').count(),304);
 await page.locator('#entry-grid [data-detail]').first().click();const first=await page.locator('#detail-heading').textContent();await page.locator('#next-detail').click();assert.notEqual(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('ArrowLeft');assert.equal(await page.locator('#detail-heading').textContent(),first);await page.keyboard.press('Escape');
 await page.locator('.jump [data-category="all"]').click();while(await page.locator('#more-wrap').isVisible())await page.locator('#load-more').click();if(!partial)assert.equal(await page.locator('#entry-grid .image-button').count(),2845);checked(partial?'All new and original term cards render; final illustration completion is checked after image generation.':'All new and original cards render with images and detail navigation.');
 await page.locator('.nav [data-view="boards"]').click();await page.locator('#board-category').selectOption('tops');assert.equal(await page.locator('#board-list .board').count(),data.boards.filter(b=>b.items.some(x=>data.entries.find(e=>e.id===x.entry_id).category==='tops')).length);checked('The sheet gallery retains ordinary clothing categories.');
 await page.locator('.nav [data-view="combinations"]').click();await page.locator('[data-combo="0"]').click();await page.locator('.nav [data-view="card"]').click();assert.equal(await page.locator('#selected-grid .entry').count(),6);
 const wait=page.waitForEvent('download');await page.locator('#export-card').click();const dl=await wait;await dl.saveAs(path.join(out,'roundtrip.json'));await page.locator('#clear-card').click();await page.locator('#import-file').setInputFiles(path.join(out,'roundtrip.json'));await page.waitForFunction(()=>document.querySelectorAll('#selected-grid .entry').length===6);checked('Appearance-card export/import and existing combinations still work.');
 const failed=await page.evaluate(async paths=>{const bad=[];for(const p of paths)await new Promise(resolve=>{const i=new Image();i.onload=resolve;i.onerror=()=>{bad.push(p);resolve()};i.src=p});return bad},[...new Set(data.boards.map(b=>b.image).concat(data.references.filter(r=>r.image).map(r=>r.image)))]);assert.deepEqual(failed,[]);checked('All '+data.boards.length+' contact sheets and six museum photographs load.');
 await page.goto(url+'?section=clothing&style=jirai');await page.emulateMedia({colorScheme:'dark'});await page.screenshot({path:path.join(out,'jirai-dark.png'),fullPage:false});await page.emulateMedia({colorScheme:'light'});await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(out,'jirai-mobile.png'),fullPage:false});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.locator('#mobile-category').selectOption('onepiece');await page.locator('#search').fill('露肩');assert.ok(await page.locator('#entry-grid .entry').count()>0);assert.equal(await page.locator('#shoulder-filter,[data-category="shoulders"]').count(),0);await page.screenshot({path:path.join(out,'clothing-mobile.png'),fullPage:false});await page.goto(url+'?section=shoulders');assert.match(await page.locator('#result-status').textContent(),/^1615 /);checked('Style deep links and legacy links, mobile categories and dark/mobile layouts work without overflow.');

 for(const [scope,n] of [['hair',315],['hooded_cloaks',33],['hair_combinations',64]]){
  await page.goto(url+'?section='+scope);assert.match(await page.locator('#result-status').textContent(),new RegExp('^'+n+' '));
  assert.equal(await page.locator('#mobile-category').inputValue(),scope);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 }
 await page.screenshot({path:path.join(out,'hair-combinations-mobile.png'),fullPage:false});
 await page.locator('.nav [data-view="boards"]').click();
 for(const scope of ['hair','hooded_cloaks']){
  await page.locator('#board-category').selectOption(scope);const expected=data.boards.filter(b=>b.items.some(x=>{const e=data.entries.find(e=>e.id===x.entry_id);return scope==='hair'?e.category.startsWith('hair_')&&e.category!=='hair_accessories':e.hooded_cloak})).length;
  assert.equal(await page.locator('#board-list .board').count(),expected);
 }
 checked('New scope deep links, mobile category selection and hair/cloak sheet-gallery filters work.');

 await page.goto(url+'?section=youthwear');assert.match(await page.locator('#result-status').textContent(),/^64 /);assert.equal(await page.locator('#mobile-category').inputValue(),'youthwear');
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);await page.screenshot({path:path.join(out,'youthwear-mobile.png'),fullPage:false});
 await page.locator('#mobile-category').selectOption('hair_accessories');await page.locator('#dimension-filter').selectOption('发簪发钗与梳饰细分');assert.equal(await page.locator('#entry-grid .image-button').count(),16);
 checked('New apparel deep links and mobile ornament subcategory filters work.');
 assert.deepEqual(report.errors,[]);checked('No script or image-resource errors.');report.passed=true;await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:report.checks,meta:data.meta}));
})().catch(async e=>{report.passed=false;report.failure=e.stack;if(browser)await browser.close();fs.writeFileSync(path.join(out,partial?'preview-report.json':'report.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exitCode=1});
