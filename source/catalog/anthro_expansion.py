"""Edition 16: original adult female kemonomimi/anthro morphology references."""
from catalog_content import CATALOG, category, add

ANTHRO_CATEGORIES=['anthro_levels','anthro_heads','anthro_parts','anthro_species']
LEGACY_ANTHRO_IDS={f'FX{i:03}' for i in [2,3,4,5,6,7,8,10,11,14,23,24,25,26,27,28]}
LEVELS=[
 {'id':1,'name':'人形兽耳','guide':'人脸、人手、人足，仅替换为一对动物耳，无尾巴。'},
 {'id':2,'name':'人形耳尾','guide':'保留人脸人手足，增加与身体相接的动物尾巴。'},
 {'id':3,'name':'局部皮毛','guide':'人脸轮廓保留，面颊与前臂出现局部被毛，手足仍偏人形。'},
 {'id':4,'name':'局部兽手兽足','guide':'人脸保留，手足成为拟人爪掌，四肢局部被毛。'},
 {'id':5,'name':'短吻兽脸','guide':'头部短吻与毛脸，躯干比例及手足仍以人形为主。'},
 {'id':6,'name':'完整兽头人形躯干','guide':'动物头部有完整吻部，身躯比例、人形手足仍保留。'},
 {'id':7,'name':'全身拟人兽型','guide':'兽头、全身被毛与爪掌，保持直立的人形躯干比例。'},
 {'id':8,'name':'偏兽体态直立','guide':'直立角色采用更明显动物头身比例与支撑轮廓，保留服装与操作能力。'}
]
SPECIES=[('猫','cat','灰色短毛、三角猫耳、细长猫尾'),('狐','fox','橙棕毛、黑耳尖、白尾尖蓬松尾'),('狼','wolf','灰毛、立耳、较厚直尾'),('兔','rabbit','奶白毛、长兔耳、圆短尾')]
EN_LEVELS=['human with animal ears','human with ears and tail','patch-fur human','human face with paw limbs','short animal muzzle','animal head with human body','full-fur humanoid','animal-proportioned biped']

category('anthro_levels','兽娘与福瑞程度对照','本图鉴8档创作标签，不是统一比例标准；头、耳尾、被毛、手足与体态可以独立组合。',['R69'])
category('anthro_heads','兽脸吻部与毛纹','按吻部长度、鼻垫、耳形、颊毛和面部毛纹比较；保留成年角色头部与完整耳根。',['R69','R70'])
category('anthro_parts','耳尾爪足与兽化肢体','比较自然耳尾根部、手掌、足部、蹄与鳞羽的幻想结构；肢体是创作改编，须保持关节和支撑连贯。',['R70','R72'])
category('anthro_species','兽娘与福瑞物种原型','哺乳类与鳞羽、水生、昆虫、幻想拟人原型分别整理；各为原创成年女性角色，物种形态与服装可另配。',['R69','R71'])

