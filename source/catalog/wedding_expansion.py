"""Edition 19: bridal gowns, wedding attire and complete ceremony ensembles."""
from catalog_content import CATALOG, category, add

NEW_CATEGORIES=['bridal_gowns','wedding_attire']
category('bridal_gowns','婚纱','按裙身廓形、领袖、材质与头纱搭配比较32款完整婚纱造型；服装、头饰和鞋履共同展示，便于拆分为角色部件。',['R75'])
category('wedding_attire','婚服','48套婚礼服装，分中式古风嫁衣、现代中式婚服及其他婚礼礼装；条目标明文化灵感与改编语境，历史形制沿资料进一步核对。',['R75','R76','R77','R78'])

def block(key,dimension,text,context,refs):
    lines=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(lines)==16,(dimension,len(lines))
    for name,en,recipe,styles in lines:
        add(key,dimension,f'{name}|{en}|{recipe}。原创成年女性婚礼整套造型，衣缘、裙裤层次与配饰固定点可辨。')
        CATALOG[-1].update(added_in='19.0',wedding_reference=True,wedding_context=context,age_context='成年女性婚礼服装参考',outfit_components=recipe.split('；'),styles=styles.split(',') if styles else [],reference_ids=refs,aliases=['婚礼服装','婚礼穿搭','新娘服装','婚礼专题',dimension,context,'bridal','wedding outfit'])

block('bridal_gowns','婚纱廓形与裙摆','''
A字缎面婚纱|A-line satin bridal gown|象牙白简洁有肩带收腰上身与A字落地缎裙；短拖尾；珍珠发梳固定肘长头纱；白色低跟鞋|minimal
公主蓬裙婚纱|princess ball-gown wedding dress|奶白有肩带贴腰上身与大体积钟形纱裙；宽裙撑轮廓；小冠固定长头纱；象牙低跟鞋|retro
膝下鱼尾婚纱|knee-flare mermaid bridal gown|白色宽肩带贴身长裙在膝下明确展开鱼尾；细蕾丝衣缘；小发梳头纱；白色细带鞋|retro
柔和喇叭裙婚纱|soft trumpet bridal gown|奶白短袖收腰婚纱在大腿下段渐渐外扩；较柔和喇叭裙摆；短头纱与小耳坠；低跟鞋|minimal
直筒柱形婚纱|column silhouette wedding gown|奶白方领宽肩带直筒及踝婚纱；裙侧少量褶量；简洁发梳长头纱；尖头平底鞋|minimal
高腰帝政式婚纱|empire-waist bridal gown|象牙色短袖婚纱腰线位于胸下；轻软裙身垂至地面；细缎带束发与轻头纱；白色便鞋|retro
茶长复古婚纱|tea-length bridal dress|奶白有肩短袖贴腰上身；蓬松伞裙长度到小腿中部；短面纱小帽；白色玛丽珍鞋|retro
及膝短婚纱|knee-length short bridal dress|白色宽肩带方领收腰短婚纱；裙摆及膝不过分蓬起；小蝴蝶结短头纱；白色低跟鞋|minimal
前短后长婚纱|high-low hem bridal gown|象牙白短袖婚纱；前裙到小腿、后裙延伸短拖尾；后脑发梳头纱；细带低跟鞋|retro
长拖尾侧展婚纱|side-view long-train wedding gown|奶白有肩带A字婚纱；四分之三侧转让长拖尾在同一格内向后展开；细冠长头纱；白色鞋尖可见|retro
极简厚缎婚纱|minimal heavy-satin bridal gown|奶白简洁圆领无袖上身；厚缎高腰中长伞裙；无大面积珠饰；珍珠发梳与白色低跟鞋|minimal
全蕾丝衬底婚纱|lined all-over lace wedding gown|象牙色花卉蕾丝外层覆盖完整不透明长袖衬底；收腰A字落地裙；蕾丝边头纱；白色鞋|retro
层叠薄纱婚纱|tiered-tulle bridal gown|奶白宽肩带上身；三层清楚分段的薄纱蓬裙配不透明内裙；细冠短头纱；白色低跟鞋|girly
箱褶裙摆婚纱|box-pleated skirt bridal gown|白色高领短袖上身；硬挺深箱褶中长裙摆；细腰带与蝴蝶结发饰头纱；白色平底鞋|retro
斜覆片不对称婚纱|asymmetric overskirt bridal gown|象牙白简洁有肩带上身；一侧缝接斜垂长覆片盖住直筒内裙；短头纱；白色细带鞋|minimal
立体花饰婚纱|sculptural-flower bridal gown|奶白方领短袖收腰婚纱；腰侧与裙摆局部缝接立体布花；圆润A字长裙；小花梳头纱与白鞋|girly
''','婚纱廓形参考',['R75'])

