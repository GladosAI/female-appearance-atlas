"""Edition 7: early twentieth-century wardrobes and contemporary fashion families."""
from catalog_content import CATALOG, category, add

def block(key, dimension, text, styles=(), refs=(), aliases=()):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e['styles']=list(styles);e['reference_ids']=list(refs);e['aliases']=list(aliases)

def split_styles(styles):
    references={'girly':['R47'],'french_girly':['R47'],'fairy_kei':['R42'],'decora':['R43'],'gyaru':['R44'],'hime_gyaru':['R44'],'visual_kei':['R45'],'grunge':['R46'],'yume_kawaii':['R47'],'yami_kawaii':['R47'],'tenshi':['R48'],'y2k':['R46']}
    for i,e in enumerate(CATALOG[-16:]):
        style=styles[0 if i<8 else 1]
        e['styles']=[style];e['aliases']=[];e['reference_ids']=references[style]

category('early20c_outfits','20世纪初女装（1900–1929）','按1900、1910、1920年代与中国近代分别整理；图例是基于时期轮廓的原创改编，年代与地区以每条说明为准。',['R37','R38','R39','R40','R49','R50','R51'])

block('early20c_outfits','1900–1909年代欧美女装','''
1900年代鸽胸日装|1900s pigeon-breast day ensemble|欧美1900年代：高领布衫胸前松褶、收腰带和贴髋喇叭长裙；侧转展示S形轮廓改编。
1900年代蕾丝两件长裙|1900s lace two-piece dress|欧美约1903年灵感：透明感蕾丝外层配不透明内衬，高领上身与同料落地裙分件连接。
1900年代衬衫腰长裙装|1900s shirtwaist and gored skirt|欧美1900年代：前排扣衬衣、袖口收紧与拼片长裙，腰头清楚，非现代短裙。
1900年代步行短上装套裙|1900s walking jacket suit|欧美1900年代：贴腰翻领短外套配及踝裙，纽扣和纵向裙片可见，利于步行。
1900年代骑行分裙装|1900s cycling divided-skirt ensemble|欧美世纪之交改编：短外套、白衬衣与宽腿分裙，裙裤分叉在站姿中可辨。
1900年代茶会长袍|1900s tea gown|欧美1900年代：松量居家长袍、蕾丝胸覆片和长袖，后部轻拖尾，腰部较柔和。
1900年代白色刺绣夏裙|1900s white embroidered summer dress|欧美1900年代：白色棉布、纵向细褶与刺绣镂空外层，立领和长裙内衬明确。
1900年代水手领日装|1900s sailor-collar day ensemble|欧美1900年代：宽水手领长袖上衣配深色及踝长裙，前胸领巾与裙腰独立。
1900年代低领晚礼服|1900s low-neck evening gown|欧美约1900年：低弧领、短袖与收腰长裙，胸前垂褶和后拖尾，原创宴会款。
1900年代肩覆片舞会裙|1900s shoulder-drape ball gown|欧美1900年代：短肩覆片、贴腰上身与拼片拖尾裙，薄纱和不透明裙层分开。
1900年代晨间包裹袍|1900s morning wrapper|欧美1900年代：宽松前开门襟长袍，细腰带、收口长袖和连贯落地裙摆。
1900年代长外套冬装|1900s long winter-coat ensemble|欧美1900年代：及小腿翻领大衣覆盖长裙，袖肩适度蓬起，帽与手套为辅助。
1900年代短斗篷出行装|1900s capelet travel ensemble|欧美1900年代：短肩斗篷覆盖高领上身，及踝裙与小手提袋形成出行层次。
1900年代蕾丝立领会客裙|1900s lace-collar reception dress|欧美1900年代：高蕾丝领、胸前覆片、肘下收口袖与窄腰拼片长裙。
1900年代吊带裙外穿衬衣装|1900s pinafore over blouse ensemble|欧美1900年代成人款：宽肩带连身长裙外穿高领泡袖衬衣，腰带与裙前片可见。
1900年代末高腰过渡裙|late-1900s raised-waist transition dress|欧美约1909年：腰线抬高、上身松褶减少，细长裙摆配柔软覆层，区别于早期鸽胸。
''',('retro',),('R37','R38','R50'),('爱德华时代','Edwardian','美好年代','Belle Époque','20世纪初','1900年代'))

