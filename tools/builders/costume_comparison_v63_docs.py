"""Describe the scope, limitations and original entries of the v63 outfit audit."""
from pathlib import Path

def write_costume_comparison_v63_docs(root, data):
    root=Path(root)
    entries=[e for e in data['entries'] if e.get('outfit_combination_v63')]
    labels={'spring_outfits':'春季','summer_outfits':'夏季','autumn_outfits':'秋季',
            'winter_outfits':'冬季','swimwear':'泳装与度假','sleepwear':'居家睡衣','fashion_outfits':'夜宴与都市造型'}
    intro='''# 参考服装搭配对照与原创补充

参考 AI Pose Gallery 的 1,407 条服装记录检索分类和标签，并抽看部分原图；原图中的服装与文字标签并不总是一致。现有图鉴已经包含许多相同单品和相近搭配，本次侧重补充此前没有明确列出的整套组合，不把已有单品视作新服装类型。不同颜色或小饰品的重复记录没有逐条增加。

本次新增 48 套原创图例：春夏秋冬各 8 套，泳装与度假、夜宴、居家和都市束腰搭配各 4 套。配图由内置 image_gen 独立生成，并非引用或复制参考项目的图像；居家部分使用人台展示。下方参考编号用于记录选题灵感，并不表示与参考图完全相同。由于参考库庞大且标签存在偏差，本次不是逐张核实 1,407 张图，不能据此断言剩余服装全部收录。

[打开四季穿搭](../index.html?section=seasonal) · [泳装与度假](../index.html?section=swimwear) · [居家睡衣](../index.html?section=sleepwear) · [风格穿搭](../index.html?section=fashion_outfits)

'''
    for cid in ['spring_outfits','summer_outfits','autumn_outfits','winter_outfits','swimwear','sleepwear','fashion_outfits']:
        group=[e for e in entries if e['category']==cid]
        intro+=f"## {labels[cid]} · {len(group)} 套\n\n| 编号 | 新增搭配 | 参考记录 |\n| --- | --- | --- |\n"
        for e in group:intro+=f"| {e['id']} | {e['name']} | {e['inspiration_reference']} |\n"
        intro+='\n'
    intro+='参考项目代码与素材的许可范围不同；本图鉴不包含该项目原图或原始数据。\n'
    (root/'docs/costume-comparison-v63.md').write_text(intro,encoding='utf-8')
