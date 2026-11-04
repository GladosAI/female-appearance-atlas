"""V34: hair surfaces, nuanced colors, facial acting and complete cosmetic looks."""
from catalog_content import CATALOG,add

def block(category,dimension,kind,text):
    start=len(CATALOG);add(category,dimension,text)
    assert len(CATALOG)-start==16
    for entry in CATALOG[start:]:
        entry.update(added_in='34.0',beauty_expansion_reference=True,beauty_kind=kind,adult_only=True,minor_reference=False,age_min=25,
                     note='原创成年角色外观参考。比较图例中的发束、颜色分区或眉眼口型与妆面落色；外观是角色设计标签，保留个体差异。')

block('hair_surface','发丝质地、粗细与蓬松层次','hair_texture','''
细软贴服直发|fine flat straight hair|发丝纤细、发根贴近头部，长直发束轻薄顺落，轮廓窄而柔软。
细软轻飘碎发|fine airy flyaway hair|浅细发丝松散飘离主发束，发缘有轻薄毛羽，整体通透轻盈。
粗硬直立短发|coarse upright short hair|粗硬短束在头顶向上支起，侧缘短而清楚，保持明显支撑感。
粗厚饱满直发|thick heavy straight hair|直发由粗厚束群形成饱满体积，发尾厚实，外缘清楚而不飘散。
丝缎柔亮发束|satin-soft hair sheen|中长发顺着柔和弧面落下，表面是一条宽而柔的丝缎亮带。
镜面顺直光泽|glass-straight glossy hair|整齐长直发有边缘清晰、连续平直的高光带，发缘非常平滑。
柔雾哑光发质|soft matte hair finish|中长发只有柔弱漫反射，发束层次清楚，没有锐利镜面光条。
蓬松棉感卷发|cottony fluffy curls|细小卷束堆叠出轻软蓬松体积，发缘有少量细毛，轮廓柔圆。
毛羽外散发缘|frizzy halo hair edge|主体自然波浪，外围细碎发丝向外散开，出现毛羽光晕般的边缘。
根部蓬松轻层发|airy lifted-root layers|头顶发根撑起空气层，耳侧与发尾分成轻薄小束，体积不压向头皮。
厚重垂坠发片|dense weighty hair panels|长发像厚发片沿肩部垂下，分缝少，发尾有明确重量与低垂弧度。
细密弹簧卷纹|fine spring-coil texture|细小紧密的弹簧卷保持独立圈形，卷群密度均匀，边缘可辨单个小卷。
粗束绳状卷纹|chunky rope-like curls|宽而连续的粗卷束向下盘旋，卷束之间有明显间隔，区别于细碎紧卷。
自然混合波卷|mixed loose-wave textures|同一头发中混合松S波、少量直束和小弯发尾，保留有规律的自然差异。
碎层羽毛感发尾|feather-light layered ends|上层较顺，末端切成很多细薄层次，发尾像羽毛般向外轻轻分散。
低密度透隙发束|low-density separated strands|成年中长发束之间可看到少量背景缝隙，分线较宽，轻量发尾不画成厚发片。
''')
block('hair_surface','自然色阶与染色细分','hair_color','''
蓝黑冷光发色|blue-black cool hair|主体近黑，亮部出现低饱和冷蓝，暗部保持深黑，区别于纯蓝发。
浓咖啡冷棕发|cool espresso brown hair|深咖啡底色带冷灰反光，阴影接近黑色，亮部仍能看出棕调。
暖巧克力棕发|warm chocolate brown hair|中深巧克力棕带温暖红金反射，色调浓郁而不变成红发。
灰橄榄棕发|muted olive-ash brown hair|棕色中混有低饱和灰绿调，整体雾感冷静，不是鲜绿色染发。
奶茶米棕发|milk-tea beige brown hair|浅米棕柔和低饱和，亮部偏奶油色，暗部保持浅灰棕。
蜂蜜焦糖棕发|honey caramel brown hair|暖棕底上有细长蜂蜜金高光束，主色与亮色交替过渡。
铜橘红发|copper-orange hair|铜红中有清楚橘调高光，发束在阴影处变成深铜棕，区别于酒红。
深莓酒红发|deep berry burgundy hair|深红发带紫莓色反射，主体偏暗，明部仍保持红紫而非铜橙。
亚麻灰金发|flaxen ash-blonde hair|浅金色混柔灰米色，不带明显橙黄，发根稍深形成轻微层次。
铂金冷白发|platinum cool-white hair|高明度冷白金色，细束阴影为淡灰紫，高光接近白色。
灰粉玫瑰发|dusty rose-pink hair|低饱和玫瑰粉混灰色，发束暗部有灰莓调，整体柔和不鲜艳。
烟紫薰衣草发|smoky lavender hair|灰紫色主体配淡薰衣草高光，颜色低饱和，保持清楚冷紫层次。
烟蓝灰发|smoky blue-grey hair|蓝灰色长发从深石板蓝阴影过渡到雾蓝亮部，避免霓虹饱和蓝。
雾青薄荷发|muted mint-teal hair|低饱和薄荷青绿色，暗部偏灰青，高光偏浅薄荷。
银黑细丝交混发|salt-and-pepper interwoven hair|黑发与银白细丝均匀交错，不是左右分区，发缘也能看出白黑混合。
珍珠多色偏光发|pearl pastel iridescent hair|珍珠浅色底发在不同发束反射淡粉、淡蓝与淡紫，保留真实发束纹理。
''')
block('expression','凝视与憋笑','gaze_laugh','''
平静正面凝视|calm direct gaze|成年正脸直视前方，双眼自然睁开，眉位放松，嘴唇轻闭。
专注前倾凝视|intensely focused gaze|头略向前，眉头轻收，视线固定在正前方，嘴唇收紧但不愤怒。
冷静侧目凝视|cool sideways gaze|脸朝前而双眼看向侧方，眼睑略压低，嘴角平直，目光方向明确。
低头抬眼凝视|upward gaze beneath lowered head|下巴微收而眼睛向上看，眉眼间距略收，双眼仍聚焦同一方向。
抬头垂眼凝视|downward gaze from raised chin|下巴轻抬而眼睛下望，上睑微压，嘴唇平静闭合。
温柔含笑凝视|gentle smiling gaze|眼睑柔和微弯，目光稳定直视，嘴角只是很轻的温暖弧度。
警惕眯眼凝视|vigilant narrowed gaze|双眼轻眯，眉心略聚，视线紧盯侧前方，嘴唇平直，面部不夸张变形。
出神远望凝视|distant thoughtful stare|眼睛平稳看向画外远方，眼睑略松，眉尾舒展，嘴唇自然留小缝。
抿唇憋笑|pressed-lip suppressed laughter|嘴唇紧抿成浅弧，嘴角努力向上但被压住，眼角已有微小笑纹。
鼓颊憋笑|puffed-cheek held-in laugh|双颊微鼓，闭嘴忍住笑意，眼睛眯起，眉毛轻抬，不能画成生气鼓嘴。
捂嘴憋笑|hand-covered suppressed laugh|一只正常五指手轻遮嘴，下方嘴角上扬，双眼弯起，脸颊略抬。
咬住下唇忍笑|lower-lip held-back laugh|上齿轻压下唇中部以忍笑，眼角带明显笑意，表情轻松而非紧张。
闭眼努力憋笑|eyes-shut holding back laughter|双眼笑得闭起，嘴唇仍紧闭，嘴角向两侧拉开，面颊抬高。
侧头躲开憋笑|turning away to hide a laugh|头转向侧方，余光仍看向画面，闭唇嘴角上扬，一侧面颊鼓起。
鼻翼紧绷忍笑|nose-tensed suppressed chuckle|嘴唇压紧，鼻翼轻轻绷起，脸颊上抬，眼睛明显带笑意。
差点笑出声|almost bursting into laughter|嘴角已失守微开一小缝，眉毛抬起，笑眼挤成弧线，处于憋笑将破的瞬间。
''')
for index,entry in enumerate(CATALOG[-16:]):
    entry['dimension']='凝视与目光方向' if index<8 else '憋笑与忍笑变化'