block('early20c_outfits','1910–1919年代欧美女装','''
1910年代高腰雪纺礼裙|1910s high-waist chiffon evening dress|欧美约1911年：抬高腰线与窄直长裙，雪纺覆层和花卉刺绣局部，区别于1920年代低腰。
1910年代窄摆步行裙|1910s narrow-skirt walking ensemble|欧美1910年代早期：贴体长外套配窄及踝裙，前开衩或裙褶提供步幅。
1910年代灯罩层裙礼服|1910s lampshade-tunic evening dress|欧美1910年代早期灵感：髋部外罩短钟形裙层，下接窄长底裙，两道裙缘明显。
1910年代交叠垂褶长裙|1910s crossover-draped long dress|欧美1910年代早期：V形交叠胸襟、偏高腰和髋侧斜垂褶，长裙内层不透明。
1910年代窄摆束口裙改编|1910s hobble-skirt adaptation|欧美1910年代早期：长裙在小腿处明显收窄，上身长袖；保留结构，作为静态造型参考。
1910年代宽腰带日裙|1910s wide-belt day dress|欧美1910年代：宽腰带与较直长裙、袖肩软褶，裙摆不过分鼓起。
1910年代套装式长外套裙|1910s long-jacket skirt suit|欧美1910年代：盖过髋部的翻领外套、窄长裙和领部小结，纵向比例明确。
1910年代中期钟形日裙|mid-1910s flared day dress|欧美约1915–1916年：裙摆比早期展开，裙长露出靴面，收腰与宽下摆形成对比。
1910年代条纹夏季裙装|1910s striped summer dress|欧美1910年代中期：浅色立式条纹、宽领口覆片和展开的小腿长裙，原创日常款。
1910年代长衬衣束带装|1910s long-blouse belted ensemble|欧美1910年代后期：长衬衣式上身、外束腰带与直裙，门襟和袖口简洁。
1910年代针织开衫套裙|1910s knitted-cardigan skirt ensemble|欧美1910年代后期：宽松长开衫覆盖衬衣，及踝直裙配软帽，针织纹理可辨。
1910年代骑马裤长外套装|1910s riding-breeches outfit|欧美1910年代运动改编：高腰宽髋骑马裤、长翻领外套与长靴，非骑装短裙。
1910年代工作围裙日装|1910s work-apron day ensemble|欧美1910年代：长袖布裙外系胸围式围裙，实用口袋、绑带与小腿长度明确。
1910年代女性工装连体裤|1910s women's work coveralls|欧美1910年代后期工业工作灵感：完整长袖连体裤、束腰和头巾，不使用军事徽记。
1910年代宽领披风冬装|1910s wide-collar cape ensemble|欧美1910年代：宽领长披风、前扣与窄裙相叠，披风开口和内层袖清楚。
1910年代末松腰直裙|late-1910s loose-waist straight dress|欧美约1918–1919年：松量上身、低落软腰带和较直小腿长裙，过渡轮廓非现代迷你裙。
''',('retro',),('R38','R49'),('1910年代','第一次世界大战时期女装','20世纪初'))

block('early20c_outfits','1920–1929年代欧美女装','''
1920年代低腰日常直裙|1920s dropped-waist day dress|欧美1920年代：腰缝落在髋部，直筒上身和膝下裙摆，低腰与自然腰明显区分。
1920年代几何珠绣晚裙|1920s geometric-beaded evening dress|欧美约1923年灵感：直身无袖膝下裙，几何珠绣竖向展开，腰部无现代紧束。
1920年代分层流苏舞裙|1920s tiered-fringe dance dress|欧美1920年代晚装改编：低腰直身裙上有多道流苏，内裙不透明，流苏末端清楚。
1920年代网球百褶裙|1920s pleated tennis dress|欧美约1926年灵感：方领无袖、低腰和活动百褶裙摆，棉麻质感，裙长及膝附近。
1920年代水手领低腰裙|1920s sailor-collar dropped-waist dress|欧美1920年代：水手领覆在直身长袖裙上，髋部腰带和膝下裙摆。
1920年代领结衬衣直裙装|1920s bow-blouse straight-skirt ensemble|欧美1920年代：小领结衬衣、低置裙腰和直裙，腰髋线不紧束。
1920年代毛衣百褶裙装|1920s sweater and pleated-skirt outfit|欧美1920年代休闲改编：长毛衣覆盖低腰百褶裙，袖口与裙褶材质区别明显。
1920年代针织开衫日装|1920s cardigan day ensemble|欧美1920年代：长开衫、简洁内搭与及膝下直裙，方形外轮廓和小圆帽辅助。
1920年代盒形宽领大衣|1920s box-cut wide-collar coat|欧美约1925年灵感：宽直盒形长大衣、大翻领和宽袖，内穿低腰裙。
1920年代毛领披肩晚装|1920s fur-style stole evening ensemble|欧美1920年代：原创仿毛肩披配直身晚裙，肩披与裙身分件，无真实毛皮来源暗示。
1920年代不对称垂片晚裙|1920s asymmetric-panel evening dress|欧美1920年代：髋部缝接垂片与不等长裙缘，直筒上身，侧垂片固定点可辨。
1920年代艺术装饰拼色裙|1920s Art-Deco color-block dress|欧美1920年代：几何拼色面片组织低腰直裙，阶梯纹饰采用原创图形。
1920年代夏季棉麻衬裙装|1920s linen summer frock|欧美1920年代：无袖方领、松身膝下裙、低置腰带与侧袋，清楚棉麻褶皱。
1920年代宽腿海滨便装|1920s wide-leg seaside ensemble|欧美1920年代末休闲改编：宽腿长裤、宽松上衣和外束带，海滨日间层次。
1920年代女式西服裤装|1920s tailored women's trouser ensemble|欧美1920年代个别前卫穿搭灵感：长翻领外套、背心与高腰长裤，非当时通用着装。
1920年代深V覆片晚裙|1920s V-overlay evening dress|欧美1920年代：V形珠饰覆片位于不透明内裙外，低腰、及小腿裙摆与长珠链。
''',('retro',),('R39','R51'),('1920年代','咆哮的二十年代','Roaring Twenties','Art Deco','flapper','20世纪初'))

