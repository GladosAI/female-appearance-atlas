"""Original Chinese appearance vocabulary for game and anime character design."""
CATALOG = []
CATEGORIES = []

def category(key, name, guide, sources):
    CATEGORIES.append(dict(id=key, name=name, guide=guide, source_ids=sources))

def add(key, dimension, text):
    for line in text.strip().splitlines():
        parts = line.strip().split('|')
        if len(parts) not in (3, 4):
            raise ValueError(line)
        name, en, desc = parts[:3]
        CATALOG.append(dict(category=key, dimension=dimension, name=name, en=en, description=desc,
                            note=parts[3] if len(parts)==4 else '', origin='editorial'))

category('hair_cut','发长与剪裁','先确定外轮廓，再拆分前发、侧发、后发；长度以人体地标描述。',['R01','R02'])
add('hair_cut','长度与轮廓', '''
寸短发|buzz cut|发长很短，头部轮廓和发际线直接显露。
精灵短发|pixie cut|耳周与后颈较短，头顶保留可塑造的发束。
耳上短发|ear-length short hair|侧发止于耳朵上部，颈部完全露出。
齐耳短发|ear-length bob|发梢接近耳垂，形成紧凑的头部轮廓。
下巴短波波|chin-length blunt bob|发梢齐至下巴附近，边缘整齐。
内扣波波|inward-curled bob|波波头末端朝颈部或下巴内弯。
外翘短发|flipped-out bob|短发末端朝外翻，轮廓出现上扬小角。
长波波|long bob lob|长度通常介于下巴下方与肩部附近。
及肩发|shoulder-length hair|发梢与肩部相接，容易因肩部支撑出现转折。
锁骨发|collarbone-length hair|发梢落在锁骨附近，可与及肩发相邻过渡。
中长发|mid-length hair|发梢在肩下至胸部附近，具体长度另标。
胸下长发|chest-length hair|后发或侧发抵达胸部下缘附近。
及腰长发|waist-length hair|后发延伸至腰线，运动时尾端滞后明显。
及臀长发|hip-length hair|后发抵达臀部附近，遮挡较多服装背面。
超长发|floor-length fantasy hair|长度接近地面或超过人体，适合夸张设定。|要设定走路与坐下时如何收拢。
齐切直发|blunt-cut hair|同一层发梢形成清楚的水平或弧形边缘。
层次剪裁|layered haircut|不同层的发梢高度错开，形成多层体积。
碎发短剪|shag haircut|以较多短层和不齐边缘形成蓬松剪影。
狼尾层次|wolf cut|头顶与两侧层次较短，后部长度保留。
公主切|hime cut|前侧两束齐切短发，与较长后发形成台阶。
不对称短发|asymmetrical bob|两侧发长不同，正面轮廓明显不对称。
单侧剃短|side shave undercut|一侧或下层剃短，与保留长发形成材质反差。
前短后长发|mullet haircut|额侧区域较短，后颈区域保留长尾。
蘑菇轮廓|bowl cut|发缘围绕头部形成圆钝整片轮廓。
''')
category('hair_bangs','刘海与分缝','刘海、分缝和额头露出量分别记录；前发不能代替整套发型。',['R01','R02'])
add('hair_bangs','刘海', '''
厚齐刘海|blunt bangs|前发较密，发缘在额头形成连续横线。
薄透刘海|wispy bangs|前发分成稀疏细束，额头局部可见。
眉上短刘海|micro bangs|前发止于眉毛上方，额头下部较多露出。
眉下长刘海|long bangs|前发落至眉下或上眼睑附近。
斜刘海|side-swept bangs|前发整体朝一侧斜向流动。
窗帘刘海|curtain bangs|中间分开、两侧向外展开，发缘常由短渐长。
八字前发|outward-swept fringe|两束前发朝外形成八字弧线。
中间尖束|central pointed fringe|前发中部保留一束明显下垂的尖形。
锯齿刘海|choppy bangs|前发边缘以不规则长短形成锯齿节奏。
弧形刘海|arched bangs|前发下缘呈弧线，而非单一水平线。
遮单眼前发|one-eye-covering fringe|一侧较长前发遮住一只眼睛。
长侧帘发|long face-framing sidelocks|两侧前发沿脸颊向下，勾出脸部边界。
''')
add('hair_bangs','分缝与额头', '''
中分|center part|发根分线位于头部中间附近。
偏分|side part|分线偏离中间，两侧发量不等。
深侧分|deep side part|分线明显靠近一侧，另一侧发量较大。
无明显分缝|no visible part|以连续前发或蓬松体积隐藏分线。
后梳露额|slicked-back hair|前发从发际线向后梳，额头露出。
蓬松露额|voluminous swept-back hair|露额同时在头顶保留向上体积。
美人尖发际|widow's peak hairline|前额发际中部有向下的小尖角。
圆弧发际|rounded hairline|发际在额头形成连续圆弧。
''')
category('hair_tie','扎发与编发','标出固定点、编织方向和尾端；正面、侧面、背面都要可解释。',['R01','R02'])
add('hair_tie','扎发', '''
高马尾|high ponytail|固定点较高，发尾从头后上方垂落。
低马尾|low ponytail|固定点在后颈附近，发尾从低处垂落。
中位马尾|mid-height ponytail|固定点介于高马尾与后颈之间。
侧马尾|side ponytail|发束在一侧固定，形成偏置重心。
高双马尾|high twin ponytails|两侧较高处分别固定发束。
低双马尾|low twin ponytails|两束发尾从耳下或后颈两侧垂落。
短双尾|short twin ponytails|两侧尾束较短，主要改变头周轮廓。
半扎发|half-up half-down|上层头发固定，下层仍披散。
半扎马尾|half-up ponytail|上层集中成一束尾巴，下层不束起。
半扎丸子|half-up bun|上层盘成发团，下层保留披发。
高丸子|high bun topknot|发团位于头顶或头后上方。
低盘髻|low chignon|发团在后颈附近，轮廓较紧凑。
双丸子|space buns|左右两侧各盘一团，可保留散落尾束。
侧盘髻|side bun|盘髻放在一侧，配饰也可沿同侧展开。
法式扭髻|French twist|头发向内纵向扭卷，后部形成长条髻。
泡泡马尾|bubble ponytail|尾束分段固定，每段形成鼓起的体积。
环形扎发|looped ponytail|发尾折回固定，形成可见环状发束。
丝带缠发|ribbon-wrapped hair|丝带绕尾束或辫子，固定节距清楚。
''')
add('hair_tie','编发', '''
三股单辫|three-strand braid|三束轮流交叉，形成连续编织节奏。
侧辫|side braid|整条辫子偏向一侧肩前或肩后。
双辫|twin braids|左右两条独立辫子，起点和长度分别记录。
法式辫|French braid|编织时逐步并入邻近发束，通常贴近头皮。
荷兰辫|Dutch braid|发束向下交叉并入，编织体积较突出。
鱼骨辫|fishtail braid|两大束通过反复交叉细束形成细密纹理。
绳索辫|rope braid|两束各自扭转后再互绕，呈螺旋轮廓。
冠状辫|crown braid|辫子绕头部形成环状发冠。
瀑布辫|waterfall braid|横向编织并放出部分发束向下披散。
细辫点缀|accent braids|在披发或扎发中加入少量独立细辫。
贴头分区辫|cornrows|多条紧贴头皮的分区辫，路径与分区清楚。
盒状分区辫|box braids|以方状或类似分区起始的多条独立辫。
''')
category('hair_surface','发质与发色','发质决定线条节奏，发色另记主色、明度和分区；不要把发色当成性格。',['R01','R02'])
add('hair_surface','发质与状态', '''
直发|straight hair|大束方向较直，发梢弯曲可局部添加。
松波浪|loose wavy hair|发束沿较大的连续弧线或S形起伏。
紧卷发|tight curly hair|卷曲节距较小，内部遮挡较多。
螺旋卷|ringlet curls|发束沿立体螺旋绕行，须画出内外侧。
自然紧密卷|coily hair|细密卷曲聚成较强的蓬松体积。
自然蓬松圆发|afro hairstyle|紧密卷发整体形成大而圆的外轮廓。
湿发束|wet hair clumps|发束聚拢、体积降低，局部贴近头皮。
蓬松碎束|fluffy flyaway hair|主发团外有少量细碎发，边缘较轻。
顺滑整束|smooth hair clumps|束与束的边界整齐，高光路径连续。
凌乱发束|messy hair|发束方向有控制地错开，保留主要流向。
发尾内卷|curled-in ends|主要卷曲集中在末端，朝身体内侧收拢。
发尾外翻|flipped ends|末端朝外转折，运动轮廓较展开。
''')
add('hair_surface','颜色与分区', '''
黑发|black hair|低明度主色，以环境色区分受光与暗部。
深棕发|dark brown hair|低明度棕色，阴影仍可保留冷暖变化。
浅棕发|light brown hair|中高明度棕色，需与肤色分开。
金发|blonde hair|以黄色、米色或冷灰金作为主色。
红棕发|auburn hair|棕底带红橙倾向，可强调暖色发束。
银白发|silver white hair|高明度发色，以灰蓝或灰紫建立体积。
灰发|gray hair|灰色可偏冷或偏暖，明度另设。
粉色发|pink hair|幻想或染发色，可用饱和度区分粉色系。
蓝色发|blue hair|幻想或染发色，暗部不必直接涂黑。
紫色发|purple hair|红紫到蓝紫均可，主色相应明确。
绿色发|green hair|幻想或染发色，需与场景植被区分。
双区发色|split-dyed hair|左右或上下两个区域使用不同主色。
挑染|highlight streaks|少量发束与底色不同，路径随发束走向。
内层染|underlayer hair color|下层头发染色，转头或扎发时显露。
渐变染|ombre hair|从发根到发尾逐步变化，过渡区可标。
发尾染|dip-dyed ends|末端一段颜色变化，分界较集中。
白色局部发束|white hair streak|少量白色发束形成识别点。
发根色差|visible hair roots|根部与其余发色不同，反映造型状态。
''')
category('face','脸型与轮廓','这些是绘画轮廓标签；真实脸形连续变化，三视图比单一名字更准确。',['R03','R09'])
add('face','整体脸型', '''
椭圆脸|oval face|脸长大于宽度，下颌向下平缓收窄。
圆脸|round face|脸长与宽较接近，颊部与下颌转折圆缓。
方脸|square face|下颌两角较明确，脸宽与下颌宽接近。
长方脸|rectangular face|纵向长度较长，同时保留较直的两侧。
心形脸|heart-shaped face|额部较宽，下脸向较窄下巴收拢。
菱形脸|diamond face|颧骨区域较宽，额部和下颌较窄。
三角脸|triangle-shaped face|下颌区域相对宽，额部相对窄。
长椭圆脸|long oval face|椭圆轮廓更纵向延伸，转折仍圆缓。
柔和棱角脸|soft angular face|颧骨和下颌有转折，但边缘不过分锐利。
饱满面颊|full cheeks|颊部体积明显，可与多种整体脸型组合。
宽下颌圆下巴|broad jaw rounded chin|下颌宽度较大，但下巴末端圆缓。
短下脸|short lower face|鼻下至下巴的比例较短，不代表实际年龄。
''')
add('face','局部轮廓', '''
圆下巴|rounded chin|下巴末端由弧线连接。
尖下巴|pointed chin|下巴向末端明显收窄。
平宽下巴|broad flat chin|下巴末端较宽，底缘相对平。
高颧轮廓|defined cheekbones|面中外侧有较明显的骨性转折。
柔和下颌|soft jawline|颊部到下巴过渡连续圆缓。
明确下颌角|defined jaw angle|耳下至下巴之间有可辨识的转角。
''')
category('features','五官与耳部','记录形状、位置与尺度；眼、眉、鼻、嘴分开组合，不以种族替代形态。',['R03','R09'])
add('features','眼部', '''
圆眼|round eyes|眼裂相对较高，弧线接近圆形。
杏眼|almond-shaped eyes|眼裂两端收窄，中部较饱满。
细长眼|narrow elongated eyes|眼裂较长，纵向高度较低。
上扬眼尾|upturned eyes|外眼角位置相对高，眉向另记。
下垂眼尾|downturned eyes|外眼角位置相对低，可配多种表情。
单眼皮轮廓|monolid eyelids|上眼睑褶线不明显，勿靠眼裂大小定义。
明显双眼皮|defined eyelid crease|上眼睑褶线清楚，褶线高度另记。
内双褶线|partly hidden eyelid crease|褶线局部被上睑遮住。
较宽眼间距|wide-set eyes|双眼间距相对角色既定比例较大。
较窄眼间距|close-set eyes|双眼间距相对角色既定比例较小。
大虹膜|large irises|虹膜在眼裂中占较大面积，适合简化画风。
小虹膜|small irises|虹膜相对眼裂较小，注视方向更明确。
长上睫毛|long upper eyelashes|上睫毛长度或束感突出。
下睫毛点缀|visible lower eyelashes|下眼缘用少量睫毛加强结构。
异色虹膜设定|heterochromia design|左右虹膜采用不同颜色，单独标注设定。
深色虹膜|dark irises|虹膜明度较低，瞳孔区可用边界分开。
浅色虹膜|light irises|虹膜较明亮，保留瞳孔与眼白区别。
''')
add('features','眉部', '''
平直眉|straight eyebrows|眉身走向接近水平。
弧形眉|arched eyebrows|眉身形成平缓连续弧线。
高眉峰|high-arched eyebrows|眉峰位置或高度较突出。
上挑眉|angled upward eyebrows|眉身整体斜向上扬。
短眉|short eyebrows|眉身长度较短，具体位置另记。
浓眉|thick eyebrows|宽度与毛量较明显。
细眉|thin eyebrows|眉身较窄，线条更轻。
断眉识别点|eyebrow slit|眉身有一小段缺口或造型间隙。
''')
add('features','鼻嘴耳', '''
直鼻梁|straight nose bridge|侧面鼻梁走向相对直。
低鼻梁|low nose bridge|鼻根到鼻尖的前突较低，依视角表现。
高鼻梁|prominent nose bridge|鼻梁前突较明显，侧面轮廓更清楚。
弧鼻梁|convex nose bridge|侧面鼻梁略向外凸。
圆鼻尖|rounded nose tip|鼻尖以圆润体积收尾。
上翘鼻尖|upturned nose tip|鼻尖方向稍上扬，鼻底可见量随视角变。
宽鼻翼|wide nostril wings|鼻翼横向跨度较大。
薄唇|thin lips|上下唇可见厚度较低。
饱满唇|full lips|上下唇体积较明显。
明确唇峰|defined cupid's bow|上唇中部有清楚的双峰结构。
柔和唇峰|soft cupid's bow|上唇中部转折较圆缓。
宽嘴型|wide mouth|嘴宽相对面部比例较大。
小嘴型|small mouth|嘴宽相对面部比例较小。
尖牙设定|fang design|一枚或两枚牙齿突出，用于幻想识别点。
圆耳轮廓|rounded ears|耳轮上缘圆缓，耳部贴附角度另记。
突出耳廓|prominent ears|耳部从头侧伸出较明显。
耳垂贴附|attached earlobes|耳垂与脸侧连接较紧。
悬垂耳垂|free earlobes|耳垂下部轮廓独立悬垂。
''')
category('skin','肤色与外观细节','肤色与表面标记独立记录；保留正常纹理与多种年龄的可见特征。',['R03','R09'])
add('skin','肤色与底色', '''
浅明度肤色|light skin tone|皮肤基础明度较高，阴影仍应保持层次。
中明度肤色|medium skin tone|皮肤基础明度居中，受光与暗面可双向展开。
深明度肤色|deep skin tone|皮肤基础明度较低，高光与反光仍清楚。
暖底色|warm undertone|基础色偏黄、橙或暖红，可与任意明度组合。
冷底色|cool undertone|基础色偏冷红或冷调，可与任意明度组合。
中性底色|neutral undertone|冷暖倾向较均衡，仍受环境光影响。
橄榄色倾向|olive undertone|基础色含较明显的黄绿色倾向。
幻想肤色|fantasy skin color|蓝、紫、绿色等设定色，仍按体积受光。
''')
add('skin','标记与质感', '''
雀斑|freckles|鼻梁、颊部等区域出现小而分散的色点。
面部痣|facial mole|固定位置的色点，可作为角色对照标记。
身体痣|body mole|身体局部稳定小色点，换装时保留位置。
胎记|birthmark|边界与大小可设计，需记录三视图位置。
面部疤痕|facial scar|线状或片状旧痕，随表面体积转折。
身体疤痕|body scar|局部纹理变化，可与故事经历联系。
色素差异斑块|skin pigmentation patches|局部明度或色相不同，以具体轮廓描述。
晒痕|tan lines|服装遮挡造成的肤色分界，边界对应衣物。
纹身|tattoo|图案贴合皮肤表面，动作时随体积变形。
战纹彩绘|war paint|人为涂绘的几何或图腾图形，可随剧情更换。
魔法印记|magical sigil|设定性的图案，标明是否发光与何时出现。
自然毛孔感|subtle skin texture|少量微小纹理帮助写实，不必逐点铺满。
细纹|fine lines|眼角、额部或口周出现细小表面纹理。
明显皱纹|visible wrinkles|面部与颈部有清楚褶纹，方向随肌肉活动。
局部红润|localized blush|颊、耳或关节等区域有较暖颜色。
光泽皮肤|dewy skin finish|较集中高光强调皮肤表面光泽。
哑光皮肤|matte skin finish|高光柔化，体积主要靠明暗交界。
''')
category('expression','表情与妆容','表情使用眉、眼、口的协同变化；妆容是可更换外观层。',['R03'])
add('expression','表情', '''
平静|neutral expression|眉眼口保持松弛，适合作为差分基准。
微笑|gentle smile|嘴角上提，眼周变化根据笑意强弱调整。
大笑|laughing expression|嘴张开，脸颊与眼周共同收缩。
抿嘴笑|closed-mouth smile|唇保持闭合，嘴角与面颊上提。
惊讶|surprised expression|眼睑张开，眉上移，口型可张可闭。
疑惑|confused expression|眉形或头部倾斜表达不确定。
专注|focused expression|视线锁定目标，眉与口部张力明确。
愤怒|angry expression|眉内侧靠拢下压，嘴型体现强度。
悲伤|sad expression|眉内侧可上提，嘴角与眼周张力变化。
害怕|fearful expression|眼眉与口部张力增强，视线可避让。
疲惫|tired expression|眼睑降低，口部与肩部较松弛。
不屑|disdainful expression|可用单侧嘴角或眉变化形成不对称。
坚定|determined expression|视线稳定，眉眼口保持目标明确的张力。
羞赧|bashful expression|目光偏移、嘴部收敛，可加局部红润。
哭泣|crying expression|眉眼口的变化与眼泪同时设计。
眨单眼|winking expression|一侧眼睛闭合，另一侧视线与表情明确。
''')
add('expression','妆容', '''
自然淡妆|natural makeup|少量颜色修饰，五官结构仍清楚。
清晰眼线|defined eyeliner|沿眼缘强调轮廓，外延长度另记。
上扬眼线|winged eyeliner|外眼角向外上方延伸一小段线。
烟熏眼妆|smoky eye makeup|眼周用柔化深色形成渐变。
单色眼影|monochrome eyeshadow|以一个主色描绘上睑色块。
亮片眼妆|glitter eye makeup|局部颗粒高光作为重点，低清时适度简化。
柔色唇妆|soft lip color|唇色与肤色反差较小。
深色唇妆|dark lipstick|嘴唇与周围皮肤形成较强明度反差。
渐变唇妆|gradient lip makeup|唇色由内向外或由中间向边缘变化。
面颊腮红|cheek blush makeup|人为设置色区，位置与边界应统一。
面部彩绘|face paint|图案覆盖面部表面，可为仪式或舞台造型。
舞台重妆|stage makeup|加大五官色块反差，适应较远观看距离。
''')
category('body','体型与比例','身高、骨架、肌肉量、软组织和头身比是独立轴；轮廓标签不是健康判断。',['R09','R04'])
add('body','体型', '''
矮个纤细|short slender build|身高较低且横向体积较窄，保持设定年龄比例。
高个纤细|tall slender build|身高较高且体积较窄，四肢长度另设。
中等体格|medium average build|作为一组角色的相对基准，不定义唯一标准。
运动体格|athletic build|肌肉线条与稳定支撑较明显，比例可多样。
强壮体格|muscular sturdy build|肩背、躯干或四肢肌肉体积较突出。
饱满体格|fuller soft build|软组织体积较丰富，轮廓转折较圆缓。
胯部较宽|wider hips narrower shoulders|髋部相对肩部较宽，腰线单独设定。
肩部较宽|broad shoulders narrower hips|肩部相对髋部较宽，四肢体积另设。
肩胯接近|balanced shoulder hip width|肩与髋跨度接近，腰部收束程度另记。
腰部较直|straight waist silhouette|腰侧收束较少，躯干形成较直轮廓。
腰部明显收束|defined waist silhouette|腰侧相对胸廓与髋部明显向内收。
厚实躯干|thick torso build|胸廓与腹部前后或横向体积较大。
细窄骨架|narrow skeletal frame|肩胯与关节宽度偏窄，软组织量可不同。
宽阔骨架|broad skeletal frame|肩胯与关节跨度较宽，肌肉量可不同。
''')
add('body','绘画比例与局部', '''
五至六头身风格|five to six head stylization|头部相对身体较大，是画风比例设定。
六至七头身风格|six to seven head stylization|常用于较简化角色，实际比例需三视图固定。
七至八头身风格|seven to eight head stylization|头部相对较小，适合常规成人风格设定。
八头身以上风格|elongated fashion proportions|适度拉长躯干或四肢，属于风格化选择。
长腿比例|long-leg proportions|下肢相对躯干更长，注意髋点位置。
长躯干比例|long-torso proportions|躯干相对下肢更长，腰线需配合。
细长颈部|long slender neck|颈段较长且横向较窄，支撑点仍可信。
短厚颈部|short thick neck|颈段较短且较宽，肩颈过渡明确。
平缓肩线|gently sloping shoulders|从颈根到肩端缓慢向下倾斜。
较平肩线|level shoulder line|肩部走向相对平，衣物结构可继续加强。
手部细长|long slender hands|指长与掌部比例偏长，关节位置保持一致。
手部宽厚|broad hands|掌宽和指体积较明显，握持道具时保留体积。
''')
category('pose','体态与动作','先画重心、支撑点和动作线，再处理肢体；静态体型与瞬时姿态分别记录。',['R04','R09'])
add('pose','静态姿态', '''
双脚均衡站立|neutral standing pose|身体重量由双脚共同支撑，适合三视图基准。
单腿承重|contrapposto pose|一腿主要承重，髋部与肩部可有反向倾斜。
单手叉腰|one hand on hip|手掌与腰侧接触，肘部改变侧面剪影。
双手叉腰|both hands on hips|双肘向两侧展开，躯干姿态需配合。
松弛抱臂|loosely crossed arms|前臂交叉在胸前，保留手臂遮挡关系。
双手身前交叠|hands clasped in front|双手在身前汇合，肩部通常较收敛。
双手背后|hands behind back|手臂后移，侧视图要交代肩肘位置。
手指托下巴|hand on chin|手与下巴有明确接触，头颈受力自然。
侧头倾听|head tilt listening|头部侧倾，颈部与肩线共同调整。
抬头注视|looking upward pose|头颈向上转，五官随俯仰角变化。
低头阅读|looking down reading|颈部前屈，书或屏幕与视线对应。
前倾观察|leaning forward pose|上身前倾，通过脚位或手部获得支撑。
靠墙休息|leaning against wall|墙面是支撑点，重心可部分离开脚底。
直坐|upright seated pose|骨盆坐稳，双脚或其他接触点有支撑。
侧坐|sideways seated pose|骨盆与腿部朝一侧，躯干可回转。
交腿坐|cross-legged chair pose|坐在椅上交腿，交叠与受压位置明确。
盘腿坐|cross-legged floor pose|双腿在身前弯曲，坐骨与地面接触。
单膝跪|one-knee kneeling|一膝与一脚支撑，髋点高度需对应。
双膝跪坐|kneeling seated pose|膝与小腿参与支撑，衣物褶皱聚于屈曲处。
蹲姿|squatting pose|髋膝屈曲，脚底或前脚掌承重。
''')
add('pose','运动与手势', '''
自然行走|natural walking pose|双侧肢体交替摆动，重心向前转移。
快跑|running pose|身体可前倾，落地与腾空阶段交替。
跳跃|jumping pose|腾空姿态由起跳方向决定，落地点另设。
回头|looking back pose|头颈与躯干有回转，面部仍贴合颅骨。
转身|turning pose|髋、肩和头部回转顺序可错开。
伸手指向|pointing gesture|手臂方向与角色注视或说明目标对应。
抬手施法|raised-arm casting pose|一臂向上或前方展开，指尖与法术焦点对应。
双手持书|holding book with both hands|书的重量与手指接触关系清楚。
双手持杖|two-handed staff pose|两手握点有间距，杖与身体遮挡关系稳定。
单手持伞|holding umbrella|手、伞柄与伞面重心连贯。
握拳准备|clenched-fist ready pose|手指闭合合理，手腕与前臂方向连贯。
护住同伴|protective gesture|身体与手臂挡在目标前，朝向清楚。
挥手|waving gesture|手掌向目标，肩肘腕形成连贯摆动。
提裙行走|lifting skirt gesture|手抓住布料，受力褶线朝握点汇聚。
整理头发|adjusting hair gesture|手与发束接触，发束在接触点弯折。
整理眼镜|adjusting glasses gesture|手指触及镜框或镜腿，镜框结构保持。
拉弓|archery draw pose|握弓、拉弦和肩背受力关系明确。
拔剑|drawing sword pose|剑柄、鞘口和手臂方向相互对应。
悬浮|levitating pose|无地面支撑时，用发束、衣摆与重心解释运动。
收翼落地|winged landing pose|脚步与翼面共同体现减速，接地姿势可信。
''')
category('tops','上装','上装记录长度、松量、闭合方式与袖型；袖领细节在服装结构类组合。',['R05','R06','R07'])
add('tops','常用上装', '''
圆领T恤|crew-neck T-shirt|针织短袖上衣，领口为较小圆弧。
宽松T恤|oversized T-shirt|肩线与衣身较宽，垂落体积明显。
长袖T恤|long-sleeve T-shirt|袖长至腕附近，弹性和松量另设。
背心|tank top|无袖上衣，肩带宽度与领口另记。
衬衫|button-up shirt|前中开襟，常有领、袖口与纽扣。
衬衫式女上衣|blouse|可用轻薄面料、装饰领或柔和袖型。
高领针织衫|turtleneck knit top|领部包住颈段，针织纹理随体积转。
套头毛衣|pullover sweater|从头部套穿的针织上衣，松量可多样。
开襟针织衫|cardigan|前中可打开，纽扣或其他闭合件另设。
连帽卫衣|hoodie|带兜帽的针织上衣，帽体在背面形成体积。
圆领卫衣|crew-neck sweatshirt|较厚针织上衣，领袖下摆常有罗纹。
短款上衣|cropped top|衣摆位置高于常规腰臀区，叠穿可补足覆盖。
长款上衣|tunic top|上衣延伸至髋部或大腿附近，可配裤装。
裹身上衣|wrap top|两片前襟交叠，通过系带或扣件固定。
束腰马甲|fitted waistcoat|无袖开襟上装，沿躯干收束。
宽松背心马甲|loose vest|无袖外层，功能口袋或保暖材质可添加。
针织背心|sweater vest|无袖针织层，可叠在衬衫或T恤外。
围裙式上装|apron top|通过肩带与腰带覆盖前身，背部结构另画。
束身式上装|corset-inspired top|用分片与支撑线形成结构感，标明是否功能束身。
水手领上装|sailor-collar top|背部方领与前部交叠或系结构成识别点。
立领上装|stand-collar top|领片从领口向上立起，开口结构另设。
交领上衣|cross-collar top|左右衣襟斜向交叠，压叠方向应固定。
运动拉链上衣|zip-up sports top|前中拉链，袖和躯干松量适应运动。
舞台装饰上衣|stage costume top|用局部反差与装饰突出远距离识别。
工作服上衣|workwear shirt|较结实材质、功能口袋与耐磨部位明显。
''')
category('bottoms','裙装与裤装','腰位、长度、裤腿或裙摆形状分开记录；活动范围由结构决定。',['R05','R06','R07'])
add('bottoms','裙装', '''
A字裙|A-line skirt|从腰臀向下逐渐展开，轮廓接近A形。
直筒裙|straight skirt|腰臀下方轮廓较直，开衩可提供活动量。
铅笔裙|pencil skirt|贴合臀部并向下收窄，长度另记。
百褶裙|pleated skirt|规则褶线围绕腰部展开，褶型与节距固定。
圆裙|circle skirt|以较大圆弧展开，摆动时体积较宽。
裹身裙|wrap skirt|前片交叠，通过系带或扣件固定。
多层荷叶裙|tiered ruffle skirt|不同高度的荷叶层叠加，边缘节奏明显。
蛋糕层裙|tiered gathered skirt|裙身分层接缝，各层可有抽褶扩量。
不对称裙摆|asymmetric hem skirt|左右或前后长度不同，三视图需一致。
鱼尾裙|mermaid skirt|臀腿段较收束，接近下摆处展开。
高腰裙|high-waisted skirt|腰头位置高于角色自然腰线。
长及踝裙|ankle-length skirt|裙摆接近踝部，走路与鞋面遮挡明确。
''')
add('bottoms','裤装', '''
直筒裤|straight-leg trousers|裤腿上下宽度变化较小。
紧身裤|fitted trousers|裤腿贴合体表，关节附近拉伸明显。
阔腿裤|wide-leg trousers|从髋或大腿向下保留较大松量。
锥形裤|tapered trousers|上部较宽，裤腿向脚踝收窄。
喇叭裤|flared trousers|膝下或腿部下段向外展开。
工装裤|cargo pants|腿侧功能口袋形成清楚外形。
牛仔裤|jeans|丹宁材质，腰头、铆钉或袋位可简化记录。
运动裤|joggers|较宽松裤身，脚口常有收束。
打底裤|leggings|弹性贴身裤，表面褶皱少且集中于屈曲处。
短裤|shorts|裤腿止于大腿区，长度和松量另记。
裙裤|culottes|裤腿较宽，从部分角度呈裙状轮廓。
背带裤|overalls dungarees|裤身通过肩带与胸前片连接。
高腰裤|high-waisted trousers|腰头高于自然腰线，裤型仍可多样。
骑装裤|riding breeches|裤型围绕骑乘活动与靴筒结构设计。
''')
category('onepiece','连身服装','先确定整件服装的轮廓、腰线与开合方式，再叠加装饰。',['R05','R06','R07','R08'])
add('onepiece','连身版型', '''
A字连衣裙|A-line dress|从上身或腰线向下逐渐展开。
直筒连衣裙|shift dress|腰部收束少，上下轮廓较连续。
合身连衣裙|sheath dress|较贴合躯干与髋部，裙摆扩量有限。
裹身连衣裙|wrap dress|前身交叠形成斜线，用系带或扣件固定。
高腰长裙|empire-waist dress|腰线移至胸下附近，下方裙身垂落。
衬衫裙|shirt dress|保留衬衫领与前襟结构，延伸成裙身。
背心裙|sleeveless dress|无袖连衣裙，肩带和领口可多样。
背带裙|pinafore dress|肩带连至裙身，常与内搭上衣组合。
针织裙|knit dress|针织材质形成柔和贴合或垂落轮廓。
宽摆礼服|ball gown|上身与大体积裙摆形成明确对比。
鱼尾礼服|mermaid gown|躯干与腿段收束，下部向外展开。
拖尾礼服|train gown|裙后延伸形成拖尾，站姿与走动长度需标。
连体裤|jumpsuit|上身与裤身连接，开合位置要可使用。
连体短裤|romper playsuit|上身与短裤连接，腰线与袖型另设。
工作连体服|coveralls|功能开襟与袋位明确，松量适合活动。
运动连体服|athletic unitard|弹性连身结构，叠穿和覆盖范围按用途设计。
睡袍|robe dressing gown|宽松开襟连身衣物，以腰带或扣件固定。
长袍|long robe|衣身较长，袖、开襟和活动开口另记。
中式旗袍灵感裙|qipao-inspired dress|可借用立领、斜襟和修长轮廓，明确创作改编。
交领襦裙灵感|hanfu-inspired ruqun|交领上衣与长裙组合成传统服饰灵感造型。
和服灵感袍|kimono-inspired robe|T形宽袖轮廓与宽腰带组成识别点，改编须标。
裙撑轮廓礼服|bustle-inspired gown|背部支撑使裙后突出，区别于单纯宽摆。
''')
category('outerwear','外套与披覆','外层决定大轮廓；画出与肩部的接触、固定点和背面长度。',['R05','R06','R07'])
add('outerwear','外层', '''
西装外套|blazer|领襟与肩部结构清楚，可合身或宽松。
风衣|trench coat|长外套配腰带、领襟与扣件，细节可按设定简化。
长大衣|long coat|厚材质延伸至膝下或更长，摆动体积明显。
短大衣|short coat|衣摆在髋部或大腿上部附近。
飞行夹克|bomber jacket|较短衣身，袖口与下摆常收束。
牛仔夹克|denim jacket|较硬挺丹宁，袋位与拼缝形成结构线。
皮夹克|leather jacket|光泽与硬挺折线突出，领型和拉链另设。
运动夹克|track jacket|轻便外层，拉链与袖侧分区可形成节奏。
羽绒外套|puffer jacket|填充与绗缝分区形成鼓起体积。
雨衣|raincoat|表面与闭合结构强调防雨用途。
派克外套|parka|较长保暖外层，帽体和口袋可较大。
斗篷|cape|披在肩上而无常规袖管，前部固定方式另设。
连帽斗篷|hooded cape|斗篷与兜帽相接，帽落下时体积清楚。
短披肩|capelet|长度较短的肩部披覆，改变肩部轮廓。
披巾|shawl|大块布料绕肩或上身，褶线朝搭接点汇聚。
围裹披布|wrap shawl|通过围绕与交叠贴合身体，固定点要明确。
短款礼服外套|bolero jacket|衣身较短，可仅覆盖肩臂与上胸。
无袖长外套|long sleeveless coat|保留长衣身与开襟，无常规袖管。
袍式外套|robe coat|宽松衣身与系带形成连贯垂落轮廓。
分层法袍|layered mage robe|内外层长度错开，动作时须分清遮挡。
''')
category('construction','领袖与服装结构','结构部件可以跨衣物组合；使用准确的开口、连接和受力关系。',['R05','R06','R12'])
add('construction','领口', '''
圆领|round neckline|领口形成圆弧，深浅与贴合量另记。
V领|V neckline|领口两侧向下汇成V形。
方领|square neckline|领口以较明确的水平与竖向转折构成。
船领|boat neckline|领口横向展开，通常较浅。
心形领|sweetheart neckline|前领形成两个圆弧向中部汇合。
高领|high neckline|领口高度较高，可贴颈或留空。
立领|stand collar|领片从领口向上竖立。
翻领|turn-down collar|领片翻折，能看见折线与领片外缘。
彼得潘领|Peter Pan collar|较平贴的圆钝领片围绕领口。
水手领|sailor collar|背部较大方领片与前部结构相连。
荷叶领|ruffled collar|领边通过褶量形成起伏。
斜肩领|one-shoulder neckline|左右肩部覆盖不对称。
''')
add('construction','袖型', '''
无袖|sleeveless|袖窿直接收边，腋下开口结构需明确。
贴身长袖|fitted long sleeves|袖管贴合手臂，肘部褶皱集中。
泡泡袖|puff sleeves|袖局部抽褶鼓起，膨起区域另记。
羊腿袖|leg-of-mutton sleeves|上袖较大、向前臂收窄，轮廓有明显对比。
喇叭袖|bell sleeves|袖口方向逐渐展开。
灯笼袖|lantern sleeves|袖中段鼓起，两端收束。
宽直袖|wide straight sleeves|袖管保持较宽，垂落边缘与手臂分离。
蝙蝠袖|batwing sleeves|袖下缘与衣身相连，腋下位置较低。
插肩袖|raglan sleeves|袖片接缝斜向连接领口附近。
落肩袖|dropped-shoulder sleeves|肩缝下移至上臂附近。
分离袖|detached sleeves|袖体与上装分开固定，连接点需说明。
开衩袖|slit sleeves|袖管局部打开，动作时开口会展开。
''')
add('construction','腰摆与闭合', '''
自然腰线|natural waistline|服装腰部标记接近角色自然腰位置。
高腰线|raised waistline|腰部标记高于自然腰位。
低腰线|dropped waistline|腰部标记低于自然腰位。
腰部抽褶|gathered waist|布料在腰部汇聚，褶线从固定线展开。
公主线分片|princess seams|纵向弧形分片塑造上身贴合。
腰下荷叶|peplum|腰部附近向外展开一段短衣摆。
侧开衩|side slit|侧缝局部开放，为活动或造型提供空间。
前短后长衣摆|high-low hem|前摆较短、后摆较长，侧面过渡应连续。
纽扣开襟|button fastening|用纽扣与扣眼闭合，间距与受力对应。
拉链闭合|zip fastening|连续齿链沿指定开口闭合。
系带闭合|lace-up fastening|系带穿过成对孔位或环，走向可追踪。
腰带固定|belt fastening|围绕腰部固定，扣件和剩余带尾清楚。
''')
category('footwear','鞋袜与手套','鞋底、鞋面和闭合件共同决定轮廓；鞋与脚的接触、靴筒与关节关系要合理。',['R06','R07'])
add('footwear','鞋靴', '''
运动鞋|sneakers|鞋底与鞋面分层，适合多种现代造型。
帆布鞋|canvas shoes|布面鞋身较轻，胶底轮廓较明确。
乐福鞋|loafers|无鞋带低帮鞋，鞋面跨带可简化。
芭蕾平底鞋|ballet flats|鞋口较浅、鞋底较薄，足背露出较多。
玛丽珍鞋|Mary Jane shoes|鞋面跨带固定，跨带数量与位置可变。
牛津系带鞋|Oxford shoes|低帮系带结构较紧凑，鞋翼与鞋面连接明确。
低跟鞋|low-heeled shoes|鞋跟高度较低，脚弓仍与鞋型匹配。
高跟鞋|high heels|鞋跟抬高后足，脚姿与前掌支撑需对应。
厚底鞋|platform shoes|前后鞋底整体较厚，区别于只有高鞋跟。
坡跟鞋|wedge shoes|鞋底从前掌到后跟连续增厚。
凉鞋|sandals|带条与开口形成鞋面，脚部接触点明确。
拖鞋|slippers|后跟或鞋口较开放，步态要考虑固定不足。
踝靴|ankle boots|靴筒止于脚踝附近。
中筒靴|mid-calf boots|靴筒止于小腿中段。
及膝靴|knee-high boots|靴筒接近膝部，屈膝时边缘位置明确。
过膝靴|over-the-knee boots|靴筒跨过膝部，需要屈曲活动结构。
系带战靴|lace-up combat boots|较厚底与系带形成实用轮廓。
骑乘靴|riding boots|靴筒与裤装配合，鞋底与跟型适应设定。
木屐灵感鞋|geta-inspired footwear|台座与带条形成传统鞋履灵感，明确改编。
幻想护甲靴|armored boots|硬片与柔性关节分区，避免全腿硬壳。
''')
add('footwear','袜与手套', '''
短袜|ankle socks|袜口位于脚踝附近。
中筒袜|crew socks|袜口在小腿较低至中段。
及膝袜|knee socks|袜口接近膝下。
过膝袜|over-knee socks|袜口在膝上，长度与角色比例对应。
连裤袜|tights|腰部到脚部连续覆盖，材质与不透明度另记。
网格袜|fishnet tights|开放网格沿体积转，低清画面宜简化。
护腿套|leg warmers|覆盖部分小腿或踝部，可与袜鞋叠加。
短手套|wrist-length gloves|覆盖手部至手腕，手指分区清楚。
长手套|long gloves|手套延伸至前臂或肘上，长度另记。
露指手套|fingerless gloves|指部局部开放，掌部与固定结构明确。
连指手套|mittens|部分手指共用一个套体，拇指独立。
护腕|wrist guards|腕部局部固定或防护，开合方式另设。
''')
category('accessories','饰品与随身物','先确定固定与悬挂方式，再记录材质和大小；配饰轮廓应经得住缩略图。',['R06','R07'])
add('accessories','头部', '''
发带|hair band|带状物围绕或固定头发，宽度和打结点明确。
发箍|headband|硬或半硬弧形支撑围绕头顶。
大蝴蝶结|large hair bow|两个环与带尾形成头部识别点。
小发夹|hair clip|局部夹住发束，位置与开合方向明确。
花形发簪|flower hairpin|花体装饰通过簪或夹固定在发束。
长发簪|hair stick|长杆穿入盘发固定，穿插位置可追踪。
装饰梳|decorative hair comb|梳齿插入发束，上方保留装饰体。
贝雷帽|beret|软圆帽体偏置或平戴，帽缘与头部接触。
棒球帽|baseball cap|帽冠与前檐形成固定结构。
宽檐帽|wide-brimmed hat|檐部横向展开，透视和遮光明显。
软边帽|soft bonnet|帽体贴合后脑或脸侧，系带固定。
兜帽|hood|衣物相连的帽体，放下时落在后颈。
尖顶魔女帽|pointed witch hat|高尖帽冠与宽檐组成强剪影。
小冠饰|tiara|局部冠架位于前额或头顶，固定方式另设。
面纱|veil|轻薄布覆盖部分头脸，边缘固定点清楚。
圆框眼镜|round glasses|圆形镜片与鼻梁、镜腿相连。
方框眼镜|rectangular glasses|角形镜框改变面部局部节奏。
护目镜|goggles|镜框、软垫与固定带形成立体体积。
眼罩|eyepatch|覆盖单眼的片体，通过带条固定。
面罩|face mask|遮住部分面部，贴合点与呼吸开口另设。
''')
add('accessories','身体与随身物', '''
吊坠项链|pendant necklace|链条或绳悬挂吊坠，垂落方向受重力影响。
贴颈项饰|choker|环绕颈部，闭合件与松量明确。
长链项饰|long necklace|链条延伸至胸前较低处，动作时可摆动。
耳钉|stud earrings|体积较小，固定在耳部穿孔位置。
垂坠耳饰|drop earrings|悬挂体向下垂落，动态时发生摆动。
耳夹|ear cuffs|沿耳廓夹附，接触位置明确。
胸针|brooch|针或扣固定在衣料上，衣物可有局部受力。
徽章|badge|图案与边框作为组织或身份识别点。
手链|bracelet|环绕手腕，可紧贴或松挂。
戒指|ring|套在指定指节附近，厚度与手指对应。
围巾|scarf|围绕颈部或肩部，布尾方向受风与运动影响。
领结|bow tie|环与结位于领口，结构可对称或偏置。
领带|necktie|长条垂落于胸前，结体与领口相连。
腰封|waist sash|较宽布带包覆腰部，结与尾带可另设。
功能腰带|utility belt|袋包和扣件沿带体固定，重量分布合理。
肩带斜包|crossbody bag|带条斜跨躯干，包体与带端连接明确。
手提包|handbag|提把与包体相连，手部握持点受力清楚。
小背包|small backpack|背面包体通过肩带固定，背视图完整。
腰包|belt pouch|小包固定在腰带或带环上。
扇子|folding fan|折叠扇骨沿枢轴展开，握点与角度明确。
阳伞|parasol|伞骨支撑伞面，柄与手部相接。
怀表|pocket watch|表体与链条组成随身物，链条固定端明确。
法术书|spellbook|书脊、封面与页块可辨，符号作为原创设计。
法杖|magic staff|杆体、握持区与头部装饰结构明确。
''')
category('materials','材质与纹样','材质用厚薄、软硬、重量、光泽描述；纹样按平面位置和重复尺度记录。',['R05','R11','R06'])
add('materials','材质', '''
棉布感|cotton fabric|可呈柔软哑光表面，褶皱取决于厚度与织法。
麻布感|linen fabric|可强调可见织纹与较明确的折痕。
羊毛呢料|wool suiting fabric|较厚哑光体积，边缘与折线较稳定。
粗针织|chunky knit|线圈与厚度形成较大尺度纹理。
细针织|fine knit|细密纹理，贴合与弹性表现较突出。
丹宁|denim|较硬挺织物，拼缝与磨损区可形成反差。
丝质感|silk-like fabric|表面和垂落随织法变化，别把丝纤维等同固定光泽。
缎面|satin surface|较平滑高光随曲面延伸，属于织物表面效果。
雪纺感|chiffon-like fabric|轻薄飘动，遮挡与叠层可改变不透明度。
薄纱|tulle mesh|细网结构可轻而蓬松，多层产生体积。
蕾丝|lace|镂空纹样与边缘轮廓相互配合。
天鹅绒|velvet|短绒表面对方向和受光敏感，明暗变化较柔。
皮革感|leather-like material|光泽和折线取决于软硬与表面处理。
漆面革感|patent leather finish|镜面高光较强，色块边界清楚。
仿毛绒|faux fur|毛向与边缘体积明显，低清时按大团概括。
金属硬片|metal plates|硬边与集中反光突出，关节区需柔性连接。
绗缝填充|quilted padded fabric|分格缝线约束填充，格内体积鼓起。
透明薄膜|clear film material|用边缘、反射和遮挡表示，不能简单省掉轮廓。
发光织物设定|emissive fabric design|发光区域与基础材质分别设定。
''')
add('materials','纹样与装饰工艺', '''
纯色|solid color|大面积同色，以体积与材质建立变化。
条纹|stripes|平行纹样随衣物弯曲，节距固定。
格纹|checks plaid|纵横交织重复，透视中格宽变化。
圆点|polka dots|圆点按间距重复，受曲面影响发生压缩。
花卉纹|floral pattern|花叶组成重复或局部构图。
叶片纹|leaf pattern|叶脉与叶形形成植物节奏。
星月纹|star and moon pattern|星与月形作为原创符号，不必满布。
几何纹|geometric pattern|线、面与重复构件建立视觉秩序。
动物纹灵感|animal-inspired pattern|抽取条纹或斑点特征，纹样尺度单独记录。
刺绣|embroidery|线迹与布面相接，可略微凸起。
珠绣|beadwork|珠体沿布面固定，重量影响垂落。
亮片|sequins|小片重复反光，低清时保留整体亮区。
流苏|fringe tassels|多个垂条从固定边缘悬下。
荷叶边|ruffle trim|沿边缘增加褶量，形成连续起伏。
滚边|piping trim|细窄条沿边或缝线突出结构。
绑带|straps|带状构件连接或固定部位，不能任意穿入身体。
拼色|color-blocking|不同面片使用不同颜色，分界随结构走。
透明叠层|sheer overlay|外层透出内层，以边缘和色差体现。
做旧磨损|weathered finish|磨损集中在接触与受力部位。
破损修补|patched repair|补丁和缝线交代材料的使用状态。
''')
category('style','整体风格与主题','风格是若干元素的组合；名称用于创作检索，不宣称涵盖所有亚文化。',['R06','R07','R08'])
add('style','造型方向', '''
日常简约|minimal casual character design|干净剪裁与少量配饰，重点放在轮廓差异。
学院灵感|academia-inspired outfit|衬衫、针织层、裙裤与书包等形成学习环境线索。
都市通勤|urban office outfit|西装、衬衫与利落鞋包形成职业场景线索。
运动休闲|athleisure outfit|运动服结构与日常配饰混合。
街头层搭|streetwear layering|宽松量、叠层和功能配饰形成轮廓。
机能装备|technical utility outfit|扣带、功能袋与活动分区有具体用途。
工装实用|workwear-inspired outfit|耐磨材质、工具位置与简洁结构相互配合。
田园布艺|pastoral outfit|柔和布料、植物纹样与方便活动的层次。
优雅礼装|formal elegant outfit|礼服结构、统一材质与少量重点首饰。
复古学院|retro academic outfit|历史感剪裁与学院物件组合，具体年代另标。
哥特灵感|gothic-inspired character design|深色、尖拱或金属饰件可组合，避免只靠黑色。
甜系洛丽塔时尚|sweet Lolita fashion-inspired outfit|膝附近蓬裙、装饰领与头饰组合，明确服装风格用途。
古典洛丽塔时尚|classic Lolita fashion-inspired outfit|较克制的复古裙装、图案与配饰组合。
朋克灵感|punk-inspired outfit|皮革感、金属件、破损与不对称可建立节奏。
蒸汽幻想|steampunk-inspired outfit|历史感衣物与架空机械装置结合，功能关系需清楚。
未来都市|futuristic urban outfit|简洁分区、技术材质与装备构成架空城市造型。
偶像舞台|idol stage outfit|鲜明重点色、舞台识别点与动作适应性结合。
军服灵感|military-inspired outfit|肩章、带具与整齐结构用作架空组织线索。
冒险旅装|adventurer travel outfit|携行、保暖、防护与地形需求决定装备。
魔女|witch character design|帽、披覆、法器可择其一作为主识别点。
法师学者|scholar mage design|书、笔记工具与施法结构相互联系。
圣职灵感|cleric-inspired fantasy outfit|袍服、徽记与仪式物件形成架空宗教线索。
轻甲战士|light-armored fighter|硬片保护重点部位，关节保持活动范围。
重甲战士|heavy-armored fighter|较大护甲体积与承重关系清楚，仍保留关节。
游侠弓手|ranger archer design|弓、箭袋与便于移动的服装结构组合。
医护职业灵感|healer medical-inspired outfit|工作服、工具与卫生需求形成职业线索。
厨师职业灵感|chef-inspired outfit|围裙、帽或工具反映工作场景。
中式幻想|Chinese-inspired fantasy design|明确借用的交领、裙装或饰件，时代混合要标。
和风幻想|Japanese-inspired fantasy design|袍袖、腰带或发饰作为灵感，改编与实物分开。
冬季旅装|winter travel outfit|保暖层、帽手套与鞋靴围绕寒冷环境配置。
夏季轻装|summer lightweight outfit|透气、轻材质与遮阳物围绕环境配置。
海港旅装|harbor travel outfit|防潮、携行与海风下的衣摆发束形成线索。
''')
category('fantasy','幻想外观扩展','额外器官与装置要有接点、活动范围和遮挡；区分生长器官与可穿戴饰件。',[])
add('fantasy','身体与装置', '''
精灵尖耳|elf ears|耳廓拉长收尖，根部仍与头侧连接。
兽耳|animal ears|说明是额外耳对还是替代耳，耳根与发束关系固定。
角|horns|标明根部、方向与材质，头部运动时随颅骨转。
鹿角状分枝|antler-like branches|主干与分枝有连续结构，避免随机漂浮。
尾巴|tail|尾根与身体连接，长度与重心影响坐姿。
羽翼|feathered wings|翼根、主骨与羽层明确，展开与收拢都要设计。
膜翼|membranous wings|骨架支撑膜面，折叠区与身体接点清楚。
透明昆虫翼|insect-like wings|翼脉与根部形成薄翼结构，数量另记。
光翼|light wings|设定为光场或实体，遮挡与投光规则固定。
鳞片局部|localized scales|沿体表分区铺排，方向与关节变形一致。
绒毛局部|localized fur|边缘毛向与生长区域清楚。
机械义肢|mechanical prosthetic limb|连接、关节与受力方向清楚，按角色功能设计。
发光眼|glowing eyes|发光区与普通眼部结构分开，失去亮光时仍可辨。
竖向瞳孔|vertical slit pupils|瞳孔形状设定改变，虹膜与视线仍一致。
星形瞳孔|star-shaped pupils|幻想瞳孔图形，近景与远景可用不同细节量。
漂浮光环|floating halo|说明与头部是否锁定，遮挡和位置规则稳定。
悬浮发饰|floating head ornament|可漂浮的道具需规定悬停距离与运动延迟。
星云发束|nebula hair design|以星云或光粒构成发束，仍保留整体流向。
元素发尾|elemental hair tips|发尾转为火焰、水或叶片，转变边界明确。
环绕符文|orbiting runes|符文轨道与角色身体有明确空间关系。
透明肢体设定|translucent limb design|定义透出什么与折射程度，关节仍连贯。
变身分区|transformation zones|不同状态的外观变化按部件记录，便于差分。
''')
