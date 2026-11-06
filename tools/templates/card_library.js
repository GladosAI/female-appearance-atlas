// Personal cards have their own storage. The former single-card record remains a migration backup.
// Translate presentation only; personal names, notes, IDs and stored order stay intact.
function ct(text,values={}){const translated=globalThis.AtlasI18n?.t(text)||text;return translated.replace(/\{(\w+)\}/g,(match,key)=>Object.hasOwn(values,key)?String(values[key]):match)}
function cardText(text){return globalThis.AtlasI18n?.text(text)||text}
function cardEntryName(entry){return globalThis.AtlasI18n?.entryName(entry)||entry.name}
function cardEntryText(entry,field){return globalThis.AtlasI18n?.entryText(entry,field)||entry[field]||''}
function cardEntrySearchText(entry){return [entry.id,entry.name,entry.en,cardEntryName(entry),categoryName(entry.category)].join(' ').normalize('NFKC').toLocaleLowerCase()}
function cardEnglishName(entry){return entry.en!==cardEntryName(entry)?`<p class="en" lang="en">${esc(entry.en)}</p>`:''}
const cardLibraryKey='female-beauty-appearance-library-v2';
let appearanceCards=[],lastAddedCardId=null,openedCardId=null,openedSystemIndex=null,editingAppearanceId=null,cardTab='mine',cardListQuery='';
let lastCardChange=null,pendingCardAction=null,libraryStorageProblem='',libraryWriteBlocked=false;
let appearancePickerEntryId=null,appearancePickerCardId=null,appearancePickerAnchor=null;
let cardEntrySort='recent';
let exampleTopic='all';
function systemExamples(){return D.combinations.map((card,index)=>({card,index})).filter(({card})=>!card.archived)}
function exampleRoute(index){return D.combinations[index]?.id||String(index+1)}
function exampleSearchText(card){return [card.id,card.name,cardText(card.name),card.description,cardText(card.description),...(card.tags||[]).flatMap(tag=>[tag,cardText(tag)]),card.chapter_name,cardText(card.chapter_name),card.palette,...card.entry_ids.flatMap(id=>{const e=E.get(id);return e?[cardEntrySearchText(e)]:[]})].filter(Boolean).join(' ').normalize('NFKC').toLocaleLowerCase()}
function filteredSystemExamples(){const q=cardListQuery.trim().normalize('NFKC').toLocaleLowerCase();return systemExamples().filter(({card})=>(exampleTopic==='all'||exampleTopic==='recommended'&&card.featured||card.chapter===exampleTopic)&&(!q||exampleSearchText(card).includes(q)))}
function renderExampleTopics(){
 const options=[{id:'all',name:'全部角色'},{id:'recommended',name:'精选角色'},...(D.example_chapters||[]).map(c=>({id:c.id,name:c.name}))];
 const all=systemExamples();$('system-example-topics').innerHTML=options.map(option=>{const count=all.filter(({card})=>option.id==='all'||option.id==='recommended'&&card.featured||card.chapter===option.id).length;return `<button type="button" data-example-topic="${esc(option.id)}" aria-pressed="${exampleTopic===option.id}">${esc(cardText(option.name))} <span>${count}</span></button>`}).join('');
}
function exampleNavigationScope(){const filtered=filteredSystemExamples();return filtered.some(item=>item.index===openedSystemIndex)?filtered:systemExamples()}
function renderExampleNavigation(card,system){
 const visible=system&&card.character_example;$('system-example-navigation').hidden=!visible;if(!visible)return;
 const scope=exampleNavigationScope(),position=scope.findIndex(item=>item.index===openedSystemIndex);
 $('system-example-position').textContent=(position+1)+' / '+scope.length;
 for(const button of document.querySelectorAll('[data-example-step]'))button.disabled=position+Number(button.dataset.exampleStep)<0||position+Number(button.dataset.exampleStep)>=scope.length;
}
function orderedAppearanceEntries(ids,system=false){
 const positions=new Map(ids.map((id,index)=>[id,index]));
 const entries=ids.map(id=>E.get(id)).filter(Boolean);
 const byAdded=(a,b)=>system?positions.get(a.id)-positions.get(b.id):positions.get(b.id)-positions.get(a.id);
 if(cardEntrySort==='category')entries.sort((a,b)=>(categoryOrder.get(a.category)??Number.MAX_SAFE_INTEGER)-(categoryOrder.get(b.category)??Number.MAX_SAFE_INTEGER)||a.category.localeCompare(b.category)||byAdded(a,b));
 else if(!system)entries.reverse();
 return entries;
}
function renderAppearanceSortButtons(){
 const system=openedSystemIndex!==null;
 document.querySelectorAll('[data-card-sort-toggle]').forEach(button=>{
  button.textContent=ct(cardEntrySort==='category'?'按类别排序':system?'按示例顺序 ↓':'按加入时间 ↓');
  button.title=ct(cardEntrySort==='category'?(system?'切换为示例顺序':'切换为加入时间排序（新到旧）'):'切换为按类别排序');
  button.setAttribute('aria-label',button.textContent+' · '+button.title);
 });
}
function newAppearanceId(){return 'card-'+(globalThis.crypto?.randomUUID?.()||Date.now().toString(36)+'-'+Math.random().toString(36).slice(2))}
function cleanAppearanceCard(value){
 if(!value||typeof value!=='object'||!Array.isArray(value.selected))throw Error(ct('外观卡缺少部件列表'));
 return {id:typeof value.id==='string'&&/^[a-zA-Z0-9_-]{1,120}$/.test(value.id)?value.id:newAppearanceId(),name:String(value.name||ct('未命名外观卡')).slice(0,200),notes:String(value.notes||'').slice(0,10000),selected:[...new Set(value.selected.filter(id=>typeof id==='string'&&E.has(id)))],createdAt:String(value.createdAt||new Date().toISOString()).slice(0,64),updatedAt:String(value.updatedAt||new Date().toISOString()).slice(0,64)};
}
function saveAppearanceLibrary(){
 if(libraryWriteBlocked)return false;
 try{localStorage.setItem(cardLibraryKey,JSON.stringify({schema:'female-appearance-library/v2',activeId:lastAddedCardId,lastAddedCardId,cards:appearanceCards}));libraryStorageProblem='';queueMicrotask(renderLibraryBackupStatus);return true}
 catch{libraryStorageProblem=ct('浏览器暂时无法保存。请使用“备份全部”或导出单张外观卡，保留本次内容。');return false}
}
function persistOpenedAppearance(){
 const card=appearanceCards.find(c=>c.id===openedCardId);if(!card)return;
 card.name=$('card-name').value.slice(0,200);card.notes=$('card-notes').value.slice(0,10000);card.updatedAt=new Date().toISOString();
 const saved=saveAppearanceLibrary();renderCardStorageNotice();if(!saved)toast(libraryStorageProblem);$('appearance-card-title').textContent=card.name||ct('未命名外观卡');updateCounts();
}
function initializeAppearanceLibrary(){
 let raw=null;
 try{raw=localStorage.getItem(cardLibraryKey)}catch{libraryStorageProblem=ct('浏览器暂时无法读取本机存储；编辑后请导出备份。')}
 if(raw!==null){
  try{const library=JSON.parse(raw);if(library.schema!=='female-appearance-library/v2'||!Array.isArray(library.cards))throw Error('格式不匹配');const used=new Set();appearanceCards=library.cards.map(value=>{const c=cleanAppearanceCard(value);if(used.has(c.id))c.id=newAppearanceId();used.add(c.id);return c});const recent=Object.hasOwn(library,'lastAddedCardId')?library.lastAddedCardId:library.activeId;lastAddedCardId=appearanceCards.some(c=>c.id===recent)?recent:null}
  catch{libraryWriteBlocked=true;libraryStorageProblem=ct('本机外观卡记录无法读取，原始数据已保留。本次编辑请导出备份，避免丢失。')}
 }else{
  try{const old=JSON.parse(localStorage.getItem(key)||'null');if(old){const card=cleanAppearanceCard(old);appearanceCards=[card];lastAddedCardId=card.id;saveAppearanceLibrary()}}catch{libraryStorageProblem=ct('旧版外观卡暂时无法读取，原始记录已保留；可从导出的文件恢复。')}
 }
}
function renderCardStorageNotice(){const notice=$('card-storage-notice');notice.hidden=!libraryStorageProblem;notice.textContent=libraryStorageProblem;queueMicrotask(renderLibraryBackupStatus)}
function appearanceMembership(id){return appearanceCards.filter(c=>c.selected.includes(id)).length}
function saveEntryButton(id,className='small-btn'){const count=appearanceMembership(id);return `<button type="button" class="${className}" data-save="${esc(id)}" aria-haspopup="dialog" title="${esc(count?ct('已加入 {count} 张外观卡，点击选择其他卡片',{count}):ct('选择要加入的外观卡'))}">${esc(ct(count?'✓ 外观卡':'＋ 外观卡'))}</button>`}
function refreshSaveButtons(){document.querySelectorAll('[data-save]').forEach(b=>{const count=appearanceMembership(b.dataset.save);b.removeAttribute('aria-pressed');b.setAttribute('aria-haspopup','dialog');b.textContent=ct(count?'✓ 外观卡':'＋ 外观卡');b.title=count?ct('已加入 {count} 张外观卡，点击选择其他卡片',{count}):ct('选择要加入的外观卡')})}
function positionAppearancePicker(){
 const dialog=$('appearance-picker');if(!dialog.open||!appearancePickerAnchor?.isConnected)return;
 const anchor=appearancePickerAnchor.getBoundingClientRect(),box=dialog.getBoundingClientRect(),width=window.innerWidth,height=window.innerHeight;
 const left=width<=560?(width-box.width)/2:Math.max(12,Math.min(anchor.right-box.width,width-box.width-12));
 const top=height-anchor.bottom>=box.height+20?anchor.bottom+8:anchor.top>=box.height+20?anchor.top-box.height-8:Math.max(12,(height-box.height)/2);
 dialog.style.left=Math.round(Math.max(12,left))+'px';dialog.style.top=Math.round(Math.min(Math.max(12,top),Math.max(12,height-box.height-12)))+'px';
}
function renderAppearancePickerOptions(){
 const query=$('appearance-picker-search').value.trim().toLocaleLowerCase();
 const cards=[...appearanceCards].sort((a,b)=>Number(b.id===lastAddedCardId)-Number(a.id===lastAddedCardId)).filter(c=>!query||c.name.toLocaleLowerCase().includes(query));
 if(appearancePickerCardId!=='__new__'&&!cards.some(c=>c.id===appearancePickerCardId))appearancePickerCardId=cards[0]?.id||null;
 $('appearance-picker-options').innerHTML=cards.map(c=>{const included=c.selected.includes(appearancePickerEntryId);return `<label class="appearance-picker-choice"><input type="radio" name="appearance-destination" value="${esc(c.id)}" ${c.id===appearancePickerCardId?'checked':''}><span><strong data-i18n-skip>${esc(c.name||ct('未命名外观卡'))}</strong><small>${esc(ct('{count} 项',{count:c.selected.length}))}${c.id===lastAddedCardId?' · '+esc(ct('最近添加')):''}${included?' · ✓ '+esc(ct('已包含此图鉴')):''}</small></span></label>`}).join('')+(cards.length?'':'<p class="appearance-picker-empty">'+esc(ct(query?'没有找到这张卡':'先新建一张外观卡'))+'</p>');
 $('appearance-picker-new').checked=appearancePickerCardId==='__new__';
 updateAppearancePickerSelection();
}
function updateAppearancePickerSelection(){
 const isNew=appearancePickerCardId==='__new__',card=appearanceCards.find(c=>c.id===appearancePickerCardId),included=card?.selected.includes(appearancePickerEntryId);
 $('appearance-picker-name-wrap').hidden=!isNew;const confirm=$('appearance-picker-add');
 confirm.disabled=isNew?!$('appearance-picker-name').value.trim():!card||included;
 confirm.textContent=isNew?ct('新建并添加'):!card?ct('请选择外观卡'):ct(included?'已在「{name}」中':'添加到「{name}」',{name:card.name||ct('未命名外观卡')});
 confirm.title=confirm.textContent;positionAppearancePicker();
}
function openAppearancePicker(id,anchor){
 if(!E.has(id))return;
 appearancePickerEntryId=id;appearancePickerAnchor=anchor;appearancePickerCardId=appearanceCards.some(c=>c.id===lastAddedCardId)?lastAddedCardId:appearanceCards[0]?.id||'__new__';
 $('appearance-picker-entry').textContent=cardEntryName(E.get(id))+' · '+id;
 $('appearance-picker-search').value='';$('appearance-picker-search-wrap').hidden=appearanceCards.length<6;
 $('appearance-picker-name').value=ct('外观卡 {number}',{number:appearanceCards.length+1});renderAppearancePickerOptions();
 const dialog=$('appearance-picker');if(!dialog.open)dialog.showModal();positionAppearancePicker();
 const focus=appearancePickerCardId==='__new__'?$('appearance-picker-name'):$('appearance-picker-add').disabled?dialog.querySelector('input:checked'):$('appearance-picker-add');focus?.focus({preventScroll:true});
}
function closeAppearancePicker(){if($('appearance-picker').open)$('appearance-picker').close()}
function addAppearancePickerEntry(){
 if(!E.has(appearancePickerEntryId)||$('appearance-picker-add').disabled)return;
 let card=appearanceCards.find(c=>c.id===appearancePickerCardId);
 if(appearancePickerCardId==='__new__'){const name=$('appearance-picker-name').value.trim();if(!name)return;card=createAppearanceCard({name},false)}
 if(!card||card.selected.includes(appearancePickerEntryId))return;
 card.selected.push(appearancePickerEntryId);card.updatedAt=new Date().toISOString();lastAddedCardId=card.id;
 const saved=saveAppearanceLibrary();closeAppearancePicker();updateCounts();refreshSaveButtons();renderCardStorageNotice();if(view==='card')renderCard();
 toast(saved?ct('已加入「{name}」',{name:card.name||ct('未命名外观卡')}):libraryStorageProblem);
}
function updateCounts(){
 $('saved-count').textContent=appearanceCards.length;
 $('personal-card-total').textContent=appearanceCards.length;
}
function createAppearanceCard(values={},save=true){const card=cleanAppearanceCard({name:ct('外观卡 {number}',{number:appearanceCards.length+1}),notes:'',selected:[],...values,id:newAppearanceId()});appearanceCards.push(card);if(save){const saved=saveAppearanceLibrary();updateCounts();renderCardStorageNotice();if(!saved)toast(libraryStorageProblem)}return card}
function scrollToAppearanceHeading(detail=false){requestAnimationFrame(()=>{if(view!=='card')return;const title=$(detail?'appearance-card-title':'library-title');title.scrollIntoView({block:'start',behavior:'instant'});title.focus({preventScroll:true})})}
function openCardLibrary(tab='mine',scroll=true,preserve=false){cardTab=tab==='examples'?'examples':'mine';openedCardId=null;openedSystemIndex=null;editingAppearanceId=null;if(!preserve){cardListQuery='';exampleTopic='all';$('card-library-search').value=''}if(!restoring)pushRoute=true;navigate('card');if(scroll)scrollToAppearanceHeading()}
function openAppearanceCard(id,scroll=true,edit=false){if(!appearanceCards.some(c=>c.id===id))return;cardTab='mine';openedSystemIndex=null;openedCardId=id;editingAppearanceId=edit?id:null;if(!restoring)pushRoute=true;navigate('card');if(scroll)scrollToAppearanceHeading(true)}
function openSystemAppearance(index,scroll=true){if(!Number.isInteger(index)||!D.combinations[index])return;cardTab='examples';openedCardId=null;openedSystemIndex=index;editingAppearanceId=null;if(!restoring)pushRoute=true;navigate('card');if(scroll)scrollToAppearanceHeading(true)}
function restoreAppearanceRoute(params,legacy=false){
 cardTab=legacy||params.get('card_tab')==='examples'?'examples':'mine';openedCardId=null;openedSystemIndex=null;editingAppearanceId=null;cardListQuery='';$('card-library-search').value='';
 const id=params.get('card');if(appearanceCards.some(c=>c.id===id)){cardTab='mine';openedCardId=id}
 const topic=params.get('example_topic');exampleTopic=topic==='recommended'||D.example_chapters?.some(c=>c.id===topic)?topic:'all';
 const query=params.get('example_q');if(cardTab==='examples'&&query){cardListQuery=query.slice(0,500);$('card-library-search').value=cardListQuery}
 const example=params.get('example'),index=example&&/^\d+$/.test(example)?Number(example)-1:D.combinations.findIndex(card=>card.id===example);if(example&&D.combinations[index]){openedCardId=null;cardTab='examples';openedSystemIndex=index}
}
function cardCover(ids){const entries=ids.map(id=>E.get(id)).filter(e=>e?.visual).slice(0,3);return entries.length?`<span class="appearance-card-cover" aria-hidden="true">${entries.map(e=>`<span class="appearance-card-cover-part">${thumb(e)}</span>`).join('')}</span>`:'<span class="appearance-card-cover is-empty" aria-hidden="true">＋</span>'}
function appearanceCardTile(card,index,system=false){const ids=system?card.entry_ids:card.selected,notes=system?cardText(card.description):card.notes,active=!system&&card.id===lastAddedCardId;return `<button type="button" class="appearance-card-tile${active?' is-active':''}" ${system?`data-open-system-card="${index}"`:`data-open-appearance-card="${esc(card.id)}"`}>${cardCover(ids)}<span class="appearance-card-tile-copy">${system&&card.character_example?`<span class="example-kind">${esc(cardText(card.chapter_name))}${card.tags?.length?' · '+esc(cardText(card.tags[0])):''}</span>`:''}<strong data-i18n-skip>${esc((system?cardText(card.name):card.name)||ct('未命名外观卡'))}</strong><small data-i18n-skip>${esc(notes||ct('还没有设定备注，打开后可编辑。'))}</small><span class="appearance-card-tile-meta"><span>${esc(ct('{count} 项参考',{count:ids.length}))}</span><b>${esc(ct(system?'打开示例 ↗':active?'最近添加 · 打开 ↗':'打开外观卡 ↗'))}</b></span></span></button>`}
function renderAppearanceCardList(){
 const system=cardTab==='examples',all=system?systemExamples():appearanceCards,q=cardListQuery.trim().normalize('NFKC').toLocaleLowerCase(),cards=system?filteredSystemExamples():all.map((card,index)=>({card,index})).filter(({card})=>!q||[card.name,card.notes,...card.selected.map(id=>E.get(id)).filter(Boolean).map(cardEntrySearchText)].filter(Boolean).join(' ').normalize('NFKC').toLocaleLowerCase().includes(q));
 $('system-example-topics').hidden=!system;if(system)renderExampleTopics();
 $('card-library-search').placeholder=ct(system?'查找角色、身份、气质或外观特征':'查找名称、设定或部件');
 document.querySelectorAll('[data-card-tab]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.cardTab===cardTab)));
 $('card-library-summary').textContent=system?ct('{count} 张角色卡 · 每张一个人物设定，可另存后自由修改',{count:all.length})+(q||exampleTopic!=='all'?' · '+ct('当前 {count} 张',{count:cards.length}):''):ct('{count} 张个人外观卡 · 每张独立保存，点击图鉴的“＋ 外观卡”选择加入哪张',{count:all.length})+(q?' · '+ct('找到 {count} 张',{count:cards.length}):'');
 $('appearance-card-list').innerHTML=cards.length?cards.map(({card,index})=>appearanceCardTile(card,index,system)).join(''):`<div class="empty" style="grid-column:1/-1"><strong>${q?'没有找到匹配的外观卡':'为第一个角色建立外观卡'}</strong><p>${q?'试试其他名称或部件关键词。':'新建一张空白卡，或从系统示例中挑选一套作为起点。'}</p>${q?'':'<div class="empty-actions"><button type="button" class="btn primary" data-card-action="new">新建外观卡</button><button type="button" class="btn" data-card-tab="examples">浏览系统示例</button></div>'}</div>`;
}
function appearanceGalleryEntry(e,system){return `<article class="entry card-gallery-entry"><button type="button" class="image-button" data-detail="${e.id}" aria-label="${esc(ct('查看{name}',{name:cardEntryName(e)}))}">${thumb(e)}</button><div class="entry-body"><div class="meta"><span>${esc(e.id)}</span>${entryCategoryTag(e)}</div><button type="button" class="title-button" data-detail="${e.id}">${esc(cardEntryName(e))}</button>${cardEnglishName(e)}${sequenceNote(e)}<p class="desc">${esc(cardEntryText(e,'description'))}</p></div><div class="entry-foot"><button type="button" class="small-btn" data-detail="${e.id}">${esc(ct('查看图鉴要点 ↗'))}</button>${system?'':`<button type="button" class="small-btn" data-remove-card-entry="${e.id}">${esc(ct('移出这张卡'))}</button>`}</div></article>`}
function renderCard(){
 updateCounts();renderCardStorageNotice();$('card-undo').hidden=!lastCardChange;if(lastCardChange)$('card-undo-message').textContent=ct(lastCardChange.kind==='delete'?'已删除「{name}」':'已清空「{name}」的部件',{name:lastCardChange.card.name});
 const system=openedSystemIndex!==null,card=system?D.combinations[openedSystemIndex]:appearanceCards.find(c=>c.id===openedCardId),detail=!!card;
 $('card-library-home').hidden=detail;$('card-library-detail').hidden=!detail;$('card-view').classList.toggle('has-open-card',detail);
 if(!detail){renderAppearanceCardList();return}
 const ids=system?card.entry_ids:card.selected,entries=orderedAppearanceEntries(ids,system);currentFilteredIds=entries.map(e=>e.id);
 renderAppearanceSortButtons();
 const editing=!system&&editingAppearanceId===card.id;$('card-source-label').textContent=system?(card.archived?ct('旧版系统示例'):ct('角色卡')+' · '+cardText(card.chapter_name)):ct('我的外观卡');$('appearance-card-title').textContent=(system?cardText(card.name):card.name)||ct('未命名外观卡');$('card-count').textContent=ct('{count} 项参考',{count:entries.length})+' · '+ct(system?'另存后可自由修改':'修改自动保存');
 const notes=system?[cardText(card.description),card.palette?ct('配色：{palette}',{palette:cardText(card.palette)}):''].filter(Boolean).join('\n'):editing?'':card.notes;$('card-notes-preview').textContent=notes;$('card-notes-preview').hidden=!notes;
 renderExampleNavigation(card,system);
 $('card-settings').hidden=!editing;if(!system){$('card-name').value=card.name;$('card-notes').value=card.notes}
 $('card-detail-actions').innerHTML=system?'<button type="button" class="btn primary" data-card-action="save-example">保存为我的外观卡</button>':`<button type="button" class="btn${editing?' primary':''}" data-card-action="edit" aria-expanded="${editing}" aria-controls="card-settings">${editing?'完成编辑':'编辑'}</button>`+'<button type="button" class="btn" data-card-action="duplicate">复制一张</button><button type="button" class="btn" data-card-action="export-card">导出这张卡</button><span class="card-danger-actions"><button type="button" class="btn" data-card-action="clear"'+(entries.length?'':' disabled')+'>清空部件</button><button type="button" class="btn" data-card-action="delete">删除外观卡</button></span>';
 $('selected-grid').innerHTML=entries.length?entries.map(e=>appearanceGalleryEntry(e,system)).join(''):'<div class="empty" style="grid-column:1/-1"><strong>这张卡还没有图鉴部件</strong><p>浏览发型、服装、五官或姿态，点击“＋ 外观卡”并选择这张卡。</p><button type="button" class="btn primary" data-card-action="browse">去图鉴挑选 ↗</button></div>';
}
function deleteOpenedAppearance(cardId=openedCardId){
 const index=appearanceCards.findIndex(c=>c.id===cardId);if(index<0)return;lastCardChange={kind:'delete',card:appearanceCards[index],index,wasRecent:lastAddedCardId===cardId};appearanceCards.splice(index,1);if(lastAddedCardId===cardId)lastAddedCardId=null;saveAppearanceLibrary();refreshSaveButtons();openCardLibrary('mine');
}
function undoAppearanceChange(){if(!lastCardChange)return;const change=lastCardChange;if(change.kind==='delete'){appearanceCards.splice(Math.min(change.index,appearanceCards.length),0,change.card);if(change.wasRecent&&!lastAddedCardId)lastAddedCardId=change.card.id}else{const card=appearanceCards.find(c=>c.id===change.card.id);if(!card)return;card.selected=[...change.selected];card.updatedAt=new Date().toISOString()}lastCardChange=null;saveAppearanceLibrary();refreshSaveButtons();openAppearanceCard(change.card.id)}
function requestCardAction(action){const card=appearanceCards.find(c=>c.id===openedCardId);if(!card)return;if(action==='clear'&&!card.selected.length)return;pendingCardAction={action,cardId:card.id};$('card-action-title').textContent=ct(action==='delete'?'删除「{name}」？':'清空「{name}」的部件？',{name:card.name||ct('未命名外观卡')});$('card-action-message').textContent=action==='delete'?ct('这会删除整张外观卡及其中的部件记录。确认后仍可在页面中撤销。'):ct('这会移出全部 {count} 个部件，名称和角色设定保留。确认后仍可撤销。',{count:card.selected.length});$('card-action-confirm').textContent=ct(action==='delete'?'确认删除外观卡':'确认清空部件');$('card-action-dialog').showModal()}
function clearAppearanceParts(cardId){const card=appearanceCards.find(c=>c.id===cardId);if(!card)return;lastCardChange={kind:'clear',card:{id:card.id,name:card.name},selected:[...card.selected]};card.selected=[];card.updatedAt=new Date().toISOString();saveAppearanceLibrary();refreshSaveButtons();renderCard()}
function removeOpenedAppearancePart(id){const card=appearanceCards.find(c=>c.id===openedCardId);if(!card)return;card.selected=card.selected.filter(value=>value!==id);card.updatedAt=new Date().toISOString();saveAppearanceLibrary();refreshSaveButtons();renderCard()}
function exportAppearanceLibrary(){const payload=appearanceBackupPayload(),exportedAt=new Date().toISOString();download(JSON.stringify({...payload,exported_at:exportedAt},null,2),ct('女性之美-全部外观卡')+'.json');recordLibraryExport(payload,exportedAt);toast(ct('已开始导出全部 {count} 张外观卡及方案历史，请确认文件已保存。',{count:appearanceCards.length}))}
function exportOpenedAppearance(){const card=appearanceCards.find(c=>c.id===openedCardId);if(!card)return;download(JSON.stringify({schema:'female-appearance-card/v1',catalog_version:D.meta.version,source_card_id:card.id,name:card.name,notes:card.notes,selected:card.selected,entries:card.selected.map(id=>E.get(id)),prompt_history:promptHistoryForCard(card.id)},null,2),(card.name||ct('角色外观卡')).replace(/[\\/:*?"<>|]/g,'_')+'.json');toast(ct('这张外观卡及方案历史已导出。'))}
function importAppearancePayload(payload){
 let source;if(payload?.schema==='female-appearance-card/v1')source=[payload];else if(payload?.schema==='female-appearance-library/v2'&&Array.isArray(payload.cards))source=payload.cards;else throw Error(ct('外观卡格式不匹配'));
 if(!source.length)throw Error(ct('备份中没有外观卡'));if(source.length>1000)throw Error(ct('单次最多导入1000张外观卡'));
 const imported=source.map(cleanAppearanceCard).map(c=>({...c,id:newAppearanceId()}));appearanceCards.push(...imported);const saved=saveAppearanceLibrary();
 const cardMap=new Map(source.map((card,index)=>[card.id||payload.source_card_id,imported[index].id]));importPromptHistory(payload.prompt_history,cardMap);
 updateCounts();refreshSaveButtons();renderCardStorageNotice();if(!saved)toast(libraryStorageProblem);return imported;
}
$('card-library-search').addEventListener('input',()=>{cardListQuery=$('card-library-search').value;renderAppearanceCardList();syncURL()});
$('appearance-picker-form').addEventListener('submit',ev=>{ev.preventDefault();addAppearancePickerEntry()});
$('appearance-picker').addEventListener('change',ev=>{if(ev.target.name!=='appearance-destination')return;appearancePickerCardId=ev.target.value;updateAppearancePickerSelection();if(appearancePickerCardId==='__new__')$('appearance-picker-name').focus({preventScroll:true})});
$('appearance-picker-search').addEventListener('input',renderAppearancePickerOptions);
$('appearance-picker-search').addEventListener('keydown',ev=>{if(ev.key==='Enter')ev.preventDefault()});
$('appearance-picker-name').addEventListener('input',updateAppearancePickerSelection);
$('appearance-picker-close').addEventListener('click',closeAppearancePicker);
$('appearance-picker').addEventListener('click',ev=>{if(ev.target!==$('appearance-picker'))return;const box=ev.target.getBoundingClientRect();if(ev.clientX<box.left||ev.clientX>box.right||ev.clientY<box.top||ev.clientY>box.bottom)closeAppearancePicker()});
$('appearance-picker').addEventListener('close',()=>{const anchor=appearancePickerAnchor;appearancePickerEntryId=null;appearancePickerCardId=null;appearancePickerAnchor=null;if(anchor?.isConnected)anchor.focus({preventScroll:true})});
window.addEventListener('resize',positionAppearancePicker);
$('card-name').addEventListener('input',persistOpenedAppearance);$('card-notes').addEventListener('input',persistOpenedAppearance);
$('card-action-cancel').addEventListener('click',()=>{pendingCardAction=null;$('card-action-dialog').close()});
$('card-action-dialog').addEventListener('cancel',()=>{pendingCardAction=null});
$('card-action-confirm').addEventListener('click',()=>{const pending=pendingCardAction;pendingCardAction=null;$('card-action-dialog').close();if(!pending)return;if(pending.action==='delete')deleteOpenedAppearance(pending.cardId);else clearAppearanceParts(pending.cardId)});
$('import-card').addEventListener('click',()=>$('import-file').click());
$('import-file').addEventListener('change',async()=>{const file=$('import-file').files[0];if(!file)return;try{if(file.size>20e6)throw Error(ct('文件超过20MB'));const cards=importAppearancePayload(JSON.parse(await file.text()));openAppearanceCard(cards[0].id);toast(ct('已新增导入 {count} 张外观卡，原有卡片保留。',{count:cards.length}))}catch(error){toast(ct('无法导入：{message}',{message:error.message}))}finally{$('import-file').value=''}});
document.addEventListener('click',ev=>{
 const b=ev.target.closest('button');if(!b)return;
 if(b.dataset.exampleTopic){exampleTopic=b.dataset.exampleTopic;renderAppearanceCardList();syncURL();return}
 if(b.dataset.exampleStep){const scope=exampleNavigationScope(),position=scope.findIndex(item=>item.index===openedSystemIndex),next=scope[position+Number(b.dataset.exampleStep)];if(next)openSystemAppearance(next.index);return}
 if(b.hasAttribute('data-card-sort-toggle')){cardEntrySort=cardEntrySort==='recent'?'category':'recent';renderCard();if($('card-synthesis-dialog').open)renderSynthesisReferences();return}
 if(b.dataset.cardTab)openCardLibrary(b.dataset.cardTab,false);
 if(b.dataset.openAppearanceCard)openAppearanceCard(b.dataset.openAppearanceCard);
 if(b.dataset.openSystemCard!==undefined)openSystemAppearance(Number(b.dataset.openSystemCard));
 if(b.dataset.removeCardEntry)removeOpenedAppearancePart(b.dataset.removeCardEntry);
 const action=b.dataset.cardAction;if(!action)return;
 if(action==='new'){const card=createAppearanceCard();openAppearanceCard(card.id,true,true)}
 if(action==='edit'&&openedCardId){editingAppearanceId=editingAppearanceId===openedCardId?null:openedCardId;renderCard();(editingAppearanceId?$('card-name'):$('card-detail-actions').querySelector('[data-card-action="edit"]')).focus({preventScroll:true})}
 if(action==='back')openCardLibrary(cardTab,true,true);
 if(action==='browse')returnToLastBrowse();
 if(action==='duplicate'){const source=appearanceCards.find(c=>c.id===openedCardId);if(source){const card=createAppearanceCard({...source,name:(source.name+' · '+ct('副本')).slice(0,200),createdAt:new Date().toISOString()});openAppearanceCard(card.id)}}
 if(action==='save-example'){const source=D.combinations[openedSystemIndex];if(source){const card=createAppearanceCard({name:cardText(source.name),notes:[cardText(source.description),source.palette?ct('配色：{palette}',{palette:cardText(source.palette)}):''].filter(Boolean).join('\n'),selected:source.entry_ids});openAppearanceCard(card.id);toast(ct('已保存为独立外观卡，可以继续编辑。'))}}
 if(action==='delete'||action==='clear')requestCardAction(action);if(action==='undo')undoAppearanceChange();
 if(action==='export-library')exportAppearanceLibrary();if(action==='export-card')exportOpenedAppearance();
});
initializeAppearanceLibrary();
