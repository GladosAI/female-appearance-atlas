"""V40: original superhero silhouettes and capability design archetypes."""
from catalog_content import CATALOG, category, add

NEW_CATEGORIES = ['superhero_outfits']
CLASSIC = '披风、面罩与战甲英雄'
ORIGINAL = '原创能力与装备型英雄'
category('superhero_outfits', '超级英雄与超级女杰', '32项全身装束参考：16项披风、面罩与战甲轮廓，以及16项能力与装备类型。女超人、神奇女侠等作为主题参考入口；全部图例为原创成年英雄装束，比较披风、面罩、护甲、手套、靴装与道具，不是原作角色设定图。', ['R145', 'R146', 'R153', 'R154'])

def classic(name, en, identity, universe, ref, aliases, recipe):
    add('superhero_outfits', CLASSIC, f'{name}|{en}|原创英雄装束；{recipe}。主题参考入口：{identity}。')
    CATALOG[-1].update(superhero_reference=True, superhero_kind='silhouette', superhero_inspiration=identity, superhero_inspiration_universe=universe,
        adult_only=True, minor_reference=False, age_min=21, added_in='40.0', reference_ids=[ref], aliases=aliases,
        outfit_components=recipe.split('；'), illustration_recipe=recipe,
        note='原创成年英雄装束，采用原创徽记、配色和衣物组合。参考人物只提供主题阅读入口，图例不表示该角色的官方造型，也不对应真人演员。观察轮廓、固定点及各件服装之间的关系。')

