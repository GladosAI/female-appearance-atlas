const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const data=read('data/catalog.json'),nav=read('data/navigation.json'),entries=data.entries.filter(e=>e.art_style_reference);
 assert.equal(entries.length,40);assert.equal(data.meta.new_count,16);assert.equal(data.meta.missing_image_count,0);
 assert.equal(new Set(data.entries.map(e=>e.id)).size,data.entries.length);
 assert.equal(nav.groups.find(g=>g.id==='art_styles').count,40);
 for(const e of entries){
  assert(e.visual&&e.fullbody_visual,e.id);assert(fs.existsSync(path.join(root,e.visual.image)),e.id);assert(fs.existsSync(path.join(root,e.fullbody_visual.image)),e.id);
  const r=e.fullbody_visual.crop;assert.equal(r.sheet_width,1024);assert.equal(r.sheet_height,1536);assert.equal(r.width,512);assert(r.height>700&&r.height<840);
 }
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1280,height:900}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 const url=pathToFileURL(path.join(root,'index.html')).href;
 await page.goto(url+'?section=topic_art_styles');await page.waitForSelector('article.entry');
 assert.equal(await page.locator('article.entry').count(),40);
 assert.equal(await page.locator('[data-art-visual-mode=fullbody]').getAttribute('aria-pressed'),'true');
 let bg=await page.locator('article.entry .thumb').first().evaluate(e=>getComputedStyle(e).backgroundImage);assert(bg.includes('fullbody'));
 await page.locator('[data-art-visual-mode=portrait]').click();
 bg=await page.locator('article.entry .thumb').first().evaluate(e=>getComputedStyle(e).backgroundImage);assert(!bg.includes('fullbody'));
 await page.locator('article.entry [data-detail]').first().click();
 assert.equal(await page.locator('#detail-dialog figcaption').count(),2);
 assert((await page.locator('#detail-dialog').innerText()).includes('全身参考'));
 assert((await page.locator('#detail-dialog').innerText()).includes('人像近景'));
 await page.goto(url+'?section=all&q='+encodeURIComponent('马克笔'));await page.waitForSelector('article.entry');
 assert((await page.locator('body').innerText()).includes('马克笔时装插画'));
 await page.goto(url+'?section=hair_accessories');await page.waitForSelector('article.entry');
 assert(await page.locator('[data-visual-mode=wearing]').isVisible());
 assert.deepEqual(errors,[]);await browser.close();
 console.log(JSON.stringify({passed:true,styles:40,new_styles:16,paired_views:40,browser_switch:'passed',search:'passed',accessory_controls:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
