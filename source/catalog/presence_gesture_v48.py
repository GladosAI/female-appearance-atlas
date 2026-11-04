"""Sixteen new presence labels and four groups of hand/face acting."""
from catalog_content import CATALOG,CATEGORIES,add
NEW_ENTRIES=[];GROUPS=[]
SYNONYMS={
 '清新':['清爽','自然感'],'素朴':['朴素','质朴'],'禁欲':['封闭领口','克制气质'],'野性':['不驯','粗粝感'],
 '妩媚':['柔媚','媚而不露'],'端丽':['秀丽端正','整饬'],'热血':['斗志','昂扬'],'好胜':['争强','竞争感'],
 '机敏':['敏捷反应','警醒'],'专注':['凝神','聚精会神'],'好奇':['探究','求知'],'乖巧':['温顺表演','规矩'],
 '笨拙':['不熟练表演','手忙脚乱'],'冒失':['莽撞表演','仓促'],'戏谑':['打趣','调侃'],'毒舌':['犀利吐槽','刻薄台词表演']}

def persona(key,title,text):
    GROUPS.append((key,'persona_looks',title,'full_body'))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(label,name,en,desc,recipe) in enumerate(rows,1):
        add('persona_looks',label,f'{label}·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(persona_reference=True,persona_extension=True,presence_gesture_reference=True,persona_tag=label,persona_group=key,persona_order=i,
          added_in='48.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[label,'气质','性格表演','代表造型',*SYNONYMS[label]],
          note='原创25岁以上成年角色的造型与表演参考。把服装轮廓、材质、发型、视线、眉唇与手势组合成创作标签；同一标签有两套方案，可以与其他气质混合，不从外貌判定真实人格或生活习惯。')
        NEW_ENTRIES.append(e)