classic('女超人主题·飞行披风装', 'flying cape heroine theme', '卡拉·佐-艾尔 / Kara Zor-El', 'DC', 'R145', ['女超人', '超级少女', 'Supergirl', '卡拉', 'Kara Zor-El'], '深棕肤色与银金色短卷发；钴蓝完整长袖长裤战衣；珊瑚橙色短披风固定于领下双扣；原创金色菱环胸徽；白色腰带与白色中筒靴')
classic('亚马逊战士·护腕战甲装', 'Amazon-warrior armor theme', '戴安娜 / Diana', 'DC', 'R146', ['神奇女侠', 'Wonder Woman', '戴安娜'], '棕色高马尾与简洁银色额环；青铜色高领轻胸甲；米白长袖内层与深紫完整长裤；青铜护腕、分片腰甲与靴；银色绳索盘在腰侧')
classic('蝙蝠主题·短披风义警装', 'bat-themed short-cape vigilante', '芭芭拉·戈登 / Barbara Gordon', 'DC', 'R147', ['蝙蝠女孩', '蝙蝠少女', 'Batgirl', 'Barbara Gordon'], '黑色短发与深灰简洁眼罩；墨绿完整长袖长裤；浅灰锯齿边短披风；几何双翼形原创胸饰；棕色工具带与运动靴，无蝙蝠耳罩')
classic('夜巡女侠·长披风护甲装', 'night-patrol armored heroine', '凯特·凯恩 / Kate Kane', 'DC', 'R148', ['蝙蝠女侠', 'Batwoman', 'Kate Kane'], '栗色低辫与海军蓝半脸眼罩；海军蓝完整长裤战衣；银灰长披风；铜色几何护肩、护腕与靴；原创竖向椭圆胸章')
classic('声波女侠·夹克行动装', 'sonic heroine jacket ensemble', '黛娜·兰斯 / Dinah Lance', 'DC', 'R149', ['黑金丝雀', 'Black Canary', 'Dinah Lance'], '紫黑短发；青灰短机车夹克；完整黑色高领内搭与黑色工装长裤；橙色声波腕环；黑色手套与平底靴')
classic('魔术女杰·礼帽燕尾装', 'stage-magic heroine tailcoat', '扎坦娜·扎塔拉 / Zatanna Zatara', 'DC', 'R150', ['扎坦娜', '扎塔娜', 'Zatanna'], '银灰盘发与酒红高顶礼帽；完整奶白衬衫与酒红燕尾长外套；深灰西装长裤；金色领结、白手套与黑靴；短银色魔术棒向下')
classic('海洋女杰·鳞纹长裤装', 'ocean heroine scale-textured suit', '湄拉 / Mera', 'DC', 'R151', ['湄拉', '海后', 'Mera'], '棕肤黑色长辫与银色小浪形额饰；深蓝色完整长袖连体长裤；细密原创鳞纹与银色衣缘；青绿色护腕、腰饰和靴；无披风')
classic('羽翼女杰·翼盔轻甲装', 'winged heroine light armor', '肯德拉·桑德斯 / Kendra Saunders', 'DC', 'R152', ['鹰女', '鹰女孩', 'Hawkgirl', 'Kendra Saunders'], '银色短发与小型铜色翼形额盔；米白完整长袖长裤飞行服；棕色小护胸与护腕；白灰色羽翼半收拢在背后；棕色靴，无武器')
classic('星芒女杰·星徽长裤装', 'star-emblem heroine suit', '卡罗尔·丹弗斯 / Carol Danvers', 'Marvel', 'R153', ['惊奇队长', '惊奇女士', 'Captain Marvel', 'Carol Danvers'], '黑色短发；深紫完整长袖长裤；银色肩部与小腿拼接；原创六芒星胸饰；青绿色手套、腰带和短靴，无披风')
classic('咒术女杰·冠饰长披风装', 'spellcasting heroine crown and mantle', '旺达·马克西莫夫 / Wanda Maximoff', 'Marvel', 'R154', ['绯红女巫', '红女巫', 'Scarlet Witch', 'Wanda Maximoff'], '黑色盘发与小型银色圆弧冠饰；深青完整长袖长裤；浅紫色前开长披风；银色腰扣、护腕与靴；手边少量淡紫光点')
classic('特工女杰·腰包战术装', 'agent heroine utility suit', '娜塔莎·罗曼诺夫 / Natasha Romanoff', 'Marvel', 'R155', ['黑寡妇', 'Black Widow', 'Natasha Romanoff', 'Natasha Romanova'], '棕肤深棕短发；浅灰完整高领长袖连体长裤；深绿短战术背心与小型腰包；青色腕套、黑色平底靴；无武器')
classic('天气女杰·扇形翼披装', 'weather heroine fan-cape suit', '奥萝洛·门罗 / Ororo Munroe', 'Marvel', 'R156', ['暴风女', '暴风女神', 'Storm', 'Ororo Munroe'], '棕色肤色与银灰色长发；深蓝完整长袖长裤；浅青扇形披风接在手腕和背部；铜色衣缘与铜色额环；灰白靴')
classic('灵鸟女杰·羽纹肩饰装', 'mythic-bird heroine feather motif', '琴·格蕾 / Jean Grey', 'Marvel', 'R157', ['凤凰女', '琴格蕾', 'Jean Grey', 'Phoenix'], '深棕短卷发；砖红完整长袖长裤；银色抽象羽纹胸饰与短肩披；米白手套、腰带与靴；无火焰')
classic('力量女杰·运动战装', 'strength heroine athletic suit', '詹妮弗·沃尔特斯 / Jennifer Walters', 'Marvel', 'R154', ['女浩克', '女绿巨人', 'She-Hulk', 'Jennifer Walters'], '深棕肤色与黑色短辫；高大结实成年体格；橙灰短袖运动式完整长裤战衣；宽腰带、护膝与黑色训练靴；手臂自然垂下')
classic('昆虫翼女杰·翼装战衣', 'insect-wing heroine flight suit', '珍妮特·凡·戴恩 / Janet van Dyne', 'Marvel', 'R154', ['黄蜂女', '黄蜂侠', 'Wasp', 'Janet van Dyne'], '栗色短发；米白完整长袖长裤；青绿色胸部与肩部软护甲；背部两对透明淡蓝昆虫翼；棕色手套与靴')
classic('力场女杰·团队制服装', 'force-field heroine team uniform', '苏珊·斯通·理查兹 / Susan Storm Richards', 'Marvel', 'R158', ['隐形女', '隐形女人', 'Invisible Woman', 'Sue Storm', 'Susan Storm'], '棕肤灰白短卷发；米灰完整长袖长裤；海蓝色短肩披、手套与靴；原创双圆环胸饰；掌旁小型透明圆形力场，身体与衣物完整可见')

def original(name, en, aliases, recipe):
    add('superhero_outfits', ORIGINAL, f'{name}|{en}|原创英雄类型；{recipe}。')
    CATALOG[-1].update(superhero_reference=True, superhero_kind='original', adult_only=True, minor_reference=False, age_min=25,
        added_in='40.0', aliases=aliases, reference_ids=[], outfit_components=recipe.split('；'), illustration_recipe=recipe,
        note='原创成年英雄装束，用能力与装备组织轮廓，胸徽和配色为原创；不是某个现有作品角色或官方设定。比较功能与衣物结构，不把发光特效当成服装本体。')

