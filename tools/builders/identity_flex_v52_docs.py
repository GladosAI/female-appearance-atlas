"""Latest identities, stage costumes and full-body flexibility index."""
from urllib.parse import quote
def write_identity_flex_v52_docs(root,data):
    text='''# 身份、功夫、小丑与柔韧姿态扩充

[本轮48项](../index.html?section=clothing_new) · [身份与经典设定](../index.html?section=branch_identity_archetypes) · [功夫装扮](../index.html?section=kungfu_outfits) · [小丑造型](../index.html?section=clown_outfits) · [柔韧姿态](../index.html?section=flexibility_poses) · [生成提示词与原图路径](../prompts/image-prompts-v52.json)

新增8种身份各两套：皇女、女领主、堕落圣女、复仇者、赏金猎人、情报贩子、黑客、守护者，共16套。功夫与小丑各4套；女性柔韧姿态24项，共48项配图。采用内置 image_gen 制作8张身份双格图页、2张服装四格图页和6张姿态四格图页。全部使用25岁以上成年角色，保留完整衣着与动作轮廓。

身份类别目前累计18种、36套。新增8张身份系统外观卡，以及功夫、小丑两张主题参考卡；系统示例总数60张。打开系统示例可直接浏览整身造型及相关部件，另存后继续编辑。

功夫装扮比较盘扣练功、武侠行旅、竞技与武馆教习；小丑比较彩色马戏、黑金菱格、白面泪点与街头表演。既有[武术训练装SP011](../index.html?section=sports&q=SP011)和[舞台小丑TC059](../index.html?section=special_costumes&q=TC059)保留，可与新增方向交叉参考。

柔韧姿态按立姿侧弯与伸展、坐姿前屈与开髋、劈叉与压腿、后弯支撑、单足舞蹈平衡、地面伸展与过渡六组浏览。比较肩与骨盆的方向、背线和四肢曲线，以及手掌、膝、小腿和足部的接触支撑。图为绘画与角色动作参考，不是训练步骤。

横向地面动作使用宽格子，立姿使用竖格子；每张图页按实际分隔线确定裁剪范围。系统示例中的部件是可选搭配参考，不要求同时使用。

'''
    by_id={e['id']:e for e in data['entries']}
    for b in [b for b in data['boards'] if b.get('edition')==52]:
        title=b['dimension'];text+=f"## {title}\n\n[原图](../{b['image']})"
        first=by_id[b['items'][0]['entry_id']]
        label=first.get('identity_kind')
        combo=next(((i,c) for i,c in enumerate(data['combinations'],1) if label and c.get('identity_kind')==label),None)
        if not combo and b['category'] in ['kungfu_outfits','clown_outfits']:
            ids={x['entry_id'] for x in b['items']};combo=next(((i,c) for i,c in enumerate(data['combinations'],1) if c.get('role_example') and ids<=set(c['entry_ids'])),None)
        if combo:text+=f" · [系统示例外观卡](../index.html?view=card&example={combo[0]})"
        text+=f"\n\n![{b['title']}](../{b['image']})\n\n"
        for item in b['items']:
            e=by_id[item['entry_id']];text+=f"- [{e['id']} · **{e['name']}**](../index.html?section={e['category']}&dimension={quote(e['dimension'])})：{e['description']}\n"
        if combo:text+='\n可选参考部件：'+'、'.join(f"[{by_id[i]['name']}（{i}）](../index.html?section={by_id[i]['category']}&q={i})" for i in combo[1]['entry_ids'] if i not in {x['entry_id'] for x in b['items']})+'。\n'
        text+='\n'
    (root/'docs/identity-costumes-flexibility-v52.md').write_text(text,encoding='utf-8')
