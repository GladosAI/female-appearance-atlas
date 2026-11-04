"""V33: worn eye-shadow, liner and coordinated eye makeup references."""
from catalog_content import CATALOG,category,add
NEW_CATEGORIES=['eyeshadow','eyeliner','eye_makeup']
for cid,name,guide,refs in [
 ('eyeshadow','眼影与晕染','16种眼影落色、层次与质感参考。单眼近景比较眼窝、眼尾、上下眼睑、截断式边界，以及哑光、细珠光、金属和亮片。虹膜与妆色分开观察。',['R107']),
 ('eyeliner','眼线与眼尾画法','16种眼线轮廓参考，比较贴根细线、粗细、延长方向、上扬下垂、双尾、留白与悬浮线；单眼近景保留内外眼角和完整眼尾。',['R106']),
 ('eye_makeup','完整眼妆组合','16种搭配眼影、眼线与睫毛的完整眼妆近景，含日常裸棕、玫瑰蜜桃、烟熏、复古、哥特与舞台图形。使用同一双眼视角比较整体配合。',['R106','R107'])]:
    category(cid,name,guide,refs)

def examples(cid,dimension,text):
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==16
    for name,en,placement,finish,description in rows:
        add(cid,dimension,f'{name}|{en}|{description}。')
        CATALOG[-1].update(added_in='33.0',eye_makeup_reference=True,eye_makeup_kind=cid,makeup_placement=placement,makeup_finish=finish,makeup_view='双眼正面近景' if cid=='eye_makeup' else '单眼正面近景',adult_only=True,minor_reference=False,age_min=25,
            note='原创成年角色眼部彩妆参考。观察落色边界、软硬过渡、眼角方向和睫毛线条，虹膜保持自然棕色以减少比较干扰。眼影页、眼线页与完整眼妆页分别聚焦颜色层次、线形与组合效果；图例是造型示意，效果因眼部结构而异。')

