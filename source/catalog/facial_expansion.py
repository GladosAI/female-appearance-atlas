"""Edition 12: adult facial acting, visible states, gestures, and fictional eyes."""
from catalog_content import CATALOG, category, add

NEW_FACE_CATEGORIES=['face_states','face_emotions','mouth_actions','face_hands','face_overlays','face_augments']

def block(key,dimension,text):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['age_context']='成年角色面部绘画参考'
        e['facial_reference']=True
        e['aliases']=['面部参考','表情参考']

category('face_states','疲劳不适与环境状态','以眼睑、眉线、嘴角、肤色和汗滴表现角色状态；病中轻重是表演强度分档，冷冻为幻想效果。',['R03'])
category('face_emotions','情绪与眉眼联动','按眉峰、眼睑、视线、嘴角与头部方向比较情绪；名称是角色表演标签。',['R03'])
category('mouth_actions','唇齿动作与口部活动','嘴部动作保留完整面孔上下文，观察唇形、齿缝、下颌与口部道具；声音口型是动画造型参考。',['R64','R65'])
category('face_hands','手部与面部互动','遮脸、托压、挠头、扶眼镜等动作，观察正常五指、接触点、遮挡与面部形变。',['R03'])
category('face_overlays','妆面痕迹与覆盖物','泪汗、妆痕、灰尘食物污迹以及眼罩、绷带分别比较位置、边缘和遮挡；覆盖物为完成外观示意。',['R03','R64'])
category('face_augments','眼色光效与机械面部','异色虹膜、目光光效和原创科幻义眼分列；机械面部以完整外壳、面板接缝与正常面孔组合。',['R03'])

block('face_states','困倦睡眠与眼下变化','''
困倦半睁眼|sleepy half-open eyes|成年正脸，上眼睑压低、目光迟缓、嘴角松弛，完整脸部。
困倦眼皮下坠|drooping sleepy eyelids|上眼睑接近闭合，眉位平缓，头略向一侧倾，不画痛苦。
熬夜黑眼圈|late-night dark eye circles|成年眼下有清楚灰褐阴影，眼睑略垂，唇自然闭合。
眼袋疲惫外观|puffy-eye tired appearance|下眼睑下方有浅隆起与阴影，眉眼疲惫，正常脸部。
强撑精神睁眼|forcing tired eyes open|眉抬高、眼睛努力睁大，眼下仍有阴影，嘴唇微抿。
频频眨眼前一帧|tired blinking frame|一侧眼睑将闭、一侧刚抬起，眉与嘴放松，成年表演。
坐着打瞌睡脸|nodding-off face|成年头部轻垂、双眼闭合、嘴唇松开一点，清楚下颌角度。
刚睡醒迷蒙脸|just-awakened groggy face|眼睑半开、眉尾松弛、嘴微张，发束少量凌乱。
午睡后发懵脸|post-nap dazed face|视线略空、眉线平缓、嘴小幅张开，成年中性状态。
疲惫闭目缓气|tired closed-eye pause|双眼轻闭，眉心微松，嘴唇轻开，肩上衣领完整。
阅读累眼眯视|eye-strain squint acting|成年脸部，眯眼向前看、眉轻聚，嘴角自然，创作表演。
睡意泪光眼|sleepy watery eyes|半睁眼角有微小泪光，眉低、嘴放松，非哭泣大泪线。
困倦口角松垂|sleepy relaxed mouth corners|双眼低垂，嘴角松垂、口缝轻开，嘴唇没有夸张湿痕。
清晨伸展后松脸|relaxed morning-stretch face|成年脸，双眼轻闭、嘴角略扬，眉间舒展，普通日常。
久等疲倦注视|fatigued waiting gaze|头微偏、上眼睑低、视线侧移，单侧嘴角轻垂。
活动后疲惫微笑|tired smile after activity|成年脸眼睑略低，嘴角轻扬，额上一两滴汗，普通活动后状态。
''')

block('face_states','病中与局部不适表演','''
轻感冒角色外观|mild-cold character acting|成年脸鼻尖轻红、眼睑略低、嘴轻闭，少量不适感的绘画分档。
重感冒角色外观|strong-cold character acting|成年脸鼻翼较红、眉内侧抬起、眼角泪光与倦容更明显，表演强度分档。
生病疲惫脸|ill-looking tired face|脸色偏淡、眼睑低、眉心微聚、嘴角下垂，作为剧情病容。
苍白虚弱表演脸|pale weak-looking acting face|成年肤色较浅且饱和度低、唇色偏淡，眼睑和嘴角轻垂。
病中脸红表演|flushed ill-looking acting face|成年双颊泛红、眉内侧上抬、眼睑低，额上少量汗珠。
鼻翼发红不适脸|reddened-nose discomfort face|两侧鼻翼和鼻尖泛红，眉轻皱，嘴轻开，正常皮肤完整。
流鼻涕少量鼻下痕|small runny-nose trace|成年一侧鼻下有一小滴半透明鼻涕，眼睑稍低，完整脸部可见。
流鼻涕纸巾擦拭|runny-nose tissue wipe|成年脸一手持小纸巾在鼻下，边缘少量透明鼻涕，正常手指与鼻孔。
流鼻血少量鼻下痕|small non-graphic nosebleed trace|成年一侧鼻孔下仅一条短细红痕，神情轻皱眉，皮肤完整，无伤口特写。
流鼻血纸巾鼻下遮挡|tissue-under-nose non-graphic trace|成年一手将纸巾放鼻下，纸巾上仅一个小红点，正常脸部，不展示伤口。
忍喷嚏鼻部紧绷|holding-back-sneeze face|成年眉眼皱起、鼻翼轻收、嘴半开，鼻和嘴的紧绷可见。
喷嚏瞬间闭眼|sneeze-instant closed eyes|成年双眼闭、眉聚、嘴张开，头略向前，没有飞溅脏污。
轻咳口型不适|light-cough mouth acting|成年眉轻聚、嘴小开、下颌收紧，普通病中表演，无病原示意。
喉部不适吞咽脸|throat-discomfort swallowing face|成年嘴唇抿住、下颌微收、眉内侧轻抬，纯外观表演。
头痛皱眉表演|headache-like furrowed face|成年双眉向中间聚、眼睛眯起、嘴角轻垂，无医疗处置场景。
反胃捂唇前表情|nauseated-looking closed-lip face|成年眉内侧抬、鼻轻皱、嘴唇紧闭，脸色淡，不展示呕吐。
''')

