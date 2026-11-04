const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const d=read('data/catalog.json'),nav=read('data/navigation.json');const es=d.entries.filter(e=>e.art_style_reference);
 assert.equal(es.length,96);assert.equal(d.meta.new_count,16);assert.equal(nav.groups.find(g=>g.id==='art_styles').count,96);
 assert.equal(new Set(d.entries.map(e=>e.id)).size,d.entries.length);
 for(const e of es){assert(e.visual&&e.fullbody_visual,e.id);for(const v of [e.visual,e.fullbody_visual])assert(fs.existsSync(path.join(root,v.image)),e.id)}
 const proportions=es.filter(e=>e.head_proportion_reference);assert.equal(proportions.length,4);
 assert(proportions.every(e=>e.dimension==='头身比画风'&&e.design_tip.includes('近似')));
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));const u=pathToFileURL(path.join(root,'index.html')).href;
 for(const [q,id] of [['平涂漫画','XG005'],['韩式幻想厚涂','XK007'],['暗黑哥特手绘','XK008'],['2.5D水彩','XB013'],['三头身','XA013'],['128x128','XB012'],['20D','SO006']]){
  await p.goto(u+'?section=all&q='+encodeURIComponent(q));await p.waitForSelector('#category-title');assert(await p.locator(`article.entry [data-detail="${id}"]`).count(),q);
 }
 await p.goto(u+'?section=art_animation&dimension='+encodeURIComponent('头身比画风'));await p.waitForSelector('article.entry');
 assert.equal(await p.locator('article.entry').count(),4);
 await p.locator('article.entry [data-detail="XA012"]').first().click();
 let text=await p.locator('#detail-dialog').innerText();assert(text.includes('全身参考'));assert(text.includes('人像近景'));assert(text.includes('不是人体发育或年龄标准'));
 await p.locator('#detail-dialog button[data-board="art-v62-4-fullbody"]').click();
 text=await p.locator('#detail-dialog').innerText();assert(text.includes('成年角色头身比对照'));assert.equal(await p.locator('#detail-dialog .caption-list button').count(),4);
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,styles:96,new_styles:16,head_proportions:4,search_and_comparison:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
