const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const d=read('data/catalog.json'),n=read('data/navigation.json'),es=d.entries.filter(e=>e.outfit_combination_v63);
 assert.equal(es.length,48);assert.equal(d.meta.new_count,48);assert.equal(d.meta.missing_image_count,0);assert.equal(d.meta.seasonal_count,288);
 assert.equal(new Set(d.entries.map(e=>e.id)).size,d.entries.length);
 for(const e of es){assert(e.visual&&e.inspiration_reference,e.id);assert(fs.existsSync(path.join(root,e.visual.image)),e.id);const c=e.visual.crop;assert(c&&c.x>=0&&c.y>=0&&c.x+c.width<=1024&&c.y+c.height<=1536,e.id)}
 for(const cid of ['spring_outfits','summer_outfits','autumn_outfits','winter_outfits'])assert.equal(es.filter(e=>e.category===cid&&e.seasonal_reference).length,8);
 assert(n.documents.some(x=>x.path==='docs/costume-comparison-v63.md'));
 const doc=fs.readFileSync(path.join(root,'docs/costume-comparison-v63.md'),'utf8');assert(doc.includes('不是逐张核实'));
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage({viewport:{width:1280,height:900}}),errors=[];p.on('pageerror',e=>errors.push(e.message));const u=pathToFileURL(path.join(root,'index.html')).href;
 for(const [q,id] of [['荷叶领风衣牛仔裙','SV065'],['开衫皮短裙长筒靴','AU065'],['毛领羽绒灯芯绒','WI065'],['纱笼泳装','SW034'],['滚边长罩袍短裤睡衣','PJ034']]){
  await p.goto(u+'?section=all&q='+encodeURIComponent(q));await p.waitForSelector('#category-title');assert(await p.locator(`article.entry [data-detail="${id}"]`).count(),q);
 }
 await p.goto(u+'?section=spring_outfits&dimension='+encodeURIComponent('春季·轻叠穿与短裙补充'));await p.waitForSelector('article.entry');
 assert.equal(await p.locator('article.entry').count(),8);const bg=await p.locator('article.entry .thumb').first().evaluate(e=>getComputedStyle(e).backgroundImage);assert(bg.includes('sheet-costume-v63-spring1.png'));
 await p.locator('article.entry [data-detail="SV065"]').first().click();assert((await p.locator('#detail-dialog').innerText()).includes('参考服装库'));
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,new_outfits:48,images:12,seasonal_outfits:288,search_and_crop:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
