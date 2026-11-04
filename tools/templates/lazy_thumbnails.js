// CSS sheet thumbnails should not download until their cards approach a viewport.
const thumbnailObserver='IntersectionObserver' in window?new IntersectionObserver(records=>{
 for(const record of records)if(record.isIntersecting){loadThumbnail(record.target);thumbnailObserver.unobserve(record.target)}
},{rootMargin:'240px'}):null;
function loadThumbnail(element){
 const source=element.dataset.thumbImage;if(!source)return;
 element.style.backgroundImage='url('+JSON.stringify(source)+')';delete element.dataset.thumbImage;
}
function observeThumbnails(root){
 if(!(root instanceof Element))return;
 const thumbnails=[...(root.matches('[data-thumb-image]')?[root]:[]),...root.querySelectorAll('[data-thumb-image]')];
 for(const element of thumbnails)if(thumbnailObserver)thumbnailObserver.observe(element);else loadThumbnail(element);
}
new MutationObserver(records=>{for(const record of records){for(const node of record.addedNodes)observeThumbnails(node);if(thumbnailObserver)for(const node of record.removedNodes)if(node instanceof Element){if(node.matches('[data-thumb-image]'))thumbnailObserver.unobserve(node);for(const element of node.querySelectorAll('[data-thumb-image]'))thumbnailObserver.unobserve(element)}}}).observe(document.body,{childList:true,subtree:true});
observeThumbnails(document.body);
