"""Nun, story-state and fictional age/size comparison documents."""
def write_nun_states_growth_docs(root,data):
    topics=[('nun-atlas.md','修女装扮图鉴',['nun_costumes'],'32套成年角色服装，按长袍与头部包覆、日常与幻想改编各16套整理。实际修会与地区服装有差异，图鉴是原创部件与造型参考。','nun_costumes'),
        ('sleep-coma-death-atlas.md','睡眠、昏迷与长眠剧情状态图鉴',['face_states'],'第22版新增48项：睡眠、昏迷、长眠各16项。采用成年角色的非血腥剧情面部图例；不能只凭闭眼、面色或表情判断真实意识与生命状态。','face_states'),
        ('age-size-atlas.md','身高、比例与成年三围设定图鉴',['female_life_stages'],'第22版新增32项：中性身高与整体比例16项、成年三围与体型16项。数字均为虚构角色设定，图像近似表现轮廓；婴幼儿采用卧长标签，三围仅存在于明确成年参考中。本专题保留第22版的原始尺寸设定；页面可切换“全部参考词条”查看。连续年龄轮廓另见 [阶段并排对照](life-stage-comparison.md)。','female_life_stages')]
    for filename,title,cids,intro,scope in topics:
        entries=[e for e in data['entries'] if e['category'] in cids and e.get('added_in')=='22.0']
        text=f'# {title}\n\n{intro}\n\n打开 [分类浏览](index.html?section={scope}) 或 [当前新增索引](index.html?section=clothing_new)。\n'
        if filename=='age-size-atlas.md':
            text+='\n## 数值设定\n\n全部单位为cm；三围是周长，不是正面宽度。头身比是画风设定。以下数字不代表同龄平均值、理想值或发育标准。\n\n| 编号 | 角色设定 | 身高／卧长 | 头身比 | 成年胸／腰／臀围 |\n| --- | --- | ---: | ---: | --- |\n'
            for e in entries:
                label='卧长' if e.get('stature_kind')=='length' else '身高';value=e.get('length_cm',e.get('height_cm'))
                bwh=f"{e['bust_cm']} / {e['waist_cm']} / {e['hip_cm']}" if e.get('adult_measurement_reference') else '—'
                text+=f"| {e['id']} | {e['name']} | {label}{value} | {e['head_units']} | {bwh} |\n"
        for dim in dict.fromkeys(e['dimension'] for e in entries):
            subset=[e for e in entries if e['dimension']==dim];ids={e['visual']['board'] for e in subset}
            text+=f'\n## {dim}\n\n'
            for board in data['boards']:
                if board['id'] in ids:text+=f"![{board['title']}]({board['image']})\n\n"
            text+='| 编号 | 词条 | 可见结构 |\n| --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n配图使用内置 imagegen 生成并保存于 images 目录，尺寸以本页数值表为准。参见 [第22版提示词](image-prompts-v22.json)、[女性年龄图鉴](female-ages-atlas.md)、[面部图鉴](facial-atlas.md) 与 [来源说明](sources.md)。\n'
        (root/'docs'/filename).write_text(text,encoding='utf-8')
