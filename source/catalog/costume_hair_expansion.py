"""Edition 20: special costumes and observable hair conditions for adult characters."""
from catalog_content import CATALOG, category, add

SPECIAL_CATEGORIES=['disguise_outfits','undead_costumes','outlaw_costumes','tactical_outfits','intimate_costumes','wet_outfits']
NEW_CATEGORIES=SPECIAL_CATEGORIES+['hair_states']
category('disguise_outfits','女扮男装','16套成年女性采用男装剪裁的原创角色造型；比较西装、长袍、工装与舞台装，服装表达不限定角色的性别认同。',['R06','R63'])
category('undead_costumes','僵尸与吸血鬼装扮','32套原创幻想装扮：中式僵尸、现代丧尸主题与吸血鬼分别设计；以衣物、配色、妆面与道具形成识别。',['R22','R63'])
category('outlaw_costumes','囚犯与匪徒装扮','16套影视与架空角色服装，按囚服、盗贼、匪徒与都市反派比较轮廓、衣层和配件。',['R06','R63'])
category('tactical_outfits','特种部队装扮','16套原创特勤与战术服装外观，比较气候层次、背心、头盔、腰带及鞋靴；是角色服装设计参考。',['R34','R63'])
category('intimate_costumes','情趣主题装扮','16套成年尺码情趣主题衣物，使用中性灰服装人台展示胸衣、连体衣、罩裙与配饰结构，便于观察裁片与层次。',['R13','R63'])
category('wet_outfits','湿水衣物与内搭','16套成年女性湿水服装造型，比较水渍边界、湿润反光、半透外层和可见的不透明内衣或内搭，保留完整穿着层次。',['R05','R11'])
category('hair_states','头发形态与状态','64项头发状态：睡醒与简易打理、湿润油润干燥、烫卷与风中运动、白发稀疏与颜色变化。发色与稀疏只表示可见特征，不能由外观判定健康原因。',['R01','R02','R79','R80'])

def outfits(key,dimension,text,aliases=(),styles=()):
    lines=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(lines)==16,(key,dimension,len(lines))
    for number,(name,en,recipe) in enumerate(lines):
        item_aliases=list(aliases)
        if key=='outlaw_costumes':item_aliases=['囚犯','监狱囚犯','prison costume'] if number<6 else ['匪徒','盗贼','outlaw']
        add(key,dimension,f'{name}|{en}|{recipe}。')
        CATALOG[-1].update(added_in='20.0',special_expansion=True,adult_only=True,
            age_context='成年角色服装参考',outfit_components=recipe.split('；'),styles=list(styles),
            aliases=['特殊装扮扩充',dimension,*item_aliases],reference_ids=['R63','R05'])
        if key=='intimate_costumes':
            CATALOG[-1].update(presentation='neutral-adult-tailoring-form',age_context='成年尺码服装人台',note='图例为中性灰成年尺码服装人台，重点展示成衣、不透明衬底、搭扣与配饰固定点。')
        if key=='wet_outfits':
            CATALOG[-1]['note']='湿水外衣的深浅、水渍边界与半透处用于表现布料；可见内搭保留独立衣缘和不透明覆盖。'

outfits('disguise_outfits','男装剪裁与身份造型','''
三件套绅士男装扮相|three-piece gentleman disguise|成年女性穿深灰男式西装外套、马甲和直筒西裤；白衬衣窄领带；短侧分发；黑色德比鞋
燕尾礼服男装扮相|tailcoat menswear disguise|成年女性穿黑色后长燕尾服；白色高腰马甲和白领结；黑色直筒礼裤；黑色漆皮鞋
双排扣长大衣男装扮相|double-breasted overcoat disguise|成年女性穿灰色宽肩双排扣长大衣；衬衣与领带；深灰长裤；皮手套和黑色短靴
报童马甲男装扮相|newsboy waistcoat disguise|成年女性穿棕色粗花呢马甲与米白衬衣；背带直筒长裤；报童帽；棕色系带鞋
侦探风衣男装扮相|detective trench menswear disguise|成年女性穿卡其长风衣；白衬衣深色领带；深棕西裤；软呢帽与棕色皮鞋
管家礼装男装扮相|butler menswear disguise|成年女性穿黑色立领燕尾外套与灰马甲；白衬衣领结；黑色长裤；白手套和黑色皮鞋
中式长衫男装扮相|Chinese long-gown menswear disguise|成年女性穿深蓝男式长衫；浅灰内领与长裤；小圆帽；黑色布鞋；架空近代舞台改编
古风书生男装扮相|scholar-robes menswear disguise|成年女性穿青灰交领直身长袍；深蓝腰带；包发巾；黑色布靴；原创古风书生改编
古风侠客男装扮相|wandering-swordsman costume disguise|成年女性穿深灰窄袖交领长衣；黑腰封与直腿长裤；束发髻；黑色布靴；无武器古风改编
骑装外套男装扮相|riding-jacket menswear disguise|成年女性穿棕色收腰骑装外套；米色衬衣和高腰长裤；短檐骑装帽；棕色长靴
水手长裤男装扮相|sailor-trouser menswear disguise|成年女性穿海军蓝翻领水手上衣；同色宽直长裤；白色无字水手帽；黑色低帮鞋
飞行夹克男装扮相|aviator-jacket menswear disguise|成年女性穿棕色飞行夹克与米色衬衣；卡其长裤；皮质飞行帽与护目镜置于帽顶；棕靴
宽肩工装男装扮相|workwear menswear disguise|成年女性穿深蓝宽肩工装外套；灰色圆领内搭与宽工装裤；布帽；黑色工作靴
复古摇滚男装扮相|retro-rock menswear disguise|成年女性穿黑色短皮夹克与白衬衣；窄直黑长裤；向后梳短发；黑色切尔西靴
舞台小胡须男装扮相|stage moustache menswear disguise|成年女性穿酒红马甲黑色西装；白衬衣与细领结；短发加可辨的贴饰小胡须；黑色长裤与皮鞋
现代中性宽西装男装扮相|oversized modern menswear disguise|成年女性穿浅灰宽肩西装和白色圆领内搭；同色宽腿长裤；简单背头；白色平底鞋
''',['女扮男装','男装扮相','反串','cross-dressing','menswear disguise'],['retro'])

