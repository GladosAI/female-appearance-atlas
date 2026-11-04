const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const data=read('data/catalog.json'),nav=read('data/navigation.json'),before=read('.work/hair-v65-before-ids.json');
 const es=data.entries.filter(e=>e.hair_comparison_v65);assert.equal(es.length,24);assert.equal(data.meta.new_count,24);
 assert.equal(data.meta.hair_count,531);assert.equal(data.meta.missing_image_count,0);
 assert.equal(new Set(data.entries.map(e=>e.id)).size,data.entries.length);
 const byId=new Map(data.entries.map(e=>[e.id,e]));for(const [id,name] of Object.entries(before))assert.equal(byId.get(id)?.name,name,id);
 for(const e of es){
  assert.equal(e.category,'hair_combinations');assert(e.inspiration_reference&&e.visual?.crop,e.id);
  assert(fs.existsSync(path.join(root,e.visual.image)),e.id);
  const c=e.visual.crop;assert(c.x>=0&&c.y>=0&&c.x+c.width<=c.sheet_width&&c.y+c.height<=c.sheet_height,e.id);
 }
 assert(nav.documents.some(d=>d.path==='docs/hair-comparison-v65.md'));
 const doc=fs.readFileSync(path.join(root,'docs/hair-comparison-v65.md'),'utf8');
 assert(doc.includes('1,499')&&doc.includes('755')&&doc.includes('没有查看参考项目的图片'));
 for(const id of ['HN079','HN080','HC004','HS067'])assert(byId.has(id),id);
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage({viewport:{width:1280,height:900}}),errors=[];p.on('pageerror',e=>errors.push(e.message));
 const url=pathToFileURL(path.join(root,'index.html')).href;
 for(const [q,name] of [['Hush Cut','韩式轻羽剪中发'],['蝴蝶剪','外翻脸侧蝴蝶层次剪'],['tassel bob','八字侧刘海流苏波波'],['迷你狼尾','短碎层迷你狼尾发'],['手刷染','厚层次中发渐层手刷染']]){
  const e=es.find(x=>x.name===name);await p.goto(url+'?section=all&q='+encodeURIComponent(q));await p.waitForSelector('#category-title');
  assert(await p.locator(`article.entry [data-detail="${e.id}"]`).count(),q);
 }
 await p.goto(url+'?section=hair_combinations&dimension='+encodeURIComponent('中发·刘海与轻层次'));
 await p.waitForSelector('article.entry');assert.equal(await p.locator('article.entry').count(),4);
 assert((await p.locator('article.entry .thumb').first().evaluate(e=>getComputedStyle(e).backgroundImage)).includes('sheet-hair-v65-medium1.png'));
 await p.screenshot({path:path.join(root,'.work','hair-v65-browser.png'),fullPage:false});
 await p.locator('article.entry [data-detail]').first().click();assert((await p.locator('#detail-dialog').innerText()).includes('未核实参考图片'));
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,new_hairstyles:24,sheets:6,unchanged_ids:Object.keys(before).length}));
})().catch(e=>{console.error(e);process.exitCode=1});
