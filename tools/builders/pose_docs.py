"""Action atlas with supported poses, phases, and compact group index."""
from urllib.parse import quote
def write_pose_docs(root,data):
    es=[e for e in data['entries'] if e['category']=='pose'];added=[e for e in es if e.get('pose_expansion_reference')]
    text=f'# 体态与动作图鉴\n\n原有236项动作继续保留，第54版再增加64项镜头摆姿、坐卧构图、日常操作、舞台、运动、施法与双人互动，共 **{len(es)}项动作参考**；另有24项柔韧姿态单列。“坐姿、蹲跪与起身”保留48项，含二郎腿、四字腿、单膝跪、跪坐与起身过渡。打开 [体态与动作](index.html?section=pose)，或直接进入 [坐姿、蹲跪与起身](index.html?section=pose&dimension={quote("坐姿、蹲跪与起身")})。\n\n'
    text+='新增卡片标明视角、动作阶段和主要支撑点；人物采用完整不透明衣着。站立、坐卧、腾空和双人接触使用不同的支撑关系，先比较整体动作线，再观察肩髋旋转与肢体遮挡。卧姿、上肢、双人与运动组采用较宽图页，人物、手足和必要支撑物完整保留。\n\n'
    text+='拍照时的自拍、写真与多人站位另见 [摄影摆姿与合影48项](index.html?section=photo_poses)；[拍照Pose详表](photo-poses-v55.md)按景别、机位与视线浏览。\n\n'
    text+='## 新增动作分组\n\n| 分组 | 数量 | 浏览 |\n| --- | ---: | --- |\n'
    for g in data['meta']['pose_groups']:text+=f"| {g['name']} | {g['count']} | [查看](index.html?section=pose&dimension={quote(g['name'])}) |\n"
    text+='\n'
    for group in dict.fromkeys(e['dimension'] for e in added):
        entries=[e for e in added if e['dimension']==group];text+=f'## {group}\n\n'
        ids={e['visual']['board'] for e in entries}
        for b in data['boards']:
            if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 动作 | 视角 | 阶段 | 主要支撑 | 观察重点 |\n| --- | --- | --- | --- | --- | --- |\n'
        for e in entries:text+=f"| {e['id']} | {e['name']} | {e['pose_view']} | {e['pose_phase']} | {e['pose_support']} | {e['pose_focus']} |\n"
        text+='\n'
    text+='## 原有60项动作\n\n| 编号 | 名称 | 分组 | 观察重点 |\n| --- | --- | --- | --- |\n'
    for e in es:
        if not e.get('pose_expansion_reference'):text+=f"| {e['id']} | {e['name']} | {e['dimension']} | {e['description']} |\n"
    text+='\n配图由内置 imagegen 生成，完整原图保存于 images 目录，提示词见 [第28版提示词](image-prompts-v28.json) 、[第37版坐蹲跪起身提示词](image-prompts-v37.json) 和 [第54版多样Pose提示词](image-prompts-v54.json)。第37版编号PO205—PO236仍归入坐姿细分；第54版编号PO237—PO300按16个新细分浏览，详见 [多样Pose扩充](varied-poses-v54.md)。延伸阅读：[CLIP STUDIO 动作线与姿态](https://www.clipstudio.net/how-to-draw/archives/156164)、[Adobe 人体绘画](https://www.adobe.com/creativecloud/illustration/discover/how-to-draw-people.html)。\n'
    (root/'docs/pose-atlas.md').write_text(text,encoding='utf-8')
