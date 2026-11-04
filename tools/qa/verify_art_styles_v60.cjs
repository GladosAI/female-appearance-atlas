const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..');const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const d=read('data/catalog.json'),nav=read('data/navigation.json');const es=d.entries.filter(e=>e.art_style_reference);
 assert.equal(es.length,64);assert.equal(d.meta.new_count,16);assert.equal(nav.groups.find(g=>g.id==='art_styles').count,64);
 assert.equal(new Set(d.entries.map(e=>e.id)).size,d.entries.length);
 for(const e of es){assert(e.visual&&e.fullbody_visual,e.id);for(const v of [e.visual,e.fullbody_visual])assert(fs.existsSync(path.join(root,v.image)),e.id);}
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));const u=pathToFileURL(path.join(root,'index.html')).href;
 for(const [q,id] of [['少女漫画','XA007'],['工笔','XD005'],['浮世绘','XD006'],['体素','XB008'],['彩绘玻璃','XE006'],['红外伪彩','XC010'],['2.5D 游戏原画立绘','XB005'],['20D','SO006']]){
  await p.goto(u+'?section=all&q='+encodeURIComponent(q));await p.waitForSelector('#category-title');
  assert(await p.locator(`article.entry [data-detail="${id}"]`).count(),q);
 }
 await p.goto(u+'?section=art_traditional');await p.waitForSelector('article.entry');
 assert.equal(await p.locator('[data-art-visual-mode=fullbody]').getAttribute('aria-pressed'),'true');
 const target=p.locator('article.entry [data-detail="XD005"]').first();await target.click();
 assert((await p.locator('#detail-dialog').innerText()).includes('全身参考'));
 assert((await p.locator('#detail-dialog').innerText()).includes('人像近景'));
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,styles:es.length,new_styles:16,paired_views:64,search_and_detail:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
