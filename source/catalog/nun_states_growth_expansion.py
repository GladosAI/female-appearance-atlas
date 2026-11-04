"""Edition 22: nun costumes, non-graphic story states and neutral age/size studies."""
from catalog_content import CATALOG, category, add
from special_age_expansion import STAGES

NEW_CATEGORIES=['nun_costumes']
category('nun_costumes','修女装扮','32套成年修女角色服装：长袍、头巾、护颈、肩布、披风与腰带分别组合；传统灵感与日常、幻想改编分组，图例不代表所有修会的通用制服。',['R83','R84'])

def nuns(dimension,text):
    lines=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(lines)==16
    for name,en,recipe in lines:
        add('nun_costumes',dimension,f'{name}|{en}|{recipe}。')
        CATALOG[-1].update(added_in='22.0',adult_only=True,minor_reference=False,special_variant_reference=True,
            nun_reference=True,age_context='25岁及以上成年修女角色服装参考',outfit_components=recipe.split('；'),
            aliases=['修女','修女服','修道服','religious sister','nun habit',dimension],reference_ids=['R83','R84','R63'],
            note='原创成年角色服装参考；修会、地区与时代的实际着装不同。传统灵感与幻想改编分别标记，服装层次以具体图例为准。')

nuns('修女长袍与头部包覆','''
黑袍白护颈修女装|black habit white-wimple nun look|黑色高领长袖及踝长袍；白色头部内帽与护颈布；黑色后垂头巾；窄腰带与黑色平底鞋
白袍黑肩布修女装|white habit black-scapular nun look|白色高领长袖及踝长袍；黑色前后长肩布与腰带；白内帽接黑头巾；黑色平底鞋；传统灵感改编
白袍白肩布修女装|white habit white-scapular nun look|白色长袖及踝长袍；白色前后长肩布与黑色窄腰带；白内帽黑后垂头巾；黑色平底鞋；传统灵感改编
棕袍黑头巾修女装|brown habit black-veil nun look|深棕高领长袖及踝长袍；白色护颈布与内帽；黑色后垂头巾；棕色绳腰带和黑色平底鞋
灰袍白护颈修女装|grey habit white-wimple nun look|灰色高领长袖及踝长袍；白色头帽和护颈布；深灰后垂头巾；窄布腰带与黑色低跟鞋
蓝灰长袍修女装|blue-grey long-habit nun look|蓝灰色长袖及踝长袍；白色圆领内层与简洁白内帽；深蓝后垂头巾；小十字吊坠和黑色鞋
黑长披风修女装|black mantle nun ensemble|黑色长袖及踝长袍；同长黑色披风在领下扣合；白护颈布接黑头巾；黑色鞋；传统灵感改编
白长袍黑披风修女装|white habit black-mantle nun look|白色长袖及踝长袍和窄腰带；外披长黑披风；白内帽黑头巾；黑色平底鞋；传统灵感改编
肩短披覆修女装|short-shoulder-cape nun look|黑色高领长袖长袍；白色护颈接短肩披覆；黑色后垂头巾；布腰带与黑色低跟鞋
圆面口头巾修女装|round-opening veil nun look|深灰长袖长袍；白内帽形成圆润面口、耳颈均包覆；黑色后垂头巾；窄腰带和黑色鞋
方形护颈修女装|square-front wimple nun look|黑色高领长袖长袍；白色护颈布在前胸形成方形覆片；黑头巾从额后垂下；黑色平底鞋
长肩布束腰修女装|long-scapular belted nun look|灰棕长袖及踝袍；同色前后长肩布与绳腰带；白色内帽和深棕头巾；棕色平底鞋
浅色头巾修女灵感装|light-veil religious-sister look|灰色长袖长袍；白内帽接奶白后垂头巾；白色护颈布；灰色布腰带与黑色鞋；原创服装参考
宽袖叠内袖修女装|wide-sleeve layered nun habit|黑色宽袖长袍内叠完整白色长袖；白内帽护颈布和黑头巾；窄腰带；黑色低跟鞋
小十字颈饰修女装|small-cross nun habit ensemble|黑色高领长袖及踝袍；白护颈与黑头巾；简洁小十字颈饰位于衣外；黑色平底鞋
绳腰带长袍修女装|cord-belt long-habit nun look|深灰不透明长袖长袍；同色绳腰带与简洁小布袋；白内帽黑头巾；黑色平底鞋
''')

