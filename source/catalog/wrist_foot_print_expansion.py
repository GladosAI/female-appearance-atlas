"""Edition 10: wrist/hand/ankle ornaments, adult foot drawing and textile graphics."""
from catalog_content import CATALOG, category, add

def block(key, dimension, text, aliases=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['aliases']=list(aliases)
        if key=='feet':e['age_context']='成年女性足部绘画参考'
        if key in ['clothing_prints','print_styles']:e['pattern_reference']=True

category('watches','腕表与佩戴结构','表壳、表盘、表带与扣件分别观察；全为原创无品牌外观，不据图判断功能性能。',['R60','R54'])
category('rings','指环与戒面结构','按环身结构、开口、戒面与镶嵌轮廓区分，展示完整指环及侧面高度。',['R54'])
category('bracelets','腕部环链与扣件','硬环、开口手环、软链、编带与腕背连接件分别收录；留意闭合和连接方式。',['R54'])
category('bead_bracelets','串珠腕饰','比较珠形、颗数密度、排列、隔珠、结绳和多圈结构；均为原创装饰，不赋予宗教或功效含义。',['R54'])
category('anklets','踝部与足部饰件','足环、脚链、踝带、趾环与足背链按位置和连接方式比较，以完整产品为主。',['R54'])
category('feet','足部形态与绘画','成年女性足部的轮廓、趾端、趾甲、观察角度和动作参考；形态连续变化，名称描述画面，不作健康或测量标准。',[])
category('clothing_prints','衣物图案与排列','将几何、植物、叙事题材和衣物上的排布分开；图案均为原创印花效果，不混同织纹或刺绣构造。',['R57','R58','R59'])
category('print_styles','印花视觉风格','比较审美、线条、色块、笔触与表面效果；是可组合的视觉参考，图例不代表真实生产工艺配方。',['R57','R58','R59'])

block('watches','表壳与表盘轮廓','''
圆壳双针极简腕表|round two-hand minimalist watch|圆形薄壳，双针与短刻度，表冠、表耳和完整窄皮带。
方壳圆角指针腕表|rounded square analog watch|圆角方壳内有指针盘，四角厚度与两端表耳可见。
长方竖盘细带腕表|vertical rectangular slim-strap watch|长方竖表盘配细带，壳长明显大于壳宽，侧冠清楚。
椭圆横盘链带腕表|horizontal oval chain watch|横向椭圆表壳，两侧以小链节接完整细链带。
酒桶轮廓弧壳腕表|tonneau curved-case watch|两侧外鼓、上下收窄的酒桶壳，弧面与表带连接清楚。
八角切面金属腕表|octagonal faceted watch|八角棱线表圈与圆盘，壳面切角及侧厚可辨。
枕形厚壳腕表|cushion-shaped watch|四边鼓出的枕形壳内嵌圆盘，表耳短而宽。
六角几何腕表|hexagonal geometric watch|六角壳体内配几何刻度，六边与连接耳完整。
圆壳小秒盘腕表|round small-seconds watch|主盘下部独立小秒盘，两个盘与指针层次清楚。
三小盘计时外观腕表|three-subdial chronograph-style watch|圆壳三个小盘，侧面两个按钮与表冠；仅外观设计。
开窗机械感腕表|open-window mechanical-style watch|盘面局部开窗露原创齿轮造型，其余刻度保留，非机芯图纸。
双时区并列盘腕表|dual-display time-zone-style watch|同一长壳内并列两个独立圆盘，各有双针。
圆盘昼夜图窗腕表|day-night motif watch|圆盘上有原创半圆日月图窗与指针，窗口边框清楚。
长方数码窗腕表|rectangular digital-window watch|长方壳内浅色空白数码显示窗，侧按钮和塑胶带可见。
圆屏触控外观腕表|round smart-watch-style watch|圆形深色空白屏、侧键及柔性带，不使用品牌界面。
方屏护角运动腕表|square protected sport watch|方形空白屏周围有四角缓冲护块，宽带与侧键完整。
''',('手表','腕表','wristwatch','watch'))

block('watches','表带扣件与佩戴方案','''
细皮带针扣腕表|thin leather pin-buckle watch|小圆盘配窄皮带，完整针扣、孔位与两个带圈，摊开展示。
宽皮垫托底腕表|wide leather backing watch|表壳下有宽皮垫，两条细带穿过垫片槽，展示层次。
双绕长带腕表|double-wrap strap watch|长皮带绕成两圈，单表盘与末端针扣，圈与圈分开。
缝边帆布带腕表|stitched canvas strap watch|织布带边缘缝线，金属针扣与带孔完整，简洁圆壳。
穿底织带腕表|pass-through fabric strap watch|一条连续织带从表壳背后穿过两表耳，尾端扣件可见。
柔性硅胶带腕表|flexible silicone strap watch|宽柔性带有成排调节孔，针扣与压纹带面，完整展示。
细密网织金属表带|fine mesh bracelet watch|圆壳连接细密金属网带，滑动夹扣与网边收口清楚。
三列铰节链带腕表|three-row link bracelet watch|三列短金属节相互铰接，折叠扣及左右表耳完整。
珠节装饰链带腕表|bead-link jewelry watch|小表盘两侧以圆珠链节连接，末端首饰扣可见。
硬镯开合腕表|hinged bangle watch|表盘嵌在硬环顶端，底部铰链和按扣，展示半开状态。
开口环端表盘腕表|open-cuff end-dial watch|C形硬环一端是小表盘，另一端圆钝，开口留清楚。
缎带系结礼饰腕表|ribbon-tie dress watch|小表盘两侧连接缎带，末端蝴蝶结与完整两尾，原创礼饰。
布褶弹力带腕表|scrunchie-band watch|小圆壳接布褶弹力环带，布褶、连接耳与内圈分开。
护盖翻开式腕表|hinged-cover wristwatch|小表盘上有翻开的独立金属盖，盖铰链与皮带可见。
可拆表壳底托腕表|detachable-case cradle watch|圆壳装在带扣底托中，旁有取下的壳，插槽与底托边缘。
表盘坠链叠层腕饰|dial-and-chain layered wrist ornament|小表盘主带外搭两条独立细链，以连接环挂到主带，不遮盘。
''',('手表','腕表','表带','watch strap','wristwatch'))

block('rings','环身开合与叠层','''
窄平片素面指环|narrow flat band ring|窄平面环身，内外边清楚，三分之四角度展示完整圆孔。
圆截面细线指环|round-wire fine ring|细圆线闭环，光滑圆截面，边缘圆润。
宽弧面素面指环|wide domed band ring|宽环外侧圆弧隆起，内孔与厚度清楚。
宽平面双边槽指环|wide twin-groove band|宽平面环身两侧有平行浅槽，槽线沿环连续。
内嵌双层转环外观|nested two-band ring|外窄环套在内宽环上，两层独立边缘，原创外观研究。
错层双轨指环|offset double-rail ring|两条平行环轨以短桥连接，前侧一高一低，轨间空隙。
交叉X形环面指环|crossed X-front ring|两条环带在戒面交叉成X，背部并合，交叠清楚。
三环互套组合指环|three interlinked band ring|三个完整环相互穿套，环间上下关系与空隙明确。
开口圆珠端指环|open bead-end ring|C形开口环两端各有小圆珠，端珠间留可见空隙。
错位双端开口指环|offset-end open ring|两端越过彼此但不接触，一端在上、一端在下。
绕指螺旋两圈指环|two-turn spiral ring|单根圆线绕成两圈螺旋，上下两圈不连成平面环。
铰链扣合指环|hinged clasp ring|侧铰链与另一侧小扣，将环体分为两半，展示略打开。
小链节柔性指环|small-link flexible ring|短小金属链围成完整指环，连接环与链节可见。
编绳结面指环|woven-cord knot ring|编绳环身顶部形成平结，绳股与末端固定清楚。
双指桥接环饰|two-finger bridge ring|两个独立指孔以顶部横桥连接，孔间距与桥面完整。
中节短筒指环|short mid-finger band|短宽环用于指中节，旁有中性灰手指定位示意，不覆盖关节。
''',('戒指','指环','ring','finger ring'))

block('rings','戒面与原创装饰','''
圆盘凹刻印面戒指|round engraved signet ring|宽环顶部圆形扁盘，原创几何凹刻线，盘面侧高可见。
方台阶印面戒指|square stepped signet ring|方形平面戒台，下部层叠台阶与环身相接。
椭圆包边宝石戒指|oval bezel-set stone ring|椭圆色石四周完整金属包边，戒托与窄环接点清楚。
四爪圆石戒指|four-prong round-stone ring|圆色石有四根可见支撑爪，石台高于环身。
六爪高托宝石戒指|six-prong raised-stone ring|六根支爪围绕高托圆石，侧面托篮与环肩清楚。
三石横排戒指|three-stone row ring|中央大石与两侧小石横排，三个独立石座。
双石斜对戒指|diagonal two-stone ring|两颗不同形石座斜向错位，开口环肩分别支撑。
满圈小石排镶戒指|continuous small-stone band|细环外侧连续小石座，环背也保持排列，非单主石。
镂空叶枝戒指|openwork leaf-branch ring|原创小叶沿枝环排布，叶间镂空，背面环身完整。
花瓣叠层戒指|layered-petal ring|原创花瓣分两层，中央小珠，花托与环肩清楚。
月牙空心戒面戒指|hollow crescent-face ring|细环上方空心月牙轮廓，内孔与顶部接点可辨。
星芒放射戒面戒指|radiating starburst ring|原创多短芒放射形戒面，中央圆台与平缓边缘。
结带镂空戒指|open bow-face ring|金属结带形成双环与短尾，结下方环身不被遮掉。
小珍珠端台戒指|pearl-top pedestal ring|单颗圆珠立在小盘托上，托盘边与环肩可见。
链垂坠饰戒指|chain-dangle charm ring|素环侧挂短链小几何坠，吊环、链长和环孔清楚。
原创浮雕山纹戒指|original mountain-relief ring|宽戒面低浮雕连绵山形，轮廓原创，背环完整。
''',('戒指','戒面','宝石戒指','ring setting'))

block('bracelets','硬环开口与腕带','''
细圆杆闭合手环|thin round-rod bangle|细圆杆完整闭环，内径和圆截面清楚。
宽平片闭合手环|wide flat bangle|宽平片闭环，外面平整，内圈与两侧边厚可辨。
弧面隆起手镯|domed bangle|宽硬环外面隆起，光滑弧面与内侧平面区分。
八角切面硬手环|octagonal faceted bangle|外缘八角切面，内孔近圆形，切角有明确棱线。
波浪起伏硬手环|wavy rigid bangle|闭环沿周向连续起伏，环体仍为同一完整杆。
双环连接手镯|linked double bangle|两个独立硬环通过短链相连，各环孔完整。
四圈堆叠硬手环|stacked four-bangle set|四根不同宽度的完整硬环独立叠放，保留层间空隙。
两端珠头开口手环|bead-ended cuff bracelet|C形硬环两端圆珠，清楚展示开口与内侧。
宽板C形开口手环|wide plate cuff bracelet|宽弧金属板围成开口C形，两端平缓圆角。
错位绕腕螺旋手环|spiral wrap cuff bracelet|连续杆绕腕一圈半，两端高低错位，整体螺旋清楚。
铰链暗扣手镯|hinged clasp bangle|硬环分两半，一端铰链、另一端小扣，略打开。
网格镂空宽手环|open lattice cuff|宽环面原创交叉网格镂空，边框与内孔可见。
拼片珐琅外观手环|panelled enamel-style bangle|环外侧有分隔的原创彩色面板，金属隔线与整环清楚。
缝边宽皮腕带|stitched wide leather wristband|宽皮带边有缝线，针扣、孔位与双带圈完整。
双扣叠层皮手环|double-buckle leather wristband|两条窄皮带叠在宽底片上，各有独立小扣与调节孔。
拉紧扣织物腕带|adjustable woven wristband|织带穿滑扣调节，末端止片与完整柔性环路。
''',('手环','手镯','腕带','bangle','cuff bracelet'))

block('bracelets','软链编带与腕背饰','''
小圆环链手链|small round-link bracelet|小圆环首尾相扣组成柔链，龙虾扣与延长链完整。
扁椭圆节手链|flat oval-link bracelet|扁椭圆大链节连续连接，尾端扣件与环形连接点。
双细链并行手链|parallel double-chain bracelet|两条细链共享两端扣环，保持并行，两链间距可见。
连续细石座手链|small-stone line bracelet|一排独立小石座铰接，盒扣与安全小环，整条闭环。
中牌双链手链|center-plate twin-chain bracelet|原创空白小牌在腕顶，两侧各接双链，牌边清楚。
垂坠小物手链|multi-charm bracelet|链上悬三个原创不同几何小坠，吊环与链根分辨。
中心花结手链|center-flower knot bracelet|编绳中间原创花形结，左右双绳与后部调节结可见。
三股编辫绳手链|three-strand braided bracelet|三股粗绳平辫围腕，尾端固定套与扣件。
扁平交织带手链|flat interwoven band bracelet|多条细布带上下交织成宽平带，织纹与端夹清楚。
可调滑结绳手链|sliding-knot cord bracelet|双绳穿滑结收紧，两端各有止结，调整路径清楚。
绕腕三圈细绳手链|three-wrap thin-cord bracelet|同一长绳绕三圈，末端小扣，两端不凭空消失。
缎带系结腕饰|ribbon-tie wrist ornament|宽缎带围腕并系双环结，结尾两条完整垂下。
小板片铰接手链|articulated small-plate bracelet|数块小矩形板用铰链相接，尾端折叠扣与板间缝。
腕指单链连接饰|single wrist-to-finger chain|腕链到指环之间仅一条足长细链，产品平铺展示三端。
腕背三叉链饰|three-branch hand-chain ornament|腕带向手背分三支细链接三个小指环，连接环位置明确。
腕部双翼装饰环|paired-wing wrist ornament|原创两片小金属翼接在开口环两端，环孔与翼底座完整。
''',('手链','手环','腕饰','手背链','bracelet'))

block('bead_bracelets','珠形排列与串联','''
等径圆珠单圈手串|uniform round-bead bracelet|等大圆珠单圈，穿珠线和内孔自然闭合，无悬空珠。
大小交替圆珠手串|alternating-size bead bracelet|大珠小珠交替，粗细节奏与完整闭环清楚。
渐变珠径手串|graduated-size bead bracelet|中央最大珠向两侧逐渐变小，后端小扣收束。
小隔珠分节手串|spacer-separated bead bracelet|大圆珠之间各有小金属隔珠，隔珠与线孔可见。
多面切珠手串|faceted-bead bracelet|透明感多面珠组成一圈，切面棱线与珠间连接。
扁圆片珠手串|flat-disc bead bracelet|短扁圆盘珠串联，平面与侧厚清楚，珠孔方向一致。
长筒管珠手串|tube-bead bracelet|短圆筒珠沿绳连续排列，管孔与圆弧串线可见。
方块珠单圈手串|cube-bead bracelet|小立方珠圆角，沿环线串接，方块边面与串孔清楚。
椭圆木珠手串|oval wood-bead bracelet|椭圆木色珠单圈，木纹仅作外观，孔与结线清楚。
不规则碎石珠手串|irregular chip-bead bracelet|原创不规则石片珠串接，片间空隙与连续绳线。
双排小珠编带手串|double-row bead-woven bracelet|两排小珠由横向细线织连，尾端扣件，非两条散环。
三圈细珠绕腕手串|three-wrap seed-bead bracelet|长串小珠绕腕三圈，开合端扣完整，三圈层次分辨。
珠组间编绳手串|bead-cluster cord bracelet|三组圆珠之间有短编绳段，后部滑结，组数清楚。
主珠双端结绳手串|center-bead knotted bracelet|一颗大主珠两侧小隔珠，左右编结绳和滑扣。
小流苏末端手串|tassel-ended bead bracelet|圆珠单圈后接原创小流苏，线束根与绕线帽可见。
悬环几何坠手串|bead bracelet with geometric charm|圆珠串上一个连接环挂原创几何坠，珠串与坠独立。
''',('手串','串珠','珠串','串珠手链','bead bracelet'))

block('anklets','脚链足环与定位','''
单细链脚踝饰|single fine-chain anklet|细链围成踝环，末端扣与短延长链，完整产品展示。
双链错层足链|double-tier anklet|两条不同长度细链共享后扣，形成上下错层。
细珠串脚踝饰|small-bead anklet|小圆珠完整踝圈，柔线与小扣，尺寸按踝部示意。
中心小坠足链|center-charm anklet|细链中心挂原创几何小坠，吊环和后扣清楚。
连续小铃外观足链|small-bell charm anklet|细链上原创空心小铃形坠，连接环可见，不作真实音响说明。
两端圆珠开口足环|bead-ended open anklet|C形硬踝环，两端圆珠与清楚开口，非手镯佩戴图。
铰链扣合硬足环|hinged rigid anklet|完整硬环一侧铰链另一侧按扣，开合结构与踝位置小示意。
镂空宽板踝环|wide openwork ankle cuff|宽弧板原创几何镂空，内衬与开口圆角清楚。
软皮针扣踝带|leather buckle ankle strap|窄软皮踝带，针扣、孔位与带圈完整，普通装饰产品。
编绳滑结踝饰|sliding-knot cord anklet|细编绳踝圈与滑结，两个短绳尾有止结。
缎带结饰踝带|ribbon-bow anklet|软缎带绕踝系小结，两短尾不拖地，环路完整。
短流苏珠链踝饰|short-tassel bead anklet|小珠链接一束短流苏，流苏帽与吊环分辨。
足背单链趾环饰|single-chain foot ornament|踝链经一条足背链接单趾环，完整展开并配成人足部定位小图。
足背三角链饰|triangular foot-chain ornament|踝环到足背中央分叉再接趾环，三角链面与三个端点清楚。
珠网足背饰片|bead-net foot panel|原创三角珠网片一端接踝带另一端接趾环，网边留完整。
开口素面脚趾环|plain open toe ring|小型圆钝开口环，产品放大并配成年趾部小定位图，非指环图。
''',('足环','脚环','脚链','足链','踝饰','anklet','toe ring'))

block('feet','整体轮廓与局部结构','''
修长窄轮廓足形|slender narrow foot outline|成人单足俯视，长轴修长、前掌较窄，五趾完整自然排列。
短宽轮廓足形|short broad foot outline|成人单足俯视，前掌宽、纵向较短，五趾与后跟清楚。
前掌宽后跟窄足形|wide forefoot narrow heel|俯视显示宽前掌向较窄后跟收束，内外侧轮廓连续。
前后宽度接近足形|similar-width forefoot and heel|俯视示例前掌与后跟宽度较接近，轮廓变化平缓。
前掌圆弧足形|rounded forefoot outline|趾根一带外轮廓近圆弧，五趾端轮廓自然，非鞋形。
前掌平缓展开足形|gently spread forefoot outline|俯视五趾轻微自然分开，前掌展开但不夸张。
内侧弧线较深足形|deeper medial contour|俯视内侧收弧明显，外侧线较平缓，五趾完整。
内侧弧线平缓足形|gentler medial contour|俯视内侧轮廓收弧较浅，足形仍自然连续。
足背平缓轮廓|low-profile dorsal contour|成人单足外侧面，足背上缘平缓，脚踝与趾端完整。
足背隆起轮廓|raised dorsal contour|成人单足外侧面，足背上缘略隆起，正常关节结构。
内侧足弓明显侧影|pronounced medial arch silhouette|内侧面看底部弧形凹线较明显，后跟与前掌平放。
内侧足弓平缓侧影|gentle medial arch silhouette|内侧面底部弧线较平缓，后跟与前掌平放，不作诊断。
圆厚后跟轮廓|rounded fuller heel contour|后侧三分之四视角，后跟轮廓圆厚，脚踝到足底连续。
窄收后跟轮廓|tapered heel contour|后侧三分之四视角，后跟轮廓较窄收，保持自然比例。
踝骨起伏清楚足形|visible ankle contour study|内外踝局部与足背连接，骨性起伏适度可见，非骨骼透视。
软轮廓踝足连接|soft ankle-to-foot contour|踝足交界较平滑柔和，脚踝到后跟与足背的转折清楚。
''',('女性足部','足形','脚型','足部','adult foot drawing'))

block('feet','趾端与趾甲形状','''
大趾较长递降趾列|big-toe-longest sequence|成人单足俯视，大趾最长，第二至第五趾依次渐短，五趾自然。
第二趾较长趾列|second-toe-longest sequence|成人俯视第二趾略长于大趾，其余趾逐次变短，五趾完整。
前三趾近齐趾列|near-even first-three toes|俯视大趾、二趾、三趾长度相近，四五趾略短。
前二趾近齐趾列|near-even first-two toes|俯视前两趾长度相近，后三趾形成下降弧线。
圆钝趾端轮廓|rounded toe-tip contour|五趾前端偏圆钝，趾缝和正常趾甲可见，成人局部绘画。
略方趾端轮廓|slightly square toe-tip contour|五趾端线偏平缓方圆，边角柔和，非变形或病理。
细长趾节比例|slender toe proportion study|趾节示例较细长，关节线自然，五趾从前掌连续生长。
短圆趾节比例|short rounded toe proportion study|趾节示例较短圆，前掌与五趾端保持自然连接。
短圆自然趾甲|short rounded natural toenails|成人五趾俯视局部，趾甲短圆，甲面与皮肤边缘清楚。
方圆短趾甲|short squoval toenails|五趾短甲前端平直、角部圆润，长宽比例自然。
短椭圆趾甲|short oval toenails|五趾短甲轮廓近椭圆，甲面无过长尖端。
窄长甲面比例|narrow nail-plate proportion|成人趾部绘画，甲面纵向略长、横向窄，仍为短甲。
宽短甲面比例|wide short nail-plate proportion|成人趾部绘画，甲面横向较宽、纵向短，正常简化形态。
纯色短甲表面|solid-color short toenails|五趾短甲涂单一低饱和色，甲面边缘与趾端清楚。
细边双色趾甲|thin-edge two-tone toenails|短甲底色与极细前缘异色，五趾甲面完整，成人装饰参考。
单点小图案趾甲|single-dot toenail motif|短甲上原创单点或小圆形装饰，五趾自然排列，不堆叠复杂饰物。
''',('女性足部','脚趾','足趾','趾甲','toe','toenail'))

block('feet','视角与自然动作','''
足部正俯视参考|top-down foot view|成人单足正上方看，脚踝末端、足背和五趾完整，投影清楚。
足部前侧三分视图|front three-quarter foot view|成人单足前方斜看，足背、内侧边与五趾端同时可见。
足部外侧面参考|lateral foot view|正外侧面，脚踝、外足缘、后跟与前趾清楚，隐藏趾不硬挤出。
足部内侧面参考|medial foot view|正内侧面，内踝、足弓、后跟到大趾连续侧影。
足部后侧三分视图|rear three-quarter foot view|后方斜看后跟与脚踝，再露部分足背，正常透视。
足底平面结构参考|sole-plane drawing study|中性单足足底视图，后跟、外缘、前掌与五趾大形，简化自然皮纹。
双足平行站立|parallel standing feet|成年人膝下局部，双足平行平放地面，五趾各自完整，短裤边在画面外。
双足轻微外开站立|slightly outward standing feet|成年人膝下局部，两足轻微外开，脚踝与接地阴影清楚。
前后错步静立|staggered stationary feet|膝下两足前后错开，两足均稳妥触地，透视与接地可辨。
一足自然迈步|natural step foot study|膝下两足，一足迈出落地、另一足跟略抬，保持行走支点。
单足抬跟过渡|heel-rise transition|成人单足侧面，前掌触地、后跟适度抬起，脚踝顺势延长。
单足抬趾回勾|toes-up dorsiflexed foot|成人单足侧面，后跟靠地、前掌抬起，踝角自然不过伸。
坐姿双足平放|seated feet flat on floor|膝下局部，坐姿双小腿垂直，两足平放地面，普通姿态。
坐姿单足轻悬|seated foot lightly hanging|小腿下端与自然悬垂单足，踝部放松，五趾不过伸。
脚趾轻屈动作|gently flexed toes|成人单足近俯视，五趾轻屈，趾根连续，不握物不极端弯折。
脚趾自然舒展动作|naturally extended toes|成人单足近俯视，五趾自然舒展，轻微间隙与趾端关系清楚。
''',('女性足部','足部视角','足部动作','脚部绘画','foot pose'))

block('clothing_prints','几何纹样题材','''
细等距直条印花|fine evenly spaced stripe print|大布样上细线等距纵排，清楚连续的单一线宽。
粗细交替直条印花|alternating-width stripe print|宽条和窄条交替，横向重复节奏明确。
断续虚线条印花|broken-line stripe print|条纹由等长短线组成，行内留间隙，区别连续条纹。
连续折线锯齿印花|continuous chevron print|上下折线形成V形重复，折角与行间距清楚。
曲线波纹印花|curved wave-line print|平行柔曲线起伏，波峰错位但保持连续。
棋盘方块印花|checkerboard print|黑白或两色正方块交替，行列直角排列，明确平面印花。
双线窗格印花|double-line windowpane print|大方格由两根细线成框，格心留大面积底色。
细小犬牙轮廓印花|small houndstooth-style print|原创四角伸出的几何小块互相错嵌，非真实织纹。
斜向菱格印花|diagonal diamond-grid print|菱形单元斜向连接，细线格与色块层次清楚。
圆点等距印花|regular polka-dot print|同径圆点横竖等距，底色留白均匀。
大小散点印花|mixed-size scattered-dot print|不同大小圆点不规则散布，留白密度可辨。
三角交错印花|interlocking triangle print|三角形上下交错连成平面，多方向边缘清楚。
蜂窝六角印花|hexagonal honeycomb print|等大六角格无缝接边，粗细一致，不画成蜂窝实物。
弧扇叠排印花|overlapping fan-arc print|原创半圆弧扇上下叠排，弧线与底色交替。
同心圆环印花|concentric-ring repeat print|每个单元有三圈同心细环，单元之间留空。
迷宫直角线印花|right-angle maze-line print|原创直角折线路径重复，转角清楚，无文字或符号。
''',('衣物印花','服装印花','几何印花','图案','textile print'))

block('clothing_prints','植物花果与自然题材','''
小碎花散排印花|tiny scattered floral print|原创小花簇散排，细小花心、花瓣与留白密度清楚。
大花单元印花|large blossom repeat print|原创大花单元重复，花径大于单元间空隙，完整花瓣。
枝藤连续印花|continuous vine print|原创弯曲枝藤贯穿布面，叶和花沿枝生长，方向连续。
单叶散落印花|scattered single-leaf print|独立叶形在不同方向散落，叶脉简化、叶间留白。
长叶交叠印花|overlapping long-leaf print|狭长叶片斜向交叠，前后层次与叶端明确。
蕨叶细枝印花|fern-frond print|原创羽状细叶枝交错，主轴与小叶展开清楚。
银杏扇叶印花|fan-shaped ginkgo-leaf print|原创扇叶单元散排，叶柄与放射脉线可见。
竹叶节枝印花|bamboo-leaf stem print|原创细竹节枝与长叶，留白大，不混入文字题款。
小果双叶印花|small-fruit paired-leaf print|原创小圆果与两叶成组，重复间隔与果梗可见。
切片水果印花|sliced-fruit print|原创圆果切面单元，果瓣扇区清楚，非照片拼贴。
花环单元印花|floral-wreath repeat print|每个原创圆花环中心留空，环形单元均匀排列。
蒲公英伞球印花|dandelion-seed-head print|原创放射细线球和短茎，种子飞点少量散布。
蘑菇草丛印花|mushroom-and-grass print|原创小蘑菇和草叶成簇，菌盖、柄与草层完整。
海藻珊瑚幻想印花|seaweed-and-coral fantasy print|原创细分枝与卷叶，浅海感平面花纹，不复制实物图案。
雨滴涟漪印花|raindrop-and-ripple print|小水滴与椭圆涟漪散排，水纹轮廓与空间清楚。
云朵山形印花|cloud-and-mountain print|原创层叠山形与小云单元，云山比例和底色留白。
''',('衣物印花','服装印花','植物印花','花卉印花','botanical print'))

block('clothing_prints','动物物件与叙事题材','''
猫影小单元印花|small cat-silhouette print|原创猫侧影与坐姿单元，清晰耳尾，均匀散排。
兔影与小花印花|rabbit-and-flower print|原创兔轮廓与小花搭配，长耳短尾、单元留白。
飞鸟斜列印花|diagonal flying-bird print|原创简化飞鸟成斜列，翼形与方向可辨。
蝴蝶对称单元印花|symmetric butterfly print|原创蝴蝶每个单元左右对称，翅纹简化。
鱼影波线印花|fish-and-wave-line print|原创鱼侧影与细波线交错，鳍尾完整。
不规则斑点动物纹印花|irregular animal-spot print|抽象环状斑点大小不同，原创动物纹灵感，非真实皮毛。
斜弧条动物纹印花|curved animal-stripe print|抽象斜弧黑条疏密变化，原创条纹动物灵感。
星月散落印花|scattered stars-and-moons print|原创小星与弯月分散排列，大小和方向明确。
星座连线幻想印花|fictional constellation print|原创点与细线连出抽象星图，无真实星座名称或文字。
小钟齿轮印花|clock-and-gear motif print|原创钟形轮廓与大小齿轮，表面无数字标识。
书本信封印花|book-and-envelope print|原创书本、信封平面小图，封面空白，排列清楚。
茶杯糕点印花|teacup-and-pastry print|原创茶杯和普通糕点小图，杯柄与轮廓可辨。
蝴蝶结礼盒印花|bow-and-gift-box print|原创布结与礼盒平面轮廓，结尾与盒边清楚。
钥匙锁孔印花|key-and-keyhole print|原创普通钥匙与抽象锁孔，大小和方向变化。
棋子卡框印花|game-piece-and-card-frame print|原创简化棋子与空白卡框，不使用现成花色或角色标识。
小街屋叙事印花|tiny street-house narrative print|原创小屋、树与短街线成组，立面轮廓，无店名或商标。
''',('衣物印花','服装印花','叙事印花','动物印花','motif print'))

block('clothing_prints','重复布局与服装定位','''
整齐满版单元排列|straight full-surface repeat|布样同一原创花单元按正方网格重复，行列完全对齐。
半落差竖排单元|half-drop motif repeat|每相邻一列原创叶单元竖向错半个单元高度，错列明显。
半砖差横排单元|half-brick motif repeat|每相邻一行原创圆花单元横向错半个单元宽度，错行明显。
菱网斜向单元排列|diagonal lattice motif repeat|原创小花沿菱形网斜排，网线仅作细印花背景。
旋转四向单元排列|four-direction rotating repeat|同一原创叶单元按四方向转动排列，四个方向都可见。
自由散落留白布局|sparse tossed motif layout|原创小物件方向随机，彼此远离，底色留白占多数。
紧密交叠满版布局|dense overlapping allover layout|原创叶花单元紧密交叠，底色间隙少，仍看清图形。
由疏到密渐变布局|density-gradient motif layout|布样顶部稀疏到底部密集，图案尺寸相同，密度改变。
由小到大尺度渐变|scale-gradient motif layout|原创花单元从上到下逐渐变大，单元间距保持清晰。
下摆边框连续印花|continuous hem-border print|灰色完整长裙产品，下摆一圈原创连续纹带，裙身留白。
领缘袖口呼应印花|coordinated collar-and-cuff print|完整衬衣产品，领边与袖口原创窄纹带，主体素色。
胸前居中定位印花|center-chest placement print|完整不透明T恤产品，胸前单幅原创圆花图，其余无图。
单侧斜向跨片印花|one-side diagonal placement print|完整连衣裙产品，原创叶枝斜跨一侧前片，接缝位置可见。
前后主题分区印花|front-back themed placement print|同一完整上衣产品的正背两视图，前小图背大图均原创。
腰侧分区拼色印花|waist-side panel print|完整连衣裙产品，腰侧两片有几何印花，中间保留素色面。
裙摆环绕叙事印花|wraparound skirt narrative print|完整长裙产品，下摆环绕原创街屋小景，单元沿水平连接。
''',('衣物印花','服装印花','印花布局','repeat layout'))

block('print_styles','审美与构图语言','''
极简线条印花风格|minimal line-art print|原创稀疏单线轮廓，少量细线与大留白，布样完整。
复古小花印花风格|retro small-floral aesthetic|原创小花与细叶，重复均匀、低饱和暖色，清楚图形。
田园细描印花风格|cottage botanical illustration print|原创细描花草与小果，柔和底色、自然疏密层次。
古典卷草印花风格|classical scrollwork print|原创对称卷曲枝叶与中央小花，卷草轮廓连续。
洛可可曲线印花改编|rococo-inspired curving print|原创不对称C形卷叶和小花簇，轻细线，非复制历史花纹。
装饰艺术几何印花|art-deco-inspired geometric print|原创阶梯线、放射扇和对称竖轴，大几何单元清楚。
工艺美术枝叶印花改编|arts-and-crafts-inspired leaf print|原创交织枝叶与花，平面色块、密集有序，不复制名家纹样。
单色田园叙事印花|monochrome pastoral-scene print|原创单色细线小树、小屋和花簇分组，留白大，非现成图画。
哥特尖拱印花风格|gothic-arch print aesthetic|原创尖拱轮廓与细藤蔓，深底浅线，抽象装饰。
朋克拼贴印花风格|punk collage print aesthetic|原创撕边矩形、斜线和别针形小图，不含标语或商标。
迷幻波形印花风格|psychedelic-wave print|原创高对比弯曲波带、同心圈与扭转色块，图形平面。
波普色块印花风格|pop-art color-block print|原创大圆点和日常物件轮廓，明快平色、粗线，无文字。
像素小图印花风格|pixel-motif print|原创方块像素花星组成小单元，边缘以方格阶梯表现。
漫画网点印花风格|comic-halftone print|原创爆炸边框、圆网点与速度线，不用人物或对话文字。
国风云枝印花改编|Chinese-inspired cloud-and-branch print|原创云曲线与细梅枝，平面印花风格参考，不标称特定朝代。
科技线路印花风格|tech-circuit print aesthetic|原创直角线路、节点和网格，深底细亮线，无实际电路图。
''',('衣物印花风格','服装图案风格','印花风格','print aesthetic'))

block('print_styles','表面效果与表现手法','''
水彩晕边印花效果|watercolor-edge print effect|原创花形有柔和晕边和局部深浅，平面布样仍清楚。
墨线淡染印花效果|ink-line wash print effect|原创细枝以墨线轮廓和浅淡晕染填色，保留布底。
手绘铅线印花效果|pencil-line print effect|原创叶轮廓有轻微铅线颗粒与交叉排线，平面印花示意。
木版刻线印花效果|woodcut-line print effect|原创粗黑叶形内留短刻线，少量不均匀边，视觉效果参考。
模板镂空印花效果|stencil-shaped print effect|原创大几何叶片有桥接断口，边缘整齐，单色块。
套色错位印花效果|misregistered-color print effect|原创花形两层色版边缘轻微错位，错位一致可辨。
双色网点印花效果|two-color halftone print effect|原创圆形图案用两色小网点叠排，网点与底色清楚。
颗粒喷点印花效果|grainy sprayed-dot print effect|原创云形由细喷点聚散形成，边缘逐渐稀疏。
干笔刷痕印花效果|dry-brush print effect|原创粗刷条有断续露底纹理，笔触方向一致。
蜡笔块面印花效果|crayon-block print effect|原创圆花用颗粒蜡笔感块面，边缘略粗糙，非布纤维。
剪纸正负形印花效果|paper-cut positive-negative print|原创叶花轮廓用双色正负形交替，镂空似的留白是印花。
拼纸纹理印花效果|paper-collage texture print|原创叠纸几何块有纸边与淡纹理，全部为平面图像。
扎染环晕视觉效果|tie-dye ring effect|原创同心浅深晕环，边界不整齐，作为染纹外观参考。
云雾渐层染纹效果|cloud-gradient dye effect|原创柔和云状渐层，不含单独花单元，布底纹理简洁。
金属光点印花效果|metallic-dot print effect|原创小金属色点组成星形，轻微反光区别底布，视觉外观参考。
浮起胶线印花外观|raised-line print appearance|原创粗弧线在布面略凸，侧影展示微小高度，不代表工艺配方。
''',('衣物印花风格','印花效果','印花手法','surface print effect'))

block('clothing_prints','常见纹样家族与组合','''
多线套格印花改编|multiline tartan-inspired print|不同宽度横竖色条交叠，形成大格中套小格；原创格纹，不标称具体家族。
双色小方格印花|two-color gingham-style print|等宽浅深横竖条形成细小方格，交叠处最深，清楚平面印花。
多色拼块格纹印花|multicolor patchwork-check print|原创多色小格区域拼成大方块，区域边框与不同格向清楚。
菱块细线叠格印花|argyle-style diamond print|双色菱块相接，上覆斜向细线格，实块与细格两层分辨。
卷尖水滴佩斯利印花|curled paisley-motif print|原创弯曲水滴形顶端内卷，内部小花细点，单元散排。
抽象分块迷彩印花|abstract camouflage print|原创大面积不规则色块嵌合，无具体国家或军种配色标识。
蛇鳞几何灵感印花|geometric snakeskin-inspired print|原创小鳞菱块形成连续斜列，中央较深、边缘浅，平面图案。
橙底虎条灵感印花|orange tiger-stripe-inspired print|原创橙色底上黑色弯条，粗根尖尾、条纹交错，不用真实皮毛。
大块牛斑灵感印花|large cow-spot-inspired print|原创黑白不规则大块斑纹，斑块彼此不接成规则网格。
柔纹大理石印花|soft marble-vein print|原创淡底上细长流动纹脉，粗细变化、局部晕边，布样而非石板。
细网裂纹印花|fine crackle-line print|原创不规则细网线分割布面，线间大块底色，非真实破损。
飞溅色点印花|paint-splatter print|原创大小色滴与短飞溅线散排，多色点形不规则，布面平整。
蕾丝轮廓平面印花|flat lace-silhouette print|原创花边镂空似的白色轮廓印在深布上，实际无孔、无绣线。
对称团花徽框印花|symmetric medallion print|原创圆形团花与卷叶框重复，框心几何花，非真实徽章。
航海绳结物件印花|nautical rope-knot print|原创普通绳结、锚形小物与细波线，平面重复，无海军标识。
万花筒放射印花|kaleidoscopic radial print|原创六向花瓣与几何片重复拼接，放射中心及单元边清楚。
''',('衣物印花','服装印花','常见印花','textile pattern'))

# Placement alias applies only to actual garment placement, not flat repeats.
for e in CATALOG:
    if e['category']=='clothing_prints' and e['dimension']=='重复布局与服装定位' and any(w in e['name'] for w in ['下摆','领缘','胸前','单侧','前后','腰侧','裙摆']):
        e['aliases'].append('定位印花')
    if e['name']=='细小犬牙轮廓印花':e['aliases']+=['千鸟格','犬牙格','houndstooth']
    if e['name']=='不规则斑点动物纹印花':e['aliases']+=['豹纹','leopard print']
    if e['name']=='斜弧条动物纹印花':e['aliases']+=['斑马纹','zebra print']
    if e['name']=='多线套格印花改编':e['aliases']+=['苏格兰格纹','tartan','格子']
    if e['name']=='双色小方格印花':e['aliases']+=['维希格纹','gingham','格子']
    if e['name']=='多色拼块格纹印花':e['aliases']+=['madras-inspired','拼布格纹']
    if e['name']=='菱块细线叠格印花':e['aliases']+=['阿盖尔纹','argyle']