block('face_states','冷热运动与汗滴状态','''
炎热眯眼脸|hot-weather squinting face|成年眼睛眯起、双颊微红、额上两滴汗，嘴轻开散气。
炎热抿唇烦躁脸|hot-weather irritated face|成年眉聚、唇紧抿，太阳穴有少量汗，普通环境表演。
大汗淋漓额颊|heavy-sweat face|成年额头、太阳穴与脸颊有数条清楚汗珠轨迹，正常肤面。
流汗单滴额角|single temple sweat drop|成年额角一颗明显汗滴，表情轻紧张，汗滴位置突出。
细汗亮面状态|fine perspiration sheen|成年额头与鼻梁细小汗点，眉眼放松，轻微光泽。
运动后喘息脸|post-exercise breathing face|成年嘴轻开、眉松、双颊红润，额上汗滴，普通活动后表演。
运动后闭眼擦汗前脸|post-exercise eyes-closed face|成年眼轻闭、唇轻开，额与颊少量汗，发际完整。
寒冷缩颈皱鼻脸|cold-weather tucked-neck face|成年围巾衣领包住下颈，鼻轻红、眼眯起、嘴微抿。
寒冷吐白气表演|cold-air visible-breath face|成年唇小开，嘴前一小团浅白气，围巾边缘完整。
寒冷牙关轻紧脸|cold-weather tightened jaw|成年唇略分露少量牙、眉内侧抬，神情冷缩，未受伤。
冷冻幻想冰霜脸|fictional frozen frost-face effect|成年脸覆浅蓝色调与少量细霜点，眼半开、嘴闭，皮肤完整，幻想外观。
冰壳侧面幻想脸|fictional side-face ice-shell effect|成年一侧脸外有薄透明冰壳光边，正常五官可见，非真实冻伤。
冷风泪光眯眼|cold-wind watery squint|成年眼角微小泪光、眉轻聚，鼻尖红，围巾领口。
雨后脸部水珠|rain-wet facial droplets|成年额、鼻尖与脸颊圆水珠，普通中性脸，区别眼角泪线。
吹风脸颊轻绷|wind-tensed cheek face|成年眼眯、嘴角轻收，少量发丝被吹向一侧，无超长发遮眼。
憋气脸颊鼓起状态|breath-holding puffed cheeks|成年双颊自然鼓起、唇闭、眉平，普通短暂表演，不画危险挑战。
''')

block('face_emotions','惊讶惊吓与空白反应','''
小幅惊讶睁眼|subtle surprised eyes|成年眉抬高一点、眼睁大、嘴小圆开，完整正脸。
明显惊讶张口|clear surprise with open mouth|成年双眉明显上抬、眼宽、下颌下落，嘴中等张开。
惊吓瞳缩表演|startled small-pupil acting|成年眼睛骤睁、圆瞳较小、眉高、嘴张开，动画夸张。
惊吓僵住脸|frozen-in-shock face|成年眉抬、眼睁大、嘴唇僵直微开，头不动的感觉。
侧看突然惊觉|sudden sideways alarm|成年头不完全转、目光猛向一侧，眉抬、嘴开一点。
受惊闭眼缩脸|eyes-closed startled flinch|成年眼闭、眉聚、脸向一侧缩，嘴角绷紧。
害怕含泪脸|fearful watery-eyed face|成年眉内侧抬、眼宽有浅泪光、嘴角收紧，无伤害场景。
忐忑左右偷看|uneasy side-glancing face|成年视线侧移、眉内侧略高、嘴抿，脸保持中性方向。
担惊皱鼻缩嘴|worried pinched-nose face|成年鼻翼轻皱、嘴缩小、眼睛眯起，担惊的表演。
愣住呆滞注视|blank stunned gaze|成年目光停在前方、眉线平直、嘴小缝开，无病理标签。
呆滞低眼睑脸|dull lowered-lid expression|成年上眼睑稍垂、视线无明确焦点、嘴角平，表演标签。
发懵微偏头脸|confused dazed head tilt|成年头微歪、眉一高一低、嘴微开，目光停顿。
难以置信凝视|disbelieving wide-eyed gaze|成年一侧眉较高、双眼宽、嘴唇半抿，明确不对称。
困惑皱眉小张口|confused brow furrow with small mouth|成年眉内侧轻聚、嘴小开，双眼朝上方看。
尴尬僵笑脸|awkward stiff-smile face|成年嘴角勉强上扬、眉内侧高、额角一滴汗，正常脸部。
松口气惊后表演|relieved-after-surprise acting|成年眉放松、双眼半闭、嘴轻开，作为惊讶后的平静转场。
''')

block('face_emotions','焦虑压力与对抗表演','''
焦虑紧抿唇脸|anxious pressed-lip face|成年眉内侧抬、眼向侧看、唇紧抿，嘴角有收紧线。
焦虑欲言又止脸|anxious hesitant-to-speak face|成年眉轻聚、嘴开一点又收，目光略低，表演迟疑。
着急皱眉催促脸|urgent impatient face|成年眉聚向下、眼直视、嘴小张，头略向前。
烦躁鼻梁皱起|irritated nose-bridge furrow|成年眉心皱、鼻梁轻皱、嘴角一侧压低。
痛苦闭眼皱脸|pain-like closed-eye grimace|成年双眼紧闭、眉聚、嘴角紧绷，完整无伤口的表演脸。
痛苦忍住张口|restrained pain-like mouth|成年眉内侧高、眼半闭、嘴张开一点，纯角色表演。
挣扎强撑表情|struggling effort face|成年眉深聚、牙关收紧、额上少量汗，表现努力坚持，无束缚场景。
挣扎犹豫矛盾脸|conflicted struggling expression|成年一侧眉高一侧紧聚、嘴角一侧下垂，视线侧移。
咬紧情绪怒视|tight-jaw angry gaze|成年眼睑压低、眉向下聚、闭唇牙关紧，面颊轻绷。
阴沉着脸下视|gloomy downward gaze|成年头略低、眉压低、嘴角平直，额上浅投影不遮五官。
板着脸严肃正视|stern straight-faced stare|成年眉平稍低、双眼正视、嘴闭成直线，五官完整。
冷淡压眉侧视|cold lowered-brow side gaze|成年一侧目光侧移、眉尾略低、嘴角平，无恶意符号。
委屈忍泪脸|holding-back-tears hurt expression|成年眉内侧高、眼角泪光、唇轻抿，情绪委屈。
崩溃泪落表演|overwhelmed crying acting|成年眉高聚、双眼泪线、嘴张开，情绪强烈，无自伤或暴力。
崩溃闭眼哭脸|overwhelmed eyes-closed crying|成年双眼闭、眉内侧抬、泪沿颊下流、唇绷，完整头像。
苦笑接受表演|wry accepting smile|成年单侧嘴角抬、另一侧微低，眼半闭，眉内侧轻高。
''')

block('face_emotions','期待催促与专注反应','''
期待睁亮双眼|expectant bright-eyed face|成年双眼抬起、眉略高、嘴角小幅上扬，目光专注。
期待闭唇浅笑|expectant closed-lip smile|成年嘴闭而角上扬、眼前视、眉松，普通等待场景。
迫不及待前探脸|eager leaning-forward face|成年头轻前探、眼睁亮、嘴角上扬，肩领在画面内。
迫不及待张口欲说|eager about-to-speak expression|成年双眉抬、眼前视、嘴小开，表达准备说话。
渴求礼物目光|yearning-for-a-gift gaze|成年向前注视、眉内侧略高、闭唇期待笑，日常非性语境。
渴求美食目光|yearning-for-food gaze|成年向侧下方凝视、眼睁亮、嘴角扬，正常唇面，无夸张舌唾。
着急等待侧望|urgent waiting side glance|成年头侧转一点、眉聚、嘴抿，视线朝画面外。
焦急搜索目光|anxious searching gaze|成年双眼向一侧转、眉内侧抬、嘴微开，头保持正面。
专注凝视小收唇|focused gaze with drawn-in lips|成年眉轻聚、眼前视、唇小幅收紧，完整头像。
思考抬眼偏嘴|thinking upward glance|成年眼向上侧看、单侧嘴角稍偏，眉一高一低。
发现线索眼亮|discovery brightening face|成年眼突然睁亮、眉抬、嘴角上扬，表现发现。
确认理解点头前脸|understanding confirmation face|成年下巴微收、双眼前视、嘴角轻扬，点头前一帧。
等夸奖含笑脸|awaiting-praise smile|成年眉松、双眼亮、嘴闭浅笑，非幼态比例。
收到邀请惊喜脸|pleased-surprise invitation face|成年眉抬、眼宽、嘴小开后角上扬，惊喜表演。
认真倾听微张唇|attentive listening lips|成年头略偏、眼看前侧、嘴唇轻开，普通倾听。
下定决心收眉脸|resolved narrowed-brow face|成年眉略向下聚、眼稳定正视、唇自然闭合，坚定表演。
''')

