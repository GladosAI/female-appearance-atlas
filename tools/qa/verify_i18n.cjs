const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {launchBrowser,sharp}=require('./runtime.cjs');
const root=path.resolve(__dirname,'../..'),output=path.join(root,'.work/qa');fs.mkdirSync(output,{recursive:true});
const data=JSON.parse(fs.readFileSync(path.join(root,'data/catalog.json'),'utf8'));
const packs=Object.fromEntries(['en','ja'].map(locale=>[locale,JSON.parse(fs.readFileSync(path.join(root,`source/i18n/${locale}.json`),'utf8'))]));
const entries=new Map(data.entries.map(entry=>[entry.id,entry])),reference=entries.get('AH020');
const libraryKey='female-beauty-appearance-library-v2',historyKey='female-beauty-prompt-history-v1';
const cards=[{id:'qa-i18n-personal-a',name:'我的发型 · My own name / 個人名',notes:'保留原文：发型、服装、主题。Do not translate / 翻訳しない。',selected:['AH020','TO086','SO093']},
 {id:'qa-i18n-personal-b',name:'第二张卡：服装与发型',notes:'Another private note：返回顶部',selected:['AH031']}];
const fixture={schema:'female-appearance-library/v2',cards,lastAddedCardId:cards[0].id};
const base=process.env.ATLAS_TEST_URL||pathToFileURL(path.join(root,'index.html')).href;
function route(values={}){const url=new URL(base);url.search='';for(const [key,value] of Object.entries(values))if(value!==undefined&&value!==null)url.searchParams.set(key,value);return url.href}
function translated(id,field,locale){return locale==='zh'?entries.get(id)[field]:packs[locale].entries[id][field]}

