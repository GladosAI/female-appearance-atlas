"""One hierarchy for the directory, filters, results and offline documentation."""
import copy,json

def build_navigation(root,data):
    result=copy.deepcopy(json.loads((root/'source/navigation.json').read_text(encoding='utf-8')))
    cats={c['id']:c for c in data['categories']};assigned=[];section_ids=[];paths={}
    for group in result['groups']:
        group['scope']='topic_'+group['id'];flattened=[]
        for section in group['sections']:
            section['scope']='branch_'+section['id'];section_ids.append(section['id'])
            section['count']=sum(cats[c]['count'] for c in section['categories'])
            section['category_count']=len(section['categories']);flattened.extend(section['categories'])
            for cid in section['categories']:paths[cid]={'domain':group['scope'],'section':section['scope']}
        assert flattened==group['categories'],group['id']
        group['count']=sum(cats[c]['count'] for c in flattened);group['category_count']=len(flattened);assigned.extend(flattened)
    assert len(assigned)==len(set(assigned)) and set(assigned)==set(cats),'Categories must have exactly one primary path'
    assert len(section_ids)==len(set(section_ids)),'Repeated section id'
    result.update(entry_count=sum(g['count'] for g in result['groups']),category_count=len(assigned),section_count=len(section_ids),category_paths=paths)
    assert result['entry_count']==len(data['entries'])
    result['style_categories']=[{'id':'style_'+f['id'],'style_id':f['id'],'name':f['name'],'count':f['clothing_count'],'guide':f['guide']} for f in data['style_families']]
    return result

