(async()=>{'use strict';
await AtlasI18n.ready;
const D=window.ATLAS_CONTRIBUTION,$=id=>document.getElementById(id),form=$('contribution-form');
const categories=new Map(D.categories.map(c=>[c.id,c]));let image=null,imageURL=null,imageGeneration=0,proposal=null;
const text=id=>$(id).value.trim(),normalize=value=>String(value).normalize('NFKC').toLocaleLowerCase();
function categoryOptions(){const selected=$('category').value;$('category').replaceChildren();for(const c of D.categories){const option=document.createElement('option');option.value=c.id;option.textContent=AtlasI18n.text(c.name);$('category').append(option)}if(categories.has(selected))$('category').value=selected}
categoryOptions();
function nearby(value){
 const words=normalize(value).split(/[\s,，]+/).filter(Boolean),list=$('nearby');list.replaceChildren();
 if(!words.length){const li=document.createElement('li');li.textContent='输入关键词，避免重复制作已有词条。';li.className='muted';list.append(li);return}
 const matches=D.entries.filter(e=>{const translated=globalThis.ATLAS_LOCALE_SEARCH?.[e.id]||{};return words.every(word=>normalize([e.name,e.en,AtlasI18n.entryName(e),translated.en,translated.ja,...(translated.aliases||[]),...e.aliases].join(' ')).includes(word))}).slice(0,6);
 for(const entry of matches){const li=document.createElement('li'),a=document.createElement('a');a.href='index.html?'+new URLSearchParams({section:entry.category,entry:entry.id,lang:AtlasI18n.locale});a.target='_blank';a.rel='noopener noreferrer';a.setAttribute('data-i18n-skip','');a.textContent=entry.id+' · '+AtlasI18n.entryName(entry)+(AtlasI18n.locale==='en'?'':'（'+entry.en+'）');li.append(a);list.append(li)}
 if(!matches.length){const li=document.createElement('li');li.className='muted';li.textContent='当前关键词未找到近似词条，也可换英文或别名继续查找。';list.append(li)}
}
function updateCategoryLabels(){const c=categories.get($('category').value);$('dimensions').replaceChildren(...c.dimensions.map(value=>{const option=document.createElement('option');option.value=value;option.label=AtlasI18n.text(value);return option}));$('identifier-note').textContent=AtlasI18n.format('建议编号：{id} · 合并前会重新检查编号冲突。',{id:c.suggested_id})}
function changeCategory(){const c=categories.get($('category').value);$('dimension').value=c.dimensions[0]||'';updateCategoryLabels();refresh()}
function refresh(){
 proposal=null;const category=categories.get($('category').value);
 let source=null;try{if(text('source-url')){source=new URL(text('source-url'));if(!['http:','https:'].includes(source.protocol))throw Error();}}catch{$('source-url').setCustomValidity(AtlasI18n.t('请使用公开的 http 或 https 链接。'));source=null;}
 if(!text('source-url')||source)$('source-url').setCustomValidity('');
 $('source-url').required=text('method')==='third-party'||text('license')!=='CC-BY-NC-4.0';
 $('rights-note').required=text('license')==='other';
 if(form.checkValidity()&&image){
  const id=category.suggested_id,base='contribution-'+id.toLowerCase(),imagePath='images/'+base+'.'+image.extension;
  const entry={stable_id:id,category:category.id,dimension:text('dimension'),name:text('name'),en:text('en'),description:text('description'),note:text('note'),origin:'editorial',aliases:[...new Set(text('aliases').split(/[,，;；]/).map(s=>s.trim()).filter(Boolean))]};
  proposal={schema:'female-appearance-contribution/v1',entries:[entry],boards:[{id:base,title:entry.name,image:imagePath,width:image.width,height:image.height,columns:1,rows:1,origin:text('method'),items:[{entry_id:id,label:id,name:entry.name}]}],references:[],submission:{status:'pending-review',catalog_version:D.catalog_version,author:text('author'),creation_method:text('method'),license:text('license'),source_url:source?.href||null,rights_note:text('rights-note')||null,generator:text('generator')||null,created_on:text('created-on')||null,generation_notes:text('generation-notes')||null,image:{original_filename:image.file.name,bytes:image.file.size,sha256:image.sha256}}};
 }
 $('proposal').value=proposal?JSON.stringify(proposal,null,2):'';$('download-proposal').disabled=!proposal;$('download-image').disabled=!proposal;
 $('proposal-status').textContent=proposal?'可以导出；图片和授权仍待维护者审核。':'请填写必需项并选择有效配图。';
}
$('existing-search').addEventListener('input',()=>nearby(text('existing-search')));
$('name').addEventListener('input',()=>{if(!text('existing-search'))nearby(text('name'))});
$('category').addEventListener('change',changeCategory);form.addEventListener('input',refresh);form.addEventListener('change',refresh);
$('image').addEventListener('change',async()=>{
 const generation=++imageGeneration,file=$('image').files[0];image=null;if(imageURL)URL.revokeObjectURL(imageURL);imageURL=null;$('image-preview').hidden=true;refresh();if(!file)return;
 let pendingURL=null;try{
  const types={'image/png':'png','image/jpeg':'jpg','image/webp':'webp'};if(!types[file.type])throw Error('请选择PNG、JPG或WebP图片。');if(file.size>25*1024*1024)throw Error('图片超过本页25MiB限制。');if(!crypto?.subtle)throw Error('此浏览器无法计算图片校验值，请从在线贡献页打开。');
  $('image-status').textContent='正在读取图片并计算校验值…';const url=pendingURL=URL.createObjectURL(file),preview=new Image();preview.src=url;await preview.decode();
  const digest=[...new Uint8Array(await crypto.subtle.digest('SHA-256',await file.arrayBuffer()))].map(n=>n.toString(16).padStart(2,'0')).join('');
  if(generation!==imageGeneration){URL.revokeObjectURL(url);return}
  image={file,extension:types[file.type],width:preview.naturalWidth,height:preview.naturalHeight,sha256:digest};imageURL=url;$('image-preview').src=url;$('image-preview').hidden=false;$('image-status').textContent=image.width+' × '+image.height+' 像素 · SHA-256 '+digest;
 }catch(error){if(pendingURL)URL.revokeObjectURL(pendingURL);if(generation===imageGeneration)$('image-status').textContent=error.message}
 if(generation===imageGeneration)refresh();
});
function download(blob,name){const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
form.addEventListener('submit',event=>{event.preventDefault();refresh();if(!proposal){form.reportValidity();return}download(new Blob([JSON.stringify(proposal,null,2)+'\n'],{type:'application/json'}),'contribution-'+proposal.entries[0].stable_id.toLowerCase()+'.json')});
$('download-image').addEventListener('click',()=>{if(proposal&&image)download(image.file,proposal.boards[0].image.split('/').pop())});
window.addEventListener('pagehide',event=>{if(!event.persisted&&imageURL)URL.revokeObjectURL(imageURL)});changeCategory();
document.addEventListener('atlas:beforelocalechange',event=>{
 event.preventDefault();const desired=event.detail.locale,selector=$('language-select');selector.disabled=true;
 AtlasI18n.setLocale(desired).then(()=>{categoryOptions();updateCategoryLabels();nearby(text('existing-search')||text('name'));refresh();AtlasI18n.apply()}).catch(()=>{selector.value=AtlasI18n.locale;$('proposal-status').textContent=AtlasI18n.t('语言包加载失败，请重试。')}).finally(()=>selector.disabled=false);
});
})();
