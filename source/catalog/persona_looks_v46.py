"""Additional adult character-presence studies; reuse the existing primary category."""
from catalog_content import CATALOG,CATEGORIES,add

NEW_ENTRIES=[]
GROUPS=[]
SYNONYMS={
 '甜酷':['甜酷感','甜辣风'],'俏皮':['顽皮','鬼马'],'羞涩':['害羞','腼腆'],'怯生':['怕生','拘谨'],
 '骄矜':['矜持自傲','自矜'],'贵气':['雍容','华贵'],'亲和':['可亲','友善'],'阳光':['明朗','朝气'],
 '冷静':['镇定','理智'],'严肃':['认真','正色'],'狡黠':['机灵','狡猾表演'],'腹黑':['笑里藏意','反差微笑'],
 '率真':['直率','坦率'],'随性':['自在','洒脱'],'坚毅':['坚韧','不屈'],'勇敢':['果敢','无畏'],
 '浪漫':['诗意','梦幻气质'],'感性':['情感丰富','细腻'],'忧郁':['惆怅','沉郁'],'脆弱':['易碎感','柔弱表演'],
 '强势':['主导感','凌厉'],'威严':['庄重','肃穆'],'中性':['无性别穿搭','雌雄同体美感'],'华丽':['繁复','耀眼']}

def block(key,title,text):
    GROUPS.append((key,'persona_looks',title))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(label,name,en,desc,recipe) in enumerate(rows,1):
        add('persona_looks',label,f'{label}·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(persona_reference=True,persona_extension=True,persona_tag=label,persona_group=key,persona_order=i,
          added_in='46.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[label,'气质','性格表演','代表造型',*SYNONYMS[label]],
          note='原创25岁以上成年角色的造型与表演参考。结合衣物轮廓、材质、眉眼、嘴角、视线与重心表现创作标签；同一标签的两套搭配可相互比较，也可与其他气质混合。不是对真实人格或健康状态的判定。')
        NEW_ENTRIES.append(e)

