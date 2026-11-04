"""Expose clothing construction and aesthetic as independent browsing axes."""
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'tools/atlas_template.html'
s=p.read_text(encoding='utf-8')
if 'id="style-filter"' not in s:
    s=s.replace('DESIGN REFERENCE COLLECTION / 03','DESIGN REFERENCE COLLECTION / 04')
    s=s.replace('本次新增服装 · 464 条','本次新增 · __NEW_COUNT__ 条').replace('本次新增服装 · 464','本次新增 · __NEW_COUNT__')
    s=s.replace("e.added_in==='3.0'","e.added_in==='4.0'")
    s=s.replace("cat==='clothing_new'?e.added_in==='4.0':e.category===cat","cat==='clothing_new'?e.added_in==='4.0':cat==='shoulders'?Boolean(e.shoulder_type):e.category===cat")
    s=s.replace("category==='clothing_new'?'本次新增 · __NEW_COUNT__ 条':C.get(category).name","category==='clothing_new'?'本次新增 · __NEW_COUNT__ 条':category==='shoulders'?'露肩款与结构 · __SHOULDER_COUNT__ 条':C.get(category).name")
    s=s.replace("(category==='clothing'||category==='clothing_new')?'按版型","category==='shoulders'?'一字肩露出双肩，挖肩只在肩端开窗；单肩、抹胸、挂脖与细吊带分别记录承托方式。落肩袖指接缝位置下移，普通无袖也不一定露出肩顶。':(category==='clothing'||category==='clothing_new')?'按版型")
    s=s.replace('每条都有图例。','新增露肩结构与 15 种风格筛选；每条都有图例。',1)
    s=s.replace('<button data-category="onepiece">裙装与连体服</button>', '<button data-category="shoulders">露肩款与结构</button><button data-style="gothic">哥特</button><button data-style="british">英伦</button><button data-style="lolita">洛丽塔</button><button data-style="punk">朋克</button>')
    s=s.replace('<button data-category="fantasy_outfits">幻想与变身装</button><button data-category="layered_outfits">日常整套搭配</button>', '<button data-category="fashion_outfits">全部风格搭配</button>')
    marker='<div class="status-line"><h2 id="category-title">'
    facets='<div class="facet-tools"><label>风格 <select id="style-filter" class="dimension-filter" aria-label="服装风格"></select></label><label>肩部结构 <select id="shoulder-filter" class="dimension-filter" aria-label="肩部结构"></select></label><button id="reset-facets" class="small-btn">重置筛选</button></div>\n'
    s=s.replace(marker,facets+marker)
    s=s.replace('</style>','.facet-tools{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:0 0 18px}.facet-tools label{display:flex;gap:8px;align-items:center;font-size:12px;color:var(--muted)}.facet-tools select{max-width:250px}.entry-facets{display:flex;gap:4px;flex-wrap:wrap;margin-top:9px}.entry-facets button,.entry-facets span{font-size:10px;background:var(--soft);color:var(--accent);padding:4px 6px;border-radius:4px}.jump button[aria-pressed="true"]{background:var(--accent);color:var(--surface)}\n</style>')
    anchor="const clothingCategories=new Set(D.categories.filter(c=>c.group==='clothing').map(c=>c.id));"
    additions="\nconst F=new Map(D.style_families.map(f=>[f.id,f]));\n$('style-filter').innerHTML='<option value=\"all\">所有风格 · '+D.style_families.length+' 种</option>'+D.style_families.map(f=>'<option value=\"'+f.id+'\">'+esc(f.name)+' · '+f.clothing_count+'</option>').join('');\n$('shoulder-filter').innerHTML='<option value=\"all\">全部肩部结构</option>'+D.shoulder_types.map(f=>'<option value=\"'+f.id+'\">'+esc(f.name)+'</option>').join('');"
    # Initialization must run after esc is defined.
    esc_line="const esc=s=>String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',\"'\":'&#39;'}[c]));"
    assert esc_line in s
    s=s.replace(esc_line,esc_line+additions)
    s=s.replace("let arr=D.entries.filter(e=>matchesCategory(e)&&", "let arr=D.entries.filter(e=>matchesCategory(e)&&($('style-filter').value==='all'||e.styles.includes($('style-filter').value))&&($('shoulder-filter').value==='all'||e.shoulder_type===$('shoulder-filter').value)&&")
    s=s.replace("e.dimension+' '+e.description+' '+(e.visual?.label||'')", "e.dimension+' '+e.description+' '+e.keywords.join(' ')+' '+(e.visual?.label||'')")
    s=s.replace("$('mobile-category').value=category}","$('mobile-category').value=category;document.querySelectorAll('[data-style]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.style===$('style-filter').value));}")
    s=s.replace("function changeCategory(next){category=next;", "function changeCategory(next){$('style-filter').value='all';$('shoulder-filter').value='all';category=next;")
    anchor='function renderCard(){'
    extra="function changeStyle(id){if(!F.has(id))return;query='';$('search').value='';changeCategory('clothing');$('style-filter').value=id;renderTerms()}\nfunction facetLabels(e){return (e.styles.length||e.shoulder_type)?'<div class=\"entry-facets\">'+e.styles.map(id=>'<button data-style=\"'+id+'\">'+esc(F.get(id).name)+'</button>').join('')+(e.shoulder_type?'<span>'+esc(e.shoulder_name)+'</span>':'')+'</div>':''}\n"
    s=s.replace(anchor,extra+anchor)
    s=s.replace('<p class="en" lang="en">${esc(e.en)}</p><p class="desc">','<p class="en" lang="en">${esc(e.en)}</p>${facetLabels(e)}<p class="desc">')
    s=s.replace('<h3>角色设计要点</h3>','${facetLabels(e)}<h3>角色设计要点</h3>')
    s=s.replace('服装专辑 <span class="count">__CLOTHING_COUNT__</span></button>`','服装专辑 <span class="count">__CLOTHING_COUNT__</span></button><button data-category="shoulders">露肩款与结构 <span class="count">__SHOULDER_COUNT__</span></button>`')
    s=s.replace('<option value="clothing_new">本次新增 · __NEW_COUNT__</option>','<option value="clothing_new">本次新增 · __NEW_COUNT__</option><option value="shoulders">露肩款与结构 · __SHOULDER_COUNT__</option>')
    s=s.replace('<option value="clothing">服装专辑图页</option>','<option value="clothing">服装专辑图页</option><option value="shoulders">露肩款与结构图页</option>')
    s=s.replace("if(b.dataset.category)changeCategory(b.dataset.category);", "if(b.dataset.category)changeCategory(b.dataset.category);if(b.dataset.style){$('detail-dialog').close();changeStyle(b.dataset.style);}")
    anchor="$('dimension-filter').addEventListener('change',()=>{limit=72;renderTerms()});"
    extra="\n$('style-filter').addEventListener('change',()=>{const value=$('style-filter').value;if(category==='all'){changeCategory('clothing');$('style-filter').value=value;}limit=72;renderTerms()});$('shoulder-filter').addEventListener('change',()=>{limit=72;renderTerms()});$('reset-facets').addEventListener('click',()=>{query='';$('search').value='';changeCategory('clothing')});\n"
    s=s.replace(anchor,anchor+extra)
    s=s.replace("updateCounts();changeCategory(new URLSearchParams(location.search).get('section')==='clothing'?'clothing':'all');", "updateCounts();const params=new URLSearchParams(location.search),initial=params.get('section');changeCategory(['clothing','clothing_new','shoulders'].includes(initial)||C.has(initial)?initial:'all');if(F.has(params.get('style'))){$('style-filter').value=params.get('style');renderTerms();}")
    s=s.replace('image-prompts-v3.json','image-prompts-v4.json').replace('服装扩充图页提示词','露肩与风格图页提示词')
    s=s.replace('<a href="atlas.md" target="_blank">完整图文文档</a>','<a href="fashion-guide.md" target="_blank">露肩与风格专辑</a> · <a href="atlas.md" target="_blank">完整图文文档</a>')
    p.write_text(s,encoding='utf-8')
