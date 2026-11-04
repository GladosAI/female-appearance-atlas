"""Original adult Chinese-fantasy immortal and spirit costume references."""
from catalog_content import CATALOG, category, add

NEW_CATEGORIES=['chinese_fairy_outfits','chinese_demoness_outfits']
GROUPS=[('immortal','chinese_fairy_outfits','中式仙女与女仙','仙女礼装与仙门行装'),('spirit','chinese_demoness_outfits','中式妖女与精怪','妖女灵怪与异化装束')]
category('chinese_fairy_outfits','中式仙女与女仙','16项原创中式仙女、女仙与仙门行装，比较广袖、披帛、云肩、叠裙、束袖、发冠、佩玉与法具。仙侠幻想与历史服装分别理解；飞天条目为乐舞飘带意象的架空改编。',['R159','R160'])
category('chinese_demoness_outfits','中式妖女与精怪','16项原创中式妖女、灵怪化身与妖修装束，比较人形服装、耳尾角等局部异化、纹样、披肩和道具。妖女是幻想身份标签，不以外貌判断善恶；狐、蛇、花木等为创作主题。',['R160','R162'])

def block(kind, text):
    _,cid,_,dimension=next(g for g in GROUPS if g[0]==kind)
    rows=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(rows)==16
    for name,en,aliases,recipe in rows:
        add(cid,dimension,f'{name}|{en}|原创成年中式幻想角色；{recipe}。')
        e=CATALOG[-1]
        e.update(added_in='41.0',adult_only=True,minor_reference=False,age_min=25,chinese_fantasy_reference=True,
            chinese_fantasy_kind=kind,styles=['chinese'],aliases=aliases.split('、'),outfit_components=recipe.split('；'),illustration_recipe=recipe,
            reference_ids=['R159','R160'] if kind=='immortal' else ['R160'],
            note='原创成年中式幻想装束，形制、配色、纹样及局部异化为设计推演，非历史服装、宗教仪轨或某部作品人物的精确复原。先区分衣领、袖型、裙裤和外层，再观察头饰、佩饰与法具；身份标签不表示角色善恶。')

