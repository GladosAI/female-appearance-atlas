// Decode an origin-clean source so local file pages can export their cropped tiles.
const exportImageCache=new Map(),imageExportTimers=new WeakMap();
function getExportImage(image){
 if(exportImageCache.has(image)){const pending=exportImageCache.get(image);exportImageCache.delete(image);exportImageCache.set(image,pending);return pending}
 const pending=(async()=>{
  let src=image;
  if(location.protocol==='file:'){
   const file=D.image_exports?.[image];if(!file)throw Error('缺少离线图片数据，请确认图鉴文件完整。');
   src=await new Promise((resolve,reject)=>{const script=document.createElement('script');script.src=file;
    script.onload=()=>{const data=globalThis.__atlasImageData?.[image];if(globalThis.__atlasImageData)delete globalThis.__atlasImageData[image];script.remove();data?resolve(data):reject(Error('离线图片数据读取失败。'))};
    script.onerror=()=>{script.remove();reject(Error('图片读取失败，请确认图鉴文件完整。'))};document.head.append(script);
   });
  }
  const img=new Image();if(location.protocol!=='file:')img.crossOrigin='anonymous';img.src=src;await img.decode();return img;
 })();
 exportImageCache.set(image,pending);pending.catch(()=>{if(exportImageCache.get(image)===pending)exportImageCache.delete(image)});
 while(exportImageCache.size>8)exportImageCache.delete(exportImageCache.keys().next().value);
 return pending;
}
async function entryImagePNG(e,kind){
 const visual=entryVisual(e,kind);if(!visual)throw Error('这个词条没有可导出的图片。');
 const image=await getExportImage(visual.image),r=visual.crop;
 const xScale=r?image.naturalWidth/r.sheet_width:1,yScale=r?image.naturalHeight/r.sheet_height:1;
 const x=r?r.x*xScale:visual.column*image.naturalWidth/visual.columns,y=r?r.y*yScale:visual.row*image.naturalHeight/visual.rows;
 const w=r?r.width*xScale:image.naturalWidth/visual.columns,h=r?r.height*yScale:image.naturalHeight/visual.rows;
 const left=Math.round(x),top=Math.round(y),width=Math.round(x+w)-left,height=Math.round(y+h)-top;
 if(width<=0||height<=0||left<0||top<0||left+width>image.naturalWidth||top+height>image.naturalHeight)throw Error('图片裁切范围无效。');
 const canvas=document.createElement('canvas');canvas.width=width;canvas.height=height;
 canvas.getContext('2d').drawImage(image,left,top,width,height,0,0,width,height);
 return new Promise((resolve,reject)=>canvas.toBlob(blob=>blob?resolve(blob):reject(Error('图片导出失败。')),'image/png'));
}
function detailImageActions(e,kind){return `<div class="detail-image-actions"><button type="button" class="small-btn" data-image-export="download" data-image-entry="${e.id}" data-image-kind="${kind}">下载图片</button><button type="button" class="small-btn" data-image-export="copy" data-image-entry="${e.id}" data-image-kind="${kind}">复制图片</button><span class="image-export-status" role="status" aria-live="polite" hidden></span></div>`}
function detailImageFigure(e,kind,label=''){return `<figure class="detail-image-item">${label?`<figcaption>${label}</figcaption>`:''}${thumb(e,kind)}${detailImageActions(e,kind)}</figure>`}
function showImageExportStatus(status,message,success=false){
 if(!status?.isConnected)return;clearTimeout(imageExportTimers.get(status));status.textContent=message;status.hidden=!message;
 if(success)imageExportTimers.set(status,setTimeout(()=>{status.textContent='';status.hidden=true},2500));
}
async function exportDetailImage(button){
 const e=E.get(button.dataset.imageEntry),kind=button.dataset.imageKind;if(!e||button.disabled)return;
 const status=button.closest('.detail-image-item')?.querySelector('.image-export-status');button.disabled=true;
 showImageExportStatus(status,'正在准备图片…');
 try{
  if(button.dataset.imageExport==='copy'){
   if(!navigator.clipboard?.write||typeof ClipboardItem==='undefined')throw Error('当前浏览器不支持复制图片，请使用下载图片。');
   // Pass the PNG promise immediately to preserve the user gesture during decoding.
   await navigator.clipboard.write([new ClipboardItem({'image/png':entryImagePNG(e,kind)})]);
   showImageExportStatus(status,'图片已复制',true);
  }else{
   const blob=await entryImagePNG(e,kind),url=URL.createObjectURL(blob),a=document.createElement('a');
   const suffix={fullbody:'全身',object:e.fullbody_visual?'近景':e.wearing_visual?'物件':'',wearing:'佩戴'}[kind]||'';
   a.href=url;a.download=(e.id+'-'+e.name+(suffix?'-'+suffix:'')).replace(/[<>:"/\\|?*\u0000-\u001f]/g,'_')+'.png';
   (button.closest('dialog')||document.body).append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);
   showImageExportStatus(status,'下载已开始',true);
  }
 }catch(error){showImageExportStatus(status,error?.name==='NotAllowedError'?'复制失败，请允许剪贴板权限，或使用下载图片。':error.message||'图片操作失败，请重试。')}
 finally{button.disabled=false}
}
document.addEventListener('click',ev=>{const button=ev.target.closest('button[data-image-export]');if(button)exportDetailImage(button)});
