const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..');const data=JSON.parse(fs.readFileSync(path.join(root,'data/catalog.json'),'utf8'));
const cases=[['写实人像写真','XC001'],['日韩杂志画报','XC005'],['复古胶片写真','XC006'],['2.5D 游戏原画立绘','XB005'],['日系二次元插画','XA005'],['新海诚感动画电影','XA006'],['日式黑白漫画网点','XF002'],['3D 次世代角色渲染','XJ005'],['3D 潮玩手办质感','XJ006'],['赛博朋克霓虹','XK003'],['角色设定集立绘（纯白底）','XB006']];
(async()=>{
 assert.equal(data.entries.filter(e=>e.art_style_reference).length,48);assert.equal(data.meta.new_count,8);
 const ids=new Set(data.entries.map(e=>e.id));assert.equal(ids.size,data.entries.length);
 for(const [term,id] of cases){const e=data.entries.find(e=>e.id===id);assert(e?.art_style_reference,term);for(const field of ['visual','fullbody_visual']){assert(e[field],id+' '+field);assert(fs.existsSync(path.join(root,e[field].image)),id)}}
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));const url=pathToFileURL(path.join(root,'index.html')).href;
 for(const [term,id] of cases){
  await page.goto(url+'?section=all&q='+encodeURIComponent(term));await page.waitForSelector('#category-title');
  assert(await page.locator(`article.entry [data-detail="${id}"]`).count(),term+' '+id);
 }
 await page.goto(url+'?section=all&q=20D');await page.waitForSelector('#category-title');
 assert(await page.locator('article.entry [data-detail="SO006"]').count(),'20D denier search');
 await page.goto(url+'?section=art_game');await page.waitForSelector('article.entry');
 await page.locator('[data-art-visual-mode=portrait]').click();
 await page.locator('article.entry [data-detail="XB006"]').first().click();
 assert((await page.locator('#detail-dialog').innerText()).includes('全身参考'));
 assert((await page.locator('#detail-dialog').innerText()).includes('人像近景'));
 assert.deepEqual(errors,[]);await browser.close();console.log(JSON.stringify({passed:true,requested_searches:cases.length,new_styles:8,each_with_full_body_and_portrait:true}));
})().catch(e=>{console.error(e);process.exitCode=1});
