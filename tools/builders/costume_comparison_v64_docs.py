"""Record original outfits selected by comparing text, without checking source images."""
from pathlib import Path

def write_costume_comparison_v64_docs(root,data):
    root=Path(root)
    labels={'spring_outfits':'春季','summer_outfits':'夏季','autumn_outfits':'秋季',
            'winter_outfits':'冬季','swimwear':'度假','sleepwear':'居家','fashion_outfits':'夜宴'}
    entries=[e for e in data['entries'] if e.get('outfit_combination_v64')]
    text='''# 参考词条对照：14 套原创搭配

本轮只根据参考库的文字名称和标签与本图鉴词条比较，未检查或复刻参考图片。编号仅用于记录选题，生成图是独立设计，因此不能视为对参考图片的确认。很多单品已在图鉴中存在；本轮补充的是整套组合。

[四季日常](../index.html?section=seasonal) · [泳装与度假](../index.html?section=swimwear) · [睡衣](../index.html?section=sleepwear) · [风格穿搭](../index.html?section=fashion_outfits) · [生成提示词](../prompts/image-prompts-v64.json) · [上轮对照](costume-comparison-v63.md)

'''
    for cid,label in labels.items():
        subset=[e for e in entries if e['category']==cid]
        text+=f'## {label} · {len(subset)} 套\n\n| 编号 | 原创搭配 | 参考词条编号 |\n| --- | --- | --- |\n'
        for e in subset:text+=f"| {e['id']} | {e['name']} | {e['inspiration_reference']} |\n"
        text+='\n'
    (root/'docs/costume-comparison-v64.md').write_text(text,encoding='utf-8')
