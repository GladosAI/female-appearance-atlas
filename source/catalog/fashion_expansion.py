"""Edition 4: exposed-shoulder construction and concrete fashion coordinates."""
from catalog_content import CATALOG, category, add

def shoulder(key, dimension, text, types):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==len(types)
    for e,t in zip(CATALOG[start:],types):e['shoulder_type']=t

shoulder('construction','露肩与肩部承托','''
一字肩领结构|off-the-shoulder Bardot neckline|领缘横向位于肩端下方，左右肩顶都露出，袖子接在上臂处。
挖肩开口结构|cold-shoulder cutout construction|衣物保留肩带或肩部布片，只在左右肩端挖出窗口。
单肩承托结构|one-shoulder neckline construction|一侧肩带或袖片承托衣身，另一侧肩部开放。
抹胸支撑结构|strapless bodice construction|没有肩带与绕颈带，衣身通过内部支撑和贴合上缘保持位置。
挂脖承托结构|halter neckline construction|衣带绕颈承托，肩端开放，前胸由完整衣片覆盖。
细肩带承托结构|spaghetti-strap construction|两条细肩带从前身延伸到背部，肩顶大部分露出。
分离袖露肩结构|detached-sleeve exposed-shoulder construction|衣身与袖体不在肩部相连，独立袖体固定在上臂。
交叉肩带开肩结构|cross-strap shoulder-opening construction|颈肩带交叉形成开放肩窗，带端固定点可追踪。
''',['bardot','cold_shoulder','one_shoulder','strapless','halter','thin_strap','detached_sleeve','cross_strap'])
shoulder('tops','露肩上装','''
一字肩贴合上衣|fitted off-shoulder top|横向领缘位于肩下，贴合衣身与短袖完整包覆躯干。
一字肩宽袖布衫|wide-sleeve off-shoulder blouse|双肩露出，领边弹力收拢，宽袖从上臂开始垂落。
一字肩罗纹针织衫|rib-knit Bardot top|横向罗纹领边在双肩下方，长袖与衣身保持针织弹性。
翻折领露肩上衣|foldover off-shoulder top|宽领边向外翻折包住上臂顶端，肩顶清楚露出。
荷叶环边露肩上衣|ruffle-edge off-shoulder blouse|一圈荷叶覆盖领缘与上臂，双肩上方没有肩带。
挖肩长袖上衣|cold-shoulder long-sleeve top|领口与肩带完整，肩端窗口连接下方长袖。
挖肩高领针织衫|cold-shoulder turtleneck|高领与肩顶窄布条保留，两侧肩端开口明确。
挖肩泡袖布衫|cold-shoulder puff-sleeve blouse|宽肩带下方露出肩端，泡袖在上臂收拢。
单肩长袖上衣|one-shoulder long-sleeve top|只有一侧长袖和肩部覆盖，另一侧肩顶开放。
单肩荷叶布衫|one-shoulder ruffle blouse|斜向上缘带荷叶，一侧肩上有承托布片。
宽带挂脖布上衣|wide-band halter blouse|宽颈带接完整前身，两侧肩端露出。
交叉挂脖上衣|cross-halter top|上胸两条宽带交叉后绕颈，躯干覆盖完整。
细吊带针织上衣|spaghetti-strap knit top|两根细带承托平整针织前后衣身，衣摆到腰下。
抹胸式布上衣|strapless woven top|无肩带的完整短衣身，上缘平直，内部支撑以接缝表现。
抹胸荷叶上衣|strapless ruffle top|无肩带衣身外叠领缘荷叶，肩顶与上臂都开放。
分离袖露肩布上衣|detached-sleeve shoulder-baring blouse|完整布衣身与两段独立长袖分开，袖顶固定在上臂。
''',['bardot','bardot','bardot','bardot','bardot','cold_shoulder','cold_shoulder','cold_shoulder','one_shoulder','one_shoulder','halter','cross_strap','thin_strap','strapless','strapless','detached_sleeve'])
shoulder('onepiece','露肩裙装','''
一字肩日常裙|off-shoulder day dress|双肩下横向领缘、短袖与收腰中长裙连接。
一字肩抽褶长裙|gathered off-shoulder maxi dress|弹力领边在上臂处收束，下方长裙布量充足。
一字肩针织裙|off-shoulder knit dress|双肩开放，罗纹长袖与直身裙体相连。
翻折领露肩礼裙|foldover off-shoulder gown|宽翻折领包住上臂，肩顶裸露，长裙由纵向接缝塑形。
荷叶领露肩裙|ruffled off-shoulder dress|领边荷叶环绕胸肩下缘，无肩带，中长裙微展。
挖肩衬衫裙|cold-shoulder shirt dress|衬衣领与前扣保留，肩端挖窗接完整袖体。
挖肩针织长裙|cold-shoulder knit maxi dress|高领长袖裙两侧肩端开口，腰身和下摆简洁。
挖肩泡袖连裙|cold-shoulder puff-sleeve dress|宽肩带与泡袖间有清楚肩窗，裙摆适度蓬起。
单肩长袖礼裙|one-sleeve asymmetrical gown|一侧肩和整条手臂由袖子覆盖，另一侧肩开放。
单肩斜褶裙|one-shoulder draped dress|一根宽肩带承托斜向褶片，腰侧固定。
挂脖收腰长裙|halter-neck fitted-waist dress|宽绕颈带接前身，两肩开放，腰下长裙展开。
交叉挂脖礼裙|cross-halter gown|前领宽带交叉后绕颈，长裙完整覆盖下身。
细吊带圆摆裙|spaghetti-strap full-skirt dress|细带承托收腰衣身，下面连接圆摆中长裙。
无肩带柱形礼裙|strapless column gown|没有肩带的支撑上身接长直裙，接缝显示衣身支撑。
无肩带蓬摆礼裙|strapless full-skirt gown|无带上缘与窄腰下方大裙摆形成对比。
分离袖露肩长裙|detached-sleeve gown|无肩连接的长裙衣身，独立袖套在上臂固定。
''',['bardot','bardot','bardot','bardot','bardot','cold_shoulder','cold_shoulder','cold_shoulder','one_shoulder','one_shoulder','halter','cross_strap','thin_strap','strapless','strapless','detached_sleeve'])

