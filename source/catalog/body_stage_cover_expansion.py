"""V24: adult body shapes/posture, four stage-costume families and worn face covers."""
from catalog_content import CATALOG, category, add

NEW_CATEGORIES=['gymnastics_outfits','cheer_outfits','reaper_costumes','runway_lingerie']
for cid,name,guide,refs in [
 ('gymnastics_outfits','体操服装','16套成年体操训练、竞技和艺术体操灵感服装，比较袖型、连体覆盖、训练叠穿和器械配合；均为原创服装参考，不声明符合某场赛事规则。',['R88']),
 ('cheer_outfits','啦啦队服装','16套成年竞技与表演啦啦队装，分辨上衣、裙裤、包覆层、鞋袜和手持花球；原创配色、无校名队徽。',['R89']),
 ('reaper_costumes','死神主题装扮','16套成年原创死神角色装扮，比较兜帽、长袍、披风、护甲、面罩和仪式道具；完整面孔及身体，无伤口或尸体损伤。',['R63']),
 ('runway_lingerie','维密风格秀场装扮','16套成年翼饰内衣秀场灵感装扮，区分胸衣、连体衣、短裤、长袍、翅饰和固定点；原创改编，不复制品牌整套造型或真人模特。',['R90'])]:
    category(cid,name,guide,refs)

SHAPES=[
 ('fitness','健身肌肉型','athletic muscular build','肩臂、背部和腿部有清楚而自然的肌肉体积，四肢结实，站姿放松','健身型、肌肉型、运动型'),
 ('pear','梨形身型','pear-shaped build','肩带较窄、骨盆与大腿外侧较宽，腰胯转折清楚，前后视角均保留自然腹部','梨形、下半身较宽'),
 ('apple','苹果形身型','apple-shaped build','躯干与腰腹体积较集中，腰部收束不明显，四肢体积相对较小','苹果形、腰腹丰满'),
 ('hourglass','沙漏形身型','hourglass build','肩部与骨盆宽度接近，腰部有自然清楚收束；保持正常人体比例','沙漏形、腰线明显'),
 ('rectangle','矩形身型','rectangular build','肩、腰、骨盆正面宽度差较小，躯干两侧线条较直','矩形、直筒型、H型'),
 ('inverted_triangle','倒三角身型','inverted-triangle build','肩带显著宽于骨盆，腰胯较窄，上宽下窄的骨架关系清楚','倒三角、宽肩窄胯'),
 ('small_bust','贫胸与小胸轮廓','small-bust contour','明确成年自然体型，胸前轮廓较平缓、前向突出较少，其他骨架与四肢采用中等体型','贫胸、平胸、小胸'),
 ('full_bust','丰胸轮廓','full-bust contour','明确成年自然体型，胸部体积较丰满、侧向前突可辨，但不使用夸张不合理比例，其他骨架中等','丰胸、大胸、胸部丰满'),
 ('projected_glutes','翘臀轮廓','projected-glute contour','明确成年自然体型，臀部后侧有较明显圆润体积和向后突出，腰背保持自然，不用拱腰制造轮廓','翘臀、臀部后突'),
 ('flat_glutes','平臀轮廓','flatter-glute contour','明确成年自然体型，臀部向后突出较少、侧面较平缓，骨盆与腰背保持自然','平臀、臀部较平'),
 ('left_shoulder_high','高低肩左高右低','left-shoulder-higher posture','正面以角色自身左肩较高、右肩较低为可见特征，骨盆保持水平；肩线不水平但没有受伤','高低肩、左肩高'),
 ('right_shoulder_high','高低肩右高左低','right-shoulder-higher posture','正面以角色自身右肩较高、左肩较低为可见特征，骨盆保持水平；肩线不水平但没有受伤','高低肩、右肩高'),
 ('rounded_shoulders','圆肩含胸体态','rounded-shoulder posture','双肩向前、肩胛带略内收，胸廓前侧稍收拢，头部接近自然位置；侧面更明显','圆肩、含胸'),
 ('rounded_back','驼背轮廓体态','rounded-upper-back posture','上背呈较明显但非极端的圆弧，肩部前移，颈部随躯干位置自然调整；完整稳定站姿','驼背、圆背、上背弯曲'),
 ('forward_head','头前伸体态','forward-head posture','耳部和头部整体前移到肩线前方，躯干相对直立，不用夸张弯腰替代；侧面明确','头前伸、探颈、颈前倾'),
 ('anterior_pelvis','骨盆前倾外观','anterior-pelvic-tilt appearance','侧面骨盆向前旋转、腰背弧度增加且腹部自然前置，膝部放松；幅度适中，不用性感摆姿','骨盆前倾、腰背弧度')
]
for view,dimension in [('front','成年身型与体态·正面'),('side','成年身型与体态·侧身')]:
    for key,label,en,shape,aliases in SHAPES:
        pose='正面平视，角色面向观众，双臂自然略离躯干，双脚稳定落地' if view=='front' else '严格朝画面右侧90度侧身，耳肩、躯干、骨盆和足侧面关系清楚，双臂自然下垂'
        add('body',dimension,f"{label}{'正面' if view=='front' else '侧身'}参考|{en} {view} study|25岁以上明确成年女性，{pose}；{shape}；穿完整不透明哑光灰色圆领长袖贴合运动上衣和深灰长裤、平底鞋。")
        CATALOG[-1].update(added_in='24.0',adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年体型与体态创作参考',
          body_shape_reference=True,body_shape_key=key,body_shape_view=view,paired_shape_label=label,
          aliases=aliases.split('、')+['成年身型','身材参考','正面' if view=='front' else '侧身'],reference_ids=['R09','R92'],
          note='自然成年体型与绘画姿态的可见轮廓标签，不用于美丑排序、年龄发育分级或疾病诊断。前后体积可结合正面和侧身一起看；上衣与长裤保持不透明，无裸露局部或透视解剖。')

