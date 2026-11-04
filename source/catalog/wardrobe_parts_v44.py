"""Expanded shoes, hosiery and gloves; keep all previously published identifiers."""
from catalog_content import CATALOG,add

GROUPS=[]
NEW_ENTRIES=[]
def block(key,cid,dimension,text):
    rows=[line.split('|') for line in text.strip().splitlines()]
    assert len(rows)==8
    GROUPS.append((key,cid,dimension))
    for order,(name,en,description,recipe) in enumerate(rows,1):
        add(cid,dimension,f'{name}|{en}|{description}。')
        entry=CATALOG[-1]
        entry.update(wardrobe_part_reference=True,part_group=key,part_order=order,added_in='44.0',
            illustration_recipe=recipe,adult_only=True,age_min=25,minor_reference=False,
            reference_ids=['R172'] if cid=='footwear' else ['R173'] if key=='sock_activity' else ['R68'] if cid=='hosiery' else ['R56'],
            note='原创成年尺码服饰设计参考。比较完整轮廓、开口、接缝、材质和穿戴连接；运动、工具与幻想款只描述外观，不表示产品性能或防护等级。鞋袜组合同时观察袜口、鞋口与脚踝的遮挡关系。')
        NEW_ENTRIES.append(entry)

block('shoe_daily','footwear','平底鞋与经典细分','''
开放襟系带德比鞋|open-lacing derby shoes|鞋耳覆盖鞋面两侧，系带区开口可见，圆头低跟|Pair of brown women's derby shoes, open lacing flaps visibly sewn on top of vamp, rounded toe, low heel, three-quarter product view
双扣孟克鞋|double-monk strap shoes|鞋面横跨两条带扣，无鞋带，方圆鞋头|Pair of burgundy double-monk strap shoes, two buckled straps across each vamp, no laces, square-rounded toe
流苏平底乐福鞋|tassel loafers|低鞋口与短流苏成组垂在脚背|Pair of dark brown flat tassel loafers, two small leather tassels on each vamp, low topline
便士带片乐福鞋|penny loafers|脚背横带中央有菱形狭口，与流苏款区分|Pair of black penny loafers with clearly visible diamond slot in leather saddle across each vamp, no tassels
软底豆豆驾车鞋|driving moccasins|软鞋身、围裙缝与后跟延伸橡胶颗粒|Pair of tan driving moccasins with apron stitching, tiny inset heel/sole view showing rubber pebble pods rising on heel
双色翼纹拼接鞋|two-tone wingtip shoes|翼形鞋头与双色鞋面拼接，孔饰沿接缝排列|Pair of cream and brown spectator wingtip lace-up shoes, distinct W wing seam and restrained perforation rows
软底莫卡辛鞋|soft moccasins|鞋头围边抽褶与外露缝线，柔软低帮|Pair of gray suede soft moccasins, visible gathered apron seam and thick hand stitching, no rigid dress heel
草编底帆布平鞋|flat canvas espadrilles|帆布包头与绕底草编纹形成上下材质分界|Pair of cream canvas flat espadrilles, closed toe, flat braided jute sidewall, thin rubber outsole
''')
block('shoe_heels','footwear','鞋跟与礼装鞋型','''
尖头猫跟鞋|pointed kitten-heel pumps|细而低的小跟配尖头，鞋口浅|Pair of muted rose pointed-toe pumps with short slender kitten heels, low vamp
方头宽跟鞋|square-toe block-heel pumps|方鞋头与矩形粗跟形成稳定块面|Pair of black square-toe pumps with broad rectangular block heels, plain leather
圆头扣带高跟鞋|round-toe strap pumps|圆头与脚背扣带，后方有独立高跟|Pair of burgundy rounded-toe high-heeled strap pumps, single instep buckle strap, medium slender heel
交叉细带礼装鞋|cross-strap evening heels|数条细带在脚背相交，脚趾端开放|Pair of silver cross-strap evening sandals, several thin crossing instep straps, open toes, stiletto heel
鱼嘴开口高跟鞋|peep-toe pumps|包覆鞋面前端留一个小型露趾开口|Pair of navy satin peep-toe pumps, enclosed vamp except small front toe opening, clear separate heel
透明柱跟浅口鞋|clear-heel pumps|鞋面不透明，透明柱状鞋跟单独显示材质|Pair of ivory closed-toe pumps with clear transparent acrylic cylindrical heels, opaque uppers
雕塑弧跟礼鞋|sculptural curved-heel shoes|后跟呈连续弧面，鞋面保持简洁|Pair of dark green closed-toe dress shoes with original sculptural curved heels, side silhouette readable
厚台细跟鞋|platform stiletto pumps|前掌有明显厚台，后跟细长，区分坡跟|Pair of black platform stiletto pumps, thick forefoot platform and independent narrow high heel, not wedges
''')
block('shoe_sandals','footwear','凉鞋、凉拖与透空鞋面','''
渔夫编带凉鞋|fisherman sandals|多条宽带编接包头，侧面有通风开口|Pair of brown fisherman sandals, closed woven cage toe, broad interlaced straps, buckle ankle strap
高筒罗马绑带凉鞋|knee-high gladiator sandals|细带从脚背延伸到膝下，后侧支撑带连贯|Pair of women's flat knee-high gladiator sandals on cropped gray lower-leg forms, straps to below knees, full soles and all top straps visible
夹趾平底凉鞋|flat thong sandals|脚趾间的立带连接分叉鞋带与平底|Pair of white flat thong sandals with one toe post and Y straps, complete soles
工字宽带凉拖|wide H-strap slides|宽横带与纵向连接片组成工字轮廓|Pair of tan flat slides with simple wide H-shaped upper straps, no logos or hardware
软木足床双带凉鞋|cork-footbed sandals|双扣宽带配凹形足床与软木侧壁|Pair of olive two-buckle sandals, shaped footbed, visible cork sidewall and dark outsole
草编坡跟系踝鞋|espadrille wedge sandals|草编楔形底连贯承托脚弓，踝带独立系结|Pair of beige espadrille wedge sandals, continuous woven jute wedge sole, ribbon ankle ties shown on cropped gray ankle forms
网面镂空平底鞋|mesh ballet flats|包头轮廓下可见连续网孔，鞋口有细包边|Pair of black mesh ballet flats on neutral gray foot forms, fine all-over mesh upper and narrow binding, no extra toes
镂空包头后空凉鞋|cutout slingback sandals|前端包头但侧面镂空，后跟仅用绊带固定|Pair of cream cutout closed-toe slingback sandals, open side windows, rear heel strap, short block heel
''')
block('shoe_boots','footwear','靴筒、开合与靴型','''
贴踝弹力袜靴|stretch sock ankle boots|弹力靴筒紧贴踝部，鞋底与筒身材质分开|Pair of black stretch-knit sock ankle boots on gray lower-calf forms, close-fitting shaft, pointed toe, short block heel
宽筒折叠长靴|foldover wide-shaft boots|宽靴筒外翻覆住部分筒身，顶口完整|Pair of tan wide-shaft knee boots with large folded-over cuff, complete top opening and full soles
前拉链短靴|front-zip ankle boots|拉链位于鞋舌中央，从脚背向筒口延伸|Pair of black ankle boots with centered front zippers, pull tabs at shaft top, no laces
双排扣带机车靴|double-buckle biker boots|厚鞋底与两条独立扣带，靴面略松|Pair of dark brown mid-calf biker boots, two buckled straps per boot, broad low heel and heavy sole
薄底高筒雨靴|tall rubber rain boots|橡胶筒身与鞋身连续，筒口高于小腿中段|Pair of muted green tall rubber wellington rain boots, continuous rubber upper, simple low heel, full shafts
厚底系带长靴|platform lace-up knee boots|长系带区与厚底同时可见，筒口不被裁掉|Pair of black platform knee-high lace-up boots, laces all the way up shaft, complete toe heel outsole and top opening
复古扣襻短靴|buttoned ankle boots|侧排扣襻与拼接鞋面形成竖向开合线|Pair of cream and brown Victorian-inspired ankle boots, row of side buttons and loops, small curved heel, original design
长筒蕾丝系带靴|lace-panel tall boots|蕾丝衬层与前系带长筒，鞋头保持完整包覆|Pair of burgundy tall fashion boots with lace side panels over opaque lining and front lacing, closed toes, full top openings
''')
block('shoe_sport','footwear','运动、机能与休闲鞋型','''
复古薄底训练鞋|low-profile trainers|扁薄外底、窄长鞋身与简洁拼片|Pair of cream low-profile retro trainers with thin gum soles and original small suede toe panels, no branding
透气网面跑鞋|mesh running shoes|网面鞋头与独立支撑拼片，弧形鞋底|Pair of gray women's mesh running shoes with plain side support overlays, moderate curved outsole, no logos
厚中底跑鞋|high-stack running shoes|中底明显加厚，鞋身与前后翘起边缘可辨|Pair of pale blue high-stack running shoes, thick sculpted foam midsole, raised forefoot rocker shape, no brand marks
齿纹外底越野鞋|lugged trail shoes|鞋底凸齿与鞋头包片形成外观差异|Pair of olive trail shoes with reinforced toe cap, chunky visible outsole lugs, small side view of sole
系带徒步短靴|hiking ankle boots|高帮包踝、金属鞋带钩与厚底齿纹|Pair of brown women's hiking ankle boots, metal lace hooks, padded collars and lugged soles, complete shoes
低帮平底滑板鞋|low-top skate shoes|平直宽外底与软垫鞋舌，低帮开口|Pair of navy low-top skate shoes, flat broad rubber outsole, padded tongue and collar, original plain panels
搭扣运动鞋|hook-and-loop trainers|用三道搭扣代替鞋带，扣带连接点清楚|Pair of white trainers with three hook-and-loop straps each, no laces, gray outsole
针织袜套运动鞋|knit slip-on trainers|针织鞋领连续包踝，弹性鞋口与运动底相接|Pair of charcoal knit slip-on trainers, sock-like elastic ankle collar, white athletic soles, no laces
''')
block('shoe_role','footwear','舞蹈、冰轮与文化灵感鞋','''
硬盒足尖舞鞋|pointe ballet shoes|前端足尖盒与长缎带固定，和软底舞鞋区分|Pair of pink satin pointe shoes displayed off feet, squared stiff toe boxes and ribbons neatly loosely coiled beside them, entire shoes
分底爵士舞鞋|split-sole jazz shoes|低帮系带鞋身，中部软区分开前后外底|Pair of black split-sole jazz dance shoes, low lace-up uppers, inset underside shows separate forefoot and heel pads
多带拉丁舞鞋|multi-strap Latin dance shoes|前掌多条细带与踝部扣带，小型喇叭跟|Pair of bronze satin multi-strap Latin dance sandals, ankle buckle and modest flared heel, plain original design
金属底片踢踏鞋|metal-tap dance shoes|鞋头与后跟底部各有金属片，附底面小图|Pair of black lace-up tap shoes, tiny underside view shows separate metal toe and heel taps, no rollers
系带花滑冰鞋|figure-skating boots|短靴下连接单条冰刀，刀架与前齿可辨|Pair of white figure-skating boots with one steel blade per boot, clear blade mounts and toe picks, no wheels
四轮双排轮滑鞋|quad roller skates|每只鞋底前后两轴、左右共四轮|Pair of cream high-top quad roller skates, exactly four wheels per skate arranged in two axles, front toe stop, no ice blades
中式绣花布鞋|Chinese-inspired embroidered cloth shoes|布面圆头与局部花卉刺绣，低底包跟|Pair of red Chinese-inspired cloth shoes, round closed toe, restrained original floral embroidery on vamp, low fabric sole
胶底分趾足袋鞋|split-toe rubber-sole footwear|大脚趾单独分区，鞋底跟随分趾轮廓|Pair of dark indigo ankle-height split-toe tabi-inspired shoes, rubber outsole follows big-toe separation, rear closures
''')
block('sock_pattern','hosiery','袜面图案与边口设计','''
斜向交叉纹连裤袜|diagonal lattice tights|斜纹相交成细格，完整腰口到足尖|Opaque charcoal tights with fine cream diagonal lattice pattern, complete waist waistband and both feet on neutral gray display form
双侧竖线长筒袜|side-striped stockings|外侧双竖线沿袜筒延伸到脚踝|Pair of navy knee-high socks with two fine cream stripes running down each OUTER side, full cuff to toes on gray lower-leg forms
渐变晕染连裤袜|ombre-gradient tights|颜色从腿上方向脚踝连续渐变|Pair of complete opaque ombre tights on gray waist-down form, muted lavender at waist to deep navy at toes, smooth continuous gradient
膝部拼色袜裤|knee-panel tights|膝部椭圆拼色片与主体袜面有清楚分界|Complete opaque gray tights with muted burgundy oval knit knee panels, waistband and full feet visible
竖向透孔针织长袜|vertical openwork knee socks|细小透孔沿纵向排列，针织纹不覆盖开孔|Pair of cream knitted knee-high socks with narrow vertical openwork lace columns, on gray leg forms, complete cuff heel and toes
蝴蝶结点缀短袜|bow-trim ankle socks|袜口外侧固定小蝶结，袜体与装饰分开|Pair of white opaque ankle socks with a small navy ribbon bow attached to outer cuff of each sock, three-quarter gray foot forms
缎带系口长袜|ribbon-tie knee socks|缎带穿过袜口孔眼后打结，固定路径可见|Pair of pale gray knee-high socks with burgundy ribbons threaded through cuff eyelets and tied into small bows, all ribbon ends inside frame
珠光细织连裤袜|pearl-sheen tights|细织袜面出现柔和珠光，和亮片点状反光区分|Complete opaque pearl-gray fine-knit tights on neutral waist-down form, subtle broad pearlescent sheen, no sequins or metallic armor
''')
block('sock_activity','hosiery','运动、舞蹈与分区袜型','''
五趾防滑瑜伽袜|five-toe grip socks|五个独立趾袋，脚底有防滑点状纹|Pair of lavender five-toe yoga grip socks on gray foot forms, exactly five separate toe pockets each, small sole inset showing grip dots
交叉脚背普拉提袜|cross-strap grip socks|浅口袜身配两条脚背交叉弹力带|Pair of dark gray low-cut Pilates socks on gray foot forms, two elastic crossing instep straps, small sole inset with grip dots
露跟舞蹈半掌袜|dance half-sole socks|只包覆前脚掌，后跟与脚踝开放|Pair of beige stretch-knit dance half-sole socks on gray adult foot forms, forefoot and toes covered, heels and ankles entirely open
一字带露趾舞蹈袜|open-toe dance socks|脚背一字固定带，前趾端与后跟开放|Pair of black open-toe dance socks on gray adult foot forms, forefoot wrap and single instep strap, toes and heel exposed, no shoe sole
滑雪分区加厚长袜|zoned ski socks|膝下高筒，胫前与脚掌不同色块分区|Pair of women's knee-high ski socks, burgundy base with light gray shin and foot padding zones, complete cuffs heels and toes, no text
徒步分区中筒袜|zoned hiking crew socks|脚跟、前掌与脚背采用不同针织区块|Pair of olive hiking crew socks, gray reinforced-looking heel and forefoot patches, thin instep knit panel, full socks
骑行高筒弹力袜|cycling crew socks|高袜筒与脚背网区分开，图案沿小腿排布|Pair of white cycling high-crew socks, black vertical rear accent and fine instep mesh panel, complete feet on gray forms
舞蹈喇叭口暖腿套|flared dance leg warmers|小腿筒形针织套在踝部展开，足部保持开放|Pair of cream rib-knit dance leg warmers on gray calf forms, flared lower openings loosely over ankles, toes and heels visible, no shoes
''')
block('sock_styling','hosiery','鞋袜叠穿与佩戴对照','''
透感短袜配玛丽珍鞋|sheer ankle socks with Mary Janes|薄袜口位于鞋口上方，脚背扣带覆盖袜面|Cropped adult gray lower-leg forms wearing sheer black ankle socks and burgundy Mary Jane shoes, full shoe straps toes and heels
蕾丝短袜配乐福鞋|lace socks with loafers|蕾丝袜边与低鞋口形成软硬材质对比|Cropped gray lower-leg forms wearing cream lace ankle socks and black loafers, entire sock cuffs and shoes visible
罗纹堆袜配短靴|slouch socks with ankle boots|袜筒堆褶露在短靴上缘，靴筒遮住袜身下段|Gray calf forms wearing thick gray ribbed slouch socks above brown ankle boots, readable overlap at boot opening, full shoes
长袜套叠运动鞋|leg warmers over trainers|针织袜套盖住部分鞋领，但前掌外底仍可见|Gray calf forms wearing cream long knit leg warmers loosely covering upper collars of white trainers, full complete shoe toes and soles
膝下长袜配系带短靴|knee socks with lace-up boots|袜口在膝下，长袜与短靴之间保持连续覆盖|Gray lower-leg forms from above knees to soles wearing navy knee-high socks and brown lace-up ankle boots, full sock top and all shoes
后缝丝袜配后空鞋|seamed hosiery with slingbacks|后缝线通过脚跟转面，后绊带压在袜面上|Rear three-quarter gray calf forms wearing black seamed stockings and cream slingback pumps, full heels soles and toe tips, show back seams
条纹长袜配厚底平鞋|striped socks with platform shoes|横条袜纹与厚底鞋侧壁形成轮廓对照|Gray calf forms wearing burgundy and cream horizontal striped crew socks and black platform lace-up shoes, complete cuff and all soles
拼色袜裤配低跟鞋|color-block tights with low heels|左右拼色连续延伸至鞋口，裙裤不遮挡观察区|Gray knee-down forms wearing opaque navy tights with burgundy vertical side panels and gray low-heel pumps, entire shoes
''')
block('glove_fashion','gloves','礼装、薄纱与装饰细分','''
手背蝶结短手套|bow-back short gloves|小蝶结固定在手背，腕口平整|Pair of cream short five-finger gloves on gray hand forms, one back and one palm view, small navy bow on back, complete fingertips and cuffs
指尖渐变长手套|gradient long gloves|从腕筒到指尖逐渐变色，保留五指轮廓|Pair of opaque blue-to-lavender gradient elbow-length gloves on gray forms, five complete fingers each, full cuff to fingertips
欧根纱短手套|organza short gloves|薄纱成衣套在灰色手模上，接缝与透明层可见|Pair of sheer pale gray organza short gloves on solid gray hand mannequins, fine seams, exactly five fingers each, no bare human skin
蕾丝花边五指短手套|lace-trim short gloves|五指均包覆，腕口接独立花边|Pair of ivory fully fingered lace short gloves on gray hand forms, scalloped lace cuff, five finger tips intact
手背开窗缎面手套|cutout-back satin gloves|缎面短手套在手背留椭圆开窗|Pair of burgundy satin short five-finger gloves on gray hand forms, oval BACK-OF-HAND window, small wrist closure, palm remains solid
中指环连接手背袖饰|finger-loop hand sleeves|手背片用中指环连接，五指自由露出|Pair of black hand-cover sleeves on gray hand forms, fabric covers wrists and back of hands, one simple loop around each middle finger, all five fingers uncovered and connected normally
三排褶线皮手套|three-point leather gloves|手背三排短褶线与柔软皮面相配|Pair of dark brown leather short gloves, three stitched raised points on back of each hand, one back one palm view, complete five fingers
反折袖口绒皮手套|turned-cuff suede gloves|腕口外翻露出不同颜色衬面|Pair of tan suede five-finger gloves with folded ivory textile cuffs, one back one palm view, all fingertips and cuff edges visible
''')
block('glove_activity','gloves','运动与日常功能外观','''
触屏拼片针织手套|touch-panel knit gloves|拇指与食指尖用不同颜色织片标示|Pair of gray knitted five-finger gloves, contrasting black thumb and index fingertip patches, palm and back views, no screens
两指露尖摄影手套|two-finger access gloves|拇指和食指端可翻开，其余三指包覆|Pair of black photography gloves on gray hand forms, thumb and index fingertip flaps folded open, middle ring little fingers covered, five digits total
潜水湿式手套|neoprene dive gloves|厚织物五指轮廓、掌面拼片与腕扣|Pair of black neoprene diving gloves, gray palm texture, blue cuff closure, five fingers on each, no fins or webbing
滑雪长护腕手套|ski gauntlet gloves|蓬厚五指手套接长护腕口和收紧带|Pair of burgundy insulated five-finger ski gloves, long gauntlet cuffs, wrist cinch strap and cuff drawcord, complete pair
拳击训练手套|boxing training gloves|弧形拳袋与独立拇指相连，腕部宽扣带|Pair of red boxing training gloves displayed off hands, rounded enclosed fist compartments, one attached thumb per glove, wide wrist closures
棒球接球手套|baseball fielding glove|掌心接球袋、拇指与食指间网片明显|One brown leather baseball fielding glove, five finger stalls, large pocket and web between thumb and index, full glove with lacing
贴合骑乘手套|close-fit riding gloves|薄型五指手套与指缝、掌侧补片|Pair of black equestrian riding gloves, close fitting five fingers, reinforced-looking inner finger panels, small wrist tabs, no reins
单侧击剑护腕手套|single fencing glove|长护腕套与手背拼片，展示单只结构|One white fencing glove on a neutral gray hand and forearm form, five fingers, long gauntlet cuff, gray back panel, no weapon
''')
block('glove_stage','gloves','舞台、甲片与幻想手套','''
分节关节甲手套|articulated plate gauntlets|各指甲片逐节覆盖，关节留活动间隔|Pair of original silver articulated plate gauntlets, five fingers each with overlapping segmented plates, flexible joint gaps, full cuffs
链甲网织手套|chainmail gloves|细小金属环网覆盖完整五指手型|Pair of silver chainmail five-finger gloves on gray hand forms, interlinked small rings, complete fingers and short cuffs
机械腕盘装饰手套|mechanical-dial gloves|布皮手套腕侧固定小型机械盘饰|Pair of dark brown leather five-finger gloves, small original brass clockwork disc fixed on each outer wrist, no weapons, complete pair
科幻光线拼片手套|science-fiction light-line gloves|深色织物拼片上有少量连续发光细线|Pair of charcoal five-finger sci-fi gloves with thin cyan glowing seam lines and matte fabric panels, no holograms, all digits visible
亮片长筒舞台手套|sequined stage gloves|密集小亮片覆盖长腕筒，五指不粘连|Pair of silver sequined elbow-length five-finger gloves on gray forms, small separate sequins, complete fingertips and cuff edges
羽边短礼仪手套|feather-cuff dress gloves|短手套腕口附一圈柔软短羽饰|Pair of black five-finger satin short gloves, small restrained black feather cuff trim, complete silhouettes and tips
国风刺绣宽腕手套|Chinese-inspired embroidered cuff gloves|宽腕口上有原创云纹刺绣，指部简洁|Pair of ivory five-finger gloves with broad navy cuffs bearing original cloud-scroll embroidery, full cuff and fingers, no historical claim
爪形指套装饰手套|claw-tip costume gloves|五指末端加短钝爪壳，标明舞台装饰|Pair of black five-finger costume gloves on gray forms, five short BLUNT decorative silver claw caps per hand, no extra digits, no sharp weapons
''')