category('fashion_outfits','服装风格与搭配','具体穿搭方案按风格标签交叉组织。风格可以混合，标签用于检索；图例为原创设计，不将一种配色视为整种风格。',['R22','R23','R24','R25'])
def styled(style,dimension,text):
    start=len(CATALOG);add('fashion_outfits',dimension,text)
    for e in CATALOG[start:]:e['styles']=[style]

styled('gothic','哥特穿搭','''
高领蕾丝哥特长裙|high-neck lace goth ensemble|高领包覆衬衣、暗色长裙与尖形首饰，蕾丝只在领袖边。
绒面束腰哥特裙装|velvet waistcoat goth ensemble|绒面外穿腰马甲罩在袖衫外，下接暗酒红长裙。
宽袖浪漫哥特装|romantic goth wide-sleeve ensemble|钟形袖、柔软叠裙和小披肩形成垂落轮廓。
后摆维多利亚哥特装|Victorian goth bustle ensemble|收腰外套与后部集中裙量，三分之二侧视显示后摆。
短尾哥特裤装|goth tailcoat trouser ensemble|短前长后外套配高领衬衣、细直裤和踝靴。
披风哥特礼装|goth cloak formal ensemble|深色长披风罩在完整礼裙外，领扣是主识别点。
尖领哥特通勤装|point-collar modern goth outfit|尖领衬衣、窄长外套和直裙，以剪裁建立轮廓。
不对称哥特叠穿|asymmetric goth layered outfit|斜摆针织上衣、长短错位裙片和硬腰带。
工业哥特工装|industrial goth utility outfit|深灰工具马甲、金属扣带与长裤，装备贴身固定。
赛博哥特荧光装|cyber-goth accent outfit|暗色机能衣裤与少量荧光带、硬质肩片形成对比。
哥特格纹长裙装|goth tartan long-skirt outfit|黑色高领短外套配暗红格纹长裙，饰件集中腰部。
哥特针织层搭|goth knit layered outfit|薄纹理外针织罩在不透明内衣外，下配直长裙。
哥特骑装剪影|goth riding-silhouette outfit|长线条收腰外衣、马裤和长靴，领饰较小。
浅色哥特改编装|pale gothic-inspired outfit|象牙色高领蕾丝、尖形银饰与层裙保留哥特剪影。
田园哥特叠裙装|pastoral goth layered-skirt outfit|深色花纹长裙、袖衫与短披肩，植物纹样局部使用。
哥特朋克混搭装|goth-punk hybrid outfit|长尾外套、格纹裙片、皮带和金属链形成混合方案。
''')
styled('british','英伦剪裁与乡村学院','''
粗花呢英伦裙套装|British-inspired tweed skirt suit|粗花呢收腰夹克、膝下裙与短靴，面料纹理清楚。
格纹英伦裤套装|British-inspired checked trouser suit|小格纹西装、前褶裤与素衬衣构成整套剪裁。
三件式英伦裤装|British-inspired three-piece outfit|外套、纽扣马甲和同料长裤分成三层。
风衣英伦城市装|British-inspired trench city outfit|长风衣外罩针织和直裤，领巾与低跟短靴搭配。
蜡感外套乡村装|British-country waxed-jacket concept|蜡感短外套、针织内搭与耐磨长裤，领面材质不同。
绗缝马甲乡村装|British-country quilted-vest concept|菱格马甲、格衬衣、灯芯绒裤和野外靴。
骑装夹克英伦装|British-inspired riding-jacket outfit|收腰骑装外套、窄腿裤与高靴，肩腰比例明确。
粗花呢披风英伦装|British-inspired tweed-cape outfit|厚短披风、袖衫和长裙，帽和鞋保持简洁。
针织背心英伦学院装|British-inspired academic knit-vest outfit|成人学院衬衣、菱形针织背心和前褶裤。
滚边西装学院装|piped-blazer adult-academic outfit|滚边西装、领带与中长格裙，使用原创无校徽设计。
海军蓝英伦裙装|navy British-inspired tailored outfit|海军蓝窄腰西装配浅色袖衫与过膝直裙。
灯芯绒英伦层搭|corduroy British-inspired layered outfit|灯芯绒外套、针织领内搭与格纹直裙。
棋盘格复古都市装|checked retro-British city concept|短方身外套、A字裙与踝靴，图案按面片对齐。
猎装腰带英伦装|British-country belted-safari concept|四袋腰带外套、卷袖衬衣与直裤，适合乡村旅行角色。
格纹围巾长大衣装|checked-scarf British-inspired coat outfit|深色长大衣、格围巾、直裤与切尔西短靴。
英伦朋克剪裁混搭|British-tailoring punk hybrid outfit|格纹剪裁外套配不对称裙、皮扣与金属件。
''')
styled('lolita','洛丽塔时尚穿搭','''
甜系蝴蝶结洛丽塔装|sweet Lolita bow coordinate|成人时尚造型，浅色圆蓬及膝裙、布衫与对称结饰。
甜系层褶洛丽塔装|sweet Lolita tiered coordinate|淡色多层褶裙、圆领长袖布衫和小头饰。
古典花纹洛丽塔装|classic Lolita floral coordinate|克制花纹A形蓬裙、高领布衫与小圆帽。
古典领结洛丽塔装|classic Lolita neck-bow coordinate|深茶色吊带裙叠袖衫，细领结与裙缘纹样相呼应。
哥特黑白洛丽塔装|gothic black-and-white Lolita coordinate|黑色及膝蓬裙、白袖衫与黑白蕾丝，轮廓完整。
哥特绒面洛丽塔装|gothic velvet Lolita coordinate|暗色绒面蓬裙与高领袖衫，银色饰件集中领腰。
田园格纹洛丽塔装|country Lolita gingham coordinate|格纹蓬裙、短袖布衫与草帽，围裙片独立。
围裙洛丽塔搭配|apron Lolita coordinate|完整及膝蓬裙外叠装饰围裙，领袖蕾丝相配。
水手领洛丽塔装|sailor Lolita coordinate|深蓝水手领上身与蓬裙，条带装饰沿领和裙缘。
立领洛丽塔连裙|standing-collar Lolita one-piece coordinate|立领长袖连衣裙保留蓬裙支撑，纽扣与蕾丝纵向排列。
朋克格纹洛丽塔装|punk Lolita tartan coordinate|格纹蓬裙、剪裁短外套、皮扣与链条，裙摆保留完整体积。
和风洛丽塔改编装|Japanese-inspired Lolita adaptation|交叠领与宽腰带改编进及膝蓬裙，明确原创混搭。
中式洛丽塔改编装|Chinese-inspired Lolita adaptation|立领盘扣上身与圆蓬裙结合，纹样沿裙边布置。
公主洛丽塔礼装|princess Lolita formal coordinate|蕾丝宽领、多层蓬裙与小头冠，装饰集中上身和裙缘。
短开衫洛丽塔日常装|cardigan Lolita daily coordinate|短针织开衫外罩吊带蓬裙，内层完整袖衫。
长线条古典洛丽塔装|longer classic Lolita coordinate|小腿长度有支撑A裙、窄袖布衫与细腰带。
''')
styled('punk','朋克穿搭','''
铆钉皮夹克朋克装|studded leather-jacket punk outfit|斜襟皮夹克、平面铆钉、格纹裙与硬底靴。
格纹拼片朋克装|tartan-panel punk outfit|格裙面片错位、素色袖衫与不对称扣带。
DIY补丁朋克裤装|DIY patchwork punk trouser outfit|手缝补丁、磨损牛仔裤和无品牌短马甲。
安全别针朋克衫装|safety-pin punk shirt outfit|不透明上衣的破损边由安全别针连接，内层覆盖完整。
宽网纹朋克层搭|open-knit punk layered outfit|宽网纹毛衣罩在不透明袖衫外，下面为长裤。
双带束脚朋克裤装|strap-detail punk trouser outfit|侧挂带固定在裤袋和膝上，裤脚收束，扣端可见。
剪裁马甲朋克装|tailored-waistcoat punk outfit|窄腰马甲、素衬衣与格裤，皮扣形成局部重点。
斜襟长外套朋克装|asymmetric long-coat punk outfit|不对称长外套和窄裤，金属扣集中前襟。
撞色格裙朋克装|contrast-tartan punk skirt outfit|两种格纹分成裙面片，黑色上装降低图案干扰。
金属链马甲朋克装|chain-waistcoat punk outfit|链条连在明确环位，短马甲配完整长裤。
破边针织朋克装|distressed-knit punk outfit|不规则针织边缘叠在实心内衣外，短裙配厚长袜。
平面印花朋克街装|graphic punk street outfit|原创抽象印花T恤、拼片裤和贴平金属饰件。
工装朋克混搭|utility-punk hybrid outfit|工裤多袋、皮短外套与少量铆钉带具。
哥特长裙朋克装|goth-punk long-skirt outfit|黑色长裙、硬马甲、链条与不对称短外套。
霓虹赛博朋克装|neon cyberpunk hybrid outfit|机能衣裤上有少量发光色块，扣带与装备固定点明确。
格纹蓬裙朋克装|full-tartan-skirt punk outfit|有体积的格纹裙配皮夹克和结扣，适合作为朋克洛丽塔混搭。
''')
styled('preppy','学院与暗黑学院','''
菱格背心学院裤装|argyle-vest preppy trouser outfit|菱格背心、衬衣与前褶裤，成人学院穿搭。
滚边开衫学院裙装|trimmed-cardigan preppy skirt outfit|短开衫与素布衫配中长褶裙，滚边色呼应。
针织Polo学院装|knit-polo preppy outfit|翻领针织衫、直裤与简洁乐福鞋。
西装领结学院装|bow-tie preppy blazer outfit|素西装、细领结与格纹直裙，不使用真实校徽。
暗黑学院长马甲装|dark-academia long-waistcoat outfit|深棕长马甲、浅高领衬衣与长裙，纹理偏哑光。
暗黑学院粗花呢装|dark-academia tweed outfit|深色粗花呢夹克、绞花背心和前褶裤。
暗黑学院长外衣装|dark-academia long-coat outfit|长羊毛外衣、领结衬衣与直裙，饰件克制。
暗黑学院书店裙装|dark-academia bookshop outfit|细褶高领袖衫、腰马甲与长格裙。
''')
styled('mori','森系与田园','''
森系亚麻层裙装|mori linen layered-skirt outfit|亚麻色宽衣、长短叠裙与编织袋，轮廓松软。
森系蕾丝围领装|mori lace-scarf outfit|浅蕾丝围领、针织层与宽长裙形成多层材质。
森系针织罩衣装|mori knit-overlayer outfit|松量针织罩衣盖在布长裙外，衣边自然垂落。
森系围裹长裙装|mori wrap-maxi outfit|柔软披布、完整袖衫与围裹长裙，固定点少而清楚。
田园抽褶布裙装|cottagecore gathered-dress outfit|小植物印花、抽褶袖和长圆摆搭配闭口鞋。
田园围裙罩裙装|cottagecore apron-overdress outfit|浅色工具围裙叠在完整长裙外，边缘有窄褶饰。
田园格纹长裙装|cottagecore gingham maxi outfit|格纹长裙、短开衫与宽帽形成户外日常搭配。
田园宽袖束腰装|cottagecore wide-sleeve outfit|方领宽袖布衫配长裙和布腰带，纹样局部使用。
''')
styled('boho','波西米亚穿搭','''
波西米亚刺绣长裙装|boho embroidered-maxi outfit|长宽裙与局部刺绣，布带和编织袋相配。
波西米亚钩织叠穿|boho crochet-layered outfit|钩织外层罩在不透明内衣外，下配长裙。
波西米亚流苏外套装|boho fringed-jacket outfit|短外套流苏固定沿接缝，下配宽直裤。
波西米亚宽裤装|boho wide-trouser outfit|松量袖衫、宽裤和多层窄珠链，主轮廓简洁。
波西米亚围裹裙装|boho wrap-skirt outfit|花纹围裹长裙与素上衣，纹样按面片分区。
波西米亚拼布长裙装|boho patchwork-skirt outfit|不同布片按纵向拼接，色彩与花纹节奏明确。
波西米亚短马甲装|boho short-waistcoat outfit|短绒面马甲、宽袖内衫与微喇叭裤。
波西米亚露肩长裙装|boho off-shoulder-maxi outfit|双肩下抽褶领边、宽袖与长裙，局部编织饰边。
''')
styled('minimal','极简与通勤','''
极简单色裙套装|minimal monochrome skirt suit|无领外套和直裙同色，表面装饰少。
极简长马甲裤装|minimal long-vest trouser outfit|平整无袖长外层与细直裤，接缝是主要细节。
极简衬衣宽裤装|minimal shirt-wide-trouser outfit|清楚肩线衬衣配宽裤，腰线与领口保持简洁。
极简柱形连裙装|minimal column-dress outfit|直身长裙、平整袖口和一枚小腰扣。
极简斜摆针织装|minimal asymmetric-knit outfit|单侧斜摆针织上衣与直裙形成几何关系。
极简短外套连体装|minimal jacket-jumpsuit outfit|短方身外套、同色连体裤与简洁鞋包。
极简围裹通勤装|minimal wrap office outfit|围裹上衣、前褶裤和窄腰带，固定点清楚。
极简露肩礼装|minimal off-shoulder formal outfit|纯色横向肩下领缘与直长裙，装饰集中一处。
''')
styled('retro','复古优雅穿搭','''
复古腰结茶裙装|retro sash-tea-dress outfit|收腰茶裙、短开衫与小圆帽，裙摆适度展开。
复古高领长裙装|retro high-neck maxi outfit|细褶高领衬衣配长裙，腰带和小扣呼应。
复古斜裁晚裙装|retro bias-evening-dress outfit|顺滑长裙配短披肩，垂褶作为轮廓重点。
复古短夹克蓬裙装|retro fitted-jacket full-skirt outfit|窄腰短夹克与宽中长裙形成大体积对比。
复古格纹骑行装|retro checked cycling outfit|格纹短外套配膝下宽裤，适合成人日常改编。
复古翻领连体裤装|retro lapel-jumpsuit outfit|翻领收腰上身连接宽裤腿，搭配细腰带。
复古一字肩礼裙装|retro Bardot formal-dress outfit|双肩露出、折领与收腰圆摆，中长裙体完整。
复古长手套礼装|retro formal glove coordinate|包覆礼裙与长手套、小披肩和素色鞋包。
''')
styled('streetwear','街头穿搭','''
宽卫衣工裤街装|oversized-hoodie cargo streetwear|宽卫衣与口袋工裤，内外下摆错位。
短夹克宽裤街装|cropped-jacket baggy streetwear|短硬外套与宽松裤形成长度对比。
球衣叠衬衣街装|jersey-shirt layered streetwear|运动球衣外层、长衬衣袖与宽裤，原创无队标。
双层T恤街装|double-tee streetwear|长袖内层外套短袖T恤，搭配宽短裤。
牛仔叠穿街装|denim-layered streetwear|大牛仔外套和长衬衣配直腿裤，磨损局部使用。
拼色运动街装|colour-block sports streetwear|拼片运动夹克、宽运动裤与厚底运动鞋。
长马甲工装街装|long-utility-vest streetwear|工具马甲罩在宽袖内衣外，裤袋位置与上层错开。
一字肩针织街装|off-shoulder knit streetwear|宽松肩下领针织衫与宽腿工裤组合。
''')
styled('techwear','机能与赛博穿搭','''
硬壳多袋机能装|hardshell pocket techwear outfit|防水短外套、层袋与关节拼片裤，带具用途明确。
立领分片机能装|stand-collar panelled techwear|立领夹克和分片裤，拉链与袋位避开关节。
短披多袋机能装|short-cape utility techwear|防雨短披覆与工具内层，下摆可收起。
可拆马甲机能装|modular-vest techwear outfit|可拆袋马甲和长袖底层，挂点清楚。
赛博光边都市装|cyberpunk edge-light city outfit|流线深色外套、发光窄边与设备腰袋。
赛博不对称短装|cyberpunk asymmetric-jacket outfit|单侧较长外套、几何裤片与小屏幕设备。
赛博透明罩衣装|cyberpunk translucent-overcoat outfit|透明外层罩在完整不透明衣裤外，内外接缝分明。
赛博硬肩长外衣装|cyberpunk rigid-shoulder long-coat outfit|硬肩片、分叉外衣与贴身设备带形成都市轮廓。
''')
styled('steampunk','蒸汽朋克穿搭','''
蒸汽朋克马甲长裙装|steampunk waistcoat-maxi outfit|衬衣、外穿腰马甲、层裙与机械仪表袋。
蒸汽朋克工具裤装|steampunk utility-trouser outfit|短皮外套、前褶裤和工具围片，机械装置有固定点。
蒸汽朋克燕尾装|steampunk tailcoat outfit|燕尾外套、细褶袖衫和长裤，铜色扣件局部使用。
蒸汽朋克后摆裙装|steampunk bustle-skirt outfit|后部裙量和硬腰封，侧腰挂小仪表而非满身齿轮。
蒸汽朋克飞行装|steampunk aviator outfit|短保暖夹克、护目镜与工具裤，带具贴身。
蒸汽朋克工程围裙装|steampunk engineer-apron outfit|完整袖衣裤外罩分袋围裙，机械零件集中工具区。
蒸汽朋克礼仪裙装|steampunk formal-dress outfit|高领长裙、短披与小型铜色结构饰件。
蒸汽朋克英伦混搭|steampunk British-tailoring hybrid|粗花呢剪裁外套、马甲与仪表腰带，长裤完整。
''')