def outfits(cid,dimension,rows,aliases,refs):
    lines=[line.strip().split('|') for line in rows.strip().splitlines()];assert len(lines)==16
    for name,en,recipe in lines:
        add(cid,dimension,f'{name}|{en}|25岁以上明确成年女性；{recipe}。')
        CATALOG[-1].update(added_in='24.0',adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年舞台与服装设计参考',
          stage_family_reference=True,stage_family=cid,outfit_components=recipe.split('；'),aliases=aliases+[dimension],reference_ids=refs,
          note='原创成年角色服装参考，服装不透明，采用服装展示的自然站姿；文化、运动及品牌灵感与实际组织服装分开理解，具体比赛规则与防护用途不由图例判定。')

outfits('gymnastics_outfits','体操训练与表演服装','''
体操素色长袖连体服|long-sleeve gymnastics leotard|深蓝圆领长袖不透明连体体操服；普通运动腿口；浅色体操软鞋；头发收拢
体操短袖拼色连体服|short-sleeve panel gymnastics leotard|蓝灰短袖连体体操服；肩胸几何拼色；普通运动腿口；体操软鞋
体操宽肩无袖连体服|wide-strap sleeveless gymnastics leotard|酒红高圆领宽肩无袖连体服；腰部简洁缝线；普通腿口；软鞋
体操四分之三袖服|three-quarter-sleeve gymnastics leotard|深绿四分之三袖连体体操服；袖口在前臂中段；完整胸腹覆盖；软鞋
体操长裤连体训练服|full-leg gymnastics unitard|蓝色圆领长袖连体衣；完整裤腿延至脚踝；腰线只有服装拼缝；软鞋
体操无袖长裤连体服|sleeveless full-leg gymnastics unitard|灰紫宽肩圆领无袖长裤连体体操服；完整胸腹与双腿覆盖；浅色软鞋
体操短袖及膝连体服|knee-length gymnastics training unitard|墨绿短袖连体训练衣；裤腿延至膝部；普通平领；软鞋
体操训练短裤叠穿|gymnastics leotard with training shorts|完整浅灰长袖体操服；外叠深灰宽松训练短裤；软鞋；双手自然下垂
体操热身长裤叠穿|gymnastics warm-up trousers layering|深蓝短袖连体训练服；外叠灰色直筒热身长裤；浅色运动鞋
体操开襟热身外套|gymnastics warm-up jacket outfit|普通不透明长袖体操服；外加前开襟短运动外套；配完整训练长裤；运动鞋
体操护掌训练装|gymnastics hand-grip practice look|深红长袖连体体操服；双腕佩戴普通护掌和窄护腕；腿口标准；软鞋；手指自然
体操半足袜训练装|gymnastics half-foot sock outfit|青蓝宽肩连体体操服；双脚半足袜覆盖脚趾脚掌、露出足跟；双腿自然直立
艺术体操持球服|rhythmic-gymnastics ball costume|紫色完整长袖连体服；腰侧小片不透明短裙摆；一手在腰旁托小型体操球；软鞋
艺术体操持圈服|rhythmic-gymnastics hoop costume|深绿不透明短袖连体服；短裙摆；一只体操圈竖直放在身侧、全部圈缘在格内；软鞋
艺术体操持棒服|rhythmic-gymnastics clubs costume|深蓝不透明长袖连体服；短裙摆；双手自然持一对体操棒；软鞋
艺术体操短带展示服|rhythmic-gymnastics ribbon-display costume|酒红不透明长袖连体服；短裙摆；一手持短杆、丝带收成小圈在身侧；软鞋；不展开大幅动态
''',['体操','体操服','竞技体操','艺术体操'],['R88'])