block('immortal','''
云裳广袖仙女装|cloud-sleeved immortal robes|云裳、广袖仙女、仙女、云仙|墨色高髻与双玉簪；月白交领内衫、淡青广袖外衫与及踝长裙；细金腰带与长披帛绕双臂；青色绣鞋露出鞋尖
月宫桂影仙姝装|moon-palace osmanthus immortal|月宫、嫦娥主题、桂花、月仙|墨色长发半挽与银色月弧发饰；银灰长袖上衣、淡紫叠裙与桂叶形云肩；腰间玉兔形小佩；银白绣鞋，无额外动物
莲华叠瓣仙女装|lotus-petal immortal ensemble|莲花、荷花、莲仙、花仙|黑色盘髻与粉白莲花发梳；奶白窄袖完整内裙；淡粉叶瓣形叠裙与青绿色短披帛；玉色腰扣与绣鞋
瑶池云肩仙女礼装|celestial-court cloud-collar robes|瑶池、仙宫、天宫、仙女礼服|黑色高盘发与小型金色花冠；朱霞色交领长袖衣；米白及踝褶裙与金边四合式云肩；腰垂双玉佩；金白绣鞋
飞天飘带仙装改编|feitian-inspired ribbon costume|飞天、飘带、敦煌灵感、仙女舞衣|墨色高髻与小型莲形额饰；完整不透明赭金长袖内衣、青绿高腰长裙；朱红披帛绕臂形成小弧；脚穿金色软鞋；双脚站立，乐舞意象改编
御剑女仙束袖装|sword-immortal fitted-sleeve robes|御剑、剑仙、女剑仙、仙侠|黑色高马尾与银色束发冠；白色交领束袖长衣；藏青及踝分片外裙下穿完整长裤；窄腰封与护腕；白靴；一手持入鞘长剑垂向地面
拂尘女仙道袍装|fly-whisk immortal robe|拂尘、女冠灵感、道袍、仙门|黑色盘发与素玉簪；青灰交领宽袖道袍式外衣、米白完整内衣与长裤；简洁布腰带；黑色布靴；一手低持白色拂尘，非仪轨复原
灵药采芝仙女装|herb-gathering immortal attire|采药、灵芝、药仙、花篮|黑色低髻与竹木发簪；草绿窄袖短襦与米白及踝长裙；短披肩、布腰带与棕色绣鞋；手提小竹篮，篮中少量灵芝与草叶
琴音抱琴女仙装|qin-bearing immortal robes|琴仙、古琴、乐仙、音修|墨色长发半挽与银簪；浅杏交领宽袖衣与墨绿及踝长裙；窄披帛与双玉佩；黑色绣鞋；双手竖抱一张窄长古琴，琴尾离地
荷灯临水仙女装|lotus-lantern river immortal|荷灯、河仙、水仙、河灵|黑色侧挽髻与水滴玉簪；淡蓝长袖上衣、青碧及踝叠裙；波纹衣缘与银色细腰链；手低提一盏小型荷灯；浅青绣鞋
竹林隐逸女仙装|bamboo-grove recluse immortal|竹林、隐仙、竹仙、隐逸|墨色低马尾与竹节簪；米白窄袖内衫、深绿长袍式外层和完整长裤；竹叶形短肩披；布腰带与棕靴；无大型道具
梅雪冬衣仙姬装|plum-and-snow winter immortal|梅花、雪仙、冬装仙女、梅仙|银灰长发盘髻与小梅花簪；月白完整长袖长裙；灰蓝短保暖披肩与深红梅枝衣缘；深红腰封与白色短靴
星斗司辰女仙装|star-chart celestial immortal|星斗、星官、司辰、星仙|黑色高盘发与小型银色星形发冠；藏蓝立领长袖衣与及踝长裙；金色简化星图纹沿外袍下摆排列；银色腰带与靴；一手持小型星盘
赤霞流火女仙装|crimson-cloud fire immortal|赤霞、火仙、赤练仙衣、霞仙|深棕长发高束与金簪；米白完整长袖内裙；朱红外衫与橙金渐层叠裙；短披帛、金色护腕与红绣鞋；无火焰遮挡衣物
云鹤羽衣女仙装|crane-feather immortal mantle|云鹤、鹤仙、羽衣、鹤氅|黑白挑染高髻与银鹤形发簪；奶白交领长袍和完整长裤；黑白羽纹短鹤氅披在肩上，不生翅膀；墨色腰带与白靴
凌波泉灵仙女装|spring-water immortal robes|凌波、泉灵、水灵、碧波|墨色长发半挽与青玉发梳；青白完整窄袖上衣与湖蓝及踝长裙；水波形外裙片、银色腰结与贝形小佩；浅蓝绣鞋，无鱼尾
''')