block('face_emotions','玩笑亲昵与狡黠表演','''
气鼓鼓双颊鼓起|annoyed puffed-cheek face|成年双颊鼓起、眉轻聚、嘴紧闭，眼正视，非憋气同眉形。
气鼓鼓单颊鼓起|one-cheek pouty annoyance|成年一侧颊明显鼓起、视线侧移、嘴角偏一边。
撒娇撅嘴表演|affectionate playful pout|成年嘴唇轻撅、眉内侧微高、头略偏，日常亲昵表演。
撒娇笑眼表演|affectionate smiling-eyes face|成年眼睑稍眯、嘴角柔和上扬、头轻歪，正常成年比例。
俏皮单眼眨眼|playful single-eye wink|成年一眼闭一眼开，眉轻扬、嘴角单侧抬，完整脸部。
俏皮歪头浅笑|playful head-tilt smile|成年头向一侧轻歪、双眼亮、闭唇浅笑。
狡猾单侧笑|sly one-corner smile|成年单侧嘴角较高、眼略眯、另一侧眉略高，清楚不对称。
狡猾侧眼窥视|sly sideways peeking gaze|成年头正面而眼侧转、眉稍低、嘴角短上扬。
轻哼偏头表演|mild huff head turn|成年头偏开、眼半闭、嘴唇轻撅，表示不满的哼。
哼声皱鼻表演|snorting-huff nose wrinkle|成年鼻轻皱、眉聚、嘴角压住，短哼表演，不加文字。
挑逗眨眼浅笑|lightly flirtatious wink-and-smile|成年一眼轻眨、嘴闭浅笑、头微偏，只有面部非露骨表演。
挑逗扬眉侧笑|lightly teasing raised-brow smile|成年一侧眉扬、双眼前视、单侧嘴角抬，轻松逗趣。
吓唬夸张瞪眼|playful intimidation wide eyes|成年双眼大睁、眉压低、嘴小张，像演戏吓唬朋友，无暴力。
吓唬皱鼻露齿|playful mock-snarl face|成年鼻轻皱、唇略分露少量牙，眼前视，玩笑演出。
得意扬下巴笑|proud raised-chin smile|成年下巴稍抬、眼半眯、嘴角扬，正常头部透视。
偷笑紧闭唇角|suppressed-mischievous smile|成年嘴紧闭而两角稍扬、眼侧看、眉松，区别捂嘴手势。
''')

block('mouth_actions','唇齿呼吸与开合','''
抿嘴唇紧闭动作|pressed-together lips|成年脸双唇向内轻收并紧闭，唇缝清楚，眉眼中性。
抿嘴唇忍笑动作|pressed-lip restrained smile|成年双唇收紧而嘴角上扬，眼轻眯，脸颊略抬。
咬嘴唇轻触下唇|light lower-lip bite|成年脸上齿轻触下唇中央，嘴不大开，无伤痕，无湿痕。
咬嘴唇侧角动作|light side-lip bite|成年脸一侧上齿轻触下唇侧角，眉轻聚，日常犹豫表演。
咬牙切齿怒视|clenched-teeth angry stare|成年眉压低、上下齿靠近、嘴横向紧绷，鼻轻皱，牙完整。
咬牙切齿侧嘴|sideways clenched-teeth grimace|成年嘴角一侧拉开露合拢牙、眉聚，完整下颌轮廓。
张大嘴正面动作|wide-open mouth front view|成年脸下颌明显下落、上下齿分离，口腔简化暗面，无夸张舌唾。
张大嘴侧面动作|wide-open mouth side view|成年侧面头像，下颌转动、唇边和少量齿边清楚。
吐舌头俏皮动作|playful short tongue-out face|成年脸舌尖仅小幅伸出下唇，双眼正常前视，轻松玩笑表演，无唾液。
吐舌头单侧小动作|small sideways tongue-out face|成年舌尖略偏一侧、单侧嘴角抬，普通调皮表演，无夸张拉长。
闭眼亲吻嘟唇|closed-eye kiss-face gesture|成年单人头像，双眼轻闭、嘴唇小幅向前嘟起，无伴侣或接触场景。
撅嘴圆唇动作|rounded pout mouth|成年脸双唇自然向前成小圆口，眉轻扬，口型清楚。
憋气闭唇鼓腮|closed-lip breath-holding cheeks|成年脸唇闭、双颊轻鼓、眉平，普通短暂表演，不画挑战或缺氧伤害。
缓慢呼气小圆唇|small rounded exhale lips|成年唇成小圆口、颊松、双眼平视，呼吸表演。
嘘声收圆唇动作|rounded hush mouth shape|成年唇向前轻收成窄圆口、眼半睁，未加手指遮挡。
无声张唇欲言|silent about-to-speak mouth|成年嘴唇刚分开、下颌微落，眉眼期待，清楚开合过渡。
''')

block('mouth_actions','饮食与口部道具动作','''
含着棒棒糖侧柄|lollipop held at mouth side|成年脸一枚普通圆棒棒糖小部分在唇间，短柄伸向侧方，正常日常吃糖。
棒棒糖唇前轻触|lollipop lightly touching lips|成年圆糖在唇前、嘴小开，手持糖柄，普通吃糖，无舔舐夸张或湿痕。
吹泡泡糖小泡|small chewing-gum bubble|成年嘴前有一个小粉色半透明泡泡，唇缘与圆泡连接清楚。
吹泡泡糖大泡|large chewing-gum bubble|成年嘴前一枚较大圆泡，泡边透光，眉眼仍可见，其他脸部不遮。
泡泡破开粘唇边|popped gum at lip edge|成年唇边少量薄粉色泡泡糖片，眼略惊讶，不做污秽或身体液体效果。
在吃东西小口咀嚼|small-bite chewing face|成年双唇闭、单侧颊轻鼓、下颌略偏，日常吃东西的脸部。
在吃东西嘴边一小屑|chewing with one food crumb|成年闭唇咀嚼、嘴角一小粒面包屑，眉眼正常，食物痕少量。
咬面包一口动作|taking a bite of bread|成年一手持小面包到嘴，嘴开一点，牙接食物边，不夸张吞咽。
咬苹果一口动作|taking a bite of apple|成年一手拿普通苹果近唇，嘴小开，食物与手指完整。
勺子入口小口型|small spoon-at-mouth pose|成年一手持小勺轻靠唇，嘴开小口，普通进食，不喂食他人。
叉子小食入口动作|small fork-held food at lips|成年小叉上普通小糕点在唇前，嘴小开、手五指自然。
杯沿饮水口型|cup-rim drinking mouth|成年杯沿轻靠下唇、头微抬，杯与嘴接触点可见，普通喝水。
吸管饮料口型|straw-drinking mouth shape|成年唇轻收住普通细吸管，手持空白杯，脸部日常中性。
流口水食物期待脸|small drool trace while anticipating food|成年看向画面边的小面包，嘴角仅一小滴透明唾液，普通饥饿喜剧表演。
流口水睡眠口角痕|small sleeping drool trace|成年双眼闭、头稍倾、嘴角仅一条短细透明痕，日常睡眠，无夸张舌唾。
抽烟成年中性侧脸|adult neutral smoking side portrait|成年侧面头像，一支无品牌香烟轻靠唇边、手指自然夹持，仅一缕细烟，普通观察图。
''')