def write_navigation_docs(root,data,navigation):
    cats={c['id']:c for c in data['categories']}
    text=f"# 图鉴总目录\n\n{len(navigation['groups'])}个领域 → {navigation['section_count']}个分组 → {len(cats)}个类别 → 类别内细分，共{len(data['entries'])}项配图。每个类别只有一个主要归属。\n\n[打开图鉴目录](../index.html?view=directory) · [查找与筛选说明](find-and-browse.md)\n\n"
    for g in navigation['groups']:
        text+=f"## {g['name']}\n\n{g['note']} 共{g['count']}项。 [领域全部](../index.html?section={g['scope']})\n\n"
        for s in g['sections']:
            text+=f"### {s['name']}\n\n[分组全部 · {s['count']}项](../index.html?section={s['scope']})\n\n| 类别 | 配图词条 | 浏览 |\n| --- | ---: | --- |\n"
            for cid in s['categories']:
                c=cats[cid];name=navigation.get('category_labels',{}).get(cid,c['name'])
                text+=f"| {name} | {c['count']} | [词条](../index.html?section={cid}) · [详表](atlas.md#{cid}) |\n"
            text+='\n'
    text+='## 快捷专题\n\n专题汇集多个类别，不计入主目录数量。风格是服装筛选条件，可与类别、细分和关键词叠加。\n\n'
    for s in navigation['shortcuts']:text+=f"- [{s['name']}](../index.html?section={s['id']})\n"
    text+='\n## 专题资料\n\n'
    for doc in navigation['documents']:text+=f"- [{doc['name']}]({doc['path'].removeprefix('docs/')})\n"
    (root/'docs/directory.md').write_text(text,encoding='utf-8')
    guide='''# 目录与检索使用说明

目录按“领域 → 分组 → 类别 → 细分”逐级收窄。首页各领域可直接进入，也可展开某个领域的完整类别。体态与持物在身体与动作，机械义肢也归于身体；配饰中的装备与Cosplay道具分别浏览。画风是独立的表现媒介与视觉语言，不是服装风格筛选。

## 查找流程

1. 知道名称、编号或特征：在首页搜索全部图鉴，输入时可选择分类或词条建议。多个关键词用空格连接，所有词都需要匹配；20D等D数作精确数值查找。
2. 只知道大致方向：从目录进入领域或分组，再选择类别和细分。每级下拉菜单只列出当前上级的选项。
3. 需要服装风格：展开筛选，选择哥特、洛丽塔、地雷系等。风格可与服装类别和关键词叠加，不再是独立目录。
4. 没有结果：查看当前条件条，可单独移除关键词、风格或细分，也可扩大到全部图鉴。“清空筛选”回到当前目录的完整内容，“全部重置”回到全图鉴。

进入其他目录时保留关键词；从首页目录进入时开始新的浏览。搜索框下方始终显示当前范围。词条卡片和分类图页使用同一结果集合，切换展示保留条件；图页中只列出匹配编号。

词条列表先显示一批内容，滚动接近底部时自动追加下一批，无需点击“再显示”。切换分类、搜索或筛选后按新的结果加载；年龄与体型并排对照、分类图页不触发词条追加。从外观卡返回浏览时，保留已经加载的内容和浏览位置。

词条详情的每张图片下方提供“下载图片”和“复制图片”。下载为当前词条裁切后的独立 PNG，文件名包含编号与名称；有全身／近景或佩戴／物件图时可分别操作。复制会将单张 PNG 放入剪贴板，可粘贴到支持图片的应用；浏览器不支持或未授权时会明确提示。直接打开本地 index.html 也可使用，离线包中 images/export-data 是配套读取数据，需与其他图片文件一并保留。

点击左侧目录中的类别或“查找图鉴”后，页面直接定位到结果标题，从图鉴内容开始浏览。上方的搜索、筛选仍可向上滚动使用。目录工具栏的“全部展开”和“全部收起”作用于所有领域及分组，“定位当前”展开并定位当前路径；这些操作只影响目录本身。

类别标题下方直接展示“按细分浏览”，每组选项标明结果数，当前选择有高亮与勾选。“全部”可恢复当前类别的完整内容；超过8组时可展开其余选项。没有更多细分的类别会明确提示。向下浏览长列表时，可用右下角“切换细分”返回这些选项。搜索和风格条件可以继续叠加，切换词条卡片或分类图页会保留细分选择。

## 保存与返回

系统示例是一组具体人物的角色卡，按日常、校园运动、职业旅途、年代礼仪、舞台时尚、奇幻、科幻、兽人与异形、Cosplay等题材组织。每张卡的外貌、服装、表情、动作和饰物服务于同一人物与当前场景，整组通过不同角色展现多样性。可按题材、精选角色或关键词查找，用上一角色／下一角色连续浏览。简介与配色保存在备注中，AI提示词仍只导出已勾选词条名称。旧链接保留原卡，点击返回列表会保留题材与搜索条件。

目录切换、筛选和展示切换可用浏览器前进或后退恢复。输入关键词时更新当前地址；复制地址可恢复分类、关键词、风格、细分、排序及展示方式。打开词条详情后，地址还会记录编号。

外观卡页面集中管理“我的外观卡”和“系统示例”。每张个人卡点击“编辑”后才显示名称与设定，修改自动保存，点击“完成编辑”回到图鉴集合。浏览图鉴时点击“＋ 外观卡”，即可在按钮旁选择卡片或新建；默认选中最近一次成功添加的卡片，确认后加入。已收录的部件会标记且不会重复添加，同一部件可以加入多张卡。“返回图鉴浏览”保留浏览位置；打开、编辑、复制或导入卡片不会改变最近添加的默认卡。系统示例可另存为个人卡后编辑，页面底部有辅助资料“人设模板”。

打开一张外观卡后，点击“导出AI提示词”可组合该卡的外观特征。首次打开默认全部勾选，再次打开自动恢复上次的勾选与手动修改；支持全选、全不选与逐项勾选。选项使用连续网格，可切换按类别或加入时间排序，个人卡默认最新加入在前；排序不改变勾选和手动修改的提示词。选项采用上图下名称的紧凑网格，点击图例或卡片留白切换勾选，点击名称查看完整介绍；关闭介绍后保留勾选和手动编辑的提示词。也可用键盘聚焦复选框后按空格操作。提示词在打开时和勾选变化后自动更新，开头为“请根据以下外观词条设计女性角色。同一类别有多个选项时，将它们作为备选分别搭配，生成一张或多张角色图像。”。各分类下每个词条独占一行，仅列中文名称与英文名称；同类多个选项并列，供模型组合或生成多种方案。用户可直接编辑提示词并复制给生图模型，更改勾选会按当前选择重新整理并覆盖手动编辑。该窗口中的勾选不会修改外观卡或设定备注。勾选和编辑时直接自动保存，不再需要保存按钮；历史按每次编辑会话保留，最多50条，可在窗口内恢复或删除。清空勾选或手动清空提示词也会保存。个人卡的导出与备份会携带对应方案历史，导入时跟随新卡恢复。

清空部件和删除整卡并列显示，均需在页面内二次确认，确认后仍可撤销；清空保留名称与设定。名称、备注和部件的修改只影响正在编辑的那张卡。图鉴集合不再分独立类别区块，默认按加入时间倒序，可用排序按钮切换为同类相邻的类别顺序；类内仍是新到旧。系统示例没有个人加入时间，默认保留示例顺序。排序只改变显示，不改写收藏或备份顺序。

旧版单张外观卡自动迁移，原始记录继续保留。单张导出保持旧版格式兼容，“备份全部”保存全部个人卡；导入单张或整库备份会新增卡片，保留原有卡片。所有个人卡保存在当前浏览器，建议定期导出备份。旧版组合示例地址会进入外观卡内的系统示例。

体型与年龄保留并排对照；选择细分或使用搜索时可查看匹配词条。发饰与眼镜保留物件图、佩戴图切换。资料与来源独立浏览，原有组合示例统一在外观卡中使用。

[返回目录](../index.html?view=directory)
'''
    (root/'docs/find-and-browse.md').write_text(guide,encoding='utf-8')