block('early20c_outfits','1900–1920年代中国近代女装','''
世纪之交立领大襟袄裙|turn-of-century Chinese ao-skirt ensemble|中国约1900年代改编：立领右大襟长袖袄与及踝裙，镶边和裙腰分开，非汉服通用形制。
世纪之交镶边袄裤|turn-of-century Chinese bordered ao-trouser ensemble|中国约1900年代改编：右衽大襟袄、宽裤与袖口多道镶边，衣摆盖髋。
世纪之交长袄百褶裙|turn-of-century Chinese long ao and pleated skirt|中国约1900年代改编：过髋长袄、立领与长百褶裙，前门襟扣结有序。
世纪之交对襟外褂套裙|turn-of-century Chinese front-opening jacket outfit|中国约1900年代改编：对襟短外褂罩在大襟内袄外，下接长裙，内外开口不同。
晚清宽身旗装改编|late-Qing wide-body banner-dress adaptation|中国约1900年代旗装灵感：宽直长袍、立领和装饰滚边，袖和袍身宽松，区别于1930年代贴身旗袍。
晚清马甲罩袍改编|late-Qing vest-over-robe adaptation|中国世纪之交旗装灵感：无袖长马甲罩长袍，双层衣缘、盘扣与直身轮廓可见。
1910年代蓝袄黑裙文明新装|1910s blue ao and black skirt|中国1910–1920年代文明新装灵感：蓝色短袄、宽倒大袖和黑色长裙，成人教师造型。
1910年代白袄长裙文明新装|1910s white ao and long skirt|中国1910–1920年代文明新装改编：白短袄、较合体上身、宽肘下袖口与深色长裙。
1910年代花绸倒大袖袄裙|1910s floral-silk flared-sleeve ensemble|中国近代文明新装馆藏灵感：花绸短袄袖口向外放大，袖长约肘下，黑色及踝裙。
1910年代立领斜襟短袄裙|1910s standing-collar short ao ensemble|中国1910年代原创改编：立领斜襟短袄与长裙，襟缘盘扣和倒大袖层次明确。
1920年代宽直早期旗袍|1920s loose early qipao adaptation|中国1920年代早期旗袍灵感：宽直身、立领、侧襟扣与宽袖，低开衩长袍；非高衩紧身现代款。
1920年代短袖宽身旗袍|1920s short-sleeve loose qipao|中国1920年代改编：短宽袖与直身长袍、低侧开衩，立领和斜襟门襟清楚。
1920年代镶边倒大袖旗袍|1920s flared-sleeve bordered qipao|中国1920年代改编：较宽袖口、宽松袍身和边缘镶饰，避免1930年代贴腰剪裁。
1920年代针织开衫袄裙装|1920s cardigan over ao-skirt ensemble|中国1920年代城市混搭改编：针织开衫外穿短袄长裙，西式外层与中式门襟分辨。
1920年代西式外套长裙装|1920s Chinese urban jacket-skirt adaptation|中国1920年代城市混搭：翻领西式外套配立领内袄及长裙，原创近代角色方案。
1920年代旗袍短外褂套装|1920s qipao with short overjacket|中国1920年代改编：宽直早期旗袍外罩对襟短外褂，短外层与长袍形成比例差。
''',('chinese','retro'),('R40','R27','R29'),('近代女装','民国女装','文明新装','晚清女装','20世纪初','近代旗袍'))

