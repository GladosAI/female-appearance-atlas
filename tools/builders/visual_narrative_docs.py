"""Single comic panels and film visual-development drawings in the main atlas."""


def write_visual_narrative_docs(root,data):
    entries=[entry for entry in data['entries'] if entry.get('visual_language_reference')]
    if not entries:return
    comic_count=sum(bool(entry.get('comic_panel_reference')) for entry in entries)
    film_count=sum(bool(entry.get('film_design_reference')) for entry in entries)
    text=f'''# 漫画单格与影视关键帧

[漫画单格与格内表现](../index.html?section=branch_comic_panel_language) · [影视分镜与关键帧设计](../index.html?section=branch_film_visual_development)

共 {len(entries)} 项，其中漫画单格 {comic_count} 项、影视设计 {film_count} 项，位于主目录“画风与视觉表现”。每项是一幅独立示意，不依赖额外的生成页面。

漫画部分关注一格里的格框与画幅、用墨与笔触、人物与场景主次、痕迹与回忆、动势、符号、气泡与拟声字；这些表达可与不同漫画画风组合。出框只突破示例内部的格框；画中画是同一示例中的细节插格。窄横格、竖长格等的内框保留在完整示例图中，不把网站卡片裁成对应形状。

眼镜反光、空白眼、灵魂出窍、石化、融化、大汗滴和青筋等属于夸张的漫画表演符号；结合上下文表达情绪，不代表实际生理状态。回忆叠画在同一格里叠入主观意象，与表示连续动作的残影区分。虚线、波浪、画外对白和图像心声展示气泡的语气与信息来源。图鉴按视觉作用命名，不把这些名称当作统一行业术语。

影视部分包括分镜缩略草图、清线与灰阶分镜、布局和表演稿、预演帧，以及凝聚空间、人物、动作、情绪、灯光和特效的概念关键帧。这里按创作用途归纳，不能视作所有剧组统一的命名标准。

色彩脚本通常是一组画面，本图鉴取其中单帧展示光色方案。“概念关键帧”也不同于动画插值关键点和视频编码I帧。覆绘示例以本项目AI原创画面模拟设计过程，没有使用真实剧组实拍底图。

所有配图均使用内置 imagegen 原创生成，非已有漫画页、影视截图或制作公司的设计原稿。示例文字用于展示气泡与版面，提示词导出仍只包含所勾选词条的中英文名称。

'''
    for category in data['categories']:
        items=[entry for entry in entries if entry['category']==category['id']]
        if not items:continue
        text+=f"## {category['name']}\n\n[浏览 {len(items)} 项](../index.html?section={category['id']})\n\n"
        for image in dict.fromkeys(entry['visual']['image'] for entry in items):
            text+=f"![{category['name']}](../{image})\n\n"
        text+='| 编号 | 名称 | English | 观察重点 |\n| --- | --- | --- | --- |\n'
        for entry in items:
            text+=f"| {entry['id']} | {entry['name']} | {entry['en']} | {entry['description']} |\n"
        text+='\n'
    text+='## 术语与流程参考\n\n这些链接提供术语和工作流程背景，配图没有取用其中图片：\n\n'
    ids={rid for entry in entries for rid in entry['related_reading']}
    for reference in data['references']:
        if reference['id'] in ids:text+=f"- [{reference['title']}]({reference['url']}) · {reference['publisher']}\n"
    text+='\n## 配图与生成记录\n\n'
    for edition in sorted({int(entry['added_in'].split('.')[0]) for entry in entries}):
        manifest='visual-narrative-sheets-v68.json' if edition==68 else f'comic-panel-sheets-v{edition}.json'
        text+=f'- 内容版{edition}：[生成提示词](../prompts/image-prompts-v{edition}.json) · [图页与词条映射](../source/{manifest})\n'
    (root/'docs/comic-film-visuals.md').write_text(text,encoding='utf-8')
