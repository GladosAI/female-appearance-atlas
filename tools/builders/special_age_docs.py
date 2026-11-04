"""Edition 21 docs for special appearance variants and female life stages."""
def write_special_age_docs(root,data):
    import special_age_expansion as expansion
    cats={c['id']:c for c in data['categories']}
    topics=[('special-variants-atlas.md','特殊装扮与外观状态补充',expansion.SPECIAL_CATEGORIES,
        '第21版新增144项：浴巾裹身16、破损衣物16、成年抱胸遮挡视图16、液体浸染32、人偶与卡通玩偶服32、机械单侧义肢16、手抱玩偶16。均为25岁及以上成年角色参考，采用中性姿态；液体染衣和义肢连接均保持身体完整。','special'),
        ('female-ages-atlas.md','女性各年龄段图鉴',['female_life_stages'],
        '当前96项：连续年龄阶段正面与侧身32项，原有头部和全身32项，另有身高整体比例16项与成年三围16项，覆盖新生儿、婴幼儿、儿童、青少年、青年成人、中年、年长与高龄。页面默认显示 [年龄阶段并排对照](life-stage-comparison.md)，其正面与侧身按统一示意标尺和脚底基线显示，婴幼儿卧姿另组。所有阶段完整适龄着装。原始图页的各格按便于阅读的比例排版，格内人物高度不代表同一现实身高标尺；年龄是设定标签，个体外观存在差异。身高与三围数值另见 [尺寸设定专题](age-size-atlas.md)，所有数字为虚构创作设定，三围仅列成年参考。','female_life_stages')]
    for filename,title,cids,intro,scope in topics:
        entries=[e for e in data['entries'] if e['category'] in cids and (scope=='female_life_stages' or e.get('added_in')=='21.0')]
        text=f'# {title}\n\n{intro}\n\n打开 [分类浏览](index.html?section={scope}) 或 [本版新增](index.html?section=clothing_new)。\n\n| 类别 | 图例 |\n| --- | ---: |\n'
        for cid in cids:text+=f"| [{cats[cid]['name']}](index.html?section={cid}) | {sum(e['category']==cid for e in entries)} |\n"
        if scope=='female_life_stages':
            text+='\n## 原有头部与全身索引\n\n| 设定区间 | 头部编号 | 全身编号 |\n| --- | --- | --- |\n'
            for stage in dict.fromkeys(e['age_stage'] for e in entries if e.get('view_type')=='portrait'):
                pair=[e for e in entries if e['age_stage']==stage and e.get('view_type') in ['portrait','fullbody']]
                text+=f"| {pair[0]['age_range']} | {next(e['id'] for e in pair if e['view_type']=='portrait')} | {next(e['id'] for e in pair if e['view_type']=='fullbody')} |\n"
        for cid in cids:
            text+=f"\n## {cats[cid]['name']}\n\n{cats[cid]['guide']}\n"
            group=[e for e in entries if e['category']==cid]
            for dim in dict.fromkeys(e['dimension'] for e in group):
                subset=[e for e in group if e['dimension']==dim];ids={e['visual']['board'] for e in subset}
                text+=f'\n### {dim}\n\n'
                for b in data['boards']:
                    if b['id'] in ids:text+=f"![{b['title']}]({b['image']})\n\n"
                text+='| 编号 | 词条 | 可见结构 |\n| --- | --- | --- |\n'
                for e in subset:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n全部图页通过内置 imagegen 生成，保存于 images 目录。参见 [第21版提示词记录](image-prompts-v21.json) 与 [第22版提示词记录](image-prompts-v22.json)、[特殊装扮总览文档](special-costumes-atlas.md)、[来源说明](sources.md)。\n'
        (root/'docs'/filename).write_text(text,encoding='utf-8')