outfits('undead_costumes','中式僵尸与现代丧尸主题','''
圆帽长袍中式僵尸装|round-cap jiangshi costume|深蓝立领宽袖长袍与黑色长裤；黑色圆顶帽前夹原创抽象纸签；浅灰舞台妆；黑布鞋；中式僵尸幻想
披肩长袍中式僵尸装|shoulder-cape jiangshi costume|紫黑长袍外加短圆披肩；暗金滚边与长裤；圆帽和原创纸签；黑布靴；中式僵尸幻想
对襟短褂中式僵尸装|short-jacket jiangshi costume|墨绿对襟盘扣短褂；黑色宽长裤；黑圆帽与原创纸签；白色裹腿和黑布鞋
云肩长裙中式僵尸装|cloud-collar jiangshi costume|暗紫立领袄与长裙；肩部云肩式覆片；圆帽加短原创纸签；深紫绣鞋
窄袖腰封中式僵尸装|narrow-sleeve jiangshi costume|蓝灰窄袖长袍；黑色宽腰封和长裤；小圆帽与两侧垂发；黑色短靴
红黑嫁衣僵尸装|red-black bridal jiangshi costume|暗红交领长衣配黑红长裙；小花冠上固定原创纸签；苍白舞台妆；红黑绣鞋；幻想改编
长袍高帽中式僵尸装|tall-cap jiangshi costume|黑色立领长袍加紫色领缘；直身长裤；高圆帽与抽象纸签；黑色厚底布鞋
破边叠袍中式僵尸装|frayed-layer jiangshi costume|暗蓝长外袍边缘做少量旧化毛边；灰色内衣与长裤完整覆盖；圆帽；黑布靴；衣物旧化无伤口
旧卫衣现代丧尸装|worn-hoodie zombie costume|旧灰卫衣配深蓝牛仔长裤；浅灰眼周妆与凌乱短发；布料破边下有完整内衬；旧运动鞋
旧夹克现代丧尸装|worn-jacket zombie costume|褐色短夹克和灰色T恤；旧黑直筒长裤；脸颊灰色舞台晕染；棕靴；无伤口与血迹
旧办公室丧尸装|office-wear zombie costume|灰色西装与歪斜领带；白衬衣和黑色长裤；松散盘发与浅灰妆；黑色皮鞋；只表现旧化
雨衣巡游丧尸装|raincoat-parade zombie costume|暗黄短雨衣外搭灰色运动套装；衣缘旧化但身体完整覆盖；湿散发与浅灰舞台妆；雨靴
旧运动服丧尸装|tracksuit zombie costume|褪色紫色拉链运动外套与长运动裤；松散头发与淡灰眼周；手腕普通运动护带；旧跑鞋
旧连体工装丧尸装|coverall zombie costume|灰绿长袖连体工装；膝肘布片磨毛与灰尘色；黑发凌乱和浅灰妆；黑色工作靴
旧礼服丧尸巡游装|worn-formal zombie parade look|灰紫长袖及踝礼服外加旧短外套；下摆少量布条装饰；乱发与苍白舞台妆；黑色低跟鞋
科幻休眠丧尸主题装|sci-fi dormant-undead costume|灰白不透明连体制服；蓝灰领肩拼片与完整手套；浅灰眼周妆和散发；灰白短靴；原创非血腥幻想
''',['僵尸','丧尸','jiangshi','zombie'])