block('fashion_outfits','地雷系完整穿搭','''
地雷系大蝴蝶结衬衫裙装|jirai oversized-bow blouse outfit|黑色荷叶边立领衬衫配粉色领结、收腰短裙与厚底鞋，袖口蕾丝与双侧小蝴蝶结。
地雷系肩窗荷叶边套装|jirai cold-shoulder ruffle ensemble|挖肩衬衫保留肩带，胸前大领结与双层荷叶边短裙，黑粉配色，肩窗轮廓清楚。
地雷系系带连衣裙|jirai lace-up day dress|黑色长袖连衣裙、浅粉胸覆片和前腰交叉系带，裙摆轻展开，无夸张裙撑。
地雷系双色领片裙装|jirai contrast-collar skirt outfit|浅色尖领布衫、黑色胸前缎带与高腰褶裙，领片和腰部装饰扣区别明显。
地雷系针织开衫套裙|jirai cardigan skirt ensemble|短黑开衫、荷叶边内衬衫和粉灰短裙，双排小蝴蝶结与厚底系带鞋。
地雷系连帽拉链裙装|jirai zipped-hoodie skirt outfit|宽松黑色拉链帽衫内搭领结衬衫，窄褶短裙与深色袜，帽衫收口和抽绳可见。
地雷系围兜领短袖裙|jirai bib-collar short-sleeve dress|粉色围兜状胸领片、黑短袖和高腰拼接短裙，胸前垂带与双侧袋盖。
地雷系皮革短外套裙装|jirai cropped-leather jacket outfit|短皮外套覆盖粉黑荷叶边衬衫，A字短裙与厚底鞋，硬外层与软蕾丝内层对比。
地雷系方领细带叠穿裙|jirai square-neck layered pinafore outfit|黑色方领肩带短裙外穿粉灰长袖衬衣，胸带连接清楚，发夹为小型原创心形。
地雷系长袖低褶连衣裙|jirai long-sleeve low-ruffle dress|黑粉撞色长袖裙，胸前领结、腰带和靠近裙底的两道低褶，强调纵向衣身。
地雷系短裤长衬衫套装|jirai shorts and long blouse outfit|长荷叶边衬衫盖住高腰短裤上缘，领结、袖口和裤脚独立，成年休闲变体。
地雷系针织背心衬裙装|jirai knit-vest blouse skirt outfit|黑色短针织背心罩粉色衬衣，领口大蝴蝶结和褶裙，背心下摆与裙腰分开。
地雷系斗篷式短大衣装|jirai cape-shaped short-coat outfit|肩部短斗篷叠在双排扣大衣上，内层领结裙装和不透明袜，前扣与袖开口清楚。
地雷系胸前镂空领结裙|jirai small-keyhole bow dress|领结下方小胸窗配不透明主体，长袖和收腰A字短裙，小开口用于服装结构示意。
地雷系宽袖外套长裙装|jirai wide-sleeve jacket long-skirt outfit|黑色宽袖短外套、粉灰领结衬衫与及小腿褶裙，成年长裙改编，装饰集中上身。
地雷系低饱和格纹裙装|jirai muted-plaid skirt outfit|黑领结与粉灰格纹短裙、荷叶边衬衫和厚底鞋，腰侧垂带与细链集中局部。
''',('jirai',),('R41','R47'),('地雷女装','地雷风','地雷系服装'))

block('fashion_outfits','量产型完整穿搭','''
量产型浅粉领结衬衫裙装|ryousangata pale-pink blouse skirt outfit|奶白衬衫、浅粉蝴蝶结与软褶短裙，蕾丝小领片和低调宝石扣，配玛丽珍鞋。
量产型圆领泡袖连衣裙|ryousangata round-collar puff-sleeve dress|小圆领、短泡袖与粉色收腰短裙，胸前结饰和裙底荷叶边，裙撑量轻。
量产型短开衫肩带裙装|ryousangata cardigan pinafore outfit|浅色短针织开衫罩肩带连衣裙，肩带纽扣、腰缝与领口小蕾丝清楚。
量产型领结针织套裙|ryousangata bow-knit matching skirt set|胸前缎带领结针织上衣配同料短裙，罗纹袖口与裙边细褶，柔和浅色系。
量产型方领长袖裙|ryousangata square-neck long-sleeve dress|方领蕾丝包边、袖肩小褶与前排扣，短A字裙摆，蝴蝶结位于领口而非整身堆积。
量产型浅色双排扣裙装|ryousangata light double-breasted outfit|浅粉双排扣短外套配白色内衫和短裙，翻领、门襟与袖口边线整洁。
量产型碎花小领结裙|ryousangata floral bow dress|细小原创花纹收腰连衣裙，短泡袖、小领结与膝上裙摆，白色袜和圆头鞋。
量产型蕾丝胸覆片裙装|ryousangata lace-yoke skirt outfit|不透明白衬衫上有蕾丝胸覆片，粉灰高腰裙和小型宝石领结扣。
量产型荷叶肩带裙装|ryousangata ruffled-strap pinafore outfit|肩带外缘荷叶边短裙罩白色立领衬衫，背带、腰线和裙身前片形成清楚结构。
量产型小披肩约会裙装|ryousangata capelet day-dress outfit|短针织肩披配浅色收腰裙，前领结固定肩披，衣裙长度及膝附近。
量产型滚边短西服裙装|ryousangata piped short-jacket outfit|奶白短西服与粉色裙，领口缎带、滚边袋盖与装饰扣，成人日常套装。
量产型百褶短裙长衬衫装|ryousangata pleated-skirt blouse outfit|浅色荷叶边衬衫配细百褶短裙，领结垂带、腰侧小饰件与短袜。
量产型宽领冬季大衣装|ryousangata wide-collar winter outfit|浅粉宽领短大衣、内搭蕾丝领裙与不透明袜，衣身前扣和袖绒边可见。
量产型马甲衬衫裙装|ryousangata vest blouse skirt outfit|浅灰粉短马甲罩白色领结衬衫，同色短裙与玛丽珍鞋，前V领和腰线清晰。
量产型双层裙缘连衣裙|ryousangata double-hem dress|奶白上身与浅粉双层裙缘，领口与腰侧两处分布小蝴蝶结，层次轻盈。
量产型珍珠扣针织长裙装|ryousangata pearl-button long-skirt outfit|浅色短开衫配及小腿褶裙，领部小结与原创珠状扣，成人长裙改编。
''',('ryousangata',),('R47',),('量产系','量产型女装','量産型'))