nuns('修女日常与幻想改编','''
书房工作修女装|library-work religious-sister outfit|成年修女穿灰色高领长袖上衣与黑色及踝长裙；黑色简洁头巾；腰侧小书袋；黑色平底鞋；原创日常造型
花园围裙修女装|garden-apron religious-sister outfit|灰棕长袖长袍外罩米白长围裙；黑头巾与白色内帽；双手自然放在身侧；棕色工作鞋
冬季披肩修女装|winter-shawl nun outfit|黑色长袖长袍外加灰色厚披肩；白护颈布接黑头巾；完整手套与灰腰带；黑色保暖鞋
雨天斗篷修女装|rain-cloak nun outfit|深灰不透明长袖长袍；外加黑色防雨长斗篷、开放面兜帽罩在头巾外；窄腰带；黑色雨靴
旅途短外套修女装|travel-jacket religious-sister outfit|灰色长袖上衣和深蓝长裙；黑色短外套与简洁头巾；小型肩背包；黑色平底鞋；原创现代改编
医护围裙修女灵感装|care-apron sister-inspired outfit|蓝灰长袖长袍外叠白色围裙；白色头巾完整包发；普通布腰带；黑色平底鞋；原创服务场景服装
现代衬衣长裙修女装|modern shirt-skirt religious-sister look|灰色长袖衬衣与黑色长裙；简洁黑色头巾；小十字吊坠；黑色低跟鞋；原创日常改编
现代针织外套修女装|modern cardigan religious-sister look|浅灰高领内搭与深灰长裙；黑色针织开衫和简洁黑头巾；小型布袋；黑色平底鞋；原创现代改编
旅行长衣裤装修女装|travel-trouser sister-inspired look|深灰长袖及膝外衣与完整黑色长裤；黑色简洁头巾；布腰带与肩包；黑色短靴；原创现代改编
礼仪长披风修女装|ceremonial-mantle nun inspiration|奶白高领长袖长袍与同色肩布；深蓝长披风和深蓝头巾；简洁小十字胸针；黑色鞋；原创礼仪改编
幻想巡礼修女装|fantasy-pilgrim nun costume|黑色高领长袖及踝袍；灰色短披风与白色护颈；黑头巾和腰侧布包；棕色短靴；架空幻想
幻想护甲修女装|fantasy-armoured nun costume|黑色完整长袖长袍与白护颈头巾；外加原创银灰肩护片和腰带；黑色长靴；无武器架空幻想
幻想星纹修女装|star-motif fantasy nun costume|深蓝完整长袖长袍；原创细小星点集中衣缘与肩布；白护颈和深蓝头巾；白色平底鞋；架空幻想
幻想雪地修女装|snow-pilgrim fantasy nun costume|奶白厚长袖长袍；灰色保暖长披风和开放面兜帽；内层白护颈与深灰头巾；灰色保暖靴；架空幻想
未来都市修女装|future-city nun-inspired costume|黑灰完整高领长袖长衣与长裤；白色几何肩布和简洁黑头巾；小十字形衣扣；黑色平底鞋；原创科幻
幻想仪式修女装|ritual-fantasy nun costume|深灰高领长袖及踝袍；奶白前后肩布与原创几何衣缘；白护颈接黑长头巾；黑色鞋；架空仪式改编
''')