def write_usage_readme(root):
    d=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'));n=json.loads((root/'data/navigation.json').read_text(encoding='utf-8'));m=d['meta'];major=m['version'].split('.')[0]
    text=f"# 女性之美\n\n**女性角色外观图鉴**\n\n第{major}版根据参考服装库的结构对照补充48套原创搭配，覆盖四季、泳装度假、居家及夜宴等；画风领域保留96项近景与全身对照。全部{m['entry_count']}项配图词条、{m['board_count']}张图页、{m['reference_count']}个参考入口和{m['combination_count']}套组合；内容编号与外观卡继续兼容。\n\n双击 **index.html**，或使用项目 `launchers/Start Appearance Atlas.cmd`。\n\n[打开总目录](index.html?view=directory) · [完整分类表](docs/directory.md) · [检索使用说明](docs/find-and-browse.md)\n\n## 目录层级\n\n{len(n['groups'])}个领域 → {n['section_count']}个分组 → {m['category_count']}个类别 → 类别内细分。服装风格是筛选条件；画风是独立领域。\n\n| 领域 | 类别 | 词条 |\n| --- | ---: | ---: |\n"
    for g in n['groups']:text+=f"| [{g['name']}](index.html?section={g['scope']}) | {g['category_count']} | {g['count']} |\n"
    text+='\n## 查找与浏览\n\n首页搜索全图鉴；目录内搜索与当前条件一起生效，条件条可单独移除筛选或扩大范围。关键词、领域、分组、类别、细分和服装风格共用检索结果。卡片与图页切换保留状态，浏览器后退可恢复上一处。旧版类别链接与外观卡仍可使用。\n\n## 资料\n\n'
    for doc in n['documents']:text+=f"- [{doc['name']}]({doc['path']})\n"
    text+=f"\n## 文件与维护\n\n`source/navigation.json`维护目录归属；`tools/templates/browse_v32.js`与`browse_v32.css`实现统一查找页面。`data/`为生成数据，`images/`保留全部配图与历史版本，`prompts/`保留生成提示词。`.work/`为备份、缓存和检查记录，不进入离线包。\n\n```powershell\npython tools/build_atlas.py\n```\n\n离线包：项目 `outputs/packages/current/female-appearance-atlas.zip`。解压后保留完整目录结构。\n"
    (root/'README.md').write_text(text,encoding='utf-8')
