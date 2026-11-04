"""Edition 18: original trend, fashion and model presentation ensembles."""
from catalog_content import CATALOG, category, add

NEW_CATEGORIES=['trend_outfits','chic_outfits','model_outfits']
category('trend_outfits','潮流穿搭','以街头、工装、运动混搭和潮流配件组织原创穿搭；重点观察廓形、长短层次与鞋包呼应。名称是创作检索方向，不表示当季流行排名。',['R06','R73'])
category('chic_outfits','时尚穿搭','以都市剪裁、色彩组织、材质对比与设计感套装比较时尚造型；衣物、鞋履和配饰共同构成完整方案。',['R06','R73'])
category('model_outfits','模特穿搭','按秀场与型录、编辑拍摄与模特场外造型区分展示语境；服装和展示方式是创作参考，不设置统一体型或身高标准。',['R73','R74'])

def block(key,dimension,text):
    rows=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(rows)==16,(key,dimension,len(rows))
    for name,en,recipe,styles in rows:
        add(key,dimension,f'{name}|{en}|{recipe}。原创成年女性整套搭配，比较衣物层次与鞋包配饰。')
        CATALOG[-1].update(added_in='18.0',trend_model_reference=True,age_context='成年女性服装与展示参考',outfit_components=recipe.split('；'),styles=styles.split(',') if styles else [],aliases=['潮流时尚模特专题',{'trend_outfits':'潮流穿搭','chic_outfits':'时尚穿搭','model_outfits':'模特穿搭'}[key],dimension])
        if name=='时尚一字肩收腰中裙':CATALOG[-1]['shoulder_type']='bardot'
        if name=='时尚单肩垂褶长裙':CATALOG[-1]['shoulder_type']='one_shoulder'

