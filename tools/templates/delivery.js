const detailLoads=new Map();let detailRequestSerial=0;
function ensureEntryDetails(entry){
 const web=window.ATLAS_WEB,domain=web?.detailDomains[entry.category];
 if(!domain)return Promise.resolve();
 if(detailLoads.has(domain))return detailLoads.get(domain);
 const pending=new Promise((resolve,reject)=>{
  const script=document.createElement('script');script.src=web.detailChunks[domain];
  script.onload=()=>{
   try{
    const records=globalThis.__atlasDetailChunks?.[domain];
    if(!Array.isArray(records)||!records.some(record=>record.id===entry.id))throw Error('词条资料不完整');
    for(const record of records){const target=E.get(record.id);if(!target||web.detailDomains[target.category]!==domain)throw Error('词条资料版本不匹配')}
    for(const record of records)Object.assign(E.get(record.id),record);
    delete globalThis.__atlasDetailChunks[domain];resolve();
   }catch(error){reject(error)}finally{script.remove()}
  };
  script.onerror=()=>{script.remove();reject(Error('详细资料加载失败，请检查网络后重试。'))};
  document.head.append(script);
 });
 detailLoads.set(domain,pending);pending.catch(()=>{if(detailLoads.get(domain)===pending)detailLoads.delete(domain)});
 return pending;
}
async function showDetail(id){
 const entry=E.get(id);if(!entry)return;
 const serial=++detailRequestSerial;currentEntryId=id;
 if(window.ATLAS_WEB){
  $('detail-heading').textContent=entry.id+' · '+categoryName(entry.category);
  $('detail-content').setAttribute('aria-busy','true');
  $('detail-content').innerHTML=`<div class="detail-copy" role="status" aria-live="polite"><h2>${esc(entry.name)}</h2><p>正在读取详细资料…</p></div>`;
  if(!$('detail-dialog').open)$('detail-dialog').showModal();
  try{await ensureEntryDetails(entry)}catch(error){
   if(serial===detailRequestSerial&&currentEntryId===id&&$('detail-dialog').open){$('detail-content').setAttribute('aria-busy','false');$('detail-content').innerHTML=`<div class="detail-copy" role="alert"><h2>${esc(entry.name)}</h2><p>${esc(error.message)}</p><button class="btn" data-detail="${esc(id)}">重新加载</button></div>`}
   return;
  }
  if(serial!==detailRequestSerial||currentEntryId!==id||!$('detail-dialog').open)return;
 }
 $('detail-content').setAttribute('aria-busy','false');
 showDetailContent(id);
}
function entryIssueURL(entry){
 const version=window.ATLAS_BUILD||D.app_release||{};
 const link=new URL('https://gladosai.github.io/female-appearance-atlas/');
 link.search=new URLSearchParams({section:entry.category,entry:entry.id});
 const body=['词条：'+entry.id+' · '+entry.name,'类别：'+categoryName(entry.category),
  '内容版本：'+D.meta.version,'程序版本：'+(version.app_version||'未知'),
  '源码提交：'+(version.source_commit||'未记录'),'图片资源版本：'+(version.image_release||'未知'),
  '词条链接：'+link.href,'','问题描述：','','期望修改：','','补充截图或来源（如有）：'].join('\n');
 const url=new URL('https://github.com/GladosAI/female-appearance-atlas/issues/new');
 url.search=new URLSearchParams({template:'material.yml',title:'[词条纠错] '+entry.id+' '+entry.name,entries:entry.id,details:body});
 return url.href;
}
$('detail-dialog').addEventListener('close',()=>{if(!$('detail-dialog').open)detailRequestSerial++});
