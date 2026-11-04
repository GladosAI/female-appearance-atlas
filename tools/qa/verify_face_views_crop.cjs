// Verify the nonuniform source-grid bounds and the browser's rendered card crops.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require('./runtime.cjs').playwright;
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
(async()=>{
 const data=read('data/catalog.json'),before=read('.work/verification/face-views-crop/catalog-before.json');
 const expectedX=[0,314,613,911,1224],expectedY=[0,311,629,937,1285];
 const board=data.boards.find(b=>b.id==='sheet-va001-va016');
 assert.deepEqual(board.column_boundaries,expectedX);assert.deepEqual(board.row_boundaries,expectedY);
 const list=data.entries.filter(e=>e.category==='face_views');assert.equal(list.length,16);
 for(let i=0;i<16;i++){
  const e=list[i],col=i%4,row=Math.floor(i/4),r=e.visual.crop;
  assert.equal(e.id,'VA'+String(i+1).padStart(3,'0'));
  assert.deepEqual(r,{x:expectedX[col],y:expectedY[row],width:expectedX[col+1]-expectedX[col],height:expectedY[row+1]-expectedY[row],sheet_width:1224,sheet_height:1285});
 }
 const prior=new Map(before.entries.map(e=>[e.id,e]));
 for(const e of data.entries)if(e.category!=='face_views')assert.deepEqual(e,prior.get(e.id),e.id+' unexpectedly changed');
 const browser=await chromium.launch({...require('./runtime.cjs').browserOptions,headless:true});
 const page=await browser.newPage({viewport:{width:1508,height:900}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.join(root,'index.html')).href+'?section=face_views');await page.waitForSelector('article.entry');
 assert.equal(await page.locator('article.entry').count(),16);
 const thumbs=await page.locator('article.entry .thumb').evaluateAll(nodes=>nodes.map(n=>({background:getComputedStyle(n).backgroundImage,position:getComputedStyle(n).backgroundPosition,size:getComputedStyle(n).backgroundSize})));
 assert.equal(thumbs.length,16);assert(thumbs.every(t=>t.background.includes('sheet-va001-va016.png')));
 assert.notEqual(thumbs[8].position,thumbs[12].position);
 await page.locator('article.entry [data-detail="VA009"]').first().click();
 assert((await page.locator('#detail-dialog').innerText()).includes('正面轻俯视'));
 assert.deepEqual(errors,[]);await browser.close();
 console.log(JSON.stringify({passed:true,corrected_cards:16,previous_other_entries_preserved:true,browser:'passed'}));
})().catch(e=>{console.error(e);process.exitCode=1});
