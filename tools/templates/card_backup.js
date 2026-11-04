const libraryBackupKey='female-beauty-library-backup-v1';let backupRenderGeneration=0,backupExportGeneration=0;
function appearanceBackupPayload(){return {schema:'female-appearance-library/v2',catalog_version:D.meta.version,activeId:lastAddedCardId,lastAddedCardId,cards:appearanceCards,prompt_history:promptHistory.filter(snapshot=>appearanceCards.some(card=>card.id===snapshot.cardKey))}}
async function backupDigest(payload){
 if(!globalThis.crypto?.subtle)return null;
 const bytes=new TextEncoder().encode(JSON.stringify(payload));
 return [...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(n=>n.toString(16).padStart(2,'0')).join('');
}
async function renderLibraryBackupStatus(){
 const generation=++backupRenderGeneration,node=$('card-backup-status');if(!node)return;
 let record;try{record=JSON.parse(localStorage.getItem(libraryBackupKey)||'null')}catch{}
 if(!record?.exportedAt||Number.isNaN(Date.parse(record.exportedAt))){node.textContent='尚未导出全部外观卡';delete node.dataset.changed;return}
 const date=new Date(record.exportedAt).toLocaleString('zh-CN',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false});
 let changed=false;try{const digest=await backupDigest(appearanceBackupPayload());changed=!!digest&&!!record.digest&&digest!==record.digest}catch{}
 if(generation!==backupRenderGeneration)return;
 const text='最近全部导出：'+date+(changed?' · 此后有新修改':'');
 if(node.textContent!==text)node.textContent=text;node.dataset.changed=String(changed);
}
async function recordLibraryExport(payload,exportedAt){
 const generation=++backupExportGeneration;
 try{
  const digest=await backupDigest(payload);if(generation!==backupExportGeneration)return;
  localStorage.setItem(libraryBackupKey,JSON.stringify({exportedAt,digest}));
 }catch{}
 await renderLibraryBackupStatus();
}
