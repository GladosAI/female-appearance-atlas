"""Build the offline atlas, reference ledger, and reusable character-design docs."""
import sys
from pathlib import Path
sys.pycache_prefix = str(Path(__file__).resolve().parents[2] / '.work/cache/python')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path
from collections import Counter
import json, copy, struct, zipfile
from catalog_content import CATALOG, CATEGORIES

ROOT = _bootstrap.ROOT
entries = copy.deepcopy(CATALOG)
categories = copy.deepcopy(CATEGORIES)
refs = json.loads((ROOT / 'data/references.json').read_text(encoding='utf-8'))
PREFIXES = ['HC','HB','HT','HS','FA','FE','SK','EX','BO','PO','TO','BT','OP','OW','CS','FW','AC','MT','ST','FX']
lookup = {c['id']:c for c in categories}
counts = Counter()
for entry in entries:
    key=entry['category']; counts[key]+=1
    entry['id'] = PREFIXES[list(lookup).index(key)] + f'{counts[key]:03}'
    entry['category_name']=lookup[key]['name']
    entry['keywords']=[entry['name'],entry['en'],entry['dimension']]
    entry['related_reading']=lookup[key]['source_ids']
    entry['design_tip']=entry.pop('note') or lookup[key]['guide']
    entry['search_query']=entry['en']+' character design reference'
for cat in categories:
    cat['count']=counts[cat['id']]