block('mouth_actions','声音口型与表演','''
打哈欠轻张口|small yawning face|成年双眼半闭、眉松、嘴张成中等竖椭圆，下颌下落。
打哈欠大开口|wide yawning face|成年双眼闭、嘴竖向张大、眼角少量泪光，无夸张舌唾。
喊叫眉聚张口|calling-out open mouth|成年眉聚、眼前视、嘴大张，下颌自然下落，声音表现不加文字。
喊叫侧面口型|side-view calling mouth|成年侧头像嘴开大，牙边与下颌转动，眼看前方。
唱歌宽开元音口型|singing broad open-vowel shape|成年头像眉松、嘴宽竖开、下颌下落，少量上齿可见。
唱歌圆收元音口型|singing rounded-vowel shape|成年头像嘴成圆口、眼半闭、眉松，区别宽开口。
唱歌微笑口型|smiling singing mouth|成年嘴角抬、唇分开露少量上齿，双眼轻眯，普通唱歌。
说话闭合唇起音|closed-lip speech onset|成年正脸双唇刚闭合，上下唇边清楚，眉眼中性，动画起音参考。
说话宽横唇形|wide horizontal speech shape|成年嘴横向拉宽、齿缝窄，嘴角张开，动画口型参考。
说话小圆口形|small-round speech shape|成年嘴成小圆口、下颌稍落，眉眼中性，动画口型参考。
说话大圆口形|large-round speech shape|成年嘴成较大圆口、上下齿少量可见，下颌下降。
说话齿边轻触下唇|upper-teeth lower-lip speech shape|成年上齿边轻靠下唇、口缝窄，完整脸部，动画口型参考。
说话舌尖齿后口形|tongue-behind-teeth speech shape|成年嘴小开，仅可见舌尖在上齿后，正常短舌，无外伸夸张。
低声耳语小开口|quiet whisper mouth|成年嘴侧开小缝、眼看侧前方，头微偏，普通说话。
笑着说话开合口型|laughing-speech mouth frame|成年嘴角扬、嘴中等开、眼轻眯，普通交流表演。
叹气收眼开唇|sighing lowered-eye mouth|成年眼半闭、眉松、唇轻开，肩领清楚，日常叹气。
''')

block('face_hands','遮脸遮嘴与即时反应','''
单手捂脸完整遮挡|one-hand face cover|成年一只手掌覆额到鼻部，五指自然展开，露下唇与下颌。
两手捂脸指缝窥看|two-hand face cover peeking|成年两掌遮大部分脸，正常十指与指缝中一眼可见，嘴下缘留少量。
捂脸只遮单眼|single-eye hand cover|成年一掌遮一侧眼，另眼和嘴完整可见，指尖不穿过眼睛。
捂嘴中性遮挡|neutral hand-over-mouth|成年一手轻覆口部，手背朝外，双眼中性，拇指与四指自然。
惊讶捂嘴睁眼|surprised hand-over-mouth|成年一手覆嘴、双眉抬、双眼睁大，口部被手自然遮挡。
捂嘴笑弯眼|laughing behind one hand|成年一手在嘴前，双眼弯起、眉松，露出少量上扬嘴角。
捂嘴忍泪表演|hand-over-mouth holding tears|成年一手覆口，眉内侧抬、眼角泪光，情绪表演。
双手捂嘴惊觉|two-hands mouth cover|成年两手并拢覆口，双眼睁大，正常手指不过多，不加其他手。
握拳掌背掩嘴轻咳|fist-back cough cover|成年轻握拳的手背在嘴前，眼微眯、嘴部分遮挡，普通遮嘴动作。
拳侧遮嘴清嗓|fist-side mouth cover|成年轻握拳侧边靠口前，眉眼中性，拇指在正确拳侧。
手挡额头避光|forehead shading hand|成年手掌横在额前、掌背朝上，眼眯、五官清楚。
指缝遮额偷看|finger-gap forehead peek|成年一手覆额半遮眼，正常五指间隙露视线，嘴微抿。
捂住单侧脸颊|single-cheek palm cover|成年一掌贴一侧颊，另一侧脸和嘴不遮，掌根有轻接触形变。
两掌遮脸侧耳|two-palms cheek-side cover|成年双掌贴两侧脸颊近耳，眼鼻嘴全可见，正常指位。
纸巾挡嘴小表情|tissue-covered mouth expression|成年一手持小纸巾在嘴前，眼轻眯，正常手五指和纸巾边。
袖口遮嘴浅笑|sleeve-cuff mouth cover smile|成年完整袖口靠嘴前，手指少量露出，眼含笑，面部遮挡清楚。
''')

block('face_hands','托压挠与佩戴动作','''
两手压着脸蛋|two hands pressing cheeks|成年双掌向内轻压两侧脸颊，颊肉轻挤、嘴成小圆口，正常十指。
两手托腮浅笑|two-hand chin-and-cheek rest|成年双掌托住下颌两侧，嘴角扬，手腕完整，正常五指每手。
单手托腮发呆|single-hand cheek-rest daydream|成年单掌托一侧颊，头轻偏，目光放松，脸颊接触线清楚。
指尖压脸颊两点|two-fingertip cheek press|成年左右食指各轻压一侧颊，其他指自然收起，颊有浅凹点。
单手捏住一侧脸颊|gentle one-cheek pinch|成年自用拇指食指轻捏单颊，皮肤仅微小变形，不画疼伤。
手指托下唇下方|fingertip under lower lip|成年一食指放在下唇下的下巴处，嘴闭，眉思考，其他指自然。
食指托下巴思考|index-finger chin support|成年食指和拇指托下巴，眼上侧看，完整正确手部。
挠头困惑表演|confused head-scratch|成年一手在头侧头发上轻挠，眉一高一低、嘴小开，完整手指。
挠头尴尬微笑|awkward smiling head-scratch|成年一手在后侧发上，眼轻眯、嘴角勉强扬，头发与手不融为一体。
扶镜框鼻梁中部|adjusting glasses at bridge|成年食指扶眼镜鼻梁，镜片仍露双眼，正确手指与镜架。
扶镜框单侧镜腿|adjusting glasses at temple|成年一手捏单侧镜腿，眼前视，镜片、镜桥与耳侧完整。
抬镜框露出双眼|lifting glasses to reveal eyes|成年一手把镜框略抬，双眼完整可见、镜腿与手接点清楚。
咬手指焦虑轻触|anxious light finger-to-lip bite|成年食指指尖仅轻触门牙边，眉焦虑、嘴小开，皮肤完整，不吸吮或伤害。
咬手指犹豫侧视|hesitant finger-to-lip contact|成年指尖轻靠一侧牙边、眼侧视、眉内侧略高，普通紧张动作。
剪刀手遮眼单侧|V-sign covering one eye|成年一手食中指成V放一眼前，另一眼可见，其他三指正确收起。
剪刀手横过双眼|horizontal V-sign across eyes|成年一手食中指横成V在双眼前，留眼部间隙，五指总数正常。
''')

