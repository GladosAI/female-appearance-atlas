"""Edition 18 topic guide and browsable outfit recipes."""

def write_trend_model_docs(root,data):
    cats=[c for c in data['categories'] if c['id'] in data['meta']['trend_model_categories']]
    text='''# 潮流、时尚与模特穿搭图鉴

第18版新增96套原创成年女性造型，三类各32套，每类分两个16套方向。打开 [图鉴](../index.html?section=trend_outfits)，在“日常、校园与风格穿搭”中选择类别。三者按观察重点分组，可以互相借用部件。

| 类别 | 重点 | 两个方向 |
| --- | --- | --- |
| [潮流穿搭](../index.html?section=trend_outfits) | 街头语汇、廓形比例、运动与工装混搭 | 街头廓形与运动混搭；机能配件与复古街拍 |
| [时尚穿搭](../index.html?section=chic_outfits) | 剪裁、色彩、材质与场合设计 | 都市剪裁与质感配色；设计感廓形与场合造型 |
| [模特穿搭](../index.html?section=model_outfits) | 衣物展示与拍摄语境 | 秀场与型录展示；编辑拍摄与场外搭配 |

“潮流”是原创设计的检索方向，不表示对某一季流行趋势的排名。“模特”描述展示语境，不代表规定的身高、体型或审美标准。每套都记录衣物、鞋履和相关配饰。

'''
    for cat in cats:
        text+=f"## {cat['name']}\n\n{cat['guide']}\n\n"
        for board in data['boards']:
            if board.get('category')==cat['id']:
                text+=f"### {board['dimension']}\n\n![{board['title']}](../{board['image']})\n\n| 编号 | 造型 | 搭配与可见特征 |\n| --- | --- | --- |\n"
                for e in data['entries']:
                    if e['category']==cat['id'] and e['dimension']==board['dimension']:
                        text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
                text+='\n'
    text+='''## 参考与提示词

- [V&A Fashion](https://www.vam.ac.uk/collections/fashion)：服装、材质与剪裁研究入口。
- [V&A 100 years of fashion photography](https://www.vam.ac.uk/articles/100-years-of-fashion-photography)：编辑、街头与摄影展示语境。
- [V&A The fashion show](https://www.vam.ac.uk/articles/the-fashion-show)：秀场展示语境。
- [本版6张图页提示词](../prompts/image-prompts-v18.json)：内置 imagegen 生成的原创动漫配图，按编号裁切展示。

保留原有4237个词条与编号；完整图鉴现有4333个词条、95个基础类别及302张分类图页。配图与词条是独立创作；相关阅读不表示每套方案来自某一馆藏或品牌。
'''
    meta=data['meta']
    text=text.replace('完整图鉴现有4333个词条、95个基础类别及302张分类图页',f"完整图鉴现有{meta['entry_count']}个词条、{meta['category_count']}个基础类别及{meta['board_count']}张分类图页")
    (root/'docs/trend-fashion-model-atlas.md').write_text(text,encoding='utf-8')