block('trend_outfits','街头廓形与运动混搭','''
潮流箱形夹克宽牛仔装|boxy jacket wide-denim street ensemble|灰白圆领T恤与短箱形靛蓝夹克；水洗宽腿牛仔裤；厚底运动鞋；银灰腋下包|streetwear
潮流棒球衫褶裙混搭|baseball overshirt pleated-skirt mix|无字宽棒球衫叠白棉内搭；炭灰膝下百褶裙；运动鞋配短袜；小斜挎包|streetwear,preppy
潮流橄榄工裤短外套|olive cargo cropped-jacket outfit|奶白高领内搭与黑色短飞行夹克；橄榄绿宽工装裤；黑色系带鞋；尼龙肩包|streetwear,techwear
潮流拼色拉链运动裙装|color-panel track-jacket skirt ensemble|蓝白拼色拉链运动夹克；深灰直筒及膝裙；白色运动鞋；弧形挎包|streetwear
潮流宽卫衣长衬衫层叠|oversized sweatshirt long-shirt layers|紫灰宽卫衣露出浅蓝长衬衫下摆；黑色直腿裤；帆布鞋；宽带邮差包|streetwear
潮流尼龙马甲宽裤装|nylon utility-vest wide-trouser look|条纹长袖衫叠灰色尼龙多袋马甲；黑色宽直裤；越野运动鞋；腰侧小袋|techwear
潮流短针织伞裙运动装|cropped knit flared-skirt sneaker mix|鹅黄及腰针织开衫配白色圆领内搭；深蓝中长伞裙；绿色运动鞋；小帆布包|streetwear,girly
潮流牛仔叠牛仔装|layered denim-on-denim street outfit|白T恤与浅蓝敞襟牛仔衬衣；深蓝高腰宽牛仔裤；棕色厚底鞋；浅色肩袋|streetwear
潮流赛车领夹克长裙|racing-collar jacket maxi-skirt look|无标志红灰拼色立领夹克；黑色前开衩及踝长裙；厚底短靴；小尼龙包|streetwear
潮流运动Polo工装裙|sport polo cargo-skirt outfit|奶白撞色领运动Polo；卡其膝下工装半裙；白色短袜运动鞋；半月斜挎包|streetwear,preppy
潮流连帽马甲直裤装|hooded vest straight-trouser outfit|浅灰长袖卫衣叠短黑色连帽马甲；灰白直筒长裤；黑白运动鞋；宽带背包|techwear
潮流宽肩衬衫五分裤|broad-shoulder shirt long-shorts look|蓝色宽肩衬衫叠白色圆领背心；炭灰及膝宽短裤；厚底乐福鞋；托特包|streetwear,minimal
潮流泡泡裙飞行夹克|bubble-hem skirt bomber ensemble|白色圆领针织与绿色短飞行夹克；黑色及膝泡泡半裙；运动鞋；小方包|streetwear
潮流宽松针织球鞋装|relaxed knit sneaker street look|藏蓝宽松V领针织叠浅色衬衣；灰色宽直裤；银白运动鞋；软皮肩包|streetwear,preppy
潮流背带工裤短衬衫|dungarees short-overshirt outfit|完整白色T恤与黑色宽背带工裤；米色短衬衫敞开叠穿；厚底帆布鞋；帆布腰袋|streetwear
潮流运动衫绸裙混搭|track pullover satin-skirt contrast|深绿色半拉链运动衫；银灰不透明缎面中长裙；灰白运动鞋；窄腋下包|streetwear,minimal
''')
block('trend_outfits','机能配件与复古街拍','''
潮流银灰壳衣束脚裤|silver-grey shell jogger ensemble|银灰短壳外套配黑色高领内搭；炭灰束脚裤；灰色越野鞋；扣带斜挎包|techwear
潮流多袋风衣裙裤装|multi-pocket trench culotte look|米灰多袋短风衣叠白衬衣；卡其宽裙裤；系带短靴；结构腰包|techwear
潮流绗缝马甲灯芯绒|quilted vest corduroy street outfit|条纹针织叠橄榄绗缝马甲；棕色灯芯绒直裤；麂皮系带鞋；帆布肩包|retro,streetwear
潮流做旧格衬补片牛仔|faded plaid patchwork denim look|灰色完整棉T恤与做旧格纹衬衣；补片宽牛仔裤；厚底帆布鞋；旧感邮差包|grunge
潮流千禧短夹克喇叭裤|millennium jacket flared-trouser look|淡蓝及腰拉链短夹克与完整白内搭；高腰微喇牛仔裤；厚底鞋；银色小肩包|y2k
潮流长针织背心衬衣|long sweater-vest shirting ensemble|白色长袖衬衣叠深绿长针织背心；灰色直筒裤；厚底乐福鞋；窄带挎包|preppy,streetwear
潮流短皮衣工装长裙|cropped leather cargo-maxi outfit|米白高领内搭与棕色短皮外套；卡其多袋长裙；黑色短靴；硬边小肩包|streetwear
潮流拼接羽绒马甲装|panelled puffer-vest outfit|奶白连帽卫衣叠蓝灰拼接羽绒马甲；宽工装裤；厚底运动鞋；抽绳背包|techwear
潮流宽条纹针织套装|wide-stripe knit street coordinates|蓝白宽条纹针织上衣；深蓝软垂针织宽裤；白运动鞋；柠黄斜挎包|streetwear
潮流雨壳叠短裤袜装|rain-shell long-shorts layered look|浅灰透明感外壳有完整不透明内搭；黑色及膝短裤；不透明运动长袜和短靴；防雨包|techwear
潮流工装连体裤围巾|utility jumpsuit scarf styling|深蓝宽松长袖工装连体裤；橙色短围巾系颈侧；厚底系带鞋；小帆布挎包|streetwear
潮流双层衬衣直裙装|double-shirt straight-skirt street look|浅蓝长衬衣外叠短白衬衣；黑色中长直裙；厚底便鞋；灰色斜挎袋|streetwear,minimal
潮流针织帽皮衣牛仔|beanie leather denim outfit|深灰圆领针织与黑色宽皮夹克；水洗蓝宽牛仔裤；系带靴；针织帽和肩包|grunge
潮流撞色绳扣外套|contrast drawcord shell outfit|水蓝立领壳外套带橘色抽绳扣；深灰锥形长裤；拼色运动鞋；小尼龙背包|techwear
潮流毛绒背心运动裙|fleece vest sport-skirt mix|米色抓绒背心叠深色长袖运动衫；藏蓝膝下直裙；白色运动鞋；软肩袋|streetwear
潮流反差色长外套装|contrast-colour long-coat street look|紫灰长大衣叠奶白针织；黑色宽直裤；鲜绿运动鞋；窄黑色腰包|streetwear,minimal
''')