block('fashion_outfits','甜美少女系与法式少女系','''
甜美系圆领针织裙装|girly round-collar knit skirt outfit|成人甜美穿搭：小圆领针织衫、柔软A字裙与小蝴蝶结鞋，装饰密度适中。
甜美系泡袖方领裙|girly square-neck puff-sleeve dress|成人女装：方领、短泡袖与收腰及膝裙，胸前小结和细碎花图案。
甜美系绣花开衫裙装|girly embroidered-cardigan outfit|成人女装：短开衫有局部花绣，内搭小领衫与及膝软褶裙。
甜美系荷叶边背带裙|girly ruffled pinafore outfit|成人女装：宽肩带裙外穿短泡袖衬衫，肩带荷叶边、裙前口袋和腰结清楚。
甜美系细格纹领结套裙|girly gingham bow skirt ensemble|成人女装：细格纹衬衫、纯色半裙和领口小结，格纹位置与腰带分开。
甜美系水手领针织装|girly sailor-collar knit outfit|成人日常：软针织水手领、领结与膝上褶裙，宽领片与针织身分辨。
甜美系花瓣领长裙|girly petal-collar long dress|成人女装：花瓣形圆领、束腰长袖与及小腿裙，花瓣领是服装领型。
甜美系围裹结饰裙装|girly wrap-bow dress|成人女装：交叠包裹前襟、腰侧小蝴蝶结与柔软过膝裙摆，接缝清楚。
法式少女系贝雷帽短裙装|French-girly beret skirt ensemble|成人风格改编：贝雷帽、针织上衣与高腰短裙，黑白奶油色组合和圆头鞋。
法式少女系滚边短外套|French-girly piped cropped-jacket outfit|成人女装：短箱形滚边外套、简单内搭与A字裙，小领结和纽扣整洁。
法式少女系条纹针织裙装|French-girly striped-knit ensemble|成人女装：横条纹针织衫配高腰短裙与玛丽珍鞋，袖口和裙腰线明确。
法式少女系细领结衬裙|French-girly narrow-bow blouse dress|成人女装：细领结衬衫、肩带短裙与小圆帽，细带和大领结地雷系区分。
法式少女系黑白格纹套裙|French-girly black-white check set|成人女装：小格纹短上衣配同料裙，黑色领边与袖口，形体简洁。
法式少女系细肩带叠衫装|French-girly camisole-over-blouse outfit|成人女装：缎面细带背心罩薄长袖衬衣，直裙和小包，三层领缘可见。
法式少女系短风衣裙装|French-girly short-trench skirt outfit|成人女装：浅色短风衣、针织内搭和膝上裙，腰带与袖袢为主要结构。
法式少女系蕾丝领长裙|French-girly lace-collar midi dress|成人女装：深色简洁及小腿裙、白色小蕾丝领与细腰带，发带和鞋保持轻量。
''',(),('R47',),('girly','少女系穿搭','成人甜美穿搭'))
split_styles(('girly','french_girly'))

block('fashion_outfits','妖精系与缀饰系','''
妖精系粉彩卫衣纱裙装|fairy-kei pastel sweatshirt tulle outfit|成人穿搭：粉彩宽卫衣、短层纱裙和条纹袜，原创星形图案与轻量塑料首饰。
妖精系云纹针织短裤装|fairy-kei cloud-knit shorts outfit|成人穿搭：软色云纹针织衫、高腰泡泡短裤与长袜，图案为原创抽象云朵。
妖精系复古运动夹克装|fairy-kei pastel retro-sport outfit|成人穿搭：粉彩拼色运动夹克、软裙和厚底运动鞋，袖线和拉链可见。
妖精系背带灯芯绒裙|fairy-kei corduroy pinafore outfit|成人穿搭：浅色灯芯绒背带裙、宽袖衬衫与星形小包，绒条方向明确。
妖精系虹色条纹针织装|fairy-kei rainbow-stripe knit outfit|成人穿搭：低饱和虹色条纹毛衣、纱裙和宽松袜，饰件集中手腕及发夹。
妖精系玩具感图案长裙|fairy-kei toy-motif long dress|成人女装：原创积木与星球印花松身长裙，粉彩开衫和软帽，无品牌玩偶图案。
妖精系大领片宽裤装|fairy-kei oversized-collar trouser outfit|成人穿搭：大圆领软衫、浅色宽裤与平台鞋，粉彩层次不依赖夸张蓬裙。
妖精系短斗篷层裙装|fairy-kei pastel capelet outfit|成人穿搭：浅紫短斗篷、星形扣与双色层裙，软织物、条纹袜和小夹饰。
缀饰系发夹密集街头装|decora abundant-hairclip street outfit|成人穿搭：彩色发夹成片、宽图案T恤与层裙，手腕彩珠和多条小项链。
缀饰系彩条纹叠穿装|decora layered-stripe outfit|成人穿搭：短袖图案衫罩长袖条纹内衫，短裙叠长袜，多色饰件沿头胸腕分布。
缀饰系牛仔短裤工具装|decora decorated-denim shorts outfit|成人穿搭：宽背心罩彩条纹内搭，牛仔短裤、可拆挂件和发夹，挂件根部可见。
缀饰系亮色雨衣装|decora bright-raincoat outfit|成人穿搭：透明感亮色雨衣罩不透明彩衫与裙，外夹饰和多彩腕链形成密集点。
缀饰系多袋吊带裙装|decora pocket-pinafore outfit|成人穿搭：鲜色吊带裙、圆领衫和多口袋挂件，发夹、袖套与珠链分区。
缀饰系不对称袜套装|decora asymmetric-legwarmer outfit|成人穿搭：彩色宽上衣与短裙，两腿不同色袜套，多层链和发夹，保持正常人体结构。
缀饰系暗色霓虹叠层装|dark-decora neon-layer outfit|成人穿搭：黑色基础上有亮色条纹袖与彩饰，深浅层裙、腕链和多枚发夹。
缀饰系手作贴布宽裤装|decora handmade-patchwork trouser outfit|成人穿搭：原创贴布宽衫、拼接宽裤和密集小挂饰，缝线与饰物固定点明确。
''',(),('R42','R43'),('原宿风','Harajuku','日系街头'))
split_styles(('fairy_kei','decora'))

