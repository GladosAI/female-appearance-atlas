// Shared directory, search, facets, card/sheet presentation, and history.
const B=new Map(N.groups.flatMap(g=>g.sections.map(s=>[s.scope,{...s,parent:g}])));
for(const [id,b] of B)scopes.set(id,{name:b.name,guide:b.parent.note});
for(const [id,l] of Object.entries(N.legacy_scopes||{}))scopes.set(id,{name:l.name,guide:'旧版专题范围；可继续按新的领域、分组与类别查找。'});
let styleFilter='',sortOrder='directory',pushRoute=false,lastURL='',filteredEntries=[],suggestionFocus=-1;
let sidebarCategory=null;
let lastBrowsePosition=null;
const termBatchSize=72,termLoadMargin=640;
let renderedTermCount=0,termLoadGeneration=0,pendingTermLoad=null,termLoadObserver=null;
function resetTermAutoLoad(){termLoadGeneration++;pendingTermLoad=null;termLoadObserver?.disconnect()}
function canAutoLoadTerms(){
 if(view!=='terms'||$('terms-view').hidden||$('entry-grid').hidden||$('more-wrap').hidden||renderedTermCount>=filteredEntries.length||document.visibilityState==='hidden'||document.querySelector('dialog[open]'))return false;
 const box=$('more-wrap').getBoundingClientRect();return box.top<=window.innerHeight+termLoadMargin&&box.bottom>=-termLoadMargin;
}
function updateTermLoadStatus(){
 const remaining=filteredEntries.length-renderedTermCount;
 $('more-wrap').hidden=view!=='terms'||$('entry-grid').hidden||remaining<=0;
 $('auto-load-status').textContent=remaining>0?`继续向下浏览，自动加载其余 ${remaining} 项`:'';
}
function queueTermAutoLoad(){
 if(pendingTermLoad!==null||!canAutoLoadTerms())return;
 const generation=termLoadGeneration;pendingTermLoad=generation;
 requestAnimationFrame(()=>{
  if(generation!==termLoadGeneration)return;pendingTermLoad=null;if(!canAutoLoadTerms())return;
  const end=Math.min(renderedTermCount+termBatchSize,filteredEntries.length),grid=$('entry-grid');
  grid.setAttribute('aria-busy','true');
  try{grid.insertAdjacentHTML('beforeend',filteredEntries.slice(renderedTermCount,end).map(entryCard).join(''));renderedTermCount=end;limit=end;
   $('result-status').textContent=`${filteredEntries.length} 个结果 · 显示 ${renderedTermCount} 个`;updateTermLoadStatus();
  }finally{grid.removeAttribute('aria-busy')}
  queueTermAutoLoad();
 });
}
function updateTermAutoLoad(){
 updateTermLoadStatus();if($('more-wrap').hidden)return;
 if(termLoadObserver)termLoadObserver.observe($('more-wrap'));
 queueTermAutoLoad();
}
try{if(typeof window.IntersectionObserver==='function')termLoadObserver=new window.IntersectionObserver(entries=>{if(entries.some(entry=>entry.isIntersecting))queueTermAutoLoad()},{rootMargin:`${termLoadMargin}px 0px`,threshold:0})}catch{termLoadObserver=null}
if(!termLoadObserver)window.addEventListener('scroll',queueTermAutoLoad,{passive:true});
window.addEventListener('resize',queueTermAutoLoad);
document.addEventListener('visibilitychange',queueTermAutoLoad);
document.addEventListener('close',queueTermAutoLoad,true);
const boardOrder=new Map(D.boards.map((b,i)=>[b.id,i]));
const normalize=s=>String(s??'').normalize('NFKC').toLocaleLowerCase().trim();
const searchIndex=new Map(D.entries.map(e=>{
 const dimension=e.history_line_name||e.dimension,keywords=e.history_line?e.keywords.filter(k=>k!==e.dimension):e.keywords;
 return [e.id,normalize([e.id,e.name,e.en,e.category_name,categoryName(e.category),dimension,e.description,...keywords,...e.styles.map(s=>F.get(s)?.name||s),...(e.aliases||[])].join(' '))];
}));
const searchAliases=new Map();
const historyRegionTokens=new Map([['南亚','south_asia'],['西亚','west_asia'],['东南亚','southeast_asia']]);
for(const [word,aliases] of Object.entries(N.search_aliases||{})){const family=[word,...aliases].map(normalize);for(const term of family)searchAliases.set(term,family)}
function tokensFor(q){return normalize(q).replace(/(?<![\d.])(\d+)\s*(?:denier|den|d)\b/g,' $1d ').split(/[\s，,、;；]+/).filter(Boolean)}
function matchesToken(e,t){
 const d=t.match(/^(\d+)d$/);if(d&&(D.meta.denier_values||[]).includes(Number(d[1])))return e.denier===Number(d[1]);
 if(e.history_track==='regional'&&historyRegionTokens.has(t))return e.history_line===historyRegionTokens.get(t);
 const season=t.match(/^(春季|夏季|秋季|冬季|春装|夏装|秋装|冬装)(.+)$/);if(season)return matchesToken(e,season[1])&&matchesToken(e,season[2]);
 const words=searchAliases.get(t)||[t],hay=searchIndex.get(e.id);if(words.some(w=>hay.includes(w)))return true;
 if(t.endsWith('耳机')&&t!=='耳机')return hay.includes(t.slice(0,-2))&&matchesToken(e,'耳机');
 return false;
}
function matchesCategory(e,cat=category){
 if(cat==='all')return true;if(G.has(cat))return G.get(cat).categories.includes(e.category);if(B.has(cat))return B.get(cat).categories.includes(e.category);
 if(N.legacy_scopes?.[cat])return N.legacy_scopes[cat].categories.includes(e.category);
 if(S.has(cat))return clothingCategories.has(e.category)&&e.styles.includes(S.get(cat).style_id);
 if(cat==='clothing_new')return e.added_in===(D.meta.last_content_version||D.meta.version);
 return cat==='life_stages'?!!e.life_stage_reference:cat==='special'?D.meta.special_costume_categories.includes(e.category):cat==='wedding'?!!e.wedding_reference:cat==='seasonal'?!!e.seasonal_reference:cat==='anthro'?!!e.anthro_reference:cat==='socks'?!!e.hosiery_reference:cat==='facial'?!!e.facial_reference:cat==='cosplay'?!!e.cosplay_reference:cat==='hair'?hairCategories.has(e.category):cat==='hooded_cloaks'?!!e.hooded_cloak:cat==='clothing'?clothingCategories.has(e.category):e.category===cat;
}
function pathFor(id=category){const b=B.get(id)||B.get(N.category_paths[id]?.section);return {domain:G.get(id)||b?.parent,branch:b,leaf:C.get(id)}}
function scopeLabel(id=category){return id==='all'?'全部图鉴':id==='clothing'?'全部服装':id==='clothing_new'?'最近补充':categoryName(id)}
function score(e,q=query){const n=normalize(q);return normalize(e.id)===n?1000:normalize(e.name)===n?500:normalize(e.name).startsWith(n)?250:normalize(e.name).includes(n)?150:normalize(e.en).includes(n)?90:40}
function getResults({scope=category,dimension=$('dimension-filter').value,style=styleFilter,q=query}={}){
 const ts=tokensFor(q);return D.entries.filter(e=>matchesCategory(e,scope)&&(dimension==='all'||!dimension||e.dimension===dimension)&&(!style||clothingCategories.has(e.category)&&e.styles.includes(style))&&ts.every(t=>matchesToken(e,t)));
}
function sortResults(arr){return arr.sort((a,b)=>{
 if(sortOrder==='relevance'&&query){const diff=score(b)-score(a);if(diff)return diff}
 if(sortOrder==='name')return a.name.localeCompare(b.name,'zh-CN');if(sortOrder==='id')return a.id.localeCompare(b.id,undefined,{numeric:true});
 if(mode==='illustrated')return (boardOrder.get(a.visual?.board)??9999)-(boardOrder.get(b.visual?.board)??9999)||a.visual.row*a.visual.columns+a.visual.column-(b.visual.row*b.visual.columns+b.visual.column);
 return categoryOrder.get(a.category)-categoryOrder.get(b.category)||a.id.localeCompare(b.id,undefined,{numeric:true});
})}
function categoryButton(id,label,count){return `<button data-category="${id}"><span>${esc(label)}</span><small>${count}</small></button>`}
function scopeCount(id){return D.entries.filter(e=>matchesCategory(e,id)).length}
function treeLink(id,label,count,kind='leaf'){
 return `<button class="tree-link tree-link-${kind}" data-category="${id}"><span class="tree-leaf-mark" aria-hidden="true"></span><span class="tree-link-label">${esc(label)}</span><small>${count}项</small><span class="tree-current-mark" aria-hidden="true"></span></button>`;
}
function treeSummary(label,count,level){
 return `<summary class="tree-summary" aria-label="展开或收起${level}：${esc(label)}"><span class="tree-toggle" aria-hidden="true"></span><span class="tree-heading"><strong>${esc(label)}</strong><small>${level} · ${count}个类别</small></span><span class="tree-action" aria-hidden="true"></span></summary>`;
}
function revealSidebarPath(scroll=false){
 const {domain,branch}=pathFor();if(domain)document.querySelector(`#categories [data-domain="${domain.scope}"]`).open=true;if(branch)document.querySelector(`#categories [data-branch="${branch.scope}"]`).open=true;
 if(scroll){const active=document.querySelector('#categories [aria-current="page"]');active?.scrollIntoView({block:'nearest',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})}
}
function renderSidebar(){
 $('categories').classList.add('catalog-tree');
 $('categories').innerHTML=`<div class="tree-guide"><span>领域</span><b aria-hidden="true">›</b><span>分组</span><b aria-hidden="true">›</b><span>类别</span></div><div class="tree-toolbar"><button type="button" id="tree-reveal">定位当前</button><button type="button" id="tree-expand">全部展开</button><button type="button" id="tree-collapse">全部收起</button></div>`+treeLink('all','全部图鉴',D.entries.length,'root')+N.groups.map(g=>`<details class="nav-topic" data-domain="${g.scope}">${treeSummary(g.name,g.category_count,'领域')}<div class="nav-children tree-domain-children">${treeLink(g.scope,'查看此领域全部',g.count,'overview')}${g.sections.map(s=>`<details class="nav-branch" data-branch="${s.scope}">${treeSummary(s.name,s.category_count,'分组')}<div class="tree-branch-children">${treeLink(s.scope,'查看此分组全部',s.count,'overview')}${s.categories.map(cid=>treeLink(cid,categoryName(cid),C.get(cid).count)).join('')}</div></details>`).join('')}</div></details>`).join('');
 $('tree-expand').addEventListener('click',()=>{$('categories').querySelectorAll('details').forEach(d=>d.open=true)});
 $('tree-collapse').addEventListener('click',()=>{$('categories').querySelectorAll('details').forEach(d=>d.open=false)});
 $('tree-reveal').addEventListener('click',()=>revealSidebarPath(true));
}
function renderDirectory(){
 $('topic-directory').innerHTML=N.groups.map((g,i)=>`<article class="domain-card"><div class="domain-title"><span class="domain-number">${String(i+1).padStart(2,'0')}</span><div><h3><button data-category="${g.scope}">${esc(g.name)} <span aria-hidden="true">↗</span></button></h3><span>${g.category_count}类 · ${g.count}项</span></div></div><p>${esc(g.note)}</p><div class="domain-branches">${g.sections.map(s=>categoryButton(s.scope,s.name,s.count)).join('')}</div><details class="domain-tree"><summary>展开全部${g.category_count}个类别</summary>${g.sections.map(s=>`<div class="tree-section"><strong>${esc(s.name)}</strong><div>${s.categories.map(cid=>categoryButton(cid,categoryName(cid),C.get(cid).count)).join('')}</div></div>`).join('')}</details></article>`).join('');
 renderSidebar();
 $('directory-shortcuts').innerHTML=N.shortcuts.filter(s=>N.featured_shortcuts.includes(s.id)).map(s=>categoryButton(s.id,s.name,scopeCount(s.id))).join('');
 $('document-links').innerHTML=N.documents.map(d=>`<a href="${d.path}" target="_blank">${esc(d.name)} ↗</a>`).join('');
}
function fillSelect(id,options,value){const el=$(id);const html=options.map(([v,n,disabled])=>`<option value="${esc(v)}"${disabled?' disabled':''}>${esc(n)}</option>`).join('');if(el.innerHTML!==html)el.innerHTML=html;el.value=value}
function prepareDimensions(value='all'){const base=D.entries.filter(e=>matchesCategory(e));const dims=[...new Set(base.map(e=>e.dimension))];fillSelect('dimension-filter',[['all','全部细分'],...dims.map(d=>[d,d.replace(/^新增/,'')+' · '+base.filter(e=>e.dimension===d).length])],dims.includes(value)?value:'all')}
function renderTopicContext(){
 const {domain,branch,leaf}=pathFor();
 fillSelect('group-filter',[['all','全部领域'],...N.groups.map(g=>[g.scope,g.name+' · '+g.count])],domain?.scope||'all');
 fillSelect('branch-filter',[['all','全部分组'],...(domain?.sections||[]).map(s=>[s.scope,s.name+' · '+s.count])],branch?.scope||'all');$('branch-filter').disabled=!domain;
 const ids=branch?.categories||domain?.categories||[];
 fillSelect('mobile-category',[['all',branch?'本分组全部':domain?'本领域全部':'全部类别'],...ids.map(id=>[id,categoryName(id)+' · '+C.get(id).count])],leaf?category:'all');$('mobile-category').disabled=!domain;
 const crumbs=[`<button data-view="directory">总目录</button>`];if(domain)crumbs.push(`<button data-category="${domain.scope}">${esc(domain.name)}</button>`);if(branch)crumbs.push(`<button data-category="${branch.scope}">${esc(branch.name)}</button>`);if(leaf)crumbs.push(`<span aria-current="page">${esc(categoryName(category))}</span>`);if(!domain)crumbs.push(`<span aria-current="page">${esc(scopeLabel())}</span>`);
 $('breadcrumb').innerHTML=crumbs.join('<span aria-hidden="true">›</span>');
 $('search-scope-label').textContent='检索范围：'+[domain?.name,branch?.name,leaf?categoryName(category):null].filter(Boolean).join(' / ')||(category==='all'?'检索范围：全部图鉴':'检索范围：'+scopeLabel());
 if(!domain)$('search-scope-label').textContent='检索范围：'+scopeLabel();
 $('search').placeholder=category==='all'?'搜索名称、编号或特征，例如：猫耳 耳机、20D…':'在“'+scopeLabel()+'”内搜索，多个关键词用空格分开';
 $('expand-search').hidden=category==='all';
 const base=getResults({style:''});const hasClothes=D.entries.some(e=>matchesCategory(e)&&clothingCategories.has(e.category));$('style-control').hidden=!hasClothes;$('extra-filters').hidden=!hasClothes&&!styleFilter;
 fillSelect('browse-style',[['','全部穿搭风格'],...D.style_families.map(f=>[f.id,f.name+' · '+base.filter(e=>clothingCategories.has(e.category)&&e.styles.includes(f.id)).length])],styleFilter);
 $('browse-sort').value=sortOrder;
 document.querySelectorAll('#categories [data-category]').forEach(b=>{const current=b.dataset.category===category;b.classList.toggle('active',current);if(current)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current')});
 document.querySelectorAll('#categories [data-domain]').forEach(d=>d.classList.toggle('is-in-path',d.dataset.domain===domain?.scope));document.querySelectorAll('#categories [data-branch]').forEach(d=>d.classList.toggle('is-in-path',d.dataset.branch===branch?.scope));
 if(sidebarCategory!==category){sidebarCategory=category;revealSidebarPath()}
 $('scope-children').hidden=!!leaf;
 $('scope-children').innerHTML=!leaf?(branch?branch.categories.map(id=>categoryButton(id,categoryName(id),C.get(id).count)).join(''):domain?domain.sections.map(s=>categoryButton(s.scope,s.name,s.count)).join(''):''):'';
}
function renderActiveFilters(){
 const chips=[];if(category!=='all')chips.push(['scope',scopeLabel()]);if(query)chips.push(['query','关键词：'+query]);if($('dimension-filter').value!=='all')chips.push(['dimension',$('dimension-filter').value]);if(styleFilter)chips.push(['style','风格：'+F.get(styleFilter).name]);
 $('active-filters').innerHTML=chips.length?`<span>当前条件</span>`+chips.map(([k,v])=>`<button data-remove-filter="${k}" aria-label="移除${esc(v)}">${esc(v)} <span aria-hidden="true">×</span></button>`).join(''):'<span>全部图鉴 · 未设置筛选</span>';
 $('filter-count').textContent=String(Number($('dimension-filter').value!=='all')+Number(!!styleFilter));
}
function renderAccessoryContext(){
 $('clothing-accessory-quicklinks').hidden=true;const show=category==='hair_with_accessories';$('styled-hair-quicklinks').hidden=!show;if(!show)return;
 $('styled-hair-quicklinks').innerHTML='<strong>按发饰看完整发型</strong>'+D.meta.hair_accessory_groups.map(g=>`<button data-styled-hair="${esc(g.name)}" aria-pressed="${$('dimension-filter').value===g.name}">${hairAccessoryLabels[g.id]}<small>${g.count}</small></button>`).join('')+`<div class="hair-motif-links"><span>发绳结构</span>${D.meta.hair_tie_motifs.map(g=>`<button data-hair-motif="${g.id}">${esc(g.name)}<small>${g.count}</small></button>`).join('')}</div>`;
}
function renderTerms(){
 resetTermAutoLoad();
 filteredEntries=sortResults(getResults());currentFilteredIds=filteredEntries.map(e=>e.id);const count=filteredEntries.length;
 $('category-title').textContent=query?'“'+query+'”的查找结果':scopeLabel();$('category-guide').textContent=C.get(category)?.guide||scopes.get(category)?.guide||'逐级选择目录，或使用关键词与筛选条件查找；每项都有对应图例。';
 $('result-status').textContent=`${count} 个结果 · 显示 ${Math.min(limit,count)} 个`;
 $('entry-grid').innerHTML=count?filteredEntries.slice(0,limit).map(entryCard).join(''):`<div class="empty" style="grid-column:1/-1"><strong>当前条件下没有结果</strong><p>可以先移除细分或风格，再扩大目录范围。</p><div class="empty-actions"><button class="btn" data-remove-filter="facets">清空筛选</button><button class="btn" data-remove-filter="scope">保留关键词，查全部图鉴</button></div></div>`;
 renderedTermCount=Math.min(limit,count);
 renderTopicContext();renderActiveFilters();renderAccessoryContext();renderWearingPreviewControls(filteredEntries);$('pose-group-index').hidden=true;$('role-kind-quicklinks').hidden=true;
 renderAgeComparison(filteredEntries);renderBodyDimensions(filteredEntries);
 renderSubdivisionNavigation();
 for(const b of document.querySelectorAll('[data-result-view]'))b.setAttribute('aria-pressed',b.dataset.resultView===view);
 if(view==='boards')renderBoards();syncURL();updateTermAutoLoad();
}
function renderBoards(){
 const ids=new Set(filteredEntries.map(e=>e.id));const boards=D.boards.map(b=>({b,items:b.items.filter(x=>ids.has(x.entry_id))})).filter(x=>x.items.length);
 $('board-results-status').textContent=`${filteredEntries.length}个匹配词条 · ${boards.length}张相关图页`;
 $('board-list').innerHTML=boards.length?boards.map(({b,items})=>`<article class="board"><h3>${esc(b.title)}</h3><p class="en">匹配 ${items.length} / ${b.items.length} 项 · 原图保留整页</p><button class="board-open" data-board="${b.id}" aria-label="放大${esc(b.title)}"><img src="${b.image}" loading="lazy" alt="${esc(b.title)}"></button><div class="caption-list">${items.map(x=>`<button data-detail="${x.entry_id}">${esc(x.label+' '+x.name)}</button>`).join('')}</div></article>`).join(''):'<div class="empty"><strong>没有匹配图页</strong><p>请移除条件或扩大目录范围。</p></div>';
}
function navigate(next){
 if(!restoring&&['terms','boards'].includes(view)&&!['terms','boards'].includes(next))lastBrowsePosition={view,scrollY:window.scrollY,category,query,styleFilter,sortOrder,mode,limit,dimension:$('dimension-filter').value,ageView,ageZoom,bodyView,bodyAxis,bodyCases:[...bodyCases]};
 if(next==='combinations'){next='card';cardTab='examples';openedCardId=null;openedSystemIndex=null}
 if(!['directory','terms','boards','references','card'].includes(next))next='directory';
 if(view!==next&&!restoring)pushRoute=true;view=next;document.body.dataset.view=next;
 if(view!=='terms')resetTermAutoLoad();
 for(const v of ['directory','terms','boards','references','card'])$(v+'-view').hidden=v!==view;
 $('browse-controls').hidden=!['terms','boards'].includes(view);
 document.querySelectorAll('.nav [data-view]').forEach(b=>{if(b.dataset.view===view||(b.dataset.view==='terms'&&view==='boards'))b.setAttribute('aria-current','page');else b.removeAttribute('aria-current')});
 if(view==='terms'||view==='boards')renderTerms();else if(view==='card'){renderCard();syncURL()}else syncURL();
 hideSuggestions();
 updateSubdivisionJump();
}
function scrollToBrowseResults(){
 requestAnimationFrame(()=>{
  if(!['terms','boards'].includes(view))return;
  const heading=$(view==='boards'?'board-results-title':'category-title');
  heading.scrollIntoView({block:'start',behavior:'instant'});
  heading.focus({preventScroll:true});
 });
}
function returnToLastBrowse(){
 const previous=lastBrowsePosition;if(!previous){navigate('terms');scrollToBrowseResults();return}
 category=previous.category;query=previous.query;styleFilter=previous.styleFilter;sortOrder=previous.sortOrder;mode=previous.mode;limit=previous.limit;ageView=previous.ageView;ageZoom=previous.ageZoom;bodyView=previous.bodyView;bodyAxis=previous.bodyAxis;bodyCases=[...previous.bodyCases];$('search').value=query;prepareDimensions(previous.dimension);navigate(previous.view);requestAnimationFrame(()=>window.scrollTo({top:previous.scrollY,behavior:'instant'}));
}
function changeCategory(next,options={}){
 const wasDirectory=view==='directory';if(S.has(next)){styleFilter=S.get(next).style_id;next='clothing'}
 category=next;const hasClothes=D.entries.some(e=>matchesCategory(e)&&clothingCategories.has(e.category));if(!hasClothes)styleFilter='';
 if(options.clearQuery||wasDirectory){query='';$('search').value=''}
 prepareDimensions();ageView='compare';bodyView='compare';if(query||styleFilter){ageView='entries';bodyView='entries'}limit=72;
 if(!restoring)pushRoute=true;navigate(options.view||(['terms','boards'].includes(view)?view:'terms'));
}
function changeStyle(id){if(!F.has(id))return;styleFilter=id;if(!D.entries.some(e=>matchesCategory(e)&&clothingCategories.has(e.category)))category='clothing';prepareDimensions($('dimension-filter').value);pushRoute=true;limit=72;navigate('terms')}
function syncURL(){
 if(restoring)return;const p=new URLSearchParams();if(view==='directory')p.set('view','directory');else if(view==='card'){p.set('view','card');if(cardTab==='examples')p.set('card_tab','examples');if(openedCardId)p.set('card',openedCardId);if(openedSystemIndex!==null)p.set('example',exampleRoute(openedSystemIndex));if(cardTab==='examples'){if(exampleTopic!=='all')p.set('example_topic',exampleTopic);if(cardListQuery)p.set('example_q',cardListQuery)}}else{p.set('section',category);if(view!=='terms')p.set('view',view)}
 if(view!=='card')for(const [k,v] of [['q',query],['style',styleFilter],['dimension',$('dimension-filter').value==='all'?'':$('dimension-filter').value],['sort',sortOrder==='directory'?'':sortOrder],['mode',mode==='all'?'':mode],['body_view',category==='body'&&bodyView==='entries'?'entries':''],['body_axis',category==='body'&&bodyAxis!=='cup'?bodyAxis:''],['body_cases',category==='body'&&bodyView==='compare'?bodyCases.join(','):''],['age_view',(category==='female_life_stages'||category==='life_stages')&&ageView==='entries'?'entries':'']])if(v)p.set(k,v);
 if($('detail-dialog').open&&currentEntryId)p.set('entry',currentEntryId);
 const u=location.pathname+'?'+p.toString();if(u!==location.pathname+location.search){history[pushRoute?'pushState':'replaceState'](null,'',u)}pushRoute=false;lastURL=u;
}
function restoreURL(){
 restoring=true;hideSuggestions();if($('detail-dialog').open)$('detail-dialog').close();
 const p=new URLSearchParams(location.search);styleFilter=F.has(p.get('style'))?p.get('style'):'';let initial=p.get('section')||'all';if(initial==='shoulders')initial='clothing';if(S.has(initial)){styleFilter=S.get(initial).style_id;initial='clothing'}
 if(initial==='expression'&&['凝视与目光方向','憋笑与忍笑变化'].includes(p.get('dimension')))initial='face_emotions';
 if(!C.has(initial)&&!G.has(initial)&&!B.has(initial)&&!scopes.has(initial)&&!['all','clothing','clothing_new'].includes(initial))initial='all';
 category=initial;if(styleFilter&&!D.entries.some(e=>matchesCategory(e)&&clothingCategories.has(e.category)))category='clothing';query=p.get('q')||'';$('search').value=query;$('directory-search').value=query;prepareDimensions(p.get('dimension')||'all');
 sortOrder=['relevance','directory','name','id'].includes(p.get('sort'))?p.get('sort'):query?'relevance':'directory';mode=p.get('mode')==='illustrated'?'illustrated':'all';limit=72;
 const filtered=!!query||!!styleFilter||$('dimension-filter').value!=='all';ageView=p.get('age_view')==='entries'||filtered?'entries':'compare';bodyView=p.get('body_view')==='entries'||filtered?'entries':'compare';bodyAxis=bodyAxes[p.get('body_axis')]?p.get('body_axis'):'cup';bodyCases=[...bodyAxes[bodyAxis].cases];const requested=(p.get('body_cases')||'').split(',').filter(k=>D.entries.some(e=>e.body_dimension_reference&&e.dimension_case===k));if(requested.length>=2&&requested.length<=8)bodyCases=requested;
 const target=p.get('view')|| (p.has('section')||query?'terms':'directory');if(target==='card'||target==='combinations')restoreAppearanceRoute(p,target==='combinations');navigate(target);
 if(p.get('entry')&&E.has(p.get('entry')))showDetail(p.get('entry'));
 restoring=false;pushRoute=false;syncURL();
}
function hideSuggestions(){for(const id of ['directory-suggestions','browse-suggestions']){const box=$(id);if(box){box.hidden=true;box.innerHTML=''}}suggestionFocus=-1;for(const id of ['directory-search','search']){$(id).setAttribute('aria-expanded','false');$(id).removeAttribute('aria-activedescendant')}}
function renderSuggestions(input,boxId,global){
 const box=$(boxId),q=input.value.trim();if(!q){hideSuggestions();return}const ts=tokensFor(q);
 const cats=D.categories.filter(c=>ts.every(t=>normalize(categoryName(c.id)+' '+c.name+' '+c.id).includes(t))).slice(0,4);
 const es=(global?D.entries.filter(e=>ts.every(t=>matchesToken(e,t))):getResults({q})).sort((a,b)=>score(b,q)-score(a,q)).slice(0,5);
 const rows=[...cats.map(c=>({kind:'category',id:c.id,name:categoryName(c.id),note:pathFor(c.id).domain.name+' / '+pathFor(c.id).branch.name})),...es.map(e=>({kind:'entry',id:e.id,name:e.name,note:e.id+' · '+categoryName(e.category)}))];
 box.innerHTML=rows.map((r,i)=>`<button type="button" role="option" id="${boxId}-${i}" data-suggest-kind="${r.kind}" data-suggest-value="${r.id}" aria-selected="false"><span>${esc(r.name)}</span><small>${esc(r.note)}</small></button>`).join('')+(rows.length?'<span class="suggestion-hint">↑ ↓ 选择 · Enter 打开 · Esc 收起</span>':'<span class="suggestion-hint">按Enter查看全部结果</span>');
 box.hidden=false;input.setAttribute('aria-expanded','true');suggestionFocus=-1;
}
function bindSuggestions(inputId,boxId,global){
 const input=$(inputId),box=$(boxId);input.addEventListener('input',()=>renderSuggestions(input,boxId,global));
 input.addEventListener('keydown',ev=>{const rows=[...box.querySelectorAll('[role="option"]')];if(ev.key==='Escape'){hideSuggestions();return}if(['ArrowDown','ArrowUp'].includes(ev.key)&&!box.hidden&&rows.length){ev.preventDefault();suggestionFocus=(suggestionFocus+(ev.key==='ArrowDown'?1:-1)+rows.length)%rows.length;rows.forEach((r,i)=>r.setAttribute('aria-selected',i===suggestionFocus));input.setAttribute('aria-activedescendant',rows[suggestionFocus].id)}else if(ev.key==='Enter'&&!box.hidden&&suggestionFocus>=0){ev.preventDefault();rows[suggestionFocus]?.click()}});
}
renderDirectory();
bindSuggestions('directory-search','directory-suggestions',true);bindSuggestions('search','browse-suggestions',false);
$('directory-search-form').addEventListener('submit',ev=>{ev.preventDefault();const q=$('directory-search').value.trim();styleFilter='';query=q;category='all';prepareDimensions();$('search').value=q;sortOrder=q?'relevance':'directory';pushRoute=true;limit=72;navigate('terms')});
$('browse-search-form').addEventListener('submit',ev=>{ev.preventDefault();hideSuggestions();renderTerms()});
$('search').addEventListener('input',()=>{query=$('search').value.trim();limit=72;if(query){sortOrder='relevance';bodyView='entries';ageView='entries'}renderTerms()});
$('clear-search').addEventListener('click',()=>{query='';$('search').value='';hideSuggestions();limit=72;renderTerms();$('search').focus()});
$('group-filter').addEventListener('change',()=>changeCategory($('group-filter').value));
$('branch-filter').addEventListener('change',()=>changeCategory($('branch-filter').value==='all'?$('group-filter').value:$('branch-filter').value));
$('mobile-category').addEventListener('change',()=>changeCategory($('mobile-category').value==='all'?$('branch-filter').value==='all'?$('group-filter').value:$('branch-filter').value:$('mobile-category').value));
$('dimension-filter').addEventListener('change',()=>{ageView='entries';bodyView='entries';limit=72;pushRoute=true;renderTerms()});
$('browse-style').addEventListener('change',()=>{styleFilter=$('browse-style').value;pushRoute=true;limit=72;renderTerms()});
$('browse-sort').addEventListener('change',()=>{sortOrder=$('browse-sort').value;mode='all';pushRoute=true;renderTerms()});
$('expand-search').addEventListener('click',()=>{category='all';styleFilter='';prepareDimensions();limit=72;pushRoute=true;renderTerms()});
$('reset-facets').addEventListener('click',()=>{query='';$('search').value='';styleFilter='';prepareDimensions();limit=72;pushRoute=true;renderTerms()});
$('reset-all').addEventListener('click',()=>{styleFilter='';query='';$('search').value='';sortOrder='directory';changeCategory('all')});
document.addEventListener('click',ev=>{
 const b=ev.target.closest('button');if(!b){if(!ev.target.closest('.search-combobox'))hideSuggestions();return}
 if(b.dataset.entryCategory&&C.has(b.dataset.entryCategory)){
  if($('detail-dialog').open)$('detail-dialog').close();
  styleFilter='';sortOrder='directory';mode='all';
  changeCategory(b.dataset.entryCategory,{clearQuery:true,view:'terms'});
  scrollToBrowseResults();
 }
 if(b.closest('.sidebar')&&(b.dataset.category||['terms','boards'].includes(b.dataset.view)))scrollToBrowseResults();
 if(b.dataset.resultView){pushRoute=true;navigate(b.dataset.resultView)}
 if(b.dataset.suggestKind){const id=b.dataset.suggestValue;query='';$('search').value='';changeCategory(b.dataset.suggestKind==='entry'?E.get(id).category:id,{clearQuery:true,view:'terms'});hideSuggestions();if(b.dataset.suggestKind==='entry')showDetail(id)}
 if(b.dataset.removeFilter){const kind=b.dataset.removeFilter;if(kind==='query'||kind==='facets'){query='';$('search').value=''}if(kind==='style'||kind==='facets')styleFilter='';if(kind==='dimension'||kind==='facets')$('dimension-filter').value='all';if(kind==='scope'){category='all';prepareDimensions()}pushRoute=true;limit=72;renderTerms()}
 if(!ev.target.closest('.search-combobox'))hideSuggestions();
});
document.addEventListener('keydown',ev=>{if($('appearance-picker').open)return;if((ev.key==='k'&&(ev.ctrlKey||ev.metaKey))||(ev.key==='/'&&!ev.ctrlKey&&!ev.altKey&&!/INPUT|TEXTAREA|SELECT/.test(ev.target.tagName))){ev.preventDefault();if(!['directory','terms','boards'].includes(view))navigate('terms');(view==='directory'?$('directory-search'):$('search')).focus()}});
const originalShowDetail=showDetail;showDetail=function(id){originalShowDetail(id);if(!restoring)pushRoute=true;syncURL()};
$('detail-dialog').addEventListener('close',()=>{if($('detail-dialog').open)return;currentEntryId=null;syncURL()});