block('face_hands','复合手势与角色反应','''
剪刀手侧眼眨眼|side-eye V-sign wink|成年V手势在一眼侧，另一眼轻眨，嘴闭浅笑，正确五指。
两手花托脸俏皮笑|two-hand flower-frame smile|成年双掌在下巴左右展开成花托，眼含笑，双手十指自然。
单指轻贴唇嘘声|index-finger hush gesture|成年食指竖在唇前，其他指收起，嘴圆收、眼前视。
手掌贴额惊讶|palm-to-forehead surprise|成年一掌贴额、眉抬、嘴小张，眼和下颌清楚。
指尖贴眉心焦虑|fingertips-to-brow anxiety|成年拇指食指轻捏眉心旁，眼半闭、嘴抿，非掐伤。
双指撑住额角思考|two-finger temple thinking gesture|成年两指在一侧额角，眼侧上看、嘴闭，手部自然。
单掌托腮气鼓鼓|palm-supported puffed cheek|成年一掌托颊、另一颊鼓起，嘴闭，眉轻聚。
双指挤颊撅嘴|two-finger cheek-squeeze pout|成年两食指各压一颊，嘴轻撅，正常自然浅形变。
手指扶镜框狡黠笑|glasses-hold sly smile|成年一手轻扶镜框一侧，眼略眯、单侧嘴角扬，镜架完整。
手掌捂额疲倦闭眼|forehead palm tired eyes|成年一掌在额、眼闭、眉松，嘴轻开，日常疲倦姿态。
手握纸巾抹泪后|tissue-at-cheek after tears|成年一手纸巾轻靠颊，眼有泪光、嘴角轻垂，纸巾无血迹。
掩嘴打哈欠动作|covered-mouth yawn gesture|成年一手在大张嘴前、双眼闭，嘴的边缘和手正常遮挡。
指尖刮鼻侧玩笑|playful fingertip beside nose|成年一食指在鼻侧轻点，单侧眉抬、嘴角上扬，普通玩笑。
脸旁拇指赞许笑|thumbs-up beside face|成年一手在脸旁比拇指，其他四指收在拳内，双眼亮、嘴浅笑。
脸旁小比心浅笑|small finger-heart beside face|成年拇指食指在脸侧成小比心，其他三指收起，正常成年比例。
两手压颊惊讶表演|two-palms cheek press surprise|成年双掌贴颊、眉抬、嘴成较大O形，正常十指与脸颊轻形变。
''')

block('face_overlays','妆痕泪汗与脏污','''
眼妆哭花双侧泪痕|tear-smudged eye makeup both sides|成年双眼下各短黑灰妆痕随浅泪线下滑，眼睛完整，无血迹。
眼妆哭花单侧晕染|one-sided tear-smudged eye makeup|成年一眼外缘与眼下少量眼线晕染，另一侧较整齐，眉委屈。
睫毛膏小点泪痕|mascara-dot tear trace|成年下眼缘少量黑灰小点与细泪线，正常睫毛根与皮肤。
眼影哭花色块|tear-smudged eyeshadow patches|成年上眼影与外眼角彩色淡晕边，眼下浅泪线，五官不遮。
揉眼后眼线晕痕|rubbed-eyeliner smudge appearance|成年单眼外侧黑灰短晕痕、眼稍眯，手已放下，非损伤。
泪干后浅颊线|faint dried-tear cheek lines|成年双颊极浅细线自眼角向下，眉松、嘴轻闭，皮肤完整。
脸上灰尘脏痕|dust smudges on face|成年一颊和额角各浅灰尘抹痕，眼鼻嘴正常，明显表面污痕。
脸上泥点脏痕|small mud specks on face|成年颊与鼻侧少量棕泥点，不遮五官，完整干净皮肤底。
脸上炭灰擦痕|charcoal-soot face smudges|成年一侧颊与鼻梁少量深灰擦痕，无灼伤或火灾现场。
脸上彩粉脏痕|colored-powder face traces|成年额角与颊少量原创彩粉颗粒，正常脸，不覆盖双眼。
嘴角巧克力小痕|small chocolate mouth-corner mark|成年嘴角一小块棕色食物痕，闭唇浅笑，日常吃东西后。
嘴边奶油一点|small cream spot near mouth|成年一侧唇边小点白奶油，正常唇形，不画大面积液体。
面颊酱汁小点|small sauce dot on cheek|成年颊下少量橙棕食物小点，眉眼中性，日常污迹。
汗后妆面局部晕边|perspiration-softened makeup edge|成年额上少量汗、外眼角淡色眼影晕边，眼形可见。
泪光与湿发贴额|tears with damp forehead strands|成年眼有泪光、两三根湿发贴额，颊有细泪线，普通表演。
鼻下纸巾绒屑痕|tiny tissue-fiber nose trace|成年鼻下少量白纸巾细屑，鼻尖轻红，正常脸部，不贴成胡须。
''')

block('face_overlays','眼罩绷带与完整覆盖物','''
睡眠双眼软眼罩|soft sleep mask on both eyes|成年戴完整软眼罩遮双眼，鼻和嘴露出，额后弹带小侧面可见。
抬起睡眠眼罩|lifted sleep mask on forehead|成年软眼罩抬到额上，双眼露出，松紧带与面罩边完整。
单眼罩右侧遮挡|right-eye patch appearance|成年右眼被圆钝单眼罩遮住，另一眼完整，细头带绕后。
单眼罩左侧遮挡|left-eye patch appearance|成年左眼被浅色单眼罩遮住，另一眼完整，斜向细带清楚。
双带单眼罩外观|double-strap single-eye patch|成年一侧单眼罩接上下两根细带，遮挡边与正常另一眼。
硬壳单眼罩道具|hard-shell single-eye costume patch|成年原创轻硬壳遮一眼，壳厚与耳后带清楚，完整皮肤。
窄布双眼遮带外观|narrow cloth eye-cover appearance|成年普通窄软布带遮双眼，后端短结，鼻嘴露出，中性角色道具。
眼罩抬起露单眼|one-eye revealed below lifted patch|成年单眼罩抬到眉上露出完整单眼，另一眼完整，手与固定带连接自然。
额头整洁绷带外观|clean forehead bandage appearance|成年额上两圈干净布绷带，双眼鼻嘴可见，未展示伤口。
单颊小方纱布外观|small cheek gauze patch|成年一颊小方白纱布及四角固定贴，皮肤完整、无渗血。
鼻梁小贴片外观|small nasal-bridge strip appearance|成年鼻梁小布贴片，边缘清楚，双眼鼻尖和嘴正常。
眉上短贴条外观|short strip above eyebrow|成年一侧眉上短布贴条，眉眼正常，完整皮肤，无伤口。
下巴小纱布外观|small chin gauze appearance|成年下巴正中小白纱布，边贴清楚、嘴唇完整。
颊侧斜贴绷带外观|diagonal cheek-bandage appearance|成年一颊有两短条浅色布贴，五官完整、皮肤无损伤表现。
单眼纱布遮盖外观|single-eye gauze covering|成年一眼被完整白纱布覆盖，窄贴条固定，另一眼鼻嘴可见，无医疗步骤。
额颊多处整洁贴片|multiple clean forehead-cheek patches|成年额角与一颊各一小贴片，完整皮肤、五官不遮，无伤口。
''')