block('bridal_gowns','婚纱领袖与头纱搭配','''
方领宽肩带婚纱|square-neck wide-strap bridal gown|象牙白方领宽肩带上身；收腰及踝A字裙；简洁发梳固定长头纱；白色方头低跟鞋|minimal
心形领吊带婚纱|sweetheart strap bridal gown|奶白心形领有细吊带上身；薄纱覆盖不透明落地伞裙；珍珠发箍短头纱；白色细带鞋|girly
无肩带抹胸婚纱|strapless bridal gown|象牙白直线抹胸完整不透明上身；腰线清楚的A字长裙；小冠固定后垂头纱；白色低跟鞋|minimal
一字肩婚纱|Bardot off-shoulder bridal gown|奶白横向折领露双肩、短袖包住上臂；收腰缎面及踝长裙；低发髻长头纱；白色鞋|retro
单肩垂褶婚纱|one-shoulder draped bridal gown|白色不透明单肩斜领上身；同侧细垂褶连接直筒长裙；细发梳头纱；银白低跟鞋|minimal
挂脖婚纱|halter-neck bridal gown|象牙白挂脖领绕颈连接完整不透明上身；肩部外露、A字长裙；短头纱与耳钉；白色细带鞋|minimal
高领长袖婚纱|high-neck long-sleeve bridal gown|奶白小立领蕾丝覆领与长蕾丝袖、主体配不透明衬底；腰线收紧、及踝长裙；细蕾丝领缘与长头纱；白色鞋|retro
网纱覆领婚纱|illusion-yoke bridal gown|奶白完整不透明心形上身外加锁骨至领口的薄网纱覆片；A字长裙；简单耳钉与后垂头纱；白鞋|retro
蕾丝长袖婚纱|lace-sleeve bridal gown|象牙色不透明方领主体接合长蕾丝袖；收腰轻蓬裙；蕾丝边中长头纱；白色低跟鞋|retro
泡泡袖婚纱|puff-sleeve bridal gown|奶白圆领短泡泡袖上身；完整收腰长伞裙；小蝴蝶结后垂头纱；白色玛丽珍鞋|girly
花边盖袖婚纱|scalloped cap-sleeve bridal gown|象牙白小圆领与花边短盖袖；A字及小腿长裙；珍珠发梳短头纱；白色平底鞋|retro
分离长袖婚纱|detachable-sleeve bridal gown|奶白不透明有细肩带主体；独立灯笼长袖在上臂用袖口带固定；高腰长裙；小冠头纱与白鞋|girly
披风肩婚纱|cape-shoulder bridal gown|白色不透明长袖直筒婚纱；领后接轻薄及地披风、区别于头顶头纱；小发梳；白色低跟鞋|minimal
短鸟笼面纱婚纱|birdcage-veil bridal ensemble|奶白短袖及膝A字婚纱；小帽网状鸟笼面纱只覆额头和上半脸、面孔可辨；珍珠耳钉；白色低跟鞋|retro
蕾丝曼蒂拉头纱婚纱|mantilla-veil bridal ensemble|象牙白收腰长婚纱配不透明主体与长蕾丝袖；蕾丝边曼蒂拉头纱从头顶沿两侧垂落、脸部敞开；小耳坠；白色鞋|retro
兜帽披纱婚纱|hooded bridal cape ensemble|奶白不透明高领长袖长婚纱；轻薄开放式兜帽披纱从领后垂落、脸部清楚；珍珠发饰；白色低跟鞋|minimal
''','婚纱结构与头纱参考',['R75'])

