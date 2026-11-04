"""Camera-specific posing index with framing and gaze annotations."""
from urllib.parse import quote

def write_photo_poses_v55_docs(root,data):
    text='''# 拍照 Pose：摄影摆姿与合影

[进入摄影摆姿](../index.html?section=photo_poses) · [基础体态与动作](../index.html?section=pose) · [提示词与原图路径](../prompts/image-prompts-v55.json)

新增48项拍照摆姿，编号PP001—PP048，分为12组，每组4项，单列于“身体与动作 → 动作与持物 → 摄影摆姿与合影”。原有300项体态动作和24项柔韧姿态继续保留。

图例侧重拍照时的视线、手部落点、肩髋朝向、机位和取景范围；自拍与镜面自拍分开，双人三人合影显示前后、高低和对称站位。33项全身，15项半身；半身取至大腿中段，保留完整头发、手势和手机，全身显示鞋履和支撑接触。景别逐项标注。

采用内置 image_gen 制作12张原创四格图页，人物均为25岁以上成年人。双人、三人组使用宽画幅，单人使用竖画幅；每页依实际分隔线裁剪，修正半身手臂、伞顶留白与编号清晰度，保留初版和修正版原图。表情与体型可替换，重点是组合思路。

## 目录

| 拍摄场景 | 数量 | 浏览 |
| --- | ---: | --- |
'''
    es=[e for e in data['entries'] if e.get('photo_pose_reference')]
    for dim in dict.fromkeys(e['dimension'] for e in es):text+=f"| {dim} | 4 | [查看](../index.html?section=photo_poses&dimension={quote(dim)}) |\n"
    text+='\n拍摄组合可以从“景别 → 身体方向 → 手部落点 → 视线 → 表情”依次选择。照片里的自然瞬间也可作为角色动作单帧；若要细看膝足支撑或连续动作，可回到基础体态图鉴。\n\n'
    by_id={e['id']:e for e in es}
    for b in data['boards']:
        if b.get('edition')!=55:continue
        text+=f"## {b['dimension']}\n\n[浏览这一组](../index.html?section=photo_poses&dimension={quote(b['dimension'])}) · [完整原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n| 编号与摆姿 | 景别 | 机位 | 视线 |\n| --- | --- | --- | --- |\n"
        for item in b['items']:
            e=by_id[item['entry_id']];text+=f"| [{e['id']} · {e['name']}](../index.html?section=photo_poses&q={e['id']}) | {e['photo_framing']} | {e['camera_height']} | {e['gaze_direction']} |\n"
        text+='\n'
    (root/'docs/photo-poses-v55.md').write_text(text,encoding='utf-8')