STATE_NOTE='睡眠、昏迷与长眠均是角色剧情设定和绘画表演标签，仅凭闭眼、肤色或面部外观不能判断真实意识或生命状态。图例保持完整面孔，不表现伤口、血液或尸体损伤。'
def states(dimension,story_state,text):
    lines=[line.strip().split('|') for line in text.strip().splitlines()];assert len(lines)==16
    for name,en,feature in lines:
        add('face_states',dimension,f'{name}|{en}|{feature}。')
        aliases=['剧情状态','非血腥状态',dimension]
        aliases+= {'sleep':['睡眠','睡着','安睡','sleep'],'coma':['昏迷','无意识剧情','coma'],'long_slumber':['长眠','安息','long_slumber']}[story_state]
        CATALOG[-1].update(added_in='22.0',adult_only=True,minor_reference=False,age_context='25岁及以上成年角色面部剧情参考',
            story_state=story_state,story_state_reference=True,facial_reference=True,aliases=aliases,note=STATE_NOTE,reference_ids=['R03','R85'])

states('睡眠与熟睡剧情表演','sleep','''
安睡闭眼正面|peaceful sleeping face front|成年头肩正面，双眼自然闭合，眉间舒展，嘴唇轻闭，普通高领睡衣
安睡侧向软枕|side-resting sleeping face|成年头部侧靠浅色枕边，双眼闭合，面颊轻受压，嘴唇放松，完整普通衣领
平卧熟睡面容|supine deep-sleep face|成年仰卧头肩，头颈自然平放，双眼闭合、嘴角平缓，高领睡衣完整
熟睡微张口|sleeping face with slightly parted lips|成年仰卧脸部，双眼轻闭，嘴缝仅小幅张开，下颌放松，无液体痕迹，普通衣领
浅睡轻皱眉|light-sleep faint frown|成年侧靠头肩，闭眼且眉心轻微聚起，嘴唇闭合，普通高领睡衣
睡梦轻微笑意|subtle smiling dream face|成年闭眼脸部，眉线放松，嘴角只有细小上扬，非夸张表情，普通衣领
午睡额侧倚靠|nap face resting at temple|成年头部略侧靠枕边，额侧接触软垫，双眼闭合，嘴角松弛，普通衣领
睡眠面颊受压|sleeping cheek compression|成年侧卧脸部，一侧面颊被浅色软枕轻压，双眼自然闭合，口型小幅偏移，普通衣领
睡眠额前碎发|sleeping face with loose fringe|成年闭眼正脸，额前少量碎发散下，眉线舒展，唇自然闭合，高领衣缘清楚
睡眠侧脸轮廓|sleeping facial side profile|成年完整头部侧面，眼睑闭合，鼻唇下颌轮廓自然，发梢和普通睡衣领均在画面内
睡眠三分之四侧脸|sleeping three-quarter face|成年斜侧头肩，双眼闭合，眉尾松弛，嘴角自然，白色枕边与高领衣缘清楚
熟睡低眉松脸|deep-sleep relaxed brows|成年正面头肩，眉位较低但不紧绷，双眼闭合、面肌放松，普通高领衣物
侧睡手背枕旁|side-sleep hand beside pillow|成年侧靠枕边，闭眼，单只正常五指手背放在枕旁而不遮面，普通长袖睡衣
趴桌睡眠托额|desk-nap forehead on forearm|成年头肩伏在穿完整长袖的前臂上，额头轻靠手臂，面孔斜向可见且双眼闭合
将醒半睁一线|nearly waking narrow eyelids|成年平卧脸部，上眼睑只抬起一条窄缝，瞳孔正常、视线尚未集中，眉嘴放松，普通衣领
睡眠后松缓睁眼|relaxed post-sleep opening eyes|成年头肩，双眼由闭合转为轻度半开的一帧，眉间舒展，嘴轻闭，枕边与普通高领衣缘可见
''')

