"""Scene references keep people, activity and environment in the same example."""
import json


def write_scene_docs(root, data):
    entries = [entry for entry in data['entries'] if entry.get('scene_reference')]
    if not entries:
        return
    text = f'''# 场景与人物活动

[打开图鉴分组](../index.html?section=branch_scene_character_design)

共 {len(entries)} 项，归入“画风与视觉表现 → 场景与人物活动”。覆盖居家、学校校园、工作、社区服务、商业、文化游览、旅行、文体、历史影视、奇幻和科幻空间。每幅图中都有与地点相符的人物及活动，可同时参考环境布局、人物尺度、姿态、着装、道具接触与照明关系。

场景是可选素材。同一外观卡可以保留多个场景作为备选；案例人物的年龄、服装与动作不会自动变成角色限制。导出 AI 提示词时归入“场景与人物活动”，仅输出勾选词条的中英文名称。

所有配图均用内置 imagegen 原创生成，没有取用现成影视截图或游戏场景。历史、年代和神话空间为创作灵感，不能替代建筑、历史、医疗或生产设计资料。

'''
    if (root/'source/scene-plan-v73.json').exists():
        text+='当前96项场景采用清晰线稿、赛璐璐上色与纤细匀称的二次元人物造型。校园学生按初高中生呈现，教师保持成年形象；寄宿中学宿舍使用完整校服运动套装，毕业合影使用校服，不使用大学学位服或学位帽。中学授课与魔法学院课堂也已同步校正学生年龄语境。\n\n'
    for category in data['categories']:
        items = [entry for entry in entries if entry['category'] == category['id']]
        if not items:
            continue
        text += f"## {category['name']}\n\n[浏览 {len(items)} 项](../index.html?section={category['id']})\n\n"
        for image in dict.fromkeys(entry['visual']['image'] for entry in items):
            text += f"![{category['name']}](../{image})\n\n"
        text += '| 编号 | 名称 | English | 场景与活动 | 观察要点 |\n| --- | --- | --- | --- | --- |\n'
        for entry in items:
            text += f"| {entry['id']} | {entry['name']} | {entry['en']} | {entry['description']} | {entry['design_tip']} |\n"
        text += '\n'
    text += '## 生成与复核记录\n\n'
    text += '早期提示词保留原始制作记录；当前图像以最新重绘批次的复核记录和图页维护源为准。\n\n'
    for plan in sorted((root/'source').glob('scene-plan-v*.json')):
        edition = plan.stem.removeprefix('scene-plan-v')
        settings=json.loads(plan.read_text(encoding='utf-8'))
        if settings.get('replace_existing'):
            sources=' · '.join(f'[沿用第{str(version).split(".")[0]}批维护源](../source/contributions/scenes-v{str(version).split(".")[0]}.json)' for version in settings['revision_of'])
        else:sources=f'[词条与图页](../source/contributions/scenes-v{edition}.json)'
        text += f'- 第{edition}批：[生成提示词](../prompts/image-prompts-v{edition}.json) · {sources} · [图像复核记录](../source/scene-review-v{edition}.json)\n'
    (root/'docs/scenes-with-characters.md').write_text(text, encoding='utf-8')