outfits('undead_costumes','吸血鬼与夜行礼装','''
高领披风吸血鬼礼装|high-collar vampire cape ensemble|黑色高立领长披风配暗红内里；白衬衣与黑马甲长裤；小型尖牙舞台妆；黑色短靴
蕾丝长裙吸血鬼装|lace-gown vampire costume|黑色不透明长袖收腰长裙；暗红蕾丝覆片和颈饰；小型尖牙与苍白妆；黑色低跟鞋
燕尾长裤吸血鬼装|tailcoat vampire trouser costume|酒红男式燕尾外套；黑衬衣与黑色修身长裤；银色胸针与尖牙舞台妆；黑色皮鞋
维多利亚吸血鬼装|Victorian-inspired vampire costume|深紫高领泡袖上衣；黑色层叠及踝裙；短斗篷与暗银胸针；黑色系带靴
黑金贵族吸血鬼装|black-gold aristocratic vampire costume|黑色金边长外套与白色高领衬衣；黑色直筒长裤；暗金胸针和小尖牙；黑色长靴
蝙蝠领披肩吸血鬼装|bat-collar vampire capelet costume|黑色角形蝙蝠领短披肩；暗红长袖连裙；原创蝙蝠形小胸针；黑色低跟鞋
都市皮衣吸血鬼装|urban-leather vampire costume|黑色长皮外套和灰色高领衫；深灰长裤；暗红眼妆与小尖牙；黑色厚底靴
白色夜宴吸血鬼装|white-evening vampire costume|象牙白高领长袖礼裙；黑色窄腰带与灰白短披风；暗红耳饰和小尖牙；白色低跟鞋
学者长袍吸血鬼装|scholar-robes vampire costume|黑色立领长袍外加深紫长马甲；白色内领与长裤；细链胸针和尖牙妆；黑色短靴
旅行斗篷吸血鬼装|traveller-cloak vampire costume|暗蓝兜帽长斗篷敞开面部；灰色衬衣黑马甲长裤；暗红领扣；黑色长靴
舞会面罩吸血鬼装|masquerade vampire costume|黑紫长袖礼服与窄裙摆；手持小型半脸面罩放在身侧；银色发梳与小尖牙；黑色鞋
皮革护肩吸血鬼装|leather-shoulder vampire costume|黑色短皮护肩接暗红长披片；黑色高领衬衣与长裤；银色腰扣；黑色长靴
复古衬衣吸血鬼装|ruffled-shirt vampire costume|白色荷叶领长袖衬衣；暗红收腰马甲和黑色中长裙；小尖牙与暗色耳坠；黑色鞋
歌剧披风吸血鬼装|opera-cape vampire costume|黑色长披风内里深紫；黑色长袖礼服和不透明长裙；银色扣饰与尖牙妆；黑色低跟鞋
冬夜长衣吸血鬼装|winter-coat vampire costume|深灰毛领长外套；暗红高领针织衫和黑色长裤；皮手套与小尖牙；黑色保暖靴
未来都市吸血鬼装|future-city vampire costume|黑色高领短夹克；暗红几何拼片与黑色长裤；原创细线发饰和小尖牙；黑色机能靴
''',['吸血鬼','vampire','夜行者'],['gothic'])

outfits('outlaw_costumes','囚服与架空匪徒装扮','''
橙色连体囚服装扮|orange prison-jumpsuit costume|橙色长袖拉链连体衣；内穿白色圆领T恤；无字号码牌布片；黑色便鞋；影视囚犯装扮
条纹上下囚服装扮|striped prison-separates costume|黑白横条长袖上衣与长裤；同材质软帽；灰色圆领内搭；黑色帆布鞋；舞台囚犯装扮
灰色两件囚服装扮|grey prison-separates costume|浅灰立领短上衣与直筒长裤；白色圆领内搭；无字胸前布片；灰色便鞋；架空囚服
蓝色工装囚服装扮|blue workwear-prison costume|褪蓝长袖工装衬衣与长裤；灰色内搭；无标记胸袋；深蓝平底鞋；架空影视囚服
冬季囚服外套装扮|winter prison-jacket costume|灰色棉服短外套叠灰色连体衣；普通针织帽；无字号码布片；黑色厚底便鞋
未来设施囚服装扮|future-facility inmate costume|灰白长袖连体衣；橙色肩侧拼条与无字胸片；软质宽腰带；白色便鞋；原创科幻装扮
荒野斗篷匪徒装|wasteland-bandit cloak costume|沙棕破边短斗篷叠灰色长袖衣；褐色工装长裤；围巾放低露出脸；棕色靴
皮马甲山匪装扮|leather-waistcoat bandit costume|深棕皮马甲与灰色交领长袖衣；黑色直腿长裤；布腰带和旧布帽；棕色布靴；古风幻想
绿兜帽盗贼装扮|green-hood rogue costume|墨绿开放面兜帽短披风；褐色长袖衣和长裤；腰侧小布袋；棕色软靴；原创奇幻盗贼
都市黑西装匪徒装|city-black-suit outlaw costume|黑色宽肩西装和深灰衬衣；黑色直筒长裤；细银领夹与手套；黑色皮鞋；架空反派角色
长皮衣都市反派装|long-leather city-villain costume|黑色长皮外套；暗红圆领上衣与深灰长裤；腰侧小包；黑色短靴；服装造型参考
围巾飞行夹克匪徒装|scarf-bomber outlaw costume|褐色飞行夹克；灰色内搭与深棕长裤；长围巾与短檐帽；棕色工作靴；架空装扮
蒸汽飞艇海盗装|steampunk-airship pirate costume|棕色长马甲与奶白衬衣；黑色长裤；护目镜固定帽顶与腰侧工具袋；棕色长靴
红腰巾海盗装扮|red-sash pirate costume|米白宽袖衬衣叠深蓝长外套；黑色长裤与红腰巾；三角帽和小耳环；黑色长靴
沙漠拾荒匪徒装|desert-scavenger outlaw costume|沙色开放面头巾与短外衣；灰褐长袖内搭和宽长裤；布腰封与背包；绑带短靴
赛博都市盗贼装|cyber-city rogue costume|黑色高领机能夹克与长裤；蓝紫原创几何拼片；面罩挂在领侧并露出全脸；黑色运动靴
''',['囚犯','监狱囚犯','匪徒','盗贼','outlaw','prison costume'])