p=root/'tools/build_atlas_v2.py';s=p.read_text(encoding='utf-8')
s=s.replace('第 3 版，面向','第 4 版，面向').replace('第 3 版：服装专辑','第 4 版：服装专辑').replace('第 3 版核验日期','第 4 版核验日期')
s=s.replace("clothing='# 女性角色服装专辑 · 第 3 版", "clothing='# 女性角色服装专辑 · 第 4 版")
s=s.replace('相比第 2 版新增 464 条、29 张分类图页。','第 4 版新增露肩款式、结构对照与风格搭配，支持 15 种风格标签。')
s=s.replace('| clothing-atlas.md | 711 条服装、护甲与套装专辑 |','| clothing-atlas.md | 服装、护甲与套装专辑 |\n| fashion-guide.md | 露肩结构与 15 种风格的交叉检索专辑 |')
s=s.replace("'stage_outfits','layered_outfits'}", "'stage_outfits','layered_outfits','fashion_outfits'}")
s=s.replace('两版内置','四版内置').replace('三版内置','四版内置')
s=s.replace('image-prompts-v3.json | 四版','image-prompts-v3.json 与 image-prompts-v4.json | 四版')
s=s.replace('第 3 版服装扩充在 [image-prompts-v3.json](image-prompts-v3.json)。','第 3 版服装扩充在 [image-prompts-v3.json](image-prompts-v3.json)，第 4 版露肩与风格扩充在 [image-prompts-v4.json](image-prompts-v4.json)。')
p.write_text(s,encoding='utf-8')
print('Cross-category style and exposed-shoulder controls installed.')