# Mixed styles are searchable under each relevant family.
cross_styles={
    '赛博哥特荧光装':['cyberpunk'], '哥特朋克混搭装':['punk'],
    '英伦朋克剪裁混搭':['punk'], '哥特黑白洛丽塔装':['gothic'],
    '哥特绒面洛丽塔装':['gothic'], '朋克格纹洛丽塔装':['punk'],
    '哥特长裙朋克装':['gothic'], '霓虹赛博朋克装':['cyberpunk'],
    '格纹蓬裙朋克装':['lolita'], '蒸汽朋克英伦混搭':['british'],
    '针织背心英伦学院装':['preppy'], '滚边西装学院装':['preppy'],
    '田园格纹洛丽塔装':['cottagecore']
}
for e in CATALOG:
    if e['name'].startswith('暗黑学院'):e['styles']=['dark_academia']
    if e['category']=='fashion_outfits' and e['dimension']=='森系与田园' and e['name'].startswith('田园'):e['styles']=['cottagecore']
    if e['category']=='fashion_outfits' and e['name'].startswith('赛博') and e['dimension']=='机能与赛博穿搭':e['styles']=['cyberpunk']
    for style in cross_styles.get(e['name'],[]):
        if style not in e.setdefault('styles',[]):e['styles'].append(style)
    if e['name'] in ['波西米亚露肩长裙装','极简露肩礼装','复古一字肩礼裙装','一字肩针织街装']:e['shoulder_type']='bardot'

