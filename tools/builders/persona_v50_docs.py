"""Readable index of ten new adult-character acting directions."""
from urllib.parse import quote
def write_persona_v50_docs(root,data):
    text='''# 软萌、卡哇伊、大小姐等气质与性格表演

[气质分类](../index.html?section=persona_looks) · [全部气质](../index.html?section=persona_looks) · [生成提示词与原图路径](../prompts/image-prompts-v50.json)

新增10种表现方向，各有两套全身搭配：软萌、卡哇伊、千金大小姐、精神异常、邋遢、拘谨、洁癖、病态、反差、占有欲。气质类别累计86种、172套。全部采用25岁以上成年原创角色，使用内置 image_gen 制作5张四格全身图页，编号QL153–QL172；原有编号与外观卡继续兼容。

软萌侧重绒感针织、柔和色彩与温软姿态；卡哇伊用糖果色、小结饰、活泼眉眼和明快动作表现。千金大小姐比较滚边套装、茶会裙、珍珠饰物、提包及矜持站姿。

精神异常以勉强微笑与紧张眉眼的错位、游离目光、绞握双手等失序表演表示；病态以冷调苍白妆面、眼下阴影和疲弱姿态表示；洁癖以检查袖口、规整衣褶和擦拭自己的手袋表示。这些是虚构角色的创作标签，配图不作为现实健康判断依据。

邋遢比较皱褶、未收齐的衣角、不齐袖口、散发和歪围巾；拘谨比较双肘贴身、并脚、握腕与捏紧包柄。反差分为“甜装冷面”和“硬朗衣着配羞涩神态”；占有欲通过护住自己的纪念盒或手袋、凝视和收紧手势表示。

可搜索“软萌”“卡哇伊／kawaii”“大小姐”“失序表演”“不修边幅”“局促”“洁癖”“病感造型”“反差萌”“独占感”，也可直接切换细分。全身图保留完整发顶、手势、衣物与鞋履，按实际分隔线裁切；每项可单独加入外观卡。

'''
    for b in [b for b in data['boards'] if b.get('edition')==50]:
        text+=f"## {b['dimension']}\n\n[原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
        for item in b['items']:
            e=next(e for e in data['entries'] if e['id']==item['entry_id'])
            text+=f"- [{e['id']} · **{e['name']}**](../index.html?section=persona_looks&dimension={quote(e['dimension'])})：{e['description']}\n"
        text+='\n'
    (root/'docs/presence-acting-v50.md').write_text(text,encoding='utf-8')