block('wedding_attire','中式古风嫁衣灵感','''
凤冠霞帔古风婚服|phoenix-coronet xiapei bridal inspiration|红色立领长袖袍裙；两条窄长霞帔式饰带从肩部垂到裙前；小型凤冠与流苏；红色绣鞋；架空古风改编|chinese
交领红袄百褶嫁衣|cross-collar red ao pleated bridal skirt|红色右衽交领短袄；金边百褶长裙；简洁花冠与后垂红带；红色绣鞋；古风婚礼改编|chinese
圆领袍式古风婚服|round-collar robe bridal inspiration|朱红圆领长袍带侧门襟；下摆露出内层长裙；金色小冠与红色腰带；红鞋；架空婚礼袍改编|chinese
对襟大袖披袍嫁衣|front-opening wide-sleeve bridal robe|绛红宽大袖对襟外袍敞开展示内层红裙；金边衣缘与窄腰带；花簪小冠；绣鞋；古风改编|chinese
袄裙马面式婚服|ao and mamian-style bridal skirt|红色立领长袖袄；金色装饰裙门与两侧褶片的红色马面式长裙；小冠发簪；红色绣鞋；形制灵感改编|chinese
立领短袄长裙嫁衣|standing-collar bridal jacket skirt|红色立领盘扣短袄；深红绣花直筒长裙；两侧小流苏发簪；红绣鞋；古风礼装改编|chinese
齐胸襦裙婚服灵感|high-bust ruqun bridal inspiration|朱红短襦配高系于胸上的红色长裙；宽披帛在两臂外侧自然垂落；花冠与绣鞋；古风创作改编|chinese
对襟半臂叠穿嫁衣|banbi-layered bridal ensemble|红色长袖内襦外叠金红对襟短袖半臂；深红长褶裙；披帛与花钿式发饰；红绣鞋；古风改编|chinese
曲裾袍式婚服灵感|curved-hem robe bridal inspiration|深红右衽长袍的衣缘以斜线绕至身侧；黑红相间宽腰带；高髻小簪；红鞋；现代古风曲裾灵感改编|chinese
玄纁配色古风嫁衣|dark-and-vermilion bridal palette|玄黑交领长袖上衣配纁红长裙；红黑分区与细金边；简洁金簪；深红鞋；架空配色方案|chinese
绿褙子朱裙嫁衣|green beizi red-skirt bridal look|墨绿长袖对襟褙子外罩红色上衣与朱红长裙；金色衣缘；小花冠与红绣鞋；古风创作改编|chinese
红背子金边长裙婚服|red long-jacket gold-border bridal look|红色长对襟背子配金色领缘；深红不透明长裙；长流苏发簪与小团扇；红鞋；古风礼装改编|chinese
窄袖长衣披帛嫁衣|narrow-sleeve bridal robe scarf|枣红窄袖交领长衣；绯红长裙与细金腰封；长披帛从肩后自然垂下；金簪和红鞋；架空改编|chinese
大袖衫团花嫁衣|wide-sleeve floral bridal ensemble|红色宽大袖外衫与同色长裙；原创圆形花卉团纹集中领缘和裙前；小冠红带；红绣鞋；古风改编|chinese
云肩式古风嫁衣|cloud-collar bridal inspiration|深红立领长袖袄裙；肩部独立金红四瓣云肩式覆片；小凤簪与流苏；红鞋；架空礼服改编|chinese
金绣围裳古风嫁衣|gold-embroidered overskirt bridal look|朱红交领长袖上衣；深红底裙外加金边围裳式覆裙；小冠与腰侧垂带；绣鞋；古风婚礼改编|chinese
''','中式古风创作改编',['R27','R76'])