BOARDS = [
    ('hair','发型示意',4,5,['下巴短波波','精灵短发','狼尾层次','直发','松波浪','螺旋卷','自然蓬松圆发','公主切','高马尾','低马尾','侧马尾','高双马尾','低双马尾','侧辫','双辫','冠状辫','低盘髻','高丸子','双丸子','半扎发']),
    ('face','脸部轮廓示意',4,3,['椭圆脸','圆脸','方脸','长方脸','心形脸','菱形脸','三角脸','长椭圆脸','柔和棱角脸','饱满面颊','宽下颌圆下巴','短下脸']),
    ('clothing','服装组合示意',4,5,['圆领T恤','衬衫式女上衣','西装外套','开襟针织衫','连帽卫衣','风衣','飞行夹克','牛仔夹克','A字连衣裙','合身连衣裙','裹身连衣裙','高腰长裙','宽摆礼服','鱼尾礼服','裙撑轮廓礼服','交领襦裙灵感','和服灵感袍','魔女','轻甲战士','未来都市']),
    ('accessories','配饰示意',5,4,['大蝴蝶结','花形发簪','长发簪','发带','贝雷帽','尖顶魔女帽','小冠饰','圆框眼镜','吊坠项链','贴颈项饰','垂坠耳饰','胸针','腰封','功能腰带','短手套','及膝袜','玛丽珍鞋','系带战靴','肩带斜包','法术书']),
    ('body-pose','体型与姿态示意',4,4,['矮个纤细','高个纤细','中等体格','运动体格','强壮体格','饱满体格','胯部较宽','肩部较宽','双脚均衡站立','单腿承重','单手叉腰','松弛抱臂','自然行走','快跑','交腿坐','抬手施法'])
]
assert len(set(e['name'] for e in entries)) == len(entries), 'Ambiguous duplicate names'
by_name={e['name']:e for e in entries}
boards=[]
for key,title,cols,rows,names in BOARDS:
    path=ROOT/'images'/f'{key}.png'
    width,height=struct.unpack('>II',path.read_bytes()[16:24])
    board={'id':key,'title':title,'image':f'images/{key}.png','columns':cols,'rows':rows,'width':width,'height':height,'origin':'AI-generated concept illustration','items':[]}
    for i,name in enumerate(names):
        entry=by_name[name]
        label=(('B' if i<8 else 'P')+f'{i+1 if i<8 else i-7:02}') if key=='body-pose' else {'hair':'H','face':'F','clothing':'C','accessories':'A'}[key]+f'{i+1:02}'
        visual={'board':key,'image':board['image'],'column':i%cols,'row':i//cols,'columns':cols,'rows':rows,'label':label,'aspect':(width/cols)/(height/rows)}
        entry['visual']=visual
        if key=='hair' and label=='H04':
            entry['design_tip']='图例展示齐刘海的长直发局部，实际发长请在全身或背面图中另行标注。'
        if key=='clothing' and label=='C15':
            entry['design_tip']='图例仅展示历史灵感正面穿搭；后部裙撑的真实突出量要另画侧面与背面，并核对实物参考。'
        board['items'].append({'label':label,'name':name,'entry_id':entry['id']})
    boards.append(board)

COMBOS = [
    ('档案馆魔女','低盘髻、圆框眼镜、长袍、短披肩、法术书','深蓝与米白；胸针作为唯一亮点','低盘髻|圆框眼镜|长袍|短披肩|法术书|低头阅读'),
    ('城市信使','高马尾、飞行夹克、工装裤、功能腰带、运动鞋','灰绿与橙；腰包形成偏置轮廓','高马尾|飞行夹克|工装裤|功能腰带|运动鞋|自然行走'),
    ('温室药师','松波浪、圆脸、围裙式上装、长及踝裙、叶片纹','浅绿与棕；围裙工具袋','松波浪|圆脸|围裙式上装|长及踝裙|叶片纹|双手身前交叠'),
    ('工坊锻造师','单侧剃短、强壮体格、工作服上衣、直筒裤、护腕','红棕与煤灰；耐磨围裙','单侧剃短|强壮体格|工作服上衣|直筒裤|护腕|宽厚手部'),
    ('观星学者','及腰长发、中分、长椭圆脸、分层法袍、星月纹','银灰与靛蓝；星形吊坠','及腰长发|中分|长椭圆脸|分层法袍|星月纹|抬头注视'),
    ('潮汐领航员','侧辫、方脸、风衣、中筒靴、小背包','海蓝与沙色；防潮图纸袋','侧辫|方脸|风衣|中筒靴|小背包|伸手指向'),
    ('音乐厅演奏者','高丸子、心形脸、合身连衣裙、垂坠耳饰、低跟鞋','黑与暖金；袖口克制装饰','高丸子|心形脸|合身连衣裙|垂坠耳饰|低跟鞋|平静'),
    ('宫廷使节','冠状辫、宽摆礼服、长手套、小冠饰、胸针','酒红与象牙；徽章标明阵营','冠状辫|宽摆礼服|长手套|小冠饰|胸针|双脚均衡站立'),
    ('夜班医护','短波波、自然淡妆、工作连体服、短袜、运动鞋','蓝灰与白；随身工具清楚分区','下巴短波波|自然淡妆|工作连体服|短袜|运动鞋|疲惫'),
    ('年长抄写师','灰发、低盘髻、细纹、开襟针织衫、长链项饰','暖棕与烟蓝；眼镜和笔是主道具','灰发|低盘髻|细纹|开襟针织衫|长链项饰|直坐'),
    ('山地游侠','双辫、运动体格、短披肩、骑装裤、骑乘靴','暗绿与赭色；箭袋固定点明确','双辫|运动体格|短披肩|骑装裤|骑乘靴|拉弓'),
    ('水晶守卫','精灵短发、明确下颌角、强壮体格、重甲战士、幻想护甲靴','石灰与蓝；硬甲和柔性关节分区','精灵短发|明确下颌角|强壮体格|重甲战士|幻想护甲靴|双手持杖'),
    ('糕点工坊主人','内扣波波、饱满体格、衬衫式女上衣、背带裙、花卉纹','奶油与莓红；围裙与发夹呼应','内扣波波|饱满体格|衬衫式女上衣|背带裙|花卉纹|微笑'),
    ('巡夜术士','遮单眼前发、长大衣、贴颈项饰、系带战靴、魔法印记','炭灰与紫；印记只在施法时发光','遮单眼前发|长大衣|贴颈项饰|系带战靴|魔法印记|抬手施法'),
    ('冬季旅人','紧卷发、厚实躯干、派克外套、围巾、连指手套','暗红与灰绿；毛绒边缘控制密度','紧卷发|厚实躯干|派克外套|围巾|连指手套|自然行走'),
    ('花园外交官','半扎发、柔和棱角脸、裹身连衣裙、花形发簪、阳伞','浅紫与暖白；花饰成为近景识别点','半扎发|柔和棱角脸|裹身连衣裙|花形发簪|阳伞|单手持伞'),
    ('现代研究员','狼尾层次、平直眉、高领针织衫、阔腿裤、方框眼镜','石墨与雾蓝；配饰少而功能清楚','狼尾层次|平直眉|高领针织衫|阔腿裤|方框眼镜|手指托下巴'),
    ('星际维修员','泡泡马尾、宽阔骨架、工作连体服、护目镜、机械义肢','蓝绿与橙；设备连接结构具体','泡泡马尾|宽阔骨架|工作连体服|护目镜|机械义肢|蹲姿'),
    ('舞台歌手','高双马尾、双区发色、舞台装饰上衣、百褶裙、舞台重妆','两种主色；舞台鞋需适应动作','高双马尾|双区发色|舞台装饰上衣|百褶裙|舞台重妆|挥手'),
    ('古城灯匠','长发簪、低盘髻、交领上衣、长及踝裙、刺绣','墨绿与铜色；传统元素明确为改编','长发簪|低盘髻|交领上衣|长及踝裙|刺绣|双手持书'),
    ('海雾召唤师','银白发、长侧帘发、宽直袖、透明叠层、吊坠项链','冷灰与海蓝；叠层边缘保持清楚','银白发|长侧帘发|宽直袖|透明叠层|吊坠项链|悬浮'),
    ('森林精灵','绳索辫、精灵尖耳、叶片纹、斗篷、踝靴','绿与棕；耳、辫与帽互相让位','绳索辫|精灵尖耳|叶片纹|斗篷|踝靴|回头'),
    ('暮色翼人','自然紧密卷、羽翼、轻甲战士、绑带、长手套','紫灰与暖金；背面预留翼根结构','自然紧密卷|羽翼|轻甲战士|绑带|长手套|收翼落地'),
    ('旧城侦探','深侧分、断眉识别点、西装外套、锥形裤、乐福鞋','棕灰与暗红；断眉与胸针是固定点','深侧分|断眉识别点|西装外套|锥形裤|乐福鞋|专注')
]
# Use the canonical catalog name for the workshop hand shape.
COMBOS = [(n,d,p,k.replace('宽厚手部','手部宽厚')) for n,d,p,k in COMBOS]
combos=[]
for n,d,p,k in COMBOS:
    names=k.split('|')
    combos.append(dict(name=n,description=d,palette=p,entry_ids=[by_name[x]['id'] for x in names]))

data={'meta':{'title':'女性角色外观图鉴','subtitle':'游戏与动漫角色设计参考集合','date':'2026-10-13','version':'1.0','entry_count':len(entries),'category_count':len(categories),'illustrated_count':sum('visual' in e for e in entries),'reference_count':len(refs),'museum_image_count':sum('image' in r for r in refs),'scope':'覆盖常见现代外观与部分历史、幻想灵感；分类用于创作，不是穷尽的时尚史或医学分类。','provenance':'词条解释与组合示例为独立编写；related_reading 是相关阅读入口，不是每个词条的逐项文献证明。动漫图为 AI 生成的创作示意，馆藏照片另有来源与公共领域标识。'},'categories':categories,'entries':entries,'boards':boards,'references':refs,'combinations':combos}
for name,obj in [('data/catalog.json',data),('data/illustrations.json',boards),('data/combinations.json',combos)]:
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

intro = f'''# 女性角色外观图鉴

适用于游戏、动漫角色设定与美术检索。共 {len(categories)} 个大类、{len(entries)} 个词条，包含 88 个动漫示意例子、六张服饰实物照片和 24 套原创组合示例。每个词条提供中文名、英文检索词和可观察的形态特征。

这套分类覆盖常见现代外观，以及部分历史和幻想灵感。真实外貌是连续变化的，标签用于描述和组合；脸型、体型、头身比都不是医学分类。服装与发型元素可用于各种性别角色。

## 使用方法

打开 [离线图鉴](index.html) 搜索、按类别筛选、查看总图，或把词条加入外观卡。收藏存储在当前浏览器；导出外观卡会下载 JSON。离线查阅无须联网，打开外部参考来源和检索入口需要联网。

先选择整体轮廓和使用场景，再组合五官、发型、服装、材质与配饰。为同一角色保留三至五个固定识别点；状态、表情、换装属于可更换的外观层。

## 分类索引

| 类别 | 词条数 | 组合方法 |
| --- | ---: | --- |
'''
for cat in categories:
    intro+=f"| [{cat['name']}](#{cat['id']}) | {cat['count']} | {cat['guide']} |\n"
intro+='''
## 分类示意图

以下五张图由内置 image_gen 工具生成，提示词保存在 [image-prompts.json](image-prompts.json)。它们是创作示意图，不能作为人体测量或历史服装复原依据。脸型、体型的部分差异经过动漫简化，请结合词条描述判断；体型图中的 P07 实际为交腿坐姿，已按图像标注。

'''
for board in boards:
    intro+=f"### {board['title']}\n\n![{board['title']}]({board['image']})\n\n"
    intro+=' · '.join(f"{x['label']} {x['name']}" for x in board['items'])+'\n\n'
intro+='''## 词条详表

英文用于检索，描述是本集合独立编写的绘画识别要点。每类后的来源链接是相关教程、词典或馆藏入口；具体年代、地域、图像权利请查看原始馆藏条目。

'''
for cat in categories:
    intro+=f"<a id=\"{cat['id']}\"></a>\n\n### {cat['name']}\n\n{cat['guide']}\n\n"
    groups=list(dict.fromkeys(e['dimension'] for e in entries if e['category']==cat['id']))
    for group in groups:
        intro+=f'#### {group}\n\n| 编号 | 中文 | English | 识别特征 |\n| --- | --- | --- | --- |\n'
        for e in entries:
            if e['category']==cat['id'] and e['dimension']==group:
                intro+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
        intro+='\n'
    relevant=[r for r in refs if r['id'] in cat['source_ids']]
    if relevant:
        intro+='相关阅读：'+'，'.join(f"[{r['title']}]({r['url']})" for r in relevant)+'。\n\n'
intro+='''## 组合与制作

参见 [角色外观卡模板](character-template.md)、[24 套组合示例](combinations.md) 与 [来源和图片说明](sources.md)。用于游戏制作时，先检查黑色剪影和头像缩略图，再决定需要独立运动的发束、披风、衣摆、饰品与道具层。

同一角色先固定身高、头身比、发际线、五官位置、主要配色与标记位置。换装可以改变服饰和头发扎法，但固定识别点应保持。常规成人、成熟及年长角色都可以使用这些部件，不用某一种眼形或身材替代年龄设定。
'''
(ROOT/'docs/atlas.md').write_text(intro,encoding='utf-8')

source_doc='''# 女性角色外观图鉴来源与图片说明

核验日期为 2026 年 10 月 13 日。词条、分类和组合示例为独立编排；来源用于提供绘画原理、词义对照与实物检索。动漫图为新增 AI 创作示意，六张馆藏照片为收集的实物参考，两种内容分别标注。

## 教程与馆藏入口

'''
for r in refs:
    source_doc+=f"### {r['id']} {r['title']}\n\n[{r['publisher']}]({r['url']}) · {r['kind']} · 核验 {r['checked']}\n\n观察主题：{r['topics']}。{r['summary']}\n\n"
    if r.get('image'):
        source_doc+=f"![{r['title']}]({r['image']})\n\n年代：{r['date']}；地域标记：{r['culture']}；材质：{r['medium']}；馆藏编号：{r['object_number']}。\n\n"
    source_doc+=f"图片处理：{r['rights']}。\n\n"
source_doc+='''## 新增分类示意

五张 PNG 使用内置 image_gen 工具，未使用 CLI/API 回退。完整提示词见 [image-prompts.json](image-prompts.json)，图中编号与词条对应关系见 [illustrations.json](illustrations.json)。原图在 images 目录保留，浏览器卡片只裁切显示原图的对应区域。

历史或地域服饰在动漫图中均为灵感改编；实物照片的年份、地域与馆藏编号以原始页面记录为准。教程和 V&A 图像没有复制到此集合。Met 图片按每件页面的 Public Domain 标识保存，开放政策见 [Met Open Access](https://www.metmuseum.org/hubs/open-access)。

外部检索按钮只是根据词条生成的查询入口，不代表其搜索结果已经收录或核验。
'''
(ROOT/'docs/sources.md').write_text(source_doc,encoding='utf-8')

combo_doc='# 女性角色外观组合示例\n\n以下 24 套为原创组合方案，用于探索剪影、材质和角色场景；不预设外貌对应性格。配色是创作建议，可自由替换。\n\n'
for i,c in enumerate(combos,1):
    combo_doc+=f"## {i} {c['name']}\n\n{c['description']}。\n\n配色与重点：{c['palette']}。\n\n词条："+'、'.join(f"{next(e['name'] for e in entries if e['id']==eid)}（{eid}）" for eid in c['entry_ids'])+'。\n\n'
(ROOT/'docs/combinations.md').write_text(combo_doc,encoding='utf-8')

template='''# 女性角色外观卡模板

把词条当作可组合部件，先描述可见形态，再说明它如何配合角色的生活、职业或战斗需求。

## 基础信息

- 角色名与角色编号：
- 设定年龄与呈现年龄感：
- 场景、地域与时代设定：
- 画风、头身比与目标显示尺寸：
- 身高、骨架、肌肉与软组织体积：

## 头部

- 脸部轮廓与侧面轮廓：
- 眼形、虹膜、眼间距与眉形：
- 鼻、嘴、耳部与固定标记：
- 发长、剪裁、刘海、分缝：
- 扎法、编法、发质、主色与染色分区：
- 发根固定点、发束数量和运动范围：

## 服装与装备

- 内层、中层、外层与鞋袜：
- 整体轮廓、腰线、领型、袖型和长度：
- 材质的厚薄、软硬、重量与光泽：
- 主色、辅色、重点色与纹样尺度：
- 配饰的固定点、道具的握持点与携行位置：
- 历史实物参考或灵感改编说明：

## 体态与差分

- 默认重心、站姿、坐姿和习惯手势：
- 行走、跑步、战斗与道具使用的动作规则：
- 表情基准与需要的差分：
- 换装或变身变化部件：
- 伤痕、痣、纹身和印记的三视图位置：

## 固定识别点

记录三至五个在头像、半身与全身图中仍能辨认的特征：

1. 头部轮廓或发束：
2. 五官或稳定标记：
3. 衣物大轮廓：
4. 道具或配饰：
5. 配色关系：

## 美术交付

- 正面、侧面、背面与常用四分之三视角：
- 黑色剪影、头像缩略图与去色对比：
- 头发前后层、躯干、手臂、衣摆、披风、饰品和道具拆层：
- 背部衣物、扎发固定点与额外器官接点：
- 关节活动、布料受力和穿插检查：
- 参考链接、作者或馆藏、日期与图片使用条件：

## 可复制的文字描述

一位【年龄设定】的女性角色，具有【身高与体格】、【脸部轮廓】和【五官特征】；头发为【发色与发质】，采用【长度＋剪裁＋刘海＋扎法】。穿着【内层＋外层＋下装或连身衣物】，以【材质、配色与纹样】呈现；佩戴【固定配饰】，携带【道具】。默认姿态为【重心与手势】，固定识别点为【三至五项】。以【画风与比例】绘制正面、侧面、背面和需要的表情差分。
'''
(ROOT/'docs/character-template.md').write_text(template,encoding='utf-8')
readme=f'''# 女性角色外观图鉴

游戏与动漫角色设计参考集合，包含 {len(entries)} 个词条、{len(categories)} 个大类、88 个动漫示意例子、六张公共领域服饰照片、19 个来源和 24 套组合示例。

## 打开

双击 index.html 或项目根目录的 Start Appearance Atlas.cmd。页面可离线使用，默认展示有示意图的 88 个词条，点击“全部词条”查看完整集合。搜索支持中文、英文、编号和描述；选择卡片可以查看说明、参考阅读并加入外观卡。

## 文件

| 文件 | 内容 |
| --- | --- |
| index.html | 离线搜索、分类、示意总图、实物参考和外观卡 |
| atlas.md | 完整图文图鉴及 {len(entries)} 条分类详表 |
| character-template.md | 可复用角色设定与美术交付模板 |
| combinations.md | 24 套原创造型组合 |
| sources.md | 来源链接、实物信息和图片使用说明 |
| catalog.json | 完整结构化词条及图像映射 |
| references.json | 19 个已核验来源及六张实物照片元数据 |
| illustrations.json | 五张分类图中的 88 个编号对应关系 |
| image-prompts.json | 内置 image_gen 的完整提示词 |
| images | 五张新增动漫图和六张实物照片 |

词条是创作分类，相关阅读是延伸检索入口。图像是 88 个典型例子，并非每个词条都有独立插图；未配插图的词条提供形态描述与外部检索词。文化与历史服装的动漫图为灵感改编，历史考据请查实物记录。

外观卡保存在当前浏览器本地；导出 JSON 可长期保存并导入。解压时保留整个文件夹及 images 子目录。更新源数据后，运行 python tools/build_atlas.py 重新生成各项文件。
'''
(ROOT/'README.md').write_text(readme,encoding='utf-8')
html=(ROOT/'tools/templates/atlas_template.html').read_text(encoding='utf-8')
html=html.replace('__ATLAS_DATA__',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(ROOT/'index.html').write_text(html,encoding='utf-8')
print(json.dumps(data['meta'],ensure_ascii=False))

if __name__=='__main__':
    bundle=_bootstrap.PACKAGE
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(ROOT.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and '.work/verification/v1' not in path.parts:
                z.write(path,path.relative_to(ROOT.parent))
    print('Bundle:',bundle, bundle.stat().st_size)