def reclassify_legacy_parts(entries,categories):
    cats={c['id']:c for c in categories}
    cats['footwear']['name']='鞋履与靴型'
    cats['footwear']['guide']='平底与经典细分、鞋跟与礼装、凉鞋、靴型、运动休闲、舞蹈冰轮及文化灵感鞋。观察完整鞋头、后跟、外底、开口和固定方式。'
    cats['hosiery']['guide']='D数参考、袜长、材质、吊带与自持结构、袜裤、图案，以及运动舞蹈袜和鞋袜叠穿；D数不能单独决定透感。完整观察袜口、足尖与鞋口重叠。'
    cats['gloves']['guide']='基础指型、礼仪与季节材质，扩展薄纱装饰、运动日常、舞台和幻想甲片；物件或佩戴图保留完整袖口和指尖。'
    for e in entries:
        n=int(e['id'][2:]) if e['id'].startswith('FW') else 0
        if 21<=n<=32:
            e['category']='hosiery' if n<=27 else 'gloves'
            e['category_name']=cats[e['category']]['name']
            e['dimension']='基础袜型与袜套' if n<=27 else '基础手套与护腕'
            e['keywords']=[e['name'],e['en'],e['dimension']]
        if e['category']=='footwear':e['category_name']=cats['footwear']['name']

assert len(NEW_ENTRIES)==96
