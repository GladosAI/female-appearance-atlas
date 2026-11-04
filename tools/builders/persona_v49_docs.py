"""Index current presence expansion and its related style/cultural costumes."""
from urllib.parse import quote
def write_persona_v49_docs(root,data):
    text='''# 圣洁、妖艳、清冷等气质与关联造型

[分类总目录](../index.html?view=directory) · [全部气质](../index.html?section=persona_looks) · [地雷系穿搭](../index.html?section=fashion_outfits&style=jirai) · [艺妓服饰](../index.html?section=traditional&dimension=艺妓·成年传统表演者造型) · [生成提示词](../prompts/image-prompts-v49.json)

新增12种气质各两套，共24套：圣洁、妖艳、清冷、病娇、厌世、疏离、天真、保持距离、空灵、肃穆、颓靡、倦怠。第49版完成时，气质类别累计76种、152套。另补4套地雷系穿搭与4套艺妓服饰，共32项，使用内置 image_gen 生成8张四格全身图页，所有角色25岁以上。

“保持隔离”按主动保持距离理解：掌心婉拒、后退半步、侧避和小包置于身前。与疏离的安静侧身、视线游离分开观察。“清冷”强调清雅与克制，“厌世”表现淡漠倦世，“倦怠”强调疲倦肢体；“病娇”以甜美微笑与执着凝视的反差表现。“妖艳”通过浓艳色彩、材质、唇眼妆和神态表示。它们是虚构角色表演标签，可与既有气质混搭。

地雷系原有16套，本轮新增4套，继续放在“服装风格与搭配”，支持“地雷女”别名。比较黑粉、黑紫、花边、领结、发饰与鞋袜，款式与性格标签分开归档。

艺妓／芸妓是传统表演身份，本轮4套放在“传统服饰与历史灵感”。图例比较持扇、舞扇、侧后腰带结构与自然妆面，采用成年表演者造型。芸妓与舞妓在和服和发饰繁简上的区别参考[日本驻悉尼总领馆《Geiko and maiko》](https://www.sydney.au.emb-japan.go.jp/document/english/japan_reports/JR50-4/JReports%20Vol%2050-4%20p.7.pdf)。配图为原创灵感改编，具体礼仪、衣装与妆面依地区、年代及表演场合变化。

所有图均完整保留发顶、手势、服装和鞋履；每格按实际分隔线裁切。可搜索上述名称或切换细分，每个词条可分别加入外观卡。

'''
    for b in [b for b in data['boards'] if b.get('edition')==49]:
        text+=f"## {b['dimension']}\n\n[原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
        for item in b['items']:
            e=next(e for e in data['entries'] if e['id']==item['entry_id'])
            text+=f"- [{e['id']} · **{e['name']}**](../index.html?section={e['category']}&dimension={quote(e['dimension'])})：{e['description']}\n"
        text+='\n'
    (root/'docs/presence-styles-v49.md').write_text(text,encoding='utf-8')
