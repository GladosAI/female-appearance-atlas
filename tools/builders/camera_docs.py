"""Document camera references in the main atlas, not in a separate diagram tool."""


def write_camera_docs(root, data):
    entries=[entry for entry in data['entries'] if entry.get('camera_reference')]
    if not entries:return
    text=f'''# 视角与拍摄图鉴

位于主目录 **画风与视觉表现** 中，共 {len(entries)} 项配图参考。

[视角、机位与景别](../index.html?section=branch_camera_viewpoints) · [构图、景深与镜头](../index.html?section=branch_camera_framing_focus) · [镜头语言与叙事](../index.html?section=branch_camera_language)

观察方向、机位高度、景别、构图、景深和透视是不同的维度，可分别检索并加入外观卡。正面不等于平视，半身不等于近景角度；背景虚化也不是一种人物朝向。

配图由内置 imagegen 生成，使用同类服装与场景便于比较。它们是视觉示意，不是精确镜头或角度标定；左右方向按画面中的面向描述。前景对焦条目有意让后方人物虚化。

镜头语言条目使用左到右三格分镜，标明关键阶段或镜头组合；静态分镜不等于真实影片，不完整表示时长、速度和摄影稳定性。正反打、长镜头等须结合图例旁的阅读顺序理解。

'''
    for category in data['categories']:
        items=[entry for entry in entries if entry['category']==category['id']]
        if not items:continue
        text+=f"## {category['name']}\n\n[打开 {len(items)} 项](../index.html?section={category['id']})\n\n"
        images=list(dict.fromkeys(entry['visual']['image'] for entry in items))
        for image in images:text+=f"![{category['name']}配图](../{image})\n\n"
        text+='| 编号 | 名称 | English | 观察重点 |\n| --- | --- | --- | --- |\n'
        for entry in items:text+=f"| {entry['id']} | {entry['name']} | {entry['en']} | {entry['description']} |\n"
        text+='\n'
    text+='[视角图例提示词](../prompts/image-prompts-v66.json) · [镜头语言提示词](../prompts/image-prompts-v67.json)\n'
    (root/'docs/camera-visuals.md').write_text(text,encoding='utf-8')
    cinematic=[entry for entry in entries if entry.get('cinematic_reference')]
    if cinematic:
        guide=f'# 镜头语言与叙事\n\n[打开主图鉴 · {len(cinematic)}项](../index.html?section=branch_camera_language) · [全部视角与拍摄资料](camera-visuals.md)\n\n'
        guide+='每项是一条从左到右阅读的三格分镜。推拉是机位移动，变焦是焦距变化，转焦改变清晰的距离层次；长镜头指连续拍摄而不是长焦。主观视点和建立、反应等功能可与不同景别、构图组合。\n\n'
        guide+='| 编号 | 镜头语言 | 分镜顺序 | 含义 |\n| --- | --- | --- | --- |\n'
        for entry in cinematic:guide+=f"| {entry['id']} | {entry['name']}（{entry['en']}） | {' → '.join(entry['sequence_labels'])} | {entry['description']} |\n"
        source_ids={rid for entry in cinematic for rid in entry['related_reading']}
        guide+='\n## 术语参考\n\n配图为本项目生成，以下是术语参考资料，不是图像来源：\n\n'
        for reference in data['references']:
            if reference['id'] in source_ids:guide+=f"- [{reference['title']}]({reference['url']}) · {reference['publisher']}\n"
        guide+='\n[生成提示词](../prompts/image-prompts-v67.json) · [图页清单](../source/cinematic-sheets-v67.json)\n'
        (root/'docs/cinematic-language.md').write_text(guide,encoding='utf-8')