outfits('tactical_outfits','特种部队与特勤服装外观','''
城市黑色特勤装|urban-black special-operations outfit|黑色长袖战术上衣和工装长裤；黑色无标记背心；开放面头盔；黑色战术靴
沙漠浅色特勤装|desert-tone special-operations outfit|沙色长袖上衣与长裤；褐色载具背心和腰侧袋；无标记软帽；沙色靴
林地迷彩特勤装|woodland special-operations outfit|原创绿褐迷彩长袖上衣与长裤；深绿背心；无标记头盔；深绿靴
雪地外罩特勤装|snow-overlayer special-operations outfit|白灰宽松外罩上衣和长裤；浅灰背心；白色开放面兜帽；灰白保暖靴
雨天硬壳特勤装|rain-shell special-operations outfit|深灰带兜帽防雨硬壳外套；黑色工装裤；轻量背心与防水小袋；黑色雨战术靴
冬季保暖特勤装|winter-insulated special-operations outfit|深绿保暖短外套；灰色长袖内搭与厚工装裤；针织帽和完整手套；黑色保暖靴
轻装侦察特勤装|light-reconnaissance costume|灰绿薄长袖衬衣；深灰工装长裤与轻量腰带袋；软檐帽；棕色徒步靴；无武器服装展示
重型护具特勤装|heavy-protective tactical costume|深灰长袖制服与长裤；较大体积的胸背护具；护肘护膝和开放面头盔；黑色靴
长途背包特勤装|rucksack tactical costume|棕绿长袖上衣与长裤；深绿短背心和背包；无标记头盔；棕色靴；背包肩带连接可见
海岸防风特勤装|coastal-wind tactical costume|灰蓝防风夹克；深蓝长裤；低体积灰色背心；开放面软帽与手套；黑色防滑靴
飞行连体特勤装|flight-coverall tactical costume|灰绿色长袖飞行连体衣；胸前拉链袋与黑色轻背心；耳机放在颈侧；黑色飞行靴
救援特勤外观装|rescue-unit tactical costume|橙灰长袖外套与灰色长裤；无字反光带和简洁背心；开放面安全盔；黑色工作靴
科幻白灰特勤装|white-grey sci-fi tactical costume|白灰不透明长袖制服与长裤；分片式原创胸肩护具；开放面头盔；灰白短靴
低可视便装特勤装|low-profile civilian tactical costume|灰色软壳外套与黑色圆领衫；深灰工装长裤；腰侧小袋与简洁手套；黑色运动靴
连帽侦察披覆特勤装|hooded-recon overlayer costume|褐绿短兜帽披覆面部敞开；灰色长袖衣和长裤；无标记背心与背包；棕色短靴
训练场特勤服装|training-ground tactical outfit|灰色长袖训练衫；黑色工装长裤与薄背心；护膝和普通布帽；黑色训练靴；无武器站姿
''',['特种部队','特种兵','特勤','战术装扮','special forces','tactical'],['techwear'])