outfits('cheer_outfits','成年啦啦队服装方案','''
啦啦队V纹背心裙装|V-panel cheer shell and skirt|蓝白圆领无袖上衣有胸前V形拼片；同色百褶短裙与内层运动短裤；白袜运动鞋；手持小花球
啦啦队长袖百褶裙装|long-sleeve pleated-skirt cheer uniform|红白长袖高圆领上衣；同色百褶短裙内有运动短裤；白袜运动鞋；头发固定
啦啦队短袖直裙装|short-sleeve straight-skirt cheer look|深绿短袖圆领上衣；同色直线短裙、侧边小开衩和完整内层短裤；运动鞋
啦啦队高领连衣裙|high-neck one-piece cheer dress|紫白高领无袖一体式短裙服；腰部分色；内置完整运动短裤；白色运动鞋
啦啦队拼色短裤装|colour-block cheer shorts ensemble|黑金短袖圆领上衣；高腰运动短裤；普通短袜与运动鞋；双手各持一只小花球
啦啦队长袖短裤装|long-sleeve cheer shorts ensemble|海军蓝长袖圆领上衣；白色运动短裤；短袜运动鞋；小蝴蝶结固定在马尾根部
啦啦队完整连体裤装|full-length cheer performance unitard|黑紫不透明长袖连体运动衣；完整长裤腿；胸前原创V纹；白色运动鞋
啦啦队热身运动套装|cheer warm-up tracksuit|蓝白拉链运动外套；配同色长运动裤；运动鞋；小花球握在身侧
啦啦队无袖高腰裙装|sleeveless high-waist cheer skirt set|米白无袖圆领上衣；红色高腰百褶短裙内含完整运动短裤；白袜运动鞋
啦啦队斜纹长袖裙装|diagonal-stripe cheer skirt uniform|青绿长袖圆领上衣；斜向拼色从肩部至腰侧；同色短裙内含运动短裤；运动鞋
啦啦队宽腰带裙装|broad-waistband cheer skirt look|黑白短袖上衣；黑色宽腰带百褶短裙与内层运动短裤；白色短袜运动鞋
啦啦队层叠裙摆装|layered-hem cheer performance look|深蓝长袖圆领上衣；双色两层短裙摆和内层短裤；白色运动鞋；小型发结
啦啦队上衣短裙裤|cheer top and athletic skort|酒红无袖圆领运动上衣；外观为短裙的运动裙裤；白袜运动鞋；花球不遮挡服装
啦啦队冬季长裤装|winter cheer trousers ensemble|深绿保暖长袖上衣；黑色修身完整运动长裤；短袜运动鞋；配小型保暖发带
啦啦队金属感表演装|metallic-panel adult cheer costume|黑色长袖不透明运动上衣；银色几何拼片；同色短裤外叠短裙片；运动鞋
啦啦队教练展示套装|adult cheer coach presentation outfit|米白短袖运动上衣；深蓝直筒运动长裤；腰侧小训练包；运动鞋；手持一对收拢花球
''',['啦啦队','啦啦操','cheerleading','成年啦啦队'],['R89'])

