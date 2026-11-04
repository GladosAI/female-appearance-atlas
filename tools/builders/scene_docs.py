"""Scene references keep people, activity and environment in the same example."""


def write_scene_docs(root, data):
    entries = [entry for entry in data['entries'] if entry.get('scene_reference')]
    if not entries:
        return
    text = f'''# 场景与人物活动

[打开图鉴分组](../index.html?section=branch_scene_character_design)

共 {len(entries)} 项，归入“画风与视觉表现 → 场景与人物活动”。覆盖居家、工作、商业、旅行、文体、历史影视、奇幻和科幻空间。每幅图中都有与地点相符的人物及活动，可同时参考环境布局、人物尺度、姿态、着装、道具接触与照明关系。

场景是可选素材。同一外观卡可以保留多个场景作为备选；案例人物的年龄、服装与动作不会自动变成角色限制。导出 AI 提示词时归入“场景与人物活动”，仅输出勾选词条的中英文名称。

所有配图均用内置 imagegen 原创生成，没有取用现成影视截图或游戏场景。历史、年代和神话空间为创作灵感，不能替代建筑、历史、医疗或生产设计资料。

'''
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
    text += '[生成提示词](../prompts/image-prompts-v71.json) · [词条与图页](../source/contributions/scenes-v71.json) · [图像复核记录](../source/scene-review-v71.json)\n'
    (root/'docs/scenes-with-characters.md').write_text(text, encoding='utf-8')
