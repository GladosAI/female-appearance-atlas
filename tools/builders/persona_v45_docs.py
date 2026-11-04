"""Readable overview of coordinated adult character-presence studies."""
from urllib.parse import quote

def write_persona_v45_docs(root,data):
    persona=[e for e in data['entries'] if e.get('persona_reference')]
    labels=list(dict.fromkeys(e['persona_tag'] for e in persona))
    boards=[b for b in data['boards'] if b.get('category') in ['persona_looks','coverage_looks']]
    text=f'''# 气质、角色表现与服装覆盖程度

[进入分组](../index.html?section=branch_character_presence) · [气质全部](../index.html?section=persona_looks) · [第50版气质与表演扩充](presence-acting-v50.md) · [第49版气质与关联造型](presence-styles-v49.md) · [第48版气质与手势扩充](presence-gestures-v48.md)

目前{len(persona)}套气质造型涵盖{len(labels)}种表现，每种有两套搭配；另有8套露肤与覆盖程度对照。所有图例采用25岁以上成年角色，使用内置 image_gen 制作{len(boards)}张四格全身图页。服装、表情、视线、手势与重心共同形成印象；这些是可混搭的创作表演标签，不是根据外貌判定真实人格的依据。

第50版新增软萌、卡哇伊、千金大小姐、精神异常、邋遢、拘谨、洁癖、病态、反差、占有欲，各两套，编号QL153–QL172。反差比较甜装冷面与硬朗衣着下的羞涩神态；健康相关词仅用于虚构角色表演。

第49版新增圣洁、妖艳、清冷、病娇、厌世、疏离、天真、保持距离、空灵、肃穆、颓靡、倦怠，各两套，编号QL129–QL152。地雷系与艺妓分别归入服装风格和传统服饰，可从本轮汇总跳转。

第48版继续新增清新、素朴、禁欲、野性、妩媚、端丽、热血、好胜、机敏、专注、好奇、乖巧、笨拙、冒失、戏谑、毒舌，各两套，编号QL097–QL128。

第46版新增甜酷、俏皮、羞涩、怯生、骄矜、贵气、亲和、阳光、冷静、严肃、狡黠、腹黑、率真、随性、坚毅、勇敢、浪漫、感性、忧郁、脆弱、强势、威严、中性、华丽，各两套。采用日常、礼装、行旅与原创幻想等搭配，保留完整表情、手势和鞋履。新增编号为QL049–QL096，原有编号保留。

[第46版提示词与图片路径](../prompts/image-prompts-v46.json) · [第45版提示词与图片路径](../prompts/image-prompts-v45.json)

“萌、呆、幼稚”描述成年角色的穿搭和表演；“幼稚”在图中表现为孩子气的鼓脸、撅嘴、小幅跺脚。“性感”用贴合剪裁、自信视线和舒展站姿表现，“暴露／高露肤”则记录衣物覆盖程度，分别检索。

## 使用方法

先选择想表现的气质，再查看同一标签的两套造型。可以把“活泼”的姿态、“含蓄”的表情和“张扬”的配色组合；词条可单独添加到外观卡。露肤类别可按肩、背、腰、腿、领口和侧面切换。图例展示服装覆盖范围，全部保留不透明衣物覆盖私密部位。

'''
    for cid in ['persona_looks','coverage_looks']:
        cat=next(c for c in data['categories'] if c['id']==cid)
        text+=f"## {cat['name']} · {cat['count']}项\n\n[浏览全部](../index.html?section={cid})\n\n"
        for b in [b for b in boards if b['category']==cid]:
            text+=f"### {b['dimension']}\n\n[原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
            for item in b['items']:
                e=next(e for e in data['entries'] if e['id']==item['entry_id'])
                text+=f"- [{e['id']} · **{e['name']}**](../index.html?section={cid}&dimension={quote(e['dimension'])})：{e['description']}\n"
            text+='\n'
    (root/'docs/character-presence.md').write_text(text,encoding='utf-8')