block('fashion_outfits','辣妹系与姬辣妹系','''
辣妹系豹纹牛仔裙装|gyaru leopard-denim skirt outfit|成人穿搭：豹纹贴身上衣、牛仔短裙和厚底鞋，蓬松卷发与原创长甲辅助。
辣妹系短夹克喇叭裤装|gyaru cropped-jacket flare-trouser outfit|成人穿搭：短夹克、宽腰带与喇叭牛仔长裤，金属饰件集中腰部。
辣妹系针织露肩裙装|gyaru off-shoulder knit outfit|成人穿搭：一字肩针织衫、短裙和长靴，领缘完整绕过双臂，肩部开口清楚。
辣妹系西服马甲短裤装|gyaru tailored-vest shorts outfit|成人穿搭：贴腰翻领马甲、短裤与厚底凉鞋，腰带和装饰链构造可见。
辣妹系白衬衫牛仔装|gyaru blouse-denim casual outfit|成人穿搭：开领白衬衫配高腰短牛仔裙，大耳环与高体积卷发，成年休闲方案。
辣妹系仿毛边皮外套装|gyaru fur-trim leather outfit|成人穿搭：仿毛领短皮外套、短裙与长靴，硬皮革和软毛边材质对比。
辣妹系斜肩包裹长裙|gyaru asymmetric-wrap maxi dress|成人穿搭：斜肩包裹式及踝长裙、腰侧结和厚底鞋，成熟长裙变体。
辣妹系图案长衫紧身裤装|gyaru graphic-tunic legging outfit|成人穿搭：长图案上衣、窄长裤和平台鞋，亮色腰带、腕饰和卷发形成重点。
姬辣妹系玫瑰结饰短裙|hime-gyaru rose-bow short dress|成人姬辣妹改编：贴腰短裙、蕾丝裙缘、原创玫瑰结饰和高体积卷发，无重型洛丽塔裙撑。
姬辣妹系绒边短外套装|hime-gyaru plush-trim jacket outfit|成人穿搭：软绒边短外套、收腰短裙与花形发饰，装饰分布在领口和裙缘。
姬辣妹系心形领连衣裙|hime-gyaru sweetheart-neck dress|成人穿搭：心形领不透明连衣裙、短泡袖、玫瑰腰饰和蕾丝短袜。
姬辣妹系蕾丝背心叠裙装|hime-gyaru lace-vest skirt outfit|成人穿搭：蕾丝边贴腰背心罩圆领衬衫，褶边短裙与大卷发，衣身线条可见。
姬辣妹系长开衫短裙装|hime-gyaru long-cardigan skirt outfit|成人穿搭：柔软长开衫、贴腰连衣短裙与花朵发带，长外层与短内层对比。
姬辣妹系花纹雪纺长裙|hime-gyaru floral-chiffon maxi dress|成人穿搭：玫瑰原创印花长裙、柔软垂肩领片和蝴蝶结腰带，内衬不透明。
姬辣妹系荷叶边短裤装|hime-gyaru ruffled-shorts outfit|成人穿搭：贴腰荷叶边上衣与蕾丝缘短裤，玫瑰发饰、软袜和厚底鞋。
姬辣妹系花结针织套裙|hime-gyaru flower-bow knit set|成人穿搭：短针织上衣配同料A字短裙，领部花结、原创新月珠饰与蓬卷发。
''',(),('R44',),('ギャル','姫ギャル','日系辣妹'))
split_styles(('gyaru','hime_gyaru'))