block('wedding_attire','现代中式婚服与敬酒礼装','''
红金龙凤褂婚服|red-gold dragon-phoenix bridal qungua|红色立领对襟短褂与直筒长裙；原创金线龙凤式装饰分别布在衣裙；小簪与绣花鞋；现代中式婚服|chinese
银线花卉裙褂婚服|silver-floral bridal jacket-skirt|红色立领对襟短褂与长裙；银色原创花卉绣纹与细滚边；珍珠发簪；红色低跟鞋；现代婚礼套装|chinese
密绣金地裙褂婚服|dense-gold embroidered qungua look|金线密绣的短褂与长裙上保留细红色底地；立领对襟与独立裙腰；小花冠；红绣鞋；现代中式婚礼装|chinese
简绣红缎裙褂婚服|minimal-embroidery satin qungua|红缎立领对襟长袖短褂；红色直筒长裙只在衣缘裙缘有少量金绣；小簪；红色便鞋；现代简约婚服|chinese,minimal
红金秀禾风格婚服|red-gold Xiuhe-inspired bridal outfit|红色宽袖斜襟上衣；金边宽摆长裙；原创花鸟纹和双侧流苏发饰；红色绣鞋；现代秀禾风格|chinese
霞粉秀禾风格婚服|dusty-pink Xiuhe-inspired bridal outfit|霞粉宽袖立领斜襟上衣与粉金长裙；少量金绣与垂穗；花簪小冠；粉色绣鞋；现代婚服改编|chinese
酒红长袖秀禾婚服|burgundy long-sleeve Xiuhe outfit|酒红立领宽袖上衣；同色宽摆长裙配金色裙前纹饰；低髻金簪；深红绣鞋；现代秀禾风格|chinese
米金秀禾风格婚服|ivory-gold Xiuhe bridal ensemble|米金立领斜襟宽袖上衣；米金不透明宽摆长裙配红色小滚边；花簪流苏；金色绣鞋；现代婚礼设计|chinese
红色长旗袍婚服|red long-qipao bridal ensemble|红色立领盘扣短袖及踝旗袍；低侧衩内层完整覆盖；金色小耳坠与小手包；红色低跟鞋；现代婚礼穿搭|chinese
金绣长袖旗袍婚服|gold-embroidered long-sleeve bridal qipao|深红立领长袖及小腿旗袍；金色花卉绣纹集中肩与下摆；小发簪和手包；红色鞋；现代婚礼装|chinese
旗袍短披肩婚服|qipao capelet bridal ensemble|酒红无袖立领长旗袍外罩同色短披肩；低侧开衩；花簪与小手包；细带低跟鞋；现代敬酒礼装|chinese
新中式短褂长伞裙|modern Chinese bridal jacket full-skirt|红色小立领盘扣短褂；同色高腰中长伞裙；金色细耳环和小手包；红色平底鞋；现代中式婚礼套装|chinese
红色立领裤装婚服|red mandarin-collar bridal trouser suit|朱红立领盘扣长袖上衣；同色垂坠阔腿长裤；金色腰扣与小手包；红色低跟鞋；现代婚礼裤装|chinese,minimal
红色云肩披覆婚服|red bridal cloud-collar overlay|红色简洁长袖连裙；金红独立云肩式短披覆；流苏发簪与小手包；红色鞋；现代中式礼服改编|chinese
红金提花敬酒礼服|red-gold jacquard reception dress|红金原创提花小立领短袖中长连裙；细金腰带；小耳坠与硬壳手包；红色低跟鞋；现代敬酒礼装|chinese
新中式红缎长马甲套装|modern red-satin bridal waistcoat set|奶白立领长袖衬衣外叠红缎长马甲；红色宽直长裤；金色小簪与手包；红色鞋；现代婚礼套装|chinese
''','现代中式婚礼穿搭',['R76','R75'])

