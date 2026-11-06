// Display translations overlay immutable catalog records; IDs and storage stay canonical.
(()=>{'use strict';
 const supported=new Set(['zh','en','ja']),storageKey='female-beauty-language-v1';
 const canonicalLocale=value=>({zh:'zh','zh-cn':'zh','zh-hans':'zh',en:'en','en-us':'en','en-gb':'en',ja:'ja','ja-jp':'ja'}[String(value||'').toLowerCase()]||null);
 let saved=null;try{saved=localStorage.getItem(storageKey)}catch{}
 const requested=canonicalLocale(new URLSearchParams(location.search).get('lang'))||canonicalLocale(saved)||'zh';
 const api={locale:requested,requestedLocale:requested,loadError:null};
 const loading=new Map(),patterns=new Map(),translatedValues=new Map(),translatedNodes=new WeakMap(),translatedAttributes=new WeakMap(),originalTitle=document.title;globalThis.ATLAS_LOCALES??={};
 const pack=locale=>globalThis.ATLAS_LOCALES[canonicalLocale(locale)||api.locale];
 const localeTag=locale=>({zh:'zh-CN',en:'en',ja:'ja'}[canonicalLocale(locale)||api.locale]);
 function ensure(locale){
  locale=canonicalLocale(locale)||'zh';if(locale==='zh')return Promise.resolve(null);
  if(pack(locale))return Promise.resolve(pack(locale));if(loading.has(locale))return loading.get(locale);
  const promise=new Promise((resolve,reject)=>{
   const script=document.createElement('script'),path=globalThis.ATLAS_LOCALE_PATHS?.[locale]||`data/locales/${locale}.js`;
   const timer=setTimeout(()=>finish(new Error('Language pack timed out: '+locale)),20000);
   function finish(error){clearTimeout(timer);script.remove();if(error){loading.delete(locale);reject(error)}else if(!pack(locale)){loading.delete(locale);reject(new Error('Invalid language pack: '+locale))}else{patterns.delete(locale);patterns.delete(locale+'|dom');translatedValues.delete(locale);resolve(pack(locale))}}
   script.src=new URL(path,document.baseURI).href;script.async=true;script.onload=()=>finish();script.onerror=()=>finish(new Error('Language pack could not load: '+locale));document.head.append(script);
  });loading.set(locale,promise);return promise;
 }
 function text(value,locale=api.locale,protectTranslated=true){
  const source=String(value??'');locale=canonicalLocale(locale)||api.locale;if(locale==='zh'||!source)return source;
  const messages=pack(locale)?.messages||{},trimmed=source.trim();
  if(protectTranslated){
   if(!translatedValues.has(locale)){
    const values=Object.values(messages);
    for(const entry of Object.values(pack(locale)?.entries||{}))for(const value of Object.values(entry))if(typeof value==='string')values.push(value);
    translatedValues.set(locale,new Set(values));
   }
   if(translatedValues.get(locale).has(trimmed))return source;
  }
  if(typeof messages[source]==='string')return messages[source];
  if(typeof messages[trimmed]==='string')return source.replace(trimmed,messages[trimmed]);
  // Complete literal messages take precedence. Substrings cover counts and labels
  // assembled by legacy templates, without rewriting IDs, URLs or form values.
  if(!/[\u3400-\u9fff]/u.test(source))return source;
  const patternKey=locale+(protectTranslated?'|dom':'');
  if(!patterns.has(patternKey)){
   const candidates=Object.keys(messages).filter(key=>typeof messages[key]==='string');
   if(protectTranslated){
    candidates.push(...Object.values(messages));
    // Protect names embedded in formatted labels. Whole translated descriptions
    // are handled by the value set without enlarging the substring matcher.
    for(const entry of Object.values(pack(locale)?.entries||{}))if(entry.name)candidates.push(entry.name);
   }
   const keys=[...new Set(candidates)].filter(key=>key.length>=2&&/[\u3400-\u9fff]/u.test(key)).sort((a,b)=>b.length-a.length);
   patterns.set(patternKey,keys.length?new RegExp(keys.map(key=>key.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|'),'gu'):null);
  }
  const pattern=patterns.get(patternKey);return pattern?source.replace(pattern,key=>protectTranslated&&translatedValues.get(locale).has(key)?key:messages[key]):source;
 }
 function translation(entry,field,locale=api.locale){
  locale=canonicalLocale(locale)||api.locale;
  if(locale==='zh')return {value:entry?.[field]??'',locale:'zh'};
  const translated=pack(locale)?.entries?.[entry?.id]?.[field];
  if(typeof translated==='string'&&translated.trim())return {value:translated,locale};
  const shared=pack(locale)?.messages?.[entry?.[field]];
  if(typeof shared==='string'&&shared.trim())return {value:shared,locale};
  if(field==='name'){
   const english=pack('en')?.entries?.[entry?.id]?.name||entry?.en;
   if(english)return {value:english,locale:'en'};
  }
  if(locale==='ja'){
   const english=pack('en')?.entries?.[entry?.id]?.[field]||pack('en')?.messages?.[entry?.[field]];
   if(typeof english==='string'&&english.trim())return {value:english,locale:'en'};
  }
  return {value:entry?.[field]??'',locale:'zh'};
 }
 const entryText=(entry,field,locale)=>translation(entry,field,locale).value;
 const entryName=(entry,locale)=>entryText(entry,'name',locale);
 const entryLanguage=(entry,field='name',locale)=>localeTag(translation(entry,field,locale).locale);
 const hasTranslation=(entry,field='name',locale=api.locale)=>translation(entry,field,locale).locale===(canonicalLocale(locale)||api.locale);
 const format=(source,values={},locale=api.locale)=>text(source,locale).replace(/\{([A-Za-z][A-Za-z0-9_]*)\}/g,(token,key)=>Object.hasOwn(values,key)?String(values[key]):token);
 function translateElement(element){
  if(!element?.getAttribute||element.closest('[data-i18n-skip]'))return;
  if(!element.hasAttribute('data-i18n-skip-attributes'))for(const attribute of ['aria-label','aria-description','placeholder','title']){
   if(element.hasAttribute(attribute)){
    const current=element.getAttribute(attribute),previous=translatedAttributes.get(element)?.get(attribute);
    if(previous?.target===current&&previous.locale===api.locale)continue;
    const source=previous?.target===current?previous.source:current;
    const target=text(source,api.locale,true);if(!translatedAttributes.has(element))translatedAttributes.set(element,new Map());
    translatedAttributes.get(element).set(attribute,{source,target,locale:api.locale});if(target!==current)element.setAttribute(attribute,target);
   }
  }
 }
 function translateTree(root){
  if(!root)return;
  if(root.nodeType===Node.TEXT_NODE){
   const parent=root.parentElement;if(!parent||parent.closest('script,style,textarea,code,pre,[data-i18n-skip],[contenteditable="true"]'))return;
   const current=root.nodeValue,previous=translatedNodes.get(root);if(previous?.target===current&&previous.locale===api.locale)return;
   const source=previous?.target===current?previous.source:current;
   const target=text(source,api.locale,true);translatedNodes.set(root,{source,target,locale:api.locale});if(current!==target)root.nodeValue=target;return;
  }
  if(root.nodeType!==Node.ELEMENT_NODE&&root.nodeType!==Node.DOCUMENT_NODE)return;
  if(root.nodeType===Node.ELEMENT_NODE){translateElement(root);if(root.matches('script,style,textarea,code,pre,[data-i18n-skip],[contenteditable="true"]'))return}
  for(const child of root.childNodes)translateTree(child);
 }
 let observer;
 function apply(){
  document.documentElement.lang=localeTag();document.title=text(originalTitle);translateTree(document.body);
  for(const element of document.querySelectorAll('[data-i18n-format]')){
   element.textContent=format(element.dataset.i18nFormat,JSON.parse(element.dataset.i18nValues||'{}'));
  }
  document.documentElement.style.setProperty('--tree-expand-label',JSON.stringify(text('展开')));document.documentElement.style.setProperty('--tree-collapse-label',JSON.stringify(text('收起')));
  const selector=document.getElementById('language-select');if(selector)selector.value=api.locale;
  // Language is part of shareable internal URLs; raw data and external links are unchanged.
  for(const link of document.querySelectorAll('a[href]')){
   const url=new URL(link.href,document.baseURI);
   if(url.origin===location.origin&&(/(?:^|\/)(?:index|contribute)\.html$/.test(url.pathname)||url.pathname.endsWith('/'))&&url.protocol===location.protocol&&(api.locale!=='zh'||url.searchParams.has('lang'))){url.searchParams.set('lang',api.locale);if(link.href!==url.href)link.href=url.href}
  }
 }
 function observe(){
  apply();if(observer)return;
  observer=new MutationObserver(records=>{
   for(const record of records){
    if(record.type==='characterData')translateTree(record.target);
    else if(record.type==='attributes')translateElement(record.target);
    else for(const node of record.addedNodes)translateTree(node);
   }
  });observer.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['aria-label','aria-description','placeholder','title']});
 }
 function switchLanguage(locale){
  locale=canonicalLocale(locale);if(!supported.has(locale))return;
  try{localStorage.setItem(storageKey,locale)}catch{}
  const url=new URL(location.href);url.searchParams.set('lang',locale);
  const event=new CustomEvent('atlas:beforelocalechange',{detail:{locale},cancelable:true});
  if(document.dispatchEvent(event))location.assign(url.href);
 }
 async function setLocale(locale){
  locale=canonicalLocale(locale);if(!supported.has(locale))throw new Error('Unsupported language');await ensure(locale);
  api.locale=api.requestedLocale=locale;api.loadError=null;try{localStorage.setItem(storageKey,locale)}catch{}
  const url=new URL(location.href);url.searchParams.set('lang',locale);history.replaceState(null,'',url.href);apply();return locale;
 }
 Object.assign(api,{ensure,t:text,text,format,entryText,entryName,entryLanguage,hasTranslation,localeTag,apply,observe,switchLanguage,setLocale});globalThis.AtlasI18n=api;
 api.ready=ensure(requested).catch(error=>{api.loadError=error;api.locale='zh';return null});
 document.addEventListener('change',event=>{if(event.target.id==='language-select')switchLanguage(event.target.value)});
 api.ready.then(()=>{
  const start=()=>{observe();if(api.loadError){const notice=document.createElement('div');notice.className='language-load-error';notice.setAttribute('role','alert');notice.innerHTML='语言包加载失败，暂时显示中文。 <button type="button">重试 / Retry</button>';notice.querySelector('button').addEventListener('click',()=>location.reload());document.querySelector('#main,main')?.prepend(notice)}};
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
 });
})();
