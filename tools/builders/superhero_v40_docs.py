"""Publish the superhero costume reference collection and source links."""
from urllib.parse import quote

def write_superhero_v40_docs(root, data):
    es=[e for e in data['entries'] if e.get('superhero_reference')]
    text='''# 超级英雄与超级女杰

[打开32项配图](../index.html?section=superhero_outfits) · [魔法、仪式与幻想身份](../index.html?section=branch_magic_religion) · [生成提示词](../prompts/image-prompts-v40.json)

目录路径：职业、主题与历史服装 → 魔法、仪式与幻想身份 → 超级英雄与超级女杰。

16项披风、面罩与战甲轮廓，以及16项能力与装备类型，全部提供原创成年英雄的全身佩戴图。先比较整体轮廓，再看胸徽、领口、披风固定点、面罩、手套、腰带与靴，最后观察装备和小型能力特效。

全部图例使用原创人物、徽记与服装，非官方设定图，不对应真人演员。女超人、神奇女侠等名称作为主题参考及官方阅读入口，图例不表示这些角色的原作造型。前16项从披风飞行、亚马逊战士、蒙面义警、舞台魔术与羽翼等主题提炼轮廓；后16项按能力和装备组织。可直接搜索“女超人”“Supergirl”等主题词找到对应的原创示意。

'''
    for kind,name in [('silhouette','披风、面罩与战甲英雄'),('original','原创能力与装备型英雄')]:
        group=[e for e in es if e['superhero_kind']==kind]
        b=next(b for b in data['boards'] if b['id']=='superhero-v40-'+kind)
        text+=f"## {name}\n\n[只看本组](../index.html?section=superhero_outfits&dimension={quote(name)})\n\n![{name}](../{b['image']})\n\n| 编号 | 装束 | 身份与外观观察 |\n| --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='## 来源与生成记录\n\n两张图页通过内置 image_gen 生成，保存在 images/，逐格对应SH001—SH032。最初的具体角色装束图页未能通过生成工具检查，最终采用原创装束示意。以下官方来源用于核对主题阅读中的人物身份、英雄题材和作品入口；不代表官方认可生成插图。\n\n'
    used={r for e in es for r in e['related_reading']}
    for r in data['references']:
        if r['id'] in used:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/superhero-costumes.md').write_text(text,encoding='utf-8')
