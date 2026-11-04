const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const d=read('data/catalog.json'),nav=read('data/navigation.json');const es=d.entries.filter(e=>e.art_style_reference);
 assert.equal(es.length,80);assert.equal(d.meta.new_count,16);assert.equal(nav.groups.find(g=>g.id==='art_styles').count,80);
 assert.equal(new Set(d.entries.map(e=>e.id)).size,d.entries.length);
 for(const e of es){assert(e.visual&&e.fullbody_visual,e.id);for(const v of [e.visual,e.fullbody_visual])assert(fs.existsSync(path.join(root,v.image)),e.id)}
 const pixels=es.filter(e=>e.pixel_density_reference);assert.equal(pixels.length,4);assert(pixels.every(e=>e.description.includes('并非对应尺寸')));
 const b=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));const u=pathToFileURL(path.join(root,'index.html')).href;
 for(const [q,id] of [['16x16','XB009'],['32x32','XB010'],['64x64','XB011'],['128x128','XB012'],['球体关节','XJ008'],['波普艺术','XE007'],['2.5D 游戏原画立绘','XB005'],['20D','SO006']]){
  await p.goto(u+'?section=all&q='+encodeURIComponent(q));await p.waitForSelector('#category-title');assert(await p.locator(`article.entry [data-detail="${id}"]`).count(),q);
 }
 await p.goto(u+'?section=art_game&dimension='+encodeURIComponent('像素尺寸对照'));await p.waitForSelector('article.entry');
 assert.equal(await p.locator('article.entry').count(),4);assert((await p.locator('body').innerText()).includes('并非对应尺寸'));
 await p.locator('[data-art-visual-mode=portrait]').click();
 await p.locator('article.entry [data-detail="XB009"]').first().click();
 const text=await p.locator('#detail-dialog').innerText();assert(text.includes('全身参考'));assert(text.includes('人像近景'));assert(text.includes('并非对应尺寸'));
 assert.deepEqual(errors,[]);await b.close();console.log(JSON.stringify({passed:true,styles:es.length,new_styles:16,pixel_levels:4,search_and_detail:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