_start=len(CATALOG)
add('fashion_outfits','露肩风格混搭','''
一字肩哥特长裙装|off-shoulder gothic maxi coordinate|黑色肩下折领、长袖、蕾丝长裙与银色尖形饰件。
挖肩哥特针织装|cold-shoulder gothic knit coordinate|黑色高领针织上衣保留窄肩带与肩窗，下配暗色长裙。
单肩朋克街装|one-shoulder punk street coordinate|一侧长袖的黑色上衣、金属链与拼片格纹裤，另一肩开放。
挖肩朋克格裙装|cold-shoulder punk tartan coordinate|肩窗黑色袖衫、格纹裙片和皮扣，带端固定明确。
一字肩英伦格裙装|Bardot British-inspired tartan coordinate|剪裁收腰格纹中长裙采用肩下折领，属于原创英伦礼装改编。
挂脖极简裤装|halter minimalist trouser coordinate|宽绕颈黑色布上衣配浅色烟管裤，无多余装饰。
细带街头叠穿装|thin-strap street layered coordinate|完整细带上衣配宽裤，外衬衣落在肘部作为独立穿搭层。
一字肩蒸汽朋克装|Bardot steampunk coordinate|肩下白布衫、外穿棕腰马甲与长裙，机械仪表挂在腰侧。
''')
for e,style,t in zip(CATALOG[_start:],['gothic','gothic','punk','punk','british','minimal','streetwear','steampunk'],['bardot','cold_shoulder','one_shoulder','cold_shoulder','bardot','halter','thin_strap','bardot']):
    e['styles']=[style];e['shoulder_type']=t
