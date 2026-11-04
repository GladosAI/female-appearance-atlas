"""Additional fictional identities, kung-fu/clown outfits and full-body flexibility studies."""
from catalog_content import CATALOG,CATEGORIES,category,add
NEW_CATEGORIES=['kungfu_outfits','clown_outfits','flexibility_poses']
category('kungfu_outfits','功夫与武术角色装扮','4套成年原创功夫与武术主题造型，比较练功、武侠、竞技与教习方向。衣层、裤量、鞋履与站姿用于角色设计。',['R63'])
category('clown_outfits','小丑与丑角舞台造型','4套成年小丑与丑角原创造型，比较彩色马戏、菱格、白面默剧与现代街头表演；看妆面、领圈、纽扣与鞋履。',['R63'])
category('flexibility_poses','柔韧、伸展与舞蹈姿态','24个完整衣着的成年女性姿态，分为立姿伸展、坐姿前屈、劈叉压腿、后弯支撑、单足平衡和地面过渡。观察身体曲线、关节方向和接触支撑点；用于绘画与角色动作设计。',['R04','R09'])
NEW_ENTRIES=[];GROUPS=[]
KINDS={
 'imperial_daughter':('identity_status','皇女',['王女','皇室继承人','imperial princess'],['HT008','PN009','GL008']),
 'lady_ruler':('identity_status','女领主',['领地统治者','女城主','lady ruler'],['HT019','BC002','BE001']),
 'fallen_saintess':('identity_duties','堕落圣女',['暗色圣女','失落圣女','fallen saintess'],['HT026','PN010','BC011']),
 'avenger':('identity_classic','复仇者',['复仇女主','复仇角色','avenger'],['HT002','BC006','GL003']),
 'bounty_hunter':('identity_duties','赏金猎人',['悬赏追踪者','bounty hunter'],['HT002','HA026','GE014']),
 'informant':('identity_duties','情报贩子',['情报商','情报中间人','information broker'],['EG004','PN007','GL007']),
 'hacker':('identity_duties','黑客',['技术宅黑客','电脑高手','hacker'],['HP001','EG002','WT014']),
 'guardian':('identity_duties','守护者',['守卫者','守护骑士','guardian'],['HT019','GE020','GL023'])}

