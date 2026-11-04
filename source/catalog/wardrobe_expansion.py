"""Edition 6: hats, bags, military, wizard and priestess wardrobes."""
from catalog_content import CATALOG, CATEGORIES, category, add

def block(key,dimension,text,aliases=(),styles=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:e['aliases']=list(aliases);e['styles']=list(styles)

category('military_outfits','军装与军旅主题服装','礼服、常服、作训服与架空军装分列；图例为原创视觉改编，具体国家、年代与等级沿实物资料核对。',['R34'])
category('wizard_outfits','巫师与魔女服装','用帽形、袍袖、披风、工具袋与材质组合区分职业；均为原创幻想服装。',[])
category('priestess_outfits','巫女与女祭司服装','日本神社装束参考与架空巫祝、女祭司设计分别标注；地区、仪式和服制并非通用。',['R35','R36'])

block('hats','日常礼仪与职业帽','''
六片弧檐棒球帽|six-panel curved-brim cap|六片帽身缝线汇聚到顶钮，前方弧形硬檐，后调节带可见。
五片营帽|five-panel camp cap|平整前片与上顶片组合，浅帽冠和短檐呈盒状轮廓。
平檐街头帽|flat-brim cap|较深帽冠与平直硬檐，檐底厚度和帽后扣带可辨。
网背卡车帽|mesh-back trucker cap|前部实心面片、后部网格帽身与弧檐，透气结构明确。
圆顶软檐遮阳帽|soft-brim sun hat|柔软圆帽冠与垂落宽檐，檐缘和下颌系绳连接可见。
短檐桶帽|short-brim bucket hat|较高桶形帽冠、窄下斜檐和帽身侧缝，区别于宽檐渔夫帽。
护颈防晒帽|neck-flap sun cap|前帽檐与后护颈布相连，后布覆盖颈部范围可辨。
带绳探险帽|chin-cord expedition hat|中等帽冠、环形檐和穿侧孔下颌绳，固定件清楚。
可折叠旅行帽|foldable travel hat|软檐、分片帽冠和收纳折线，材质可弯曲，整体完整展示。
狩猎双檐帽|deerstalker-style cap|前后各有短帽檐，侧护耳片可翻起并在顶上系结。
小圆筒无檐帽|pillbox hat|低圆柱帽身没有外檐，帽底与侧壁明确，适合礼仪改编。
船形侧帽|garrison side cap|狭长折叠帽身形成船形上缘，两侧折线与前后尖端可见。
硬檐军官帽|peaked service cap|宽帽冠、前硬檐和横向帽带，正面徽位留空。
平顶水手帽|flat-top sailor cap|圆形平顶、窄帽围与后部飘带，不使用真实军队标记。
褶边波奈特帽|ruffled bonnet|帽冠罩住后头部，前缘褶边与下颌系带完整。
软布系带睡帽|soft tied nightcap|软布帽身和后垂帽尾，前缘松紧或系带，不画成长睡衣。
''',['帽子','帽型','帽饰','hat','cap'])

block('hats','保暖复古与幻想帽','''
三角折檐帽|tricorn-style hat|环檐在三个方向向上折起，三角外轮廓与帽冠清楚。
双角硬檐帽|bicorne-style hat|宽檐向两侧折起形成两角，帽冠和折檐的连接可辨。
隧道檐波奈特帽|poke bonnet|较深帽冠与前伸隧道形帽檐，后颈布和下颌系带完整。
折尖巫师帽|bent-tip wizard hat|尖帽冠顶端向一侧折弯，完整环檐与帽围带可见。
宽檐魔女尖帽|wide-brim witch hat|高尖帽冠与宽平檐连接，尖顶、帽根和檐缘形成三层轮廓。
短尖软巫帽|short-point soft wizard cap|较短柔软尖冠配窄檐，帽尖塌落方式与高尖帽不同。
铃铛双尖舞台帽|bell-tipped jester cap|两个布尖从帽冠分出，每尖末端有小铃，布尖根部清楚。
高圆柱绒帽|tall cylindrical fur-style hat|高筒软毛帽冠、平整顶面和无檐底缘，绒毛表现为材质。
贴头护耳绒帽|close-fitting earflap cap|较低帽冠接长护耳片，绒边和下颌扣带独立。
巴拉克拉法头套帽|balaclava hood|一体布罩覆盖头颈，只留清楚面部开口，材质和颈缘可见。
包头软巾帽|wrapped-cloth headwear|布条绕头形成前额交叠和后部收尾，属于构造参考。
披肩连帽帽兜|capelet hood|完整帽兜连短肩披，面部开口、领缘和系结明确。
护颈雨帽|rain hat with neck flap|防雨圆帽冠与环檐，后部护颈片加长，接缝完整。
护镜飞行帽改编|aviator cap with goggles|贴头皮帽、护耳片与额前护镜，护镜带绕过帽身。
硬壳骑行帽|cycle helmet headwear|圆弧硬壳有透气孔，内衬、下颌带与后调节环可辨。
织藤斗笠改编|woven-rattan conical hat|较平锥形藤编帽体、内撑圈和下颌绳，编织纹理可见。
''',['帽子','帽型','帽饰','hat','headwear'])

block('bags','手提肩背与造型包','''
手提波士顿包|Boston-style handbag|横向弧顶包体、双短提手和顶部拉链，侧片厚度清楚。
弧顶保龄球包|bowling-shaped handbag|圆弧上顶配平底，宽侧片和双提手形成立体包身。
医生口金手提包|doctor-frame handbag|宽口金开合架撑住包口，皮包身和两侧折口可辨。
扣框贝壳包|shell-shaped clasp bag|上部弧形硬框与鼓起包体连接，中央扣具明确。
硬挺箱形手提包|structured box handbag|硬直侧壁、平底与翻盖，提手连接在加固顶缘。
翻盖琴谱包|music-folio satchel|扁长矩形包体、完整翻盖与提手，可装平面谱册。
手腕环带小包|wristlet pouch|小型拉链包侧接短腕环，环带根部和包口可見。
肩背法棍包|baguette shoulder bag|细长窄包体配短肩带，带根与翻盖扣明确。
软褶新月包|soft hobo bag|软包身向中央下垂，单肩带形成弧形轮廓，褶皱自然。
腋下矩形短带包|underarm rectangular bag|较扁矩形包体与短肩带，顶部开合和带根可见。
双提手梯形包|double-handle trapezoid bag|包体上窄下宽，两个提手从上缘加固片伸出。
单柄三角小包|single-handle triangular bag|三角包身有平整底边，顶端单柄和包口独立。
结绳手提小包|knotted-handle pouch|软包体的提带形成结扣，结的位置和袋口不同。
穿孔镂空托特包|perforated tote bag|大包体有规则穿孔，内层布袋与外层硬边分开。
口金钱夹小包|kiss-lock purse|扁小包体与金属口框，顶部两颗交叉扣头清楚。
透明展示手袋|transparent display handbag|透明外包体、独立内袋与提手，边框和口袋可辨。
''',['包','包包','包袋','手提包','bag'])

block('bags','背包行李与功能包','''
翻盖帆布双肩包|flap-top canvas backpack|翻盖压住束口，双肩带、侧袋和底部厚度可见。
卷口防水背包|roll-top dry backpack|包口卷折后用侧扣锁合，防水面片和肩带完整。
轻量抽绳双肩包|drawstring gym backpack|扁袋体靠两侧抽绳收口，绳同时形成双肩带。
单肩胸背包|sling chest bag|斜向单带配贴身小包体，扣具和前侧袋口明确。
双拉链小腰包|two-zip belt bag|前后两道独立拉链，腰带从两侧延伸并有扣具。
运动圆筒行李包|barrel sports duffel|横向圆筒袋、双提带和长肩带，圆端面可见。
周末旅行手袋|weekender travel bag|容量较大的软长包体、顶拉链和宽提手，底部加固明显。
伸缩拉杆行李箱|telescopic rolling suitcase|硬箱体、伸缩拉杆、轮组和侧提把，箱扣明确。
箱形硬壳背包|box-shell backpack|刚性箱形后壳接背带，后背软垫和开合缝分开。
挂颈手机小袋|neck-strap phone pouch|窄长小袋与挂颈带，翻盖或拉链及带根可见。
胸前证件小包|chest document pouch|扁小包有透明证件窗，短固定带和主袋口独立。
斜挎水瓶筒袋|crossbody bottle holder|圆筒袋包住瓶形轮廓，袋口束绳和斜肩带分开。
腰带模块工具袋|modular belt tool pouches|几个独立袋体挂在腰带上，背扣和袋口可拆连接明确。
斜挎书卷筒包|crossbody scroll tube bag|硬筒包体、可拆端盖与肩带，长卷收纳空间可辨。
网壳水桶包|net-shell bucket bag|网绳外壳包住布内袋，圆底和顶部抽绳独立。
法师卷轴背包|wizard scroll backpack|背包侧面接卷轴筒，书册翻盖和皮带扣固定清楚，原创幻想。
''',['包','包包','包袋','背包','行李','bag'])

block('military_outfits','军装礼服与常服改编','''
陆军翻领常服裤装|army-inspired service trouser uniform|绿色单排扣翻领外套、衬衣、领带和长裤，徽位留空；原创改编。
陆军翻领常服裙装|army-inspired service skirt uniform|翻领军装外套与膝下直裙，腰带、肩袢和鞋配合。
立领军装常服|standing-collar service uniform|高立领、直门襟与胸袋，长裤折线和靴完整。
短外套军装裤装|short-jacket service uniform|短军装外套配高腰长裤，前扣与胸袋比例清楚。
海军白色军装改编|white naval-inspired uniform|白色双排扣外套与长裤，深色领饰和帽带，原创无国别徽章。
海军深蓝军装改编|navy-blue naval uniform adaptation|深蓝双排扣长外套、直裤和制式帽轮廓，帽徽留空。
水手领军旅服|sailor-collar military-inspired attire|平直后领片与前胸领结，完整长袖上衣配宽裤。
空军蓝灰常服改编|blue-gray air-service uniform|蓝灰单排扣外套、衬衣和长裤，不画真实单位标识。
军装夏季短袖常服|short-sleeve summer service uniform|短袖有领军装衬衣、肩袢与胸袋，下配长裤。
军装冬季呢大衣|winter military overcoat|厚呢双排扣大衣、肩袢、腰带与长靴，衣摆完整。
仪仗长礼服军装|ceremonial long military coat|长礼服外套有对称滚边和原创礼绳，下配长裤与高靴。
军乐队礼服改编|military-band dress adaptation|装饰领襟、对称绳饰和明确袖口，采用原创纹样。
近代绳饰军装改编|historical braid-uniform adaptation|前胸横向绳饰、窄腰短衣和长裤，标注近代视觉改编。
军装披肩礼装|military capelet dress uniform|完整制服外搭短肩披，前系扣与内外层独立。
军装裙裤礼装|military culotte dress coordinate|军装上衣配宽腿裙裤，褶量和腰带可见。
晚间军装礼服|mess-dress-inspired uniform|短礼服外套、马甲与正式长裤，袖缘装饰简洁。
''',['军装','军服','制服','military uniform'])

block('military_outfits','作训勤务与架空军装','''
迷彩作训军装|camouflage field-uniform adaptation|原创迷彩上衣与工装长裤，胸袋、袖袋和膝部松量清楚。
素色野战军装|solid-color field uniform|素绿野战外衣、多袋长裤和靴，扣带少而明确。
丛林轻装军旅服|jungle field attire|轻布长袖衣裤、通风褶与多袋结构，装备固定在腰带。
沙漠轻装军旅服|desert field attire|浅色长袖作训服、护颈帽与靴，服装面片清楚。
冬季野战军装|cold-weather field uniform|厚夹层外衣、保暖长裤和护耳帽，活动关节留松量。
防雨军旅外装|military rainwear adaptation|带帽防雨外套罩住作训内层，门襟与袖口封合可見。
装甲车勤务连体服|armored-vehicle crew coverall|完整长袖连体服、前拉链和膝肘面片，头盔作为佩戴物。
军旅飞行连体服|military flight-coverall adaptation|长袖连体飞行服、拉链袋和装备环，不使用真实单位章。
海上勤务工作服|naval working-uniform adaptation|完整耐磨衣裤、工作靴和实用口袋，颜色分区克制。
通信勤务军装|communications-service outfit|作训衣裤外加小型通信设备袋，带具连接在腰胸固定点。
医疗勤务军装|medical-service field outfit|作训服配药箱肩袋与医护识别色块，服装与携行用品分区。
后勤工具军装|logistics tool-uniform adaptation|多袋工作军装配工具腰袋，袋口与带具用途明确。
架空空艇军官装|fantasy airship-officer uniform|硬领短外套、长裤与原创肩饰，仪表袋固定在腰侧。
架空星舰指挥装|original starship command uniform|未来制服有清楚领襟、设备接口和长裤，原创非真实军队。
架空卫队长军装|fantasy guard-captain uniform|翻领外衣、披风与护腕组合，礼绳和扣具都可追踪。
架空蒸汽军旅装|steampunk military-inspired outfit|复古军装剪裁与机械仪表腰袋结合，原创虚构徽形。
''',['军装','军服','作训服','军旅','military uniform'])
CATALOG[-1]['styles']=['steampunk']

block('wizard_outfits','巫师魔女服装结构','''
经典尖帽巫师长袍|classic pointed-hat wizard robe|高尖宽檐帽、完整长袍和束带，袍袖与内层衣清楚。
兜帽旅行巫师袍|hooded traveling-wizard robe|兜帽外袍、窄袖内衣和长裤，旅行袋固定在腰带。
短披肩魔女长裙|capelet witch maxi dress|短肩披罩住有袖长裙，尖帽与腰封形成完整剪影。
前开襟巫师外衣|open-front wizard coat|长外衣前开口露出完整衣裤，领襟和衣摆分片清楚。
双排扣巫师长衣|double-breasted wizard coat|交叠前片与双列扣具，长袖衣身配长裤，袍带不遮住扣位。
卷袖药草魔女装|rolled-sleeve herbal witch outfit|卷袖布衫、长裙和多袋短围裙，帽沿与工具袋明确。
口袋炼金巫师装|pocketed alchemist-wizard outfit|硬领衣、耐磨围裙与药瓶带，工具挂点落在加固处。
宽袖仪式巫师袍|broad-sleeve ritual wizard robe|宽袖长袍与完整内层，袖口留手部活动空间，纹样原创。
成人学院巫师服|adult academic wizard outfit|布衫、马甲与长袍外衣，成年研究者造型，无真实校徽。
星图占卜魔女装|star-chart diviner witch coordinate|有袖长裙、罩袍与星图腰袋，星纹按衣缘分区。
厚披风冬季魔女装|winter-cloak witch attire|厚披风、长袖衣裙和靴，尖帽采用柔软厚布。
拼补乡间巫师服|patchwork rural-wizard attire|补丁长袍、系结腰带与旧布软帽，补片接缝清楚。
哥特高领魔女服|gothic high-neck witch costume|高领蕾丝长裙、短肩披与尖帽，布层保持完整。
机械硬领巫师服|mechanical-collar wizard outfit|硬边高领、长外衣与仪表袋，软硬连接明确。
短披风巫师裤装|short-cloak wizard trouser outfit|短披风配窄袖衫长裤，袖手和腰部工具带开放可见。
扫帚旅行魔女服|broom-travel witch outfit|耐磨长外衣、长裤和短靴，扫帚背带作为原创携行装置。
''',['巫师','魔女','魔法师','法袍','wizard','witch'])
for e in CATALOG[-16:]:
    if '哥特' in e['name']:e['styles']=['gothic']
    if '学院' in e['name']:e['styles']=['dark_academia']
    if '机械' in e['name']:e['styles']=['steampunk']

block('wizard_outfits','巫师职业与幻想主题','''
冰霜保暖巫师袍|frost-wizard insulated robe|厚长袍、保暖帽与手套，冰晶纹位于外缘，内层完整。
风纹轻披巫师装|wind-wizard light-cloak outfit|多片轻披风配贴合袖衫长裤，披片固定点可见。
雷纹拼片巫师服|storm-wizard paneled outfit|多片硬边外衣罩住完整内层，原创光纹沿面片边缘排列。
潮汐防水巫师衣|tide-wizard water-resistant coat|防水长外衣、短下摆内裤装与筒形袋，袖口收束明确。
岩纹硬领巫师袍|stone-wizard rigid-collar robe|硬领和厚袍肩有石纹饰片，肘部仍为柔软布袖。
树皮层片魔女服|bark-layer forest-witch outfit|布长裙外叠树皮形软片，植物纹与衣料分区。
菌菇圆帽魔女服|mushroom-hat witch coordinate|圆顶宽沿帽配有袖叠裙，帽根和腰袋有明确连接。
花瓣领魔女服|petal-collar witch outfit|花瓣形领片搭配完整长裙，叶形饰件固定在衣缘。
月弧披领巫师服|moon-collar wizard ensemble|弧形披领、长袍和月纹法器袋，纹样不替代真实扣具。
日曜礼仪巫师服|solar ceremonial wizard outfit|对称金色衣缘、宽袖长袍和完整内衣，太阳纹为原创符号。
星轨夜行巫师服|star-trail night-wizard attire|深色长外衣、遮风肩披和腰袋，局部光纹保持节制。
梦境分层魔女服|dream-layer witch costume|半硬领罩衣与多层完整长裙，漂浮饰片有清楚承托设定。
骨纹守墓巫师服|bone-motif guardian wizard outfit|完整暗色长袍上缀骨形装饰，饰件是原创道具，不表现伤害场景。
沙舟游历巫师服|desert-travel wizard outfit|护颈软帽、松量长衣与长裤，水瓶袋和卷轴筒固定在腰背。
国风符术巫师服|Chinese-fantasy talisman wizard outfit|交领长衣、窄袖和分片外裙，符袋与卷轴为原创架空装置。
都市短衣魔女服|urban short-coat witch outfit|尖帽、短外套、完整布衫与长裤，传统巫师主题转成都市搭配。
''',['巫师','魔女','魔法师','法袍','wizard','witch'])
CATALOG[-2]['styles']=['chinese']

block('priestess_outfits','日本巫女装束参考与改编','''
白衣绯袴巫女装|white-hakui red-hakama miko attire|白色交叠领有袖上衣配红色长袴，腰系与白袜草履清楚；装束参考。
千早祭礼巫女装|chihaya-overlayer miko attire|白衣绯袴外罩轻薄千早，外层系结、袖缘和内层分别可辨。
花簪神乐巫女装|flower-headdress kagura miko attire|完整白衣红袴、祭礼外层和花簪，手持小舞具作为装束参考。
舞扇巫女服参考|fan-bearing miko attire study|白衣红袴与祭礼罩层，展开舞扇独立于宽袖，不混作衣摆。
宽袖白衣巫女服|wide-sleeve hakui miko study|宽长袖白衣与红袴，白衣下缘、腰绳和袖袋轮廓明确。
束袖勤务巫女改编|sleeve-secured working-miko adaptation|白衣红袴配背部交叉束袖绳，绳带收袖，不改变交叠领。
冬季加层巫女改编|winter-layer miko adaptation|完整白衣红袴内加保暖层，外衣体积较厚，标注角色改编。
历史巡行巫女改编|historical traveling-miko adaptation|短千早、红色袴与黑色笠、携行舞具，参考服饰博物馆案例改编。
短披肩巫女幻想服|capelet fantasy miko costume|白色袖衫、完整长袴与短肩披，明确为原创幻想装。
护腕旅装巫女服|travel-armguard fantasy miko outfit|完整交领袖衫与长袴，布护腕、腰袋和靴为架空旅行部件。
层叠袴巫女幻想服|layered-hakama fantasy miko outfit|完整长袴外加短层片，腰带和层片固定点清楚。
月纹千早巫女幻想服|moon-pattern fantasy chihaya outfit|千早式罩衣、完整长袴与原创月纹，区别于真实神社服制。
雪境长披巫女服|snowland fantasy miko attire|完整白衣、长袴和厚长披，寒冷场景层次为架空设计。
机关护片巫女服|mechanical-panel fantasy miko attire|完整巫女主题衣袴外有少量护片与仪表，原创机械混搭。
云纹仪式巫女幻想服|cloud-pattern fantasy miko costume|完整长袴、袖衫与云形肩领，纹样及配色均为原创。
街装长袴巫女混搭|urban hakama-miko hybrid|有袖短外套、完整内衫与长袴，成年都市幻想时尚改编。
''',['巫女','巫女服','神社装束','miko','shrine maiden'])

block('priestess_outfits','架空巫祝与女祭司','''
国风巫祝交领长衣|Chinese-fantasy ritualist wrap robe|完整交领长衣、宽束带和原创仪式挂袋，标注架空巫祝。
国风女祭司云肩装|Chinese-fantasy priestess cloud-collar attire|长袖长裙外加云形肩片，肩颈固定点和裙腰清楚。
国风舞祝披帛装|Chinese-fantasy ritual-dancer outfit|完整高腰衣裙配绕臂披帛，舞具与布带分开。
国风山林巫祝装|Chinese-fantasy forest ritualist attire|厚布交领衣、长裙和编织腰袋，植物饰件为原创设计。
国风星盘女祭司服|Chinese-fantasy astral priestess attire|直领叠袍、长裙与星盘携行架，仪式符号全部原创。
国风雪原巫祝袍|Chinese-fantasy snow ritualist robe|加厚长袍与完整内衣裤，毛边和腰系构造清楚。
国风水乡祭礼服|Chinese-fantasy riverside ceremonial outfit|袖衫、长裙和薄外披，水纹装饰位于边缘，不作为真实地方服制。
国风铜铃巫祝装|Chinese-fantasy bell ritualist outfit|完整交领衣裙外有小铃带，带具固定在腰侧，不替代衣身。
架空林地女祭司袍|original forest-priestess robe|布长袍和叶形披领，植物纹是虚构世界设定。
架空月殿女祭司服|original lunar-priestess attire|完整长袖礼袍、弧形肩披与月饰腰带，符号原创。
架空日殿女祭司服|original solar-priestess attire|完整礼袍采用金色滚边、长肩带与宽袖，装饰固定明确。
架空潮海女祭司服|original sea-priestess attire|完整长裙、波形披肩和贝形饰件，沿衣缝连接。
架空岩城女祭司服|original stone-city priestess outfit|厚布长衣与几何硬领，硬片不封住手臂活动。
架空风塔女祭司服|original wind-tower priestess attire|完整袖衫长裙外有多片轻披，飘带末端和固定点可追踪。
架空星舰仪式服|original starship ceremonial attire|未来高领长衣、完整长裤与光带，宗教体系为虚构设定。
架空机械女祭司服|original mechanical-priestess attire|完整长衣、硬边披领和仪表装置，机械和布层分开。
''',['巫女','女祭司','巫祝','祭礼服','priestess'])
for e in CATALOG[-16:-8]:e['styles']=['chinese']
for e in CATALOG[-16:]:e['reference_ids']=[]
for c in CATEGORIES:
    if c['id']=='bags':c['source_ids']=list(dict.fromkeys(c['source_ids']+['R33']))

for e in CATALOG:
    if e['category']=='wizard_outfits':e.setdefault('aliases',[]).append('女巫')