block('sweetcool_playful','甜酷与俏皮','''
甜酷|缎带机车短裙装|sweet-cool ribbon biker outfit|黑色短皮衣、雾粉圆领内搭与及膝褶裙；小蝴蝶结配厚底靴，微笑带一点挑眉|Adult25 woman, black high ponytail with small dusty-pink ribbon, black cropped biker jacket over opaque dusty-pink crewneck, charcoal knee-length pleated skirt, black lace-up ankle boots; balanced stance, one hand on jacket lapel, raised outer brow and tiny confident smile, sweet details contrasted with sharp leather
甜酷|薄荷工装裤造型|sweet-cool mint cargo outfit|薄荷短夹克与黑色工装长裤，圆润发卡点缀；双手插袋，嘴角轻扬|Adult25 olive-skinned woman, dark chin-length bob and one small mint rounded hair clip, mint cropped utility jacket over opaque black tee, black full cargo trousers and chunky white sneakers; hands in pockets, head slightly tilted and playful confident half-smile, clear adult face
俏皮|条纹背带裤造型|playful striped-overall outfit|细条纹圆领衫与牛仔背带长裤；侧抬一只手比小剪刀，神态灵动|Adult25 woman, chestnut short wavy bob, opaque cream-and-coral striped long-sleeve tee, blue denim full-length overalls, white canvas shoes; one small V sign beside shoulder, lively asymmetric closed-mouth smile and gently tilted head, standing balanced, adult proportions
俏皮|柠黄风衣眨眼造型|playful yellow-coat wink outfit|柠黄短风衣与奶白中长裙；一手捏帽檐、单眼轻眨，动作轻快|Adult25 medium-brown-skinned woman with short natural curly hair, lemon-yellow short trench over opaque cream crewneck midi dress, small ivory beret and white low shoes; one hand lightly touches beret brim, single playful wink and bright small smile, complete standing figure
''')
block('shy_timid','羞涩与怯生','''
羞涩|樱粉衬衣轻握袖口|shy blush-blouse outfit|樱粉长袖衬衣与灰色中裙；视线轻垂又回看，捏住袖口，脸颊微红|Adult25 woman, dark low side braid, opaque blush-pink long-sleeve blouse with closed neckline, gray calf-length A-line skirt, brown flats; fingertips lightly hold opposite cuff, gaze gently lowered toward viewer with a small shy smile and slight cheek blush, relaxed adult shoulders
羞涩|蓝白针织背手造型|shy knit outfit with hands behind|蓝白圆领针织衫与米色直裤；双手背后轻交握，脚尖微内收，微笑含蓄|Adult25 woman, shoulder-length brown hair tucked behind one ear, opaque pale-blue-and-ivory crewneck knit, beige straight trousers and white loafers; hands naturally clasped behind back, toes only subtly inward, tiny shy smile and soft blush, full adult body
怯生|抱包侧站造型|timid close-held-bag outfit|灰紫针织外套与藏蓝长裙；包放在身前作轻微遮挡，手肘收紧，观察旁侧|Adult25 woman, neat dark bob, muted lavender cardigan over opaque ivory high-neck top, navy ankle skirt and flats; holds a small handbag close in front, elbows tucked and body angled slightly away, watchful sideways gaze and closed neutral mouth, mild social hesitation without fear caricature
怯生|收肩握带休闲装|timid strap-holding casual outfit|浅棕夹克与完整长裤；一手握背包肩带，另一手收在身侧，肩部轻收|Adult25 medium-brown-skinned woman with tied-back dark curls, tan jacket over opaque cream tee, charcoal full trousers and sneakers; one hand holds backpack shoulder strap, other stays close to hip, slightly drawn-in shoulders and hesitant small smile, upright standing, no distress scene
''')
block('proud_regal','骄矜与贵气','''
骄矜|奶白修身礼装|proud ivory tailored outfit|奶白短西装配窄身中裙；下颏轻抬、眉梢微扬，单手轻扶手套|Adult28 woman, smooth dark swept-up hair, ivory tailored blazer with covered blouse and matching knee-length pencil skirt, tiny pearl studs, gloves and closed heels; chin slightly lifted, outer brow subtly raised and restrained self-satisfied closed-mouth smile, one hand lightly adjusting opposite glove
骄矜|紫色领结裙装|proud plum bow-neck outfit|深梅紫领结衬衣与黑色伞裙；身体略侧、视线斜看，手持小包而不贴身|Adult28 woman, glossy dark long hair, opaque deep-plum bow-neck long-sleeve blouse and black calf-length structured skirt, small handbag and pumps; body slightly turned, eyes glance sideways with a composed proud half-smile, free hand lightly at waist
贵气|香槟色珠饰礼裙|regal champagne evening outfit|香槟色长袖礼裙与少量珠饰；低盘发、肩颈舒展，双手平稳轻叠|Adult30 woman, elegant dark low bun, opaque champagne-gold long-sleeve ankle gown with restrained pearl embroidery at cuffs and high neckline, small drop earrings and low heels; open relaxed neck and shoulders, hands gently overlapped at waist, serene poised gaze, no crown
贵气|祖母绿披肩套装|regal emerald shawl outfit|祖母绿丝绒长裙与米白披肩；金色耳饰点缀，站姿从容，目光平和|Adult30 deep-brown-skinned woman with dark braided updo, opaque emerald velvet calf-length dress with modest square neckline, ivory shawl around upper arms, simple gold earrings and closed pumps; composed full standing posture, calm generous small smile, one hand lightly holding shawl edge
''')
block('friendly_sunny','亲和与阳光','''
亲和|暖杏围裙休闲装|approachable apricot apron outfit|暖杏衬衣、米白半围裙与长裙；双掌自然摊开，眉眼放松，笑容温暖|Adult28 woman with brown shoulder-length curls, opaque warm-apricot blouse, ivory plain half-apron over muted teal calf-length skirt, comfortable flats; two relaxed open palms near waist, soft brows and warm approachable smile, no kitchen background
亲和|浅绿开衫迎接造型|approachable green cardigan outfit|浅绿开衫与宽松长裤；身体稍向前倾，一只手作轻柔邀请，视线平视|Adult28 medium-brown-skinned woman with short curly bob, soft sage-green cardigan over opaque white tee, cream wide trousers and brown loafers; slight friendly forward lean, one open inviting hand and gentle level eye contact, warm smile without huge open mouth
阳光|珊瑚运动夹克造型|sunny coral sports-casual outfit|珊瑚夹克、白色圆领内搭与蓝色牛仔；抬头开怀笑，步伐轻快|Adult25 woman, brown high ponytail, coral lightweight sports jacket over opaque white crewneck, full blue straight jeans and white sneakers; bright open cheerful smile, head lifted and buoyant small step, both arms relaxed with light movement
阳光|明黄衬衣清爽造型|sunny yellow-shirt outfit|明黄短袖衬衣与奶白及膝裙；袖口整齐，肩部打开，向观者大方招手|Adult25 olive-skinned woman with short dark pixie hair, opaque sunny-yellow short-sleeve shirt with normal closed neckline, ivory knee-length A-line skirt and white canvas shoes; open shoulders, friendly high wave and radiant confident smile, clear full figure
''')
block('calm_serious','冷静与严肃','''
冷静|灰蓝风衣思考造型|calm blue-gray trench outfit|灰蓝风衣与白高领、直裤；眉线舒平，视线稳定，一手轻触下颏|Adult28 woman, dark low ponytail, blue-gray knee-length trench over opaque white turtleneck, navy straight trousers and loafers; one hand lightly touches chin, brows level, steady attentive eyes and neutral lips, composed thoughtful stance
冷静|极简马甲裤装|calm minimalist waistcoat outfit|深灰马甲叠浅蓝衬衣与直裤；双手轻搭身前，肩颈放松，目光专注|Adult28 woman with dark bob, charcoal tailored waistcoat over opaque pale-blue long-sleeve shirt, matching full trousers and black low shoes; hands lightly together in front, relaxed shoulders, calm focused gaze with gently closed mouth, no glare
严肃|藏蓝制服式套装|serious navy formal outfit|藏蓝立领外套与中长裙；扣件简洁，抿直嘴角，双臂自然下垂|Adult30 woman, dark neat bun, opaque navy standing-collar formal jacket and matching calf-length straight skirt, black closed shoes; upright centered full stance, firm level brows and straight closed lips, arms at sides, original costume with no real insignia
严肃|白衬衣黑领带造型|serious shirt-and-tie outfit|白衬衣、黑领带与灰色长裤；持薄文件夹，眉心略收，正视前方|Adult28 deep-brown-skinned woman with sleek short hair, opaque white button shirt with black necktie and charcoal tailored full trousers, low black shoes; closed plain folder held at side, slight brow concentration and unsmiling direct gaze, disciplined posture
''')
block('sly_hidden','狡黠与腹黑','''
狡黠|斜领马甲挑眉造型|sly asymmetric-vest outfit|不对称短马甲与衬衣长裤；一边眉梢抬高，嘴角偏向一侧，手指轻点脸旁|Adult25 woman with copper-brown chin-length bob, asymmetric charcoal waistcoat over opaque cream shirt, dark full trousers and ankle boots; one outer brow raised, knowing asymmetric closed-mouth grin, index finger lightly rests beside cheek, clear adult face
狡黠|酒红短披肩造型|sly burgundy capelet outfit|酒红短披肩叠灰色长裙；视线斜回，单手轻转小硬币，笑容像藏着主意|Adult28 olive-skinned woman with long dark braid, burgundy short capelet over opaque gray high-neck calf-length dress, boots; one hand holds a single small plain coin at waist, sideways knowing glance and tilted small grin, no extra coins or magic effects
腹黑|微笑黑白衬裙装|hidden-agenda smiling outfit|黑白领衬衣与长裙；双手交握，笑容礼貌，眼睑稍低，与嘴角形成反差|Adult28 woman, smooth dark long hair, opaque white small-collar blouse, black high-waist ankle skirt and plain black pumps; hands calmly folded in front, polite soft closed-mouth smile but lowered upper eyelids and steady calculating eyes, clearly readable eyes, no horror shading
腹黑|奶油西装背手造型|hidden-agenda cream suit outfit|奶油西装与深色完整内搭；双手背后，头略偏，温和微笑中带观察感|Adult28 woman, wavy dark low ponytail, cream tailored blazer over opaque dark high-neck top, taupe full trousers and loafers; hands naturally behind back, small head tilt, composed gentle smile paired with subtly narrowed observant eyes, no evil symbols
''')
block('frank_easygoing','率真与随性','''
率真|蓝色工装衬衣造型|frank denim-shirt outfit|蓝色工装衬衣与米色长裤；掌心向上直接表达，眉眼开阔，笑容坦然|Adult25 woman with short dark pixie cut, opaque blue utility shirt with neatly rolled sleeves, beige straight full trousers and brown lace-up shoes; one palm-up direct conversational gesture, open honest brows and straightforward warm smile, standing grounded
率真|红白拉链夹克造型|frank red-white jacket outfit|红白夹克、圆领内搭与黑色长裙；双手叉腰幅度自然，目光直视，神态爽朗|Adult25 medium-brown-skinned woman with dark tied-back curls, red-and-white zip jacket over opaque white tee, black calf-length A-line skirt and sneakers; both hands naturally on hips, direct gaze and candid broad small smile, no exaggerated chest pose
随性|宽松衬衣牛仔造型|easygoing loose-shirt outfit|宽松亚麻衬衣、完整内搭与牛仔长裤；衣摆一侧松放，单手插袋，重心偏一脚|Adult28 woman with loose wavy brown shoulder-length hair, open oatmeal linen shirt over opaque cream crewneck, full blue jeans and brown loafers; shirt hem casually untucked, one hand in pocket, easy one-leg weight shift and relaxed smile, not slumped
随性|薄针织肩搭造型|easygoing shoulder-knit outfit|白色圆领衫与橄榄宽裤，薄针织搭肩；一手拎小软包，目光自在|Adult28 olive-skinned woman with brown low messy bun, opaque white tee, olive full wide trousers, camel thin knit draped over shoulders, flat sandals; one hand holds a small soft tote, relaxed uncrossed stance and easy calm gaze, all shoes inside frame
''')
block('resolute_brave','坚毅与勇敢','''
坚毅|耐磨行旅裤装|resolute travel outfit|土灰短外衣与深色长裤；肩背挺直、眉心轻收，双手稳住背包带|Adult28 woman with dark low braid, taupe durable travel jacket over opaque dark tee, charcoal full hiking trousers and boots, plain backpack; both hands steadily grip backpack straps, spine upright, gently knitted brows and firm closed lips, determined but not angry, no weapon
坚毅|缠腕训练休闲装|resolute training-casual outfit|深蓝运动外套与完整长裤；腕部普通运动护带，一手轻握拳，目光不回避|Adult28 deep-brown-skinned woman with short natural curls, navy track jacket fully covering torso, gray full athletic trousers, simple white sports wristbands and sneakers; one relaxed small fist beside hip, square steady shoulders and unwavering determined gaze, no combat injury
勇敢|橙色救援主题造型|brave rescue-inspired outfit|橙色功能夹克、反光边线与深灰长裤；向前跨小步，一手示意跟上，神态坚定|Adult28 woman with dark tucked-back bob, orange functional jacket with plain reflective trim over opaque undershirt, charcoal full utility trousers and sturdy boots; small forward stride and one hand gesturing follow me, direct determined encouraging gaze, fictional costume no logos or tools
勇敢|短斗篷远行造型|brave traveler cape outfit|青绿短斗篷与深色连身长裤；站在迈步起点，手势主动，眼神坚定明亮|Adult28 woman with long dark braid, teal short travel cape over opaque dark high-neck full-length fitted utility jumpsuit, brown belt and flat boots; upright preparing-to-step stance and open hand extended at waist, bright resolute eyes and controlled confident mouth, no sword or weapon
''')
block('romantic_sensitive','浪漫与感性','''
浪漫|柔紫花边长裙造型|romantic lavender dress outfit|柔紫长袖长裙与细花边；松卷发配小花发夹，双手捧一枝花，目光轻柔|Adult25 woman, brown loose long curls with one small lavender floral clip, opaque lavender long-sleeve calf-length dress with subtle lace edging, closed low heels; holds one single small flower between hands at waist, dreamy soft upward gaze and gentle smile, no extra figures
浪漫|奶白薄纱叠裙造型|romantic layered cream outfit|奶白衬衣与浅蓝叠层长裙，轻薄外层有完整衬里；一手轻提少量裙摆，姿态舒展|Adult28 olive-skinned woman with braided dark updo, opaque ivory blouse with softly gathered sleeves, pale-blue layered ankle skirt with fully opaque lining beneath fine tulle, pale flats; one hand lightly lifts a tiny side of skirt without exposing legs, softly turned torso, serene poetic smile
感性|暖玫瑰披肩造型|emotionally expressive rose shawl outfit|暖玫瑰披肩与灰色中长裙；一手靠近锁骨，眉梢轻抬，眼神像被故事触动|Adult28 woman with chestnut shoulder-length curls, muted warm-rose shawl over opaque gray closed-neck midi dress and flats; one open hand gently near collarbone, inner brows slightly lifted and moist-looking attentive eyes, small touched smile, no tears streaming
感性|蓝绿针织捧信造型|sensitive teal-knit outfit|蓝绿针织衫与棕色伞裙；双手捧一封素色信封，目光柔软，嘴角欲笑未笑|Adult28 medium-brown-skinned woman with dark low curls, opaque teal crewneck knit and brown calf-length skirt, loafers; holds one plain closed envelope in both hands at waist, emotionally attentive gentle eyes and small almost-smile, no readable text
''')
block('melancholy_fragile','忧郁与脆弱','''
忧郁|雨灰大衣垂眸造型|melancholic gray-coat outfit|雨灰大衣与深蓝长裙；视线落向地面，眉内端轻抬，肩部略沉但站姿完整|Adult28 woman with long dark loose hair, rain-gray long coat over opaque navy high-neck ankle dress, black flat boots; downward distant gaze, subtly raised inner brows, neutral slightly downturned mouth, mildly lowered shoulders while standing upright, clean neutral studio no rain or harm
忧郁|雾蓝针织抱肘造型|melancholic mist-blue knit outfit|雾蓝针织衫与深色直裤；一手轻扶对侧手肘，头略低，视线停在远处|Adult28 olive-skinned woman with brown long bob, opaque mist-blue crewneck sweater and dark full straight trousers, gray loafers; one hand lightly holds opposite elbow, head gently bowed and gaze into distance, quiet sad brows and softly closed lips, no crying or injury
脆弱|浅米围巾轻护造型|fragile cream-scarf outfit|浅米围巾叠灰紫长袖裙；双手贴近身前，眉眼微收，像在寻求回应|Adult25 woman with light-brown softly waved shoulder hair, cream scarf over opaque muted-lavender long-sleeve calf-length dress, plain flats; hands held close together before waist, slightly drawn shoulders, tender tentative eyes with raised inner brows and small parted lips, healthy natural adult body, no injury
脆弱|薄灰开衫轻捏袖边|fragile gray-cardigan outfit|薄灰开衫、白色完整内搭与蓝色中裙；轻捏袖边，唇线略颤，目光带迟疑|Adult25 deep-brown-skinned woman with dark short natural curls, light-gray cardigan over opaque white round-neck top, pale-blue calf-length skirt and flats; fingertips softly pinch sleeve edge, tentative eye contact and delicate uncertain closed mouth, adult normal body, no medical equipment or illness
''')
block('assertive_majestic','强势与威严','''
强势|宽肩红色西装造型|assertive red power-suit outfit|宽肩红西装与黑色长裤；一手扶腰，另一手作明确指示，目光有主导感|Adult30 woman with sleek dark shoulder-length bob, bold structured red blazer over opaque black high-neck top, black full tailored trousers and closed heels; one hand at hip, other open palm makes a decisive sideways directional gesture, direct firm eyes and controlled mouth, no pointing at viewer
强势|黑白高腰裤装|assertive black-white outfit|白色高领衬衣与黑色高腰长裤；双臂自然抱起，身体正对，眉眼凌厉|Adult30 medium-brown-skinned woman with short sleek hair, opaque crisp white high-neck blouse, black high-waist full wide trousers and black low heels, small silver earrings; natural crossed arms, frontal grounded stance, keen direct gaze and confident unsmiling lips, no aggression props
威严|深紫高领礼装|majestic purple ceremonial outfit|深紫高领长礼服配窄披肩；中央金属扣件克制，站姿中正，眉眼庄重|Adult35 woman with dark braided updo, opaque deep-purple high-neck long-sleeve ankle ceremonial gown with narrow capelet and one simple gold clasp, closed heels; perfectly centered upright posture, hands calmly overlapped, dignified level gaze and solemn mouth, no crown or real religious symbols
威严|墨蓝长外衣仪典装|majestic midnight formal coat outfit|墨蓝长外衣与灰白内搭；竖向装饰线突出秩序，双臂垂落，视线平直|Adult35 olive-skinned woman with salt-and-pepper hair in low bun, opaque midnight-blue long formal coat over gray high-neck top and dark full trousers, black boots; sparse original vertical gold piping without real badges, still balanced stance with arms at sides, solemn authoritative level gaze
''')
block('androgynous_ornate','中性与华丽','''
中性|短发宽版西装造型|androgynous loose tailoring outfit|利落短发、宽版灰西装与白圆领；直线轮廓、低跟牛津鞋，姿态自然|Adult28 woman with dark pixie cut, charcoal loose boxy blazer over opaque white crewneck, matching full straight trousers and black flat Oxford shoes; clean straight silhouette, hands loosely in pockets, calm natural level gaze, feminine adult identity without exaggerated curves
中性|马甲长裤领带造型|androgynous waistcoat-and-tie outfit|米白衬衣、黑马甲与宽腿长裤；细领带和后梳短发，目光平静，手势简洁|Adult28 woman with dark slicked-back short hair, opaque ivory button shirt and narrow black tie, black waistcoat and full wide trousers, black loafers; one hand adjusting opposite cuff, relaxed upright stance, clear adult female face and natural proportions, understated expression
华丽|宝蓝层裙舞会装|ornate royal-blue ball outfit|宝蓝长裙配金色提花与层叠袖口；珠饰集中在领口，姿态舒展，笑容从容|Adult30 deep-brown-skinned woman with dark elaborate braided updo, opaque royal-blue long-sleeve ankle ball gown with original gold brocade panels and layered sleeve cuffs, covered modest neckline with small pearl trim, gold closed heels; one hand gently holds a little skirt side, confident graceful small smile, no crown
华丽|酒红羽饰礼服造型|ornate burgundy feather-detail outfit|酒红长礼服配少量肩侧羽饰与金色耳坠；衣料分层明显，侧身轻转，目光大方|Adult30 woman with brown sculpted wavy updo, opaque burgundy long-sleeve ankle evening gown with a SMALL decorative feather cluster on one shoulder and layered satin skirt, gold drop earrings and closed heels; slight elegant torso turn, one hand rests at waist, composed radiant smile, no lingerie or huge wings
''')

next(c for c in CATEGORIES if c['id']=='persona_looks')['guide']='48种创作表现标签，各有两套全身搭配；通过衣物、表情、视线和动作共同表现，可跨标签混搭。标签不用于根据外貌判断真实人格；萌与孩子气表演均为成年角色。'
assert len(NEW_ENTRIES)==48 and len(SYNONYMS)==24 and len(GROUPS)==12
