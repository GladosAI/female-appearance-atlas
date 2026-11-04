"""Latest pose contact sheets with stable links, full originals and support annotations."""
from urllib.parse import quote

def write_pose_v54_docs(root,data):
    text='''# 多样 Pose 与角色摆姿扩充

[体态与动作](../index.html?section=pose) · [本轮64项](../index.html?section=clothing_new) · [300项动作总索引](pose-atlas.md) · [提示词与原图路径](../prompts/image-prompts-v54.json)

新增64个动作单帧，编号PO237—PO300，分成16组，每组4项。体态与动作现有300项，另有24项[柔韧、伸展与舞蹈姿态](../index.html?section=flexibility_poses)。旧编号、外观卡与原有图页保留。

本轮用内置 image_gen 制作16张四格图页。站姿与坐姿用竖格，沙发、地面和双人构图用宽格；每页按实际分隔线确定裁剪区域。人物与手足、必要家具及支撑接触完整保留，动作不以训练步骤编排。角色均为25岁以上成年人，穿完整服装。

## 分类索引

| 细分 | 数量 | 浏览 |
| --- | ---: | --- |
'''
    es=[e for e in data['entries'] if e.get('pose_v54_reference')]
    for dim in dict.fromkeys(e['dimension'] for e in es):text+=f"| {dim} | 4 | [进入](../index.html?section=pose&dimension={quote(dim)}) |\n"
    text+='\n每项标明视角、动作阶段和主要支撑。摆姿先看头、胸廓与骨盆的方向，再看手足位置；持物看手掌与物件接触；坐卧看座面、背垫和地面承重；双人看各自重心与接触手臂。图为单帧绘画参考，动态连续性可按角色和场景另行设计。\n\n'
    by_id={e['id']:e for e in es}
    for b in data['boards']:
        if b.get('edition')!=54:continue
        text+=f"## {b['dimension']}\n\n[浏览这一组](../index.html?section=pose&dimension={quote(b['dimension'])}) · [完整原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n| 编号与动作 | 视角 | 支撑 | 阶段 |\n| --- | --- | --- | --- |\n"
        for item in b['items']:
            e=by_id[item['entry_id']];text+=f"| [{e['id']} · {e['name']}](../index.html?section=pose&q={e['id']}) | {e['pose_view']} | {e['pose_support']} | {e['pose_phase']} |\n"
        text+='\n'
    (root/'docs/varied-poses-v54.md').write_text(text,encoding='utf-8')
