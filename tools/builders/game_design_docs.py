"""Original game-character concept-method examples in the main atlas."""


def write_game_design_docs(root, data):
    entries = [entry for entry in data['entries'] if entry.get('game_design_reference')]
    if not entries:
        return
    text = f'''# 游戏角色原稿与设计方法

[打开图鉴分组](../index.html?section=branch_game_character_design)

共 {len(entries)} 项，归入“画风与视觉表现 → 游戏角色原稿与设计方法”。这里展示设计方法的具体案例，每项的备选图、局部图或过程图都保留在同一个词条内。

角色概念探索关注主题转译、轮廓、形状、明暗、配色和识别点；3A案例偏重服装结构、材质、功能与游戏镜头可读性；乙游案例关注立绘、差分、事件CG和动态准备；制作交接案例整理多视图、道具、结构、动作和设计阶段。

这些方法可以跨类型使用。3A不是一种固定画风，乙游也不限于单一画风或角色性别。女性图例以原创成年主角与配角示范，不对应任何真实游戏项目的生产要求。这些是可挑选的参考，不是本网站规定的必做流程。

## 如何阅读案例

先看词条要解决的设计问题，再看同稿保持不变的部分与正在比较的变量。例如剪影探索改变外形，配色探索保留线稿，表情差分保留人物身份，转面设定检查同一设计在不同方向的对应。

所有配图均用内置 imagegen 原创生成。不是已有游戏的原稿、截图或设计师作品；灰模、覆绘、动态分件和界面留白均为绘制的方法示意，没有附带模型、PSD、绑定或工程参数。多视图与结构仍需制作人员核对后才能用于实际制作。

AI提示词导出仍只包含勾选词条的中英文名称，按本次四个实际类别排列；不会自动插入案例人物的服装、年龄、说明或限制。

'''
    for category in data['categories']:
        items = [entry for entry in entries if entry['category'] == category['id']]
        if not items:
            continue
        text += f"## {category['name']}\n\n[浏览 {len(items)} 项](../index.html?section={category['id']})\n\n"
        for image in dict.fromkeys(entry['visual']['image'] for entry in items):
            text += f"![{category['name']}](../{image})\n\n"
        text += '| 编号 | 名称 | English | 观察重点 |\n| --- | --- | --- | --- |\n'
        for entry in items:
            text += f"| {entry['id']} | {entry['name']} | {entry['en']} | {entry['description']} |\n"
        text += '\n'
    text += '## 流程背景与相关阅读\n\n以下为开发团队、技术厂商与行业课程主办方的原始资料。它们提供相关流程背景，不表示本图鉴的每种案例都来自该来源，也不构成配图授权：\n\n'
    ids = {rid for entry in entries for rid in entry['related_reading']}
    for reference in data['references']:
        if reference['id'] in ids:
            text += f"- [{reference['title']}]({reference['url']}) · {reference['publisher']}。{reference.get('summary', '')}\n"
    text += '\n[生成提示词](../prompts/image-prompts-v69.json) · [图页与词条映射](../source/game-concept-sheets-v69.json)\n'
    (root/'docs/game-character-design.md').write_text(text, encoding='utf-8')