outfits('reaper_costumes','原创死神袍服与道具','''
死神基础兜帽长袍|classic hooded reaper robe|黑色不透明高领长袖及踝长袍；宽兜帽面口露出完整成年面孔；黑色靴；无道具
死神宽袖绳腰袍|wide-sleeve cord-belt reaper robe|炭灰宽袖及踝长袍内有完整长袖内层；绳腰带；兜帽开放面口；黑靴
死神短披肩长袍|short-cape reaper robe|黑色高领长袍；灰色短肩披与兜帽；几何金属小扣；平底长靴
死神长斗篷裤装|reaper mantle and trousers|黑色高领长袖上衣与完整长裤；长黑斗篷和开放面兜帽；黑靴；完整手套
死神白袍变体|ivory-robed reaper variation|奶白不透明长袖及踝袍；灰色衣缘与开放面兜帽；白色靴；原创架空配色
死神残边外披装|ragged-overlayer reaper costume|完整黑色长袖内袍与长裤；外披边缘破旧灰斗篷；面孔和皮肤完整；黑靴
死神骨纹衣饰装|bone-motif reaper costume|黑色高领完整长袖长袍；衣面抽象浅灰骨形纹；兜帽与黑靴；不是裸骨或骷髅身体
死神半面装饰面具|half-mask reaper ensemble|黑色完整长袖长袍；开放面兜帽；额眼部佩戴灰色原创半面具、下半脸可见；黑靴
死神整面素面具|full-mask reaper ensemble|灰黑完整长袖长袍与斗篷；佩戴浅灰素面具，眼孔和固定带清楚；手套黑靴
死神肩甲护臂装|armoured-shoulder reaper costume|黑色不透明长袍；原创银灰肩甲与护臂；开放面兜帽；腰带与黑靴
死神仪式长肩布|ceremonial-scapular reaper look|深灰高领长袍；银白长肩布在前后垂下；几何腰扣；开放面兜帽黑靴
死神持镰道具装|reaper with ceremonial scythe prop|完整黑色长袍与开放面兜帽；一手竖持小型原创钝缘弧刃镰形舞台道具，全部在格内；黑靴
死神提灯装|lantern-bearing reaper costume|黑灰长袖及踝长袍；开放面兜帽；一手在腰旁提封闭小灯笼；黑色靴
死神沙漏装|hourglass-bearing reaper costume|深灰高领长袖长袍；短肩披和开放面兜帽；双手在腹前托小沙漏；黑靴
死神冥册装|book-bearing reaper costume|黑色不透明长袖长袍；灰色直条衣缘；腰侧书袋，一手持无文字小书；兜帽黑靴
未来死神装甲长衣|future-reaper armour coat|黑灰完整高领长衣与长裤；分片肩护甲；开放面几何帽兜；手套长靴；原创科幻无武器
''',['死神','收割者','grim reaper','兜帽死神'],['R63'])