states('昏迷与无意识剧情表演','coma','''
昏迷闭眼正面|unconscious-story face front|成年平卧头肩正面，双眼闭合，眉线平缓，嘴唇轻闭，完整高领衣缘；剧情设定为昏迷
昏迷平卧微张口|unconscious-story parted-lip face|成年仰卧头肩，双眼闭合，下颌轻度放松、嘴缝小幅张开，普通衣领完整；剧情昏迷
昏迷侧向面容|unconscious-story side-turned face|成年头部轻转一侧，双眼闭合，面部结构完整，嘴角平缓，高领衣缘；剧情昏迷
昏迷三分之四脸|unconscious-story three-quarter face|成年斜侧头肩，眼睑闭合、眉尾平放、口型放松，简洁枕边；剧情昏迷
昏迷松眉面容|unconscious-story relaxed-brow face|成年正面头肩，眉间舒展、双眼闭合，嘴唇轻闭，普通衣领；剧情昏迷
昏迷眉心轻聚|unconscious-story faint brow tension|成年平卧脸部，闭眼且眉心少量紧张，嘴缝轻开，普通衣领完整；非血腥剧情昏迷
昏迷苍白色感|unconscious-story pale lighting|成年完整脸部，双眼闭合，自然肤色在柔和偏冷光下略显苍白，嘴角松弛，高领衣缘；剧情昏迷
昏迷自然肤色|unconscious-story natural complexion|成年完整脸部，保留正常暖肤色，双眼闭合，眉嘴放松，高领衣缘；剧情昏迷
昏迷低垂下颌|unconscious-story relaxed jaw|成年仰卧头肩，下颌轻度放松但关节自然，嘴缝小幅张开，双眼闭合，普通衣领；剧情昏迷
昏迷耳侧散发|unconscious-story side hair|成年侧转头肩，耳侧发束自然散开，闭眼、唇轻闭，完整高领衣缘；剧情昏迷
昏迷短发侧脸|short-haired unconscious-story profile|成年短发完整侧脸，眼睑闭合，眉鼻唇轮廓清楚，普通衣领；剧情昏迷
昏迷长发枕边|long-haired unconscious-story face|成年仰卧头肩，长发在枕上自然展开但不遮面，闭眼，嘴角放松，普通高领衣缘；剧情昏迷
昏迷额侧汗滴|unconscious-story forehead perspiration|成年平卧完整面孔，双眼闭合，额侧仅一两滴小汗，眉线略聚，普通衣领；非诊断剧情昏迷
昏迷平静面容|calm unconscious-story face|成年正面头肩，闭眼且面部肌肉平静，正常肤色，嘴唇轻闭，普通高领衣缘；剧情昏迷
昏迷半睑剧情脸|half-lidded unconscious-story face|成年平卧脸部，眼睑留很窄缝隙、瞳孔正常且无翻白眼，嘴角松弛，普通衣领；剧情昏迷
昏迷侧光面容|side-lit unconscious-story face|成年斜侧头肩，柔和侧光表现完整鼻颊体积，双眼闭合，唇自然放松，高领衣缘；剧情昏迷
''')