block('expression','日常情绪与细微表情','micro_expression','''
松口气的浅笑|relieved small smile|眉心松开，眼睑轻落，嘴角缓慢上扬，表现紧张结束后的放松。
尴尬礼貌微笑|awkward polite smile|嘴角勉强对称上扬，但眉毛内侧略抬，眼神避开正前方。
半信半疑挑眉|skeptical raised-brow look|一侧眉高挑、另一侧轻压，双眼斜看，嘴角保持平直。
无奈摊眉苦笑|resigned wry smile|眉毛内侧略抬、眼睑放松，嘴角一侧上扬成无奈浅笑。
安心闭眼微笑|reassured closed-eye smile|双眼自然闭合，眉线舒展，嘴角对称柔和上扬。
欣慰含泪微笑|tearful proud smile|眼里少量泪光但不流大泪，眉眼柔和，嘴角带温暖笑意。
认真等回答|patient attentive waiting|头轻偏向一侧，眉毛略抬，双眼专注对方，嘴唇轻闭等待。
欲言又止犹豫|hesitating before speaking|嘴唇微开后收住，眉内侧轻聚，视线略偏，面部保持克制。
恍然大悟一瞬|moment of realization|眉毛向上舒展，眼睛突然明亮，嘴形成小幅圆口而非惊恐。
压住不满的微笑|strained smile hiding annoyance|嘴角有礼貌弧线，眼睑略压低，眉心轻收，表现克制的不满。
期待被夸奖|hopeful for praise|眉线轻抬，双眼直视略带亮光，嘴唇抿成小小期待弧度。
受到称赞的羞笑|bashful smile after praise|脸颊浅红，眼睛向旁边看，嘴角轻轻上扬，下巴略收。
不服气侧眼|unconvinced sidelong look|一边眼睑略低，眉峰轻挑，嘴角偏向一侧，视线斜看。
认真自我鼓劲|quiet self-encouragement|眉毛内侧略收，眼神稳定，嘴唇紧抿成坚定的小弧线。
懒洋洋淡笑|languid relaxed smile|眼睑轻垂、眉毛放松，嘴角形成很浅的笑意，头部自然偏斜。
听到笑话后的停顿|processing a joke|眉毛轻抬，嘴角刚开始上扬，双眼先显惊讶再出现笑意的过渡瞬间。
''')
block('expression','底妆、腮红与唇妆组合','everyday_makeup','''
清透雀斑裸妆|sheer freckled natural makeup|保留自然小雀斑，浅棕眉、透明裸粉唇与极轻腮红，底妆轻薄。
柔雾米杏妆|soft-matte beige-apricot makeup|底妆呈柔雾质感，米杏眼影配浅杏腮红和柔棕粉唇，色区克制。
水光桃粉妆|dewy peach-pink makeup|颧骨与鼻梁有小范围柔亮水光，蜜桃眼影、粉桃腮红与透明亮唇。
冷调灰玫瑰妆|cool dusty-rose makeup|灰玫瑰眼影与腮红呼应，眉色冷棕，嘴唇为低饱和玫瑰豆沙色。
暖棕焦糖妆|warm caramel-brown makeup|暖棕眼影、焦糖色面颊过渡与棕橘唇妆形成统一暖调，完整眉形自然。
豆沙低饱和妆|muted mauve-bean makeup|眼周与唇部为低饱和豆沙粉棕，腮红较淡，整体柔和不闪亮。
日晒横扫腮红妆|sun-kissed across-nose blush|暖珊瑚腮红从双颊上部连过鼻梁，眼妆轻量，唇色自然裸橘。
高位蜜桃腮红妆|high-placed peach blush|腮红集中在眼下外侧至颧骨的较高位置，蜜桃唇与细棕眼线配合。
低位横向腮红妆|low horizontal blush placement|腮红主要横向分布于面颊中下部，眼下留干净肤色，唇为柔粉色。
斜向提拉腮红妆|diagonally lifted blush makeup|低饱和玫瑰腮红沿颧骨斜向太阳穴过渡，配细上扬眼线与雾面唇。
奶茶棕裸唇妆|milk-tea brown nude-lip makeup|奶茶棕雾面唇为重点，眼周浅棕、腮红极淡，唇形边缘清晰柔和。
莓果内深渐变唇妆|berry-centered gradient lip makeup|嘴唇中心为深莓色，向唇缘渐淡，眼影浅粉棕，面颊只留微弱粉色。
镜面果冻亮唇妆|glossy jelly-lip makeup|透明粉红唇有清楚镜面反射与厚润光泽，眼妆为轻量裸棕。
丝绒红唇淡眼妆|velvet red lips with subtle eyes|完整丝绒红唇边缘明确，眼影很淡，睫毛分离，面颊仅轻微修饰。
微光香槟高光妆|subtle champagne-highlight makeup|香槟细光集中在颧骨、眉骨和鼻尖，裸粉唇、浅棕眼影，其余肤面柔雾。
深肤金铜日常妆|gold-copper makeup on deep skin|成年深棕肤色，金铜上眼睑、温暖莓棕腮红与棕红亮唇，保留深肤层次。
''')
block('expression','风格妆面与创意彩妆','creative_makeup','''
复古细翼正红唇妆|vintage wing and red-lip makeup|黑色细长上扬眼线、明确弧眉、正红饱满唇，底妆柔雾，腮红克制。
巧克力棕唇烟熏妆|chocolate-lip smoky makeup|深棕柔烟熏眼周搭配巧克力雾面唇，轮廓清楚，不涂整片黑色眼罩。
银灰冷光晚宴妆|silver-grey evening makeup|银灰眼影与细黑眼线、冷粉颧骨高光、浅灰玫瑰唇相配，完整脸部。
酒红浆果晚妆|burgundy-berry evening makeup|酒红眼影集中在眼尾，深浆果唇与低饱和莓色腮红形成协调。
祖母绿宝石妆|emerald jewel-tone makeup|上眼皮以祖母绿为主，眼尾深绿、细金点亮眼头，唇为清淡裸色。
钴蓝锐线舞台妆|cobalt graphic stage makeup|钴蓝色上眼线拉长成锐利折角，少量同色下眼尾，裸粉唇与干净底妆。
紫金对照舞台妆|violet-gold stage makeup|紫色眼尾与金色眼皮中央形成对照，配深玫瑰唇，保留完整眉眼结构。
白色睫毛冰晶妆|white-lash frost-inspired makeup|白色上睫毛、浅蓝银细光眼影与冷粉唇，鼻梁和颧骨少量细亮点。
彩色渐层眉妆|pastel-gradient eyebrow makeup|眉毛从浅粉逐渐变淡紫，眼妆与唇妆简洁，让彩眉结构清楚可见。
太阳穴珠点妆|temple pearl-dot makeup|眼尾到太阳穴排列少量小珍珠装饰，暖棕眼影、豆沙唇，不覆盖眉眼。
眼下星点亮片妆|under-eye star-glitter makeup|眼下外侧点缀少量星形与小点亮片，眼影浅紫，嘴唇淡粉，亮片位置清晰。
几何半框眼周妆|geometric half-frame face makeup|一侧眼外画细线几何半框，另一眼保留普通眼线，唇色简单，属于原创创意妆。
柔色水彩面颊妆|watercolor pastel-cheek makeup|浅粉、淡蓝与淡紫在双颊边缘柔和交叠，保留中央肤色，眼唇妆轻量。
双色拼接唇妆|two-tone split lip makeup|上唇为深莓色、下唇为柔粉色，边界清楚，眼影淡棕，面部正视。
金箔局部点缀妆|small gold-leaf accent makeup|一侧颧骨外缘贴少量不规则金箔薄片，棕金眼影、裸红唇，其余皮肤干净。
泪滴水钻编辑妆|teardrop rhinestone editorial makeup|双眼下方各有一枚小泪滴水钻，浅香槟眼影与灰玫瑰唇，非真实泪痕。
''')