block('wedding_attire','其他文化婚服与现代礼装','''
白无垢棉帽子婚服灵感|shiromuku wataboshi bridal inspiration|日式灵感：白色小袖内衣与白色外穿打挂；宽白色腰带；圆顶棉帽子开放面孔；白袜与草履；原创改编|
白无垢角隐婚服灵感|shiromuku tsunokakushi bridal inspiration|日式灵感：白色小袖和白色打挂；白腰带；白色角隐式横向头覆带、区别于圆棉帽；白袜草履；原创改编|
红地色打挂婚服灵感|red iro-uchikake bridal inspiration|日式灵感：白色小袖与白腰带外穿敞开红色打挂；原创金色鹤与花卉纹；简洁花发饰；白袜草履；原创改编|
金地色打挂婚服灵感|gold iro-uchikake bridal inspiration|日式灵感：白色小袖与白腰带外穿敞开金色打挂；原创松花纹与红色下摆缘；低髻发簪；白袜草履；原创改编|
韩式红地花绣婚礼袍|red-floral hwarot bridal inspiration|韩式婚礼袍灵感：红色宽长袖绣花外袍覆盖高腰长裙；袖口有多色横条；小型花冠和后垂发带；低跟鞋；原创改编|
韩式花冠长裙婚服改编|Korean-inspired floral-crown bridal look|韩式现代灵感：奶白短上衣以宽带在胸前系结；朱红高腰宽长裙；小花冠和长发带；绣花平底鞋；原创婚礼改编|
红金莱亨加婚服灵感|red-gold lehenga bridal inspiration|印度婚礼服装灵感：红金完整覆盖的短袖上衣；同色长伞裙；披巾从头顶一侧垂过肩、脸部敞开；金色小耳饰和鞋；原创改编|
米金莱亨加婚服灵感|ivory-gold lehenga bridal inspiration|印度现代婚礼灵感：米金短袖完整覆盖上衣；金边刺绣长伞裙；轻披巾搭头肩与细腰带；金色小耳坠和鞋；原创改编|
白色新娘西装裤装|white bridal trouser suit|完整白色圆领内搭与白色收腰西装；白色阔腿裤；短头纱与小手包；白色低跟鞋；现代婚礼裤装|minimal
白色披肩领连体婚服|shawl-collar bridal jumpsuit|白色不透明披肩领长袖连体长裤；细缎面腰带；小花发梳短头纱；白色低跟鞋；现代婚礼礼装|minimal
珍珠扣新娘短套裙|pearl-button bridal skirt suit|奶白圆领内搭与珍珠扣短外套；同色及膝A裙；小花帽短面纱；白色低跟鞋；现代登记婚礼穿搭|retro
短披风新娘裤裙装|capelet bridal culotte ensemble|白色圆领上衣与白色短披风；同色宽裙裤、两条裤腿分叉清楚；珍珠发梳与手包；低跟鞋；现代礼装|minimal
香槟色缎面婚礼礼服|champagne satin wedding ensemble|香槟色不透明方领短袖收腰长裙；同色轻披肩；小耳坠与硬壳手包；金色低跟鞋；现代婚礼礼装|retro
雾粉花饰婚礼套装|dusty-pink floral bridal coordinates|雾粉短袖短上衣与同色中长伞裙；腰侧缝接布花；小花发梳与手包；粉色低跟鞋；现代婚礼套装|girly
复古衬衫领新娘套裙|shirt-collar vintage bridal skirt set|奶白小尖领长袖衬衣；同色及小腿伞裙与细腰带；小花帽短面纱；白色玛丽珍鞋；现代复古婚礼套装|retro
长披风新娘直裙装|long-cape bridal column ensemble|白色完整不透明高领长袖直筒长裙；肩部独立及地长披风；珍珠发梳与手包；白色低跟鞋；现代婚礼礼装|minimal
''','文化灵感与现代婚礼礼装',['R75','R77','R78'])

shoulders={'心形领吊带婚纱':'thin_strap','无肩带抹胸婚纱':'strapless','一字肩婚纱':'bardot','单肩垂褶婚纱':'one_shoulder','挂脖婚纱':'halter','分离长袖婚纱':'detached_sleeve'}
for e in CATALOG:
    if e['name'] in shoulders:e['shoulder_type']=shoulders[e['name']]
assert sum(e.get('wedding_reference',False) for e in CATALOG)==80
