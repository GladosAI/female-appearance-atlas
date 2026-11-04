"""Build the current edition index independently of persistent topic documents."""
import sys,json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path

def write_latest_docs(root,data):
    root=Path(root);meta=data['meta'];edition=meta['version'].split('.')[0]
    entries=[e for e in data['entries'] if e.get('added_in')==meta['version']]
    if not entries:
        release=json.loads((root/'source/content-release.json').read_text(encoding='utf-8'))
        text=f"# 本版修订 · 内容{meta['version']}\n\n{release.get('summary','本版维护现有词条。')}\n\n保留全图鉴{len(data['entries'])}个词条的编号与收藏引用。\n\n"
        for path in sorted((root/'source/quality-reviews').glob('*.json')):
            report=json.loads(path.read_text(encoding='utf-8'))
            if report.get('catalog_version')!=meta['version']:continue
            scope=report['scope']
            text+=f"本批复核{scope['entries']}个词条、{scope['visuals']}幅主图与佩戴图，修正{len(report['changed_entries'])}项。\n\n"
        text+='[质量复核记录](material-quality.md) · [进入图鉴](index.html?section=all) · [完整图文索引](atlas.md) · [变更记录](../CHANGELOG.md)\n'
        (root/'docs/fashion-guide.md').write_text(text,encoding='utf-8')
        return
    if edition=='32':
        (root/'docs/fashion-guide.md').write_text('# 第32版 · 目录与检索改版\n\n保留全部5629项配图词条，重整为8个领域、42个分组和133个类别。目录归属、筛选和结果展示使用同一层级。\n\n- 风格作为服装筛选条件，与类别、细分和关键词叠加。\n- 卡片与分类图页共用结果，切换保留当前条件。\n- 条件可单独移除，支持扩大查找范围、键盘建议、后退与地址恢复。\n- 原有图片、编号、专题链接和外观卡继续兼容。\n\n[进入图鉴](../index.html) · [完整目录](directory.md) · [检索使用说明](find-and-browse.md) · [最近补充：耳机佩戴](headphone-atlas.md)\n',encoding='utf-8')
        return
    ids={e['id'] for e in entries}
    boards=[b for b in data['boards'] if any(x['entry_id'] in ids for x in b['items'])]
    if edition=='30':boards=[b for b in data['boards'] if any(x['entry_id'] in ids for x in b['items']) or b.get('role')=='wearing_reference' and b.get('edition')==30]
    text=f"# 本版新增图文专辑 · 第{edition}版\n\n新增 {len(entries)} 项，{len(boards)} 张图页；全图鉴 {len(data['entries'])} 项，全部配图。\n\n"
    if edition=='32':
        text+='本版整理目录和检索逻辑，不新增或删除词条。8个领域、42个分组覆盖全部133类。关键词、目录、细分与穿搭风格统一筛选，卡片与图页共用结果。见 [目录与检索说明](find-and-browse.md)。\n\n'
    elif edition=='34':
        text+='新增32项发质发色、32项表情（含凝视与憋笑）与32项日常及创意妆面；归入原有“发质与发色”和“表情与妆容”。同时调整细分控件、搜索建议与多外观卡编辑。见 [第34版完整配图](beauty-expansion-v34.md)。\n\n'
    elif edition=='33':
        text+='新增眼影、眼线和完整眼妆各16项，共48项眼部佩戴近景。归于脸部与表情 → 眼睛、肤色与眼部彩妆，支持分开查找与组合。见 [眼部彩妆专题](eye-makeup-atlas.md)。\n\n'
    elif edition=='31':
        text+='新增32种耳机、耳塞与耳麦佩戴图，分头戴与专业造型、耳塞与开放式两组。小型设备附同侧耳部放大图，比较接触位置与固定结构。见 [耳机佩戴完整专题](headphone-atlas.md)。\n\n'
    elif edition=='30':
        text+='新增32种发绳佩戴造型，发绳类现共48项。另为原有64项发饰与16项眼镜补齐佩戴图，物件图保留，详情可并排比较；本轮共新增112个图例、7张图页。见 [佩戴专题](wearing-reference-atlas.md)。\n\n'
    elif edition=='29':
        text+='本版新增128项衣着配饰，以及64种佩戴发卡、发绳、发箍、发簪的完整发型，共192项。配饰按腰部、腿部、颈部、衣襟肩臂及巾带绳饰分列；发型图展示发饰与发束的实际固定关系。参见 [配饰与发饰发型完整专题](accessory-hairstyles-atlas.md)。\n\n'
    elif edition=='28':
        text+='本版新增144项体态与动作，分9组各16项；现共204项。包含站姿与重心、上肢手势、坐蹲跪起身、卧姿地面、走跑跳阶段、日常持物、情绪肢体、双人协作与运动冒险，新增卡片标明视角、阶段与支撑点。参见 [完整动作专题](pose-atlas.md)。\n\n'
    elif edition=='27':
        text+='本版以扩充种类为主：32种职业、舞台与奇幻身份，每种2套，共64套。都市职业、户外作业、舞蹈杂艺、奇幻身份各8种；两套比较实际剪裁、服装层次和道具。参见 [32种身份完整专题](diverse-roles-atlas.md)。\n\n'
    elif edition=='26':
        text+='本版新增16组成年角色尺寸设定，各有正面与侧身，共32项。体型页默认并排对照，可切换罩杯、身高、肩宽、腰围与臀围，选择2至4列；尺寸均为虚构角色设定。参见 [完整尺寸与罩杯专题](body-dimensions-atlas.md)。\n\n'
    elif edition=='25':
        text+='本版新增魔法少女装扮32套、忍者装扮32套。两类各按2组16套细分：基础变身礼装、主题与进阶礼装、布装与行动装备、环境与幻想改编。全部为明确成年原创角色参考，包含服装、头饰、鞋袜与必要配饰。参见 [魔法少女与忍者完整专题](magical-ninja-atlas.md)。\n\n'
    elif edition=='24':
        text+='本版新增144项：成年体型与体态32项，体操、啦啦队、死神、维密风格秀场各16套，口罩、防毒面具和一般面具佩戴各16项。体型卡片提供正面＋侧身对照。参见 [完整新增专题](body-stage-cover-atlas.md)。\n\n'
    elif edition=='23':
        text+='本版新增16个年龄阶段的正面与侧身图，共32项。年龄页默认按年龄并排、按统一示意标尺和脚底基线比较，婴幼儿卧姿另组；相近衣着减少体型菜单与数值造成的干扰。既有平静闭眼剧情图例统一名称为长眠。参见 [阶段对照专题](life-stage-comparison.md)。\n\n'
    elif edition=='22':
        text+='本版新增修女装扮32套，睡眠、昏迷与长眠剧情状态各16项，以及身高整体比例16项、成年三围16项。年龄分类页附可展开的数值对照图；尺寸均为虚构角色设定，未成年参考仅有完整着装的中性身高与比例。\n\n'
    else:
        text+='本版新增内容按以下细分编排，每个编号均对应独立图例。\n\n'
    text+=f"[四季日常总览 · {meta['seasonal_count']} 套](index.html?section=seasonal) · [四季完整专题](seasonal-atlas.md) · [兽娘与福瑞总览 · {meta['anthro_count']} 项](index.html?section=anthro) · [兽娘完整专题](anthro-atlas.md) · [面部总览 · {meta['facial_count']} 项](index.html?section=facial) · [面部完整专题](facial-atlas.md) · [袜类完整专题](socks-atlas.md)\n\n"
    text+='## 新增索引\n\n| 细分 | 数量 | 类别入口 |\n| --- | ---: | --- |\n'
    for dimension in dict.fromkeys(e['dimension'] for e in entries):
        group=[e for e in entries if e['dimension']==dimension]
        text+=f"| {dimension} | {len(group)} | [查看](index.html?section={group[0]['category']}) |\n"
    text+='\n配图由内置image_gen制作，每个编号对应一格。人物年龄、着装与剧情状态以词条说明为准；图像用于角色创作。\n\n'
    for dimension in dict.fromkeys(e['dimension'] for e in entries):
        group=[e for e in entries if e['dimension']==dimension];text+=f"## {dimension}\n\n"
        used={e['visual']['board'] for e in group}
        for board in boards:
            if board['id'] in used:text+=f"![{board['title']}]({board['image']})\n\n"
        text+='| 编号 | 名称 | English | 可见特征 |\n| --- | --- | --- | --- |\n'
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
        text+='\n'
    text+='## 相关阅读\n\n'
    keys=list(dict.fromkeys(k for e in entries for k in e['related_reading']))
    refs={r['id']:r for r in data['references']}
    for key in keys:
        r=refs[key];text+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    text+=f"\n[目录与检索说明](find-and-browse.md) · [全图鉴](atlas.md) · [来源说明](sources.md)\n" if edition=='32' else f"\n[第{edition}版图页提示词](image-prompts-v{edition}.json) · [全图鉴](atlas.md) · [来源说明](sources.md)\n"
    (root/'docs/fashion-guide.md').write_text(text,encoding='utf-8')