examples('eyeshadow','眼影落色、晕染与质感','''
裸棕轻雾平涂眼影|sheer nude-brown lid wash|上眼睑整片|轻雾哑光|浅裸棕均匀铺在上眼睑，边缘柔和，眉骨与下眼睑保留干净肤色，不画明显眼线
眼窝弧形加深眼影|crease-defined eyeshadow|眼窝弧线|哑光渐层|中棕沿眼窝形成柔和弧形带，活动眼皮较浅，向眉骨自然淡出
眼尾外V加深眼影|outer-V eyeshadow|眼尾外侧V区|深浅哑光|外眼角的上睑与眼窝交成深棕V形，内侧眼皮浅米色，边缘晕开
中央提亮光环眼影|halo eyeshadow|内外眼睑深色与中央亮区|柔光对照|内眼角与外眼尾各有深棕色，中部留一块清楚的浅香槟亮区，向两侧衔接
横向浅深渐变眼影|inner-to-outer gradient shadow|眼头至眼尾|哑光渐变|内眼角浅米色过渡到中央暖棕，再到眼尾深巧克力色，沿横向连续变化
纵向烟雾渐变眼影|lash-to-crease gradient shadow|睫毛根至眼窝|柔雾渐层|靠近上睫毛线是深灰棕，向眼窝逐渐变浅，形成从下到上的柔雾，不画硬截断
全截断眼窝眼影|full cut-crease eyeshadow|整条眼窝与活动眼皮|清晰截断|深棕眼窝弧带下缘是一道干净的弧形边界，整片活动眼皮为浅奶油色，边界与睫毛线分开
半截断眼窝眼影|half cut-crease eyeshadow|内侧半片活动眼皮|半硬半软边界|眼皮内侧半片为浅奶油色截断区域，眼尾深棕保留柔和晕染，形成一半清晰一半烟雾
下眼尾三角晕染眼影|lower-outer triangle shadow|下眼尾小三角区|轻雾哑光|上眼睑仅淡裸色，下眼睑外侧三分之一有小棕色三角晕染，与眼尾相接而不铺满眼下
眼头香槟提亮眼影|champagne inner-corner highlight|内眼角及相邻上睑|细珠光|小范围香槟珠光集中在眼头，活动眼皮其余部分为浅棕，不把整只眼或虹膜变亮
玫瑰哑光单色眼影|matte rose monochrome shadow|活动眼皮与眼窝边缘|细腻哑光|低饱和玫瑰粉铺满活动眼皮，眼窝边缘略深，表面呈干净细腻的柔雾
香槟细珠光眼影|fine champagne shimmer shadow|活动眼皮中央至内侧|细珠光|浅香槟色有均匀细小反光，眼尾淡棕收边，珠光细腻连续
铜金金属光眼影|copper metallic eyeshadow|活动眼皮整片|金属箔光|铜金色在活动眼皮形成连贯金属反光面，边缘暖棕晕开，金属色不进入虹膜
稀疏亮片点缀眼影|scattered glitter eyeshadow|上眼皮中央|离散亮片|浅裸棕底上有少量分离的银金亮片，颗粒疏密清楚，与细珠光的连续反光区别明显
蓝紫双色晕染眼影|blue-violet two-tone shadow|内蓝外紫的上眼睑|彩色柔雾|活动眼皮内侧为蓝色、外侧为紫色，中段柔和衔接，眉骨留白且虹膜仍为自然棕色
几何色块图形眼影|geometric color-block shadow|眼窝上方与外侧|哑光硬边|上眼睑橙色块带有清楚平直折角与外侧几何边界，少量肤色留白，不采用烟雾渐层
''')
examples('eyeliner','眼线粗细、方向与图形','''
睫毛根贴根眼线|tightline lash-root definition|上睫毛根部|极细棕黑线|颜色集中在上睫毛根部，几乎没有超出根部的色带，也没有眼尾延长，轮廓自然
完整上睑细眼线|thin full upper eyeliner|上睫毛线全段|清晰细线|一条可见的细黑线从内侧沿上睑到外角，始终细而均匀，眼尾不伸出
加粗上睑眼线|thick upper eyeliner|上睫毛线上方|清晰粗线|上睑黑色带明显宽于普通细线，中央和外侧较厚，眼窝区域不涂黑
外半段眼线|outer-half eyeliner|上睑外侧一半|局部细线|内侧半段保持无眼线，只有外侧半段出现深棕线，止于外眼角
平拉短延长眼线|short horizontal extension liner|眼尾水平外延|细线短尾|上睑细线在外眼角沿近水平线向外延长一小段，末端尖细而不上翘
微上扬短尾眼线|short lifted wing liner|外眼角小上扬|短三角尖尾|上睑细线接一枚短而轻微上扬的尖尾，长度克制，区别于长猫眼
长尾猫眼眼线|long cat-eye wing liner|上睑与外侧长尾|清晰锐角|外眼角拉出较长上扬尖翼，外侧逐渐加宽后收尖，完整长翼留在画面内
下垂小狗眼线|downturned puppy liner|顺外眼角向下延伸|柔和短尾|眼尾沿上睑原本的下落弧度略向下延长，末端短柔，不画上扬猫眼
双尾分叉眼线|double-wing eyeliner|外眼角上下分叉|双细尖尾|上睑一条上扬尾与下眼尾短线在外侧分成两条清楚尖尾，中间留肤色缝隙
留白空心翼眼线|negative-space hollow wing|眼尾三角轮廓|空心图形|外眼角延长成细线勾出的空心三角翼，三角内部保留肤色，不能填成实心黑块
眼窝悬浮弧线|floating crease eyeliner|眼窝上方独立弧线|独立细弧|一条黑色弧线浮在上眼皮眼窝附近，与普通贴睫毛细线之间留明显肤色间隙
折线图形眼线|angular graphic eyeliner|上睑及眼尾外侧|锐角折线|普通上睑细线在眼尾外侧转成小折角几何线，轮廓由直线与尖角组成，不变成大面积眼影
棕色柔晕眼线|soft smudged brown liner|上睫毛线与短眼尾|柔边晕线|棕色眼线沿上睫毛线轻轻晕开，线边柔而有带状边界，眼窝不大面积染色
下眼尾三分之一眼线|outer-third lower liner|下睫毛线外侧|局部细线|下睫毛线只在外侧三分之一有细黑线，中段和眼头留空，上睑保留极淡贴根线
白色叠加点睛眼线|white accent over black liner|黑眼线上缘|黑白双层细线|细黑上睑眼线上缘叠一小段白色线，从中部至眼尾可辨两色，白色不涂入眼球
钴蓝彩色上眼线|cobalt blue upper liner|上睫毛线与短尾|纯色细线|钴蓝色代替黑色沿上睫毛线延伸成短尾，眼影为干净裸色，虹膜保持棕色
''')
examples('eye_makeup','眼影、眼线与睫毛组合','''
日常裸棕完整眼妆|everyday nude-brown eye makeup|双眼上睑与睫毛线|自然哑光|浅棕眼影、很细棕色眼线与自然分离睫毛共同呈现轻量日常效果，眼窝保留轻微层次
玫瑰单色完整眼妆|rose monochrome eye makeup|双眼眼皮与眼尾|柔雾玫瑰|低饱和玫瑰眼影、酒棕短眼线与纤细上睫毛色调协调，下眼睑仅淡粉过渡
蜜桃橘调完整眼妆|peach-orange eye makeup|双眼活动眼皮与下眼尾|柔光暖色|蜜桃至橘色的上眼皮渐变，眼尾棕色短线与自然睫毛相配，下眼尾有少量同色呼应
冷灰褐通勤眼妆|cool taupe workday eye makeup|双眼眼窝与上睫毛线|冷调哑光|灰褐色眼窝柔晕、细灰棕眼线和分离睫毛，整体克制，避免暖铜色或闪片
黑灰烟熏完整眼妆|black-grey smoky eye makeup|双眼上下睫毛周围|浓郁烟雾|黑色贴近上下睫毛根，向外渐变成灰色，配浓密上睫毛，眼窝边界柔和而非硬黑色块
柔棕烟熏完整眼妆|soft brown smoky eye makeup|双眼上下眼睑边缘|暖棕柔雾|深咖啡贴根色向外晕成暖棕，上下眼睑形成连贯柔影，睫毛清晰但不过分浓重
复古折线猫眼眼妆|retro mod crease-and-wing makeup|双眼眼窝弧线与眼尾|米色配黑线|浅米活动眼皮配独立眼窝深线、长黑猫眼与略分束睫毛，形成复古图形层次
酒红哥特完整眼妆|burgundy gothic eye makeup|双眼上下眼睑与长尾|深色哑光|深酒红眼影与黑色拉长眼线、浓密上睫毛配合，下眼尾深色呼应，保留棕色虹膜
舞台粉金闪片眼妆|pink-gold stage glitter makeup|双眼上睑及眼下局部|闪片与清晰睫毛|粉金眼影、小范围可辨亮片、上扬细线与有间隔的分束睫毛组合，成年舞台造型
金棕截断礼服眼妆|gold-brown formal cut-crease makeup|双眼活动眼皮与眼窝边界|金属光配硬边|深棕眼窝与金色活动眼皮之间有干净截断边界，配锐利短翼与长睫毛
青紫双色节庆眼妆|teal-violet festival eye makeup|双眼眼头眼尾与上睑|彩色柔光|青绿内眼皮过渡到紫色外眼尾，配深紫细眼线和黑色分离睫毛，左右采用相同搭配
白线图形编辑眼妆|white graphic editorial eye makeup|双眼眼窝外侧与上睑|白色图线与裸色底|裸色眼皮上有白色几何弧线与细黑贴根线，配简洁上睫毛，大部分肤色保持留白
金色双端拉长眼妆|gold elongated-corner eye makeup|双眼内外眼角延伸|金色配深黑线|金色眼皮搭配内眼角短尖与外眼角长尖黑线，形成两端延长轮廓；原创舞台灵感
青紫偏光完整眼妆|teal-plum duochrome eye makeup|双眼活动眼皮反光区|青紫偏光|梅紫底的活动眼皮在中央反射青绿色光，配短黑眼线与自然睫毛，表现妆面而非虹膜变色
落日橘紫完整眼妆|sunset orange-purple eye makeup|双眼上睑与眼尾|橘红紫渐变|内侧暖橙到中央红色再到外侧紫色形成落日渐变，配黑色小翼与纤长睫毛
蓝色睫毛点睛眼妆|blue-mascara accent eye makeup|双眼睫毛与极淡眼皮|裸色配蓝色睫毛|眼皮只有浅裸色、上睫毛根为极细棕线，睫毛本身为清楚钴蓝色，虹膜保留自然棕色
''')
