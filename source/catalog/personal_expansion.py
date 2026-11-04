"""Edition 9: hair ornaments, jewelry, gloves, body art and everyday clothing."""
from catalog_content import CATALOG, category, add

def block(key,dimension,text,aliases=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['aliases']=list(aliases)
        if key in ['schoolwear','youthwear']:e['age_context']='13–17岁服装设计参考'
        elif key in ['body_art','studs']:e['age_context']='成年角色装饰参考'

category('hair_accessories','发饰与固定结构','按箍、夹、簪、圈分组；每项展示可佩戴物件的形状、扣件和固定方式。',['R14','R55'])
category('earrings','耳饰与佩戴扣件','圈形、垂坠、贴耳、包耳和耳夹结构分列；产品图展示佩戴连接件。',['R54'])
category('pendants','吊坠与项链垂饰','吊坠主体、吊环、链孔、链条和多件连接方式分别观察，采用原创装饰图案。',['R54'])
category('studs','钉饰与局部饰件','以首饰物件与成年头部局部展示耳钉、鼻饰及其他小型钉饰的可见形状与位置。',['R54'])
category('gloves','手套与手部服饰','按指型、长度、袖口、开合和材质区分；产品图观察五指、掌背和接缝。',['R56','R06'])
category('body_art','皮肤装饰与妆面图案','彩绘与纹身为成年角色的原创装饰示意；记录图案、位置、对称性和可见轮廓。',[])
category('sleepwear','睡衣与居家夜服','两件睡衣、睡裙、连体夜服和外罩袍分列，展示完整不透明服装与开合结构。',['R06'])
category('schoolwear','校服与校园制服','13–17岁校园服装原创参考，分日常制服、运动与季节穿搭；校徽位置留空。',[])
category('youthwear','青少年与青春期日常服装','13–17岁日常、运动、季节与活动穿搭，按舒适松量、活动范围和叠穿设计整理。',[])

block('hair_accessories','发箍与发带细分','''
窄硬齿梳发箍|narrow toothed headband|窄弧形硬箍内侧有短齿，两端弯向耳后，齿与饰面分开。
宽缎面包布发箍|wide satin-covered headband|宽弧形骨架包缎面，内侧止滑层和两端包边清楚。
软垫隆起发箍|padded raised headband|箍面有隆起软垫，内弧贴头，截面厚度可辨。
中央扭结发箍|center-knot headband|包布箍顶部形成中央扭结，结的交叠与箍骨分开。
侧结短尾发箍|side-bow short-tail headband|结饰在箍侧，两个短尾垂下，结根缝在箍面。
双轨细弧发箍|double-rail slim headband|两条平行细弧通过两端连接，轨间空隙和耳后端点。
波浪金属发箍|wavy metal headband|金属细箍沿额上呈连续波浪，内侧光滑，两端圆钝。
链节软骨发箍|chain-link flexible headband|短链节覆在柔性箍骨上，链环、内垫和端点可见。
珠串单排发箍|single-row bead headband|小珠沿弧形箍单排排列，珠根固定在包布骨架上。
花簇侧饰发箍|side-flower cluster headband|原创布花簇在单侧，花簇底座和箍面连接清楚。
蕾丝软带发箍|lace-covered soft headband|蕾丝覆在完整软带上，后端弹性连接，带宽和内衬可见。
交叉前额弹力发带|cross-front elastic hairband|两条布带在前额交叉，后部弹力段，交叉上下关系。
系结长尾头巾带|long-tail tied hairband|长布带两端打结并垂尾，带体宽度和结环完整。
运动止滑宽发带|wide nonslip sports hairband|宽针织环带，内侧细止滑条、弹性后段和缝线。
环形编绳发带|woven-cord ring hairband|编绳构成闭环，后部调节结，绳股交编清楚。
细链额饰发带|fine-chain forehead hairband|原创细链绕额，后部小扣与中央垂饰，链长留完整。
''',('发箍','头箍','发带','headband','hairband'))

block('hair_accessories','发卡与发夹细分','''
按压弹片发卡|snap hair clip|弧形金属弹片按压开合，中央舌片与外框分开。
长方弹簧背夹|rectangular spring barrette|长方饰面背后有弹簧扣，展示背面夹条与铰链。
小型交叉一字夹|crossed bobby pins|两枚一字夹交叉，各夹有上下两片与波纹止滑边。
波纹单枚一字夹|wavy bobby pin|一面波纹一面平直，末端圆头与弹性夹口清楚。
双齿短侧发夹|two-prong side clip|两个短夹齿接在装饰底座上，背面夹齿和弹片可见。
鸭嘴长尖发夹|duckbill hair clip|细长上下夹片前端收尖，尾端弹簧和指压片。
鳄鱼齿口发夹|alligator hair clip|夹口有连续短齿，尾部弹簧与铰接可见，展示张开状态。
大齿抓夹|large claw clip|两组弧形长齿交错，中央弹簧与背部按柄完整。
小圆壳抓夹|small rounded claw clip|圆壳外形接短抓齿，开口和弹簧根部可辨。
蝴蝶轮廓抓夹|butterfly-shaped claw clip|原创蝶形两翼作为按柄，背后交错抓齿明确。
镂空三角背夹|open-triangle barrette|三角空框饰面与后夹条，装饰框不代替夹口。
布结横条发卡|fabric-bow barrette|大布结固定在横条背夹上，结根、夹条与弹簧。
圆盘转扣发卡|disc twist-clasp hair clip|圆盘饰面接旋转卡扣，卡扣和盘面分件显示。
软磁夹片发卡|magnetic flat hair clip|两片包布薄片磁吸，边缘缝线、分离夹面与小磁扣可见。
细珠悬链侧夹|bead-chain side barrette|短侧夹下挂细珠链，链根小环与背夹结构完整。
梳齿侧插发卡|side-insert comb clip|短饰面下接一排梳齿，插入方向与齿根可辨。
''',('发卡','发夹','卡子','一字夹','抓夹','barrette','hair clip'))

block('hair_accessories','发簪发钗与梳饰细分','''
单杆圆头素簪|single-stick round-head hairpin|单根长杆与圆头，杆尾圆钝，主体略弯便于观察。
双叉U形盘发簪|U-shaped bun pin|双长叉从弯曲顶端伸出，叉尖圆钝，发髻插入结构清楚。
双杆平行发钗|parallel double-stick hairpin|两根平行杆连接同一饰头，杆间距与共同根部。
螺旋旋入盘发针|spiral twist-in hair pin|螺旋杆形成旋入形，顶部连接与圆钝端点；图例采用单杆装饰变体。
扁杆叶形簪|flat leaf-headed hair stick|扁长杆接原创叶形饰头，扁截面和叶柄根部。
曲杆月形簪|curved crescent hair stick|轻弯杆与月形饰头，饰头开口和杆部接点。
花头短垂链簪|flower-head dangling hairpin|原创花饰头下悬两条短链，链环、花根和长杆清楚。
珠顶双链步摇改编|bead-top double-chain hairpin|原创珠顶与双垂链，按现代装饰改编，双链挂点和簪杆分辨。
几何环顶发簪|geometric-ring hair stick|环形镂空饰头接单杆，圆环厚度与杆根清楚。
分叉枝形发簪|branch-shaped hairpin|原创短枝饰头向两侧分叉，下方单杆完整，枝不是头发。
长杆穿孔盘发饰|pierced-panel bun ornament|薄饰板中央穿孔，长杆穿过板孔，板与杆是独立部件。
横梳珠边盘发饰|bead-edged hair comb|一排梳齿上方横弧珠边，齿根与珠架分开。
宽弧镂空梳饰|wide openwork hair comb|宽弧镂空饰面下接短齿，金属板厚度与齿数可见。
细齿侧插花梳|fine-tooth floral side comb|原创小花横排下接细梳齿，花簇底座与插齿分辨。
簪杆发网组合饰|hair-stick and net ornament|长簪穿过小发网边圈，网线、边圈和簪杆固定关系。
折叠叉骨盘发夹|folding-fork bun clasp|两根叉骨在铰点折合，后扣与饰面分开，原创盘发件。
''',('发簪','发钗','盘发簪','步摇','簪子','hairpin','hair stick','hair comb'))

block('hair_accessories','发圈与扎发固定件','''
无接缝细弹力发圈|seamless thin elastic hair tie|细圆绳闭环，无外露金属接头，圈体厚度可见。
宽扁弹力发圈|wide flat elastic hair tie|扁宽弹性环带，接缝在内侧，内外面分辨。
布褶甜甜圈发圈|fabric scrunchie|软布围成有褶圆圈，内藏弹力芯，褶边和中孔清楚。
大蝴蝶结发圈|large-bow hair tie|弹力圈上缝大布结，圈根和结尾清楚，完整展示。
长飘带发圈|long-ribbon hair tie|布圈接两条长飘带，接缝与带末端，可比较带长。
双珠绳扣发圈|two-bead cord hair tie|两端珠扣通过弹性绳收束，珠孔与绳圈可见。
电话线螺旋发圈|spiral coil hair tie|弹性螺旋圈围成闭环，连续绕线与接头完整。
钩端弹绳扎发件|hook-ended elastic hair bungee|弹绳两端各有小钩，钩口、绳段与连接套分开。
滑扣可调发绳|adjustable sliding-cord hair tie|发绳穿过滑扣改变环长，扣孔、双绳与止端。
软管包芯发圈|tube-covered elastic hair tie|软布管包住弹力芯，管体和内侧接缝，原创建构。
花形布团发圈|flower-scrunchie hair tie|布褶形成原创花形外圈，中央弹圈清楚，花根相接。
珠链环扣发圈|bead-chain clasp hair tie|珠串与弹性段组成发圈，装饰珠链不代替弹力部分。
金属壳套筒扎发件|metal cuff ponytail tie|外部圆筒壳套在发圈外，壳开合与内圈分件。
双环连接发圈|linked double hair ties|两个弹力圈以短连接带相连，两环各有独立开口。
软布包边发尾扣|soft fabric tail clasp|包布短扣环围住发尾，侧扣和内衬可见。
丝巾绕圈扎发件|scarf-wrapped hair tie|小丝巾绕在弹圈上，结尾与圈根分开，原创图案。
''',('发圈','头绳','发绳','皮筋','扎发件','scrunchie','hair tie'))

block('earrings','耳饰形态与佩戴扣件','''
细线扣合圈耳环|thin hinged hoop earrings|细圆环在一端铰接，另一端细扣针与扣座，成对展示。
宽管铰链圈耳环|wide tubular hoop earrings|中空宽管环、铰接处与扣口，厚度和内圈可见。
贴耳小圈耳环|small huggie earrings|小直径宽圈紧凑，后端扣合，示意耳垂位置的小侧图。
椭圆垂环耳环|oval drop-hoop earrings|耳钩下挂椭圆环，环根小吊环与钩体分开。
方框垂环耳环|square-frame drop earrings|细方框悬在短耳扣下，方框转角和连接环。
开口弧片耳环|open-arc plate earrings|薄弧金属片接后针，开口与板厚清楚，非完整闭环。
双圆叠环耳环|double-linked circle earrings|上下两个不同大小圆环互接，最上方耳扣明确。
转轴摆片耳环|pivot-panel earrings|几何小片通过横轴摆动，耳扣、轴和悬片分件。
耳线穿链垂饰|threader-chain earrings|细长穿耳棒接链条与小吊件，完整链长和棒端。
扭绳结环耳环|rope-knot hoop earrings|环面有原创扭绳纹，闭合扣与纹理两层清楚。
叶片短垂耳环|short leaf-drop earrings|原创叶片从耳钩小环垂下，叶脉为刻纹，连接可见。
球串短垂耳环|short bead-drop earrings|数枚小球沿短杆连接，顶部耳钩和底部收尾。
双侧不等长耳环|asymmetric-length earrings|一侧短环一侧长垂链，成对展示，原创建构。
螺旋压夹耳饰|screw-back clip earrings|圆饰面后有可调螺旋夹背，夹垫和旋钮清楚。
弹片耳夹饰|spring-clip earrings|短弹片夹背与软夹垫，正饰面和背扣分开。
无针弧形耳骨夹|open-arc ear cuff|开口弧形扣夹住耳缘，产品旁小耳侧图说明位置。
''',('耳环','耳饰','earring'))

block('pendants','吊坠主体与链环结构','''
圆片刻纹吊坠|engraved disc pendant|圆片主体、顶部吊环与细链，刻纹为原创几何图案。
镂空环形吊坠|open-ring pendant|厚圆环作主体，吊环与环体分件，内孔清楚。
水滴框嵌吊坠|teardrop-set pendant|水滴框包住透明感饰石，爪口、背座与链环可见。
长条坠牌项链|bar-tag pendant necklace|窄长坠牌横向或竖向挂链，链孔与板边厚度。
几何多片吊坠|geometric-panel pendant|三片原创几何板由小环连接，最上方链环明确。
双环套叠吊坠|nested double-ring pendant|大小双环套叠但各有连接点，细链与双环分辨。
可开合小盒吊坠|hinged locket pendant|小盒有侧铰链和开合缝，内外壳与吊环可见。
透明框夹片吊坠|clear-frame inset pendant|透明框夹原创小图片，外框扣点、图片和链环。
珠滴单坠项链|single-bead-drop necklace|单珠下方小金属托、顶孔吊环与完整细链段。
星月叠件吊坠|star-moon layered pendant|原创星与月两件用短环相连，分别悬挂而不融为一块。
羽片刻纹吊坠|feather-plate pendant|原创羽片形板、刻纹与顶环，板为首饰而非真羽毛。
钥匙轮廓吊坠|key-shaped pendant|原创短钥匙形主体与顶环，齿形和厚度清楚。
棱柱包框吊坠|framed-prism pendant|透明感棱柱包在细框中，棱线、底托和吊环。
长链流苏吊坠|long-chain tassel pendant|上方主链连接多条短流苏链，束口小帽与链尾。
双端穿链横坠|two-hole horizontal pendant|横向饰板两端穿链，双链孔与中心图形，原创建构。
可滑动珠环吊坠|sliding-bead loop pendant|细链穿过可滑珠环，珠孔、自由链尾和小垂件。
''',('吊坠','项链','坠饰','颈饰','pendant','necklace'))

block('studs','钉饰形态与佩戴位置','''
圆珠耳钉|round-bead ear studs|圆珠饰头、直针与独立后扣，产品三分之二视图。
扁圆片耳钉|flat-disc ear studs|薄圆片与后针，片厚和后扣清楚，成对展示。
四爪小饰石耳钉|four-prong stone studs|小饰石由四爪固定，爪座、针和后扣分开。
方片耳钉|square-plate ear studs|小方板饰头和后针，圆钝转角与后扣可见。
小环连片耳钉|mini-ring panel studs|后针饰头下连一只小环，小环活动连接。
弧线贴耳排钉|curved cluster ear studs|多个小珠沿弧形底架排布，后针位置与排珠分开。
平背小耳钉|flat-back ear stud|前饰头、短直杆和平背圆片，产品分件可见。
短杆双球耳饰|short double-ball ear bar|短杆两端各有圆球，成品完整，不展示佩戴操作。
耳钉连耳夹短链|stud-to-cuff short chain|耳钉与无针耳夹用短链连接，钉背、夹口与链根。
双钉连环耳饰|linked double-stud earrings|两枚小钉由短连接环相连，两个后扣和吊点明确。
小弧鼻环饰|small nose-ring ornament|成年鼻翼局部显示小弧环，旁边完整产品，表面平滑。
单珠鼻钉饰|single-bead nose stud|成年鼻翼局部有小珠饰点，产品形状与饰头清楚。
弯杆眉饰钉|curved-bar eyebrow ornament|成年眉外侧小弯杆两端圆球，局部位置明确，原创建构。
平珠唇侧钉饰|flat-bead side-lip ornament|成年脸部嘴角外侧小平珠装饰，侧位局部与独立物件。
双球耳横杆饰|double-ball ear crossbar ornament|成年耳缘示意横杆与两端球头，展示成品形状，原创建构。
胸前布料铆钉饰|fabric rivet-stud ornament|铆钉固定在衣料上，圆头、布料与背座剖分示意，区别于身体首饰。
''',('钉饰','stud','piercing jewelry'))

block('gloves','指型与礼仪手套','''
五指短棉手套|short five-finger cotton gloves|五指完整分开，腕口到腕骨，掌背缝线和棉布褶皱。
露指短布手套|short fingerless fabric gloves|每指留独立指口，指根有缝线，腕口松紧可辨。
半指皮手套|half-finger leather gloves|皮革包住掌部及指根，半指端口和背部扣袢。
拇指分离连指手套|thumb-separated mittens|四指合在一只指袋内，拇指独立，腕口罗纹。
翻盖连指手套|flip-top mittens|四指盖片可翻起，内层半指结构、固定纽扣与拇指。
三分区指袋手套|three-section finger-pocket gloves|拇指独立，其余四指分为两组双指袋，分组缝线清楚。
腕口V缺礼仪手套|V-notch wrist dress gloves|五指薄布手套腕背有小V缺口，包边与短扣袢。
珍珠扣短礼仪手套|pearl-button dress gloves|腕侧一枚珠状扣，短开口和五指缝线，原创物件。
肘下长布手套|below-elbow fabric gloves|完整五指接长筒到肘下，腕段与筒侧缝清楚。
过肘缎面礼仪手套|above-elbow satin gloves|五指和长筒完整，缎面反光、肘部软褶与筒口。
长筒露指蕾丝手套|long fingerless lace gloves|独立指口、腕部和长蕾丝筒，内有浅色人台承托，不画身体细节。
系带长筒手套|lace-up long gloves|完整五指长筒一侧穿孔系带，带孔、交叉带与底衬。
开衩钮扣长手套|button-slit long gloves|腕内侧纵向扣开口，多枚小扣和长筒接缝可见。
荷叶腕边短手套|ruffled-cuff short gloves|五指薄布手套腕口接一圈荷叶边，边根缝线。
拳背镂空驾驶手套|knuckle-cutout driving gloves|皮手套拳背小开孔、指根透孔与腕扣，独立五指。
对比包边网纹手套|contrast-bound mesh gloves|网纹五指手套指缘与腕口有实色包边，网孔和内人台清楚。
''',('手套','指套','礼仪手套','露指手套','gloves','mittens'))

block('gloves','材质季节与工具手套','''
罗纹针织保暖手套|rib-knit warm gloves|完整五指针织、长罗纹腕口，针目与指根接缝。
绒里翻口冬手套|fleece-lined winter gloves|厚五指手套、翻折绒腕口与掌片，不同材质可见。
绗缝长腕冬手套|quilted long-cuff winter gloves|背部绗缝、独立掌片和长腕筒，拉紧带在腕处。
防风布壳手套|wind-shell fabric gloves|平滑布壳、软掌片和松紧腕口，外观结构参考。
长筒雨用橡胶手套|long-cuff rubber-style gloves|五指连贯橡胶感、长筒卷边与指端纹理，物件示意。
短腕薄膜手套|thin-film short-cuff gloves|五指薄膜感手套套在平滑中性手模上，腕口卷缘清楚。
帆布掌片工具手套|canvas-palmed work gloves|厚帆布掌片、织物手背和指根加固，腕口明确。
皮革护掌园艺手套|leather-palm garden gloves|掌部皮片、布手背与中长护腕，缝线和指尖补片。
运动抓握短手套|sports-grip short gloves|半指手套掌部有分区垫、背部网布和腕扣。
骑行长指手套|full-finger cycling gloves|五指运动布、掌部分区和背部拉片，原创建构。
攀爬指端补片手套|reinforced-tip climbing-style gloves|指尖与掌边补片、腕部扣带，完整五指，视觉装备改编。
剑术长腕手套改编|long-cuff fencing-style gloves|厚掌片、长护腕筒和筒口扣带，原创运动装备外观。
金属片装饰手套|metal-panel decorative gloves|五指布手套背面加原创小金属片，片根有铆扣固定。
魔法印纹长手套|magic-pattern long gloves|不透明长布手套印原创几何纹，纹样与接缝分开。
可拆腕筒组合手套|detachable-cuff modular gloves|短手套与独立长腕筒用按扣连接，图例为露指内手套变体，拆分点清楚。
腕袋机能手套|wrist-pocket utility gloves|五指手套腕背有小拉链袋，袋面与掌背结构可见。
''',('手套','冬手套','工具手套','运动手套','gloves'))

block('body_art','脸部彩绘与原创妆面标记','''
单颊花瓣彩绘|single-cheek petal face paint|成年脸颊单侧原创花瓣图形，沿颧部展开，颜色贴皮而非立体花饰。
双颊对称星点彩绘|symmetric star-dot face paint|成年两颊对称小星与点，图案边缘清楚，眼鼻嘴完整。
鼻梁横条彩绘|nose-bridge stripe face paint|成年鼻梁与两颊连成短横色条，条宽均匀，不当作伤口。
额心菱形彩绘|forehead diamond face paint|成年额心原创菱形图形，下尖止于眉上，眉眼仍清楚。
单眼外缘弧纹彩绘|single-eye outer-arc face paint|成年单眼外侧两道弧线，避开眼球，曲线沿眼眶外缘。
双眼几何面罩彩绘|geometric eye-mask face paint|成年双眼周围原创几何涂色，眼睑与虹膜清楚，非真实面具。
颧侧羽纹彩绘|cheekbone feather-line paint|成年一侧颧部原创羽状线条，羽纹为平面绘色。
脸侧叶蔓彩绘|side-face leaf-vine paint|成年鬓侧至颊部的原创叶蔓线纹，头发与绘纹分辨。
下颌折线彩绘|jawline zigzag face paint|成年下颌侧有规则折线色纹，沿脸轮廓分布，嘴部不遮挡。
眼下滴形装饰彩绘|under-eye droplet face paint|成年眼下小滴形装饰图案，平面清楚，无流血或受伤语境。
额侧彩块拼色|temple color-block face paint|成年额侧数块原创彩色几何块，块缘、皮肤和发际分开。
半脸渐变彩绘|half-face gradient paint|成年半侧脸有柔和色彩渐变，额鼻中线为分界，正常五官可见。
双颊细点带彩绘|cheek dotted-band paint|成年两颊各一条细点带，点距规律，区别于自然雀斑。
鼻尖圆点节庆彩绘|nose-tip festival dot paint|成年鼻尖一枚小色点、颊部短线，节庆原创妆面示意。
银色弧线额饰彩绘|silver-arc forehead paint|成年前额银灰原创弧线与短点，金属色是平面颜料。
原创舞台分区妆面|original stage color-zone makeup|成年额颊分区涂色与简洁眼部线条，原创图形，不套用戏曲脸谱程式。
''',('脸部彩绘','面部彩绘','彩妆标记','脸部绘画','face paint','face painting'))

block('body_art','纹身贴与成年装饰纹样','''
前臂细线花枝纹身|forearm fine-line floral tattoo design|成年前臂局部有原创细线花枝，线宽、朝向和前臂弧面清楚。
前臂几何环带纹身|forearm geometric-band tattoo design|成年前臂原创几何带绕臂，正面与侧面连接，非布手环。
腕侧星点纹身|wrist-side star-dot tattoo design|成年手腕外侧小星点群，点距和腕部位置明确。
手背叶片纹身|hand-back leaf tattoo design|成年手背原创细叶图形，沿手背展开，不覆盖指关节细节。
上臂水波线纹身|upper-arm wave-line tattoo design|成年上臂局部原创水波线，连续曲线跟随肌肤表面。
肩外几何片纹身|outer-shoulder geometric tattoo design|成年肩外小面积几何片图案，展示肩部局部和不透明衣缘。
颈侧小月纹身|neck-side crescent tattoo design|成年颈侧小月形原创图案，位于耳下，发束不遮挡。
耳后短线纹身|behind-ear short-line tattoo design|成年耳后原创短线与点，侧面近景，耳廓和纹样分辨。
眉外星纹纹身贴|outer-brow star tattoo decal|成年眉外侧小星图案贴，轮廓平面，眼部正常清楚。
颊侧细叶纹身贴|cheek-side leaf tattoo decal|成年颊侧原创细叶纹身贴，图案和头发分层，非伤痕。
太阳穴几何纹身贴|temple geometric tattoo decal|成年太阳穴小型原创几何贴纹，线条紧凑，发际明确。
下颌月点纹身贴|jaw crescent-dot tattoo decal|成年下颌侧小月与点组合，平面贴纹，位置不延入嘴部。
小腿外侧藤线纹身|outer-calf vine tattoo design|成年小腿局部原创藤线，裤脚衣缘和脚踝位置提供上下文。
踝侧小环纹身|ankle-side ring tattoo design|成年踝侧几个原创细线小环，图形贴皮，不是金属脚链。
肩背花形纹身贴|upper-back floral tattoo decal|成年上背肩外局部原创花形贴纹，周围为不透明上衣边缘。
原创几何魔纹贴|original geometric magic decal|成年前臂上原创环线魔纹，平面颜料或贴纹，不表现发光伤口。
''',('纹身','纹身贴','刺青图案','tattoo','tattoo decal'))

for e in CATALOG[-16:]:
    if any(word in e['name'] for word in ['眉外','颊侧','太阳穴','下颌']):e['aliases']+= ['脸部纹身','面部纹身']

for e in CATALOG:
    if e['category']=='earrings':
        if '夹' in e['name']:e['aliases'] += ['耳夹','clip-on earring']
        if '耳骨夹' in e['name']:e['aliases'] += ['ear cuff']
    if e['category']=='studs' and '耳' in e['name']:e['aliases'] += ['耳钉']
