"""Add an aggregate clothing section and edition-3 metadata, retaining old cards."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'tools/atlas_template.html'
s=p.read_text(encoding='utf-8')
if "function matchesCategory" not in s:
    s=s.replace('DESIGN REFERENCE COLLECTION / 02','DESIGN REFERENCE COLLECTION / 03')
    s=s.replace('width:min(__ILLUSTRATED_COUNT__0px,92vw)','width:min(1100px,92vw)')
    s=s.replace('<span>配图词条</span>','<span>全部配图词条</span>')
    s=s.replace('<div class="stat"><strong>__CATEGORY_COUNT__</strong><span>细分类别</span></div>','<div class="stat"><strong>__CLOTHING_COUNT__</strong><span>服装／护甲／套装</span></div>')
    s=s.replace('把可观察的形态整理成可检索、可组合的创作词汇。','服装专辑现有 __CLOTHING_COUNT__ 条，涵盖单件、制服、护甲与整套搭配；每条都有图例。')
    s=s.replace('<div class="tools"><div class="search-wrap">','<div class="jump"><button data-category="clothing">只看服装 · __CLOTHING_COUNT__ 条</button><button data-category="onepiece">裙装与连体服</button><button data-category="fantasy_outfits">幻想与变身装</button><button data-category="layered_outfits">日常整套搭配</button><button data-category="all">全部外观</button></div>\n<div class="tools"><div class="search-wrap">',1)
    s=s.replace('image-prompts-v2.json','image-prompts-v3.json').replace('新增图页提示词','服装扩充图页提示词')
    anchor="const key='female-appearance-atlas-v1';"
    s=s.replace(anchor,anchor+"\nconst clothingCategories=new Set(D.categories.filter(c=>c.group==='clothing').map(c=>c.id));\nfunction matchesCategory(e,cat=category){return cat==='all'||(cat==='clothing'?clothingCategories.has(e.category):e.category===cat)}")
    s=s.replace("(category==='all'||e.category===category)","matchesCategory(e)")
    s=s.replace("filter(e=>category==='all'||e.category===category)","filter(e=>matchesCategory(e))")
    s=s.replace(":C.get(category).name;",":category==='clothing'?'服装专辑 · __CLOTHING_COUNT__ 条':C.get(category).name;")
    s=s.replace(":C.get(category).guide;",":category==='clothing'?'按版型、职业和场景细分；含单件服装、护甲部件与套装方案。整套搭配和历史改编均单独标注，可拆成外观卡部件。':C.get(category).guide;")
    s=s.replace("<span class=\"count\">__ENTRY_COUNT__</span></button>`+D.categories", "<span class=\"count\">__ENTRY_COUNT__</span></button><button data-category=\"clothing\">服装专辑 <span class=\"count\">__CLOTHING_COUNT__</span></button>`+D.categories")
    s=s.replace("所有类别 · __ENTRY_COUNT__</option>'", "所有类别 · __ENTRY_COUNT__</option><option value=\"clothing\">服装专辑 · __CLOTHING_COUNT__</option>'")
    s=s.replace("b.items.some(x=>E.get(x.entry_id).category===cat)","b.items.some(x=>matchesCategory(E.get(x.entry_id),cat))")
    s=s.replace("全部图页 · __BOARD_COUNT__</option>'", "全部图页 · __BOARD_COUNT__</option><option value=\"clothing\">服装专辑图页</option>'")
    s=s.replace("updateCounts();changeCategory('all');", "updateCounts();changeCategory(new URLSearchParams(location.search).get('section')==='clothing'?'clothing':'all');")
    p.write_text(s,encoding='utf-8')
p=root/'tools/build_atlas_v2.py'
s=p.read_text(encoding='utf-8')
s=s.replace("'version':'2.0'","'version':'3.0'")
s=s.replace("'category_count':len(categories),","'category_count':len(categories),'clothing_count':sum(counts[k] for k in CLOTHING_CATEGORIES),'clothing_categories':CLOTHING_CATEGORIES,")
s=s.replace("'__ATLAS_DATA__':", "'__CLOTHING_COUNT__':str(meta['clothing_count']),'__ATLAS_DATA__':")
s=s.replace('第 2 版','第 3 版').replace('六張','六张')
s=s.replace('第 3 版提示词](image-prompts-v2.json)','服装扩充提示词](image-prompts-v3.json)')
s=s.replace('新增图页的提示词在 [image-prompts-v2.json](image-prompts-v2.json)', '第 2 版扩充在 [image-prompts-v2.json](image-prompts-v2.json)，第 3 版服装扩充在 [image-prompts-v3.json](image-prompts-v3.json)')
s=s.replace('image-prompts.json 与 image-prompts-v2.json | 两版', 'image-prompts.json、image-prompts-v2.json 与 image-prompts-v3.json | 三版')
s=s.replace("第 3 版，面向游戏与动漫角色设计。共", "第 3 版，面向游戏与动漫角色设计。服装专辑包含 {m['clothing_count']} 条服装、护甲与套装参考。共")
s=s.replace("第 3 版：{m['entry_count']} 个词条", "第 3 版：服装专辑 {m['clothing_count']} 条；全部 {m['entry_count']} 个词条")
s=s.replace('每个词条均有图，默认按类别排列；','首页增加“只看服装”入口，服装专辑可按细分维度筛选；每个词条均有图，默认按类别排列；')
p.write_text(s,encoding='utf-8')
print('Updated clothing section and edition-3 documentation.')
