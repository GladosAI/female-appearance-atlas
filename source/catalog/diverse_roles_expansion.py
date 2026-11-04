"""V27: many costume identities, two distinct outfits for each identity."""
from catalog_content import CATALOG,category,add
NEW_CATEGORIES=['urban_role_outfits','outdoor_role_outfits','dance_variety_outfits','fantasy_role_outfits']
for key,name,guide in [
 ('urban_role_outfits','都市职业与行业装扮','8种都市职业各2套：法官、律师、法医、交通警察、体育裁判、记者、电影导演、调酒师。以服装层次、头饰、包袋和职业道具区分；均为原创角色设计，不对应特定国家或机构制式。'),
 ('outdoor_role_outfits','户外作业与竞技装扮','8种户外身份各2套：赛车手、摩托骑手、潜水员、养蜂人、驯鹰师、渔业作业者、灯塔守望员、极地考察员。比较完整衣着、帽盔面罩、手套、鞋靴和携行物，图例用于角色造型。'),
 ('dance_variety_outfits','舞蹈与杂艺装扮','8种舞台或运动表演身份各2套：弗拉门戈、探戈、爱尔兰舞、桑巴巡游、花样滑冰、花样游泳、腹语师、魔术助理。比较裙摆、裤装、袖型、鞋履、头饰和手持道具；舞种款式为原创舞台灵感改编。'),
 ('fantasy_role_outfits','奇幻身份与异界装扮','8种奇幻身份各2套：吟游诗人、驯龙师、森林德鲁伊、亡灵法师、圣骑士、召唤师、结界师、傀儡师。按衣物、护具、披覆、头饰与道具组织，使用原创游戏幻想语境。')]:
    category(key,name,guide,['R95'])

def pair(cid,kind,key,one,two):
    for variant,text in enumerate([one,two],1):
        name,en,recipe=text.split('|');add(cid,kind,f'{name}|{en}|25岁以上明确成年女性；{recipe}。')
        CATALOG[-1].update(added_in='27.0',adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年原创角色装扮参考',stage_family_reference=True,stage_family=cid,diverse_role_reference=True,role_kind=key,role_kind_name=kind,role_variant=variant,outfit_components=recipe.split('；'),reference_ids=['R95'],aliases=[kind,key],
          note='每种身份提供两套结构不同的原创成年角色服装。区分服装主体、头部装饰、鞋靴、携行物和道具固定方式；专业装备为外观灵感，舞种与奇幻款为原创改编，不将图例等同于统一制式或史实复原。')

pair('urban_role_outfits','法官','judge',
 '法官宽袖长袍装|judge wide-sleeve robe costume|黑色不透明宽袖及踝长袍；白色短领片；内搭深色长裤与平底皮鞋；一手持合拢素面卷宗，无国徽徽章',
 '法官披肩领礼袍装|judge cape-collar robe costume|深酒红不透明长袖及踝礼袍；黑色短披肩式领片；白色小领巾；黑皮鞋与合拢文件夹，无国家标记')
pair('urban_role_outfits','律师','advocate',
 '律师三件套出庭装|advocate three-piece trouser suit|炭灰西装外套与马甲；白衬衣和素色领带；同色长裤、皮鞋；一手持棕色公文包',
 '律师前开长袍装|advocate open-front gown costume|黑色不透明前开长袖袍；内搭白衬衣、白色短领片与深色膝下直裙；黑色鞋与文件夹，不采用特定地区假发')
pair('urban_role_outfits','法医勘验','forensic_examiner',
 '法医连体勘验外观装|forensic examiner coverall styling|白色不透明连帽完整连体工作服；简洁口罩与护目镜；蓝色手套、包覆鞋；一手持封闭小型硬箱，无尸体或血迹',
 '法医深色工作外衣装|forensic examiner dark workcoat|藏蓝长袖及膝工作外衣；浅色衬衣与深色长裤；蓝色手套、包覆鞋；一手托素面记录板，无受伤人物')
pair('urban_role_outfits','交通警察','traffic_officer',
 '交通警察反光背心装|traffic officer reflective-vest costume|浅蓝短袖衬衣与藏蓝长裤；荧黄反光背心；白色简洁勤务帽；白手套、黑皮鞋及腰侧小包，无官方徽章',
 '交通警察雨天外披装|traffic officer rain-cape costume|荧黄不透明防雨披衣至膝部；藏蓝长裤；白色带透明护面片头盔；黑雨靴与白手套，无文字或徽章')
pair('urban_role_outfits','体育裁判','sports_referee',
 '篮球裁判条纹上衣装|basketball referee striped uniform|黑白竖条纹短袖翻领上衣；黑色直筒运动长裤；腰侧夹式小哨；黑色运动鞋，无号码与队徽',
 '足球裁判口袋运动装|football referee pocketed uniform|亮黄短袖翻领上衣带两个胸袋；黑色及膝运动短裤；黑色长运动袜与运动鞋；腕表和胸前小哨')