persona('fresh_plain','清新与素朴','''
清新|浅蓝棉衬衣长裙装|fresh blue-cotton skirt outfit|浅蓝棉衬衣与奶白中长裙，细小发夹和帆布鞋；目光明亮，笑容轻松|Adult25 woman with dark shoulder-length hair and small blue clip, opaque pale-blue cotton shirt, ivory calf-length A-line skirt and white canvas shoes; bright relaxed eyes, small easy smile, one hand lightly holding a canvas tote, complete standing adult figure
清新|薄荷针织直裤装|fresh mint-knit trouser outfit|薄荷圆领针织与浅灰直裤；低位马尾、白鞋和简洁布包，站姿舒展|Adult28 olive-skinned woman with dark low ponytail, opaque mint crewneck knit, light-gray full straight trousers, white low shoes and plain cloth shoulder bag; open relaxed shoulders, clean natural makeup, clear gentle gaze and tiny smile
素朴|原色棉麻围巾装|plain natural-linen outfit|原色棉麻上衣、棕色长裙与朴素围巾；少量装饰，双手自然相搭|Adult30 woman with brown low braid, opaque undyed linen long-sleeve blouse, brown ankle skirt, plain oatmeal scarf and flat brown closed shoes; minimal ornament, hands lightly together, quiet direct gaze, adult face and natural proportions
素朴|浅褐针织背心裤装|plain tan-knit-vest outfit|浅褐针织背心叠完整衬衣与深蓝直裤；短发、布鞋，表情平和|Adult30 medium-brown-skinned woman with short natural dark curls, tan knit vest over opaque ivory long-sleeve shirt, navy full straight trousers and plain flat canvas shoes; arms relaxed, calm modest closed-mouth smile, no decorative jewelry
''')
persona('restrained_untamed','禁欲与野性','''
禁欲|高领窄线条套装|restrained high-neck tailored outfit|高领衬衣、深灰西装和完整长裤；扣件收束、头发后梳，目光克制|Adult30 woman with sleek dark low bun, opaque white high-neck button blouse, charcoal fitted blazer and full tailored trousers, closed black Oxford shoes; straight still shoulders, composed narrow gestures, reserved neutral mouth, no erotic content, restraint expressed through enclosed tailoring
禁欲|封闭领口长裙造型|restrained closed-neck long dress|烟蓝长袖高领长裙与低跟短靴；窄腰带、少量耳饰，双手轻叠|Adult30 olive-skinned woman with dark smooth bob, opaque smoke-blue high-neck long-sleeve ankle dress, narrow dark belt and low closed ankle boots; tiny stud earrings, hands gently overlapped, steady unsmiling calm gaze, no religious costume or body emphasis
野性|粗纹皮革夹克造型|untamed textured-leather outfit|粗纹棕皮夹克、完整深色内搭与工装长裤；散卷发、厚底靴，站姿有力|Adult28 fair-skinned woman with tousled auburn shoulder curls, rugged brown leather jacket over opaque dark tee, charcoal full cargo trousers and heavy lace-up boots; firm grounded stance, hands at hips, intense free direct gaze, original urban costume with no cultural stereotypes or animal parts
野性|不对称外披裤装|untamed asymmetric-layer outfit|橄榄不对称短外披与黑色完整内搭、长裤；少量金属扣，目光锐利|Adult28 olive-skinned woman with long loose dark wavy hair, olive asymmetric short outer layer over opaque black high-neck top and full trousers, black flat boots and sparse metal clasps; balanced wide stance, one hand in pocket, keen unconfined gaze, no tribal symbols or weapons
''')
persona('alluring_composed','妩媚与端丽','''
妩媚|垂褶长袖中裙装|alluring draped-midi outfit|梅紫长袖垂褶中裙与闭口鞋；侧分卷发、略侧的视线和柔和嘴角|Clearly adult30 woman with mature face and dark side-swept waves, opaque plum long-sleeve calf-length draped dress with modest neckline and closed heels; head gently angled, softly lowered eyelids and small warm closed-mouth smile, tasteful non-explicit adult fashion pose
妩媚|丝质衬衣铅笔裙装|alluring blouse-and-pencil outfit|烟玫瑰衬衣配深灰及膝铅笔裙；衣料贴合适度，轻扶耳坠，神态柔媚|Clearly adult30 medium-brown-skinned woman with dark swept-up curls, opaque dusty-rose long-sleeve blouse with covered neckline, charcoal knee-length pencil skirt and low closed heels; one hand lightly near a small earring, soft sideways gaze and restrained asymmetric smile, natural adult body
端丽|米白立领整饬裙装|composed ivory standing-collar outfit|米白立领上衣、蓝灰中长裙与低跟鞋；发髻整洁、配色清楚，正视浅笑|Adult30 woman with neat dark low bun, opaque ivory standing-collar long-sleeve blouse, blue-gray calf-length tailored skirt and low closed shoes; tidy uncluttered silhouette, hands lightly at waist, level attentive eyes and small polished smile
端丽|藏蓝短外套礼裙装|composed navy jacket-dress outfit|藏蓝短外套与浅灰连衣中裙；小耳钉、干净发线，肩颈端正|Adult30 olive-skinned woman with dark hair neatly tucked behind ears, navy short tailored jacket over opaque pale-gray calf-length dress with modest neckline, small pearl studs and closed flats; straight relaxed neck, arms at sides, clear composed gaze and restrained smile
''')
persona('fervent_competitive','热血与好胜','''
热血|红色运动夹克握拳|fervent red track-jacket outfit|红色运动夹克、完整内搭与深色长裤；一手握小拳，眉眼昂扬，嘴角有劲|Adult25 woman with brown high ponytail, red track jacket over opaque ivory tee, full charcoal sports trousers and sneakers; one small fist raised near shoulder, lifted focused brows and determined bright smile, upright energetic standing, no fighting scene
热血|橘黑行旅迈步装|fervent orange-black travel outfit|橘黑外套与完整长裤、行旅鞋；向前迈小步，手掌打开，目光坚定|Adult28 deep-brown-skinned woman with short dark natural curls, orange-and-black practical jacket over opaque crewneck, full black trousers and hiking shoes; small forward step and one open encouraging hand, spirited determined eyes, no weapons or risky action
好胜|钴蓝短夹克叉腰装|competitive cobalt jacket outfit|钴蓝短夹克、完整圆领与直裤；叉腰幅度自然，下颏轻抬，目光不退让|Adult25 woman with dark chin-length bob, cobalt short jacket over opaque white crewneck, full gray straight trousers and sneakers; hands naturally on hips, chin slightly lifted, competitive keen direct gaze and faint confident half-smile, no anger caricature
好胜|黑白运动衫抱臂装|competitive monochrome sports outfit|黑白拼色运动长袖与完整长裤；双臂抱起，眉梢轻挑，嘴角像在应战|Adult28 olive-skinned woman with dark low braid, opaque black-and-white long-sleeve sports top and full black trousers, clean trainers; natural crossed arms, raised outer brow and slight challenging closed-mouth grin, balanced adult standing
''')
persona('alert_focused','机敏与专注','''
机敏|侧望轻转行旅装|alert travel outfit|轻便卡其外套与直裤；头向侧面小幅转动，眉眼警醒，一手稳住包带|Adult28 woman with dark short pixie hair, khaki lightweight jacket over opaque cream tee, full navy trousers and low lace-up shoes; head turned a little toward side, alert open attentive eyes, one hand lightly holds crossbody strap, no fear or weapon
机敏|短马甲停步造型|alert waistcoat paused-step outfit|深灰短马甲叠蓝色衬衣与宽裤；脚步轻停，一手微抬，目光迅速回看|Adult28 medium-brown-skinned woman with tied-back dark curls, charcoal short waistcoat over opaque blue long-sleeve shirt, cream full wide trousers and flats; paused small step, one hand subtly lifted, quick attentive backward glance with level mouth, adult anatomy
专注|读图夹板通勤装|focused clipboard outfit|灰蓝上衣与深色长裤；双手持素面夹板，视线稳定，眉心轻收|Adult30 woman with brown low ponytail, opaque gray-blue long-sleeve blouse, full charcoal trousers and loafers; holds one plain closed clipboard at waist, focused steady gaze slightly downward, gently knitted brows and closed relaxed lips, no readable text
专注|捧书凝神针织装|focused book-holding knit outfit|米白针织衫与棕色中裙；捧一本素面书，肩部安静，眼神凝聚|Adult30 olive-skinned woman with dark low bun, opaque ivory crewneck knit and brown calf-length skirt, closed flats; holds one open plain book at waist, eyes intently on pages, still shoulders and softly closed lips, no text
''')
persona('curious_wellmannered','好奇与乖巧','''
好奇|偏头探看衬裙装|curious tilted-head outfit|浅绿衬衣与奶白中长裙；头轻偏、眼睛明亮，指尖轻触下颏，嘴唇微张|Clearly adult25 woman with dark loose long bob, opaque pale-green long-sleeve blouse, ivory calf-length skirt and flats; small head tilt, bright curious eyes, one fingertip lightly beneath chin and lips barely parted, mature adult proportions
好奇|翻看地图休闲装|curious map-holding casual outfit|蓝色短外套、完整内搭与直裤；手持小幅无字折页，目光从折页抬起|Adult28 medium-brown-skinned woman with short dark curls, blue casual jacket over opaque white tee, beige full straight trousers and sneakers; holds a small folded blank paper map at waist, eyes looking up with inquisitive raised inner brow and tiny smile, no readable map text
乖巧|整齐衬衣并手裙装|well-mannered tidy blouse outfit|整齐浅粉衬衣与灰色中长裙；双手轻叠身前，站姿收敛，表情认真温和|Clearly ADULT25 woman, dark neatly tied low braid, opaque pale-pink long-sleeve blouse, charcoal calf-length skirt and plain loafers; hands gently together in front, small contained upright stance, attentive gentle smile, normal mature face and body, no school or childish uniform
乖巧|圆领开衫持包裤装|well-mannered cardigan outfit|奶白圆领开衫与深蓝直裤；双手轻握小包，眉眼放松，微笑克制|Clearly adult28 olive-skinned woman with neat dark bob, opaque ivory round-neck cardigan over covered light top, full navy straight trousers and flats; both hands loosely hold a small handbag in front, calm attentive gaze and tiny polite smile, mature adult face
''')
persona('awkward_rash','笨拙与冒失','''
笨拙|抱书失衡针织装|awkward book-stack outfit|宽针织衫与完整长裤；抱两本略不齐的书，手肘收得局促，笑容有些不好意思|Adult25 woman with brown shoulder-length waves, opaque oatmeal loose knit top, full charcoal trousers and sneakers; holding exactly two closed plain books slightly misaligned against torso, elbows tucked awkwardly, small embarrassed smile, safe upright balance and correct natural hands
笨拙|手套整理停顿造型|awkward glove-adjusting outfit|短外套与中长裙；一只手正在笨拙整理另一只手的袖口，眉眼迟疑|Adult28 deep-brown-skinned woman with short natural dark curls, muted lavender short jacket over opaque cream blouse, navy calf-length skirt and flats; one hand trying to straighten opposite glove cuff, hesitant brows and small apologetic half-smile, correctly formed hands with natural occlusion, not tied or injured
冒失|仓促整理包带造型|rash hurried bag-strap outfit|珊瑚外套与完整直裤；一手整理偏斜包带、另一手微抬，头发少量散开|Adult25 woman with slightly loose dark ponytail, coral casual jacket over opaque white tee, full gray straight trousers and sneakers; one hand straightens a slightly crooked shoulder bag strap while free hand rises in small apologetic gesture, hasty surprised eyes, safely standing with no fall
冒失|急停举手致歉造型|rash stopped-step apology outfit|蓝绿衬衣与深色中裙；脚步刚停，一掌抬起致歉，嘴角像刚想起什么|Adult28 olive-skinned woman with dark short bob, opaque teal long-sleeve shirt, charcoal calf-length skirt and flats; small just-stopped forward step, one open hand raised near shoulder in apology, sudden realizing brows and tiny open mouth, no collision or dropped clutter
''')
persona('teasing_sharp','戏谑与毒舌','''
戏谑|挑眉偏笑马甲装|teasing waistcoat outfit|灰色马甲叠白衬衣与直裤；单眉轻挑、嘴角偏笑，一手轻点下颏|Adult28 woman with copper-brown chin-length bob, gray waistcoat over opaque white long-sleeve shirt, full black trousers and loafers; one outer brow raised, amused asymmetric small grin and fingertip lightly at chin, friendly ironic acting, no speech text
戏谑|摊手打趣夹克装|teasing open-palm jacket outfit|酒红夹克与完整圆领、宽裤；一掌轻摊，头微偏，眼神带笑|Adult28 medium-brown-skinned woman with low dark curly ponytail, burgundy jacket over opaque cream crewneck, full charcoal wide trousers and sneakers; one small palm-up joking gesture, head tilted and eyes warmly amused, restrained sly smile, no text
毒舌|抱臂侧睨黑白装|sharp-tongued monochrome acting outfit|黑白衬衣与长裤；抱臂、眼睑微压，嘴角像在冷静吐槽，神态犀利|Adult30 woman with sleek dark bob, opaque white blouse with narrow black neck ribbon, full charcoal trousers and closed black shoes; naturally crossed arms, slightly lowered upper eyelids and dry critical sideways glance, mouth forming a tiny controlled speaking shape, no hateful symbols or speech text
毒舌|单掌示意深绿套装|sharp-tongued green tailored outfit|深绿短西装与完整内搭、中裙；单掌作小幅说明，眉线收紧，口型短促|Adult30 olive-skinned woman with dark low bun, forest-green short blazer over opaque ivory blouse, charcoal calf-length skirt and low heels; one open palm makes a small precise explanatory gesture, keen brow and terse slightly parted speaking lips, sardonic fictional acting, no insulting text
''')