block('face_augments','虹膜异色与目光光效','''
蓝棕异瞳完整双眼|blue-brown heterochromia eyes|成年从眉到鼻梁眼部特写，一眼蓝虹膜一眼棕虹膜，正常圆黑瞳。
灰绿异瞳完整双眼|gray-green heterochromia eyes|成年双眼特写，一眼灰一眼绿虹膜，中央圆黑瞳与小高光。
金紫异瞳幻想双眼|gold-violet fantasy heterochromia|成年双眼特写，原创一眼金一眼紫，圆瞳可见，幻想色。
扇区异色虹膜特写|sector-colored iris close-up|成年单眼大特写，虹膜一扇区异色，中央圆黑瞳完整。
中央异色双眼特写|central-color-ring eyes|成年双眼虹膜近瞳孔一圈异色，外环颜色不同，黑圆瞳完整。
左右光线差别目光|differently lit paired eyes|成年双眼虹膜同色，一侧受光一侧浅暗，说明光线效果而非异瞳。
两眼放光星点高光|bright eyes with star highlights|成年双眼睁亮，各虹膜有小星状白高光，中央正常圆瞳仍可见。
两眼放光圆光高光|bright eyes with round highlights|成年双眼有清楚圆反光与轻亮感，正常虹膜和黑圆瞳，不画发射光束。
两眼放光兴奋目光|excited luminous-eye acting|成年眉略抬、双眼亮、嘴浅笑，眼内多个小白高光，正常圆瞳。
含泪期待目光|watery expectant eyes|成年双眼略睁、眼缘少量泪光与反光，眉内侧轻高。
低高光疲倦目光|reduced-highlight tired eyes|成年双眼半睁、虹膜高光小、眼下浅影，正常圆瞳。
瞪视小瞳动画特写|small-pupil glaring animation eyes|成年双眼宽睁、圆瞳较小、眉略低，动画夸张而非测量示例。
眯视狡黠双眼特写|sly narrowed-eyes close-up|成年双眼眯、眉一高一低，虹膜部分被眼睑遮，正常眼部。
单眼聚焦另一眼轻闭|one-eye focus with opposite eye closed|成年一眼睁开聚焦另一眼轻闭，眉形随之不对称。
闭目微笑眼线特写|closed smiling-eye lines|成年双眼闭成上弯柔线，眼角微抬，眉放松。
睁眼反光环幻想|fictional reflected-ring eyes|成年虹膜外有浅圆环反光，中央圆黑瞳清楚，原创幻想光效。
''')

block('face_augments','电子义眼与半机械面孔','''
单眼电子义眼圆光环|single electronic-eye ring|成年一眼为原创圆环电子义眼，另一眼正常，周围完整皮肤与金属细边。
单眼电子义眼光圈片|single electronic iris-blade eye|成年一眼为原创机械光圈片结构，另一眼正常，完整外壳，无手术细节。
单眼电子义眼十字准纹|single electronic-eye cross motif|成年一眼电子镜面内部原创细十字纹，另一眼正常，无武器锁定界面。
单眼电子义眼竖光窗|single electronic-eye vertical light window|成年一眼是原创竖向光窗，另一眼正常，壳边与眉线完整。
双电子义眼环瞳|paired electronic-eye rings|成年双眼各原创小环形镜面瞳，正常眉鼻嘴，金属细边完整。
双电子义眼点阵|paired electronic dot-array eyes|成年双眼为原创点阵光面，眼眶外壳完整，不画破损。
单眼外置扫描镜|external single-eye scanner lens|成年一眼前有原创圆镜罩，连接额侧细支架，另一眼和脸正常。
单眼电子镜罩翻起|flipped-up electronic eye cover|成年原创电子眼罩翻到眉上，下方义眼环可见，另一眼正常。
半人半机器左右面孔|half-human half-machine face|成年正脸一侧正常面孔、一侧完整金属面板和电子眼，直分区、完整无伤口。
半人半机器斜分面孔|diagonal human-machine face division|成年面孔原创斜向板片覆盖额侧至颊，电子眼和正常眼并列，皮肤完整。
半机械额侧与义眼|mechanical temple and artificial eye|成年单侧额角金属板接电子眼边框，鼻嘴正常，接缝完整。
半机械下颌与正常眼|mechanical jaw with natural eyes|成年下颌原创金属外壳分片，双眼正常，嘴唇外框完整，无内部肉体。
半机械颊片与耳侧|mechanical cheek-and-ear panel|成年一颊原创圆角板与耳侧外壳接缝，眼鼻嘴保持正常。
仿生面孔细接缝|android face with fine seams|成年完整仿生脸有少量额颊几何细缝，双电子眼，表面平整，无裂伤。
全机械人形面孔|fully mechanical humanoid face|原创成年比例完整金属人形面孔，有眉鼻唇外形与环形电子眼，不露线路或伤口。
电子义眼关闭待机|electronic eye in standby appearance|成年一电子义眼为暗色镜面小待机点，另一眼正常，脸部完整。
''')

ALIASES={
    '困倦半睁眼':['困倦','困乏','sleepy'],
    '轻感冒角色外观':['轻感冒'],
    '重感冒角色外观':['重感冒'],
    '生病疲惫脸':['生病','病容'],
    '病中脸红表演':['脸红'],
    '苍白虚弱表演脸':['苍白'],
    '愣住呆滞注视':['呆滞'],
    '含着棒棒糖侧柄':['含着棒棒糖','含棒棒糖'],
    '脸上灰尘脏痕':['脸上有脏东西','脸部脏污'],
    '两手压着脸蛋':['两手压着脸蛋','挤脸蛋'],
    '剪刀手遮眼单侧':['剪刀手遮眼','遮眼剪刀手'],
    '扶镜框鼻梁中部':['扶镜框','推眼镜'],
    '抿嘴唇紧闭动作':['抿嘴唇','抿唇'],
    '半人半机器左右面孔':['半人半机器'],
    '单眼电子义眼圆光环':['电子义眼','机械义眼']
}
for e in CATALOG:
    if e['name'] in ALIASES:e['aliases']+=ALIASES[e['name']]

# Edition 13: append variants within existing categories; retain all earlier IDs.
start=len(CATALOG)
block('face_states','眩晕与晕眩表演','''
眩晕失焦注视|dizzy unfocused gaze|成年正脸，目光松散、上眼睑半垂、眉内侧略抬、嘴小幅张开，剧情晕眩表演。
眩晕偏头合眼|dizzy tilted-head closed eyes|成年头向一侧轻倾、双眼轻闭、嘴角松垂，颈领完整，区别普通中性脸。
眩晕闭目皱眉|dizzy eyes-closed brow furrow|成年双眼轻闭、眉心聚拢、唇微抿，头保持正面，表现停下来缓神。
眩晕额侧轻扶|dizzy hand-at-temple face|成年一手轻贴额侧，正常五指与手腕，眼半睁、眉内侧抬、嘴轻开。
眩晕手掌捂额|dizzy palm-on-forehead face|成年一掌贴额头上缘，双眼仍可见且微闭、唇轻分，手部自然无额外手指。
眩晕托腮缓神|dizzy cheek-rest pause|成年一掌轻托一侧脸颊，头轻倾、目光散、嘴角平，手腕与衣袖边可见。
眩晕转头后迟滞|dizzy delayed gaze after turn|成年三分之四侧脸，头向左而目光仍偏前，眼睑低、唇轻开，清楚方向差。
眩晕低头抬眼|dizzy lowered-head upward gaze|成年下巴轻收、眼从低头位置向前抬，眉内侧略高、嘴闭而放松。
眩晕努力定睛|dizzy trying-to-focus expression|成年眉心微聚、眼睛努力向前看、上下眼睑收紧，唇轻抿，区别失焦例。
眩晕侧视轻皱鼻|dizzy side-glance discomfort|成年视线向一侧移、鼻轻皱、眉内侧抬、嘴角轻下垂，纯外观表演。
眩晕伴额角小汗|dizzy face with temple sweat|成年头微偏、双眼半睁、眉聚，额角一小滴汗、唇自然轻分。
眩晕脸色偏淡|dizzy pale-looking face|成年肤色与唇色偏淡、目光松散、眉内侧轻抬，皮肤完整，作为剧情画面标签。
眩晕缓缓睁眼|dizzy slowly-opening-eye frame|成年双眼由闭向半睁，眉线稍舒展、嘴轻闭，表现缓神过程的一帧。
眩晕头侧星点动画|dizzy orbiting-star animation face|成年完整正常双眼半睁、头轻倾，头旁少量小星点和一条弧线，是漫画提示符而非诊断图。
眩晕头侧旋环动画|dizzy orbiting-swirl animation face|成年半闭眼、嘴小开，头侧上方一条小旋环，五官仍完整，不把旋环画成发饰。
眩晕双眼旋纹动画|dizzy spiral-eye animation face|成年正脸，双眼内各一条清楚细螺旋线、眉内侧抬、嘴小开；明确动漫符号，不是正常虹膜结构。
''')
for e in CATALOG[start:]:e['aliases']+=['眩晕','晕眩','头晕','dizzy','dizziness']

