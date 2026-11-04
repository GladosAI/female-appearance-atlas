"""Index clothing accessories and visibly worn hair accessories together."""
from urllib.parse import quote
def write_accessory_hairstyle_docs(root,data):
    acc=[e for e in data['entries'] if e.get('accessory_expansion_reference')];hair=[e for e in data['entries'] if e.get('styled_hair_reference')]
    text=f"# 衣着配饰与佩戴发饰的完整发型\n\n共{len(acc)}项衣着配饰与{len(hair)}种佩戴发饰的完整发型。发绳48项，发卡、发箍、发簪各16项；第30版新增组绳长带结、双侧蝶结、侧鬓缠绳和额前小束共32项。原有64项发饰与16项眼镜补齐佩戴图，见 [佩戴专题](wearing-reference-atlas.md)。\n\n"
    text+='打开 [配饰主题](index.html?section=topic_accessory_design)、[佩戴发饰的完整发型](index.html?section=hair_with_accessories) 或 [头发与发型主题](index.html?section=topic_hair_design)。独立发饰物件继续在 [发饰与固定结构](index.html?section=hair_accessories) 浏览。\n\n'
    text+='## 配饰类别\n\n| 类别 | 数量 | 主要观察位置 |\n| --- | ---: | --- |\n'
    for cid in data['meta']['accessory_expansion_categories']:
        c=next(c for c in data['categories'] if c['id']==cid);es=[e for e in acc if e['category']==cid]
        text+=f"| [{c['name']}](index.html?section={cid}) | {len(es)} | {'、'.join(dict.fromkeys(e['accessory_anchor'] for e in es))} |\n"
    text+='\n## 发饰完整发型分组\n\n| 分组 | 数量 | 查看 |\n| --- | ---: | --- |\n'
    for g in data['meta']['hair_accessory_groups']:text+=f"| {g['name']} | {g['count']} | [查看](index.html?section=hair_with_accessories&dimension={quote(g['name'])}) |\n"
    text+='\n'
    for cid in data['meta']['accessory_expansion_categories']:
        c=next(c for c in data['categories'] if c['id']==cid);es=[e for e in acc if e['category']==cid];text+=f"## {c['name']}\n\n{c['guide']}\n\n"
        ids={e['visual']['board'] for e in es}
        for b in data['boards']:
            if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
        if cid=='cords_tassels':
            text+='按头发、腕臂、腕踝、腰腹和腿部五组筛选；每张佩戴图显示独立绳饰的绕行、结位与完整绳尾。\n\n'
            text+='| 编号 | 名称 | 区域 | 佩戴位置 | 视角 | 结位 | 结构 |\n| --- | --- | --- | --- | --- | --- | --- |\n'
            for e in es:text+=f"| {e['id']} | {e['name']} | {e['cord_region']} | {e['accessory_anchor']} | {e['cord_view']} | {e['cord_knot_anchor']} | {e['accessory_construction']} |\n"
        else:
            text+='| 编号 | 名称 | 佩戴位置 | 结构 |\n| --- | --- | --- | --- |\n'
            for e in es:text+=f"| {e['id']} | {e['name']} | {e['accessory_anchor']} | {e['accessory_construction']} |\n"
        text+='\n'
    for g in data['meta']['hair_accessory_groups']:
        es=[e for e in hair if e['hair_accessory_kind']==g['id']];text+=f"## {g['name']}\n\n"
        if g['id']=='tie':
            text+='本组包括16项实物发圈结构和32项动画发绳结构变化，主图保留完整发型，局部放大图显示同一束根或辫尾上的固定关系。结构参考：[Scunci 弹力发绳](https://www.scunci.com.au/elastics)、[Scunci 布褶发圈](https://www.scunci.com.au/scrunchies)、[invisibobble 螺旋发圈](https://invisibobble.com/products/original-crystal-clear-2023)；参考记录见 [发绳研究笔记](../source/hairtie-reference-notes-v29.json)。\n\n'
        ids={e['visual']['board'] for e in es}
        for b in data['boards']:
            if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 发型 | 发饰 | 视角 | 固定位置 |\n| --- | --- | --- | --- | --- |\n'
        for e in es:text+=f"| {e['id']} | {e['name']} | {e['hair_accessory_name']} | {e['hair_accessory_view']} | {e['hair_accessory_anchor']} |\n"
        text+='\n'
    text+='配图由内置 imagegen 生成，完整原图保存于 images 目录，提示词见 [第29版提示词](image-prompts-v29.json)。参考入口：[V&A 首饰收藏](https://www.vam.ac.uk/collections/jewellery)、[Met 中国发簪馆藏](https://www.metmuseum.org/art/collection/search/60875)。图例为原创结构与佩戴设计，未复制馆藏照片或具体品牌样式。\n'
    (root/'docs/accessory-hairstyles-atlas.md').write_text(text,encoding='utf-8')