outfits('runway_lingerie','成年翼饰内衣秀场灵感','''
维密风格白羽翼胸衣套装|white-feather-wing lingerie runway look|白色不透明有衬里结构胸衣与普通全包覆三角裤；背部小型白羽舞台翅饰有肩带固定；白色秀场鞋
维密风格黑羽翼连体装|black-feather-wing runway bodysuit|黑色不透明有衬里无袖连体内衣；标准腿口与完整胸部覆盖；背部小型黑羽翅饰固定；黑色秀场鞋
维密风格彩羽翼短裤装|colour-feather-wing runway shorts look|深蓝不透明结构胸衣与高腰短裤；背部紧凑彩羽扇形翅饰有固定肩架；秀场鞋
维密风格粉色蝴蝶翼装|pink-butterfly-wing lingerie runway look|浅粉不透明有衬里结构胸衣和高腰普通三角裤；背部小型原创蝴蝶舞台翅饰；秀场鞋
维密风格银色星芒翼装|silver-starburst-wing runway look|银灰不透明无袖连体胸衣；背部紧凑放射状软质星芒舞台翅饰；银色秀场鞋
维密风格金色叶片翼装|gold-leaf-wing runway look|金色不透明有衬里短胸衣和高腰短裤；背部小型叶片舞台翅饰有背架；金色鞋
维密风格缎面束身胸衣|satin-structured corset runway look|酒红不透明缎面结构胸衣和普通全包覆三角裤；垂下的短缎带只在衣侧；秀场鞋；无翅饰
维密风格丝绒连体胸衣|velvet runway bodysuit|深绿不透明丝绒无袖连体胸衣；普通腿口；几何细边；同色秀场鞋；无翅饰
维密风格珠饰外罩套装|beaded-overlay runway ensemble|黑色不透明结构胸衣和高腰短裤作为完整内层；外加短珠串肩披，珠串不遮面；黑色鞋
维密风格花瓣翼连体装|petal-wing runway bodysuit|淡紫不透明有衬里连体胸衣；背部小型花瓣扇形舞台翅饰；浅紫秀场鞋
维密风格缎袍内衣装|satin-robe lingerie runway ensemble|米白不透明结构胸衣和普通全包覆三角裤；外披自然垂落的长缎袍，门襟敞开；秀场鞋
维密风格短披风秀场装|short-cape lingerie runway ensemble|深蓝不透明有衬里结构胸衣和高腰短裤；短披风在肩上固定；秀场鞋
维密风格羽领连体装|feather-collar runway bodysuit|灰白不透明无袖连体胸衣；肩颈外缘小型软羽领不遮脸；标准腿口；秀场鞋
维密风格几何背架装|geometric-backpiece runway look|黑金不透明结构胸衣与高腰短裤；背后紧凑椭圆几何背架通过肩带连接；黑色鞋
维密风格宝石饰边套装|jewel-trim lingerie runway look|深蓝不透明有衬里连体胸衣；普通腿口与衣缘少量原创宝石形装饰；秀场鞋；无翅饰
维密风格长手套翼饰装|long-glove winged runway ensemble|浅灰不透明有衬里长裤连体胸衣；完整长手套；背部小型银灰羽状舞台翅饰；灰色秀场鞋
''',['维密','维多利亚的秘密风格','内衣秀','翼饰秀场','runway lingerie'],['R90'])

def covers(dimension,text,kind,refs):
    lines=[line.strip().split('|') for line in text.strip().splitlines()];assert len(lines)==16
    for name,en,feature in lines:
        add('face_overlays',dimension,f'{name}|{en}|25岁以上成年女性完整头肩佩戴图；{feature}；普通不透明高领衣物覆盖肩胸。')
        CATALOG[-1].update(added_in='24.0',adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年面部覆盖物绘画参考',
          face_cover_reference=True,face_cover_kind=kind,aliases=['佩戴面部覆盖物',dimension]+{'mask':['口罩'],'respirator':['防毒面具','呼吸器'],'decorative':['一般面具','面具']}[kind],reference_ids=refs,
          note='佩戴方式与遮挡范围的原创外观参考。防护器材仅示意外壳、滤盒和固定带，不声明过滤等级或适用危险环境；真实防护不能由外观图判定。一般面具是装饰道具，与呼吸防护器不同。')

