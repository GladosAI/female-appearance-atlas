"""Build one complete topic directory without altering canonical entry records."""
import copy
import json


def build_navigation(root, data):
    navigation = json.loads((root / 'source/navigation.json').read_text(encoding='utf-8'))
    categories = {c['id']: c for c in data['categories']}
    assigned = [cid for group in navigation['groups'] for cid in group['categories']]
    assert len(assigned) == len(set(assigned)), 'Category assigned to multiple primary topics'
    assert set(assigned) == set(categories), f'Unassigned categories: {set(categories) - set(assigned)}'
    assert len({g['id'] for g in navigation['groups']}) == len(navigation['groups'])
    result = copy.deepcopy(navigation)
    for group in result['groups']:
        group['scope'] = 'topic_' + group['id']
        group['count'] = sum(categories[c]['count'] for c in group['categories'])
        group['category_count'] = len(group['categories'])
    result['entry_count'] = sum(g['count'] for g in result['groups'])
    result['category_count'] = len(assigned)
    assert result['entry_count'] == len(data['entries'])
    result['style_categories'] = [
        {'id':'style_' + f['id'], 'style_id':f['id'], 'name':f['name'] + '穿搭',
         'count':f['clothing_count'], 'guide':f['guide']}
        for f in data['style_families']
    ]
    assert result['style_parent'] in {g['id'] for g in result['groups']}
    for style in result['style_categories']:
        assert style['count'] == sum(style['style_id'] in e['styles'] and e['category'] in data['meta']['clothing_categories'] for e in data['entries'])
    return result


def write_navigation_docs(root, data, navigation):
    cats = {c['id']: c for c in data['categories']}
    text = f'''# 女性外貌图鉴总目录

整理日期：{navigation['date']}。{len(navigation['groups'])} 个主题，{len(cats)} 个类别，{len(data['entries'])} 个配图词条。

打开 [图鉴总目录](../index.html?view=directory)，按主题、类别、细分浏览。哥特、量产型等在“日常、校园与风格穿搭”的类别中选择；材质与印花单独浏览。每个基础类别在主目录中只有一个归属；交叉专题与穿搭风格会汇总相关词条，数量不能与主目录累加。

## 主题索引

| 主题 | 类别数 | 词条数 | 范围 |
| --- | ---: | ---: | --- |
'''
    for group in navigation['groups']:
        text += f"| [{group['name']}](../index.html?section={group['scope']}) | {group['category_count']} | {group['count']} | {group['note']} |\n"
    for group in navigation['groups']:
        text += f"\n## {group['name']}\n\n{group['note']}\n\n| 类别 | 配图词条 | 浏览 |\n| --- | ---: | --- |\n"
        for cid in group['categories']:
            c = cats[cid]
            label = navigation.get('category_labels', {}).get(cid, c['name'])
            text += f"| {label} | {c['count']} | [词条](../index.html?section={cid}) · [详表](atlas.md#{cid}) |\n"
        if group['id'] == navigation['style_parent']:
            text += '\n### 按穿搭风格浏览\n\n汇集相关服装单件与套装；同一套穿搭可以符合多种风格。\n\n'
            for style in navigation['style_categories']:
                text += f"- [{style['name']}](../index.html?section={style['id']}) · {style['count']}项\n"
    text += '\n## 交叉专题\n\n'
    for shortcut in navigation['shortcuts']:
        text += f"- [{shortcut['name']}](../index.html?section={shortcut['id']})\n"
    text += '\n## 文档与创作工具\n\n'
    for doc in navigation['documents']:
        text += f"- [{doc['name']}]({doc['path'].removeprefix('docs/')})\n"
    text += '\n原有词条编号、图片裁切及外观卡格式保留。旧版页面分类链接仍然可用。\n'
    (root / 'docs/directory.md').write_text(text, encoding='utf-8')


