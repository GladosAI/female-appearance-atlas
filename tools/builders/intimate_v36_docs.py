"""Current themed-apparel additions, catalog paths and image provenance."""
def write_intimate_v36_docs(root,data):
    es=[e for e in data['entries'] if e.get('intimate_theme_reference')]
    text='''# 情趣主题成衣与装扮扩充

第36版新增48种主题，每种一套完整图例，与原有16套共同组成64套情趣主题装扮。目录归属保持为“职业、主题与历史服装 → 主题装扮与人偶服 → 情趣主题装扮”。

[打开全部64套](../index.html?section=intimate_costumes) · [生成提示词](../prompts/image-prompts-v36.json)

配图沿用中性灰成年尺码服装人台，比较胸衣、连体衣、短裤、罩裙、披肩、头饰、袜类和鞋履如何组成完整主题。蕾丝、网纱与透明罩衣作为外层，保留不透明成衣衬底。复古和职业款均为原创舞台灵感改编。

'''
    for dim in dict.fromkeys(e['dimension'] for e in es):
        group=[e for e in es if e['dimension']==dim]
        board=next(b for b in data['boards'] if group[0]['id'] in {item['entry_id'] for item in b['items']})
        text+=f"## {dim}\n\n![{board['title']}](../{board['image']})\n\n| 编号 | 主题 | 成衣与配件组合 |\n| --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='## 图像与使用\n\n使用内置 image_gen 生成3张4×4图页，保存在 images/；每格与IN017—IN064逐一对应。图鉴中可按三个内容细分直接查找，点击“＋ 外观卡”将整套主题保存到选择的卡片。原IN001—IN016及其配图保持不变。完整提示记录见第36版提示词文件。\n'
    (root/'docs/intimate-theme-expansion.md').write_text(text,encoding='utf-8')