block('spirit','''
白狐妖女披领装|white-fox spirit robes|白狐、狐妖、狐仙、狐狸精|银白长发、白色狐耳与一条收于身侧的白色狐尾；深红完整交领长袖衣与及踝白裙；白色短绒披领、玉扣腰带与红色绣鞋
九尾狐妖宽袖装|nine-tailed fox spirit costume|九尾狐、狐妖、青丘、狐狸精|墨红长发与红褐狐耳；紫红完整长袖长裙与金色腰结；九条红褐色毛尾在背后分成紧凑扇形，各尾尖可辨；黑色绣鞋，尾部不遮人物衣身
白蛇化身素衣装|white-snake spirit attire|白蛇、蛇妖、白蛇精、蛇女|黑色盘髻与银色蛇形小簪；白色交领长袖衣与及踝叠裙；浅银鳞纹沿袖口和裙缘排列；青玉腰带与白鞋；少量颊侧鳞片，保留完整人形双腿
青蛇妖女剑装|green-snake spirit sword attire|青蛇、蛇妖、青蛇精、蛇女|墨绿高马尾与弯曲玉簪；青绿完整束袖长衣与深绿长裤；墨色短外裙片、护腕和靴；一手持入鞘短剑；太阳穴少量细鳞，无蛇尾
玄猫妖女短褂装|black-cat spirit jacket ensemble|猫妖、猫女、玄猫、猫精|黑色短发与黑色猫耳、单条细长黑尾；紫灰交领短褂与完整黑色长袖内衣；及踝灰裙和黑色布靴；小型铃铛系于腰侧
蝶妖斑纹叠裙装|butterfly spirit layered robes|蝶妖、蝴蝶精、蝶女|黑紫长发半挽与蝶形发簪；浅紫完整长袖内裙；紫黑蝶翅纹外裙片；背后两对小型蝶翼半收，完整留在画格内；黑色绣鞋
蛛妖织纹长袍装|spider spirit web-patterned robe|蛛妖、蜘蛛精、蛛女|黑色高髻与银丝网形发饰；墨紫完整长袖及踝长袍；银色几何蛛网纹沿肩袖与裙缘排列；细银腰带与黑靴；保持人形两臂两腿，无额外蜘蛛腿
鲤鱼精鳞纹裙装|carp spirit scale-patterned skirt|鲤鱼精、鱼妖、鲤女、锦鲤|栗红盘发与小型金鳍形发饰；米白完整窄袖上衣；橙红及踝鱼鳞纹长裙与鳍形外裙片；金色腰扣与红鞋；双腿人形，无鱼尾
山鹿灵角披肩装|mountain-deer spirit mantle|鹿灵、鹿妖、山灵、鹿女|棕色长发与两只小型分叉鹿角；赭色交领长袖长裙；青绿叶形短披肩与鹿斑衣缘；布腰带、木珠佩饰和棕色软靴
乌羽夜鸦妖女装|night-raven spirit robes|鸦妖、乌鸦、鸦女、羽妖|黑色长发与乌羽簪；蓝黑完整立领长袖长衣；深紫及踝长裙；乌羽形小披肩与银色扣带；黑色长靴，无大型翅膀
牡丹花妖云肩装|peony spirit petal collar robes|牡丹、花妖、牡丹精、花灵|黑色高髻与深红牡丹发饰；奶白完整长袖内裙；深红花瓣形短云肩与墨绿叠裙片；金色细腰带与红绣鞋
桃花妖女襦裙装|peach-blossom spirit ruqun|桃花、花妖、桃花精、桃灵|栗棕长发半挽与桃枝发簪；浅粉完整交领上襦；深粉及踝褶裙；米白小披肩与花瓣佩饰；粉色绣鞋，无大片漂浮花瓣
青竹木灵长衣装|bamboo-and-wood spirit robes|竹妖、木灵、竹精、树精|黑绿低髻与细竹簪；深绿完整束袖长衣和米白长裤；竹叶形短外裙片；棕色树皮纹腰带与软靴；手腕少量木纹，身体仍为人形
赤焰妖修束袖装|ember sorceress fitted-sleeve costume|妖修、赤焰妖女、魔修、邪派|深红高马尾与黑玉簪；炭灰完整长袖内衣与黑色长裤；暗红前开束袖长外袍；几何金色护腕与黑靴；额间一点红纹，无火焰遮衣
霜角妖女冷色袍装|frost-horn spirit robes|霜妖、冰妖、角妖、雪妖|银蓝长发与两只短冰晶形角；灰白完整长袖内裙；靛蓝及踝外袍与小型冰晶肩饰；银色腰封、白手套与短靴
幽灯妖女长帷装|ghost-lantern spirit veiled robes|幽魂、灯妖、幽灯、鬼女|黑色长发与浅灰后垂长帷、面部可见；灰紫完整长袖及踝长衣；墨青短披肩与银色扣带；手低提一盏小青灯；黑鞋露出，无伤痕
''')

e=next(e for e in CATALOG if e.get('chinese_fantasy_reference') and e['name']=='飞天飘带仙装改编')
e['reference_ids']=['R161','R159'];e['note']='飞天源自佛教艺术中的天人乐舞意象，此项仅借鉴飘带、色彩与舞衣结构，改编为完整覆盖的原创站姿装束，不把飞天等同于道教女仙，也不作宗教仪轨或壁画复原。'
for e in CATALOG:
    if e.get('chinese_fantasy_reference') and any(a in e['name'] for a in ['白狐','九尾狐']):e['reference_ids']=['R162','R160']
assert sum(bool(e.get('chinese_fantasy_reference')) for e in CATALOG)==32