(async()=>{
 const browser=await launchBrowser();
 try{
  const page=await browser.newPage({viewport:{width:1365,height:950}}),errors=[],detailRequests=[];
  page.on('pageerror',error=>errors.push(error.message));page.on('request',request=>{if(/\/details-[^/]+\.js/.test(request.url()))detailRequests.push(request.url())});
  const waitLanguage=async locale=>{
   await page.waitForFunction(locale=>globalThis.AtlasI18n?.locale===locale&&document.documentElement.lang===({zh:'zh-CN',en:'en',ja:'ja'}[locale]),locale);
   await page.locator('#language-select').waitFor({state:'visible'});assert.equal(await page.locator('#language-select').inputValue(),locale);
  };
  const switchLanguage=async locale=>{
   await Promise.all([page.waitForURL(url=>url.searchParams.get('lang')===locale),page.locator('#language-select').selectOption(locale)]);
   await waitLanguage(locale);
  };
  const referenceCard=()=>page.locator('#entry-grid .entry').filter({has:page.locator('.title-button[data-detail="AH020"]')});
  const assertPersonalData=async()=>{
   const stored=await page.evaluate(key=>JSON.parse(localStorage.getItem(key)),libraryKey);
   for(const expected of cards){const actual=stored.cards.find(card=>card.id===expected.id);assert(actual);for(const field of ['name','notes','selected'])assert.deepEqual(actual[field],expected[field],'Language changes preserve personal '+field)}
  };
  const waitPrompt=async value=>page.waitForFunction(value=>document.getElementById('synthesis-prompt').value===value,value);
  const assertNameOnlyPrompt=async(locale,ids)=>{
   await page.waitForFunction(({locale,id,name})=>document.getElementById('synthesis-language').value===locale&&document.getElementById('synthesis-prompt').value.includes(name),{locale,id:ids[0],name:translated(ids[0],'name',locale)});
   const prompt=await page.locator('#synthesis-prompt').inputValue();
   for(const id of ids){assert(prompt.includes(translated(id,'name',locale)),`${locale} prompt includes ${id} name`);for(const field of ['description','design_tip']){const detail=translated(id,field,locale);if(detail&&detail.length>12)assert(!prompt.includes(detail),`${locale} prompt excludes ${id} ${field}`)}}
   assert(!prompt.includes('【图1'));return prompt;
  };
  await page.goto(route({lang:'zh',section:'hair_with_accessories'}));await waitLanguage('zh');
  await page.evaluate(({libraryKey,historyKey,fixture})=>{localStorage.setItem(libraryKey,JSON.stringify(fixture));localStorage.removeItem(historyKey);localStorage.removeItem('female-beauty-prompt-language-v1')},{libraryKey,historyKey,fixture});

  // Old links retain the original Chinese dimension value; only labels change.
  await page.goto(route({section:reference.category,dimension:reference.dimension,lang:'ja'}));await waitLanguage('ja');
  await referenceCard().waitFor();assert.equal(await page.locator('#dimension-filter').inputValue(),reference.dimension);
  assert.equal(new URL(page.url()).searchParams.get('dimension'),reference.dimension);
  assert(await page.evaluate(()=>['半身','中性','内向','交通警察','外观道具与装备','角色头饰与面部道具','角色手持与场景道具','Cosplay头饰、外挂与道具'].every(source=>{
   const once=AtlasI18n.t(source);return AtlasI18n.t(once)===once;
  })),'Explicit helpers must not translate localized Japanese a second time');
  assert(await page.evaluate(()=>Object.values(ATLAS_LOCALES.ja.entries).every(entry=>Object.values(entry).filter(value=>typeof value==='string').every(value=>AtlasI18n.t(value)===value))),'Known Japanese entry fields are already localized');
  // Already localized Japanese must survive the DOM observer unchanged, even
  // when a translated compound contains a shorter Chinese source term.
  await page.evaluate(()=>{
   const fixture=document.createElement('div');fixture.id='qa-localized-text';fixture.hidden=true;
   for(const source of ['半身','中性','内向','交通警察']){
    const span=document.createElement('span');span.dataset.expected=AtlasI18n.t(source)+' · 12';span.textContent=span.dataset.expected;fixture.append(span);
   }
   const privateLabel=document.createElement('span');privateLabel.dataset.i18nSkip='';privateLabel.title='发型、服装、主题';privateLabel.textContent='发型、服装、主题';fixture.append(privateLabel);document.body.append(fixture);
  });
  await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
  assert(await page.locator('#qa-localized-text [data-expected]').evaluateAll(elements=>elements.every(element=>element.textContent===element.dataset.expected)),'Do not translate Japanese compounds a second time');
  assert.equal(await page.locator('#qa-localized-text [data-i18n-skip]').getAttribute('title'),'发型、服装、主题');
  await page.locator('#qa-localized-text').evaluate(element=>element.remove());
  assert.equal(await referenceCard().locator('.title-button').textContent(),translated(reference.id,'name','ja'));
  const thumbLabel=await referenceCard().locator('.thumb[role="img"]').getAttribute('aria-label');
  assert(thumbLabel&&!['物件或造型参考','AI 创作示意','全部词条','类别'].some(fragment=>thumbLabel.includes(fragment)),'Japanese image labels contain no untranslated Chinese fragments');
  const categoryTag=referenceCard().locator('[data-entry-category]');
  for(const attribute of ['aria-label','title']){const label=await categoryTag.getAttribute(attribute);assert(label&&!['浏览','全部词条','打开','类别'].some(fragment=>label.includes(fragment)),'Japanese category attributes are formatted before insertion');}
  assert.equal((await referenceCard().locator('.desc').textContent()).trim(),translated(reference.id,'description','ja'));
  assert.equal(detailRequests.length,0,'Browsing must not fetch detail chunks');
  await referenceCard().locator('.title-button').click();await page.locator('#detail-dialog [data-entry-feedback="AH020"]').waitFor();
  assert.equal(await page.locator('#detail-dialog .detail-copy > h2').textContent(),translated(reference.id,'name','ja'));
  assert((await page.locator('#detail-dialog .detail-copy').textContent()).includes(translated(reference.id,'design_tip','ja')));
  if(/^https?:/.test(base))assert(detailRequests.length>0,'HTTP details remain lazy loaded');
  await page.locator('#close-dialog').click();

  // Search in one language is usable from another interface language.
  const japaneseQuery=translated(reference.id,'name','ja');
  await page.locator('#search').fill(japaneseQuery);await page.locator('#search').press('Enter');await referenceCard().waitFor();
  await switchLanguage('en');await referenceCard().waitFor();
  assert.equal(await page.locator('#search').inputValue(),japaneseQuery);
  assert.equal(await referenceCard().locator('.title-button').textContent(),translated(reference.id,'name','en'));
  assert.equal(await page.locator('#dimension-filter').inputValue(),reference.dimension);
  await referenceCard().locator('.title-button').click();await page.locator('#detail-dialog [data-entry-feedback="AH020"]').waitFor();
  assert.equal(await page.locator('#detail-dialog .detail-copy > h2').textContent(),translated(reference.id,'name','en'));
  assert((await page.locator('#detail-dialog .detail-copy').textContent()).includes(translated(reference.id,'description','en')));
  await page.locator('#close-dialog').click();
  await page.locator('#search').fill(reference.en);await page.locator('#search').press('Enter');await referenceCard().waitFor();
  for(const locale of ['zh','en','ja']){
   await switchLanguage(locale);await referenceCard().waitFor();
   assert.equal(await page.locator('#search').inputValue(),reference.en);
   assert.equal(await referenceCard().locator('.title-button').textContent(),translated(reference.id,'name',locale));
   await page.reload();await waitLanguage(locale);await referenceCard().waitFor();
   const url=new URL(page.url());url.searchParams.delete('lang');await page.goto(url.href);await waitLanguage(locale);await referenceCard().waitFor();
   assert.equal(await page.locator('#dimension-filter').inputValue(),reference.dimension);
  }
  await page.screenshot({path:path.join(output,'i18n-japanese-browse.png')});

  // UI locale and prompt locale are independent; user content remains literal.
  await page.goto(route({view:'card',card:cards[0].id,lang:'en'}));await waitLanguage('en');
  await page.locator('#appearance-card-title').waitFor();assert.equal(await page.locator('#appearance-card-title').textContent(),cards[0].name);
  assert.equal(await page.locator('#card-notes-preview').textContent(),cards[0].notes);await assertPersonalData();
  await page.locator('#open-card-synthesis').click();await page.locator('#card-synthesis-dialog').waitFor();
  await assertNameOnlyPrompt('en',cards[0].selected);
  await page.locator('#synthesis-language').selectOption('ja');await assertNameOnlyPrompt('ja',cards[0].selected);
  assert.equal(await page.locator('#language-select').inputValue(),'en');assert.equal(await page.locator('html').getAttribute('lang'),'en');
  await page.locator('#synthesis-language').selectOption('en');await assertNameOnlyPrompt('en',cards[0].selected);
  await page.locator('[data-synthesis-entry="AH020"] input').uncheck();
  const manual='请保留：发型和服装。\nMy manually edited prompt / 手動編集した文章。';
  await page.locator('#synthesis-prompt').fill(manual);
  await page.waitForFunction(({historyKey,card,manual})=>JSON.parse(localStorage.getItem(historyKey)||'[]').some(item=>item.cardKey===card&&item.prompt===manual&&item.promptLanguage==='en'&&!item.selected.includes('AH020')),{historyKey,card:cards[0].id,manual});
  await page.locator('#close-card-synthesis').click();await switchLanguage('ja');
  assert.equal(new URL(page.url()).searchParams.get('card'),cards[0].id);
  assert.equal(await page.locator('#appearance-card-title').textContent(),cards[0].name);
  assert.equal(await page.locator('#card-notes-preview').textContent(),cards[0].notes);
  await page.locator('#open-card-synthesis').click();await waitPrompt(manual);
  assert.equal(await page.locator('#synthesis-language').inputValue(),'en');assert(!(await page.locator('[data-synthesis-entry="AH020"] input').isChecked()));
  await page.reload();await waitLanguage('ja');await page.locator('#open-card-synthesis').click();await waitPrompt(manual);
  assert.equal(await page.locator('#synthesis-language').inputValue(),'en');await assertPersonalData();
  await page.screenshot({path:path.join(output,'i18n-prompt-independent-desktop.png')});
  await page.setViewportSize({width:390,height:844});
  assert(await page.locator('#card-synthesis-dialog').evaluate(element=>element.scrollWidth<=element.clientWidth+1));
  assert.equal(await page.locator('#synthesis-references').evaluate(element=>getComputedStyle(element).gridTemplateColumns.split(' ').length),3);
  await page.screenshot({path:path.join(output,'i18n-prompt-independent-mobile.png')});await page.locator('#close-card-synthesis').click();
  await page.goto(route({view:'card',card:cards[1].id,lang:'ja'}));await waitLanguage('ja');await page.locator('#open-card-synthesis').click();
  const otherPrompt=await assertNameOnlyPrompt('en',cards[1].selected);assert(!otherPrompt.includes(manual));
  await page.locator('#close-card-synthesis').click();await assertPersonalData();
  // The contribution form switches in place, retaining unsaved input and files.
  await page.goto(route({section:reference.category,lang:'en'}));await waitLanguage('en');
  assert.equal(new URL(await page.locator('footer a[href*="contribute.html"]').getAttribute('href'),base).searchParams.get('lang'),'en','Contribution links retain the shared URL language');
  const contribution=new URL('contribute.html',base);contribution.searchParams.set('lang','en');
  await page.goto(contribution.href);await waitLanguage('en');
  const privateName='发型 · untouched personal input',privateDescription='衣服与主题：私有草稿，保持原文。';
  await page.locator('#name').fill(privateName);await page.locator('#description').fill(privateDescription);
  const image=await sharp({create:{width:8,height:8,channels:3,background:'#c0b0a0'}}).png().toBuffer();
  await page.locator('#image').setInputFiles({name:'private-preview.png',mimeType:'image/png',buffer:image});await page.locator('#image-preview').waitFor({state:'visible'});
  const preview=await page.locator('#image-preview').getAttribute('src'),canonicalCategory=await page.locator('#category').inputValue(),canonicalDimension=await page.locator('#dimension').inputValue();
  for(const locale of ['ja','zh','en']){
   await page.locator('#language-select').selectOption(locale);await waitLanguage(locale);await page.waitForFunction(()=>!document.getElementById('language-select').disabled);
   assert.equal(await page.locator('h1').textContent(),locale==='zh'?'贡献一个素材词条':packs[locale].messages['贡献一个素材词条'],'In-place switching restores static text, including Chinese');
   assert.equal(await page.locator('#language-select').getAttribute('aria-label'),locale==='zh'?'页面语言':packs[locale].messages['页面语言'],'In-place switching restores accessible labels');
   assert.equal(await page.locator('#name').inputValue(),privateName);assert.equal(await page.locator('#description').inputValue(),privateDescription);
   assert.equal(await page.locator('#category').inputValue(),canonicalCategory);assert.equal(await page.locator('#dimension').inputValue(),canonicalDimension);
   assert.equal(await page.locator('#image').evaluate(element=>element.files.length),1);assert.equal(await page.locator('#image-preview').getAttribute('src'),preview);
   assert(await page.locator('main').evaluate(element=>element.scrollWidth<=element.clientWidth+1));
  }
  await page.screenshot({path:path.join(output,'i18n-contribution-mobile.png')});
  if(/^https?:/.test(base)){
   const languageAsset=/\/(?:locale-ja-[^/?]+|ja)\.js(?:\?|$)/;
   await page.route(languageAsset,route=>route.abort());await page.goto(route({section:reference.category,lang:'ja'}));
   await page.locator('.language-load-error').waitFor();await waitLanguage('zh');await referenceCard().waitFor();
   assert.equal(new URL(page.url()).searchParams.get('lang'),'ja','Keep requested language so Retry can recover');
   await page.unroute(languageAsset);await page.locator('.language-load-error button').click();await waitLanguage('ja');await referenceCard().waitFor();
   assert.equal(await page.locator('.language-load-error').count(),0);
  }
  assert.deepEqual(errors,[]);
  const result={passed:true,locales:['zh','en','ja'],file_or_http:new URL(base).protocol,legacy_dimension_urls:true,language_route_and_reload:true,cross_language_search:true,localized_details:true,lazy_details:/^https?:/.test(base),personal_names_notes_preserved:true,independent_prompt_language:true,name_only_prompt:true,manual_history_preserved:true,contribution_input_and_image_preserved:true,language_failure_and_retry:/^https?:/.test(base),mobile:true};
  fs.writeFileSync(path.join(output,'i18n-report.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