pair('urban_role_outfits','记者','reporter',
 '外景记者多袋夹克装|field reporter utility jacket|卡其长袖多袋夹克；深蓝完整长裤与防水短靴；斜挎设备包；一手在身侧持无台标短麦克风',
 '演播记者西装裤装|studio reporter tailored trouser ensemble|青灰短西装外套；奶白圆领上衣与同色长裤；小型领夹麦克风；低跟鞋与一手托持的素面记录夹')
pair('urban_role_outfits','电影导演','film_director',
 '电影导演背心工作装|film director utility-vest outfit|黑色多袋工作背心；灰色长袖T恤与黑色工装长裤；轻便耳机；运动鞋，一手在身侧持无字合拢场记板',
 '电影导演户外夹克装|film director location jacket|橄榄色长袖工装夹克；深色针织上衣与卡其长裤；棒球帽与挂颈耳机；短靴、一手托素面平板')
pair('urban_role_outfits','调酒师','bartender',
 '调酒师马甲领结装|bartender waistcoat and bow-tie outfit|白色长袖衬衣；黑色合体马甲与小领结；黑色长裤与皮鞋；一手持合拢金属调饮壶',
 '调酒师皮围裙工作装|bartender leather-apron outfit|深绿卷袖衬衣；棕色交叉肩带及膝皮围裙；完整深色长裤；短靴，腰侧插入小布巾')

pair('outdoor_role_outfits','赛车手','racing_driver',
 '赛车手高领连体装|racing driver high-collar coverall|白灰拼色不透明高领长袖完整连体服；宽腰带与包覆手套；赛车短靴；一手在身侧抱无标识全盔',
 '卡丁车手拼片连体装|kart racer panelled coverall|深蓝橙色拼片高领长袖连体服；外层短护肋背心；完整长裤腿、手套与短靴；无标识全盔抱在腰侧')
pair('outdoor_role_outfits','摩托车骑手','motorcycle_rider',
 '摩托骑手分体夹克装|motorcycle rider two-piece outfit|深棕厚夹克与黑色长裤；肩肘膝外观护片；完整手套、包覆骑行靴；一手抱无标识全盔',
 '摩托骑手连体皮衣装|motorcycle rider one-piece leather suit|黑灰拼片不透明立领长袖完整连体皮衣；肩肘膝护片；包覆手套与长靴；一手抱素面全盔')
pair('outdoor_role_outfits','潜水员','diver',
 '潜水员完整湿式服装|diver full-length wetsuit styling|深蓝不透明高领长袖完整潜水连体服；面镜挂于颈部；完整潜水短靴；一手在身侧抱一对短脚蹼，另一手自然放松',
 '潜水员干式外衣装|diver drysuit styling|宽松厚实灰蓝完整长袖干式服；完整手套和包覆靴；背部单气瓶与肩带；调节器软管接至领前，一手抱透明面镜')
pair('outdoor_role_outfits','养蜂人','beekeeper',
 '养蜂人圆帽面纱装|beekeeper round-veil coverall|米白完整连帽长袖连体工作服；宽圆帽沿与前后闭合网纱面罩可见成年脸；完整手套、包覆靴；无蜜蜂群',
 '养蜂人拱形罩帽装|beekeeper fencing-veil jacket outfit|奶白拱形支架网罩帽连长袖夹克；完整卡其长裤；长手套与包覆靴；腰侧扁工具包，不带蜂群')
pair('outdoor_role_outfits','驯鹰师','falconer',
 '驯鹰师皮手套旅装|falconer gauntlet field outfit|深绿长袖及膝猎装外衣；棕色长裤和包覆靴；左前臂戴厚长皮手套；腰侧扁皮袋，无活体动物',
 '驯鹰师短披肩装|falconer capelet outfit|橄榄色短披肩覆灰色长袖衬衣；棕色背心与完整长裤；软毡帽、长皮手套和短靴；腰带挂小型封口袋')
pair('outdoor_role_outfits','渔业作业者','fishery_worker',
 '渔业胸高涉水裤装|fishery worker chest-wader outfit|深绿不透明胸高防水背带长裤连包覆长靴；内搭浅色完整长袖衫；软沿帽和完整手套；一手提小封闭工具桶',
 '渔业防雨背带装|fishery worker rain-bib outfit|黄色厚防雨长袖夹克；橙色高腰背带长裤；深色防水长靴与手套；带帽领口，无渔获或血迹')