def block(key,dimension,text):
    start=len(CATALOG);add(key,dimension,text)
    assert len(CATALOG)-start==16,(key,dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e.update(age_context='成年女性幻想角色参考',anthro_reference=True)
        e['aliases']=['兽娘','福瑞','兽化','furry','anthro','kemono','拟人动物']

for group in [range(1,5),range(5,9)]:
    rows=[]
    for level in group:
        spec=LEVELS[level-1]
        for cn,en,features in SPECIES:
            name=f"兽化{level}档{spec['name']}·{cn}型"
            desc=f"成年女性{cn}型全身对照，{spec['guide']}{features}中仅采用本档出现的部件。组内穿近似普通高领长袖外套和直筒长裤；低档可穿普通鞋，局部兽化后手足轮廓可见，完整头耳与脚端。"
            rows.append(f"{name}|tier {level} {en}-type {EN_LEVELS[level-1]}|{desc}")
    start=len(CATALOG)
    block('anthro_levels','兽化1–4档人形与局部对照' if group.start==1 else '兽化5–8档兽脸与全身对照','\n'.join(rows))
    for e,(level,species) in zip(CATALOG[start:],[(level,species) for level in group for species in SPECIES]):
        e.update(anthro_level=level,anthro_species=species[1])
        e['aliases'] += [f'兽化{level}档',f'L{level}',LEVELS[level-1]['name'],species[0]+'型',species[1]]

block('anthro_heads','兽脸吻部与耳鼻轮廓','''
猫型短吻兽脸|short-muzzle feline face|成年女性拟人猫头近景，短吻、三角鼻垫、一对三角耳与短颊毛，普通高领衣边。
狐型尖吻兽脸|tapered fox muzzle face|成年女性拟人狐头三分视角，较尖吻部、黑鼻、立耳及白颊，完整颈领。
狼型长吻兽脸|long-muzzle wolf face|成年女性拟人狼头侧三分视角，完整长吻、鼻垫和厚颊毛，一对立耳。
犬型圆吻兽脸|rounded canine muzzle face|成年女性拟人犬头，圆钝吻部、鼻垫、一对垂耳，眼眉用于表情，完整头像。
兔型短吻兽脸|short-muzzle rabbit face|成年女性拟人兔头，小短吻、兔鼻、两只完整长耳，颊毛柔软，衣领完整。
猞猁耳簇兽脸|lynx tuft-ear face|成年女性拟人猞猁头，双耳尖有短毛簇，宽颊毛与短猫吻，一对真实耳。
狮型短颊鬃兽脸|lioness-inspired cheek-ruff face|成年女性狮型拟人头，圆耳、宽短吻和克制颊鬃，原创风格，不画雄狮大鬃。
虎型宽吻兽脸|broad-muzzle tiger face|成年女性拟人虎头，宽猫吻、圆耳和原创条纹，眼鼻口清楚。
熊型圆耳宽吻|round-ear bear face|成年女性拟人熊头，圆耳、宽鼻吻、厚颊轮廓，正常成熟头像。
小熊猫型兽脸|red-panda-inspired face|成年女性拟人头，红棕毛、白眉颊、圆三角耳与短吻，普通颈领。
浣熊型面罩毛脸|raccoon-mask fur face|成年女性拟人浣熊头，黑色眼周毛纹、一对圆耳、短鼻吻，不是佩戴面具。
水獭型圆短吻|otter rounded-short muzzle face|成年女性拟人水獭头，小圆耳、圆短吻、鼻垫与少量胡须毛，衣领完整。
鹿型长鼻兽脸|deer long-nose face|成年女性原创鹿型头，长鼻吻、大侧耳，额上无角的本例，头颈完整。
羊型横向耳兽脸|goat side-ear face|成年女性原创羊型头，细长吻、两侧耳与一对短弯角，角根完整。
马型长吻侧脸|horse long-muzzle side face|成年女性拟人马头侧面，长鼻吻、上立耳与后颈鬃，普通完整高领衣边。
鼠型细鼻兽脸|mouse fine-nose face|成年女性拟人鼠头，圆大耳、小鼻尖、短胡须毛，非幼态比例，完整颈领。
''')

block('anthro_heads','面部被毛纹理与分区','''
短顺毛兽脸|short-smooth fur face|成年女性拟人猫脸，短顺毛边与细微毛向，鼻吻清楚，简洁衣领。
厚颊毛兽脸|thick cheek-fur face|成年女性拟人狼脸，两侧厚颊毛呈连续束状边，完整长吻与耳根。
额前毛旋兽脸|forehead fur-whorl face|成年女性拟人犬脸，额前小毛旋绕连续生长点，鼻与眼睛完整。
前额短鬃兽脸|short forehead-mane face|成年女性拟人兽脸，额前一束短直鬃连到头顶，其余短毛，衣领完整。
鼻梁深毛分区|dark nose-bridge fur zone|成年女性拟人狐脸，深色毛沿鼻梁到额前，两颊浅色，分区不是面部彩绘。
白吻深颊毛分区|white muzzle dark-cheek fur|成年女性拟人犬脸，吻部白毛、颊部深棕毛，鼻垫与毛边完整。
浅眉眼周毛分区|pale-brow eye-fur markings|成年女性拟人兽脸，双眼上方浅毛斑与深色周围对照，眼睛正常完整。
眼周面罩毛分区|eye-mask fur markings|成年女性浣熊型头，双眼周围真实深毛带与浅毛额颊，不是眼镜或面罩。
虎条纹面部毛区|tiger-stripe facial fur|成年女性虎型头，额颊原创短条纹随脸体积转，完整耳与短吻。
豹玫瑰斑面部毛区|rosette-marked facial fur|成年女性豹型拟人头，颊额原创小玫瑰斑，鼻吻与眼睛不被图案遮住。
雀斑式斑点毛区|small spotted fur-face zone|成年女性拟人鹿型脸，额颊少量浅毛小点，完整鼻吻与侧耳。
左右异色毛脸|two-tone asymmetric fur face|成年女性拟人猫头，一侧浅灰、一侧深灰毛区，毛界自然，双眼与鼻吻完整。
背深腹浅头颈毛区|dark-top pale-neck fur|成年女性拟人狐头，头顶深毛、下颌和外露上颈浅毛，高领遮住胸部。
耳内绒毛近景|inner-ear fur close-up|成年女性兽耳头像，完整一对三角耳，内侧短绒和外侧长毛边区分，正常耳根。
胡须垫与短须毛|whisker-pad facial detail|成年女性拟人猫头三分近景，鼻两侧须垫与数根短须，正常完整口鼻。
眉颊长毛混合|mixed brow-cheek fur lengths|成年女性拟人兽脸，眉上短毛、颊侧长毛，毛向沿脸体积，耳与吻部清楚。
''')

block('anthro_parts','自然耳角尾与附肢根部','''
三角猫耳自然耳根|natural triangular cat ears|成年女性人形头像只有一对猫耳，完整耳根从头部生长，侧面不另露人耳，普通高领衣边。
高位狐耳自然耳根|natural high-set fox ears|成年女性人形头像只有一对高位狐耳，耳内绒毛、黑尖与连续根部，非发箍道具。
狼型立耳耳根|wolf upright-ear roots|成年女性人形狼耳头像，一对立耳连头部，耳背毛向清楚，不添加第二对人耳。
犬型垂耳耳根|canine floppy-ear roots|成年女性人形犬耳头像，一对垂耳从两侧固定耳根垂下，完整耳端与衣领。
兔型长直耳根|rabbit straight long-ear roots|成年女性人形兔耳头像，一对长直耳与头顶自然相接，耳端全部在画面内。
兔型一垂一直耳|rabbit one-lop one-upright ears|成年女性人形兔耳头像，一耳直立、一耳软垂，完整两耳根与耳端，原创不对称例。
猫尾与尾口连接|cat tail and garment opening|成年女性腰至脚后侧图，直筒长裤尾口处猫尾自然连到尾根，完整细尾端，非腰带挂饰。
狐蓬尾与尾根|fox bushy-tail root|成年女性穿长裤后侧完整下半身，单条大蓬尾连到骨盆尾根，从尾口露出，尾端完整。
狼厚尾与尾根|wolf thick-tail root|成年女性后侧下半身，长裤尾口露一条中等厚毛尾，腰裤完整，尾端不截断。
兔圆尾与尾根|rabbit round-tail root|成年女性长裤后侧下半身，一枚小圆尾自然接尾口，完整腰腿与脚部。
鹿型双耳短角根|deer-style ear and short-antler roots|成年女性原创鹿型头像，两侧耳与一对短分枝角分别有完整根部，角形属幻想改编。
羊型双耳短角根|goat-style ear and short-horn roots|成年女性原创羊型头像，一对短弯角加一对侧耳，耳与角不混为同一根结构。
爬虫鳞尾连接|scaled reptile-tail attachment|成年女性拟人爬虫腰至脚后图，裤尾口露一条连续鳞尾，完整尖尾端，正常服装。
鸟型羽尾连接|avian feather-tail attachment|成年女性拟人鸟角色后侧下半身，长裤尾口露扇状羽尾，羽根与羽层清楚，非裙饰。
龙型膜翼根部|dragon membrane-wing roots|成年女性原创龙型角色背面上半身，宽松完整外套翼口露一对膜翼，翼根与支骨连续。
昆虫薄翼根部|insect thin-wing roots|成年女性原创昆虫拟人角色背面上半身，完整外套翼口露一对薄翼，翼脉和胸背根部清楚。
''')

block('anthro_parts','拟人爪掌蹄足与支撑','''
五指人手带肉垫|five-digit hand with paw pads|成年规格完整手与袖口，四长指加一拇指、掌和指端小肉垫，手仍偏人形，非手套。
五指短爪毛手|five-digit short-claw fur hand|成年规格带袖口的完整毛手，四长指加可对向拇指，五指端各短爪，指掌连接正常。
圆爪掌拟人手|rounded anthropomorphic paw-hand|成年规格完整圆爪掌和袖口，四指圆爪掌、四枚指垫与掌垫清楚，幻想操作型手。
细长指鳞手|slender scaled five-digit hand|成年规格袖口外完整鳞手，四长指加拇指、五短爪，鳞片沿关节完整铺排。
鸟型羽腕操作手|avian feather-wrist hand|成年规格完整操作手与袖口，四指加拇指，腕侧短羽与五个短指爪，原创拟人改编。
熊型厚掌毛手|bear-style thick fur hand|成年规格完整厚毛手、四粗指与一拇指，掌垫和短爪清楚，袖口连接正常。
猫型跖行爪足|feline plantigrade paw feet|成年规格穿不透明长裤的双小腿与完整爪足，脚跟较低、足掌整体支撑，原创拟人脚。
犬型趾行爪足|canine digitigrade paw feet|成年规格长裤下露双腿侧三分图，踝跟抬高、脚趾与爪掌着地，膝不向后反折，完整地面支撑。
狼型高踝趾行腿|wolf high-hock digitigrade legs|成年规格从大腿到脚的侧面图，不透明裤装，膝、踝跟与趾部依次连贯，踝跟高而前爪着地。
兔型长后足支撑|rabbit long-hindfoot support|成年规格穿裤的双小腿，长毛后足向前延伸、脚跟较低，完整脚端与地面。
鹿型双趾蹄足|deer-style split-hoof feet|成年规格裤装下半腿与双足，每足一枚分成两瓣的蹄，蹄端着地，完整足腿。
马型单蹄足|horse-style single-hoof feet|成年规格裤装下半腿侧三分图，每足一枚完整单蹄，蹄缘与腿连续，不画鞋。
爬虫型四趾足|reptile-style four-toe feet|成年规格裤装下半腿与两只完整幻想爬虫足，每足四根有短爪趾，鳞面完整。
鸟型三前一后趾足|bird three-front-one-back toes|成年规格裤装下半腿与鸟足，每足三前趾一后趾，完整趾爪和地面支撑，原创拟人形。
趾行侧面站姿|digitigrade side standing pose|成年女性兽型全身侧面，完整高领外套与长裤，脚趾着地、踝跟离地，膝正常方向，尾端完整。
跖行正面站姿|plantigrade front standing pose|成年女性兽型全身正面，完整外套与长裤，双足掌着地、脚跟较低，尾与头耳完整。
''')

block('anthro_species','哺乳类成年女性兽型原型','''
灰猫全身福瑞原型|gray-cat adult female anthro|完整成年女性灰猫型，兽头与短吻、全身灰毛、爪掌、猫尾，普通高领长袖衬衫与长裤。
橙狐全身福瑞原型|orange-fox adult female anthro|完整成年女性狐型，尖吻、黑耳尖、白尾尖蓬尾、爪掌，普通长袖夹克和长裤。
灰狼全身福瑞原型|gray-wolf adult female anthro|完整成年女性狼型，长吻、灰颊毛、直尾与拟人爪足，普通高领外套和长裤。
垂耳犬福瑞原型|floppy-eared dog adult female anthro|完整成年女性犬型，垂耳、圆吻、粗尾与跖行爪足，普通长袖衣和长裤。
长耳兔福瑞原型|long-eared rabbit adult female anthro|完整成年女性兔型，长耳短吻、圆尾与长后足，普通长袖外套和长裤。
耳簇猞猁福瑞原型|tuft-eared lynx adult female anthro|完整成年女性猞猁型，耳簇、宽颊毛、短尾与爪足，普通长袖夹克及长裤。
母狮型福瑞原型|lioness-inspired adult female anthro|完整成年女性狮型，圆耳、宽短吻、短颊毛和穗尾，普通长袖外套长裤，非雄狮大鬃。
虎条纹福瑞原型|tiger-striped adult female anthro|完整成年女性虎型，兽头、原创条纹毛区、长尾与爪足，普通长袖衬衣及长裤。
豹斑福瑞原型|rosette-leopard adult female anthro|完整成年女性豹型，短猫吻、原创玫瑰斑、长尾，完整长袖外套与长裤。
圆耳熊福瑞原型|round-ear bear adult female anthro|完整成年女性熊型，厚颊宽吻、圆耳、短尾与大跖行足，宽松长袖外套长裤。
小熊猫福瑞原型|red-panda adult female anthro|完整成年女性小熊猫型，红棕毛、白颊、环纹长尾，普通完整长袖外套与长裤。
面罩浣熊福瑞原型|mask-marked raccoon adult female anthro|完整成年女性浣熊型，眼周黑毛、圆耳、环纹尾和操作型爪手，长袖夹克长裤。
水獭福瑞原型|otter adult female anthro|完整成年女性水獭型，小圆耳、圆短吻、长粗渐细尾和短毛，完整长袖外套长裤。
无角鹿福瑞原型|antlerless deer adult female anthro|完整成年女性鹿型，长鼻、大耳、短尾、双瓣蹄，头无角，普通长袖外套与长裤。
山羊型福瑞原型|goat adult female anthro|完整成年女性原创山羊型，一对短弯角和侧耳、细吻、双瓣蹄，完整长袖衣与长裤。
马型福瑞原型|horse adult female anthro|完整成年女性马型，长吻、立耳、后颈鬃、长鬃尾、单蹄，普通完整高领外套及长裤。
''')

block('anthro_species','鳞羽水生昆虫与幻想拟人拓展','''
蜥蜴型鳞肤兽娘|lizard-scaled adult female anthro|完整成年女性拟人蜥蜴，鳞肤、长鳞尾、无哺乳动物耳，普通完整长袖外套和长裤。
鳄型长吻兽娘|crocodile-muzzle adult female anthro|完整成年女性拟人鳄型，长闭合吻、鳞脊尾，无兽耳，普通完整长袖外套和长裤。
壁虎型趾垫兽娘|gecko-toepad adult female anthro|完整成年女性拟人壁虎，短蜥头、宽趾垫与渐细尾，无哺乳耳，完整长袖外套长裤。
青蛙型蹼足兽娘|frog-webfoot adult female anthro|完整成年女性拟人青蛙，短头、平滑绿色肤面、宽蹼足，无尾无兽耳，完整长袖外套长裤。
蝾螈鳃羽兽娘|axolotl-gill adult female anthro|完整成年女性幻想蝾螈拟人，头两侧外鳃枝与长平尾、无哺乳耳，完整长袖外套长裤。
渡鸦羽型兽娘|raven-feather adult female anthro|完整成年女性拟人渡鸦，黑羽头、鸟喙、操作型羽腕手与羽尾，完整长袖外套长裤，无兽耳。
猫头鹰羽型兽娘|owl-feather adult female anthro|完整成年女性拟人猫头鹰，面盘、小喙、羽冠不是哺乳耳，羽腕手和羽尾，完整外套长裤。
隼型羽毛兽娘|falcon-feather adult female anthro|完整成年女性拟人隼，弯短喙、原创眼侧羽纹、羽腕手与鸟趾足，完整长袖外套长裤。
企鹅型羽毛兽娘|penguin-feather adult female anthro|完整成年女性拟人企鹅，黑白羽区、短喙、宽鸟足与短尾，完整长袖外套长裤，无兽耳。
鲨型鳍尾兽娘|shark-fin adult female anthro|完整成年女性幻想鲨型拟人，鲨头闭嘴、背鳍和水平展开的鳍状双臂手部改编、竖向尾鳍，完整外套长裤。
海豚型鳍尾兽娘|dolphin-fin adult female anthro|完整成年女性幻想海豚型拟人，海豚头、背鳍、横向尾鳍，操作型双手，完整高领长袖外套长裤。
鱼鳍侧耳兽娘|fish-fin adult female anthro|完整成年女性幻想鱼型拟人，鳞肤、头侧鳍膜和尾鳍，非哺乳兽耳，完整高领外套长裤。
蛾型触角薄翼兽娘|moth-antenna adult female anthro|完整成年女性幻想蛾型拟人，两条羽状触角与一对薄翼、操作型双手，完整长袖外套长裤。
螳螂型外壳兽娘|mantis-shell adult female anthro|完整成年女性幻想螳螂拟人，三角头、两触角、外壳前臂、双操作手与两支撑腿，完整外套长裤。
龙型角翼尾兽娘|dragon-horn-wing-tail adult female anthro|完整成年女性原创龙拟人，长吻、短角、一对背膜翼、鳞尾和爪足，完整长袖外套长裤。
狮鹫型喙翼兽娘|griffin-beak-wing adult female anthro|完整成年女性原创狮鹫拟人，鸟喙头、一对背羽翼、双操作爪手、狮型后足与穗尾，完整外套长裤。
''')
