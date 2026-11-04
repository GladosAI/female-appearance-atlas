"""Adult character styling and performance tags, distinct from age and coverage."""
from catalog_content import CATALOG,category,add

category('persona_looks','气质与性格表演造型','24种创作表现标签，各有两套全身搭配；通过衣物、表情、视线和动作共同表现，可跨标签混搭。标签不用于根据外貌判断真实人格；萌与孩子气表演均为成年角色。',['R06'])
category('coverage_looks','露肤与服装覆盖程度','8套成年服装对照，从完整覆盖到肩、背、腰、腿、领口、侧面和多部位露肤。性感气质与露肤面积分别记录；图例均为完整服装，无裸露私密部位。',['R06'])
NEW_CATEGORIES=['persona_looks','coverage_looks']
NEW_ENTRIES=[]
GROUPS=[]
SYNONYMS={
    '萌':['可爱','甜美'],'成熟':['轻熟','成熟感'],'性感':['妩媚','性感气质'],
    '典雅':['优雅','端庄'],'呆':['天然呆','呆萌','愣神'],'幼稚':['孩子气','稚气表演'],
    '活泼':['元气','青春活力'],'沉稳':['稳重','沉着'],'冷酷':['冷峻','严厉'],
    '高冷':['清冷','疏离','冰山感'],'傲娇':['别扭','口嫌体正直表演'],'含蓄':['内敛','克制'],
    '外向':['开朗','热情'],'内向':['文静','安静'],'谨慎':['小心','警觉'],
    '自信':['笃定','从容自信'],'温柔':['柔和','温婉'],'飒爽':['英气','利落'],
    '干练':['精干','职业感'],'知性':['书卷气','理性沉静'],'慵懒':['松弛','闲适'],
    '神秘':['神秘感','难以捉摸'],'张扬':['鲜明','大胆'],'叛逆':['不羁','反叛']}

def block(key,title,traits,text):
    GROUPS.append((key,'persona_looks',title))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(label,name,en,desc,recipe) in enumerate(rows,1):
        assert label in traits
        add('persona_looks',label,f'{label}·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(persona_reference=True,persona_tag=label,persona_group=key,persona_order=i,
            added_in='45.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
            aliases=[label,'气质','性格表演','代表造型',*SYNONYMS[label]],note='原创25岁以上成年角色的创作表演标签。服装、视线、嘴角、肩肘与重心共同组织视觉效果；同一标签有两套搭配，可与其他标签混合，不把外貌当作真实人格证据。萌、呆与孩子气不是年龄分类。')
        NEW_ENTRIES.append(e)