def write_usage_readme(root):
    data = json.loads((root / 'data/catalog.json').read_text(encoding='utf-8'))
    navigation = json.loads((root / 'data/navigation.json').read_text(encoding='utf-8'))
    meta = data['meta']
    text = f'''# 女性角色外观图鉴

面向游戏、动漫与原创角色设计。第{meta['version'].split('.')[0]}版共 **{meta['entry_count']} 个配图词条、{meta['category_count']} 个类别、{meta['board_count']} 张分类图页**，含 {meta['clothing_count']} 项服装参考、{meta['seasonal_count']} 套四季日常穿搭、30种风格标签及40套组合示例。

双击本目录的 **index.html**，或项目 `launchers/Start Appearance Atlas.cmd`。首页是 [图鉴总目录](index.html?view=directory)，按12个主题进入类别；[文字总目录](docs/directory.md) 列出全部分类。词条页按“主题 → 类别 → 细分”浏览，穿搭风格属于服装穿搭的类别选择。可搜索中文、英文与编号，点击图例查看细节，再加入角色外观卡。

## 浏览顺序

| 主题 | 类别 | 配图词条 |
| --- | ---: | ---: |
'''
    for group in navigation['groups']:
        text += f"| [{group['name']}](index.html?section={group['scope']}) | {group['category_count']} | {group['count']} |\n"
    text += '''
每个基础类别在主目录中只有一个归属。服装单件和整套搭配分别浏览；发饰在配饰主题，假发在Cosplay主题，自然兽耳在兽娘主题。哥特、英伦、洛丽塔、朋克、地雷系等在“日常、校园与风格穿搭”的类别中选择；整体造型示例也在此主题，材质与印花另列。交叉专题与穿搭风格汇集相关词条，数量不与主目录累加。

## 常用资料

| 入口 | 内容 |
| --- | --- |
| [本版体型、舞台与面罩专题](docs/body-stage-cover-atlas.md) | 第24版新增144项，含正侧面体型对照与三类面部覆盖物佩戴 |
| [衣着配饰与发饰发型](docs/accessory-hairstyles-atlas.md) | 128项配饰＋96种佩戴发饰发型，发绳48项 |
| [耳机与耳麦佩戴](docs/headphone-atlas.md) | 32项头戴、入耳、开放式、专业耳麦与造型款 |
| [发绳与佩戴专题](docs/wearing-reference-atlas.md) | 新增32种发绳造型，64项发饰与16项眼镜补齐佩戴图 |
| [体态与动作完整专题](docs/pose-atlas.md) | 第28版新增144项，共204项，按视角、阶段与支撑点查看 |
| [更多职业、舞台与奇幻身份](docs/diverse-roles-atlas.md) | 第27版32种身份，每种2套，共64套 |
| [成年尺寸与罩杯对照](docs/body-dimensions-atlas.md) | 第26版16组正面＋侧身，身高、肩宽、上下胸围、腰臀围及罩杯 |
| [魔法少女与忍者装扮](docs/magical-ninja-atlas.md) | 第25版两类各32套，共64套，含服装与配饰结构 |
| [图文详表](docs/atlas.md) | 按同一套12主题目录排列的全部图例与说明 |
| [服装专辑](docs/clothing-atlas.md) · [四季穿搭](docs/seasonal-atlas.md) | 单件、制服、历史与幻想服饰、春夏秋冬搭配 |
| [修女装扮](docs/nun-atlas.md) · [睡眠昏迷长眠](docs/sleep-coma-death-atlas.md) · [尺寸设定](docs/age-size-atlas.md) | 第22版图例与尺寸设定表 |
| [年龄阶段并排对照](docs/life-stage-comparison.md) | 第23版新增32幅正面与侧身图，默认按年龄并排比较 |
| [女性各年龄段](docs/female-ages-atlas.md) · [特殊外观补充](docs/special-variants-atlas.md) | 96项年龄与尺寸参考、144项特殊外观 |
| [特殊装扮](docs/special-costumes-atlas.md) · [头发形态](docs/hair-states-atlas.md) | 新增128套装扮与64项头发状态 |
| [婚纱与婚服](docs/wedding-atlas.md) | 婚纱32款、婚服48套及头纱配饰搭配 |
| [潮流、时尚与模特穿搭](docs/trend-fashion-model-atlas.md) | 新增三类96套完整造型 |
| [头发](docs/hair-atlas.md) · [面部](docs/facial-atlas.md) · [袜类](docs/socks-atlas.md) | 部件、状态与专项索引 |
| [Cosplay](docs/cosplay-atlas.md) · [兽娘与福瑞](docs/anthro-atlas.md) | 完整方案、外观部件、装饰和展示 |
| [组合示例](docs/combinations.md) · [设定模板](docs/character-template.md) | 角色造型组合与美术交付记录 |
| [来源说明](docs/sources.md) | 全部参考入口与六张实物照片的来源 |

## 文件分工

| 目录 | 内容 |
| --- | --- |
| index.html、README.md | 离线浏览入口与使用说明 |
| docs/ | 总目录、完整详表及专题文档 |
| data/ | 页面词条、主题目录、图页映射、来源与组合JSON |
| images/ | 分类图、历史生成版本与实物照片；保留编号文件名 |
| prompts/ | 第1至18版图页提示词 |
| source/ | 主题归属、图片任务、图像映射和参考输入 |
| source/catalog/ | 原始词条及历次扩充代码 |
| tools/ | 构建、图片任务与登记入口 |
| tools/builders/、tools/templates/ | 文档与页面生成器、网页模板 |
| tools/qa/ | 当前版页面、目录与离线包检查 |
| tools/history/ | 旧版检查及一次性脚本 |
| .work/ | 预览、缓存、锁、备份和历次验证，不进入离线包 |

主要数据：[catalog.json](data/catalog.json)、[navigation.json](data/navigation.json)、[illustrations.json](data/illustrations.json)、[references.json](data/references.json)、[combinations.json](data/combinations.json)。主题归属从 [source/navigation.json](source/navigation.json) 生成；新增类别必须归入一个主题，构建时会检查重复或遗漏。

## 维护

在本图鉴目录中运行：

```powershell
python tools/build_atlas.py
node tools/qa/verify_atlas_v18.cjs
node tools/qa/verify_navigation_v18.cjs
python tools/qa/verify_archive_v18.py
```

图片任务用 `python tools/prepare_image_jobs.py`。构建入口生成页面、数据、文档及离线包，并检查词条配图。当前离线包在项目 `outputs/packages/current/female-appearance-atlas.zip`，整理前及旧版包在 `outputs/packages/history/`。解压时保留完整的 `female-appearance-atlas` 文件夹。

## 版本与保存

词条内容为第18版；目录整理日期为2026-10-15。原有编号、图片裁切与分类链接保留，已有外观卡仍可导入。外观卡保存在当前浏览器，可导出JSON长期保存。

配图是原创动漫设计示意，历史、地域及专业服饰用于角色灵感参考；六张实物照片另有馆藏记录，来源见专题说明。
'''
    major=meta['version'].split('.')[0]
    text=text.replace('80个参考入口',f"{meta['reference_count']}个参考入口").replace('第1至18版',f'第1至{major}版').replace('词条内容为第18版',f'词条内容为第{major}版')
    for stem,suffix in [('verify_atlas','cjs'),('verify_navigation','cjs'),('verify_archive','py')]:
        text=text.replace(f'{stem}_v18.{suffix}',f'{stem}_v{major}.{suffix}')
    (root / 'README.md').write_text(text, encoding='utf-8')
