"""Current special-costume and observable hair-state topic documents."""
def write_costume_hair_docs(root,data):
    import costume_hair_expansion as expansion
    categories={c['id']:c for c in data['categories']}
    topics=[('special-costumes-atlas.md','特殊装扮图鉴',data['meta']['special_costume_categories'],
        f"当前共{data['meta']['special_costume_count']}项，第36版新增48套情趣主题成衣；第27版新增32种职业、舞台与奇幻身份各2套，共64套；魔法少女与忍者装扮64套继续提供；体操、啦啦队、死神和维密风格秀场64套继续提供；32套修女装扮保留；此前144项特殊外观继续保留。浴巾裹身、破损、成年遮挡视图、浸染、人偶玩偶服、义肢和抱玩偶，以及此前的女扮男装、僵尸与吸血鬼、囚犯与匪徒、特种部队、情趣主题、湿水衣物以及其他特殊装扮分别浏览。情趣成衣使用成年尺码中性灰服装人台；湿水造型说明外层水渍和不透明内搭。",
        'special'),
        ('hair-states-atlas.md','头发形态与状态图鉴',['hair_states'],
        '第20版新增64项，分睡醒与简易打理、湿透油润与干燥、烫卷与运动、白发稀疏与颜色变化四组，每组16项。可与原有剪裁、刘海、扎编和完整发型组合使用。发色、稀疏和干哑等只表示外观，不能据此确认营养状况或具体病因。',
        'hair_states')]
    for filename,title,cids,intro,scope in topics:
        es=[e for e in data['entries'] if e['category'] in cids]
        text=f'# {title}\n\n{intro}\n\n打开 [分类浏览](index.html?section={scope})，或查看 [本次新增](index.html?section=clothing_new)。页面右下角在下滚后出现“返回顶部”按钮，电脑和手机均可使用；系统减少动态效果设置开启时直接返回。\n\n| 类别 | 配图词条 |\n| --- | ---: |\n'
        for cid in cids:text+=f"| [{categories[cid]['name']}](index.html?section={cid}) | {categories[cid]['count']} |\n"
        for cid in cids:
            cat=categories[cid];group=[e for e in es if e['category']==cid]
            text+=f"\n## {cat['name']}\n\n{cat['guide']}\n"
            shown_boards=set()
            for dim in dict.fromkeys(e['dimension'] for e in group):
                dim_es=[e for e in group if e['dimension']==dim]
                board_ids={e['visual']['board'] for e in dim_es}
                text+=f'\n### {dim}\n\n'
                for board in data['boards']:
                    if board['id'] in board_ids and board['id'] not in shown_boards:
                        text+=f"![{board['title']}]({board['image']})\n\n";shown_boards.add(board['id'])
                text+='| 编号 | 词条 | 可见结构 |\n| --- | --- | --- |\n'
                for e in dim_es:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n配图使用内置 imagegen 生成并检查编号与格子映射。参见 [第20版提示词](image-prompts-v20.json) 与 [第21版提示词](image-prompts-v21.json) 与 [第22版提示词](image-prompts-v22.json)、[第27版提示词](image-prompts-v27.json)、[第36版提示词](image-prompts-v36.json)、[完整头发图鉴](hair-atlas.md) 与 [来源说明](sources.md)。\n'
        (root/'docs'/filename).write_text(text,encoding='utf-8')