block('cute_mature','萌与成熟',['萌','成熟'],'''
萌|软色针织裙装|cute pastel-knit outfit|奶油开衫、浅粉中长裙与圆头鞋；明亮眼神、小幅微笑和双手轻握|Clearly adult25 woman, mature adult face and7-head proportions, warm brown shoulder-length hair, cream cardigan over opaque crewneck, blush-pink calf-length A-line skirt, round flats; bright eyes, small cheerful smile, hands loosely clasped in front, cute through gentle color and expression
萌|缎带休闲裤装|cute ribbon casual outfit|薄荷短夹克、白色圆领内搭与宽直长裤；小缎带点缀，轻抬一手问候|Adult25 woman, dark-brown high ponytail with small mint ribbon, mint cropped casual jacket over opaque white crewneck, ivory wide trousers, white sneakers; friendly wave and bright smile, adult proportions, no school uniform
成熟|深色收腰通勤装|mature tailored city outfit|深酒红西装、米白内搭与炭灰直裤；低位盘发，神态从容|Adult28 woman, low dark-brown bun, burgundy tailored blazer over ivory high-neck top, charcoal straight trousers, black low heels, small structured bag; calm poised expression and relaxed upright stance
成熟|缎面中长裙装|mature satin-midi outfit|烟灰长袖衬衣与藏蓝缎面中长裙；少量耳饰，肩颈舒展|Adult28 woman, softly waved shoulder-length brown hair, smoke-gray opaque long-sleeve blouse, navy satin calf-length skirt, small silver earrings and pumps; composed gentle smile, one hand lightly holding handbag, no cleavage focus
''')
block('sensual_elegant','性感与典雅',['性感','典雅'],'''
性感|修身垂褶礼裙|sensual draped evening outfit|酒红不透明长裙、侧腰垂褶与小开衩；舒展站姿，目光自信|Clearly adult28 woman, dark swept-back hair, opaque burgundy sleeveless draped midi evening dress with modest V neckline and below-mid-thigh side slit, simple black heels; relaxed confident eye contact and subtle closed-mouth smile, natural adult proportions, tasteful fashion portrait
性感|方领针织铅笔裙装|sensual square-neck pencil outfit|黑色方领长袖上衣与驼色铅笔裙；贴合剪裁表现曲线，双手自然垂落|Adult28 woman, black opaque square-neck long-sleeve knit top and camel knee-length pencil skirt, slim belt and dark pumps; natural adult curvy silhouette without exaggeration, assured restrained gaze, arms relaxed at sides
典雅|提花长裙礼装|elegant jacquard dress outfit|墨绿长袖提花长裙、珍珠耳钉与低跟鞋；闭口微笑，双手轻叠|Adult28 woman, neat brown low bun, opaque forest-green high-neck long-sleeve ankle-length jacquard dress, tiny pearl studs, low heels; refined straight posture, hands lightly overlapped at waist, quiet closed-mouth smile
典雅|盘扣中长裙装|elegant knot-button midi outfit|米白盘扣短上衣配蓝灰长裙；装饰克制，步幅与手势轻缓|Adult28 woman, swept-up brown hair, ivory opaque standing-collar short jacket with original simple knot buttons, blue-gray long A-line skirt and plain flats; one small gentle step, restrained hand gesture, refined serene expression, original modern design
''')
block('blank_childish','呆与孩子气表演',['呆','幼稚'],'''
呆|捧杯空白反应|blank cup-holding reaction|宽松衬衣与直筒长裤；捧住杯子，眼神短暂停顿，嘴唇微张|Clearly adult25 woman with mature adult face, pale-blue loose shirt and cream straight trousers, loafers; holds one plain mug in both hands, softly blank unfocused gaze, lips barely parted, small head tilt, no caricature or child proportions
呆|双手垂落愣神|blank standing reaction|浅灰圆领衫与中长伞裙；双臂放松，眉眼暂时失去回应|Adult25 woman, gray opaque crewneck sweater and navy calf-length A-line skirt, white flats; arms hanging naturally, mild wide-eyed paused reaction and neutral small mouth, fully upright stance, no exaggerated stupidity caricature
幼稚|鼓脸抱枕表演|adult childish pout with cushion|成年休闲卫衣与宽腿长裤；抱小靠垫、鼓起脸颊，表现孩子气的不服气|Clearly ADULT25 woman, mature face and adult body, coral oversized sweatshirt, charcoal wide trousers and sneakers; hugging a small plain cushion, puffed cheeks and playful stubborn pout, childish ACTING by an adult, no toddler clothes or child body
幼稚|小幅跺脚表演|adult childish foot-stamp acting|彩色短夹克与牛仔长裤；手肘收起、轻抬一脚，嘴角撅起|Clearly adult25 woman, teal casual jacket over opaque cream T-shirt, full-length jeans and sneakers; a small playful foot-stamp with one heel slightly lifted, elbows close to body and tiny pout, adult proportions, no school uniform or babyish accessories
''')
block('lively_steady','活泼与沉稳',['活泼','沉稳'],'''
活泼|撞色运动休闲装|lively color-block casual outfit|奶白棒球夹克、橙红内搭和直筒裤；招手迈步，头发轻动|Adult25 woman, brown high ponytail, cream bomber jacket with coral trim over opaque orange-red crewneck, charcoal straight trousers, sneakers; lively small step and friendly raised wave, bright open smile, full hands and shoes
活泼|短外套褶裙装|lively jacket-and-pleat outfit|钴蓝短外套、白内搭与及膝褶裙；张开一只手臂，神态轻快|Adult25 woman, cobalt cropped jacket over opaque white round-neck top, cream knee-length pleated skirt, white sneakers; cheerful half-turn and one arm extending in a welcoming gesture, lightly moving hair, balanced adult anatomy
沉稳|大地色直线套装|steady earth-tone outfit|棕灰夹克、深色内搭与宽直裤；双脚稳定，目光平和|Adult28 woman, dark low ponytail, taupe structured jacket over dark high-neck top, matching wide straight trousers, low leather shoes; balanced feet, arms relaxed, calm level gaze and still shoulders
沉稳|长开衫中裙装|steady long-cardigan outfit|深蓝长开衫与灰色中长裙；双手轻握，重心平稳|Adult28 woman, shoulder-length brown hair, navy long cardigan over opaque gray crewneck, charcoal midi skirt and flats; hands loosely clasped at lower waist, grounded balanced stance, composed soft neutral mouth
''')
block('ruthless_aloof','冷酷与高冷',['冷酷','高冷'],'''
冷酷|硬线条黑色裤装|stern black tailored outfit|黑色短外套、直裤和靴；眉线压低、唇线收紧，肩部保持硬朗|Adult28 woman, slick dark bob, black opaque structured cropped jacket and full straight trousers, black ankle boots; firm level shoulders, slightly narrowed eyes and tightly controlled closed lips, hands at sides, no weapon or threatening action
冷酷|深灰皮革叠穿|stern leather-layer outfit|深灰皮外套与黑高领；双手戴短手套，视线直接而克制|Adult28 woman, dark hair tied low, charcoal leather jacket over black opaque turtleneck, dark trousers and short gloves, boots; direct cool stare, flat brows, unsmiling firm mouth, relaxed still hands, no violence props
高冷|冷色长大衣造型|aloof cool-tone coat outfit|灰蓝长大衣配奶白高领与长裤；视线略越过观者，表情疏离|Adult28 woman, long smooth dark hair, blue-gray long coat over ivory opaque turtleneck, navy tailored trousers, sleek flats; chin level, eyes looking slightly past viewer, quiet distant expression without angry brows, upright elegant stance
高冷|极简高领裙装|aloof minimalist dress outfit|烟灰高领中长裙与简洁短靴；手臂自然下垂，少量表情变化|Adult28 woman, neat dark low bun, smoke-gray opaque high-neck long-sleeve midi dress and clean ankle boots; long composed silhouette, relaxed arms, reserved distant calm gaze, lips neutral, no hostile grimace
''')
block('tsundere_reserved','傲娇与含蓄',['傲娇','含蓄'],'''
傲娇|抱臂别脸表演|tsundere crossed-arm acting|短夹克与高腰长裤；抱臂、脸转开而视线回看，嘴角微撅|Clearly adult25 woman, burgundy casual cropped jacket over ivory opaque crewneck, high-waist charcoal trousers, loafers; arms folded naturally, head turned slightly away but eyes glance back, tiny pout and subtle blush, adult playful acting
傲娇|拎包轻哼表演|tsundere restrained huff acting|浅色衬衣与膝下直裙；握住包带，眉梢微抬、唇线轻抿|Adult25 woman, pale blue long-sleeve blouse and charcoal calf-length straight skirt, low heels; one hand grips small shoulder-bag strap, face a little averted, raised outer brow and faint closed-lip huff, mature adult face
含蓄|小幅微笑针织装|reserved soft-smile outfit|米白针织衫与雾粉中裙；双手轻叠，微笑幅度较小|Adult25 woman, ivory opaque round-neck knit top and muted rose midi skirt, simple flats; hands gently overlapped below waist, soft restrained eye contact and tiny closed-mouth smile, shoulders natural
含蓄|衬衣宽裤造型|reserved blouse-and-trousers outfit|灰蓝衬衣与奶油宽裤；轻捏袖口，视线温和停留|Adult25 woman, blue-gray opaque blouse with normal closed neckline and cream wide trousers, brown loafers; one hand lightly touches opposite cuff, gentle quiet eye contact and subtle smile, upright adult posture
''')
block('outgoing_introverted','外向与内向表演',['外向','内向'],'''
外向|开放手势休闲装|outgoing open-gesture casual outfit|橘色开衫、白内搭与蓝牛仔；一手挥动、一手摊开，笑容明显|Adult25 woman, orange cardigan over opaque white crewneck, blue full-length jeans, sneakers; one hand waving and other palm open at waist, warm bright smile, open relaxed shoulders
外向|主动问候裙装|outgoing greeting skirt outfit|浅绿短外套与及膝裙；身体略转向交流对象，手势主动|Adult25 woman, pale green casual jacket and cream knee-length A-line skirt, white flats; welcoming palm gesture and small forward step toward viewer, lively conversational smile, clear adult proportions
内向|近身持书造型|introverted close-held-book outfit|藏蓝开衫与灰色直裤；书本靠近身前，手肘内收，笑容轻微|Adult25 woman, navy cardigan over opaque gray top, straight gray trousers, loafers; holds one closed plain book close to torso, elbows near ribs, small quiet smile, gaze slightly lowered but face readable
内向|轻握包带裙装|introverted bag-strap outfit|浅褐长袖衫与深色中裙；双手轻握细包带，站姿收敛|Adult25 woman, tan opaque long-sleeve crewneck top, dark calf-length skirt and flats; both hands loosely holding small bag strap in front, compact relaxed posture, gentle averted gaze and restrained smile, not fearful
''')
block('cautious_confident','谨慎与自信表演',['谨慎','自信'],'''
谨慎|侧看观察行旅装|cautious observing travel outfit|卡其短风衣与长裤；目光先向侧方确认，一手稳住包带|Adult28 woman, khaki short trench over opaque ivory top, navy trousers and practical low shoes; one hand secures crossbody strap, head slightly turned to scan to the side, attentive brows and restrained movement, no panic
谨慎|迈步前停顿造型|cautious paused-step outfit|灰色外套、深蓝中裙与短靴；脚步轻停，双手靠近身体|Adult28 woman, gray jacket over opaque light top, navy midi skirt and ankle boots; one foot lightly paused before stepping, elbows close to torso, alert side glance with focused neutral mouth, balanced stable body
自信|直立西装宽裤装|confident tailored-trouser outfit|酒红西装与黑色宽裤；下颏平稳，单手自然扶腰|Adult28 woman, burgundy blazer over opaque cream crewneck, black wide trousers and pumps; tall relaxed upright stance, one hand rests lightly on waist, steady direct gaze and small assured smile
自信|简洁收腰连裙装|confident clean-line dress outfit|钴蓝长袖中裙与细腰带；肩部打开，双臂轻松下垂|Adult28 woman, cobalt opaque long-sleeve calf-length dress with thin belt, simple heels; open relaxed shoulders and arms down, calm assured eye contact, poised adult figure without exaggerated curves
''')
block('gentle_brisk','温柔与飒爽',['温柔','飒爽'],'''
温柔|柔色开衫长裙装|gentle soft-cardigan outfit|浅杏开衫与淡蓝长裙；眉眼舒展，一手轻伸作回应|Adult28 woman, soft apricot cardigan over opaque ivory blouse, pale blue ankle-length flowing skirt and flats; relaxed brows and warm gentle smile, one open hand extended a little at waist
温柔|棉衬衣宽裤装|gentle cotton-shirt outfit|奶白棉衬衣与浅咖宽裤；手势轻缓，目光有回应感|Adult28 woman, ivory opaque cotton long-sleeve shirt, light coffee wide trousers and brown flats; one hand loosely resting over other wrist, soft attentive eyes and gentle smile, relaxed posture
飒爽|短皮衣利落裤装|brisk leather-jacket outfit|短皮衣、白内搭与高腰长裤；短发向侧方轻扬，站姿利落|Adult28 woman, short brown bob lightly swept to one side, black cropped leather jacket over opaque white crewneck, charcoal high-waist trousers and boots; brisk upright pose with one hand on hip, focused confident small smile
飒爽|风衣迈步造型|brisk trench walking outfit|蓝灰短风衣与黑直裤；迈步带动衣摆，手臂动作干净|Adult28 woman, low brown ponytail, blue-gray short trench over opaque top, black straight trousers and lace-up shoes; crisp walking stride with modest coat movement, direct bright eyes and controlled confident smile, complete feet
''')
block('efficient_intellectual','干练与知性',['干练','知性'],'''
干练|短西装文件夹造型|efficient blazer-and-folder outfit|灰色短西装与直裤；文件夹握在身侧，目光专注|Adult28 woman, neat dark bob, gray tailored short blazer over opaque ivory blouse, matching straight trousers, low pumps and simple watch; one plain closed folder held at side, focused level gaze and practical upright stance
干练|卷袖衬衣长裤装|efficient rolled-sleeve outfit|卷袖衬衣、细皮带与锥形裤；袖口整齐，姿态简洁|Adult28 woman, dark low bun, blue opaque button shirt with neatly rolled sleeves, charcoal tapered trousers and brown loafers; straight stance, one hand lightly checks cuff, attentive expression, no office logos
知性|眼镜衬衣中裙装|intellectual glasses-and-skirt outfit|细框眼镜、米白衬衣与棕色中裙；翻看书页，神态沉静|Adult28 woman, thin round spectacles and shoulder-length dark hair, ivory opaque blouse, brown calf-length skirt, loafers; holds an open plain book at waist and looks thoughtfully toward viewer, calm engaged eyes, no readable text
知性|针织马甲阅读装|intellectual knit-vest outfit|灰蓝针织马甲叠衬衣与宽裤；书本收在臂侧，目光思索|Adult28 woman, brown low ponytail, gray-blue knit vest over opaque white long-sleeve shirt, cream wide trousers and flats; one closed plain book under arm, thoughtful calm gaze and small smile, no spectacles needed
''')
block('languid_mysterious','慵懒与神秘',['慵懒','神秘'],'''
慵懒|宽松针织休闲装|languid loose-knit outfit|宽针织衫与柔软长裤；眼睑稍低，肩部放松，双手收在袖边|Adult28 woman, loose brown shoulder-length hair, opaque oatmeal oversized crewneck knit top and relaxed dark trousers, soft loafers; relaxed shoulders, half-lidded calm eyes and tiny sleepy smile, hands lightly at sleeve cuffs, standing fully clothed
慵懒|长开衫轻伸展|languid cardigan stretch outfit|奶白长开衫与完整内搭、长裙；一手轻触颈侧，动作缓慢|Adult28 woman, ivory long cardigan over opaque gray crewneck and navy midi skirt, flats; one hand gently touches side of neck in a small relaxed stretch, soft half-lidded eyes, unhurried stance, no yawning mouth closeup
神秘|深色连帽长外衣|mysterious hooded-coat outfit|深紫连帽外衣配完整长裙；帽缘形成阴影，面部仍清楚|Adult28 woman, deep purple hooded long coat over opaque charcoal high-neck ankle dress, black boots; hood frames face without hiding eyes, composed unreadable small smile, hands relaxed together, no weapons or glowing effects
神秘|暗色层裙礼装|mysterious dark layered outfit|深蓝长袖层裙、银色小吊坠；眼神略侧，动作停留在半途|Adult28 woman, dark long hair, opaque midnight-blue long-sleeve layered ankle dress with small silver pendant, low boots; sideways thoughtful gaze and restrained neutral lips, one hand paused near pendant without gripping chest, subtle quiet mood
''')
block('bold_rebellious','张扬与叛逆',['张扬','叛逆'],'''
张扬|鲜色宽肩街头装|bold bright street outfit|红色宽肩短外套与黑色宽裤；一手扶腰，目光直接，轮廓鲜明|Adult25 woman, brown high ponytail, bright red oversized-shoulder cropped jacket over opaque black crewneck, black wide trousers and chunky sneakers; hand on hip, playful assured direct gaze, striking silhouette, no logos
张扬|撞色几何裙装|bold color-block skirt outfit|钴蓝上衣、橘色中裙与白鞋；手臂舒展，笑容带一点自得|Adult25 woman, cobalt opaque long-sleeve top and orange calf-length geometric A-line skirt, white low shoes; one arm opens outward confidently, small proud closed-mouth smile, bold but coordinated colors, adult fashion
叛逆|不对称皮衣牛仔装|rebellious asymmetric leather outfit|不对称皮夹克、素色内搭与破洞外层牛仔；下颏微抬，手插袋|Adult25 woman, side-swept dark bob, asymmetric black leather biker jacket over opaque white tee, distressed full jeans with opaque fabric beneath tears, boots; hands in pockets, chin slightly raised and defiant restrained gaze, no weapon or smoking
叛逆|格纹叠层裤装|rebellious plaid-layer outfit|暗红格纹衬衣叠黑内搭与工装裤；肩带饰件少量使用，站姿随性|Adult25 woman, brown low ponytail with small dark clip, unbuttoned dark-red plaid shirt over opaque black crewneck, charcoal full cargo trousers and lace-up boots; relaxed asymmetrical stance with one elbow out, wry small smile, no gang emblems
''')

