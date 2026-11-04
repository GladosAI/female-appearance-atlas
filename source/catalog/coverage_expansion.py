"""Edition 5: concrete additions requested by the atlas user."""
from catalog_content import CATALOG, category, add

def block(key, dimension, text, styles=(), aliases=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['styles']=list(styles);e['aliases']=list(aliases)

category('chinese_outfits','中国古代与国风服装','朝代参考与架空国风分开记录；图例为原创改编，形制与穿法沿博物馆资料核对。',['R27','R28','R29'])
category('opera_outfits','中国戏曲行头','按戏衣、行当与舞台用途组织；行头具有舞台程式，不等同于对应朝代的日常服装。',['R30'])
category('swimwear','泳装与海滩服装','按连体、分体、袖长、裤裙和水上活动分列，图例展示具体剪裁与连接方式。',['R06'])
category('special_costumes','女仆与兽耳主题装扮','记录整套服装和头饰、耳饰、围裙的组合；兽耳发箍与幻想器官分开理解。',[])
category('underwear','内衣与贴身内搭','以服装物件和裁缝人台比较杯型、肩带、覆盖范围、接缝与内搭长度。',['R05','R06'])
category('space_suits','宇航服与科幻密封服','舱内压力服、舱外服与原创科幻服分列；观察密封连接、关节与背包装置。',['R31'])
category('masks','面具与面部装扮','按覆盖区域、材料、眼孔和固定方式组织；戏剧主题面具是原创装扮。',[])
category('eyewear','眼镜与镜片类型','框形、镜片、鼻梁、镜腿与附加结构分别观察；矫正眼镜、太阳镜和装备镜分列。',[])
category('eyes','虹膜与瞳孔','虹膜是有颜色的部分，瞳孔是中央开口；自然观察与幻想形态分别标注。',['R32'])

block('traditional','中国传统服装形制','''
交领齐腰襦裙汉服|cross-collar waist-tied ruqun|交叠衣领、腰部系裙与长褶裙组合，系带收束点可见。
对襟齐腰襦裙汉服|front-opening waist-tied ruqun|上襦前襟左右对开，下接独立腰系长裙，内层衣片完整。
齐胸裙半臂汉服|high-tied skirt with banbi|短袖半臂罩在衫外，长裙高系，胸前系带与层次清楚。
坦领襦裙披帛装|open-neck ruqun with pibo|平缓开领上襦配高腰裙，披帛绕过肩臂，衣身不透明。
交领短袄汉服套装|cross-collar ao and skirt|有夹层厚度的短袄交叠系结，下配有独立腰头的长裙。
立领对襟袄裙汉服|standing-collar front-opening aoqun|上袄竖领与前扣明显，下裙腰线独立，领缘和袖缘对照。
方领袄裙汉服|square-neck aoqun|方形领缘配完整内层，短袄下摆盖住裙腰，袖身宽松。
长褙子襦裙汉服|long beizi with ruqun|直领对襟长外衣不在腰部紧束，内襦和长裙从前开口可见。
短褙子汉服搭配|short beizi coordinate|直领短外衣罩在内衫外，衣长与长裙形成明显比例差。
比甲袄裙汉服|bijia vest with aoqun|无袖长比甲罩住有袖上衣，前开襟露出裙装内层。
大袖衫长裙汉服|wide-sleeve shan and skirt|宽袖外衫形成大幅垂布，下裙腰线和完整内搭可辨。
马面裙短衫汉服|mamian skirt and short top|裙前后平整裙门与两侧褶裥分区，短衫让腰系结构可见。
百褶长裙汉服|pleated long-skirt hanfu|长裙整体密褶，腰头系带收拢，上衫素净以突出褶纹。
间色长裙汉服|striped-panel skirt hanfu|长裙按纵向拼片形成交替色带，上襦与裙体分开。
曲裾深衣改编|quju wrap-robe adaptation|交领长衣的下部衣片绕体，斜向裾线和腰带清楚，参考汉代改编。
直裾长衣改编|straight-hem wrap-robe adaptation|交领长衣以较直下缘收尾，腰带束合，轮廓与曲裾区分。
''',['chinese'],['汉服','中国传统服饰','中式服装'])

block('chinese_outfits','中国古代与近代改编','''
汉代曲裾窄袍改编|Han-inspired narrow quju robe|窄长衣身和绕体衣片配细腰带，裙底略展；依据博物馆复原参考改编。
魏晋绞缬襦裙改编|Wei-Jin-inspired tie-dyed ruqun|短襦宽袖、缘饰与曳地长裙，局部绞缬纹样保持独立。
唐风半臂高腰裙装|Tang-inspired banbi ensemble|齐肘半臂罩住内衫，配高腰长裙与轻披帛，衣片层次清楚。
唐风窄袖骑行装|Tang-inspired narrow-sleeve riding outfit|窄袖翻领长袍配小口长裤、腰革带与靴，参考胡汉交流服饰。
唐风圆领女官改编|Tang-inspired round-collar official adaptation|圆领长袍与完整长靴，腰带和前襟保持明确，不使用真实等级章纹。
宋风褙子长裙装|Song-inspired beizi ensemble|细长对襟外衣罩住内衫长裙，袖量和腰部层次克制。
宋风大袖衫改编|Song-inspired broad-sleeve ensemble|宽袖罗衫配褶裙，内层完整，轻薄外料只表现边缘透光。
明风立领袄裙装|Ming-inspired standing-collar aoqun|竖领短袄、系扣与长褶裙，上下衣分离，花纹按领袖分区。
明风方领长袄装|Ming-inspired square-neck long ao|方领长袄盖过裙腰，袖口有缘边，完整衬层从领口可见。
明风比甲叠裙装|Ming-inspired bijia ensemble|长无袖比甲罩住袄裙，前开口让内外长度与材质可比较。
清代氅衣叠穿改编|Qing-inspired changyi layering|侧开裾长外袍罩在完整内袍外，云头边饰与外层长度清楚。
清代旗装长袍改编|Qing-inspired banner robe adaptation|直身长袍、宽滚边和袖缘装饰，整体轮廓与近代收腰旗袍不同。
清风镶滚袄裙装|Qing-inspired bordered aoqun|上衣和长裙分离，襟边、袖边采用多层窄镶滚。
民国长袖旗袍改编|Republican-era long-sleeve qipao|收腰长袍、立领、盘扣与长袖，侧开衩保留活动空间。
民国宽身旗袍改编|Republican-era loose qipao|宽直衣身、短立领与较低侧衩，腰部松量明显。
现代新中式短衫装|modern Chinese-style blouse outfit|斜襟盘扣短衫配简洁长裤，以中式细节构成当代日常装。
''',['chinese'],['中国古代','古装','中国服饰'])

block('chinese_outfits','架空国风与神话','''
国风剑修窄袖装|Chinese-fantasy swordswoman coordinate|交领窄袖衣、长裤和分片外裙，腰带固定剑鞘与小袋；原创架空。
国风符师叠袍装|Chinese-fantasy talisman scholar outfit|直领叠袍、宽腰封与原创符片袋，袖口不遮住手部操作。
国风丹师围裙装|Chinese-fantasy alchemist outfit|交领长衣外加工具围裙，药囊和布护袖固定清楚。
国风巡山护腕装|Chinese-fantasy ranger outfit|短袄、裙裤、布护腕与披肩，方便步行，纹样局部使用。
国风机关师裤装|Chinese-fantasy mechanic outfit|盘扣上衣、宽长裤与小型仪表带，机械部件有明确固定点。
国风书院成人装|Chinese-fantasy adult academy outfit|交领长衣、简洁束带与书册袋，成年学者形象。
国风月宫仙衣|moon-palace fantasy costume|完整襦裙、月弧云肩与披帛，银色纹样沿衣缘排列；神话创作。
国风花神叠裙装|flower-spirit Chinese-fantasy outfit|布衫外叠花瓣形裙片，花簪和腰结呼应，内裙完整。
国风龙纹战裙装|dragon-motif Chinese-fantasy battle outfit|窄袖衣与护甲分片，原创龙纹沿边缘排列，肘膝活动可见。
国风凤羽礼裙装|phoenix-feather fantasy ceremonial outfit|长袄、长裙与羽形肩饰，饰件固定在外衣，不使用真实品级纹样。
国风飞天舞衣改编|feitian-inspired fantasy dance costume|完整高腰衣裙、绕臂披帛与轻飘外裙，采用原创壁画灵感。
国风鲛人纹裙装|merfolk Chinese-fantasy costume|交领衣与完整长裙，鳞形纹样、贝形饰件和透明外披组合。
国风雪域披袍装|snow-travel Chinese-fantasy robe|厚外袍、布护腿与系带披风，寒冷场景的层次与固定点明确。
国风茶馆掌柜装|Chinese-fantasy teahouse keeper outfit|斜襟短衣、长裙与账册袋，素布和局部盘扣形成日常剪影。
国风赤纹祭礼装|red-motif fantasy ritual attire|长衣和对称云肩采用原创几何纹，不作为真实宗教服饰复原。
国风中式洛丽塔混搭|Chinese-inspired Lolita coordinate|立领布衫、盘扣和有裙撑的膝下蓬裙组合，成年时尚改编。
''',['chinese'],['国风','仙侠','中式幻想'])
CATALOG[-1]['styles'].append('lolita')

block('opera_outfits','旦角戏衣与舞台改编','''
女蟒戏曲礼装|female-role mang stage robe|长绣袍、宽袖与舞台装饰腰带，蟒纹采用原创图案；戏曲行头灵感。
女帔戏曲绣袍|female-role pei stage robe|对襟绣袍罩住内衣裙，衣缘和长袖装饰形成舞台辨识。
女靠戏曲武装|female-role kao stage armor|绣布靠衣、胸腹装饰与腿部垂片，表现舞台靠衣而非实战甲胄。
靠旗刀马旦装|flag-bearing daomadan stage outfit|靠衣背部插舞台靠旗，头饰、旗杆与肩背固定点清楚。
短靠武旦装|short kao wudan stage outfit|较短舞台靠衣配长裤和靴，关节与武打活动范围清楚。
青衣素褶子装|qingyi plain xuezi stage costume|素色长褶子配裙，白水袖从本袖袖口延长，领袖缘对照。
花旦花褶子装|huadan floral xuezi costume|花纹褶子、较利落衣长与长裤，布料和彩绣分区明确。
宫装旦角礼装|dan-role court stage costume|装饰性宫装以长裙、肩片与层叠垂带形成舞台轮廓。
裙袄花旦装|huadan ao-and-skirt stage outfit|短袄与褶裙分别穿着，绣缘和腰系位置清楚。
戏曲旗装改编|Chinese-opera banner-costume adaptation|旗装式直身长袍与夸张舞台头饰，装饰密度按远观设计。
古装旦角叠裙|dan-role historical stage layers|长裙、衣襟与肩饰多层叠合，作为戏曲古装视觉灵感。
旦角斗篷装|dan-role stage cloak|完整戏衣外加长斗篷，颈部系结明确，袖手与裙摆露出。
水袖练功裙装|water-sleeve rehearsal outfit|简洁有袖上衣和长裙配白色延长袖，便于观察水袖动作。
戏曲云肩裙装|opera cloud-collar outfit|四向云肩盖在裙袄肩部，绣缘和肩颈连接可见。
昆曲闺门旦改编|Kunqu guimendan-inspired coordinate|绣帔与长裙、柔和水袖组成文戏舞台装，原创改编。
越剧改良古装灵感|Yue-opera adapted historical costume|收束衣身与层叠长裙形成舞台线条，区别于古代日常穿法。
''',['chinese'],['戏曲','京剧','旦角','行头','中国传统'])

block('swimwear','连体泳装细分','''
高领连体泳装|high-neck one-piece swimsuit|前领覆盖较高，腰臀由连续泳布包覆，腿口与背带清楚。
细肩带连体泳装|thin-strap one-piece swimsuit|两条细带连接完整连体衣身，侧缝和腰部贴合可见。
宽肩带连体泳装|wide-strap one-piece swimsuit|宽带从前身延伸到背部，领缘与腿口使用连续包边。
交叉背带连体泳装|cross-back one-piece swimsuit|肩带在背面交叉，三分之二后视展示交叉点与连接端。
工字背连体泳装|racerback one-piece swimsuit|后背两带向中央汇合，肩胛区域开口与背片可见。
挂脖连体泳装|halter one-piece swimsuit|颈带承托完整连体衣身，背面开口边缘明确。
单肩连体泳装|one-shoulder one-piece swimsuit|衣身上缘斜向跨过一肩，另一侧无肩带。
抹胸连体泳装|strapless one-piece swimsuit|平直无肩带上缘与完整连体衣身，侧部支撑接缝清楚。
前拉链连体泳装|front-zip one-piece swimsuit|短前拉链从高领延至上胸，衣身与拉链包边可辨。
侧拼片连体泳装|side-panel one-piece swimsuit|侧腰用不同色泳布拼片，所有拼片完整覆盖身体。
抽褶连体泳装|ruched one-piece swimsuit|前身有沿侧缝收束的抽褶，腿口与肩带仍保持平整。
荷叶边连体泳装|ruffle-trim one-piece swimsuit|领缘小荷叶与完整连体主体分层，荷叶不充当支撑带。
短袖连体泳装|short-sleeve one-piece swimsuit|贴合短袖接在完整衣身上，领口与腿口清楚。
长袖连体泳装|long-sleeve one-piece swimsuit|手腕长袖和完整连体衣身，领口及袖口有包边。
平角连体泳装|boyleg one-piece swimsuit|衣身连续延伸到上腿，裤口平整，区别于高腿口款。
裙摆连体泳装|swimdress one-piece swimsuit|完整连体泳衣外接短裙摆，三分之四侧视展示内外层。
''',aliases=['泳装','泳衣','连体泳衣'])

block('swimwear','分体与水上穿搭','''
三角杯比基尼泳装|triangle-cup bikini|三角上片与普通覆盖下装分离，泳布不透明，系带端点清楚。
宽带比基尼泳装|wide-band bikini|宽肩带与胸下宽带连接上衣，配中腰泳裤。
抹胸比基尼泳装|bandeau bikini|无肩带横向上衣配普通泳裤，上衣侧部支撑可见。
高腰比基尼泳装|high-waist bikini|上衣与高腰下装分离，下装腰缘覆盖肚脐附近。
运动比基尼泳装|sport bikini|运动式上衣与平整泳裤，带具稳定且少装饰。
裙裤分体泳装|skirted two-piece swimsuit|泳上衣与有内裤结构的短裙裤组合，外裙固定在腰缘。
坦基尼长上衣泳装|tankini swimsuit|长泳上衣到腰下，与独立泳裤组合，侧缝分层可见。
挂脖坦基尼泳装|halter tankini swimsuit|绕颈带连接较长泳上衣，下面为独立平角泳裤。
短裤分体泳装|swim-top and board-shorts outfit|完整泳上衣配及上腿的宽松泳短裤，裤腰单独系结。
短袖防磨泳装套装|short-sleeve rash-guard set|贴合短袖防磨上衣与泳短裤分离，袖长和接缝清楚。
长袖防磨泳装套装|long-sleeve rash-guard set|长袖高领泳上衣配中长泳裤，完整覆盖腰腹。
拉链防晒泳裤装|zip-front rash-guard trouser set|拉链泳上衣与长泳裤组合，领口和袖口边缘清楚。
包覆式长泳装套装|full-coverage swim set|长上衣、长裤与泳用头部覆盖组合，外层长度与裤脚独立。
泳衣薄罩裙组合|swimsuit and cover-up skirt|完整泳衣外加可拆围裹罩裙，系结位于裙腰。
泳衣开襟罩衫组合|swimsuit and open cover-up|完整泳衣外搭轻薄开襟长罩衫，内外层不混为一件。
泳衣沙滩衬衫组合|swimsuit and beach shirt|泳衣外罩宽松有扣衬衫，袖口、门襟与泳衣各自独立。
''',aliases=['泳装','泳衣','分体泳衣'])

block('special_costumes','女仆装扮细分','''
维多利亚长裙女仆装|Victorian-inspired long-skirt maid attire|深色长袖长裙外系白围裙，袖口与帽饰简洁，成年工作造型。
高领长袖女仆装|high-neck long-sleeve maid costume|高领连裙、袖口和长围裙，黑白色块按服装面片组织。
经典膝长女仆装|classic knee-length maid costume|膝长蓬裙、完整布衫、腰围裙与小头饰，成年主题服装。
方领围裙女仆装|square-neck apron maid coordinate|方领连裙有完整胸前布片，肩带围裙在背部系结。
背带围裙女仆装|pinafore-apron maid coordinate|有胸兜的背带围裙罩在袖衫长裙外，肩带和腰结独立。
腰围裙女仆装|waist-apron maid coordinate|只覆盖腰下的围裙配有袖连裙，围裙与裙体长度可比较。
爱德华长裙女仆改编|Edwardian-inspired maid costume|高领布衫、长裙与大胸兜围裙，袖身松量明确。
乡村布裙女仆装|country maid costume|素色布裙、窄缘围裙和软头巾，材质以棉麻表现。
茶室侍奉女仆装|teahouse maid coordinate|布衫与膝下长裙配多袋围裙，工具口袋可见。
酒馆工作女仆装|tavern working-maid costume|卷袖衫、长裙和厚布围裙，腰袋固定在围裙上。
日式和风女仆混搭|Japanese-inspired maid hybrid|交叠领袖衫配完整长裙和围裙，标注原创时尚混搭。
中式盘扣女仆混搭|Chinese-inspired maid hybrid|立领盘扣衫、长裙和围裙形成成年主题装，不作为历史复原。
哥特高领女仆装|gothic high-neck maid costume|高领黑裙、窄白围裙与蕾丝帽饰，裙长到膝下。
洛丽塔围裙女仆混搭|Lolita apron-maid coordinate|有裙撑的膝下蓬裙与布衫外加围裙，成年洛丽塔时尚混搭。
机能工作女仆装|utility maid costume|简洁有袖衣裙配可拆工具围裙，扣带与袋口用途清楚。
科幻服务女仆装|science-fiction service-maid costume|完整未来衣裙、硬边围裙与小设备袋，固定点明确。
''',aliases=['女仆','女仆装','maid'])
for e in CATALOG[-16:]:
    if '哥特' in e['name']:e['styles']=['gothic']
    if '洛丽塔' in e['name']:e['styles']=['lolita']
    if '中式' in e['name']:e['styles']=['chinese']
    if '机能' in e['name']:e['styles']=['techwear']

block('special_costumes','猫耳与兔耳主题装扮','''
猫耳发箍日常装|cat-ear headband casual outfit|三角猫耳固定在可见发箍上，配衬衫与长裤，属于配饰装扮。
猫耳女仆主题装|cat-ear maid costume|成年女仆裙、围裙和猫耳发箍，装饰尾巴固定在腰后。
猫耳连帽街头装|cat-ear hoodie street outfit|帽顶缝两只布三角耳，连帽衫与宽裤形成日常剪影。
猫耳哥特长裙装|cat-ear gothic long-dress outfit|猫耳发箍配高领蕾丝长裙，耳形与头发轮廓分开。
猫耳制服主题装|cat-ear adult uniform costume|成人服务制服、窄围裙和猫耳发箍，不使用真实校徽。
猫耳软帽冬装|cat-ear knit-cap winter outfit|针织帽自带三角耳，外套和长裤完整覆盖，耳根与帽体连接。
猫耳幻想游侠装|cat-ear fantasy ranger outfit|幻想猫耳从头部两侧生长，配完整窄袖衣裤与工具袋。
猫耳舞台裤装|cat-ear stage trouser costume|亮色夹克、长裤与可拆猫耳，尾饰连接腰带，成年舞台装。
兔耳发箍礼裙装|rabbit-ear headband evening dress|长兔耳固定在发箍上，配完整及膝礼裙与鞋。
兔女郎经典礼装|classic adult bunny costume|不透明连体礼衣、黑色连裤袜、领结与袖口，长兔耳与短绒尾为可拆饰件。
兔耳燕尾裤装|rabbit-ear tailcoat trouser outfit|兔耳发箍、燕尾外套、马甲和长裤，成人主持主题装。
兔耳女仆主题装|rabbit-ear maid costume|长兔耳发箍搭配膝下女仆裙与围裙，耳根和系带清楚。
兔耳连帽休闲装|rabbit-ear hood casual outfit|帽顶缝长布耳，软卫衣和长裤组合，耳朵自然垂落。
垂兔耳森系裙装|lop-ear mori costume|垂耳发箍配多层亚麻长裙与开衫，布耳与头发可区分。
兔耳幻想信使装|rabbit-ear fantasy messenger outfit|幻想长兔耳与完整旅行衣裤，信袋固定在腰侧。
兔耳舞台西装裙|rabbit-ear stage blazer-dress costume|成人西装连裙、领结和长兔耳发箍，剪裁与饰件分区清楚。
''',aliases=['特殊装扮','兽耳主题','cosplay'])
for e in CATALOG[-16:]:
    if '哥特' in e['name']:e['styles']=['gothic']
    if '森系' in e['name']:e['styles']=['mori']
    e['aliases'] += ['猫耳装','猫娘'] if '猫' in e['name'] else ['兔耳装','兔娘']

block('underwear','文胸与胸衣细分','''
全罩杯文胸|full-cup bra|杯体包覆较高，肩带、胸下带与侧翼完整；用裁缝人台展示。
四分之三罩杯文胸|three-quarter-cup bra|杯体上缘较全罩杯降低，杯缝和肩带位置清楚。
半罩杯文胸|demi-cup bra|杯缘较低、肩带靠外，展示杯体与下缘支撑结构。
阳台杯文胸|balconette bra|杯缘偏横向，较宽肩带间距和独立杯缝可辨。
三角软杯文胸|triangle soft-cup bra|无模压杯形的三角布片、细肩带与胸下带相连。
无钢圈软杯文胸|wire-free soft-cup bra|柔软杯片与宽底围相接，不画钢圈轨迹。
抹胸式文胸|bandeau bra|横向包覆布带没有肩带，侧缝和下缘弹力带清楚。
可拆肩带文胸|convertible-strap bra|杯体和下围完整，肩带端部可拆钩与连接环明确。
交叉背带文胸|cross-back bra|后视裁缝人台展示两条肩带交叉与后扣位置。
前扣式文胸|front-clasp bra|杯间中央扣具可见，后部带片连续。
长线胸衣内搭|longline bra|胸下带向腰上延长，纵向接缝与杯体分开。
无缝模杯文胸|seamless molded-cup bra|平滑杯面无拼缝，肩带、侧翼与底围边缘明确。
工字背运动内衣|racerback sports bra|肩带在背部汇合成工字形，宽底围和完整前片可见。
高包覆运动内衣|high-coverage sports bra|前胸覆盖较高、肩带较宽，包边与面片缝清楚。
长款运动内衣|longline sports bra|运动上片向腰上延长，底围位置与衣长可比较。
背心式贴身胸衣|vest-style bra top|连贯前后片和宽肩带组成背心形内搭，边缘平整。
''',aliases=['内衣','文胸','胸罩','贴身内搭'])

block('underwear','内裤与贴身内搭细分','''
低腰三角内裤|low-rise briefs|低腰缘与普通三角裤型，以独立服装物件展示，接缝可见。
中腰三角内裤|mid-rise briefs|腰缘介于低腰与高腰，前后布片和腿口包边清楚。
高腰三角内裤|high-rise briefs|高腰布片与较低腿口，腰边和侧缝完整。
平角内裤|boyshort underwear|前后布片延伸成短平角裤，腿口与腰带可区分。
长腿平角内裤|long-leg underwear shorts|裤腿延至上腿，裆部拼片和内侧缝明确。
无缝贴身内裤|seamless briefs|平滑弹性布面、压边腿口和较少外露缝线。
丁字内裤|thong underwear garment|孤立展示服装正背两面，前片、窄后带与侧带结构清楚。
高腰加宽腰带内裤|wide-waistband briefs|高腰带加宽，裤身和腰带接缝区分，不表现身体塑形效果。
背心式内衣|undershirt vest|独立浅色贴身背心，宽肩带与下摆包边明确。
吊带式内衣|camisole undergarment|细肩带与完整长衣身，领缘和腋下包边清楚。
长衬裙内搭|full slip underdress|完整及膝吊带衬裙，薄而不透明，胸部与腰部缝线可辨。
半衬裙内搭|half slip underskirt|只有腰下的衬裙，弹性腰缘和下摆分别可见。
连体打底内衣|underwear bodysuit|完整连体内搭从肩带延至裤型下部，用裁缝人台展示。
短衬裤内搭|pettipants undershorts|宽松短衬裤，薄布与腿口小褶边清楚。
保暖长内衣套装|thermal underwear set|长袖上衣与长裤分离，罗纹袖口、裤口和腰带可见。
肚兜传统内搭|dudou traditional undergarment|独立服装物件展示菱形前片、颈带和背系带，完整布片不透明。
''',aliases=['内衣','内裤','衬衣内搭','贴身内搭'])
CATALOG[-1]['styles']=['chinese']

block('onepiece','紧身服与连体训练服','''
高领长袖紧身连体服|high-neck long-sleeve unitard|完整不透明衣身延至腕踝，高领和纵向接缝可见。
前拉链紧身连体服|front-zip fitted unitard|立领到腰部的前拉链，完整长袖长裤连接成一体。
圆领无袖紧身连体服|sleeveless round-neck unitard|无袖上身与长裤连成一体，圆领和腋下包边清楚。
短袖短腿紧身连体服|short-sleeve short-leg unitard|短袖与及上腿裤腿连接，完整前后片便于比较。
半袖骑行连体服|cycling skinsuit|半袖与及膝紧身裤连体，拉链和功能拼片明确。
长袖舞蹈紧身衣|long-sleeve dance leotard|长袖练功衣配完整不透明紧身裤袜，腰与腿口接缝清楚。
无袖舞蹈紧身衣|sleeveless dance leotard|宽带无袖练功衣配不透明长紧身裤袜，肩带与衣身完整。
七分腿训练连体服|capri training unitard|袖身完整，裤腿收在小腿中段，区分衣长与裤口。
拼色紧身训练服|color-panel fitted training suit|完整长袖长裤用侧部不同色拼片表达接缝走向。
缝线分区紧身服|seam-mapped fitted bodysuit|不透明弹性衣用细缝线分区，胸腹不使用透明开窗。
短领机能紧身服|utility-collar fitted suit|短领连体衣配少量设备环，带具固定在接缝加固处。
哑光英雄紧身服|matte superhero bodysuit|完整不透明长袖长裤与手套靴组合，原创简洁徽形。
护片英雄紧身服|armored-panel superhero bodysuit|紧身衣外有独立肘膝护片和胸片，软硬连接明确。
科幻驾驶紧身服|science-fiction pilot suit|完整贴合长袖长裤，接口饰件与关节面片可见，原创非宇航装备。
分区发光紧身服|luminous-panel fantasy bodysuit|不透明完整衣身上有局部发光线，接缝与光线分别处理。
带裙片紧身连体服|unitard with overskirt panels|完整长裤连体衣外加短裙片，内外层腰部连接清楚。
''',aliases=['紧身服','连体紧身服','紧身衣','bodysuit','unitard'])

block('space_suits','舱内舱外与科幻宇航服','''
舱内橙色压力服参考|orange intravehicular pressure-suit study|封闭式压力服、颈部头盔环、手套和接口，强调舱内用途的视觉参考。
舱内白色压力服改编|white intravehicular suit adaptation|较轻的封闭衣身与长靴，管线接车辆式接口；原创外观改编。
舱内坐姿适配服|seat-compatible intravehicular suit|中立站姿展示腹股与膝部活动面片、接口和头盔环。
舱外EMU轮廓参考|EMU-inspired extravehicular suit study|宽厚多层外衣、硬上躯干、密封手套、头盔和生命保障背包。
舱外月面服改编|lunar EVA suit adaptation|宽厚密封衣、月面靴、关节褶段与独立背包，原创改编。
舱外工作服带工具|EVA work-suit with tools|密封宇航服外有胸前控制件、工具系带与安全连接点。
舱外服后部结构|EVA suit rear-view construction|背面展示独立背包、腰部连接和肩肘关节，外轮廓完整。
舱外服头盔护罩|EVA suit helmet-visor study|全身宇航服采用清楚的头盔护罩、锁环和手套密封连接。
科幻深空探索服|original deep-space exploration suit|完整封闭衣、硬胸片和生命保障背包，未来设计与实物参考分列。
科幻采矿宇航服|original asteroid-mining suit|封闭厚衣与工具挂点，肩膝保护面片不妨碍关节。
科幻维修宇航服|original orbital-repair suit|封闭头盔、手套和带具，细长工具固定在胸前与腰侧。
科幻救援宇航服|original space-rescue suit|封闭衣身采用醒目分区色，背包装置与救援挂点明确。
科幻极地星球服|original icy-planet sealed suit|厚保温外层、完整密封头盔与靴，动作面片位于膝肘。
科幻沙尘星球服|original dust-planet sealed suit|低突出的防尘外层、密封环与背部装置，面罩完整。
科幻重型外骨骼宇航服|heavy exoskeleton space suit|密封软服外有承重骨架，铰接轴与肢体关节对应。
科幻轻型舱内工作服|original light cabin crew suit|完整轻型衣身与可拆头盔接口，明确为舱内原创科幻方案。
''',aliases=['宇航服','航天服','太空服','spacesuit'])

block('masks','面具覆盖与主题细分','''
双眼半脸面具|eye-area half mask|面具覆盖双眼周围，两个眼孔与鼻梁弧面明确，后系带可见。
单侧半脸面具|one-sided face mask|只覆盖脸部一侧的额眼颊，眼孔和侧系带完整。
下半脸装饰面具|lower-face decorative mask|面具盖住口鼻与下颊，上方眼部开放，侧面固定带可辨。
全脸素面具|plain full-face mask|完整额鼻颊下巴曲面，眼孔与小口孔，边缘有系带。
舞会羽饰面具|feathered masquerade mask|眼部面具一侧有羽饰，羽根与面具连接，手持或系带方式明确。
金属镂纹面具|metal filigree mask|眼部金属细框与镂纹，纹样保留眼孔，不遮住鼻梁结构。
木雕面具改编|carved-wood mask adaptation|孤立木制全脸面具，雕刻层次和后缘穿带孔可见，原创图案。
陶瓷素面具|ceramic face mask|白陶全脸曲面、眼孔和光滑釉面，厚边与固定孔清楚。
狐形主题面具|fox-inspired costume mask|长耳和尖鼻的原创狐形面具，孔位与人脸佩戴位置一致。
猫形主题面具|cat-inspired costume mask|三角耳、短鼻与双眼孔，表面猫纹与结构分开。
兔形主题面具|rabbit-inspired costume mask|长耳全脸装饰面具，眼孔和耳根加固位置明确。
鹿角主题面具|antler-inspired costume mask|完整面具外接小型分枝角，角根固定在额部。
机械分片面具|mechanical segmented mask|硬面片通过小铰链和侧扣组合，口鼻区域有完整盖片。
透明护面装扮|clear visor costume mask|透明弧形罩与硬边框、后固定带组合，不作为防护等级说明。
发光线纹面具|luminous-line fantasy mask|不透明完整面具上有原创发光线路，眼孔不变成实心光块。
戏剧彩绘主题面具|painted theatrical costume mask|孤立全脸面具采用原创舞台色块，区别于直接画在脸上的戏曲脸谱。
''',aliases=['面具','面部装扮','mask'])

block('eyewear','框形镜片与装备眼镜','''
细金属圆框眼镜|thin-metal round spectacles|细圆镜圈、窄鼻梁和细镜腿，透明镜片与鼻托清楚。
粗板材方框眼镜|thick-acetate square spectacles|厚方形镜圈、宽镜腿与完整透明镜片，边角较直。
椭圆框眼镜|oval spectacles|横向椭圆镜圈配细镜腿，镜片形状与圆框区分。
猫眼框眼镜|cat-eye spectacles|镜圈外上角上扬，鼻梁和镜腿接点明确。
六边形框眼镜|hexagonal spectacles|镜片周围六段折线形成多角边框，鼻托清楚。
眉线半框眼镜|browline spectacles|上框加厚，下方为细金属圈，鼻梁连接完整。
下半无框眼镜|semi-rimless spectacles|上缘框条与下缘透明线固定镜片，镜腿接点可见。
全无框眼镜|rimless spectacles|镜片边缘无镜圈，鼻梁和镜腿通过小孔件连接。
双梁飞行框眼镜|double-bridge aviator spectacles|水滴形透明镜片与两道鼻梁，细金属框明确。
小圆墨镜|small round sunglasses|较小圆形深色镜片、窄桥与细腿，区别于透明矫正镜。
方形墨镜|square sunglasses|方形深色镜片和较粗框条，镜腿宽度可见。
渐变镜片眼镜|gradient-lens eyewear|同一镜片从上深下浅渐变，框形和镜片效果分别可辨。
夹片太阳镜眼镜|clip-on sunglass spectacles|普通框上有可翻起夹片，小夹点与内层镜片都可见。
运动包覆眼镜|wraparound sports eyewear|弯曲镜片包向面侧，鼻托和镜腿末端贴合结构清楚。
单片链式眼镜|chained monocle|孤立圆形单镜片与边框，固定小链连接下缘。
双目密封护目镜|sealed two-lens goggles|两个镜片嵌在贴脸软边框中，后部弹性头带清楚。
''',aliases=['眼镜','镜框','镜片','glasses','eyewear'])

block('eyes','自然虹膜与圆瞳观察','''
深棕虹膜圆瞳|dark-brown iris and round pupil|虹膜为深棕色，中央瞳孔保持黑色圆形，放大眼部展示。
浅棕虹膜圆瞳|light-brown iris and round pupil|浅棕虹膜有放射纹理，中央圆瞳与虹膜边缘区分。
琥珀虹膜圆瞳|amber iris and round pupil|金棕虹膜、黑圆瞳和清楚的外缘，不把虹膜颜色写成瞳孔颜色。
榛色虹膜圆瞳|hazel iris and round pupil|棕绿交织的虹膜纹理，瞳孔为中央黑色圆开口。
绿色虹膜圆瞳|green iris and round pupil|绿色虹膜围绕黑色圆瞳，眼白与虹膜边界明确。
灰色虹膜圆瞳|gray iris and round pupil|灰色虹膜有柔和放射细纹，中央圆瞳保持独立。
蓝色虹膜圆瞳|blue iris and round pupil|蓝色虹膜、黑色中央圆瞳与角膜小高光分开表现。
蓝灰虹膜圆瞳|blue-gray iris and round pupil|低饱和蓝灰虹膜，圆瞳和外缘清楚，颜色参考不等同于分类边界。
双眼异色虹膜|complete heterochromia visual study|一对眼睛左右虹膜颜色不同，两边中央瞳孔都保持圆形。
扇区异色虹膜|sectoral heterochromia visual study|单眼虹膜的一块扇区颜色不同，黑色圆瞳保持完整。
中央异色虹膜|central heterochromia visual study|瞳孔周围内环与外部虹膜色不同，中央开口仍是圆瞳。
明显虹膜外环|pronounced iris outer-ring study|虹膜外缘较深的环形边界，和中央圆瞳分开。
放射纹虹膜|radial iris-texture study|细放射纹从圆瞳周围向外延伸，颜色克制，避免画成机械符号。
斑点纹虹膜|speckled iris-texture study|虹膜内部有细小色斑，瞳孔边缘仍为完整圆形。
较小圆瞳观察|small round-pupil visual study|中央圆瞳相对较小，虹膜颜色和眼形保持一致，只比较形态。
较大圆瞳观察|large round-pupil visual study|中央圆瞳相对较大，虹膜可见环较窄，只作为绘画观察参考。
''',aliases=['瞳孔','虹膜','眼睛细节','瞳色','iris','pupil'])

block('eyes','幻想瞳孔与虹膜图案','''
细竖缝瞳幻想|thin vertical-slit fantasy pupil|幻想眼睛中央黑瞳是细竖缝，虹膜与眼白完整，非自然人眼类型。
宽竖椭圆瞳幻想|vertical-oval fantasy pupil|中央瞳孔为竖向宽椭圆，区别于细缝，两端弧线平滑。
横缝瞳幻想|horizontal-slit fantasy pupil|中央瞳孔呈横向长缝，明确为幻想生物设计。
四芒星瞳幻想|four-point star fantasy pupil|中央黑瞳为四尖星形，虹膜完整围绕，与高光区分。
六芒星瞳幻想|six-point star fantasy pupil|中央黑瞳是清楚的六尖轮廓，标记幻想，避免依赖眼部高光。
菱形瞳幻想|diamond fantasy pupil|中央黑色菱形瞳孔，虹膜的圆外边界保持完整。
心形瞳幻想|heart-shaped fantasy pupil|中央黑瞳呈心形，心形不是角膜反光，明确为幻想。
十字瞳幻想|cross-shaped fantasy pupil|中央黑色十字开口在虹膜内部，四臂长度清楚。
三角瞳幻想|triangular fantasy pupil|中央瞳孔为单个三角形，眼白和圆形虹膜保持完整。
双环虹膜幻想|double-ring fantasy iris|圆瞳外有两道独立光色环，瞳孔自身不变成环形。
符文虹膜幻想|rune-pattern fantasy iris|圆瞳外的虹膜含原创小符号环，符号与中央开口区分。
机械光圈瞳幻想|mechanical-aperture fantasy eye|眼部以机械叶片包围中央开口，标注机械义眼创作。
星云虹膜幻想|nebula-pattern fantasy iris|虹膜里有星云色块，中央瞳孔保持黑圆，纹样为原创幻想。
火焰纹虹膜幻想|flame-pattern fantasy iris|火焰形纹路位于虹膜内部，圆瞳、纹样和高光分开。
晶体切面虹膜幻想|faceted-crystal fantasy iris|虹膜色块形成晶体切面，中央开口与外边界清楚。
双环异色幻想眼|dual-ring heterochromic fantasy eyes|一对眼睛各有两色环和圆瞳，明确为虚构角色设定。
''',aliases=['瞳孔','虹膜','幻想眼睛','特殊瞳孔','iris','pupil'])

# Recognize existing Chinese references in the same broad style index.
for e in CATALOG:
    if e['category']=='traditional' and e['name'] in {
        '对襟短衫长裙灵感','齐胸系裙灵感','坦领襦裙灵感','圆领袍裙灵感','披帛长裙灵感',
        '短袄褶裙灵感','立领长袍灵感','盘扣现代中式裙','交领短袄马面裙灵感','立领长衫马面裙灵感',
        '半臂长裙灵感','褙子叠裙灵感','比甲长裙灵感','道袍式宽袖服灵感','短褂中式裤装灵感',
        '斜襟长裙灵感','袄裙披肩灵感','长衫长裤灵感','盘扣宽袖礼装'
    }:
        e.setdefault('styles',[]).append('chinese')
        e.setdefault('aliases',[]).extend(['中国传统服饰','中式服装'])