start=len(CATALOG)
block('face_emotions','困惑疑问与不解反应','''
困惑单眉高挑|confused single-raised-brow face|成年正脸，一侧眉明显高挑、另一侧平，双眼前视、嘴闭而略偏，疑问表演。
困惑双眉内收|confused inward-brow face|成年双眉内侧向中间轻收、眼睁开、嘴小幅张开，眉心清楚但没有怒视。
困惑眉内侧上抬|confused inner-raised brows|成年双眉内端上抬成浅斜线、眼前视、嘴角轻下垂，表现不解而非哭泣。
困惑左倾头圆口|confused left-head-tilt small round mouth|成年头向角色左侧轻歪、双眼抬起、嘴成小圆口，完整头颈与眉眼。
困惑右倾头抿唇|confused right-head-tilt pressed lips|成年头向角色右侧轻歪、眉一高一低、嘴轻抿，区别左倾小圆口。
困惑抬眼回想|confused upward-recall gaze|成年眼向上方偏侧看、眉内侧轻聚、唇闭、下巴微抬，清楚眼神方向。
困惑侧眼确认|confused sideways-checking gaze|成年头正面、两眼向一侧移、一侧眉抬、嘴小缝开，像确认刚听见的信息。
困惑低眼睑停顿|confused lowered-lid pause|成年双眼上睑略低、眉不对称、嘴角一侧轻压，神情停顿而非困倦。
困惑睁眼欲问|confused wide-eyed about-to-ask face|成年眼睁开、双眉略高、嘴刚分开，下颌轻落，像准备发问。
困惑眯眼辨认|confused squinting recognition face|成年双眼轻眯、眉心聚、嘴轻抿，头向前探一点，正常五官不夸张变形。
困惑歪嘴思索|confused asymmetric-mouth thinking face|成年正脸、嘴角向一侧偏、眉一高一低、眼上侧看，突出嘴角与眉的不对称。
困惑三分侧面回看|confused three-quarter look-back face|成年三分之四头部视角，视线向后侧回看、外侧眉抬、嘴小开，清楚鼻梁方向。
困惑指尖点下巴|confused fingertip-at-chin face|成年一食指轻贴下巴、其他四指自然收起、眼上侧看、眉轻聚，正常手腕。
困惑手指贴脸颊|confused fingertip-at-cheek face|成年一食指轻点一侧脸颊、头微偏、眉一高一低、嘴小圆开，区别托腮。
困惑轻挠头侧|confused light head-scratch face|成年一手轻触头侧发际，正常五指、手腕可见；眉不对称、嘴微开，手不遮双眼。
困惑勉强浅笑|confused uncertain slight smile|成年嘴角勉强浅扬、一侧眉高挑、眼向侧移，像没有理解但礼貌回应，不加汗泪。
''')
for e in CATALOG[start:]:e['aliases']+=['困惑','疑惑','不解','迷惑','confused','puzzled']

# Edition 15: blush placement and nonexplicit adult flirting/charisma acting.
start=len(CATALOG)
block('face_states','潮红位置与色感表现','''
潮红双颊浅粉|light pink cheek flush|成年中性正脸，两颊局部浅粉渐变，眼睛正常前视、唇闭，边界柔和。
潮红双颊明显|pronounced cheek flush|成年两颊较明显暖红渐变，眉眼放松、嘴轻闭，完整鼻与眼部。
潮红高颧部位|high-cheekbone blush|成年颧骨高处各一小片粉红，颊下较淡，眼睑正常，突出色块位置。
潮红低颊部位|lower-cheek blush|成年脸颊较低处有软粉色，鼻梁与眼下较淡，唇自然闭合。
潮红鼻梁连颊|nose-bridge-connected flush|成年鼻梁与两颊连接成浅红色带，五官完整，眉眼中性，色带不是伤痕。
潮红鼻尖轻染|subtle nose-tip flush|成年鼻尖轻红、双颊只有很浅色感，完整鼻翼，正常平静脸。
潮红耳尖与双颊|ear-tip and cheek flush|成年短发露双耳，耳尖与双颊浅红，眉松、闭唇小笑，耳廓正常。
潮红单侧脸颊|one-sided cheek flush|成年仅一侧颊较粉红、另一侧保持基础肤色，头微偏、双眼可见。
潮红暖橙色感|warm peach blush|成年两颊浅桃橙色感与自然肤色融合，正常前视与闭唇，非面部油彩图案。
潮红玫瑰色感|rose-colored cheek blush|成年两颊玫瑰粉渐变，边缘柔软，鼻与眼下保持基础色，正常神情。
潮红深肤暖红|warm flush on deep skin tone|成年深肤色脸部，双颊有克制暖红与稍亮色差，完整五官，不画成不透明粉片。
潮红浅肤柔粉|soft blush on light skin tone|成年浅肤色头像，双颊柔粉渐变与透明色感，眼睑正常、嘴闭。
潮红害羞低视|blushing shy downward glance|成年双颊粉红、视线略低、眉松、闭唇小幅浅笑，普通社交害羞。
潮红惊喜睁眼|blushing pleased-surprise face|成年双颊暖红、双眉略抬、眼睁亮、嘴小幅张开，普通惊喜表演。
潮红轻笑侧望|blushing slight-smile side glance|成年双颊浅红、双眼侧移、嘴角轻扬，头保持正面，日常情绪头像。
潮红闭目含笑|blushing closed-eye smile|成年双颊粉红、眼轻闭、闭唇柔和微笑，完整头颈，普通亲切情绪。
''')
for e in CATALOG[start:]:e['aliases']+=['潮红','泛红','脸部潮红','blush','flushed']