COVERAGE=[
('完整覆盖','高领长袖长裤','fully covered outfit','高领、长袖与完整长裤，肩背腰腹均覆盖','Adult25 woman, medium-light skin, brown low bun, opaque ivory turtleneck long sleeves, navy full-length straight trousers, black flats, all torso shoulder back waist and legs covered'),
('露肩','一字肩中长裙','exposed-shoulder outfit','肩部开放，胸腹与腿部保持较多覆盖','Same adult25 woman, brown low bun, opaque blue-gray off-shoulder LONG-SLEEVE calf-length dress with securely supported bodice, black low heels, only shoulder tops exposed'),
('露背','背开口长裙','open-back outfit','以背面视角显示后背开口，前胸和腰下覆盖','Same adult25 woman shown REAR THREE-QUARTER, opaque forest-green long-sleeve ankle dress, a modest oval upper-back opening ending ABOVE waist, covered front and skirt, full heels visible'),
('露腰','短上衣高腰裤','waist-gap outfit','上衣与裤腰之间留窄幅腰部间隙，其余部位覆盖','Same adult25 woman, opaque cream long-sleeve cropped crewneck ending just above high-waist charcoal wide trousers, a narrow natural midriff band visible, sneakers, no low-rise or deep neckline'),
('露腿','长袖上衣短裙','exposed-leg outfit','上身完整长袖覆盖，短裙使腿部露肤增加','Same adult25 woman, opaque navy high-neck long-sleeve top and cream A-line skirt to mid-thigh, bare legs and simple flats, upright neutral fashion stance, no stockings'),
('领口开放','V领中长连衣裙','open-neckline outfit','V形领口开放，上臂与腰下保持完整衣料','Same adult28 woman, opaque burgundy long-sleeve midi dress with moderately deep V neckline, securely covered breasts, natural adult proportions, low heels, no breast emphasis or exaggerated cleavage'),
('侧面开口','腰侧镂空长裙','side-cutout outfit','长裙在两侧腰部留小开口，正面胸腹仍有连接衣片','Same adult25 woman, opaque black high-neck sleeveless ankle dress with TWO SMALL waist-side cutouts only, continuous broad central torso panel and full skirt, low heels, front three-quarter view'),
('暴露／高露肤','两件式泳装示例','high-skin-exposure swimwear','用完整两件式泳装表现多部位露肤，胸部与裆部由不透明衣料覆盖','Same clearly ADULT25 woman, brown low bun, opaque simple navy two-piece bikini with ordinary securely covered top and moderate-rise moderate-coverage bottoms, no thong, no transparency; neutral upright fashion stance, arms relaxed at sides away from body, bare feet fully visible, no sexual pose')
]
for start in [0,4]:
    key='coverage_a' if start==0 else 'coverage_b';GROUPS.append((key,'coverage_looks','覆盖程度对照·'+('基础露肤区域' if start==0 else '领腿侧面与高露肤')))
    for i,(dim,name,en,desc,recipe) in enumerate(COVERAGE[start:start+4],1):
        add('coverage_looks',dim,f'覆盖对照·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(coverage_reference=True,coverage_group=key,coverage_kind=dim,coverage_order=start+i,
            added_in='45.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
            aliases=['露肤','覆盖程度',dim]+(['暴露','高露肤','多部位露肤'] if dim=='暴露／高露肤' else []),note='原创25岁以上成年服装覆盖对照。露肤区域与性感、典雅等气质标签是不同维度；服装开口、固定与遮挡可单独组合，图例不把面积作为人格或价值判断。')
        NEW_ENTRIES.append(e)
assert len(NEW_ENTRIES)==56
