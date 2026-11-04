"""V30 companion index of motif variations and supplementary wearing images."""
from urllib.parse import quote
def write_wearing_reference_docs(root,data):
    new=[e for e in data['entries'] if e.get('anime_hairtie_reference')]
    text='# 发绳扩充与发饰、眼镜佩戴图\n\n第30版新增32种发绳发型，发绳类现共48项。原有64项发饰和16项眼镜分别补充佩戴图，保留原物件结构图；共新增112个图例，7张图页，不重复增加80条词条。\n\n'
    text+='打开 [发绳发型](index.html?section=hair_with_accessories&dimension='+quote('佩戴发绳的完整发型')+')、[发饰与固定结构](index.html?section=hair_accessories) 或 [眼镜与镜片类型](index.html?section=eyewear)。发饰与眼镜默认显示佩戴图，可切换物件图，详情内并排展示。\n\n'
    text+='## 发绳造型来源与变化\n\n| 结构方向 | 数量 | 观察参考 |\n| --- | ---: | --- |\n'
    for g in data['meta']['hair_tie_motifs']:text+=f"| {g['name']} | {g['count']} | [{g['reference']}]({g['url']}) |\n"
    text+='\n酒精喵喵的额前短冲天揪以用户提供的截图确认。图例提取发绳的结构与扎束位置，绘制原创成年人物与变化方案。\n\n'
    ids={e['visual']['board'] for e in new}
    for b in data['boards']:
        if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
    text+='| 编号 | 发型 | 结构方向 | 固定位置 |\n| --- | --- | --- | --- |\n'
    for e in new:text+=f"| {e['id']} | {e['name']} | {e['hair_tie_motif_name']} | {e['hair_accessory_anchor']} |\n"
    for cid in ['hair_accessories','eyewear']:
        es=[e for e in data['entries'] if e['category']==cid];c=next(c for c in data['categories'] if c['id']==cid);text+=f"\n## {c['name']} · {len(es)}项佩戴参考\n\n{c['guide']}\n\n"
        ids={e['wearing_visual']['board'] for e in es}
        for b in data['boards']:
            if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 物件 | 佩戴图 | 物件图 |\n| --- | --- | --- | --- |\n'
        for e in es:text+=f"| {e['id']} | {e['name']} | [{e['wearing_visual']['label']}]({e['wearing_visual']['image']}) | [结构]({e['visual']['image']}) |\n"
    text+='\n配图由内置imagegen生成，原图位于images目录，见 [第30版提示词](image-prompts-v30.json) 与 [角色发绳参考记录](../source/anime-hair-reference-notes-v30.json)。\n'
    (root/'docs/wearing-reference-atlas.md').write_text(text,encoding='utf-8')