states('长眠与安息剧情表演','long_slumber','''
长眠闭眼正面|non-graphic long-slumber face front|成年平卧完整面孔，双眼自然闭合，眉嘴放松，普通高领衣缘；剧情设定为长眠而非医学判定
长眠侧向平卧|non-graphic long-slumber side turn|成年头部平卧并转向一侧，双眼闭合、嘴唇轻闭，完整面部与普通衣领；非血腥长眠剧情
长眠三分之四脸|non-graphic long-slumber three-quarter face|成年斜侧平卧头肩，眼睑闭合，眉线平缓，嘴角自然，普通高领衣缘；非血腥长眠剧情
长眠微张口静止|non-graphic long-slumber parted lips|成年平卧脸部，双眼闭合、下颌轻松、嘴缝小幅张开，普通衣领完整；非血腥长眠剧情
长眠半睁失焦|non-graphic long-slumber unfocused half eyes|成年完整脸部，眼睑半开且保留正常虹膜瞳孔，视线失焦，嘴唇轻开，高领衣缘；剧情长眠
长眠闭眼苍白色感|non-graphic long-slumber pale face|成年完整面孔在柔和冷光下肤色略淡，眼睑闭合，眉嘴放松，普通衣领；非诊断长眠剧情
长眠自然肤色面容|non-graphic long-slumber natural complexion|成年完整面孔保留自然暖肤色，闭眼，嘴唇轻闭，高领衣缘；剧情长眠，不用肤色作为判据
长眠平缓眉线|non-graphic long-slumber relaxed brows|成年正面头肩，眉位平缓、眼睑自然闭合，嘴角不带笑，普通衣领完整；非血腥长眠剧情
长眠短发侧脸|non-graphic long-slumber short-haired profile|成年完整短发侧脸，闭眼，鼻唇下颌结构自然，普通高领衣缘；非血腥长眠剧情
长眠长发枕边|non-graphic long-slumber long hair on pillow|成年平卧头肩，头发在枕边散开但脸部清楚，闭眼，嘴角放松，完整衣领；非血腥长眠剧情
长眠额前散发|non-graphic long-slumber loose forehead hair|成年闭眼正脸，额前几束散发，眉线平缓，口唇自然闭合，高领衣缘；非血腥长眠剧情
长眠年长面容|non-graphic long-slumber older adult face|明确年长成年女性平卧面孔，灰发、自然细纹和完整皮肤，双眼闭合，普通衣领；非血腥长眠剧情
长眠成熟面容|non-graphic long-slumber mature adult face|40岁以上成年女性完整平卧面孔，闭眼且眉口平静，普通高领衣缘；非血腥长眠剧情
长眠斜侧半睑|non-graphic long-slumber three-quarter half eyes|成年斜侧面孔，半垂眼睑下虹膜瞳孔正常，视线未集中，唇轻闭，普通衣领；剧情长眠
长眠安静告别面容|non-graphic quiet-farewell face|成年完整平卧头肩，闭眼，眉间舒展但不做夸张微笑，普通高领衣缘；非血腥长眠剧情
长眠侧光安息面容|non-graphic repose face side light|成年斜侧完整面孔，柔和侧光强调鼻颊与闭合眼睑，嘴角自然，衣领完整；非血腥长眠剧情
''')

# All numeric values below are invented character-design settings, not population norms.
HEIGHTS=[52,66,78,98,118,136,154,163,165,168,160,164,158,162,154,150]
HEAD_UNITS=[3.5,4,4.5,5,5.5,6,6.5,7,7.25,7.5,7.25,7.4,7.1,7.25,7,6.9]
for i,stage in enumerate(STAGES):
    ident,label,low,high,group,en,face,body=stage
    infant=low<2;metric='卧长' if infant else '身高';minor=low<18
    value=HEIGHTS[i];head=HEAD_UNITS[i]
    name=label+'身长比例设定' if infant else label+'身高比例设定'
    feature=f'{body}；{metric}{value}cm、约{head:g}头身，均为原创角色比例设定；衣物完整、姿态中性'
    add('female_life_stages','身高与整体比例设定',f'{name}|{en} stature and proportion setting|{feature}。')
    CATALOG[-1].update(added_in='22.0',life_stage_reference=True,growth_reference=True,age_min=low,age_max=high,
        age_stage=ident,age_range=label,life_stage_group=group,view_type='proportion',adult_only=not minor,minor_reference=minor,
        age_context=label+'；适龄完整日常着装',stature_kind='length' if infant else 'height',head_units=head,
        measurement_basis='fictional-character-setting',aliases=['身高对照','头身比','发育比例','中性成长参考',label,group,f'{value}cm'],
        reference_ids=['R81','R86'],note='身高、卧长和头身比都是原创角色创作数值，不是平均值、生长标准或健康判断。婴幼儿用卧长、其余用身高标签；图页按格子归一化，数值差异在页面对照图中查看。')
    CATALOG[-1]['length_cm' if infant else 'height_cm']=value