def gesture(key,label,framing,text):
    GROUPS.append((key,'face_hands',label,framing))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(name,en,desc,recipe) in enumerate(rows,1):
        add('face_hands',label,f'{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(facial_reference=True,presence_gesture_reference=True,gesture_reference=True,gesture_kind=label,gesture_group=key,gesture_order=i,
          added_in='48.0',age_min=25,adult_only=True,minor_reference=False,age_context='25岁以上成年角色的手势与面部表演参考',illustration_recipe=recipe,
          aliases=[label,'面部参考','手势','手部与面部互动'],
          note='原创成年角色的表情与手势配合图。观察手掌朝向、拇指与四指的遮挡、双腕和肘部位置，再比较眉、眼、口与头部角度；许愿、祈祷和行礼是通用创作表演标签，具体礼仪因场合而异。')
        NEW_ENTRIES.append(e)

gesture('wishing','许愿','upper_body','''
双手交扣闭眼许愿|eyes-closed interlaced-hands wish|双手轻交扣停在下颏下方，眼睛闭合、眉线舒展，嘴角轻扬；双腕与拇指清楚|Adult28 woman with brown loose shoulder waves, opaque ivory high-neck blouse; both hands loosely interlaced BELOW chin at upper chest, thumbs visible and wrists complete, gently closed eyes and tiny hopeful smile, natural distinct fingers and plausible occlusion, waist-up portrait
十指相抵仰面许愿|upward steepled-fingers wish|两手指腹轻相抵成小尖塔，头部微抬，双眼向上看，双手不遮口鼻|Adult28 olive-skinned woman with dark low bun, opaque pale-blue crewneck knit; fingertips of both hands gently touch in a small steeple BELOW chin, separate palms and complete wrists, gaze slightly upward, softly parted hopeful lips, face entirely visible, waist-up
双手轻握贴颏许愿|soft-clasp near-chin wish|两手松松相握贴近下颏，头微偏，闭眼浅笑，手指与下颌之间保留间隙|Adult25 medium-brown-skinned woman with tied-back dark curls, opaque lavender blouse; hands loosely clasped near but not pressed into chin with a small visible gap, head gently tilted, closed eyes and light smile, complete hands and forearms, waist-up portrait
捧纸星轻声许愿|paper-star wish gesture|双手捧一枚小纸星放在胸前，眼睑轻闭、唇微动；纸星与指尖分离可辨|Adult28 woman with dark chin-length bob, opaque sage high-neck top; both cupped hands support ONE small folded paper star at upper chest, clear fingertips and palms, softly closed eyes and tiny whisper-like parted lips, complete wrists, waist-up, no magical glow
''')
gesture('praying','祈祷','upper_body','''
双掌合十低头祈祷|palms-together bowed-head prayer|双掌竖直贴合置于胸前，四指平行、拇指自然弯曲；低头闭眼，眉间平静|Adult30 woman with dark low bun, opaque cream long-sleeve high-neck blouse; two palms pressed together vertically at upper sternum, fingers point upward in parallel and thumbs naturally bent, complete wrists and elbows, head gently bowed and eyes closed, calm reverent expression, waist-up, no specific religious symbols
双手交扣俯首祈祷|interlaced-hands bowed prayer|两手交扣放在口部下方，俯首闭眼，唇线收拢；不让手掌遮住整张脸|Adult30 deep-brown-skinned woman with neat dark braided updo, opaque blue-gray covered blouse; two hands interlaced below mouth at upper chest, head gently lowered, eyes closed, solemn relaxed closed lips; complete natural hands and wrists, face readable, waist-up portrait
一手覆心低头祈祷|hand-over-heart quiet prayer|一手自然覆在上胸衣料上，另一手垂于身侧，低头闭眼，肩颈放松|Adult30 olive-skinned woman with dark smooth bob, opaque muted teal high-neck long-sleeve top; one open hand rests flat on upper sternum over fabric, other arm relaxed with hand visible near waist, head bowed and eyes closed, peaceful neutral mouth, waist-up, no chest emphasis
双掌朝上静心祈祷|open-palms quiet prayer|双手在胸腹前轻托，掌心向上、手指自然弯曲；双眼轻闭，嘴唇微张|Adult30 woman with brown low braid, opaque ivory covered blouse; both forearms rise gently before torso with separate cupped palms facing upward at lower chest, naturally curved fingers and complete wrists, closed eyes and slightly parted calm lips, waist-up, general acting pose not a named ritual
''')
gesture('pleading','乞求','upper_body','''
合掌前倾乞求|forward-lean palms-together plea|双掌在下颏下合拢，身体略前倾，眉内端抬起，目光向上请求|Adult28 woman with dark shoulder-length hair, opaque gray-blue blouse with covered neckline; palms together below chin, small forward torso lean, inner brows lifted and eyes looking gently upward, tentative parted mouth; complete hands and wrists, waist-up, nonsexual pleading acting
交握双手仰望乞求|clasped-hands upward plea|两手交握停在胸前，头部轻抬、眼神恳切，唇线紧张但不夸张哭喊|Adult28 medium-brown-skinned woman with short dark curls, opaque rose covered blouse; hands clasped at upper chest, head slightly raised, earnest upward eyes, mildly tense small closed mouth and lifted inner brows, complete fingers and wrists, waist-up, no distress scene
双掌向前请求|open-palms earnest request|双掌相隔向前轻伸，掌心斜向上；眉线靠拢，视线停在观者，嘴唇微张|Adult28 olive-skinned woman with dark low ponytail, opaque cream high-neck top; both separate hands extend a short distance forward at lower chest, palms tilted upward and fingers naturally curved, earnest direct eye contact and gently knitted brows, small parted lips, complete hands, waist-up
捏袖轻声乞求|sleeve-holding quiet plea|双手轻捏自己袖边，肩部微收，头轻偏，眉内侧抬起，嘴角带请求感|Adult25 woman with brown long bob, opaque lavender long-sleeve blouse; fingertips lightly pinch her own opposite sleeve edges near waist, no other person, shoulders subtly drawn inward, head tilted and pleading lifted inner brows, tiny tentative smile, complete wrists and visible hands, waist-up
''')
gesture('saluting','行礼','head_to_knees','''
合十颔首行礼|palms-together nodding greeting|胸前合十、头部轻颔，眼睑低垂、嘴角礼貌；手掌与脸部保持清楚间隙|Adult30 woman with dark low bun, opaque ivory blouse and navy calf-length skirt; two palms together at upper chest, small polite nod with lowered eyelids and closed-mouth smile, hands separated visually from chin, head-to-knees portrait including both complete arms and hands, no specific ritual claim
交手置腹俯首行礼|overlapped-hands formal bow|双手轻交叠放在上腹，躯干小幅前倾，低头垂眸；双肘自然，衣领整齐|Adult30 olive-skinned woman with sleek dark bob, opaque pale-blue long-sleeve blouse and charcoal calf-length skirt; hands lightly overlapped at upper abdomen, modest forward torso bow and lowered eyes, neat collar, complete head arms and hands, head-to-knees framing, no extreme bend
轻扶帽檐颔首致礼|hat-brim nod greeting|一手轻扶帽檐、另一手垂落，头微低、视线礼貌回望，保持完整指尖|Adult30 medium-brown-skinned woman with dark low curls, plain brown brimmed hat, opaque cream blouse, charcoal tailored jacket and full trousers; one hand gently touches hat brim with distinct fingers, other hand relaxed by hip, small polite head nod and soft eye contact, head-to-knees portrait
提裙欠身行礼|skirt-holding curtsy greeting|双手轻提两侧裙摆，屈膝欠身、低头浅笑；裙摆只作小幅提起，保留膝部动作|Adult30 woman with brown low updo, opaque muted-rose long-sleeve calf-length full dress; each hand lightly holds a small fold of skirt at respective side without lifting above knee, small curtsy with subtly bent knees and head gently lowered, polite smile, frame full head through just BELOW both knees, complete hands and skirt gestures, no exposure
''')

next(c for c in CATEGORIES if c['id']=='persona_looks')['guide']='64种创作表现标签，各有两套全身搭配；通过衣物、表情、视线和动作共同表现，可跨标签混搭。标签不用于根据外貌判断真实人格；萌与孩子气表演均为成年角色。'
hc=next(c for c in CATEGORIES if c['id']=='face_hands');original_guide=hc['guide']
for e in CATALOG:
    if e['category']=='face_hands' and not e.get('note'):e['note']=original_guide
hc['guide']=original_guide+'新增许愿、祈祷、乞求和行礼，比较手形、视线、头部角度与躯干配合。'
assert len(NEW_ENTRIES)==48 and len(GROUPS)==12 and len(SYNONYMS)==16