covers('口罩结构与佩戴','''
三褶耳挂口罩佩戴|pleated ear-loop mask worn|正面，浅蓝三褶口罩完整覆盖口鼻至下巴；左右耳挂清楚；鼻梁贴合线清楚
三褶绑带口罩佩戴|pleated tie-back mask worn|三分之四脸，白色三褶口罩覆盖口鼻；头后上下两组绑带可见
平折立体口罩佩戴|vertical-fold mask worn|正面，白色竖向中缝折叠口罩形成鼻口立体空间；左右耳挂清楚
三片立体口罩佩戴|three-panel mask worn|三分之四脸，白色三片折叠口罩有横向上下折边；头后两根带子可见
鸭嘴式口罩佩戴|duckbill mask worn|严格侧脸，白色口罩向前形成短鸭嘴形空间；上缘在鼻梁、下缘包下巴；头带清楚
杯形口罩佩戴|cup-shaped mask worn|三分之四脸，白色半球杯形口罩覆盖鼻口；鼻夹与双头带可见；没有印刷等级
黑色布口罩佩戴|black cloth mask worn|正面，黑色双层布口罩有中央缝线；覆盖鼻口下巴；耳挂从颊侧延伸
棉布褶口罩佩戴|pleated cotton mask worn|三分之四脸，米灰棉布口罩有横褶和包边；耳挂清楚；没有装饰图案
系带布口罩侧面|tie-back cloth mask profile|严格侧脸，灰色布口罩完整包鼻口；上带绕头、下带绕颈后；绑结不遮面
透明窗口口罩佩戴|clear-window mask worn|正面，口罩边缘为不透明浅灰布；嘴部前方小透明窗口，鼻部仍覆盖；耳挂清楚
运动面罩口罩佩戴|sport fabric face covering worn|三分之四脸，深蓝弹性布口罩包覆鼻口下巴；侧边接耳挂；普通头部不加运动头盔
加长下巴口罩佩戴|extended-chin mask worn|严格侧脸，灰色立体口罩下片延长包下巴；中缝与耳挂清楚
软垫鼻梁口罩佩戴|padded-nose mask worn|正面，白色平折口罩上缘有窄软垫边；耳挂明确；鼻口全覆盖
可调耳挂口罩佩戴|adjustable-ear-loop mask worn|三分之四脸，米灰立体口罩；耳挂上小调节扣位于耳侧；口鼻完整覆盖
头后扣连接口罩|mask with rear strap connector|严格侧后转头，脸部仍可辨；灰色口罩覆盖口鼻，双侧耳带接头后窄扣条
高鼻梁立体口罩佩戴|high-bridge shaped mask worn|三分之四脸，白色高拱鼻梁立体口罩；颊侧压折线和耳挂清楚；不印认证文字
''','mask',['R91'])

covers('防毒面具与呼吸器佩戴','''
双滤盒半面呼吸器正面|dual-cartridge half-face respirator front|正面，灰色半面体覆盖鼻口下巴；左右两只对称短滤盒；后脑双带连接；眼睛露出
双滤盒半面呼吸器侧面|dual-cartridge half-face respirator profile|严格侧面，半面体盖住口鼻；近侧滤盒和后脑头带清楚，远侧滤盒仅露合理边缘
单滤盒半面呼吸器|single-cartridge half-face respirator|三分之四脸，半面体覆盖口鼻，下前方一只短滤盒；后脑固定带；眼睛露出
低轮廓半面呼吸器|low-profile half-face respirator|正面，紧凑灰色半面体，左右扁滤盒贴近面颊下缘；后脑固定带清楚
双圆片半面呼吸器|round-filter half-face respirator|三分之四脸，半面体两侧安装扁圆滤片；中部有短圆形呼气阀外壳；头带可见
前置滤罐整面防毒面具|front-canister full-face gas mask|正面，整面体覆盖完整脸部；大透明眼窗保留正常眼睛；下前方一只短滤罐；后脑头带
侧置滤罐整面防毒面具|side-canister full-face gas mask|三分之四脸，整面体有完整透明眼窗；仅佩戴者左下侧一只滤罐；另一侧平封盖；头带清楚
双滤盒整面防毒面具|dual-cartridge full-face gas mask|正面，完整大眼窗整面体；左右下侧各一只对称短滤盒；五点头带连接清楚
全景眼窗整面呼吸器|panoramic-visor full-face respirator|三分之四脸，单片宽大弧面透明眼窗覆盖双眼鼻上部；口鼻内杯与下方滤罐连接
双眼窗复古防毒面具|twin-eyepiece vintage gas-mask prop|正面，灰黑复古道具面具；左右独立圆透明眼窗；下方短滤罐；橡胶面体与头带清楚
双眼窗面具侧面|twin-eyepiece gas-mask profile|严格侧脸，近侧圆眼窗与下前方滤罐；面体沿额颊下巴贴合；后脑头带清楚
工业整面双滤片呼吸器|industrial full-face round-filter respirator|三分之四脸，大透明眼窗整面体；左右下侧两片扁圆滤片；普通固定头带
软管式整面呼吸器道具|hose-connected full-face respirator prop|三分之四脸，透明整面体；下方一根短波纹软管接画面下缘可见的小型腰挂盒上端；连接完整不悬空
带头盔整面呼吸器|full-face respirator with plain helmet|三分之四脸，普通无标记工作头盔下佩戴整面呼吸器；大眼窗和双侧短滤盒；固定点不穿插
护目镜加半面呼吸器|goggles plus half-face respirator|正面，独立透明护目镜在眼部，双滤盒半面体在口鼻；两组固定带分清、不穿过眼睛
科幻封闭面罩呼吸器|original sci-fi full-face respirator|三分之四脸，原创灰白整面外壳、大透明眼窗和下方滤盒；无发光眼珠或品牌标记
''','respirator',['R91'])

