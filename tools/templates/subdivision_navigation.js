let expandedSubdivisionCategory=null;
function categorySubdivisionGroups(){
 if(!C.has(category))return [];
 const counts=new Map();for(const entry of D.entries)if(entry.category===category)counts.set(entry.dimension,(counts.get(entry.dimension)||0)+1);
 return [...counts].map(([name,total])=>({name,total}));
}
function renderSubdivisionNavigation(){
 const groups=categorySubdivisionGroups(),matching=getResults({dimension:'all'}),matches=new Map();for(const entry of matching)matches.set(entry.dimension,(matches.get(entry.dimension)||0)+1);
 const selectedDimension=$('dimension-filter').value,expanded=expandedSubdivisionCategory===category,visible=new Set(groups.slice(0,8).map(g=>g.name));if(selectedDimension!=='all')visible.add(selectedDimension);
 for(const id of ['category-subdivisions','board-subdivisions']){
  const panel=$(id);panel.hidden=!groups.length;if(!groups.length){panel.innerHTML='';continue}
  panel.classList.toggle('is-single',groups.length===1);
  if(groups.length===1){panel.innerHTML=`<div class="subdivision-heading"><h2>内容细分</h2></div><p class="subdivision-single-note">本类未再细分，共 ${groups[0].total} 项，可直接浏览全部内容。</p>`;continue}
  const shown=expanded?groups:groups.filter(group=>visible.has(group.name)),remaining=groups.length-shown.length;
  const option=(value,label,count)=>`<button type="button" class="subdivision-option" data-dimension-choice="${esc(value)}" aria-pressed="${selectedDimension===value}"${value!=='all'&&count===0&&selectedDimension!==value?' disabled':''}><span>${esc(label)}</span><small>${count} 项</small></button>`;
  panel.innerHTML=`<div class="subdivision-heading"><h2>按细分浏览 <span>${groups.length} 组</span></h2><p>点击选项切换，可随时回到全部</p></div><div id="${id}-options" class="subdivision-options" role="group" aria-label="${esc(scopeLabel())}的内容细分">${option('all','全部',matching.length)}${shown.map(group=>option(group.name,group.name.replace(/^新增/,''),matches.get(group.name)||0)).join('')}</div>${groups.length>8?`<button type="button" class="subdivision-more" data-expand-subdivisions="${!expanded}" aria-expanded="${expanded}" aria-controls="${id}-options">${expanded?'收起更多 ▴':`展开其余 ${remaining} 组 · 共 ${groups.length} 组 ▾`}</button>`:''}${query||styleFilter?'<p class="subdivision-search-note">各组数量随当前搜索和风格筛选更新。</p>':''}`;
 }
 updateSubdivisionJump();
}
function changeSubdivision(value){
 if(value!=='all'&&!categorySubdivisionGroups().some(group=>group.name===value))return;
 $('dimension-filter').value=value;ageView='entries';bodyView='entries';limit=72;pushRoute=true;renderTerms();
 const panel=$(view==='boards'?'board-subdivisions':'category-subdivisions');[...panel.querySelectorAll('[data-dimension-choice]')].find(button=>button.dataset.dimensionChoice===value)?.focus({preventScroll:true});
}
function updateSubdivisionJump(){
 const button=$('jump-subdivisions'),browsing=['terms','boards'].includes(view),groups=browsing?categorySubdivisionGroups():[];
 if(groups.length<2){button.hidden=true;return}
 const panel=$(view==='boards'?'board-subdivisions':'category-subdivisions');button.hidden=panel.getBoundingClientRect().bottom>=0;
 button.textContent='切换细分 · '+groups.length+'组';button.title='当前细分：'+($('dimension-filter').value==='all'?'全部':$('dimension-filter').value);
}
document.addEventListener('click',event=>{
 const button=event.target.closest('button');if(!button)return;
 if(button.dataset.dimensionChoice!==undefined)changeSubdivision(button.dataset.dimensionChoice);
 if(button.dataset.expandSubdivisions!==undefined){expandedSubdivisionCategory=button.dataset.expandSubdivisions==='true'?category:null;renderSubdivisionNavigation();$(view==='boards'?'board-subdivisions':'category-subdivisions').querySelector('[data-expand-subdivisions]')?.focus({preventScroll:true})}
});
$('jump-subdivisions').addEventListener('click',()=>scrollToBrowseResults());
window.addEventListener('scroll',updateSubdivisionJump,{passive:true});
