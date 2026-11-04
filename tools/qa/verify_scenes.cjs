// Exercise scene discovery and name-only prompt export without requiring release image packs.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {launchBrowser}=require('./runtime.cjs');
const root=path.resolve(__dirname,'../..'),base=process.env.ATLAS_TEST_URL||pathToFileURL(path.join(root,'index.html')).href;
const data=JSON.parse(fs.readFileSync(path.join(root,'data/catalog.json'),'utf8'));
(async()=>{const scenes=data.entries.filter(e=>e.scene_reference);assert(scenes.length>=60);
 const categories=[...new Set(scenes.map(e=>e.category))];
 const browser=await launchBrowser();try{
 const page=await browser.newPage({viewport:{width:1280,height:900}}),errors=[];page.on('pageerror',error=>errors.push(error.message));
 await page.goto(base+'?section=branch_scene_character_design');
 await page.locator('#entry-grid .entry').first().waitFor();
 assert.equal(await page.locator('#category-title').innerText(),'场景与人物活动');
 for(const term of ['厨房','医院','沙滩','学校','邮局','博物馆']){
  await page.goto(base+'?section=branch_scene_character_design&q='+encodeURIComponent(term));
  await page.locator('#entry-grid .entry').first().waitFor();
  const found=await page.locator('#entry-grid [data-detail]').evaluateAll(elements=>elements.map(e=>e.dataset.detail));
  assert(found.some(id=>scenes.some(scene=>scene.id===id&&scene.name.includes(term))),term+' scene search');
  if(term==='学校')for(const scene of scenes.filter(e=>e.category==='scene_campus'))assert(found.includes(scene.id),scene.id+' must be discoverable as a school scene');
 }
 const scene=scenes[0],second=scenes.find(e=>e.category!==scene.category);
 await page.goto(base+'?section='+scene.category+'&entry='+scene.id);await page.locator('#detail-dialog').waitFor({state:'visible'});
 await page.locator('#detail-dialog [data-entry-feedback]').waitFor();
 assert((await page.locator('#detail-content').innerText()).includes('场景与人物要点'));
 assert.equal(await page.locator('#detail-dialog .sequence-note').count(),0);await page.locator('#close-dialog').click();
 await page.goto(base+'?view=card');
 await page.locator('#import-file').setInputFiles({name:'scenes.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify({schema:'female-appearance-card/v1',name:'场景备选检查',selected:['AH020',scene.id,second.id]}))});
 assert.equal(await page.locator('#selected-grid > .entry').count(),3);
 await page.locator('#open-card-synthesis').click();const prompt=await page.locator('#synthesis-prompt').inputValue();
 assert(prompt.includes('发型：'));assert(prompt.includes('场景与人物活动：'));
 assert(prompt.includes(scene.name+'（'+scene.en+'）；'));assert(prompt.includes(second.name+'（'+second.en+'）；'));
 assert(!prompt.includes(scene.description));assert(!prompt.includes(scene.design_tip));assert(!prompt.includes('配饰与道具：'));assert(!prompt.includes('画风：'));
 await page.setViewportSize({width:390,height:844});assert(await page.locator('#card-synthesis-dialog').evaluate(e=>e.scrollWidth<=e.clientWidth+1));
 await page.locator('#synthesis-select-none').click();assert.equal(await page.locator('#synthesis-prompt').inputValue(),'');
 await page.locator('#synthesis-select-all').click();assert.equal(await page.locator('#synthesis-prompt').inputValue(),prompt);
 assert.deepEqual(errors,[]);console.log(JSON.stringify({passed:true,scene_entries:scenes.length,scene_categories:categories.length,search:true,detail_semantics:true,scene_alternatives:true,name_only_prompt:true,mobile:true}));
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