block('chic_outfits','都市剪裁与质感配色','''
时尚宽肩西装长裙|broad-shoulder blazer maxi look|奶白衬衣与灰褐宽肩西装；同色及踝直裙；尖头低跟鞋；深棕结构手袋|minimal
时尚短西装高腰阔裤|cropped blazer high-waist trousers|黑色圆领内搭与奶油短西装；同色高腰阔腿裤；黑色低跟鞋；弧形肩包|minimal
时尚无领呢外套直裙|collarless wool jacket pencil-midi|奶白薄针织与浅灰无领呢夹克；炭灰及膝直裙；银色平底鞋；小硬壳包|french_girly
时尚酒红针织驼色裤|burgundy knit camel trousers|酒红半高领细针织；驼色宽褶长裤；深棕乐福鞋；同色细腰带与手袋|retro
时尚浅蓝衬衫白长裙|pale-blue shirt white maxi|浅蓝硬挺衬衫卷袖；不透明白色A字长裙；红棕细带鞋；棕色软手提包|minimal
时尚全灰材质叠穿|tonal grey mixed-texture ensemble|浅灰细针织与深灰短毛呢马甲；灰缎面中长裙；深灰低跟靴；小灰包|minimal
时尚海军蓝白裤装|navy knit white-trouser look|藏蓝短开衫配完整白色内搭；白色宽直长裤；深蓝便鞋；编织手提包|minimal
时尚棕皮衣褶长裙|brown leather pleated-maxi look|奶白领口针织与棕色短皮衣；浅咖细褶长裙；黑色踝靴；宽带小肩包|retro
时尚条纹衬衣丝巾装|striped shirt neck-scarf styling|蓝白细条纹衬衣配小几何丝巾；炭灰直筒裤；酒红乐福鞋；方形手袋|british
时尚奶油针织套裙|cream knit skirt coordinates|奶油色细针短上衣与同色中长针织裙；棕色低跟鞋；浅金耳圈和小肩包|minimal
时尚长马甲阔裤套装|long waistcoat wide-trouser suit|白色圆领衬衣叠黑色长西装马甲；黑色阔腿裤；方头皮鞋；几何手提包|minimal
时尚滚边短外套牛仔|piped cropped jacket denim styling|白棉内搭与黑白滚边短外套；深蓝直筒牛仔裤；玛丽珍平底鞋；小翻盖包|french_girly
时尚橄榄绿衬衫裙|olive belted shirtdress look|橄榄绿不透明及小腿衬衫连裙；宽棕腰带；棕色短靴；奶油色手袋|minimal
时尚针织披肩直裙|knit shoulder-wrap straight-skirt look|奶白高领针织配灰褐针织披肩；炭灰中长直裙；尖头低跟鞋；深棕肩包|minimal
时尚黑白箱形套裙|black-white box-jacket skirt suit|白色圆领内搭与黑色箱形短西装；白色及膝A裙；黑色便鞋；黑白小包|minimal
时尚雾粉西装灰裤|dusty-pink blazer grey trousers|奶白衬衣与雾粉轻西装；灰色高腰褶裤；银灰低跟鞋；灰白手提包|girly,minimal
''')
block('chic_outfits','设计感廓形与场合造型','''
时尚斜门襟西装套裙|asymmetric-front blazer skirt suit|奶白内搭与黑色斜门襟西装；同色直筒长裙；尖头鞋；小金属扣手包|minimal
时尚披肩领连体裤|shawl-collar tailored jumpsuit|深蓝不透明披肩领长袖连体长裤；细腰带；银灰低跟鞋；几何耳饰与手包|minimal
时尚一字肩收腰中裙|off-shoulder belted midi look|奶油色一字肩中袖收腰连裙；棕色细腰带；低跟凉鞋；圆弧小手袋|retro
时尚单肩垂褶长裙|one-shoulder draped evening dress|酒红不透明单肩垂褶及踝长裙；小耳坠；黑色细带鞋；素色手包|retro
时尚斗篷肩短西装|cape-shoulder cropped tailoring|奶白短西装带连贯斗篷肩覆片；黑色高腰宽裤；低跟皮鞋；方形手包|minimal
时尚建筑感折片裙|architectural folded-panel skirt look|黑色简洁长袖上衣；蓝灰硬挺折片中长裙；黑色低跟靴；几何小包|minimal
时尚宽袖收腰衬衣装|sculptural sleeve belted-shirt outfit|白色宽袖高领衬衣配宽黑腰带；炭灰阔腿裤；黑色尖头鞋；结构手袋|minimal
时尚银灰缎面套装|silver-grey satin tailored coordinates|银灰不透明垂领上衣与同色长袖轻外套；银灰宽裤；黑色低跟鞋；哑光手包|minimal
时尚短风衣伞长裙|cropped trench full-maxi styling|奶白内搭与米色短风衣；黑色中长伞裙；红棕平底鞋；棕色手提包|retro
时尚花卉提花礼装|floral jacquard formal coordinates|深蓝高领短袖提花上衣；同花卉织纹及膝A裙；深蓝低跟鞋；素色小包|retro
时尚长围巾西装裙|long-scarf blazer-dress styling|炭灰长袖及膝西装连裙；奶白长围巾绕颈垂至裙摆；黑色长靴；小手包|minimal
时尚弧形下摆两件裙|curved-hem two-piece midi ensemble|奶油色弧形下摆长袖短上衣；同色直筒中长裙；酒红低跟鞋；小硬壳包|minimal
时尚格纹短上装伞裙|checked cropped-jacket full-skirt suit|蓝灰小格纹短夹克；同料中长伞裙；黑色玛丽珍鞋；深蓝手袋|british,retro
时尚围裹长衣裤装|long wrap-top trouser ensemble|奶白不透明长袖围裹上衣；黑色窄直长裤；方头低跟鞋；银灰小手包|minimal
时尚风琴褶色块长裙|colour-block accordion-maxi outfit|黑色短针织上衣；深蓝与橘色拼块风琴褶长裙；黑色短靴；纯黑肩包|minimal
时尚珠饰领口宴会裙|beaded-collar evening-midi look|墨绿不透明长袖中长连裙；领缘少量原创珠饰；细带低跟鞋；黑色手拿包|retro
''')