covers('一般装饰面具佩戴','''
素白整面面具佩戴|plain white full-face mask worn|正面，素白整面硬质面具，正常双眼孔与小鼻口轮廓；颊侧固定带可见
双眼舞会面具佩戴|masquerade eye mask worn|正面，黑色上半脸舞会面具覆盖眼眶至鼻梁；口鼻下半部露出；头后细带固定
左半脸面具佩戴|left-half face mask worn|正面，佩戴者左半脸覆盖浅灰面具；右半脸露出；中线与侧边固定带清楚
右半脸面具佩戴|right-half face mask worn|正面，佩戴者右半脸覆盖深灰面具；左半脸露出；眼孔与侧边带清楚
下半脸装饰面具佩戴|lower-face decorative mask worn|三分之四脸，不透明灰色硬壳只覆盖鼻下至下巴；眼睛和上鼻梁露出；颊侧带固定
狐狸主题面具佩戴|fox-inspired decorative mask worn|正面，原创白色狐形整面道具面具；短狐耳与眼孔完整；正常成年头肩关系
猫形主题面具佩戴|cat-inspired decorative mask worn|三分之四脸，原创灰色猫形面具覆盖上半脸；小三角猫耳与侧边系带清楚；嘴部露出
兔形主题面具佩戴|rabbit-inspired decorative mask worn|正面，原创白色整面面具顶部两只短直兔耳；眼孔正常，全部耳尖在格内
鸟喙主题面具佩戴|short-beak decorative mask worn|严格侧脸，原创短鸟喙硬质道具面具、双眼孔和头后带；喙短小完整，不是防护器材
木质雕纹面具佩戴|carved-wood decorative mask worn|三分之四脸，棕色木质整面面具；原创浅雕线纹、双眼孔；颊侧布带固定
陶瓷裂纹面具佩戴|ceramic crackle mask worn|正面，奶白陶瓷整面面具；只有釉面浅裂纹装饰，完整不破损；眼孔与侧带清楚
金属镂花面具佩戴|filigree metal eye mask worn|三分之四脸，银灰金属镂花上半脸面具；眼孔与鼻梁支点清楚；口部露出
素色戏剧面具佩戴|plain theatrical mask worn|正面，原创米白整面戏剧道具面具；嘴部为小开口；不抄现有角色面谱
织物包覆面具佩戴|fabric-covered structured mask worn|三分之四脸，完整硬质整面面具外包深灰织物，双眼开孔和鼻形明显；后脑带清楚
几何分片面具佩戴|geometric segmented mask worn|正面，灰白几何分片构成完整整面道具面具；正常双眼孔与侧边带；没有机械义眼
额上抬起面具佩戴|decorative mask raised to forehead|三分之四脸，素白整面道具面具抬至额上并由头带固定，成年完整脸部露出；不是手持
''','decorative',['R03','R63'])

assert sum(bool(e.get('body_shape_reference')) for e in CATALOG)==32
assert sum(bool(e.get('stage_family_reference')) for e in CATALOG)==64
assert sum(bool(e.get('face_cover_reference')) for e in CATALOG)==48
