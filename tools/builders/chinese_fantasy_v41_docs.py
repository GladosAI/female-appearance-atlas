"""Publish original Chinese immortal and spirit outfit reference collection."""
def write_chinese_fantasy_v41_docs(root,data):
    es=[e for e in data['entries'] if e.get('chinese_fantasy_reference')]
    text='''# 中式仙女、妖女与精怪装束

[魔法、仪式与幻想身份](../index.html?section=branch_magic_religion) · [提示词](../prompts/image-prompts-v41.json)

新增32项原创成年角色全身图，分别归入“中式仙女与女仙”和“中式妖女与精怪”，各16项。两个类别位于：职业、主题与历史服装 → 魔法、仪式与幻想身份。

需要实际蛇尾、鱼尾或兽体下身时，可查看[半人形与复合躯体](../index.html?section=hybrid_body_forms)；本页蛇妖和鲤鱼精条目保留完整人形双腿。

仙女组比较广袖、束袖、云肩、披帛、叠裙、袍裤、发冠、玉佩与法具；妖女组比较完整人形衣着与耳、尾、角、鳞纹等局部异化。妖女是幻想身份标签，不表示角色善恶；它既包含灵怪化身，也包含妖修装束。

所有人物、服装组合、配色及纹样为原创仙侠设计，不是某件文物、某部作品人物或宗教服制的复原。古画和馆藏资料作为衣带流向、云肩及神话主题的阅读入口，不意味着全部款式在古籍中均有记载。飞天改编仅借鉴佛教天人乐舞的飘带与舞衣意象，与道教女仙的宗教身份区分。

'''
    for kind,cid,title in [('immortal','chinese_fairy_outfits','中式仙女与女仙'),('spirit','chinese_demoness_outfits','中式妖女与精怪')]:
        group=[e for e in es if e['chinese_fantasy_kind']==kind];b=next(b for b in data['boards'] if b['id']=='chinese-fantasy-v41-'+kind)
        text+=f"## {title}\n\n[打开16项配图](../index.html?section={cid})\n\n![{title}](../{b['image']})\n\n| 编号 | 装束 | 结构与主题 |\n| --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='## 资料与生成记录\n\n两张图页通过内置 image_gen 生成并保存在 images/，分别逐格对应XI001—XI016、YA001—YA016。以下为研究与术语入口，未复制馆藏图片。\n\n'
    used={r for e in es for r in e['related_reading']}
    for r in data['references']:
        if r['id'] in used:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/chinese-immortals-and-spirits.md').write_text(text,encoding='utf-8')