start=len(CATALOG)
block('face_emotions','挑逗逗趣与轻度调情','''
挑逗单眼慢眨|teasing slow wink|成年一眼轻闭、另一眼正常看前方，单侧眉略扬、嘴闭小笑，轻度逗趣表演。
挑逗眨眼歪头|teasing wink with head tilt|成年一眼眨、头轻向一侧歪、闭唇浅笑，完整短发与高领衣边。
挑逗双眉轻扬|teasing raised brows|成年双眉略扬、眼前视、嘴角轻抬，表情轻松，没有夸张口型。
挑逗单眉挑起|teasing single-brow arch|成年一侧眉高挑、双眼正视、单侧嘴角上扬，清楚不对称。
挑逗半眯笑眼|teasing narrowed smiling eyes|成年双眼轻眯成笑意、眉松、嘴闭小笑，普通社交调情。
挑逗侧眼偷笑|teasing sideways suppressed smile|成年头正面、视线侧转、嘴角克制扬起，双眉轻松。
挑逗偏头浅哼|teasing mild-huff face|成年头略偏开、眼半睁、嘴轻撅一点后角扬，像玩笑地哼一声。
挑逗轻抬下巴|teasing lifted-chin smile|成年下巴略抬、双眼看前方、闭唇小笑，颈部透视自然。
挑逗收下巴抬眼|teasing tucked-chin upward look|成年下巴轻收、眼向前抬、单侧眉扬、唇闭，完整眉眼可见。
挑逗三分侧笑|teasing three-quarter smile|成年三分之四脸视角、眼看镜头方向、嘴角一侧略高，鼻梁方向清楚。
挑逗回眸小笑|teasing look-back smile|成年轻转头回看、眉略扬、嘴闭浅笑，普通高领服装边完整。
挑逗正视抿笑|teasing pressed-lip smile|成年双眼正视、嘴唇轻抿但两角扬起、眉松，区别紧张咬唇。
挑逗眼尾轻弯|teasing gently lifted outer eyes|成年眼尾随浅笑轻弯、眉尾放松、嘴闭，表演自然不过度拉长五官。
挑逗指尖点脸|teasing fingertip-to-cheek pose|成年一食指轻点颊、其他四指自然收起，眨一眼、嘴闭小笑，手腕完整。
挑逗脸旁比心|teasing finger-heart beside face|成年一手在脸旁比小比心，正常五指、眼含笑、唇闭，不遮五官。
挑逗扶镜框浅笑|teasing glasses-frame smile|成年一手轻扶单侧镜框，眼看前方、眉一侧略扬、嘴闭小笑，镜架与手指正常。
''')
for e in CATALOG[start:]:e['aliases']+=['挑逗','轻度调情','逗趣','teasing','flirtatious']

start=len(CATALOG)
block('face_emotions','魅惑目光与含蓄笑意','''
魅惑柔和正视|charming soft direct gaze|成年双眼平稳正视、眉舒展、闭唇柔和小笑，轻度魅力表演。
魅惑自信抬眉|charming confident raised-brow face|成年一侧眉轻抬、目光稳定、嘴角浅扬，完整正脸与高领衣边。
魅惑半睑凝视|charming lowered-lid gaze|成年上眼睑略低、正常虹膜与圆瞳仍可见，闭唇浅笑，无空白或上翻双眼。
魅惑侧望回笑|charming side glance with smile|成年头正面、视线侧移、眉松、嘴闭并稍扬一角。
魅惑下巴轻收|charming tucked-chin gaze|成年下巴稍收、眼看前方、双眉柔和、闭唇小笑，正常脸型比例。
魅惑下巴轻抬|charming raised-chin gaze|成年下巴略抬、眼平看镜头方向、嘴角柔和上扬，头颈透视正常。
魅惑三分侧脸|charming three-quarter face|成年三分之四脸、眼看前侧、闭唇含笑，鼻与眼部完整。
魅惑侧脸回眸|charming profile look-back|成年头略偏侧但双眼仍可辨、视线回看、嘴角小幅上扬。
魅惑单眼轻眨|charming subtle wink|成年一眼轻眨、另一眼正常正视、眉轻扬、闭唇柔和微笑。
魅惑温柔笑眼|charming warm smiling eyes|成年双眼轻弯、眉放松、嘴角柔和扬起，普通亲切而有魅力的头像。
魅惑克制偏笑|charming restrained asymmetric smile|成年一侧嘴角较高、视线前方、眉一高一低但不皱，完整脸部。
魅惑期待浅笑|charming expectant smile|成年双眼专注、眉内侧略抬、唇闭浅笑，普通期待交流。
魅惑托颊浅笑|charming cheek-rest smile|成年一掌轻托一侧颊、手腕完整、眼看前方、嘴闭微笑，正常五指。
魅惑指尖托下巴|charming fingertip-chin pose|成年一手食指与拇指轻托下巴、其他三指自然，眉松、闭唇微笑。
魅惑轻偏头凝视|charming tilted-head gaze|成年头向一侧轻偏、双眼正常凝视、嘴角克制小幅扬起，成熟比例。
魅惑轻笑垂眼|charming slight-smile lowered gaze|成年目光稍向下、眼睑放松、闭唇柔和浅笑，额和鼻完整。
''')
for e in CATALOG[start:]:e['aliases']+=['魅惑','魅力表情','含蓄魅惑','charming','alluring']

start=len(CATALOG)
block('face_emotions','含蓄勾引与暧昧邀约','''
含蓄勾引正视浅笑|inviting direct-gaze smile|成年正脸，双眼稳定看前方、单侧眉轻扬、闭唇小笑，轻度暧昧邀约头像。
含蓄勾引侧望浅笑|inviting side-glance smile|成年头正面、眼向一侧看、闭唇柔和笑，像邀请对方跟上话题。
含蓄勾引回眸含笑|inviting look-back smile|成年轻转头回看、眼含笑、嘴闭，肩颈只露完整普通衣领。
含蓄勾引低头抬眼|inviting lowered-head upward gaze|成年下巴稍收、视线抬起、眉松、闭唇小笑，正常圆瞳清楚。
含蓄勾引抬眉眨眼|inviting brow-lift wink|成年一眉轻抬、一眼眨、另一眼正常前视，闭唇小笑，玩笑邀约。
含蓄勾引歪头等待|inviting head-tilt waiting look|成年头轻歪、双眼看前方、嘴角浅扬，像等待回答，非夸张张口。
含蓄勾引侧脸停望|inviting three-quarter pause|成年三分之四脸、视线看前侧、眉松、唇闭，面部完整可辨。
含蓄勾引轻抬下巴|inviting lifted-chin smile|成年下巴略抬、目光稳定、嘴角一侧上扬，普通恋爱剧情表演。
含蓄勾引笑眼期待|inviting smiling-eyes expectation|成年眼尾轻弯、眉内侧微抬、嘴闭浅笑，期待交流的非露骨头像。
含蓄勾引抿唇含笑|inviting restrained closed-lip smile|成年唇轻抿、两角上扬、眼前视，表现克制笑意，不咬或舔嘴唇。
含蓄勾引镜框上望|inviting gaze above glasses|成年眼镜略低、双眼从镜框上方看前侧、一眉抬、嘴闭小笑，镜架完整。
含蓄勾引扶镜框|inviting glasses-adjusting smile|成年一手扶镜腿，正常五指、双眼可见、唇闭微笑，手腕完整。
含蓄勾引脸旁招手|inviting small wave beside face|成年一手在脸旁轻招手，正常五指自然展开、腕部完整，眼和嘴含笑。
含蓄勾引脸旁指势|inviting raised-finger gesture|成年一手在脸旁抬起食指与拇指，其余三指自然收起，闭唇浅笑，普通邀约表演。
含蓄勾引掌托脸侧|inviting palm-at-cheek pose|成年一掌轻贴脸侧、另一侧五官完整、眼看前方、嘴闭浅笑，正常指位。
含蓄勾引遮笑侧望|inviting hand-covered smile|成年一手轻遮嘴角、正常五指、眼侧望带笑，露少量闭唇笑角，普通暧昧表演。
''')
for e in CATALOG[start:]:e['aliases']+=['勾引','含蓄勾引','暧昧邀请','暧昧邀约','inviting','flirty invitation']
