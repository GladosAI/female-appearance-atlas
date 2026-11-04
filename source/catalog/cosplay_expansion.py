"""Edition 11: original cosplay role kits and visible wearable construction."""
from catalog_content import CATALOG, category, add

def block(key,dimension,text,aliases=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['aliases']=['Cosplay','cos','coser','角色扮演']+list(aliases)
        e['cosplay_reference']=True
        e['age_context']='成年角色Cosplay创作参考'

category('cosplay_outfits','Cosplay整套服装','原创角色原型套装，比较假发、衣物、装饰与道具的整套轮廓；服装本体与外挂件分辨。',['R61','R63'])
category('cosplay_looks','角色妆面与外观改造','成年脸部妆面和可穿戴外观件分列；图例着重外轮廓、标记位置和造型边缘。',['R61','R63'])
category('cosplay_wigs','假发与拼接造型','区分发套、发网、前额边缘、发片和造型结构；展示完整发束及其连接根部。',['R62'])
category('cosplay_headgear','角色头饰与面部道具','冠、帽、耳角、额框与面罩按完整物件观察；头箍、夹具、带具和头部定位明确。',['R61','R63'])
category('cosplay_accessories','角色身体装饰与外挂件','领肩、胸腰、四肢及背部尾翼外装分列；比较成对件、层次和安装位置。',['R61','R63'])
category('cosplay_props','角色手持与场景道具','魔法、日常、科幻与冒险道具，均为原创外观物件；观察手柄、环口、体积与携带结构。',['R61','R63'])
category('cosplay_build','穿戴固定与外装结构','扣件、连接带、底托、关节覆盖和可拆分外壳，以完成件及装配关系示意展示。',['R61','R62'])
category('cosplay_presentation','角色展示与动作','成年扮演者的站姿、手势、回望与道具呈现，优先保留服装、头饰和外挂件的可见关系。',['R63'])

block('cosplay_outfits','变身与舞台角色套装','''
星盘巡游者Cos套装|star-chart traveler cosplay kit|成年角色穿蓝白长袖齐膝层裙、 不透明连裤袜、短靴，双色短假发、星盘胸扣与长杖。
月环守望者Cos套装|moon-ring guardian cosplay kit|银灰长袖上衣与小腿长裙，半月额框、低盘假发和月环手持道具。
太阳舞台使者Cos套装|sun-stage envoy cosplay kit|橙金滚边高领短外套、膝下褶裙、长裤内搭，放射胸牌与太阳长杖。
铃兰花使Cos套装|lily-bell messenger cosplay kit|绿色连袖长裙、叶形肩片，波波假发、铃花腰坠及小花篮。
雪晶歌者Cos套装|snow-crystal singer cosplay kit|白蓝长袖小腿裙、层叠短披肩，白色外翘假发、雪晶冠与空白麦克风道具。
火羽演出者Cos套装|fire-feather performer cosplay kit|红黑长袖燕尾上衣与长裤，肩上扇形羽片、短红假发、羽形手扇。
蝶翼变身者Cos套装|butterfly transformation cosplay kit|紫色高领长袖膝下裙、 不透明紧身裤，双髻假发，背部小蝶翼与腰托连接。
水波礼仪者Cos套装|wave ceremonial cosplay kit|蓝绿长袖长裙、波纹腰带，长卷假发、额上水滴头饰和透明感空心圆杖。
糖果管弦者Cos套装|candy-orchestra cosplay kit|条纹长袖衬衣、短背带裙、 不透明裤袜，小圆帽、卷发假发和小琴盒。
时钟司仪Cos套装|clock-master-of-ceremonies kit|棕铜立领燕尾外套与长裤，时钟胸牌、单侧短假发、钟形手持道具。
云朵庆典者Cos套装|cloud-festival cosplay kit|奶白蓬袖齐膝衣裙与长裤，软云肩片、短卷假发、云形头箍及小旗。
流星舞台骑士Cos套装|meteor-stage knight cosplay kit|深蓝短外套和长裤，轻量星形肩壳、短束假发、泡沫圆钝道具剑。
哥特人偶长裙Cos套装|gothic-doll long-dress cosplay kit|黑紫高领长袖及踝裙，白蕾丝领边、卷发假发、小冠及可拆背部钥匙装饰。
镜面幻术师Cos套装|mirror-illusionist cosplay kit|黑银高领长外套与长裤，拼色长假发、菱形胸镜装饰和手持镜框。
丝带信使Cos套装|ribbon-messenger cosplay kit|米粉长袖衬衣、短层裙、 不透明裤袜，侧尾假发、短结饰和折页道具书。
机械音符偶像Cos套装|mechanical-note idol cosplay kit|青黑长袖短夹克、齐膝裙与长裤，耳机式头饰、双尾假发和琴键腕外壳。
''',('Cos服','cos服装','舞台角色','变身套装'))

block('cosplay_outfits','幻想与冒险角色套装','''
叶冠精灵旅人Cos套装|leaf-crown elf traveler kit|绿色长袖束腰外套与长裤，长耳外观件、辫尾假发、叶冠和肩背小包。
龙角守塔者Cos套装|dragon-horn tower-keeper kit|棕红长袍、宽腰带和长裤，泡沫角头箍、短假发、护肩与可拆尾件。
羽翼图书使Cos套装|winged library-messenger kit|米白长袖长裙、短披肩，背带装纸页翼、白色低髻假发与空白大书。
学院符文师Cos套装|academy-rune scholar kit|深棕长袖衬衣与膝下裙、长外袍，低马尾假发、抽象符文胸片与卷轴。
沙海护符旅人Cos套装|desert-talisman traveler kit|米色长袖罩袍与宽长裤，包头布、短编发假发、几何护符及水壶道具。
冰原披毛骑士Cos套装|ice-field fur-cape knight kit|蓝灰长袖长裤、仿毛肩披，白短假发、泡沫臂壳和圆盾道具。
森林弓手Cos套装|forest-archer costume kit|绿棕长袖短袍与长裤，贴头辫假发、软肩片、装饰箭袋和无发射功能弓形道具。
海港罗盘盗客Cos套装|harbor-compass rogue kit|蓝长外套、束腰背心与长裤，波浪假发、斜戴软帽、圆钝短刃和罗盘道具。
古堡烛灯旅人Cos套装|castle-lantern traveler kit|黑灰立领长裙、短披风，长直假发、尖拱领饰与无火烛灯。
蒸汽修械师Cos套装|steampunk mechanic kit|棕色长袖衬衣、背带长裤、皮色短围裙，侧编假发、齿轮肩饰与扳手道具。
蘑菇林旅者Cos套装|mushroom-grove traveler kit|红米长袖短斗篷、及膝裙与长裤，圆壳软帽、短卷假发与蘑菇形手杖。
花庭药草师Cos套装|garden-herbalist costume kit|浅绿长袖长裙、腰围裙，盘髻假发、植物胸饰、空瓶架与花草篮道具。
原创中性王子Cos套装|original androgynous-prince kit|成年女性穿高领滚边长外套与长裤，短层假发、小冠、肩绶带和圆钝礼仪剑道具。
星河圣殿旅人Cos套装|star-temple traveler kit|紫白高领长袍、窄腰带，双辫假发、星环肩饰和空心星杖。
纸扇云游者Cos套装|folding-fan wanderer kit|原创交叠领长袖外衣与宽长裤，低髻假发、小发冠和空白折扇，不标称古代服制。
齿轮长耳使者Cos套装|gear-eared messenger kit|铜绿长袖高领套装和长裤，机械长耳头饰、短假发、齿轮背板与信封道具。
''',('Cos服','cos服装','幻想角色','冒险角色'))

block('cosplay_outfits','科幻与机械角色套装','''
轨道航行员Cos套装|orbital-navigator cosplay kit|蓝白高领连体长裤服，短银假发、手持头盔道具、胸面板和假数据板。
轻壳机甲驾驶员Cos套装|light-shell mecha-pilot kit|灰黑长袖连体服，轻量分片肩胸壳、紫短假发、头侧通信装饰。
能源巡检员Cos套装|energy-inspector costume kit|橙灰工装上衣与长裤，腰侧假电源盒、短假发、腕面板和圆头检测棒道具。
仿生城市使者Cos套装|synthetic-city envoy kit|白色长袖长外套与长裤，拼色波波假发、半脸机械遮片与几何胸饰。
星舰礼仪官Cos套装|starship-ceremonial officer kit|深蓝高领长外套、长裤，银色短假发、空白肩章、胸带和圆形徽框。
透明罩壳观测者Cos套装|clear-dome observer kit|灰色长袖膝下罩衣与长裤，非密封透明感罩壳头饰、短假发及望远镜道具。
赛博夜巡者Cos套装|cyber-night-patrol kit|黑绿高领机能外套和长裤，双色侧削假发、护目镜、臂壳与假终端道具。
机翼背包飞行员Cos套装|wing-backpack pilot kit|棕蓝长袖连体长裤服，短假发、护目镜、背带机翼外装与腰盒。
未来实验室记录员Cos套装|future-lab recorder kit|米白长袖外罩与长裤，短蓝假发、透片胸饰、装饰试管架和电子板外观道具。
装甲信标守卫Cos套装|armored-beacon sentinel kit|黑灰长袖长裤底衣，泡沫胸肩膝壳、短假发、开放头冠和空心信标杖。
星尘舞台机器人Cos套装|stardust-stage robot kit|全覆盖灰银连体长裤服，关节分片外壳、短粉假发、耳侧圆盘与腰灯壳。
轨道快递者Cos套装|orbital-courier costume kit|青灰短外套与长裤，长侧尾假发、软头盔饰、斜背包与条形箱道具。
水域机械研究员Cos套装|aquatic-mechanical researcher kit|蓝黑高领长袖长裤服，鳍形肩片、短假发、开口眼罩与鱼形探测器道具。
方盒机偶管理者Cos套装|box-robot caretaker kit|浅黄长袖工装与长裤，短卷假发、箱形肩托、空白腕屏和小机偶道具。
星图投影师Cos套装|star-projection designer kit|紫灰长袖长外套与长裤，波浪长假发、几何额框、半透明星盘道具。
白壳太空骑士Cos套装|white-shell space-knight kit|黑色长袖长裤底衣，白泡沫分片胸肩腿壳、短假发、圆钝光剑外观道具。
''',('Cos服','cos服装','机甲Cos','科幻角色'))

block('cosplay_outfits','都市与主题职业角色套装','''
双领侦探Cos套装|double-collar detective kit|灰格长风衣、衬衣与长裤，侧分短假发、空白侦探牌、放大镜道具。
夜宴怪盗Cos套装|evening-masquerade rogue kit|白黑燕尾套装与长裤，短卷假发、小眼罩、帽饰及空白卡牌道具。
巡回咖啡师Cos套装|traveling-barista character kit|棕白长袖衬衣、长裤与腰围裙，短卷假发、布结领饰和空杯道具。
机械维修女仆Cos套装|mechanic-maid character kit|黑白长袖小腿裙、工具腰围裙，短假发、小蕾丝头饰和假工具包。
幻想城市邮递员Cos套装|fantasy-city postal character kit|绿灰滚边短外套与长裤，侧辫假发、原创空白帽徽、信包与信封。
赛车维修队员Cos套装|racing-pit crew character kit|白蓝长袖工装连体长裤，短假发、耳机道具、腰包与圆头扳手道具。
月夜马戏司仪Cos套装|moon-circus master kit|红黑燕尾长外套、背心与长裤，高帽、短假发、星链胸饰与软短杖。
海边音乐家Cos套装|seaside-musician character kit|蓝白长袖上衣、膝下裙与长裤，长辫假发、贝壳领饰及原创小琴道具。
纸牌游戏裁判Cos套装|card-game referee character kit|紫黑长袖马甲套装与长裤，平直波波假发、几何领结、空白卡框道具。
朋克乐队鼓手Cos套装|punk-band drummer kit|格纹长袖衬衣、拼片马甲与长裤，蓬松短假发、铆钉腰带及软鼓棒道具。
魔法糕点师Cos套装|magical-pastry chef kit|米粉长袖厨师外套、长裤及前围裙，短卷假发、软圆帽与假糕点盒。
星光广播员Cos套装|starlight-broadcaster kit|蓝紫长袖西装、长裤，长尾假发、星形胸扣、耳机和空白麦克风道具。
花市拍卖师Cos套装|flower-market auctioneer kit|奶绿长袖长外套与膝下裙、长裤，盘发假发、花胸饰与圆头小槌道具。
城市怪兽照护员Cos套装|city-creature caretaker kit|卡其长袖工作上衣与长裤，短辫假发、小尾形胸扣和原创小布偶道具。
架空法庭书记Cos套装|fictional-court clerk kit|深灰高领长袖外套与长裤，后梳短假发、空白胸牌、卷宗夹和羽笔道具。
灯塔故事讲述者Cos套装|lighthouse-storyteller kit|深蓝长袖小腿裙、短肩披，长卷假发、灯形吊饰、空白书与无火灯笼。
''',('Cos服','cos服装','都市角色','职业角色'))

block('cosplay_looks','妆面轮廓与原创标记','''
平直英气眉角色妆|straight-brow character makeup|成年正脸，平直眉与短外眼线、低饱和唇，妆面而非天然脸型分类。
上挑细眉舞台妆|lifted fine-brow stage makeup|成年正脸，细眉略上挑、外眼角线抬起，左右轮廓对照清楚。
圆弧柔眉角色妆|rounded soft-brow character makeup|成年正脸，圆弧眉、圆眼外框线和自然唇色，妆面边缘清楚。
宽尾刀形眉角色妆|wide-tail angular-brow makeup|成年正脸，宽眉尾与折角眼线，明确画出的几何边缘。
短尾猫眼角色妆|short-wing cat-eye makeup|成年脸部，眼线外尾短且尖，瞳孔与虹膜保持正常可见。
长尾双线角色妆|long-wing double-line makeup|成年脸部，外眼角两条独立平行眼线，眼线不代替眼睛。
下眼睑点线角色妆|lower-lid dot-and-line makeup|成年脸部，下眼外侧短线与小点，正常眼形保留。
单侧彩线眼妆|one-sided colored-line makeup|成年正脸，仅一眼外侧有彩色短线，另一侧自然，非伤痕。
双色对称眼影妆|two-color symmetric eye makeup|成年正脸，两眼上方各有同样两色区，边界与眉眼位置明确。
哑光深唇舞台妆|matte dark-lip stage makeup|成年正脸，深色哑光完整唇面，眉眼清楚，非裂口或伤口。
柔渐层唇角色妆|soft gradient-lip character makeup|成年正脸，唇内深外浅，正常唇轮廓完整，不改变嘴部解剖。
星点颊面角色妆|star-dot cheek character mark|成年正脸，一侧颊有原创小星与两点，平面彩绘清楚。
额心菱形角色标记|forehead diamond character mark|成年额心原创菱形彩绘，四角清楚、眉眼不遮挡。
双颊短条角色标记|paired cheek-bar character marks|成年双颊各两条短彩绘，对称位置和条宽可辨。
额侧弧线角色标记|temple-arc character mark|成年额侧一条原创细弧线与节点，平面妆纹而非裂纹。
科技半脸妆面分区|tech-themed half-face graphic makeup|成年正脸一侧原创几何淡色块和细线，另一侧正常，非真实机械植入。
''',('角色妆容','Cos妆','cosplay makeup','脸部妆面'))

block('cosplay_looks','可穿戴局部外观件','''
短尖耳壳外观件|short pointed-ear costume shells|成对浅色耳壳产品，旁有成年耳部佩戴定位，尖端短、壳边和耳口清楚。
长尖耳壳外观件|long pointed-ear costume shells|成对长尖耳壳，三分视图与成年侧头定位小图，佩戴边缘明确。
鳍形耳罩外观件|fin-shaped ear covers|成对鳍形耳罩，分片鳍边与后部固定环，附成年头部小定位图。
圆鼓耳套外观件|rounded ear-cap costume pieces|成对圆鼓软耳套，内侧耳口与外形厚度分开，成年定位小图。
双片眉骨造型外观件|paired brow-ridge costume pieces|完成的浅色眉上造型片，前侧与背面边缘，成年额部定位示意，无施作过程。
小额脊造型外观件|small forehead-ridge costume piece|原创短额脊软片，有独立薄边，产品与成年额头完成佩戴小图。
颊侧鳞片装饰贴|cheek-scale decorative pieces|原创少量薄鳞片有圆角，产品与成年脸颊完成佩戴小图，正常皮肤。
鼻梁几何软遮片|soft geometric nose-bridge cover|原创薄几何鼻梁罩片，完整边缘与成年脸部定位，非真实改造。
眼外短羽装饰片|short feather temple pieces|原创小羽片固定在额侧带上，眼睛不遮挡，产品与成年侧头示意。
下颌软甲遮片|soft jaw-armor cover|原创软分片覆在下颌外侧，薄边与耳后带可见，嘴鼻保持开放。
半脸机器人面片|half-face robot costume cover|完整半脸外装面片有眼口开口及耳后带，附成年佩戴小图。
颈侧鳃纹装饰片|neck-side gill-motif decoration|原创扁平弧线软片贴在成年颈侧完成外观，皮肤完整、衣领可见。
手背鳞纹软罩|scale-pattern hand-back cover|原创软罩覆盖成年手背，五指正常，腕端布带与边缘可见。
前臂树皮纹软罩|bark-texture forearm costume cover|原创树纹软罩套成年前臂，接缝与袖缘，正常手臂保留。
膝侧晶片外观件|knee-side crystal costume pieces|原创圆角晶片安装在膝侧布带上，灰色成人腿模定位，不画植入。
小腿兽纹外罩片|animal-pattern lower-leg costume covers|成对软罩片覆成人灰腿模小腿，背部带具与完整鞋边，非真实兽肢。
''',('外观改造','耳壳','妆面道具','可穿戴外观件','costume prosthetic'))

block('cosplay_wigs','发套基础与可拆发片','''
短波波基础假发套|short bob base wig|灰色成人头模上的完整短假发，旁放翻面小图，帽底和发帘根清楚。
长直发基础假发套|long straight base wig|灰头模到腰架，完整长假发发尾，内侧帽底小图，原产品造型。
卷发基础假发套|curly base wig|成人灰头模，卷发层与内帽底小图，发卷不遮掉套口。
露耳短层假发套|ear-revealing layered wig|成人灰头模短层假发，露耳轮廓、后颈发尾和帽边小图。
前额薄网假发边缘|lace-front wig edge reference|完整成人头模假发，前额薄网边小放大图，与发束根部连接清楚。
中央分缝假发顶|center-part wig crown|成人灰头模顶前视图，中分发缝与发帘走向，内侧小图。
可调后扣假发帽底|adjustable-back wig cap|翻面的完整假发帽底，后部调节带、挂扣与松紧边，外发套小图。
缝帘排布假发帽底|wefted wig-cap layout|完整翻面帽底上平行发帘根，弹性连接带与边圈，发束小样。
单条补量发帘|single volume-addition weft|完整发帘根带和垂下发束，头模上一小段连接位置示意。
夹式短刘海发片|clip-on short fringe piece|独立刘海发片有后夹，成人灰头模额前安装小图，夹与发帘分开。
双夹侧发片|two-clip side hair piece|长侧发片有两枚背夹，头模侧面小定位，发根连接清楚。
夹式长马尾件|long clip-on ponytail|独立完整长尾发件，根部抓夹与头模侧后安装小图，发尾不裁切。
抽绳收口马尾件|drawstring ponytail piece|发件根部收口网袋、抽绳扣和尾束，完整产品与安装小图。
盘髻包罩假发件|bun-cover hair piece|圆盘髻发件底有网罩口与小扣，成人头模后侧定位。
编辫加长假发件|braided extension hair piece|完整一根长编辫，顶端夹件与头模后侧小定位，辫尾可见。
双色拼接假发套|two-color spliced wig|成人灰头模上的左右双色发套，内侧分区发帘根部小图。
''',('假发','发套','发片','假毛','wig','wig cap'))

block('cosplay_wigs','戏剧造型与支撑轮廓','''
扇状尖束造型假发|fan-spiked styled wig|灰色成人头模上五束扇状尖发束，根部连贯，完整帽外轮廓。
后梳尖峰造型假发|swept-back peaked wig|灰成人头模上发束向后梳出三角尖峰，前额与帽根相连。
硬弧前刘海假发|rigid-curved fringe wig|成人灰头模前刘海形成一个清楚弧面，帽体与弧形发束连续。
大侧卷造型假发|large side-roll wig|成人灰头模两侧各一大卷，卷口与发根固定点可见。
双圆髻长尾假发|twin-round-bun long-tail wig|成人灰头模到腰架，两个圆髻各垂一条长尾，结构与发尾完整。
双角髻造型假发|twin horn-bun wig|成人灰头模顶部两个发髻形成向上弧角，均由头发造型，非真角。
高环发髻造型假发|high loop-bun wig|成人灰头模后侧三分视图，后发收成一个高环，环口与根部清楚。
前后双层髻假发|front-back double-bun wig|成人灰头模后侧，两髻前后错层，各有独立固定根。
冠状盘辫假发|crown-braid styled wig|成人灰头模上发辫沿头顶成冠圈，真实编发与帽根可辨。
超长粗辫假发|extra-long thick-braid wig|成人灰头模到臀架，一根粗长辫与完整束尾，长度可见。
分段球尾假发|segmented bubble-tail wig|成人灰头模到腰架，马尾有五个发束球段，扎点和尾端。
浮弧侧尾支撑假发|supported arched side-tail wig|成人灰头模到腰架，单侧尾有内支撑形成大弧，发尾自然向下。
外翻扇尾造型假发|outward fan-tail wig|成人灰头模后侧，一条高尾末端展开扇形，根部与展开端清楚。
异色内层挑束假发|contrast-underlayer styled wig|成人灰头模，外层深色内层浅色仅在几束外翻处显露，结构清楚。
辫网盘髻造型假发|braid-lattice bun wig|成人灰头模后侧，几条编辫交织覆盖圆髻，交叉层次可辨。
悬环结带造型假发|loop-and-ribbon styled wig|成人灰头模后侧，实际发束环髻与独立布带结分开，完整假发造型。
''',('假发','造型假毛','造型假发','styled wig'))

block('cosplay_headgear','冠帽耳角与面部框饰','''
几何尖冠Cos头饰|geometric pointed cosplay crown|原创轻量圆冠三尖，内衬、后部小带与完整底圈，成人头模小定位。
双弧小冠Cos头饰|double-arch cosplay tiara|原创两个不等高弧形饰面接细头箍，连接根与内圈。
悬环额框Cos头饰|floating-ring forehead frame|原创圆环接两侧头箍支杆，环在额上方，支杆与成年头模定位小图。
月牙横额Cos头饰|crescent forehead cosplay ornament|原创横月牙接弹性额带，两端后扣与完整月形。
羽扇侧冠Cos头饰|side-feather fan headpiece|原创轻量扇羽饰面固定在侧梳底座，梳齿和羽根可见。
花角结合Cos头箍|flower-and-horn cosplay headband|原创一对短弧泡沫角与少量布花接硬箍，角根底托清楚。
长耳夹座Cos头箍|long-ear mounted cosplay headband|原创一对长耳道具接两个夹座，头箍、耳片前后面和夹座。
可换猫耳Cos头箍|interchangeable cat-ear headband|原创猫耳从头箍小插座取下一个，三角耳片与插口可见。
折片兔耳Cos头箍|folded-panel rabbit-ear headband|两片长耳以软折线造型，硬箍和耳根连接明确。
双侧机械耳盘Cos饰|paired mechanical ear-disc headpiece|原创两侧圆盘由头顶弧带连接，盘厚、耳侧底垫与成年人定位小图。
开面薄壳Cos头盔|open-face thin-shell cosplay helmet|原创轻壳头盔留完整面口，内衬和下颌带，非真实防护装备。
猫轮廓半脸Cos面罩|cat-outline half-face costume mask|原创上半脸罩有猫耳轮廓、双眼孔、侧带与内边，非现成角色。
长鼻舞台Cos面具|long-nose stage costume mask|原创圆钝长鼻面具、眼孔与头带，展示完整侧厚。
钟面小帽Cos头饰|clock-disc miniature cosplay hat|小平顶软帽上原创钟盘，底部夹与短带清楚，无数字标识。
书页羽笔Cos帽饰|page-and-quill cosplay hat ornament|原创小帽外装书页片与羽笔形饰，夹具、页根与帽底。
晶簇额冠Cos头饰|crystal-cluster forehead crown|原创圆角晶片簇接细弧底架，后带与成年人定位小图。
''',('Cos头饰','头冠','兽耳','头盔道具','headpiece'))

block('cosplay_accessories','领肩胸腰与肢体装饰','''
立体星领Cos饰件|star-shaped cosplay collar|原创宽领片前有星形低浮雕，后扣与内衬，产品完整。
波瓣领缘Cos饰件|wave-petal cosplay collar|原创波瓣围领由软片叠接，完整后部带与领口。
三层软肩Cos饰件|triple-layer soft cosplay pauldrons|成对软肩片三层错开，内侧肩带与上臂带，产品侧厚可见。
扇羽单肩Cos饰件|single feather-fan pauldron|原创单肩扇羽片，底托和肩下布带，羽根不悬空。
齿轮胸盘Cos饰件|gear chest-disc ornament|原创圆盘周围短齿、背面挂片和肩带接口，完整产品。
几何胸绶Cos饰件|geometric chest-sash ornament|原创布绶带串三块几何片，斜向带路和后扣可见。
结带腰封Cos饰件|bow-front cosplay waist wrap|原创宽布腰封与前结，两短尾、后部闭合结构。
分片腰甲Cos饰件|panelled cosplay hip armor|三块轻量片接同一腰带，片间有活动空隙，非真实护甲。
长裙外叠腰饰Cos件|over-skirt waist drape piece|原创前后叠布片接腰带，完整垂片、扣与内裙人台小图。
对称腕甲Cos饰件|paired cosplay wrist shells|成对圆角泡沫腕壳，内侧布带与开口，成人灰手模小定位。
尖角袖口Cos饰件|pointed cuff costume ornaments|成对圆钝三角袖边片装在袖口带上，袖口孔与扣件。
指背连片Cos手饰|finger-back panel hand ornaments|成人灰手模正常五指，各指背小片以软布连到腕带，关节间留空。
鞋面覆盖Cos饰件|cosplay shoe-upper covers|成对普通鞋外覆原创几何软片，鞋底边和背面固定带可见。
长靴外罩Cos饰件|cosplay boot-cover shells|成对小腿靴罩前片与后带，下方普通鞋小示意，整件至膝下。
小腿分片Cos饰件|segmented shin costume pieces|成对原创泡沫胫片，每片有后部带具与圆角，成人灰腿模小定位。
肩腰连接飘带Cos件|shoulder-to-waist ribbon decoration|原创飘带一端接肩片另一端接腰扣，产品展开展示两端与带路。
''',('Cos装饰','Cos配饰','腰甲','腕甲','costume accessory'))

block('cosplay_accessories','背部尾翼与大型外挂','''
分片蝶翼背饰Cos件|panelled butterfly-wing costume attachment|原创左右蝶翼片接背部小底板，背带与翼根清楚，产品完整。
折页书翼背饰Cos件|folded-page wing costume attachment|两侧纸页造型翼片接同一背板，层数、翼根和肩带。
骨架羽翼背饰Cos件|framed feather-wing costume attachment|左右轻量羽片覆在可见骨架上，背板、肩腰带与外翼端。
短鳍肩背Cos件|short-fin back costume attachment|原创四块短鳍接背板，鳍厚与背带，非生物骨骼。
晶簇背板Cos饰件|crystal-cluster backplate costume piece|原创圆角晶片簇安装背板，背面肩带与前侧簇根。
圆盘悬环背饰Cos件|ring-disc back costume attachment|原创大环用两根短杆连接背板，杆、内孔和背带清楚。
机翼背箱Cos件|winged costume backpack shell|原创轻量箱壳两侧有短翼，箱背肩带和腰带，完整展示。
软壳兽尾Cos件|soft animal-tail costume piece|原创软毛尾有完整末端，根部腰带挂环与底托，非真实身体尾巴。
分节机械尾Cos件|segmented mechanical-tail costume piece|原创圆角分节尾壳，根部腰带与连续内带，尾端不裁切。
扇形多尾Cos件|fan-arranged multiple-tail costume piece|三条原创软尾通过扇形底托接腰带，三个根与完整尾端。
鱼尾裙外挂Cos件|fish-tail skirt costume attachment|原创鱼尾形软片挂在完整长裙后腰，腰扣与裙底人台小图。
蝴蝶肩披Cos件|butterfly shoulder-cape attachment|原创短软披风呈左右蝶形边，领口、胸扣与完整边缘。
甲壳后背Cos件|shell back costume attachment|原创轻壳分左右两叶接背板，中央缝与背带，成人轮廓小定位。
触须边裙Cos件|tentacle-edged skirt costume attachment|原创软触须造型挂在外裙下沿，内层完整不透明裙，圆钝末端。
环绕星带Cos背饰|orbiting star-band back attachment|原创两条弧带挂在背板短支杆上，小星片与固定根，完整物件。
提线人偶背框Cos件|puppet-string back-frame costume piece|原创轻背框上有短悬装饰线，线接肩腰外饰，不连接真实人体关节。
''',('Cos装饰','背饰','翅膀道具','尾巴道具','costume attachment'))

block('cosplay_props','魔法日常与舞台手持','''
星窗短杖Cos道具|star-window short cosplay wand|原创圆钝短杖顶有空心星框，手柄、顶框连接和完整末端。
月环长杖Cos道具|moon-ring long cosplay staff|原创轻量长杖顶接月环，完整杆长、分节接口与下端圆钝帽。
开页符文书Cos道具|open-page rune-book prop|原创空白开页书壳，封皮厚度、页边与几何印花，不含文字。
圆筒卷轴Cos道具|cylindrical scroll prop|原创软卷轴两端短杆，中间空白卷面展开，轴与面接点。
手持透明星盘Cos道具|handheld transparent star-disc prop|原创半透明圆盘有抽象星点，侧手柄与盘边厚度。
无火提灯Cos道具|flameless cosplay lantern|原创小灯笼形空壳，提环、支架与底座，内部仅装饰光点。
圆框手镜Cos道具|round-frame costume hand mirror|原创圆框镜面与短柄，背面几何装饰小图，边缘圆钝。
花枝小篮Cos道具|flower-branch basket prop|原创小篮装布花枝，篮柄与篮体编纹，整个物件可见。
空白卡牌束Cos道具|blank-card fan prop|几张原创空白卡呈扇形展开，圆角卡边，不含现成游戏角色。
折扇画面Cos道具|folding-fan costume prop|原创扇面简化云枝，扇骨、枢轴与扇口完整，无文字。
琴形手持Cos道具|small instrument-shaped costume prop|原创小竖琴外形，完整框体与装饰弦线，完整握持边。
空白麦克风Cos道具|blank microphone costume prop|原创短柄与网状罩头，完整外观，无品牌或电气结构说明。
齿轮钥匙Cos道具|gear-key costume prop|原创大型钥匙形轻量道具，齿轮环柄、短杆与圆角齿。
羽笔卷宗Cos道具|quill-and-folder costume props|原创羽笔形饰件与空白卷宗夹成套，夹脊与笔尾完整。
布偶伙伴Cos道具|original plush companion prop|原创小长耳布偶，完整四肢与底部抱持带，非现成角色。
假糕点展示盒Cos道具|faux-pastry display box prop|原创开盒内三枚普通假糕点，盒盖连接和提带，非真实食品推荐。
''',('Cos道具','手持道具','魔法道具','cosplay prop'))

block('cosplay_props','冒险科幻与大型道具','''
圆钝泡沫长剑Cos道具|blunt foam sword costume prop|原创轻量泡沫长剑，圆钝剑尖与护手、握柄，非真实武器。
短护手礼剑Cos道具|short-guard ceremonial sword prop|原创圆钝礼剑道具与空鞘，护手、握柄和挂环完整。
无弦弓形Cos道具|unstrung bow-shaped costume prop|原创弓形外壳不装发射弦，手握中段与完整上下弧端。
轻壳圆盾Cos道具|light-shell round shield prop|原创圆盾外壳、边圈和背面软握带，正背两视图。
圆头锤形Cos道具|round-headed hammer costume prop|原创轻量大锤头圆角，手柄、假金属涂装与完整下端。
软刃镰形Cos道具|soft-edged scythe-shaped prop|原创圆钝软刃接轻量长柄，柄接口和完整上下端，非武器制作图。
空箭袋背携Cos道具|empty costume quiver prop|原创空袋有背带、袋口与底部，无真实箭或发射器。
科幻臂炮壳Cos道具|sci-fi arm-cannon shell prop|原创空壳大孔与腕托、后臂带具，非功能武器，不含内部机构。
科幻扫描棒Cos道具|sci-fi scanning-rod prop|原创短棒头有透明感罩，握柄与装饰屏面，无真实探测功能。
空白数据板Cos道具|blank data-tablet costume prop|原创方形板面深色空白窗，侧握把与完整外壳边。
假通信终端Cos道具|faux communication-terminal prop|原创手持小盒有装饰按钮、短圆天线，无实际电子线路。
能源晶匣Cos道具|energy-crystal case prop|原创透明感空匣内圆角假晶体，框、提把与合页，完整箱体。
折分长杖外壳Cos道具|sectioned staff-shell costume prop|原创长杖外壳分两段并列，套接头与完成外形小图，非加工说明。
开合宝箱Cos道具|opening treasure-chest prop|原创轻量小宝箱，空腔、合页、搭扣和提带完整。
罗盘望镜Cos道具组|compass-and-spyglass prop set|原创无字罗盘圆壳与短望镜外形，完整两件和携带绳。
圆框大型时钟Cos道具|large clock-frame costume prop|原创圆壳空白刻度盘、装饰双针与侧把手，完整正面和侧厚。
''',('Cos道具','泡沫道具','科幻道具','大型道具','costume prop'))

block('cosplay_build','扣件带具与连接底托','''
按扣布片外装连接|snap-tab costume attachment|两块布片用一对按扣相接，分离与扣合小视图，布边完整。
双环织带外装连接|double-ring webbing costume connector|短织带穿双D形环再回折，带路与缝合端明确。
插扣腰带外装连接|side-release buckle costume belt|完整织带腰环、侧插扣分离两半和后段滑扣，物件示意。
钩环搭片外装连接|hook-loop tab costume connector|两片软布搭接，毛面与钩面小局部，完成佩戴边缘示意。
磁扣小饰件底托|magnetic ornament mount|原创小饰件与两块圆磁扣底托分件，薄布夹层明确，不作承重指南。
夹口胸饰固定座|clip-back chest ornament mount|原创饰件背有弹簧夹，侧厚、夹口与衣物边小定位图。
穿杆发饰固定座|rod-through headpiece mount|原创小饰板由圆钝杆穿孔，头模假发小定位，孔与杆分件。
头箍耳角插座|headband ear-horn socket|完整硬头箍有两个小插座，一个短角取下，插口和底托。
肩带背板连接座|shoulder-strap backplate mount|原创背板配双肩带，带孔、回折缝和中心外装插槽。
腰带尾件连接座|belt-mounted tail socket|原创腰带中心小底托接软尾根，分件与完成小图，腰扣完整。
裙片扣带连接座|buckle-tab overskirt mount|两块原创外裙片用短扣带接腰带，片根、扣和整体人台小图。
鞋底绕带外罩连接|under-sole strap boot-cover mount|原创软靴罩通过绕鞋底短带相接，普通鞋底、带路及罩口。
腕甲短带连接座|short-strap bracer mount|原创圆角腕壳内侧两条短带与小扣，成人灰腕模定位。
腿壳双带连接座|two-strap shin-shell mount|原创腿壳背有上下两带，各有扣件，成人灰腿模小定位。
扇翼背框连接座|fan-wing back-frame mount|原创小背框两个短插槽接左右翼根，双肩腰带完整。
挂环道具携带座|loop-ring costume-prop holder|原创腰带挂环与短带托住圆钝小杖，挂环、杖根和后扣可见。
''',('穿戴固定','固定扣件','带具','道具固定','costume mount'))

block('cosplay_build','外壳关节与拆分结构','''
泡沫肩壳分片外装|segmented foam shoulder shell|原创肩壳三片错叠，软内带把片相连，圆角片边和底托完整。
胸壳侧开外装|side-opening chest shell|原创成人灰衣人台上薄胸壳，两侧短扣带，正背小视图，非防护结构。
背板开槽外装|slotted costume backplate|原创薄背板两个插槽与完整带具，取下的翼根小件和槽方向。
肘关节留空外装|elbow-gap costume armor|成人灰袖人台上上臂壳与前臂壳分离，肘弯处留活动空隙。
膝关节分片外装|segmented knee costume armor|成人灰裤腿人台上膝片与胫片分开，连接软带及弯曲小图。
手指关节短片外装|short finger-joint costume shells|成人灰手模五指正常，指背短壳在关节处留间隙，腕带相连。
软芯尾壳分节外装|soft-core segmented tail shell|原创分节尾壳串在连续软带上，根部挂环与完整尾端。
翼膜骨架分件外装|wing-membrane frame costume parts|原创翼片薄膜与轻骨架分件并列，边界和背板接口，无工具。
半透晶簇壳外装|translucent crystal-cluster shell|原创圆角晶簇轻壳，背面空腔与底托，不画真实矿物锋边。
装饰光窗空壳|decorative light-window costume shell|原创小盒壳正面透片窗、后盖与布带，内部空白，无接线图。
拼接长柄道具外壳|section-joint long-handle prop shell|原创圆钝长柄分两段，短套接口与完整拼合小图，外观装配示意。
可拆帽冠饰面|removable crown-panel assembly|原创冠底圈与多片饰面分件，插口、薄边及合体小图。
分离面罩头带外装|separate mask-and-headband assembly|原创半脸面罩、弹性头带和两侧挂环，分件与完成小图。
折叠软翼收拢外装|folding soft-wing costume assembly|原创软翼通过中部软连接折合，展开和收拢两状态，背带可见。
胸腰叠层外装拆分|chest-waist layered costume assembly|成人灰人台外套、胸饰与腰饰三层分件并列，完成叠穿小图。
完整Cos套装平铺分件|complete cosplay-kit flat lay|原创上衣、长裤、假发套、头饰、腕片与短杖平铺，各件独立清楚。
''',('外装结构','外壳','拆分','泡沫外装','costume assembly'))

block('cosplay_presentation','站姿手势与道具呈现','''
正面角色识别站姿|front character-identification pose|成年女性穿原创长袖高领膝下裙与长裤，双手自然下垂，头饰胸饰和鞋完整。
侧身肩饰展示姿|side shoulder-ornament display|成年女性穿原创长袖长裤Cos服，侧身自然站，肩片侧厚与假发尾可见。
背面尾翼展示姿|rear costume-tail-and-wing display|成年女性穿原创长袖长裤，背面站姿，背板、两软翼、软尾根与鞋完整。
三分身轻回望姿|three-quarter turn-and-look pose|成年女性穿原创长袖小腿裙与长裤，身体轻转回望，长假发与裙层完整。
双手身前托书姿|both-hands book presentation|成年女性穿原创长袖长袍与长裤，双手托空白开书，握持与手指自然。
单手持短杖展示姿|one-hand short-wand presentation|成年女性穿原创长袖齐膝裙与长裤，一手持圆钝短杖，杖不遮脸，另一手自然。
长杖侧立展示姿|staff-beside-body display|成年女性穿原创长袖长袍与长裤，长杖轻靠地面在身体侧，完整杖与支点。
手镜抬至肩侧姿|hand-mirror shoulder-side pose|成年女性穿原创长袖小腿裙与长裤，手镜在肩侧，脸不遮挡，另一手自然。
提灯低位站姿|low-held lantern pose|成年女性穿原创长袖外套与长裤，提无火灯在腰侧，灯环握持和地面支点。
折扇半开呈现姿|half-open fan presentation|成年女性穿原创交叠领长袖长衣与长裤，半开扇在胸侧，头与扇面均可见。
圆盾侧托展示姿|side-held round-shield presentation|成年女性穿原创泡沫肩壳与长袖长裤底衣，圆盾在侧，背面握带关系清楚。
圆钝剑垂持展示姿|blunt-sword downward display|成年女性穿原创长袖长裤骑士Cos服，圆钝道具剑朝下，握柄、护手与鞋完整。
小伙伴双臂抱持姿|plush-companion holding pose|成年女性穿原创长袖上衣与长裤，双臂抱原创小布偶，人物头饰与布偶轮廓分开。
坐姿裙层整理展示|seated layered-costume display|成年女性穿原创长袖及踝裙，直坐凳上，手放膝上，裙层与完整鞋，普通展示姿。
单手致意展示姿|one-hand greeting display|成年女性穿原创高领长袖外套与长裤，一手掌心向外致意，正常五指与脸可见。
双手展开外披展示|open-cape costume presentation|成年女性穿原创长袖长裤底衣，双手轻展开短披两边，内衣物完整覆盖，站姿自然。
''',('角色展示','Cos姿势','角色动作','cosplay pose'))

STYLE_TAGS={
    '哥特人偶长裙Cos套装':['gothic'],
    '学院符文师Cos套装':['preppy','dark_academia'],
    '古堡烛灯旅人Cos套装':['gothic'],
    '蒸汽修械师Cos套装':['steampunk'],
    '赛博夜巡者Cos套装':['techwear','cyberpunk'],
    '朋克乐队鼓手Cos套装':['punk'],
}
for e in CATALOG:
    if e['name'] in STYLE_TAGS:e['styles']=STYLE_TAGS[e['name']]

# Actual illustrated variants retain their source generation prompts.
for e in CATALOG:
    if e['name'] in ['糖果管弦者Cos套装','丝带信使Cos套装']:
        e['note']='图例采用短层裙与不透明裤袜；需要膝下版本时可延长下摆并保留腰部与裙层固定。'
    if e['name']=='森林弓手Cos套装':e['note']='图例包含箭袋内的装饰短箭；弓与箭均为角色扮演外观道具参考。'
    if e['name']=='膝侧晶片外观件':e['note']='图例采用膝下较长晶片外装；膝侧短片款可缩短并上移固定带位置。'