outfits('intimate_costumes','情趣主题成衣与配饰组合','''
缎面胸衣情趣套装|satin-corset intimate-apparel set|黑色不透明缎面有肩带胸衣；高腰不透明平口内裤；吊袜带接黑色长袜；小领结与低跟鞋；中性灰成年尺码人台
蕾丝衬底胸衣情趣套装|lined-lace corset apparel set|酒红不透明胸衣外覆黑蕾丝；同色高腰平口内裤；黑色长袜；窄颈带与低跟鞋；中性灰成年尺码人台
高领连体情趣装|high-neck bodysuit intimate-apparel set|黑色高领长袖不透明连体衣；腰部布质拼片；不透明连裤袜；小手套与低跟鞋；中性灰成年尺码人台
短披肩连体情趣装|capelet-bodysuit intimate-apparel set|深紫不透明宽肩带连体衣；同色短披肩；黑色长袜与手套；小扣饰和低跟鞋；中性灰成年尺码人台
蕾丝罩裙情趣套装|lined-lace overdress apparel set|黑色不透明吊带衬裙；外层长袖蕾丝中长罩裙；可见分层衣缘；黑色低跟鞋；中性灰成年尺码人台
缎面晨袍情趣套装|satin-robe intimate-apparel set|酒红短袖缎面晨袍敞开；内穿不透明及膝吊带衬裙；缎面腰带垂在两侧；同色便鞋；中性灰成年尺码人台
蝴蝶结胸衣情趣套装|bow-corset intimate-apparel set|奶油白不透明宽肩带胸衣；同色高腰平口内裤与小罩裙；肩带小蝴蝶结；白色长袜与低跟鞋；中性灰成年尺码人台
燕尾短外套情趣装|tail-jacket intimate-apparel set|黑色短燕尾外套；白色不透明高领连体衣；黑色不透明连裤袜；小领结与低跟鞋；中性灰成年尺码人台
女仆围裙情趣装|apron-themed intimate-apparel set|黑色不透明有肩带连体衣；白色短围裙覆盖正面；黑色不透明连裤袜；白色发箍与平底鞋；中性灰成年尺码人台
猫耳主题情趣装|cat-ear themed intimate-apparel set|黑色高领不透明短袖连体衣；高腰小罩裙与不透明连裤袜；可见猫耳发箍；小手套和低跟鞋；中性灰成年尺码人台
兔耳主题情趣装|rabbit-ear themed intimate-apparel set|酒红不透明宽肩带连体衣；黑色不透明连裤袜；兔耳发箍与独立白领结；白腕饰和低跟鞋；中性灰成年尺码人台
礼帽马甲情趣装|top-hat waistcoat apparel set|黑色短马甲叠白色不透明连体衣；黑色不透明连裤袜；小礼帽和短手套；黑色低跟鞋；中性灰成年尺码人台
侧系带胸衣情趣套装|side-laced corset apparel set|黑色不透明有肩带胸衣侧面穿绳闭合；深紫高腰平口内裤；黑色长袜；银色小扣与低跟鞋；中性灰成年尺码人台
长手套胸衣情趣套装|opera-glove corset apparel set|深蓝不透明有肩带胸衣；同色高腰平口内裤与不透明连裤袜；长手套到上臂；小领结与低跟鞋；中性灰成年尺码人台
腰饰衬裙情趣套装|waist-accent slip apparel set|黑色不透明及膝吊带衬裙；腰部独立缎带小结；短蕾丝手套与长袜；黑色低跟鞋；中性灰成年尺码人台
网纱叠层情趣套装|mesh-overlayer intimate-apparel set|深灰不透明高领无袖连体衣；外罩黑色细网纱长袖短衫；不透明连裤袜；小腕饰与低跟鞋；中性灰成年尺码人台
''',['情趣','情趣装扮','成人主题服饰','intimate apparel'])

outfits('wet_outfits','湿水半透外层与可见内搭','''
湿水白衬衣深色内衣搭配|wet-white-shirt opaque-bra outfit|成年女性穿湿水白色长袖衬衣；胸肩半透区域可见深蓝不透明高覆盖文胸衣缘；黑色长裤；黑色平底鞋；普通站姿
湿水白T恤内衣搭配|wet-white-tee opaque-bra outfit|成年女性穿湿润白色圆领T恤；半透处可见黑色不透明高覆盖运动文胸；蓝色牛仔长裤；白色运动鞋
湿水浅蓝衬衣内搭|wet-pale-blue shirt layered outfit|成年女性穿半湿浅蓝长袖衬衣；湿水深色边界和内层白色不透明背心可辨；灰色长裤；白色便鞋
湿水米白衬衣短裤搭配|wet-ivory-shirt shorts outfit|成年女性穿湿水米白宽衬衣；半透处可见深灰不透明运动文胸；海军蓝及膝短裤；深蓝便鞋
湿水薄棉连裙内衬搭配|wet-cotton dress lined outfit|成年女性穿湿润浅灰短袖及膝棉连裙；局部半透可见独立浅色不透明内衬裙衣缘；灰色平底鞋
雨湿针织上衣内搭|rain-damp knit top layered outfit|成年女性穿浅米薄针织长袖上衣；湿处颜色加深并略透出深灰不透明吊带背心；黑色宽长裤；黑色短靴
湿水宽领T恤内搭|wet-wide-neck tee layered outfit|成年女性穿浅灰宽圆领短袖T恤；湿水半透区域可见黑色高覆盖运动内衣；深蓝长裤；白色运动鞋
湿水开衫背心搭配|wet-cardigan camisole outfit|成年女性穿半湿白色薄开衫；内穿深蓝不透明背心；胸肩湿处透出背心肩带与衣缘；灰色长裙和深灰便鞋
湿水白背心运动内衣搭配|wet-white-tank sports-bra outfit|成年女性穿湿水白色宽肩带运动背心；半透区域可见深灰不透明高覆盖运动内衣；黑色运动长裤；灰色跑鞋
湿水亚麻衬衣内搭|wet-linen shirt layered outfit|成年女性穿米白亚麻长袖衬衣；湿水斑块透出棕灰不透明高覆盖文胸衣缘；褐色宽长裤；棕色平底鞋
湿水薄外套连体泳装搭配|wet-cover-shirt swimsuit outfit|成年女性穿湿水浅蓝宽松薄衬衣；内层海军蓝不透明高领连体泳装可辨；外加灰色及膝短裤；防水便鞋
湿水长款衬衣内衬搭配|wet-long-shirt underlayer outfit|成年女性穿湿水白色及大腿长衬衣；半透处显出灰色不透明长背心的完整衣缘；黑色直筒长裤；黑色便鞋
雨湿肩背衬衣内衣搭配|rain-wet shoulder-back shirt outfit|成年女性四分之三背面站姿；白衬衣肩背湿润处可见深灰不透明文胸肩带与后背带；深蓝长裤；白色鞋
半干半湿衬衣内搭|partly-dried shirt layered outfit|成年女性穿白色长袖衬衣；一侧肩胸仍湿润半透、另一侧干燥更白；内穿深蓝不透明高覆盖文胸；灰色长裤与平底鞋
湿水袖口衬衣内搭|wet-cuff shirt layered outfit|成年女性穿浅灰长袖衬衣；袖口与下摆明显水渍、胸前轻微半透可见不透明白背心；黑色长裤；黑色低帮鞋
湿水叠穿双层T恤|wet-double-layer tee outfit|成年女性穿半湿白色短袖T恤；灰色不透明高领背心在湿处透出独立领肩衣缘；深灰运动长裤；白色跑鞋
''',['湿水','湿透衣服','湿衣','半透','可见内衣','wet clothing','damp fabric'])