def pair(key,character,text):
    cid,label,aliases,parts=KINDS[key];GROUPS.append((key,cid,label,2,1,'paired_identity',character))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==2
    for i,(name,en,desc,recipe) in enumerate(rows,1):
        add(cid,label,f'{label}·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(identity_reference=True,identity_flex_v52_reference=True,identity_kind=label,identity_pair=key,identity_order=i,identity_character_design=character,identity_components=parts,
          added_in='52.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[label,'身份','经典设定','经典人设',*aliases],note='成年原创角色的身份与故事造型参考，同页两套方案保持面容、发色与标志饰物一致；通过衣物、道具与表演交代身份和处境。')
        NEW_ENTRIES.append(e)

pair('imperial_daughter','SAME clearly adult27 woman in both cells: light warm skin, glossy black half-up waves, amber eyes, mature oval face, small pearl-drop pendant; same face, hair and pendant.','''
珍珠冠饰宫廷裙装|imperial daughter pearl court outfit|小型珍珠冠饰、奶白高领长裙与雾蓝披带；珍珠吊坠、双手轻叠，姿态矜持|Small low pearl circlet, opaque ivory high-neck long-sleeve ankle court dress with pale-blue sash and narrow silver edging, small pearl-drop pendant, closed ivory low heels; hands quietly overlapped at waist, poised attentive gaze and tiny polite smile, original fictional adult royal daughter rather than reigning queen
短披骑行行装|imperial daughter riding travel outfit|雾蓝短披、完整白衬衣与长裤、骑行靴；保留珍珠吊坠与半扎发，神态从容|Smoke-blue short shoulder cape over opaque white collared blouse and navy tailored waistcoat, full navy riding trousers, flat knee-high riding boots, same pearl-drop pendant; one hand on small plain satchel strap, other relaxed, calm alert adult gaze, no horse or weapons
''')
pair('lady_ruler','SAME clearly adult36 woman in both cells: olive skin, auburn single braid, green eyes, mature defined face, bronze leaf brooch; identical face, braid and brooch.','''
叶徽长外套议事装|lady ruler administrative coat outfit|深绿长外套、完整内搭与深色中裙；青铜叶徽、薄册与稳重站姿|Forest-green long tailored coat over opaque ivory high-neck blouse, charcoal calf-length straight skirt, bronze leaf brooch and closed brown low shoes; one plain closed folio at side, other hand makes small measured explaining gesture, composed authoritative adult gaze
束袖巡地长裤装|lady ruler field-inspection outfit|棕色束袖外衣、宽腰带与完整长裤、平底靴；同款叶徽，视线观察远处|Opaque brown fitted-sleeve travel coat over covered cream shirt, full olive trousers, broad plain belt, same bronze leaf brooch, flat brown lace-up boots; hands loosely at belt height, grounded upright stance and attentive distant gaze, original territorial leader outfit, no weapons
''')
pair('fallen_saintess','SAME clearly adult30 woman in both cells: light skin, silver-blonde crown braid, pale green eyes, mature oval face, small darkened crescent pendant. Keep the same face, braid and pendant.','''
暗月高领礼装|fallen saintess dark-moon ceremonial look|黑银高领长裙、灰色披肩与暗月吊坠；冠状发辫、平静压低的目光，保留旧仪式轮廓|Opaque black high-neck long-sleeve ankle dress with restrained silver edging, gray shoulder mantle, small darkened crescent pendant and closed gray low heels; hands gently together at waist, cool composed downcast gaze and quiet firm lips; fictional fallen fantasy identity with no real religious symbols, blood, wounds or sexualization
灰白旧披巡行装|fallen saintess faded-mantle travel look|灰白完整衣裙与深墨短披、旅行靴；同一暗月吊坠，旧披边缘轻度磨损，神态坚定|Opaque faded ivory covered blouse and full calf-length gray skirt, charcoal short cape with slight edge wear, same dark crescent pendant and flat dark lace-up boots; one hand lightly holds own cape edge, alert resolute adult gaze, same crown braid, no injury or horror makeup
''')
pair('avenger','SAME clearly adult32 woman in both cells: medium-brown skin, dark low ponytail, hazel eyes, mature angular face, small old silver leaf clasp; identical face, ponytail and clasp.','''
旧徽暗色旅装|avenger old-emblem travel outfit|深灰外套、完整高领内搭与长裤；旧银叶扣、露指手套、坚定凝视|Charcoal long travel coat over opaque black high-neck top, full dark trousers, old silver leaf clasp, thin fingerless gloves and closed flat ankle boots; arms relaxed but hands lightly tense, steady determined direct gaze and firm closed lips, fictional revenge-story protagonist, no weapons, violence, injuries or blood
平民外披隐行装|avenger plain-cloak low-profile outfit|原色衬衣与深棕直裤、旧外披；叶扣仍可见，低马尾，侧身谨慎回看|Opaque undyed long-sleeve blouse, full brown straight trousers, worn gray short cloak with SAME silver leaf clasp, flat brown boots; quarter-turned stance and controlled watchful look back, one hand on small shoulder-bag strap, no chase, weapons or violence
''')
pair('bounty_hunter','SAME clearly adult29 woman in both cells: olive skin, dark low ponytail, gray eyes, mature oval face, small copper compass pendant; same face, ponytail and pendant.','''
多袋外套追踪装|bounty hunter field-tracking outfit|棕色多袋外套、完整内搭与工装长裤；罗盘吊坠、地图袋与平底靴，神态警觉|Brown multi-pocket field jacket over opaque cream crewneck, full charcoal cargo trousers, copper compass pendant, small folded map pouch and flat lace-up boots; one hand holds a plain folded map at waist, alert focused gaze, fictional bounty-tracker fashion with no weapons or apprehension scene
都市短夹克联络装|bounty hunter urban contact outfit|深绿短夹克、完整高领与直裤；同一罗盘吊坠，肩包、平檐营帽和谨慎目光|Dark-green short utility jacket over opaque charcoal high-neck, full black straight trousers, same small compass pendant, plain five-panel cap, small crossbody satchel and closed flat boots; one hand lightly near satchel strap, composed observant eyes and neutral mouth, no weapons or confrontation
''')
pair('informant','SAME clearly adult33 woman in both cells: warm light skin, sleek black chin bob, dark brown eyes, mature oval face, tiny oval silver locket; identical face, bob and locket.','''
酒红长外套会面装|information broker burgundy meeting outfit|酒红长外套、完整奶白衬衣与中裙；猫眼镜、小盒吊坠、短手套，神态从容|Burgundy long tailored coat over opaque ivory high-neck blouse, charcoal calf-length pencil skirt, subtle cat-eye eyeglasses, tiny silver oval locket, short black gloves and closed low heels; one plain sealed envelope held at waist, knowing restrained half-smile and attentive side glance, no readable text
灰蓝低调便装|information broker low-profile casual outfit|灰蓝开衫、完整内搭与长裤；保留短发和吊坠，普通手袋与轻收的目光|Smoke-blue cardigan over opaque cream covered top, full gray trousers, same tiny oval silver locket, plain small handbag and closed flat loafers; one hand lightly on bag handle, calm watchful direct gaze and small composed closed lips, no document text or surveillance instructions
''')
pair('hacker','SAME clearly adult27 woman in both cells: medium-brown skin, short dark curls with one subtly cropped side, brown eyes, mature face, small silver stud earrings; same face, hair and earrings.','''
宽夹克耳机技术装|hacker headset-and-jacket outfit|宽松深灰夹克、完整T恤与工装裤；头戴耳机、方框眼镜、素面便携电脑，目光专注|Oversized charcoal casual jacket over opaque muted-teal crewneck tee, full black cargo trousers, plain over-ear headphones around neck, square eyeglasses, small digital watch and sneakers; one closed plain laptop tucked under arm, focused thoughtful gaze, original fictional computer-specialist look, no code, logos or hacking instructions
简洁卫衣工作装|hacker simple sweatshirt work outfit|蓝灰圆领卫衣与完整直裤；同一发型耳钉、小耳麦与笔记本，站姿放松|Opaque blue-gray crewneck sweatshirt, full charcoal straight trousers, tiny headset earpiece, same silver studs, simple sneakers; holding ONE plain closed notebook at waist and a pen, relaxed standing with concentrated eyes and small neutral mouth, no screen text or logos
''')
pair('guardian','SAME clearly adult35 woman in both cells: light olive skin, long dark single braid, blue-gray eyes, mature strong oval face, small blue shield-shaped brooch; identical face, braid and brooch.','''
蓝银轻甲守望装|guardian blue-silver armor outfit|蓝银轻甲叠完整长衣与长裤；盾形胸针、平底靴和素面圆盾，站姿稳定|Original blue-silver light armor over opaque navy high-neck long tunic and full trousers, small blue shield-shaped brooch, flat armored ankle boots; one plain small round shield rests vertically beside her leg with hand holding its top edge, other arm relaxed, steady protective gaze, no blade or combat action
厚披巡守行装|guardian heavy-cloak patrol outfit|深蓝厚披与完整内搭、长裤及耐用靴；保留盾徽，手持提灯，表情沉稳|Deep-blue thick shoulder cloak over opaque gray covered tunic and full navy trousers, same blue shield brooch, sturdy flat boots; one small brass lantern held at side, grounded balanced standing and calm attentive look, no weapons, injury or fight
''')

def block(key,cid,title,text,framing='full_body'):
    GROUPS.append((key,cid,title,2,2,framing,''))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(name,en,desc,recipe) in enumerate(rows,1):
        add(cid,title,f'{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(identity_flex_v52_reference=True,expansion_group=key,expansion_order=i,added_in='52.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[title,'功夫','武术','kung fu'] if cid=='kungfu_outfits' else [title,'小丑','丑角','clown'] if cid=='clown_outfits' else [title,'柔韧性','柔韧姿态','伸展姿态','女性体态','身体线条'],
          note='成年原创角色的完整服装与表演造型参考。' if cid!='flexibility_poses' else '成年女性绘画姿态参考。比较肩、骨盆与四肢的方向、身体曲线及地面或道具接触点；完整衣着下展示动作轮廓，不作为训练步骤。')
        if cid=='flexibility_poses':e.update(flexibility_reference=True,pose_family=title,view=recipe.split(' VIEW: ')[-1] if ' VIEW: ' in recipe else '见图示')
        else:e.update(special_role_v52_reference=True)
        NEW_ENTRIES.append(e)

block('kungfu','kungfu_outfits','功夫·练功、武侠与竞技','''
盘扣练功宽裤装|kung-fu frog-button training outfit|靛蓝盘扣长袖上衣、宽松练功裤与平底布鞋；头发扎起，双掌抱拳致意|Clearly adult29 woman with dark high ponytail, opaque indigo long-sleeve frog-button training jacket, full loose matching trousers and flat black cloth shoes; hands in a simple fist-and-palm respectful salute at upper chest with natural hands, composed upright stance, original Chinese martial-arts-inspired clothing, no named school claim or weapons
束袖武侠行旅装|wuxia fitted-sleeve travel outfit|灰白束袖短袍叠完整内搭与长裤；窄腰带、轻披肩与布靴，身形舒展|Adult30 olive-skinned woman with dark long braid, opaque gray-white fitted-sleeve short robe over covered shirt and full charcoal trousers, narrow plain belt, short blue shoulder cape and flat cloth ankle boots; grounded small side stance with relaxed arms, alert calm adult gaze, original wuxia heroine costume, no sword or combat
红黑竞技练功装|red-black martial-arts performance outfit|红黑拼色长袖练功衣与完整宽裤；简洁发绳、软底鞋，一掌前伸、一手收于腰侧|Adult27 medium-brown-skinned woman with neat dark bun, opaque red-and-black long-sleeve martial-arts performance top and full loose black trousers, soft flat sports shoes; a clear stable small lunge with one open palm extended at chest height and other hand loosely by waist, no exaggerated kick, no weapon or injury
武馆教习长衫装|martial-arts instructor long-jacket outfit|深绿盘扣长衫、奶白完整内搭与长裤；低位发髻、布鞋，双手背后，神态沉稳|Adult36 woman with dark low bun, opaque forest-green frog-button knee-length long jacket over cream covered blouse and full charcoal trousers, flat black cloth shoes; upright steady standing, hands naturally behind back, composed observant expression, original martial-arts instructor fashion, no real insignia
''')
block('clowns','clown_outfits','小丑·马戏、菱格、白面与街头','''
彩色马戏圆扣小丑|colorful circus clown outfit|红蓝拼色宽外套、圆纽扣与完整长裤；小圆鼻妆、圆顶帽、放大圆头鞋，表情明快|Clearly adult30 woman with mature face, copper curly bob, opaque red-blue oversized circus jacket with large round buttons over covered cream top and full loose trousers, small bowler hat, small red painted nose and oversized round CLOSED clown shoes; one open-palmed playful wave and cheerful adult expression, no horror, balloon or child figure
黑金菱格丑角装|black-gold diamond harlequin outfit|黑金菱格分片衣与完整裙裤；双尖软帽、小铃饰与短靴，侧身摊手|Adult30 olive-skinned woman with mature face and dark low curls, opaque black-gold diamond-panel long-sleeve costume, knee-length split overskirt over full black trousers, soft two-point cap with tiny bells and flat ankle boots; quarter-turned stance with one small palm-up theatrical gesture, refined playful brow, original harlequin-inspired adult costume without copied character design
白面泪点皮埃罗装|white-face Pierrot-inspired clown outfit|白色宽松衣裤、大圆领与黑绒球；克制白底妆、单枚泪点，手势轻柔，表情含蓄|Adult32 woman with mature face and dark tucked hair, opaque white loose long-sleeve blouse with large round ruffle collar, three black pompoms, full loose white trousers, small black cap and closed flat black shoes; restrained white stage foundation, one small painted tear dot below eye, hands lightly together at waist and tender wistful gaze, adult Pierrot-inspired stage styling, no horror or injury
条纹街头表演小丑|striped street-performance clown outfit|彩色条纹上衣、背带宽裤与软帽；小范围彩妆、圆头鞋，俏皮偏头致意|Adult29 medium-brown-skinned woman with short natural dark curls, opaque colorful narrow-striped long-sleeve top, charcoal loose full suspender trousers, plain soft cap and closed round-toe shoes; small original cheek dots rather than full face paint, head playfully tilted, one hand lightly touches cap brim in greeting, warm adult smile, no horror or extra person
''')

block('standing_stretch','flexibility_poses','立姿侧弯与伸展','''
并足上举延伸|standing overhead lengthening pose|双脚接地、双臂上举，手指交扣、掌心向上；肩线与身体纵向延伸|Adult28 woman in opaque long-sleeve sage sports top and full charcoal leggings, tied-back dark hair, barefoot; standing upright with both feet grounded close together, both arms extended above head, hands lightly interlaced palms upward, ribs and pelvis aligned naturally, complete body with generous space above fingertips and below feet. VIEW: 正面
单手扶腰侧弯|standing one-arm side bend|双脚分开接地，一手扶腰、另一臂越过头顶；骨盆稳定、躯干向侧面弯曲|Adult28 woman in opaque long-sleeve blue sports top and full navy leggings, dark low bun, barefoot; feet apart firmly on floor, right hand rests at right waist, left arm arcs overhead toward right, torso bends moderately right with pelvis over feet, smooth believable side curve, complete raised hand and both feet. VIEW: 正面略侧
抱肘肩部伸展|standing elbow-held shoulder stretch|一臂横过胸前，另一手轻托肘侧；肩颈放松、身体直立，双脚接地|Adult30 olive-skinned woman in opaque muted-rose long-sleeve sports top and full charcoal leggings, ponytail, barefoot; standing with feet hip-width, left arm reaches horizontally across upper torso, right hand gently supports outside of left elbow, head turns slightly opposite, normal shoulder joints, full-body framing. VIEW: 四分之三正面
弓步躯干转向|lunge torso-turn pose|前膝弯曲、后腿伸展，两脚接地；躯干小幅转向，一臂向侧后展开|Adult29 medium-brown-skinned woman in opaque teal long-sleeve sports top and full dark leggings, low bun, barefoot; modest forward lunge with front knee bent and rear leg extended, both feet on floor; torso rotates gently toward front leg, arms open horizontally with one pointing front and one toward rear, no extreme spinal twist, complete limbs. VIEW: 四分之三侧面
''', 'standing_pose')
block('seated_stretch','flexibility_poses','坐姿前屈与开髋','''
并腿坐姿前屈|seated straight-leg forward fold|双腿并拢向前伸直，脚跟接地；躯干前倾、双手靠近脚踝，颈部顺着背线|Adult28 woman in opaque sage long-sleeve sports top and full charcoal leggings, dark tied hair, barefoot; seated on plain thin mat with BOTH legs together extended forward, heels down and toes upward, torso gently folded from hips toward thighs, hands rest near own ankles, neck continues natural spine line, clear side silhouette, complete head hands and feet. VIEW: 正侧面
宽坐支撑前倾|wide-seated supported forward lean|双腿向两侧打开，双手撑在前方地面；骨盆坐稳，背线延伸，脚尖上指|Adult29 olive-skinned woman in opaque blue long-sleeve sports top and full navy leggings, bun, barefoot; seated wide straddle on thin plain mat, both straight legs open laterally in a moderate wide V, heels down toes up, torso slightly leans forward, two palms planted on floor ahead, clear hips and separate natural legs, no extreme oversplit. VIEW: 正面略俯视
蝴蝶坐姿俯身|butterfly seated forward lean|双脚掌相对、双膝向两侧，双手轻握脚踝；身体略前倾，肩颈放松|Adult28 medium-brown-skinned woman in opaque muted-rose long-sleeve top and full charcoal leggings, low ponytail, barefoot; seated butterfly position with soles gently together, knees open to sides, hands rest around own ankles, torso leans a little forward, relaxed natural spine and shoulders, full body clearly framed. VIEW: 四分之三正面
坐姿单膝转体|seated bent-knee torso turn|一腿向前伸直、另一膝弯曲，手掌在身后接地；躯干轻转，肩与骨盆方向有别|Adult30 woman in opaque teal long-sleeve sports top and full dark leggings, low bun, barefoot; seated with left leg extended forward and right knee bent upright with right foot on floor just across left thigh, left forearm lightly outside raised knee, right palm on floor behind hip, moderate torso turn right, normal coherent joints, no extreme twist. VIEW: 四分之三侧面
''', 'floor_pose')
block('splits','flexibility_poses','劈叉与压腿轮廓','''
侧面竖叉直立|upright front split side view|前腿向前、后腿向后沿同一直线伸展；双手在髋侧接地，躯干保持直立|Adult28 woman with athletic natural adult proportions, opaque sage long-sleeve top and full charcoal leggings, tied-back hair, barefoot; clear SIDE VIEW full front split on thin mat: right leg straight forward heel on floor toes up, left leg straight backward with top of foot on floor, pelvis between legs, upright torso, both hands lightly on floor beside hips, two normal legs only, complete head hands and toes, no oversplit. VIEW: 正侧面
正面横叉直立|upright middle split front view|双腿向左右伸展、脚跟接地，躯干正直；双掌放于身前，观察髋与腿线|Adult29 olive-skinned woman in opaque blue long-sleeve top and full navy leggings, bun, barefoot; FRONT VIEW full middle split seated on floor, two straight legs extend left and right along same floor line, heels down toes upward, torso upright with hands on floor just in front of pelvis, natural adult hip anatomy and no exposed skin at pelvis, generous horizontal margin beyond toes, no oversplit. VIEW: 正面
低台单腿压伸|low-platform supported leg stretch|一脚接地、另一腿脚跟置于低台；双手轻扶台上腿，躯干前倾，足部完整可见|Adult28 medium-brown-skinned woman in opaque muted-rose long-sleeve top and full charcoal leggings, low ponytail, barefoot; standing left foot firmly on floor while right straight leg extends forward with right heel resting on a SIMPLE stable low rectangular platform around knee height, both hands lightly on right thigh, torso leans gently toward extended leg, both complete feet and platform visible. VIEW: 正侧面
半跪前腿伸展|half-kneeling front-leg extension|一膝与小腿接地，另一腿向前伸直；双手在前腿两侧支撑，背线顺着前倾方向|Adult30 woman in opaque teal long-sleeve top and full dark leggings, low bun, barefoot; half-kneeling side pose, left knee and shin grounded behind, right leg straight forward heel on floor toes up, both palms on floor one on each side of extended leg, torso leans forward naturally from hips, clear knee shin heel palm contact points, no extra limbs. VIEW: 四分之三侧面
''', 'wide_floor_pose')
block('backbends','flexibility_poses','后弯曲线与支撑','''
侧面桥式四点支撑|bridge backbend side view|双手与双脚接地，腹部向上、背部形成弧线；头部悬于双臂之间，支撑点清楚|Adult29 woman in opaque sage long-sleeve sports top and full charcoal leggings, dark hair in tight bun, barefoot; SIDE VIEW gymnastic wheel/bridge backbend on plain thin mat: BOTH soles on floor hip-width with knees bent, BOTH palms on floor behind shoulders with elbows extended naturally, torso forms one smooth raised arch with abdomen upward, head hangs naturally between upper arms and DOES NOT touch ground, exactly two arms two legs, correct shoulder connections and hands/feet all complete, no contortion. VIEW: 正侧面
跪姿轻后弯|kneeling gentle backbend|双膝与小腿接地，双手扶在腰后，胸廓上提；躯干适度后弯，头颈顺势|Adult30 olive-skinned woman in opaque blue long-sleeve top and full navy leggings, bun, barefoot; kneeling upright with both knees and shins on thin mat, hands support own lower back above hips, chest lifted into a moderate smooth backward curve, head follows spine without hanging sharply, hips above knees, clear knee-shin contact and complete body. VIEW: 正侧面
俯卧撑胸抬头|prone supported chest lift|髋腿俯卧接地、双掌在肩侧支撑；胸部抬起、肘部保留弯曲，背线舒展|Adult28 medium-brown-skinned woman in opaque muted-rose long-sleeve sports top and full charcoal leggings, tied hair, barefoot; lying prone with pelvis thighs lower legs and insteps supported on mat, palms on floor near shoulders and elbows bent, upper chest gently lifted with natural extended spine, face looks diagonally forward, no sharp neck compression, full hands and feet visible. VIEW: 正侧面
站姿扶腰轻后仰|standing supported mild backbend|双脚接地、双手扶腰，胸口上提、肩部向后；后仰幅度适中，膝部自然|Adult30 woman in opaque teal long-sleeve sports top and full dark leggings, low bun, barefoot; standing firmly with both feet hip-width, hands support own rear waist, chest lifted and upper torso gently arched backward in a mild curve, knees soft and pelvis balanced over feet, head follows curve naturally, complete body and believable anatomy. VIEW: 四分之三侧面
''', 'wide_floor_pose')
block('dance_balance','flexibility_poses','单足平衡与舞蹈线条','''
单足后举臂展|single-leg backward extension|一脚接地、另一腿向后抬起；双臂向两侧展开，躯干略前倾，腿线延长|Adult28 woman in opaque sage long-sleeve sports top and full charcoal leggings, bun, barefoot; left foot supports full body on floor, right leg extends backward about45 degrees with pointed toes, torso tilts slightly forward, both arms open to sides below shoulder height, complete side silhouette, clear standing support foot and lifted rear leg, no extreme splits. VIEW: 正侧面
抱膝单足平衡|single-leg knee-hold balance|一脚站立、另一膝抬向身前，双手抱在小腿上；躯干正直、骨盆稳定|Adult30 olive-skinned woman in opaque blue long-sleeve top and full navy leggings, ponytail, barefoot; standing upright on left foot, right knee raised in front to waist height, both hands lightly around upper right shin below knee, lifted lower leg hangs naturally, level pelvis and calm balanced posture, complete supporting foot and lifted toes. VIEW: 四分之三正面
侧举腿扶踝平衡|side-leg ankle-held balance|一脚接地，另一腿向侧上方举起；同侧手轻扶脚踝，另一臂展开，关节关系清楚|Adult28 medium-brown-skinned woman in opaque muted-rose long-sleeve sports top and full charcoal leggings, bun, barefoot; standing on left foot, right straight leg raised to the right SIDE at roughly hip height, right hand gently holds right ankle, left arm extends left for balance, torso upright with natural hips, full toes and hands in frame, no leg overhead or extra limb. VIEW: 正面
后屈膝扶脚舞姿|bent-back-leg dancer balance|一脚站立、另一膝向后弯曲，同侧手扶住脚部；另一臂向前延伸，躯干微倾|Adult30 woman in opaque teal long-sleeve sports top and full dark leggings, tied hair, barefoot; side-view single-leg balance on left foot, right knee bent behind and right hand holds right instep at moderate height behind hip, left arm extends forward, torso leans only slightly forward, natural arch and no forced extreme backbend, exactly two coherent arms and legs, complete lifted foot. VIEW: 正侧面
''', 'standing_pose')
block('floor_transitions','flexibility_poses','地面伸展与过渡','''
仰卧单腿上举|supine single-leg lift|背部接地，一腿向前平放、另一腿向上伸直；双手轻扶抬起的腿后侧，脚趾完整|Adult29 woman in opaque sage long-sleeve sports top and full charcoal leggings, tied hair, barefoot; lying supine on thin mat, left leg fully extended along floor, right leg lifted upward around80 degrees with natural straight knee, hands lightly supporting back of right thigh rather than pulling toes, shoulders and head on mat, complete body from crown through both feet. VIEW: 正侧面
侧跪躯干延伸|side-kneeling torso extension|一膝接地、另一腿向侧面伸出；一手轻扶伸腿，另一臂越头，身体侧线延长|Adult30 olive-skinned woman in opaque blue long-sleeve top and full navy leggings, bun, barefoot; kneeling on left knee with right leg straight extended to right side and right sole on floor, right hand rests lightly on right thigh, left arm arcs overhead toward right, torso forms moderate smooth side bend, stable knee-foot support, full fingertips and toes visible. VIEW: 正面
跪坐前伸休息姿|kneeling forward-reach resting pose|双膝与小腿接地、臀部靠近脚跟；躯干前伏、双臂向前，背部形成柔和曲线|Adult28 medium-brown-skinned woman in opaque muted-rose long-sleeve top and full charcoal leggings, low bun, barefoot; kneeling with shins and tops of feet on mat, hips near heels, torso folded gently forward over thighs, both arms extended forward on floor with palms down, forehead lightly near mat, clear coherent relaxed rounded back, complete hands and feet visible in side view. VIEW: 正侧面
双手双足倒V支撑|hands-and-feet inverted-V support|双掌与双脚接地，髋部抬高形成倒V；双臂与背线延伸，膝部可轻弯，头在臂间|Adult30 woman in opaque teal long-sleeve sports top and full dark leggings, tied hair, barefoot; SIDE VIEW standing inverted-V support on thin mat, both palms flat on floor shoulder-width, hips lifted high, both feet grounded behind with heels near floor and knees softly bent, arms and spine form a long natural line, head relaxed between arms without bearing weight, exactly two coherent arms and legs, complete hands and feet. VIEW: 正侧面
''', 'wide_floor_pose')

for cid in ['identity_status','identity_duties','identity_classic']:
    c=next(c for c in CATEGORIES if c['id']==cid)
    c['guide']+= {'identity_status':'新增皇女与女领主，各两套。','identity_duties':'新增堕落圣女、赏金猎人、情报贩子、黑客与守护者，各两套。','identity_classic':'新增复仇者，两套衣着与表演方案。'}[cid]
assert len(NEW_ENTRIES)==48 and len(GROUPS)==16

def make_v52_combinations(entries):
    by_id={e['id']:e for e in entries};out=[]
    for key,(cid,label,aliases,parts) in KINDS.items():
        es=[e for e in entries if e.get('identity_pair')==key];assert len(es)==2
        ids=[e['id'] for e in es]+parts;assert all(i in by_id for i in ids)
        out.append({'name':'身份设定·'+label,'description':'两套身份造型与可选搭配部件，比较同一人物的面容、饰物、服装与处境。','palette':'以两套代表图的配色为基础，可更换局部饰物。','entry_ids':ids,'identity_example':True,'identity_kind':label,'added_in':'52.0'})
    for cid,label,parts in [('kungfu_outfits','功夫与武术',['SP011','HT002']),('clown_outfits','小丑与丑角',['TC059','HA010'])]:
        es=[e for e in entries if e['category']==cid];ids=[e['id'] for e in es]+parts;assert len(es)==4 and all(i in by_id for i in ids)
        out.append({'name':'角色装扮·'+label,'description':'四套主题造型及既有相关图鉴的参考集合，可另存后挑选需要的部件。','palette':'比较各套配色与轮廓，选择一套作为主方向。','entry_ids':ids,'role_example':True,'added_in':'52.0'})
    return out
