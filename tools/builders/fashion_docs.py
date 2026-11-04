"""Clothing additions and aesthetic styles, with original image examples."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path

def write_fashion_docs(root,data):
    from hosiery_docs import write_hosiery_docs
    write_hosiery_docs(root,data)
    es=data['entries'];boards=data['boards']
    hair=[e for e in es if e['category'].startswith('hair_') and e['category']!='hair_accessories']
    combination_count=sum(e['category']=='hair_combinations' for e in hair)
    document=f"# 女性角色头发图鉴\n\n共 {len(hair)} 项：剪裁、刘海、扎编、卷纹与染色、局部发束、64项头发形态与状态，以及{combination_count}套完整组合和{data['meta']['styled_hair_count']}种佩戴发饰的完整发型；每个词条都有图。\n\n打开 [全部头发](index.html?section=hair)、[完整发型](index.html?section=hair_combinations)、[佩戴发饰的完整发型](index.html?section=hair_with_accessories) 或 [头发形态](index.html?section=hair_states) 筛选。发绳佩戴发型48种，发卡、发箍、发簪各16种，展示固定位置与发束接触。独立物件另见 [发饰部件](index.html?section=hair_accessories)。先选剪裁和刘海，再选扎编、卷纹与局部发束；完整方案提供可拆分的搭配。所有人物为成年女性。局部图着重展示结构，未展示的侧背面可沿文字补画。\n\n"
    shown=set()
    for c in data['categories']:
        group=[e for e in hair if e['category']==c['id']]
        if not group:continue
        document+=f"## {c['name']} · {len(group)} 项\n\n{c['guide']}\n\n"
        used={e['visual']['board'] for e in group}
        for b in boards:
            if b['id'] in used and b['id'] not in shown:
                shown.add(b['id']);document+=f"![{b['title']}]({b['image']})\n\n"
        document+='| 编号 | 发型与部件 | English | 可见结构 |\n| --- | --- | --- | --- |\n'
        for e in group:document+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
        document+='\n'
    document+='相关阅读：[动漫发型结构教程](https://www.clipstudio.net/how-to-draw/archives/171638) · [完整来源说明](sources.md)。\n'
    (Path(root)/'docs/hair-atlas.md').write_text(document,encoding='utf-8')
