"""Current age-comparison entry point; preserve earlier size-reference appendices."""
def write_life_comparison_docs(root,data):
    entries=[e for e in data['entries'] if e.get('comparison_reference')]
    text='# 女性身体年龄阶段并排对照\n\n第23版新增32幅图：16个年龄阶段各一幅正面和侧身参考。打开 [年龄阶段对照页](index.html?section=female_life_stages)，默认先看同一标尺、同一脚底基线的连续年龄轮廓；切换“放大细看”可以在图内横向滚动。点击人物查看该阶段说明。\n\n'
    text+='各阶段采用相近的普通长袖上衣、长裤和平底鞋，减少服装和多种体型造成的干扰。婴幼儿俯视卧姿与卧姿侧视另组比较，不与站立身高混排。原有面容、全身及成年尺寸资料在“全部参考词条”中继续提供。\n\n'
    text+='图例是完整着装的原创年龄阶段示例，标尺只用于保持图内相对大小。青春期的变化时序和各阶段体态有个体差异，不是临床发育分级或平均体型标准。\n\n'
    text+='| 年龄阶段 | 正面／俯视 | 侧身／侧视 | 观察要点 |\n| --- | --- | --- | --- |\n'
    front=sorted((e for e in entries if e['comparison_view']=='front'),key=lambda e:e['comparison_order'])
    for e in front:
        side=next(x for x in entries if x['age_stage']==e['age_stage'] and x['comparison_view']=='side')
        text+=f"| {e['age_range']} | {e['id']} | {side['id']} | {e['comparison_observation']} |\n"
    text+='\n## 原始图页\n\n网页将下方原图中的完整人物裁切显示，按同一示意标尺排在一起；原图保持未修改。\n\n'
    for b in data['boards']:
        if any(x['entry_id'] in {e['id'] for e in entries} for x in b['items']):text+=f"![{b['title']}]({b['image']})\n\n"
    text+='配图使用内置 imagegen。参见 [第23版提示词](image-prompts-v23.json)、[年龄完整图鉴](female-ages-atlas.md)、[既有尺寸设定表](age-size-atlas.md)、[NHS：成长阶段的整体变化与个体时序](https://www.justonenorfolk.nhs.uk/child-development-additional-needs/supporting-development/puberty/) 与 [来源说明](sources.md)。\n'
    (root/'docs/life-stage-comparison.md').write_text(text,encoding='utf-8')