outfits('special_costumes','异境职业与巡游特殊装扮','''
鸟嘴面具长袍巡游装|beaked-mask parade costume|黑色高领长袍与黑色长裤；原创鸟嘴面具手持身侧露出面孔；宽檐帽和肩披；黑色靴
旧式潜水员巡游装|vintage-diver parade costume|黄褐厚布长袖连体装；圆形铜色头盔手持身侧；胸口软管为封闭装饰连接；棕色厚靴
荒原防尘旅人装|wasteland-dust traveller costume|沙灰长袖长外套与宽长裤；开放面兜帽和灰色内搭；小型背包；棕色短靴
废土修理师巡游装|wasteland-mechanic parade costume|灰褐长袖工装连体衣；补丁膝片与短皮围裙；护目镜置于额上；深棕工作靴
复古侦探雨夜装|retro-detective rainy-night costume|深灰长风衣与米白衬衣；黑色长裤与领带；宽檐帽和折叠伞垂在身侧；黑色皮鞋
星空占星师巡游装|star-map astrologer parade costume|深蓝高领长袖长袍；原创星点刺绣与短披肩；软圆帽和腰侧布袋；深蓝低跟鞋
沙漏时间旅人装|hourglass time-traveller costume|棕灰长外套与高领内搭；深棕长裤；小型原创沙漏形胸针固定于衣领；棕色短靴
面具修复师巡游装|mask-restorer parade costume|墨绿长袖上衣配黑色直筒长裤；米色长围裙；两枚小面具道具挂在围裙侧袋；黑色工作鞋
纸偶剧团舞台装|paper-puppet theatre costume|奶白高领长袖连裙；肩裙外覆折纸形布质硬片；原创圆帽；黑白平底鞋；身体为正常人类
机械发条人偶舞台装|clockwork-doll stage costume|铜棕不透明长袖收腰上衣和长裙；小型发条形道具通过背带固定；小礼帽；棕色系带靴
稻草人巡游套装|scarecrow-parade outfit|棕色长袖格纹衬衣与宽长裤；缝接草色布条露在袖口裤口；软草帽；棕色布鞋
冰雪巡礼使者装|frost-pilgrim messenger costume|冰蓝长袖及踝外袍；奶白内层和短肩披；半透明冰晶形胸针为装饰件；白色靴
深海信使巡游装|deep-sea messenger costume|深蓝高领长袖外套和长裤；青色鳍形肩片缝接衣服；小型圆贝形侧袋；深蓝短靴
荧光矿工幻想装|glow-miner fantasy costume|灰绿长袖工装与长裤；原创小灯固定安全帽；青色假晶石装在腰袋；黑色工作靴
面纱魔术师舞台装|veiled-magician stage costume|黑色高领长袖西装与长裤；紫色短披风；薄面纱固定小帽但脸部清楚；黑色低跟鞋
邮差精灵巡游装|courier-sprite parade costume|棕绿短外套与长袖内搭；灰色宽腿长裤；肩背邮袋和小帽；棕色短靴；小布翼接背带而非身体
''',['特殊服装','奇异装扮','主题巡游','special costume'])

def hair(dimension,text,aliases=()):
    lines=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(lines)==16,(dimension,len(lines))
    for name,en,feature in lines:
        add('hair_states',dimension,f'{name}|{en}|{feature}。')
        item_aliases=[]
        if '睡醒' in name or '枕压' in name:item_aliases+=['刚睡醒','睡乱']
        if '油' in name:item_aliases+=['发油','油润头发']
        if '湿' in name:item_aliases+=['湿发','湿透头发']
        if '干枯' in name or '干燥' in name:item_aliases+=['干枯头发']
        if '烫' in name:item_aliases+=['烫发']
        if '风' in name or '飘' in name:item_aliases+=['风吹','飘动']
        if '白发' in name or '银灰' in name or '盐胡椒' in name:item_aliases+=['白发']
        if '落发' in name or '掉发' in name:item_aliases+=['掉发']
        if '失养' in name or '深浅分段' in name:item_aliases+=['营养不足','缺营养','头发变色']
        CATALOG[-1].update(added_in='20.0',hair_state_reference=True,age_context='成年女性头发状态参考',
            aliases=['头发形态','头发状态',dimension,*item_aliases],reference_ids=['R01','R02','R79','R80'],
            note='描述可见发束、分区、反光与密度，用于角色作画；颜色、发量或稀疏不能单独说明营养状况或具体病因。')

