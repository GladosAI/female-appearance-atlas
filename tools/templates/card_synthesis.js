// A transient selection for the open card; never writes to the user's card library.
let synthesisEntryIds=[],synthesisSelected=new Set(),synthesisReturnFocus=null;
let synthesisCopyTimer;
const promptHistoryKey='female-beauty-prompt-history-v1';
let synthesisCardKey='',promptHistory=[],synthesisSessionSnapshotId=null;
try{const saved=JSON.parse(localStorage.getItem(promptHistoryKey)||'[]');if(Array.isArray(saved))promptHistory=saved.filter(x=>x&&typeof x.id==='string'&&typeof x.cardKey==='string'&&typeof x.prompt==='string'&&Array.isArray(x.selected)).slice(0,50)}catch{}
function persistPromptHistory(){try{localStorage.setItem(promptHistoryKey,JSON.stringify(promptHistory));return true}catch{toast('方案无法保存在此浏览器，请复制提示词或导出外观卡备份。');return false}}
function promptHistoryForCard(cardKey){return promptHistory.filter(snapshot=>snapshot.cardKey===cardKey)}
function importPromptHistory(records,cardMap){
 if(!Array.isArray(records))return;
 const imported=records.slice(0,50).filter(x=>x&&cardMap.has(x.cardKey)&&typeof x.prompt==='string'&&x.prompt.length<=100000&&Array.isArray(x.selected)).map(x=>({id:newAppearanceId(),cardKey:cardMap.get(x.cardKey),cardName:String(x.cardName||'').slice(0,200),selected:[...new Set(x.selected.filter(id=>typeof id==='string'))].slice(0,10000),availableIds:Array.isArray(x.availableIds)?x.availableIds.filter(id=>typeof id==='string').slice(0,10000):undefined,prompt:x.prompt,createdAt:!Number.isNaN(Date.parse(x.createdAt))?x.createdAt:new Date().toISOString()}));
 if(imported.length){promptHistory=[...imported,...promptHistory].slice(0,50);persistPromptHistory()}
}
function renderPromptHistory(){
 const history=promptHistory.filter(x=>x.cardKey===synthesisCardKey);
 $('synthesis-history-count').textContent=history.length?`方案历史 · ${history.length}`:'方案历史';
 $('synthesis-history-list').innerHTML=history.length?history.map(x=>`<option value="${esc(x.id)}">${esc(new Date(x.createdAt).toLocaleString())+' · '+x.selected.length+'项'}</option>`).join(''):'<option value="">暂无保存的方案</option>';
 $('synthesis-history-restore').disabled=!history.length;$('synthesis-history-delete').disabled=!history.length;
}
function saveSynthesisSnapshot(){
 const prompt=$('synthesis-prompt').value;if(!synthesisCardKey)return;
 const selected=synthesisEntryIds.filter(id=>synthesisSelected.has(id));
 const previous=promptHistory.find(x=>x.cardKey===synthesisCardKey);
 if(previous&&previous.prompt===prompt&&JSON.stringify(previous.selected)===JSON.stringify(selected)&&JSON.stringify(previous.availableIds||synthesisEntryIds)===JSON.stringify(synthesisEntryIds))return;
 const snapshot={id:synthesisSessionSnapshotId||newAppearanceId(),cardKey:synthesisCardKey,cardName:$('card-synthesis-card').textContent.split(' · ')[0],selected,availableIds:[...synthesisEntryIds],prompt:prompt.slice(0,100000),createdAt:new Date().toISOString()};
 synthesisSessionSnapshotId=snapshot.id;
 promptHistory=[snapshot,...promptHistory.filter(item=>item.id!==snapshot.id)].slice(0,50);
 persistPromptHistory();renderPromptHistory();
}
function applySynthesisSnapshot(snapshot,automatic=false){
 const available=Array.isArray(snapshot.availableIds)?snapshot.availableIds:null;
 const added=available?synthesisEntryIds.filter(id=>!available.includes(id)):[];
 const removed=snapshot.selected.filter(id=>!synthesisEntryIds.includes(id));
 synthesisSelected=new Set([...snapshot.selected.filter(id=>synthesisEntryIds.includes(id)),...(automatic?added:[])]);refreshSynthesisPrompt();
 // Preserve the exact manual wording instead of silently rebuilding it.
 if(!automatic||!added.length&&!removed.length){$('synthesis-prompt').value=snapshot.prompt;$('synthesis-copy-prompt').disabled=!snapshot.prompt.trim()}
 if(automatic&&(added.length||removed.length)){saveSynthesisSnapshot();toast('外观卡内容已变化，已更新选项；原提示词保留在方案历史。')}
 if(!automatic)toast(removed.length?`已恢复提示词；其中 ${removed.length} 项已不在当前卡中，历史文字保留。`:'已恢复勾选与提示词');
}
function restorePromptSnapshot(){
 const snapshot=promptHistory.find(x=>x.id===$('synthesis-history-list').value&&x.cardKey===synthesisCardKey);if(!snapshot)return;
 synthesisSessionSnapshotId=null;applySynthesisSnapshot(snapshot);saveSynthesisSnapshot();
}
function renderSynthesisReferences(){
 const entries=orderedAppearanceEntries(synthesisEntryIds,openedSystemIndex!==null);
 $('synthesis-references').innerHTML=entries.length?entries.map(e=>{const checked=synthesisSelected.has(e.id);return `<article class="synthesis-reference${checked?' is-selected':''}" data-synthesis-entry="${esc(e.id)}" title="${esc(e.name)}"><label class="synthesis-reference-toggle"><input type="checkbox" value="${esc(e.id)}" ${checked?'checked':''} aria-label="选用${esc(e.name)}"><span class="synthesis-reference-image" aria-hidden="true">${thumb(e)}</span></label><button type="button" class="synthesis-reference-name" data-detail="${esc(e.id)}" aria-label="查看${esc(e.name)}完整介绍" aria-haspopup="dialog">${esc(e.name)}</button></article>`}).join(''):'<p class="synthesis-empty">这张外观卡还没有图鉴。请先在图鉴浏览中添加部件。</p>';
 renderAppearanceSortButtons();
}
function setSynthesisCopyStatus(message='',success=false){
 clearTimeout(synthesisCopyTimer);
 const status=$('synthesis-copy-status');status.textContent=message;status.hidden=!message;status.classList.toggle('is-error',!!message&&!success);
 if(success)synthesisCopyTimer=setTimeout(()=>setSynthesisCopyStatus(),2000);
}
function synthesisTraitGroup(e){
 if(e.camera_reference||e.visual_language_reference||e.game_design_reference)return categoryName(e.category);
 if(['age','female_life_stages'].includes(e.category))return '年龄';
 if(e.category==='body')return '体型';
 if(e.category==='persona_looks')return '气质';
 if(e.category==='portrait_lighting')return '光照';
 if(e.art_style_reference||e.category.startsWith('art_'))return '画风';
 if(hairCategories.has(e.category)||e.category==='cosplay_wigs')return '发型';
 if(['pose','photo_poses','flexibility_poses','face_hands','cosplay_presentation'].includes(e.category))return '姿态';
 if(['expression','face_states','face_emotions','mouth_actions'].includes(e.category))return '表情';
 if(['eyeshadow','eyeliner','eye_makeup','lip_makeup','cosplay_looks'].includes(e.category))return '妆容';
 if(['skin','skin_details','body_art','feet','hands'].includes(e.category))return '身体特征';
 if(e.anthro_reference||['liquid_humanoids','hybrid_body_forms','quadruped_forms'].includes(e.category))return '幻想形态';
 if(e.facial_reference||['face','features','eyes','lips','nose_ear_teeth'].includes(e.category))return '面部特征';
 if(e.category==='hosiery')return '袜类';
 if(e.category==='footwear')return '鞋履';
 if(e.category==='construction')return '服装细节';
 if(['materials','clothing_prints','print_styles','palettes'].includes(e.category))return '材质与配色';
 if(clothingCategories.has(e.category)||e.category==='garment_dynamics')return '服装';
 return '配饰与道具';
}
// Only selected term names belong in the prompt; descriptions stay in entry details.
function synthesisTraitText(e){
 return e.name+(e.en?`（${e.en}）`:'');
}
function refreshSynthesisPrompt(){
 const selected=synthesisEntryIds.filter(id=>synthesisSelected.has(id));
 for(const el of $('synthesis-references').querySelectorAll('[data-synthesis-entry]')){
  const id=el.dataset.synthesisEntry,checked=synthesisSelected.has(id);
  el.classList.toggle('is-selected',checked);el.querySelector('input').checked=checked;
 }
 $('synthesis-selection-count').textContent=`已选 ${selected.length} / ${synthesisEntryIds.length} 项`;
 const groups=new Map();
 for(const id of selected){const e=E.get(id),group=synthesisTraitGroup(e);if(!groups.has(group))groups.set(group,[]);groups.get(group).push(synthesisTraitText(e))}
 const order=['年龄','体型','幻想形态','身体特征','面部特征','发型','服装','服装细节','袜类','鞋履','配饰与道具','材质与配色','妆容','表情','气质','姿态','画风','光照','观察方向','机位高度与俯仰','景别与取景范围','画面构图','景深与对焦','镜头与透视'];
 const orderedGroups=[...order,...[...groups.keys()].filter(group=>!order.includes(group))];
 const lines=orderedGroups.filter(group=>groups.has(group)).map(group=>group+'：\n'+[...new Set(groups.get(group))].map(text=>text+'；').join('\n'));
 $('synthesis-prompt').value=selected.length?'请根据以下外观词条设计女性角色。同一类别有多个选项时，将它们作为备选分别搭配，生成一张或多张角色图像。\n\n'+lines.join('\n\n'):'';
 $('synthesis-copy-prompt').disabled=!selected.length;
 $('synthesis-select-all').disabled=!synthesisEntryIds.length||selected.length===synthesisEntryIds.length;
 $('synthesis-select-none').disabled=!selected.length;
 setSynthesisCopyStatus();
}
function openCardSynthesis(){
 const system=openedSystemIndex!==null,card=system?D.combinations[openedSystemIndex]:appearanceCards.find(c=>c.id===openedCardId);if(!card)return;
 synthesisEntryIds=[...new Set((system?card.entry_ids:card.selected).filter(id=>E.has(id)))];synthesisSelected=new Set(synthesisEntryIds);
 synthesisCardKey=system?'system:'+(card.id||openedSystemIndex):card.id;
 synthesisSessionSnapshotId=null;
 synthesisReturnFocus=document.activeElement;
 $('card-synthesis-card').textContent=(card.name||'未命名外观卡')+' · '+synthesisEntryIds.length+' 个图鉴部件';
 renderSynthesisReferences();
 renderPromptHistory();$('synthesis-history').open=false;
 refreshSynthesisPrompt();const latest=promptHistory.find(snapshot=>snapshot.cardKey===synthesisCardKey);if(latest)applySynthesisSnapshot(latest,true);
 const dialog=$('card-synthesis-dialog');if(!dialog.open)dialog.showModal();dialog.scrollTop=0;$('synthesis-references').scrollTop=0;$('close-card-synthesis').focus({preventScroll:true});
}
async function copySynthesisPrompt(){
 const field=$('synthesis-prompt'),text=field.value;if(!text)return;
 let copied=false;
 try{if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(text);copied=true}}catch{}
 if(!copied){const active=document.activeElement,start=field.selectionStart,end=field.selectionEnd;field.focus({preventScroll:true});field.select();try{copied=document.execCommand('copy')}catch{}if(copied){field.setSelectionRange(start,end);active?.focus({preventScroll:true})}}
 setSynthesisCopyStatus(copied?'提示词已复制':'复制失败，请选中提示词后手动复制。',copied);
 if(copied)saveSynthesisSnapshot();
}
$('open-card-synthesis').addEventListener('click',openCardSynthesis);
$('close-card-synthesis').addEventListener('click',()=>$('card-synthesis-dialog').close());
$('synthesis-select-all').addEventListener('click',()=>{synthesisSelected=new Set(synthesisEntryIds);refreshSynthesisPrompt();saveSynthesisSnapshot()});
$('synthesis-select-none').addEventListener('click',()=>{synthesisSelected.clear();refreshSynthesisPrompt();saveSynthesisSnapshot()});
$('synthesis-references').addEventListener('change',ev=>{const input=ev.target;if(!input.matches('input[type="checkbox"]'))return;if(input.checked)synthesisSelected.add(input.value);else synthesisSelected.delete(input.value);refreshSynthesisPrompt();saveSynthesisSnapshot()});
$('synthesis-references').addEventListener('click',ev=>{
 // The image label toggles natively; the name button opens details separately.
 if(ev.target.closest('button,label,input'))return;
 ev.target.closest('[data-synthesis-entry]')?.querySelector('input').click();
});
$('synthesis-copy-prompt').addEventListener('click',copySynthesisPrompt);
$('synthesis-prompt').addEventListener('input',()=>{$('synthesis-copy-prompt').disabled=!$('synthesis-prompt').value.trim();setSynthesisCopyStatus();saveSynthesisSnapshot()});
$('card-synthesis-dialog').addEventListener('close',()=>{setSynthesisCopyStatus();if(synthesisReturnFocus?.isConnected)synthesisReturnFocus.focus({preventScroll:true})});
$('synthesis-history-restore').addEventListener('click',restorePromptSnapshot);
$('synthesis-history-delete').addEventListener('click',()=>{const id=$('synthesis-history-list').value;promptHistory=promptHistory.filter(x=>x.id!==id);persistPromptHistory();renderPromptHistory()});
$('card-synthesis-dialog').addEventListener('click',ev=>{if(ev.target!==ev.currentTarget)return;const r=ev.currentTarget.getBoundingClientRect();if(ev.clientX<r.left||ev.clientX>r.right||ev.clientY<r.top||ev.clientY>r.bottom)ev.currentTarget.close()});
document.addEventListener('click',ev=>{if($('card-synthesis-dialog').open&&ev.target.closest('button[data-entry-category],button[data-category],button[data-style],button[data-view]'))$('card-synthesis-dialog').close()});