block('fashion_outfits','视觉系与Grunge做旧穿搭','''
视觉系不对称长外套装|visual-kei asymmetric long-coat outfit|成人女性：不对称长外套、窄裤与靴，深色发束、舞台感妆容和原创扣带。
视觉系荷叶边衬衫马甲装|visual-kei ruffled-blouse vest outfit|成人女性：荷叶领衬衫、贴腰马甲与窄长裤，胸前细链和高体积发型。
视觉系带扣拼层裙装|visual-kei buckle-layer skirt outfit|成人女性：短夹克、带扣腰封与不等长层裙，金属件和片裙固定关系明确。
视觉系长披挂短裤装|visual-kei long-drape shorts outfit|成人女性：长垂挂背心外层、深色内衫和短裤，长靴与单侧腰链。
视觉系深红翻领礼服装|visual-kei crimson tailored outfit|成人女性：深红长翻领外套、黑衬衫和长裤，舞台领饰与袖口滚边，原创造型。
视觉系宽袖和风混搭|visual-kei Japanese-inspired wide-sleeve outfit|成人女性：原创宽袖交叠短外层、带扣腰带与窄裤，日式灵感舞台混搭，不当作传统服制。
视觉系网纹叠袖裙装|visual-kei mesh-layered skirt outfit|成人女性：网纹外袖罩不透明长袖上衣，拉链短裙、宽腰带和靴，面料层次可见。
视觉系长短燕尾裙装|visual-kei high-low tailcoat outfit|成人女性：前短后长燕尾外套、领结衬衣与层裙，侧面展示燕尾长度，原创舞台款。
Grunge格衬针织长裙装|grunge plaid-cardigan slip outfit|成人穿搭：松量格纹衬衣、做旧针织外层与不透明长裙，配旧感系带靴。
Grunge宽T恤破边牛仔装|grunge oversized-tee denim outfit|成人穿搭：宽T恤、毛边牛仔长裤与厚底靴，磨损沿衣缘，不画身体损伤。
Grunge条纹毛衣层裙装|grunge stripe-knit layered-skirt outfit|成人穿搭：宽条纹毛衣、长短两层裙与软袜，颜色低饱和、边缘轻磨损。
Grunge工装外套背心装|grunge work-jacket vest outfit|成人穿搭：旧感工装外套、针织背心和宽长裤，肘部补片和口袋接缝清楚。
Grunge格纹腰系裙装|grunge waist-tied plaid outfit|成人穿搭：宽T恤配短裙，格衬系在腰外，结和垂袖、靴筒可见。
Grunge长风衣牛仔装|grunge oversized-coat denim outfit|成人穿搭：宽松旧感长外套、简单衬衣和牛仔裤，面料褶皱与轻度磨边。
Grunge针织帽罩衫装|grunge beanie tunic outfit|成人穿搭：针织帽、松肩长罩衫与窄裤，罩衫有可控旧感纹理和不等长下摆。
Grunge拼布衬衣宽裤装|grunge patchwork-shirt wide-trouser outfit|成人穿搭：不同格纹拼布衬衣、宽裤和旧感运动鞋，修补缝线成为装饰。
''',(),('R45','R46'),('视觉摇滚','ヴィジュアル系','做旧风'))
split_styles(('visual_kei','grunge'))

block('fashion_outfits','梦かわ与病かわ图案穿搭','''
梦かわ云星卫衣裙装|yume-kawaii cloud-star sweatshirt outfit|成人穿搭：粉紫蓝卫衣、柔软短裙和长袜，原创梦幻云星图案与轻量小包。
梦かわ薄纱外罩长裙|yume-kawaii tulle-overlay long dress|成人女装：不透明长裙外罩粉彩薄纱，星形扣与软肩披，层纱缘清楚。
梦かわ月亮领结裙装|yume-kawaii moon-bow dress|成人女装：大圆领、月亮原创饰件与柔软收腰裙，渐变仅在布料印花中出现。
梦かわ毛绒短外套装|yume-kawaii plush cropped-jacket outfit|成人穿搭：粉彩仿毛短外套、云纹内衫与软褶裙，圆形包和平台鞋。
梦かわ渐变针织宽裤装|yume-kawaii gradient-knit trouser outfit|成人穿搭：柔和渐变宽毛衣配浅色长裤，小星饰和鞋带，区别于蓬裙型。
梦かわ星点背带裙|yume-kawaii star-dot pinafore outfit|成人女装：原创星点肩带长裙罩宽袖衬衣，肩带连接、裙腰和小结饰明确。
梦かわ软色运动套装|yume-kawaii pastel sports-inspired set|成人穿搭：粉彩拼片运动外套与宽短裤、不透明长袜，星形拉链头和侧条。
梦かわ云边领长衬裙|yume-kawaii scalloped-collar dress|成人女装：云边圆领、宽长袖与及膝裙摆，软色原创图案和蝴蝶结腰带。
病かわ裂心图案卫衣装|yami-kawaii cracked-heart hoodie outfit|成人穿搭：粉黑宽卫衣与短裙，抽象裂心印花和条纹袜，仅为服装图案。
病かわ黑粉双色层裙|yami-kawaii black-pink layered-skirt outfit|成人穿搭：双色衬衫、软层裙与交叉缎带装饰，领口小结和原创符号。
病かわ不对称蝴蝶结裙|yami-kawaii asymmetric-bow dress|成人女装：深浅粉拼片短裙、左右不对称结饰和宽袖，拼线强调设计。
病かわ线条心形针织装|yami-kawaii outlined-heart knit outfit|成人穿搭：浅色宽毛衣有深色线条心形，黑直裙和厚底鞋，原创装饰图形。
病かわ交叉缎带长外套|yami-kawaii ribbon-laced coat outfit|成人穿搭：粉灰长外套、黑色交叉缎带和内搭裙，带从金属孔穿过，作为服装系带。
病かわ双色条纹罩衫装|yami-kawaii split-stripe tunic outfit|成人穿搭：左右双色条纹长罩衫、黑短裤与不透明袜，装饰缝线和星形挂件。
病かわ包裹袖短裙套装|yami-kawaii wrap-sleeve skirt outfit|成人穿搭：布条式装饰袖罩不透明袖身，宽领上衣与短裙，布条为缝接服装结构。
病かわ心锁图案长裙|yami-kawaii heart-lock long dress|成人女装：黑粉心锁原创印花及小腿裙，短开衫和小结饰，印花与真实扣具分开。
''',(),('R47',),('梦可爱','病可爱','ゆめかわいい','やみかわいい'))
split_styles(('yume_kawaii','yami_kawaii'))