pair('outdoor_role_outfits','灯塔守望员','lighthouse_keeper',
 '灯塔守望员呢外套装|lighthouse keeper wool-coat outfit|藏蓝双排扣及膝厚呢外套；奶白高领针织衫；完整长裤和防滑短靴；一手在身侧提封闭玻璃提灯',
 '灯塔守望员防雨装|lighthouse keeper rainwear outfit|黄色及膝连帽不透明雨衣；藏蓝长裤与黑雨靴；针织帽露在帽兜边；一手提小型封闭手灯')
pair('outdoor_role_outfits','极地考察员','polar_researcher',
 '极地考察员保暖大衣装|polar researcher insulated-parka outfit|橙色厚长袖连帽保暖大衣；深色完整保暖长裤；厚手套与雪地长靴；护目镜置于帽前、背部小型包',
 '极地考察员背带裤装|polar researcher bib-trouser outfit|蓝灰色厚长袖套头外衣；红色胸高保暖背带长裤；厚手套与包覆雪靴；针织帽和紧凑工具包')

pair('dance_variety_outfits','弗拉门戈舞台灵感','flamenco',
 '弗拉门戈层褶舞裙装|flamenco-inspired tiered-ruffle costume|红色不透明长袖高圆领上衣；黑红层叠荷叶边及踝宽摆裙；低跟舞鞋；盘发侧花，无高开衩',
 '弗拉门戈波点长裙装|flamenco-inspired polka-dot dress|黑白波点不透明长袖及踝连衣裙；袖口与下摆多层荷叶边；红色短肩披和侧花；低跟舞鞋')
pair('dance_variety_outfits','探戈舞台灵感','tango',
 '探戈垂褶长裙装|tango-inspired draped long dress|酒红不透明圆领长袖及踝垂褶裙；收束腰带与不透明完整裙衬；包覆低跟舞鞋；侧分盘发，无高开衩',
 '探戈西装长裤装|tango-inspired tailored trouser outfit|黑色短西装外套与马甲；白色长袖衬衣及细领带；完整高腰长裤；黑色低跟舞鞋，简洁盘发')
pair('dance_variety_outfits','爱尔兰舞台灵感','irish_dance',
 '爱尔兰舞几何绣裙装|Irish-dance-inspired embroidered dress|深蓝不透明立领长袖及膝A字裙；前胸与裙摆原创几何盘线饰纹；完整不透明袜裤；黑色系带软舞鞋，无特定团体标记',
 '爱尔兰舞背心百褶装|Irish-dance-inspired waistcoat ensemble|白色不透明长袖衬衣；深绿短背心与及膝百褶裙；完整深色袜裤；黑色系带舞鞋与小发带')
pair('dance_variety_outfits','桑巴巡游灵感','samba_parade',
 '桑巴巡游连体羽饰装|samba-parade-inspired feather-backpiece unitard|青绿不透明高领长袖完整连体长裤；金色饰带；小型蓝绿羽毛背架与发箍，固定于肩背带；平底舞靴，所有羽尖在格内',
 '桑巴巡游阔腿裤装|samba-parade-inspired wide-trouser costume|橙金色不透明圆领长袖长上衣；完整宽腿舞裤；小型羽毛肩领与小羽饰发箍；包覆舞鞋，无翅膀或巨大冠饰')
pair('dance_variety_outfits','花样滑冰','figure_skater',
 '花滑长袖短叠裙装|figure-skater long-sleeve skirt costume|蓝灰不透明高领长袖上衣连完整运动裤袜；腰部短叠裙；少量银色几何饰边；白色花滑冰鞋且金属刀刃清楚，无舞姿',
 '花滑立领长裤装|figure-skater high-collar trouser costume|深紫不透明立领长袖上衣；灰色完整合体运动长裤；肩袖银色饰片；黑色花滑冰鞋且刀刃清晰，自然站立')
pair('dance_variety_outfits','花样游泳','artistic_swimmer',
 '花样游泳高领泳装|artistic-swimmer high-neck costume|藏蓝不透明高领宽肩带标准完整连体泳装；普通运动腿口；青绿几何拼色与配套贴头泳帽；裸足自然站立，正常成年运动体态',
 '花样游泳长腿训练装|artistic-swimmer full-leg training suit|青绿不透明圆领短袖完整长腿泳装连体服；白色几何拼片；贴头泳帽；裸足中性站姿，无眼罩或头盔')
pair('dance_variety_outfits','腹语师','ventriloquist',
 '腹语师燕尾裤装|ventriloquist tailcoat trouser outfit|深蓝燕尾外套；白衬衣、领结与完整长裤；黑皮鞋；一手在身侧戴小型布偶手套，另一手放松，布偶是道具非真人',
 '腹语师条纹背心装|ventriloquist striped-shirt waistcoat outfit|灰白条纹长袖衬衣；酒红背心与完整深色长裤；皮鞋；双手在腰侧托一个小型完整着装木偶，无巨大人头')