block('model_outfits','秀场与型录展示','''
模特秀场雕塑感大衣|runway sculptural overcoat ensemble|奶白高领内搭与钴蓝夸张弧肩长大衣；黑色直裤；黑色短靴；手持小几何包；自然直立展示|特制
模特秀场立体折片裙|runway sculpted folded-skirt look|白色简洁长袖上装；黑色硬挺立体折片中长裙；黑色低跟鞋；小银色耳饰；轻微侧转展示折片|特制
模特秀场单色长套装|runway monochrome elongated suit|灰褐长西装与同色圆领内搭；高腰及地阔腿裤露出鞋尖；棕色皮鞋；窄带手包；平稳步态|特制
模特秀场缎面披覆裙|runway satin cape-drape dress|酒红不透明长袖缎面及踝裙；连领披覆片垂至侧腰；细带低跟鞋；小耳坠；站姿展示垂褶|特制
模特秀场宽肩窄腰套裙|runway broad-shoulder cinched-waist suit|炭灰宽肩收腰西装；黑色中长直裙；尖头低跟鞋；小手包；双臂自然分开不遮腰线|特制
模特秀场拼色几何裙|runway geometric colour-block dress|奶油与钴蓝拼色高领中长连裙；结构性几何裙片；白色低跟鞋；简洁耳环；正面展示|特制
模特秀场立领长马甲|runway high-collar long-vest ensemble|白色衬衣与黑色立领及膝长马甲；灰色阔裤；黑色皮鞋；窄手包；完整层次展示|特制
模特秀场泡泡袖长裙|runway puff-sleeve column gown|墨绿不透明泡泡长袖及踝直裙；收腰结构；低跟细带鞋；小耳钉；自然站姿|特制
模特型录正面西装装|lookbook front-view tailoring|白圆领内搭与奶油单排扣西装；同色直筒长裤；棕色便鞋；方形手袋；双脚自然分开正面站立|minimal
模特型录侧转针织裙|lookbook three-quarter knit dress|深灰高领长袖针织中长裙；细腰带；黑色踝靴；短带肩包；四分之三侧转留出腰侧轮廓|minimal
模特型录长衬衣裤装|lookbook long-shirt trouser outfit|浅蓝长衬衣叠奶白短针织马甲；黑色宽直裤；白色帆布鞋；帆布托特包；直立展示叠穿|minimal
模特型录风衣开合装|lookbook open-front trench outfit|米色开襟长风衣露出白衬衣与灰色直筒裤；棕色低跟鞋；小肩包；一手自然轻触衣襟|british
模特型录短夹克半裙|lookbook cropped jacket midi ensemble|黑色圆领内搭与灰白短呢夹克；炭灰膝下A裙；玛丽珍鞋；小手袋；简洁站姿|french_girly
模特型录工装连体裤|lookbook utility jumpsuit|藏蓝不透明长袖宽工装连体裤；同料腰带；白色厚底运动鞋；灰色斜挎包；自然双手垂落|streetwear
模特型录斜襟长裙|lookbook asymmetric wrap dress|奶油不透明斜襟长袖中长连裙；侧腰系结；棕色平底鞋；小圆弧包；轻转展示腰结|minimal
模特型录宽短裤套装|lookbook tailored long-shorts suit|奶白内搭与灰色宽肩短西装；灰色及膝宽短裤；黑色乐福鞋；小黑包；正面自然站立|minimal
'''.replace('|特制','|minimal'))
block('model_outfits','编辑拍摄与场外搭配','''
模特杂志黑白反差装|editorial black-white contrast ensemble|白色大翻领长袖衬衣；黑色高腰长伞裙；黑色低跟鞋；白色方形手袋；自然一手扶腰不遮衣物|minimal
模特杂志红灰色块装|editorial red-grey colour story|正红长袖短西装叠完整灰色内搭；深灰阔腿裤；银灰鞋；纯黑手包；略微侧转|minimal
模特杂志长丝巾风衣|editorial scarf-and-trench styling|奶白衬衣和卡其长风衣；黑色宽裤；黑色短靴；钴蓝长丝巾与方包；丝巾自然垂落|british
模特杂志金属感褶裙|editorial metallic pleated-skirt ensemble|黑色高领针织；银灰不透明细褶中长裙；黑色低跟靴；硬壳手拿包；直立展示材质|minimal
模特杂志帽饰长大衣|editorial hat long-coat styling|灰色圆顶宽檐帽；奶白高领内搭与炭灰长大衣；黑直裤；深色低跟鞋；几何手袋|retro
模特杂志雕塑领衬衣|editorial sculpted-collar shirt look|白色立体折片领长袖衬衣；深蓝高腰直裙；黑色方头鞋；小银色耳饰与手包|minimal
模特杂志缎裙针织对比|editorial satin-knit texture contrast|奶油色粗针织长袖上衣；棕色不透明缎面长裙；深棕靴；编织手提包；安静自然站姿|minimal
模特杂志风琴褶套装|editorial accordion-pleat coordinates|黑色合身长袖上装；钴蓝风琴褶中长裙；黑色短靴；方形手袋；轻微迈步展示裙摆|minimal
模特场外背心西装裤|off-duty vest tailored-trouser outfit|完整白色圆领棉背心与黑色短开衫；灰色宽西裤；黑色乐福鞋；小棕色肩包|minimal
模特场外皮夹克牛仔|off-duty leather-jacket denim outfit|白棉T恤与黑色宽皮夹克；蓝色直筒牛仔裤；黑色短靴；大软肩包|streetwear
模特场外大衣棒球帽|off-duty overcoat baseball-cap look|灰色棒球帽；黑色高领衫与驼色长大衣；黑色直裤；运动鞋；宽带托特包|minimal
模特场外针织衫短裤|off-duty knit long-shorts outfit|奶油色宽松长袖针织；深灰及膝宽短裤；棕色乐福鞋配短袜；黑色肩包|minimal
模特场外衬衣直筒裙|off-duty shirt straight-skirt look|浅蓝宽松衬衣；黑色中长直裙；白色帆布鞋；软布托特包|minimal
模特场外拉链卫衣长裙|off-duty zip-hoodie maxi outfit|浅灰拉链卫衣配完整白色内搭；黑色直筒长裙；灰白运动鞋；小肩包|streetwear
模特场外长风衣宽牛仔|off-duty trench wide-denim ensemble|白色棉T恤与米色长风衣；宽腿水洗蓝牛仔裤；低跟鞋；深棕手袋|british
模特场外条纹针织白裤|off-duty striped knit white trousers|藏蓝奶白条纹长袖针织；白色宽直长裤；棕色平底鞋；深棕腰带和小包|minimal
''')

assert sum(e.get('trend_model_reference',False) for e in CATALOG)==96
for e in CATALOG:
    if e['name']=='潮流棒球衫褶裙混搭':
        e['note']='图例采用棒球夹克式宽外层；保持运动领口、宽松门襟与百褶裙的对比，也可替换成棒球衫。'
    if e['name']=='模特杂志雕塑领衬衣':
        e['note']='图例采用较简化的折领；画更强的雕塑感时，可在领片端增加硬衬、折线与分层侧视图。'