original('披风飞行型英雄装', 'caped aerial heroine', ['飞行英雄','披风英雄'], '短银发；藏蓝完整长袖长裤；铜橙色短披风和靴；肩部双扣与原创圆环胸徽；轻量护腕')
original('动力装甲型英雄装', 'powered-armor heroine', ['动力装甲','科技英雄','装甲英雄'], '棕肤成年女性短卷发；象牙白与橙色分片全身动力甲；抬起面罩露出脸部；胸腹和膝肘关节结构清楚；宽底装甲靴')
original('都市蒙面义警装', 'masked urban vigilante', ['义警','蒙面英雄','街头英雄'], '深紫短外套叠穿炭灰长裤战衣；简洁紫色眼罩；窄型工具腰带、护膝和运动靴；无披风与耳状头套')
original('极速跑者英雄装', 'speedster heroine', ['极速','速度型英雄','跑者英雄'], '深棕肤色短发；青绿完整流线运动战衣；橙色弧线从肩延伸至小腿；贴合护目镜与轻型跑靴；无披风')
original('雷电导能英雄装', 'electric-channeling heroine', ['雷电英雄','电能英雄'], '紫黑短发；紫灰完整绝缘长裤战衣；黄色导能腕环、小腿分节护具与靴；原创电路胸饰；指尖少量电弧')
original('冰晶护甲英雄装', 'ice-crystal armored heroine', ['冰系英雄','冰晶英雄'], '白色短发；冰蓝完整长袖长裤；半透明浅蓝小肩甲与前臂冰晶护片；厚底白靴；晶体不遮脸')
original('耐热焰纹英雄装', 'heat-resistant flame heroine', ['火系英雄','火焰英雄'], '深肤红褐卷发；砖红与炭灰耐热长裤服；橙色短衣领与火焰形几何肩线；厚手套和隔热靴；小型热能背包')
original('深海水压英雄装', 'deep-sea pressure-suit heroine', ['深海英雄','水系英雄'], '黑色短发；深青完整潜水式战衣；浅珊瑚色分片肩肘护具；贴合透明护目镜；鳍状小腿护片和靴，无鱼尾')
original('植物共生英雄装', 'botanical symbiosis heroine', ['植物英雄','自然系英雄'], '棕色盘发与橄榄肤色；墨绿完整布质长裤战衣；米黄叶形外层护肩与腰侧护片；软靴；少量原创藤纹而非裸露身体藤缠')
original('念力浮环英雄装', 'telekinetic ring heroine', ['念力英雄','精神系英雄'], '灰紫长发扎低马尾；浅灰完整高领长裤战衣；紫色分片腰带和手套；两只小型悬浮几何环在手掌外；无大光幕')
original('护盾救援英雄装', 'shield-and-rescue heroine', ['救援英雄','护盾英雄','防御型英雄'], '黑色短辫；白色长袖上衣与海蓝工装长裤；橙色救援背心、小急救包与护膝；前臂小型圆盾；防护靴')
original('星际巡航英雄装', 'orbital patrol heroine', ['宇宙英雄','星际英雄','太空英雄'], '银灰短发；深紫完整轻型宇航战衣；白色分片护胸和靴；肩部小推进器与开放式透明颈罩；原创双弧徽章')
original('机械翼侦察英雄装', 'mechanical-wing scout heroine', ['机械翼','侦察英雄','翼装英雄'], '棕肤黑色高马尾；浅灰长裤飞行服；铜色紧凑机械翼半折收在背后；飞行护目镜、手套和短靴；翼尖保持在画格内')
original('微型科技英雄装', 'micro-tech heroine', ['微型英雄','缩小英雄','昆虫科技'], '深蓝短发；青灰完整轻甲长裤服；透明短面罩；腰侧缩放控制器、手腕发射器与靴；无翅膀，以装备表现能力')
original('重力操控英雄装', 'gravity-control heroine', ['重力英雄','引力英雄'], '深棕肤色银色短卷发；酒红完整长袖长裤；石墨色悬浮小护肩、重型腕套和磁力靴；原创同心圆胸饰')
original('光能弓手英雄装', 'light-bow heroine', ['弓手英雄','光能英雄','能量弓'], '赤褐低辫；米白完整长袖长裤；金棕色短肩披、护臂和靴；一手持小型光能弓垂向地面；原创菱形胸扣，无拉弓射击')

assert sum(bool(e.get('superhero_reference')) for e in CATALOG) == 32