hair('睡醒蓬乱与生活简易打理','''
睡醒顶发翘起|waking crown cowlicks|棕色中短发头顶两三束向不同方向翘起，发根仍连贯，侧发自然压扁
睡醒单侧压扁|one-side flattened bedhead|棕色齐肩发一侧被枕压得平贴，另一侧较蓬，刘海留轻微折线
睡醒刘海分叉|separated bedhead fringe|深棕刘海形成三四束不规则分叉，额头间隙可见，后发基本自然
睡醒后脑乱蓬|tousled back-of-head bedhead|四分之三后侧头部，后脑短发向外散开成小束，颈部发尾略压平
枕压波折长发|pillow-kinked long hair|棕色长发中段出现不规则浅折弯，发根较平，发尾仍垂至胸前
蓬头散发生活态|everyday loose tousled hair|深棕中长发整体蓬松，碎发和打散的发束有疏密变化，面孔清楚
手梳后残留乱发|finger-combed casual hair|棕色齐肩发被手顺过后大束较齐，头顶与耳边仍有少量飞散短发
睡醒随手低扎|quick low bedhead ponytail|棕色中长发在后颈用普通发圈松扎，头顶不完全平顺，两侧碎发保留
随手高团子打理|quick loose topknot|深棕长发随手卷成高处松团，普通发圈固定，一两束发尾从团边露出
随手半扎夹起|quick half-up clipped hair|棕色上半发在后脑用普通小夹固定，下半发自由垂落，头顶保留轻微蓬松
耳后别发简易打理|quick ear-tucked hair|棕色齐肩发一侧别到耳后，另一侧自然落在脸侧，发根走向和耳后束发可辨
临时抓夹盘起|quick claw-clip twist|四分之三后视棕色长发扭起，普通抓夹固定在后脑，发尾在夹上方散开
随手松辫生活态|quick loose everyday braid|棕色长发编成宽松低三股辫，辫结松紧不完全相同，鬓角留少量碎发
低丸子外散发尾|low bun with loose ends|深棕发在后颈挽成松丸子，普通发圈固定，发尾从一侧扇形散出
出门前压平刘海|lightly smoothed everyday fringe|棕色短发刘海被顺成整片但末端略有零碎，头顶仍有少量翘发，脸侧清楚
橡皮筋松脱后散发|released elastic-mark hair|棕色长发已解开发圈，后脑中段保留一道浅束痕，发尾向两侧自然展开
''',['刚睡醒','睡醒','蓬头','生活简易打理'])

hair('湿透油润与干燥发质外观','''
全头湿透贴发|fully soaked clumped hair|深棕齐肩发完全湿润，发色变深且成连续细束，头顶贴近头皮，发梢有两三滴小水珠
湿透长发成束|soaked long hair in strands|深棕长发湿成较重的竖直束，前侧贴颈，胸前发尾收拢并带少量水滴
湿刘海贴额|wet fringe on forehead|深棕刘海湿成数束贴在额头上，束间有小间隙，其余短发略湿
洗后半干蓬发|partly air-dried washed hair|棕色齐肩发根已较干而发尾仍深湿，分界自然，局部发束重新松开
湿卷发凝束|wet curls clumped together|深棕卷发湿后聚成清楚的卷束，卷径仍可辨，表面反光集中在弯折处
浴后擦干毛躁|towel-dried fuzzy hair|棕色齐肩发擦干后大束松开，表层有细碎毛躁，衣领干燥且穿普通高领上衣
汗湿鬓角发束|sweat-damp temple strands|深棕短发只有鬓角和额前几束变深贴肤，头顶其余发较干，面孔平静
发根油润贴合|oily flattened hair roots|深棕齐肩发根分束贴合头皮，顶部反光窄而集中，发尾仍较松
隔日刘海油束|second-day oily fringe|深棕刘海聚成几束窄小油润束，束间露额，后发基本正常，不添加水滴
护发油顺亮发尾|hair-oil glossy ends|棕色长发根部自然，发尾更整齐并有连续窄高光，整体松量仍在，不做湿水滴
发蜡塑形短束|wax-shaped short locks|深棕短发顶部分成清楚的塑形尖束，根部自然支撑，发蜡形成局部低亮光
发胶后梳定型|gelled slick-back hair|深棕短中发向后梳贴，连续梳理纹从额上延至后脑，窄高光与干净发际线可辨
干枯哑光发束|dry matte hair lengths|棕色中长发缺少连续亮带，发束表面偏粗糙且色调略浅，毛流仍自然
干燥毛躁外轮廓|dry frizzy hair silhouette|棕色齐肩发外缘有一层细碎飞发，内部大束仍可辨，不画成烟雾或棉花
分叉发尾可见|visible split hair ends|棕色长发尾端有数束细小分叉，旁边同格小放大框显示一根分成两叉，保留完整头发定位
静电竖起细发|static-lifted flyaway hairs|棕色中发头顶与两侧少量细发离开主发束竖起，弧线细而分散，主要发体仍垂落
''',['湿发','湿透','发油','油头','干枯','毛躁'])