pair('dance_variety_outfits','魔术助理','magic_assistant',
 '魔术助理短披风裤装|magic-assistant capelet trouser costume|黑白短燕尾外套覆不透明白色高领长袖上衣；完整长裤；红色短披肩与白手套；黑皮鞋，一手持短钝头道具杖',
 '魔术助理长手套裙裤装|magic-assistant skort ensemble|深紫不透明高圆领长袖上衣；及膝上完整裙裤内置安全短裤；完整不透明袜裤与长手套；小礼帽及踝靴，无内衣式服装')

pair('fantasy_role_outfits','吟游诗人','bard',
 '吟游诗人短披风装|bard short-cape outfit|酒红短披风；奶白高领长袖衬衣和棕色系带背心；完整长裤及翻口靴；小型鲁特琴靠身侧抱持，无文字',
 '吟游诗人行旅长衣装|travelling bard long-tunic outfit|蓝灰及膝长袖束腰外衣；米白短肩披；完整长裤与软靴；腰侧琴袋，一手在身侧持小型里拉琴')
pair('fantasy_role_outfits','驯龙师','dragon_tamer',
 '驯龙师皮护肩工作装|dragon-tamer leather-shoulder outfit|深棕长袖完整厚皮外衣；肩部圆形护片；灰色长裤与包覆靴；完整厚手套和宽腰带、封口饲料袋，无活体龙',
 '驯龙师兜帽背心装|dragon-tamer hooded-vest outfit|深绿带帽厚背心叠米白长袖衬衣；完整灰色工装长裤；皮护前臂与长靴；腰侧软包，无翅膀或龙头替换')
pair('fantasy_role_outfits','森林德鲁伊','forest_druid',
 '森林德鲁伊叶披长袍|fantasy druid leaf-mantle robe|深绿不透明高领长袖及踝袍；叶片形布披肩；小型枝条发箍；包覆短靴，一手持短木杖，不对应真实宗教礼服',
 '森林德鲁伊行旅短衣|fantasy travelling druid tunic|米棕不透明长袖及膝短袍；深绿腰带与完整长裤；棕靴；小型植物纤维背包，肩上短叶形布饰')
pair('fantasy_role_outfits','亡灵法师','necromancer',
 '亡灵法师高领长衣|necromancer high-collar coat|炭灰不透明高领长袖及踝长衣；紫色内襟与骨形平面织物饰纹；完整手套和靴；一手持合拢素面书，无尸骨或血腥',
 '亡灵法师兜帽披覆|necromancer hooded-mantle outfit|灰紫开放面口兜帽长披风；内搭黑色完整长袖衣裤；包覆长靴；腰侧封闭小瓶与几何胸针，无幽灵或尸体')
pair('fantasy_role_outfits','圣骑士','paladin',
 '圣骑士白金全甲装|paladin white-gold full-armour outfit|白金原创完整胸肩臂腿护甲；不透明长袖长裤衬衣；蓝色及膝护裙布；包覆靴，一手在身侧持小圆钝盾，无武器或宗教徽标',
 '圣骑士罩袍链甲装|paladin surcoat-and-mail outfit|银灰链甲长衣覆完整深蓝长袖内衣与长裤；米白无袖及膝罩袍；皮腰带、完整手套与长靴，原创几何胸饰')
pair('fantasy_role_outfits','召唤师','summoner',
 '召唤师纹章短披装|summoner emblem-capelet outfit|紫色不透明高领长袖及膝外衣；银灰短肩披与原创几何饰片；完整长裤及长靴；一手持合拢小册，无召唤生物',
 '召唤师白蓝长外套装|summoner white-blue long-coat outfit|白蓝不透明立领长袖及膝长外套；完整深色长裤；几何腰牌与腰侧软包；包覆靴，一手持小型钝圆道具片')
pair('fantasy_role_outfits','结界师','barrier_mage',
 '结界师几何叠袍装|barrier-mage geometric-layer robe|青灰不透明交领长袖及踝叠袍；肩前小型几何布片；深蓝腰带和腕环；包覆靴，一手托小型透明钝棱晶体道具，无悬浮光阵',
 '结界师都市机能装|urban barrier-mage utility outfit|深蓝不透明高领长袖衣与灰色短外套；完整工装长裤；短几何肩披和腕部小装置；短靴、腰侧封口包，无发光效果遮住衣物')
pair('fantasy_role_outfits','傀儡师','puppeteer',
 '机关傀儡师工具长衣|mechanical puppeteer utility-coat outfit|棕灰不透明长袖及膝工具外衣；完整长裤和短靴；腰侧卷线盘与扁工具包；一手在身侧托小型完整木偶，无跨格长线',
 '布偶傀儡师拼片围裙装|fabric puppeteer patchwork-apron outfit|米白完整长袖衬衣；蓝灰及膝拼片围裙；完整深色长裤和短靴；腰侧布袋中露出一个小型布偶头，道具与人物分明')