ADULT_SETTINGS=[
 ('成年25—34岁小个体型',25,34,150,84,66,92,6.9,'small-stature adult','自然小个体型，肩臂和四肢比例成熟'),
 ('成年25—34岁中等体型',25,34,160,90,72,98,7.2,'medium-build adult','自然中等体型，躯干与四肢关系均衡'),
 ('成年25—34岁高个直线体型',25,34,170,86,72,94,7.5,'tall straight-build adult','自然高个体型，腰胯转折较缓'),
 ('成年25—34岁高个丰润体型',25,34,180,100,82,108,7.6,'tall fuller-build adult','自然高个丰润体型，身体体积均匀而不夸张'),
 ('成年35—49岁小个体型',35,49,152,88,74,98,7,'small-stature mature adult','自然小个成熟体型，头肩与四肢清楚'),
 ('成年35—49岁中等丰润体型',35,49,162,98,84,106,7.2,'medium fuller mature adult','自然中等丰润体型，腰腹轮廓柔和'),
 ('成年35—49岁高个直线体型',35,49,172,92,76,100,7.5,'tall straight mature adult','自然高个体型，躯干较直且四肢舒展'),
 ('成年35—49岁高个宽体型',35,49,182,106,90,114,7.6,'tall broad mature adult','自然高个宽体型，肩部与骨架体积较大'),
 ('成年50—64岁小个体型',50,64,148,90,82,100,6.9,'small-stature middle-aged adult','自然小个中年体型，腹腰轮廓保留个体变化'),
 ('成年50—64岁中等丰润体型',50,64,158,100,90,110,7.1,'medium fuller middle-aged adult','自然中等丰润体型，整体体积不只集中一处'),
 ('成年50—64岁高个体型',50,64,168,96,84,104,7.4,'tall middle-aged adult','自然高个中年体型，站姿放松，皮肤完整'),
 ('成年50—64岁高个宽体型',50,64,178,110,98,118,7.5,'tall broad middle-aged adult','自然高个宽体型，腰腹和肩胯均有体积'),
 ('年长65岁以上小个体型',65,None,146,86,80,96,6.8,'small-stature older adult','自然小个年长体型，灰发与轻度皱纹，站姿稳定'),
 ('年长65岁以上中等体型',65,None,156,94,88,104,7,'medium-build older adult','自然中等年长体型，腰部较缓，姿态舒适'),
 ('年长65岁以上高个体型',65,None,166,100,94,110,7.2,'tall older adult','自然高个年长体型，保留挺拔站姿和个人面容'),
 ('年长65岁以上高个宽体型',65,None,176,106,100,116,7.4,'tall broad older adult','自然高个宽体型年长女性，灰发，稳定重心')
]
for i,(label,low,high,height,bust,waist,hip,head,en,shape) in enumerate(ADULT_SETTINGS):
    feature=f'{low}岁以上明确成年女性，{shape}；穿不透明无图案高领长袖贴合运动上衣与完整长裤、平底鞋；身高{height}cm，胸围{bust}cm、腰围{waist}cm、臀围{hip}cm，约{head:g}头身；数值均为虚构角色设定'
    add('female_life_stages','成年三围与体型设定',f'{label}尺寸参考|{en} fictional circumference setting|{feature}。')
    CATALOG[-1].update(added_in='22.0',life_stage_reference=True,adult_measurement_reference=True,adult_only=True,minor_reference=False,
        age_min=low,age_max=high,age_stage=f'adult_measure_{i+1:02}',age_range=label,life_stage_group='成年体型设定',view_type='adult_measurements',
        age_context=f'{low}岁以上成年女性；完整不透明日常运动着装',height_cm=height,bust_cm=bust,waist_cm=waist,hip_cm=hip,head_units=head,
        stature_kind='height',measurement_basis='fictional-character-setting',
        aliases=['成年三围','成人三围','胸围','腰围','臀围','身高','体型尺寸',f'{height}cm',label],reference_ids=['R09','R81'],
        note='三围仅用于明确成年原创角色，数值是周长而非正面宽度；图片近似表现体型，精确设定以数字和对照图为准。身高与三围不对应固定年龄、发育程度或理想标准。')

assert sum(bool(e.get('nun_reference')) for e in CATALOG)==32
assert sum(bool(e.get('story_state_reference')) for e in CATALOG)==48
assert sum(bool(e.get('growth_reference')) for e in CATALOG)==16
assert sum(bool(e.get('adult_measurement_reference')) for e in CATALOG)==16