block('fashion_outfits','天使系与Y2K穿搭','''
天使系白蓝运动夹克装|tenshi-kaiwai white-blue track outfit|成人穿搭：白色运动夹克、淡水蓝短裙与平台运动鞋，袖条和拉链；天使系为穿搭标签。
天使系宽袖连帽裙装|tenshi-kaiwai wide-sleeve hoodie outfit|成人穿搭：白蓝宽袖帽衫、直短裙和不透明长袜，袖带为装饰固定件。
天使系白色工装长裤装|tenshi-kaiwai white cargo-trouser outfit|成人穿搭：淡蓝短夹克、白宽腿工具袋长裤与白鞋，袋盖、扣带和色块清楚。
天使系水蓝肩带裙装|tenshi-kaiwai pale-blue pinafore outfit|成人女装：淡水蓝肩带短裙罩白色长袖内搭，双肩扣带和裙腰，现代轻机能方向。
天使系拉链罩衫短裤装|tenshi-kaiwai zipped-tunic shorts outfit|成人穿搭：白色长拉链罩衫与蓝色短裤，侧开口、袖口和不透明长袜。
天使系反光滚边长裙装|tenshi-kaiwai reflective-trim skirt outfit|成人穿搭：白色短外套、浅蓝及小腿直裙，银灰滚边与扣带，服装不带真实翅膀。
天使系白蓝针织套装|tenshi-kaiwai white-blue knit set|成人穿搭：水蓝圆领宽针织衫与白色软裙，白蓝鞋袜和细银色包扣。
天使系半拉链立领装|tenshi-kaiwai half-zip stand-collar outfit|成人穿搭：白蓝半拉链立领上衣、工装短裙和运动鞋，领口开合与拼片可见。
Y2K短上衣喇叭牛仔装|Y2K cropped-top flared-denim outfit|成人复古改编：短上衣、喇叭牛仔长裤和宽腰带，银色腰饰与小肩包。
Y2K亮面短夹克裙装|Y2K glossy cropped-jacket outfit|成人穿搭：亮面短夹克、简单内衫与迷你裙，金属拉链与平台鞋形成千禧风灵感。
Y2K挂脖针织长裤装|Y2K halter-knit trouser outfit|成人穿搭：不透明挂脖针织上衣、低置腰带宽裤和腋下包，肩带绕颈连接可见。
Y2K运动外套短裙装|Y2K track-jacket mini-skirt outfit|成人穿搭：拼色运动外套、短裙与厚底鞋，装饰条、拉链和小包，原创无品牌。
Y2K牛仔连衣短裙|Y2K denim mini-dress|成人女装：贴身牛仔连衣短裙、前拉链和装饰腰带，明线、袋盖与厚底凉鞋。
Y2K网层短袖叠穿装|Y2K mesh-layered tee outfit|成人穿搭：网纹短袖罩不透明小上衣，工装长裤和亮色肩包，双层领口明确。
Y2K金属色背心宽裤装|Y2K metallic-vest wide-trouser outfit|成人穿搭：金属色短背心、宽腿长裤和平台鞋，材质反光集中上身。
Y2K粉色绒面运动套装|Y2K pink velour tracksuit|成人穿搭：绒面拉链外套和微喇长裤，贴袋、袖口和裤腰清楚，原创无品牌文字。
''',(),('R48','R46'),('千禧风','天使界隈','白蓝系'))
split_styles(('tenshi','y2k'))
