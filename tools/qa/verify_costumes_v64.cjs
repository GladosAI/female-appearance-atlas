const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const data=read('data/catalog.json'),nav=read('data/navigation.json');
 const outfits=data.entries.filter(e=>e.outfit_combination_v64);
 assert.equal(outfits.length,14);assert.equal(data.meta.new_count,14);assert.equal(data.meta.missing_image_count,0);
 assert.equal(data.meta.seasonal_count,297);assert.equal(new Set(data.entries.map(e=>e.id)).size,data.entries.length);
 assert.equal(data.entries.filter(e=>e.outfit_combination_v63).length,48);
 for(const e of outfits){
  assert(e.inspiration_reference&&e.visual&&e.visual.crop,e.id);
  assert(fs.existsSync(path.join(root,e.visual.image)),e.id);
  const c=e.visual.crop;assert(c.x>=0&&c.y>=0&&c.x+c.width<=1024&&c.y+c.height<=1536,e.id);
 }
 assert.deepEqual(['spring_outfits','summer_outfits','autumn_outfits','winter_outfits','swimwear','sleepwear','fashion_outfits'].map(cid=>outfits.filter(e=>e.category===cid).length),[2,3,3,1,2,1,2]);
 assert(nav.documents.some(x=>x.path==='docs/costume-comparison-v64.md'));
 assert(fs.readFileSync(path.join(root,'docs/costume-comparison-v64.md'),'utf8').includes('未检查或复刻参考图片'));
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage({viewport:{width:1280,height:900}}),errors=[];p.on('pageerror',e=>errors.push(e.message));
 const url=pathToFileURL(path.join(root,'index.html')).href;
 for(const name of ['雪纺蝴蝶结上衣中裙装','灰衬衫牛仔长裙凉鞋装','蕾丝衬衣灯芯绒长裤装','丝绒吊带毛绒大衣长裤装','碎花长裤开衫凉鞋度假装','荷叶吊带蕾丝短裤睡衣','束腰短裙蕾丝短袜发箍装']){
   const e=outfits.find(x=>x.name===name);assert(e,name);
   await p.goto(url+'?section=all&q='+encodeURIComponent(name));await p.waitForSelector('#category-title');
   assert(await p.locator(`article.entry [data-detail="${e.id}"]`).count(),name);
 }
 await p.goto(url+'?section=summer_outfits&dimension='+encodeURIComponent('夏季·牛仔与清凉叠穿'));
 await p.waitForSelector('article.entry');assert.equal(await p.locator('article.entry').count(),3);
 const bg=await p.locator('article.entry .thumb').first().evaluate(e=>getComputedStyle(e).backgroundImage);assert(bg.includes('sheet-costume-v64-summer.png'));
 await p.screenshot({path:path.join(root,'.work','costume-v64-browser.png'),fullPage:false});
 await p.locator('article.entry [data-detail]').first().click();assert((await p.locator('#detail-dialog').innerText()).includes('未核实参考图片'));
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,new_outfits:14,sheets:7,seasonal:data.meta.seasonal_count}));
})().catch(e=>{console.error(e);process.exitCode=1});