hair('烫卷定型与风中运动','''
新烫规则卷束|fresh regular permed curls|棕色及肩发呈均匀中卷，发根自然衔接，卷束一圈圈有前后遮挡，非卷发棒道具
蓬松大波浪烫发|voluminous large-wave perm|棕色长发从耳下形成宽大的S形波浪，顶部自然蓬起，胸前两侧波峰可辨
细密小卷烫发状态|fine tightly permed curls|深棕中发为细密小螺旋卷，整体体积大，单个发束仍清楚，保持自然头部比例
发根蓬松烫状态|root-lift perm state|棕色中短发主要在根部抬高，发中与发尾较直，头顶轮廓比耳侧更蓬松
发尾内扣定型|styled inward-curved ends|棕色齐肩发尾整齐向内弯，根部和中段较直，内扣弧线朝颈部收回
发尾外翻定型|styled outward-flipped ends|棕色齐肩发末端同时向外翘，头部两侧形成清楚翻边，根部自然
卷度松散后的发束|relaxed formerly-curled lengths|棕色长发上段较直，下段卷度变松且不完全均匀，仍能读出几段宽波浪
辫子解开压波纹|braid-release crimped hair|棕色中长发解辫后呈细密均匀折波，发根较顺，波纹不同于圆螺旋卷
微风吹动脸侧发|light breeze moving face-framing locks|棕色中长发主体垂落，脸侧与刘海少量细束向画面右侧弯动，面部清楚
侧风吹开长发|side-wind spread long hair|棕色长发从发根连续向画面右侧飘开，束间拉开间隙，头与全部发梢都在格内
迎风后扬发束|headwind swept-back hair|棕色中长发从额前和脸侧向后抬起，四分之三侧视可见发根支点，面孔不被遮住
背风前拢发束|tailwind forward-drifting hair|棕色长发从后脑向两肩前方漂动，两侧束尾前拢但不遮面，发根连续
转身散开长发|turning-motion fanned hair|棕色长发在肩后展开弧扇形，发束随转头方向有前后层次，头部轻侧转而非夸张甩头
轻跳上浮发尾|light-bounce lifted hair ends|棕色齐肩发根跟随头部，发尾稍向上外飘成圆弧，细小惯性束分明
低马尾风中飘动|low ponytail in wind|棕色长发在后颈由发圈固定，马尾从固定点向画面右侧弯起，全部发尾可见
水中缓慢漂发|slow underwater floating hair study|成年女性普通高领上衣的头肩研究，深棕长发在浅蓝色水中向两侧松散漂浮，发束不重力下垂，面孔清楚
''',['烫发','风吹','散开','飘动','头发动态'])

hair('白发稀疏与颜色变化外观','''
零星白发混入|scattered greys among dark hair|深棕齐肩发中有少量细白发随机混入，保留大部分深色发体和清楚毛流
鬓角集中白发|temple-concentrated grey hair|深棕中发两侧鬓角白发较多，头顶和后发仍深色，分区过渡柔和
头顶盐胡椒灰发|salt-and-pepper crown hair|成年女性短发头顶灰白与深灰细发相间，后侧稍深，整体为混合发色而非条纹染发
前额一束白发|single white forelock|深棕齐肩发额前一束自然白发从根到梢连续，其余发束保持深色
大面积银灰发状态|mostly silver-grey hair|成年女性中长发主要为银灰，少量深灰发夹杂，根部与发尾颜色连续自然
自然白发低扎|natural white low-tied hair|成年女性完整白发低扎在后颈，发根与发尾均为白色，少量细发散在耳侧
发缝加宽稀疏感|widened parting appearance|成年女性深棕中发顶部斜前俯视，中央发缝可见宽度增加，两侧仍保留头发，头皮完整
头顶弥散稀疏感|diffuse crown thinning appearance|成年女性深棕短中发顶部整体密度较低，发束间有完整自然肤色头皮，非剃发或创口
两鬓发量减少|reduced temple density|成年女性棕色中发两侧发际较疏，细软短发混入，后脑发量较完整
细软低体积头发|fine low-volume hair|棕色齐肩发单束细软，贴近头部且总体体积较小，发际线与毛流完整
发梳少量落发可见|loose shed hairs on brush|成年女性深棕齐肩发自然垂落，身侧手持普通梳子，梳齿上有少量分离细发，保留完整头部与手腕
肩头零散掉发可见|loose shed hairs on shoulder|成年女性棕色中长发自然垂落，深色衣肩上有数根独立浅棕落发，主发与落发清楚分开
深发局部褪浅外观|locally lightened dark hair|深棕长发中段局部变成偏浅棕，过渡不规则且表面哑光，作为失养或受损等故事外观灵感，不标为诊断
失养感干淡发束|dry pale hair storytelling reference|棕色中长发颜色偏浅且干哑，部分细束更淡、密度稍低，作为营养不足题材的创作参考，外观本身不确定病因
深浅分段发色外观|alternating pale-dark hair segments|成年女性深棕中长发有横向浅棕分段而非挑染，局部小放大框显示同一束的深浅区，创作参照不作病因判断
短新生发与长发并存|short regrowth among longer hair|成年女性棕色中长发际线与分缝附近有细软短新生发，后侧长发正常，短束从头皮自然长出
''',['白发','掉发','稀疏','营养不足','缺营养','头发变色'])

assert sum(bool(e.get('special_expansion')) for e in CATALOG)==128
assert sum(bool(e.get('hair_state_reference')) for e in CATALOG)==64
