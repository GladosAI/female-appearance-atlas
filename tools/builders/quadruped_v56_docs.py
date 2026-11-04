"""Four-legged complete-animal reference index."""
def write_quadruped_v56_docs(root, data):
    es = [e for e in data['entries'] if e.get('quadruped_reference')]
    text = '''# 完全动物体态与四足装饰

[浏览4项配图](../index.html?section=quadruped_forms) · [兽娘与福瑞](anthro-atlas.md) · [生成提示词](../prompts/image-prompts-v56.json)

这组保留完整动物头颈、横向躯干、四条动物腿和自然尾部，四只脚均接触地面，只配少量帽子、领巾、发结或短披饰。小马两种、狐狸与猫各一种，均为原创幻想图例。

它与已有形态分开：BS016是双足直立马型福瑞；HY017是人形上身连接马躯的半人马；QF001、QF002没有人形上身或人手，采用完整四足马体。原有L1—L8程度对照继续保留，四足类别不作为统一的兽化百分比或社群标准。

![完整四足动物体态图例](../images/sheet-qf001-qf004.png)

| 编号 | 形态 | 可见结构 |
| --- | --- | --- |
'''
    for e in es:
        text += f"| [{e['id']}](../index.html?section=all&entry={e['id']}) | {e['name']} | {e['description']} |\n"
    text += '\n小马图可以承接四足小马的宽泛形态参考，不要求为每个角色另做特定毛色、标记或饰物。图鉴示意与原作截图、原作描述及年龄事实分开记录。四足图不套用人类年龄图鉴。\n\n配图使用内置 image_gen 制作，原图完整保存，按实际2×2分隔线裁切。\n'
    (root / 'docs/quadruped-forms-v56.md').write_text(text, encoding='utf-8')
