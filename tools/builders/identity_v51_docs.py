"""Identity directory, paired full-body studies and collectible component sets."""
from urllib.parse import quote
def write_identity_v51_docs(root,data):
    counts={c['id']:c['count'] for c in data['categories']}
    identity_boards=[b for b in data['boards'] if b.get('category') in data['meta']['identity_categories']]
    text=f'''# 身份与经典设定

[进入身份分组](../index.html?section=branch_identity_archetypes) · [当前{data['meta']['identity_count']}套身份](../index.html?section=branch_identity_archetypes) · [第52版扩充](identity-costumes-flexibility-v52.md) · [系统示例外观卡](../index.html?view=card&card_tab=examples) · [生成提示词与原图路径](../prompts/image-prompts-v51.json)

当前共{len(data['meta']['identity_kinds'])}种身份、{data['meta']['identity_count']}套全身造型，分为“地位与家世”“使命与职业身份”“经典人设与双重身份”。采用内置 image_gen 制作{len(identity_boards)}张左右双格对照图；每张图保持成年人物的面容、发色与标志物一致。全部角色25岁以上，服装为原创架空或现代创作方案。

| 类别 | 身份与设定 | 配图数 |
| --- | --- | ---: |
| 地位与家世 | 反派千金、落魄千金、女王、亡国公主、皇女、女领主 | {counts['identity_status']} |
| 使命与职业身份 | 圣女、女管家、女总裁、堕落圣女、赏金猎人、情报贩子、黑客、守护者 | {counts['identity_duties']} |
| 经典人设与双重身份 | 文学系、三无系、双重身份、复仇者 | {counts['identity_classic']} |

角色身份由衣物、道具、家徽、处境和表演共同交代。反派千金对比夜宴与议事；落魄千金保留旧吊坠和端正姿态；女王对比礼仪与议政；亡国公主保留逃亡前后的发辫和吊坠。圣女比较祈愿与巡礼，女管家比较执事与事务，女总裁比较商务与会谈。文学系采用成年读者的书册、手记和眼镜；三无系以少言、表情与动作幅度小的虚构表演表示。双重身份明确为同一人物的日间职员与夜间联络身份。

每种设定都有一张系统示例外观卡，包含两套整身参考和可选的发型、首饰、手套、表情或道具图鉴。打开系统示例即可查看集合，再保存为独立外观卡继续编辑。可选部件用于搭配扩展，不要求全部同时佩戴。

'''
    by_id={e['id']:e for e in data['entries']}
    for b in identity_boards:
        label=b['dimension'];example=next((i,c) for i,c in enumerate(data['combinations'],1) if c.get('identity_kind')==label)
        text+=f"## {label}\n\n[系统示例外观卡](../index.html?view=card&example={example[0]}) · [原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
        for item in b['items']:
            e=by_id[item['entry_id']]
            text+=f"- [{e['id']} · **{e['name']}**](../index.html?section={e['category']}&dimension={quote(e['dimension'])})：{e['description']}\n"
        text+='\n可选搭配图鉴：'+'、'.join(f"[{by_id[i]['name']}（{i}）](../index.html?section={by_id[i]['category']}&q={i})" for i in example[1]['entry_ids'][2:])+'。\n\n'
    (root/'docs/identity-archetypes.md').write_text(text,encoding='utf-8')
