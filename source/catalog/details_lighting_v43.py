"""Local-form studies and controlled light/cloth comparisons for adult character art."""
from catalog_content import CATALOG,category,add

NEW_CATEGORIES=['hands','nose_ear_teeth','skin_details','portrait_lighting','garment_dynamics']
category('hands','手部形态与握持','16项独立手部近景，分掌指结构与表面、握持与接触；比较掌型、指长、骨节、手背、拇指对指和接触点。完整保留相关指尖与物件。',['R166'])
category('nose_ear_teeth','局部五官近景','24项局部绘画参考，鼻部、耳廓耳垂、牙齿与露齿各8项。名称描述轮廓，不作美丑、健康或人群分类。',['R167','R168','R169'])
category('skin_details','皮肤局部纹理与痕迹','16项面颈、手部、四肢的自然局部纹理，包含毛孔、细纹、关节褶皱、细毛、雀斑、胎记与晒痕。细节略作放大便于绘画观察，不作医学诊断。',['R166'])
category('portrait_lighting','脸部光照与明暗','同一原创成年面孔、同一正面机位、发型与中性表情的8种布光示意；比较鼻影、眼窝、颊部明暗和轮廓光。切换分类图页可同时看整组。',['R170'])
category('garment_dynamics','衣物褶皱与动态','两套固定服装各8项：棉衬衫长裤与长袖连衣裙。各组采用同一成年人物与同款衣物，比较站立、坐姿、抬手、屈蹲、行走和风吹时的受力与褶皱。',['R171'])

GROUPS=[
 ('hand_structure','hands','掌指结构与表面'),('hand_contact','hands','握持与接触'),
 ('nose','nose_ear_teeth','鼻部近景'),('ear','nose_ear_teeth','耳廓与耳垂近景'),('teeth','nose_ear_teeth','牙齿与露齿近景'),
 ('skin_face','skin_details','面颈与手部纹理'),('skin_body','skin_details','四肢与日常皮肤痕迹'),
 ('lighting','portrait_lighting','同一面孔·八种布光'),('cotton','garment_dynamics','衬衫长裤·动作与受力'),('dress','garment_dynamics','长袖连衣裙·受力对照')]

def block(group,text):
    _,cid,dim=next(g for g in GROUPS if g[0]==group);rows=[x.strip().split('|') for x in text.strip().splitlines()];assert len(rows)==8
    for order,(name,en,focus,view,recipe) in enumerate(rows,1):
        add(cid,dim,f'{name}|{en}|观察：{focus}；{view}。')
        CATALOG[-1].update(added_in='43.0',study_reference=True,study_group=group,study_order=order,study_focus=focus,study_view=view,
            adult_only=True,minor_reference=False,age_min=25,illustration_recipe=recipe,
            reference_ids={'hands':['R166'],'nose_ear_teeth':[{'nose':'R167','ear':'R168','teeth':'R169'}.get(group,'R169')],'skin_details':[],'portrait_lighting':['R170'],'garment_dynamics':['R171']}[cid],
            note='原创成年角色绘画示意，细节与明暗为观察用途；不规定唯一外貌，也不作医学判断。手部核对拇指、其余四指及接触点；局部形态与光线分别理解。衣物褶皱需结合材质、重力、支撑和动作，不将示意当作布料模拟结果。')

block('hand_structure','''
手型近景·窄长掌面|long narrow palm|掌长相对掌宽的关系|右手掌面，五指放松伸展|One complete adult female RIGHT hand PALM facing viewer, long narrow palm, average-length fingers relaxed and separated, thumb on viewer LEFT, plain short nails, whole wrist to fingertips in frame
手型近景·宽短掌面|broad compact palm|掌宽与短掌轮廓|右手掌面，手腕保持自然|One complete adult female RIGHT hand PALM facing viewer, visibly broad compact palm, normal relaxed fingers and thumb, thumb on viewer LEFT, whole wrist and every fingertip
手型近景·修长指列|slender long fingers|指长、指缝与掌型|右手背面，五指轻微分开|One adult female RIGHT hand BACK facing viewer, slender long fingers, medium palm, thumb on viewer RIGHT, five total fingers with unpainted short nails, wrist-to-tips complete
手型近景·短指列|compact short fingers|较短指列与圆钝指端|右手背面，同角度观察|One adult female RIGHT hand BACK, visibly shorter compact fingers relative to palm, thumb on viewer RIGHT, natural relaxed separation, short plain nails, all tips visible
手背近景·骨节起伏|pronounced knuckle contours|掌指关节与腱线起伏|右手背面，轻微屈指|Adult female right hand BACK, five fingers gently curved without fist, clear but natural knuckle bumps and subtle extensor tendons, no skeletal exaggeration, all fingertips visible
手背近景·柔和轮廓|soft-contour hand back|骨节较柔和时的体积|右手背面，手指自然放松|Adult female right hand BACK, soft rounded knuckle contours and smoother hand back, five relaxed fingers, natural proportions, full wrist-to-fingertips
掌面近景·指根褶线|palm and finger-base creases|掌丘、指根与屈曲褶线|右手掌面，近距离完整手掌|Adult female right PALM with five fingers loosely open, detailed natural palm creases and finger-base folds, normal thenar pad at thumb base, whole hand in view, no labels or palm-reading symbols
手指近景·拇食指对指|thumb-index opposition|拇指旋转与指腹接触|右手侧前视，另外三指自然弯曲|One adult female right hand, thumb pad touching index fingertip softly to form a small loose circle, other three fingers naturally curled but individually visible, side-three-quarter view, five digits total
''')
block('hand_contact','''
握持近景·杯柄接触|hand holding cup handle|指腹与杯柄的接触关系|右手侧前视，完整杯柄与指尖|One adult female right hand holding a plain ceramic mug by its handle, index and middle fingers through handle, thumb resting above, remaining fingers naturally curled, mug and whole hand visible
握持近景·执笔书写|writing grip contact|拇食中指的三点支撑|右手侧前视，笔尖贴近纸面|One adult female right hand holding a pencil in ordinary tripod writing grip over a small plain sheet, thumb/index pinch and pencil resting on middle finger, ring and little fingers gently bent, five total digits
握持近景·手机边缘|smartphone edge grip|手掌与手机背面承托|右手背侧视，完整手机与手指|One adult female right hand holding an upright blank-screen smartphone, thumb on near edge and other four fingers wrapping behind, show anatomically plausible grip, five digits total
握持近景·书脊与书页|book-edge support|拇指压页与其余手指承托|右手侧面，露出接触边界|One adult female right hand supporting a small plain closed book from below, thumb on front cover near spine, other four fingers under book, complete wrist and book, no printed words
握持近景·提带受力|bag-strap load contact|提带压向弯曲手指的位置|右手侧前视，包带与指节完整|One adult female right hand carrying two narrow fabric bag handles, four fingers curled under handles, thumb resting across index side, slight skin compression at contact, only a small plain bag top below
握持近景·托住圆球|cupped sphere support|掌心、指腹与球体接触|右手掌侧视，指尖围合但不穿透|One adult female right hand cupping a small matte ball, thumb on one side and four fingers wrapping around opposite side, all digit roots plausible, sphere and whole hand visible
接触近景·掌根撑桌|palm-heel table contact|掌根、指腹与桌面的支撑|右手侧前视，前臂短段完整|One adult female right hand resting palm-down on a plain tabletop, five fingers relaxed spread, palm heel and fingertips touching surface, subtle contact shadow, complete hand and short wrist
接触近景·指尖捏布|fingertip fabric pinch|拇食指夹点与放射褶线|右手侧前视，另三指放松|One adult female right hand gently pinching a small corner of opaque cotton fabric between thumb and index, other three fingers relaxed, visible radial cloth folds from contact point, no body or clothing being undressed
''')
block('nose','''
鼻部近景·直梁侧影|straight bridge profile study|鼻背连续线与鼻尖转折|同一观察尺度的侧面局部|Close-up side profile of an adult woman's nose with straight bridge, include brow base to upper lip, neutral warm skin, subtle light, no whole face
鼻部近景·弧梁侧影|convex bridge profile study|鼻背轻弧与鼻尖位置|侧面局部，保留鼻翼根部|Close-up side profile adult female nose with gently convex bridge, natural tip and nostril, brow base to upper lip, no exaggeration
鼻部近景·圆钝鼻尖|rounded nose-tip study|鼻尖体积与鼻翼过渡|侧前三分视角|Adult female nose close-up at three-quarter view, rounded softly defined tip, natural alar wings and nostril shadows, brow-to-upper-lip crop
鼻部近景·上翘鼻尖|upturned nose-tip study|鼻尖朝向与鼻孔可见程度|侧面局部，保持正常比例|Adult female nose side close-up, subtly upturned tip, natural nostril aperture and philtrum, realistic restrained proportions
鼻部近景·较宽鼻翼|broad alar-base study|正面鼻翼宽度与鼻底形|正面局部，左右结构完整|Adult female nose frontal close-up, broad natural alar base, rounded tip and symmetric nostrils, upper lip edge below, neutral lighting
鼻部近景·较窄鼻翼|narrow alar-base study|较窄鼻翼与鼻尖体积关系|正面局部，同尺度观察|Adult female nose frontal close-up, narrower natural alar base, clear nose-tip volume and nostril wings, same neutral light and crop scale
鼻部近景·低机位鼻底|underside nose-base study|鼻小柱、鼻孔与鼻翼连接|轻微仰视局部，不夸大透视|Adult female nose close-up viewed slightly from below, readable columella and nostril shapes, alar connection, tasteful neutral study, no mouth opening
鼻部近景·侧前转面|three-quarter nose-plane study|鼻背、侧壁与鼻翼受光面|侧前三分视角，弱侧光|Adult female nose three-quarter close-up, moderate bridge and tip, gentle side illumination showing bridge plane, sidewall and alar plane, no diagram arrows
''')
block('ear','''
耳部近景·贴附耳垂|attached earlobe study|耳垂与面颊的连续连接|成年女性侧面局部|Adult woman's natural ear side close-up, attached earlobe smoothly joining cheek, hair tucked away, complete helix and ear base, no jewelry
耳部近景·悬垂耳垂|free earlobe study|独立垂下的耳垂轮廓|同尺度侧面局部|Adult woman's natural ear side close-up, free hanging earlobe distinct from cheek, complete ear, no jewelry, natural skin shading
耳部近景·宽耳轮|broad helix study|外耳轮宽度与耳舟间隙|侧面近景，完整耳廓|Adult female ear side close-up, broader rounded outer helix, clear antihelix and concha, no pointed elf shape, complete ear
耳部近景·薄耳轮|slender helix study|较薄耳缘与内侧起伏|侧面近景，同角度观察|Adult female ear side close-up, slender outer helix rim, normal inner ear folds and earlobe, no jewelry, full contour
耳部近景·对耳轮分叉|antihelix branching study|对耳轮分叉与耳甲腔体积|侧前近景，阴影保持清楚|Adult female ear close-up, clear natural Y-shaped antihelix branches and concha hollow, restrained educational realism, hair tucked away
耳部近景·耳屏与耳甲|tragus and concha study|耳屏、耳甲与开口边界|侧前三分视角|Adult female ear close-up viewed slightly from front, natural tragus and concha shape, ear canal entrance softly shadowed, no medical instruments
耳部近景·后侧耳根|rear ear-root study|耳后沟与头部连接|后侧三分视角|Adult female ear viewed from rear-three-quarter, complete helix and earlobe, clear ear-root attachment and shallow groove behind ear, hair lifted away
耳部近景·正面外展|frontal ear-projection study|正面可见耳缘与外展角度|单侧耳廓与少量面颊|Adult female ear from near-frontal view, ear slightly projects outward naturally, visible outer rim and lobe against cheek, no whole face or jewelry
''')
block('teeth','''
露齿近景·自然整齐牙列|aligned-teeth smile study|牙列整体弧线与明暗分组|成年女性口部微笑近景|Close-up adult woman's natural gentle open-lip smile showing an aligned upper tooth row, teeth as soft grouped forms with subtle boundaries, no heavy black outlines or full face
露齿近景·轻微门牙缝|small central tooth-gap study|中切牙之间的小间隙|同尺度轻微露齿|Adult female mouth close-up, relaxed small smile with a subtle small gap between the two upper central incisors, healthy natural ivory teeth, no exaggeration
露齿近景·虎牙识别点|canine accent smile study|犬齿尖端与邻牙轮廓|侧前微笑局部|Adult female gentle smile close-up with one naturally slightly prominent upper canine tip, not vampire fangs, normal surrounding tooth sizes
露齿近景·圆润切牙边缘|rounded incisor-edge study|切牙边缘较圆的轮廓|正面小幅微笑|Adult female mouth close-up, upper incisors with gently rounded corners and edges, natural ivory tone, relaxed smile
露齿近景·较方切牙边缘|squarer incisor-edge study|切牙边缘较平直的轮廓|同角度正面微笑|Adult female mouth close-up, upper incisor shapes slightly squarer with flatter lower edges, no jagged teeth, same small relaxed smile
口部近景·轻张口上下牙列|slightly open upper/lower teeth study|上下牙列之间的空间与口内暗部|正面轻张口，非大幅张嘴|Adult female mouth slightly open, natural upper and lower front tooth rows with visible dark separation, lips relaxed, no tongue protrusion or dental tools
口部近景·轻合齿轮廓|gently closed teeth study|上下牙边缘的重叠观察|双唇轻分、牙齿自然轻合|Adult female mouth close-up, lips gently parted with upper/lower teeth lightly together, natural tooth overlap, no forced bite, no diagnostic diagram
露齿近景·侧前牙列转折|three-quarter tooth-row study|牙弓转向与远侧牙齿遮挡|侧前三分微笑局部|Adult female small smile at three-quarter view, nearer teeth broader and far-side teeth receding in perspective, natural mouth corners, no whole face
''')
block('skin_face','''
皮肤近景·鼻颊毛孔|nose-cheek pore texture|毛孔密度与轻微高光|鼻翼旁与面颊局部|Adult female nose-side and cheek skin patch, subtle natural pores and restrained surface highlights, close-up painterly realistic texture, no inflamed lesions
皮肤近景·眼尾细纹|outer-eye fine-line texture|眼尾浅纹与眼睑体积|成年女性眼尾局部|Adult woman's outer eye corner and adjacent skin with gentle fine lines, neutral relaxed expression, natural skin, no makeup emphasis
皮肤近景·鼻唇沟过渡|nasolabial volume transition|面颊与口周的体积过渡|侧前面颊至嘴角局部|Adult woman's cheek to mouth corner close-up, subtle nasolabial volume transition and soft shadow, no drawn deep black crease
皮肤近景·颈部横纹|neck fold texture|颈部转折与浅横纹|颈侧至锁骨上方局部|Adult woman's neck side and above-collarbone skin close-up, natural shallow horizontal neck lines, head outside crop, opaque high collar at lower edge
皮肤近景·指关节褶纹|finger-joint crease texture|关节屈曲时的细褶|一组成人手指关节局部|Close-up of adult woman's two adjacent finger knuckles lightly bent, natural skin creases and short unpainted nail edge, no extra fingers
皮肤近景·掌面细褶|fine palm-surface texture|掌面较浅褶线与掌丘|成年右手掌局部|Close-up adult female palm surface and thumb-base pad, fine natural shallow skin lines, no palm-reading symbols, complete local forms
皮肤近景·手背薄皮与腱线|hand-back skin and tendon texture|薄皮、腱线与细小起伏|成年手背局部|Adult woman's hand back close-up, subtle extensor tendon relief beneath intact natural skin, fine texture, no strongly enlarged veins or injury
皮肤近景·前臂细毛|forearm fine-hair texture|细毛顺向与表面受光|成年女性前臂局部|Close-up of adult woman's forearm patch with delicate short natural fine hair, warm neutral skin and side light, no shaved patterns or jewelry
''')
block('skin_body','''
皮肤近景·肘部屈曲褶线|bent-elbow fold texture|肘弯压缩纹与外侧拉伸|手臂轻弯的局部|Adult female elbow bent moderately, close-up intact skin showing inner-elbow compression folds and outer smooth stretch, crop excludes torso
皮肤近景·膝部弯曲纹理|bent-knee surface texture|膝前转面与浅褶|成年膝部局部|Adult woman's bent knee close-up with natural kneecap surface and shallow skin lines, plain opaque trouser hem above crop, nonmedical reference
皮肤近景·腕部日晒分界|wrist tan-line study|腕表遮挡形成的颜色分界|成年前臂与腕部局部|Adult woman's wrist and short forearm, a soft lighter band where a watch usually sits, ordinary mild tan contrast, no watch, no inflamed skin
皮肤近景·肩部雀斑|shoulder freckle distribution|点状色差的疏密与大小|成年肩峰与上臂局部|Adult woman's shoulder cap and small upper-arm area with scattered natural freckles, opaque shirt edge visible, no chest or cleavage in crop
皮肤近景·上臂胎记|upper-arm birthmark study|平坦色斑的边界与肤色关系|成年上臂外侧局部|Adult female outer upper arm with a small flat soft-edged light-brown birthmark, natural intact skin, simple neutral patch study, no medical scale or labels
皮肤近景·小腿细毛|lower-leg fine-hair texture|细毛方向与胫骨转面|成年女性小腿局部|Adult woman's lower shin/calf close-up with fine short natural hair and soft form shading, intact skin, no entire body
皮肤近景·脚跟表面细纹|heel surface-line texture|脚跟转面与日常细纹|成年脚跟后侧局部|Adult woman's heel rear-three-quarter close-up, natural slightly dry fine surface lines without wounds or severe cracking, ordinary foot reference
皮肤近景·虎口表面细纹|thumb-web surface texture|虎口弧面与浅表细纹|成年手部局部|Adult female hand thumb web close-up, thumb gently open from index finger, subtle fine surface lines and natural skin texture, no injury or deep fissures
''')

LIGHT_BASE='同一原创成年女性：黑色齐下巴短发、深棕眼、灰色圆领上衣；正面机位、相同裁切与中性表情'
block('lighting','''
布光对照·正面柔光基准|frontal soft-light baseline|正面柔光下较浅的鼻影与眼窝|固定正面头像，仅改变光照|Same adult woman: chin-length straight black bob tucked behind ears, dark-brown eyes, medium-light warm skin, gray crewneck shirt, neutral closed lips, perfectly frontal eye-level camera. Large neutral softbox directly in front, soft shallow facial shadows
布光对照·画面左前四十五度|image-left 45-degree soft light|鼻影向画面右侧延伸与颊部转面|同一面孔、同一正面机位|EXACT SAME WOMAN/HAIR/EXPRESSION/CROP as baseline. Soft key light from IMAGE LEFT front45degrees, nose shadow falls to image right, right cheek dimmer, neutral gray background
布光对照·画面右侧硬光|image-right hard side light|明暗交界与清楚的鼻部投影|同一面孔，光源位于画面右侧|EXACT SAME WOMAN, frontal unchanged. Small hard key light from IMAGE RIGHT90degrees, image-right face lit and image-left face in clear deeper shadow, crisp nose shadow, readable eyes
布光对照·顶部硬光|overhead hard-light study|眼窝、鼻底与下颏阴影|同一面孔，光从头顶稍前方照下|EXACT SAME WOMAN, frontal unchanged. Hard light high above forehead slightly toward camera, shadows under brow, nose and chin, no beauty-light fill flattening the effect
布光对照·低位上照|low-angle upward-light study|鼻影朝上与眉骨下缘受光|同一面孔，光源位于镜头下方|EXACT SAME WOMAN, frontal unchanged. Main light from BELOW the face in front, upward-cast nose shadow, underside of nose/chin illuminated, neutral expression without horror makeup
布光对照·背光与轮廓|backlight and rim-light study|发缘亮边与正面较暗的关系|同一面孔，背光配微弱正面填充|EXACT SAME WOMAN, frontal unchanged. Main light behind head creates clear hair/shoulder rim, frontal face dim but still readable with weak neutral fill, no giant glowing halo
布光对照·窗边大面积柔光|large-window soft-light study|宽大柔光下的渐层与软鼻影|同一面孔，画面左侧大窗光|EXACT SAME WOMAN, frontal unchanged. Very large diffuse window light from IMAGE LEFT, broad soft tonal transitions with weaker shadows than cell2, no visible window or scenery
布光对照·暖主光冷环境|warm-key cool-fill study|暖亮部与冷暗部的色温关系|同一面孔、同机位的双光色温示意|EXACT SAME WOMAN, frontal unchanged. Warm amber key from IMAGE LEFT front and gentle cool blue environmental fill on image-right shadow side, balanced subtle skin color, no colored makeup or expression change
''')
for e in CATALOG:
    if e.get('study_group')=='lighting':
        e.update(comparison_set='portrait-light-v43',comparison_order=e['study_order'],comparison_baseline='IL001',fixed_conditions=LIGHT_BASE,changed_condition=e['study_focus'])
        e['aliases']={1:['顺光','正面光','柔光'],2:['左前光','四十五度光'],3:['侧光','硬光','右侧光'],4:['顶光','上方光'],5:['底光','下方光','上照光'],6:['逆光','轮廓光','背光'],7:['窗光','窗边光','大面积柔光'],8:['冷暖光','混合光','色温对照']}[e['study_order']]

COTTON_BASE='同一成年女性：黑色低马尾、白色宽松长袖棉衬衫（塞入裤腰）、蓝灰直筒长裤、白色平底鞋；服装款式、材质、人物比例与中性柔光固定'
DRESS_BASE='同一成年女性：棕色盘发、灰蓝不透明长袖中长连衣裙、细腰带、白色平底鞋；裙长到小腿中下段，衣物款式、人物比例与中性柔光固定'
block('cotton','''
衬衫长裤·自然站立基准|shirt-trousers standing baseline|肩部悬垂、腰口收束与自然裤褶|固定服装的正侧前三分全身|Same adult woman in white loose opaque long-sleeve cotton button shirt TUCKED into blue-gray straight trousers, white flat shoes, black low ponytail. Standing relaxed, arms down; shirt shoulder drape and small waist-tuck folds, all feet visible
衬衫长裤·双臂上举|shirt-trousers raised-arm folds|腋下牵拉与肩袖褶线|同款衣物，保持衬衫塞入裤腰|EXACT SAME WOMAN AND OUTFIT. Both arms lifted above head, elbows slightly bent; natural underarm tension folds and sleeve bunching, shirt remains tucked and torso covered, full body and hands visible
衬衫长裤·屈肘抱臂|shirt-trousers elbow-compression folds|肘内压缩与肘外拉伸|同款衣物，胸前自然抱臂|EXACT SAME WOMAN AND OUTFIT. Arms naturally folded across chest, elbows bent, short compressed folds inside elbows and smoother stretched outer sleeves, full body same scale
衬衫长裤·上身转动|shirt-trousers torso-twist folds|腰侧斜向牵拉与衣摆收束|同款衣物，髋部基本朝前|EXACT SAME WOMAN AND OUTFIT. Hips mostly front while shoulders turn toward image left, moderate torso twist, diagonal tension folds at waist and shirt side, hands relaxed, full shoes visible
衬衫长裤·坐姿压缩|shirt-trousers seated folds|髋前、膝窝与腰口的压缩褶|坐在简单无靠背凳上|EXACT SAME WOMAN AND OUTFIT. Seated upright on simple backless stool, both feet flat and knees near90degrees; compression folds around front hip, waist tuck, bent knees and behind knees, full body
衬衫长裤·屈蹲受力|shirt-trousers crouching folds|膝前张力与膝窝堆褶|同款衣物，双脚支撑的自然下蹲|EXACT SAME WOMAN AND OUTFIT. Balanced comfortable deep squat with feet on ground and hands resting lightly on knees; clear stretched fabric over knees and compressed folds behind knees/hip, no anatomy distortion
衬衫长裤·侧风鼓起|shirt-trousers side-wind folds|迎风受压与背风侧鼓起|同款衣物，人物站立不改变姿势|EXACT SAME WOMAN AND OUTFIT standing neutral. Wind blows from IMAGE LEFT to RIGHT, loose shirt sleeves and untight side fabric move toward image right while shirt remains tucked, ponytail bends right, trousers restrained; no flying props
衬衫长裤·迈步过渡|shirt-trousers walking folds|跨步时裤腿拉伸与松弛差异|侧前三分全身，一脚前一脚后|EXACT SAME WOMAN AND OUTFIT. Calm walking mid-step, one foot forward and one back, mild opposite arm swing; readable diagonal hip-to-thigh tension and loose folds on trailing trouser leg, full hands and shoes
''')
block('dress','''
长袖连衣裙·站立悬垂基准|long-sleeve dress standing baseline|腰带支撑与裙摆竖向悬垂|固定款式、站姿与柔光|Same adult woman, brown hair in low bun, opaque muted blue-gray LONG-SLEEVE belted midi dress to lower calves, white flats. Standing relaxed, arms down, natural vertical skirt folds below thin waist belt, complete hands/hem/shoes
长袖连衣裙·抬手牵拉|dress raised-arm tension|肩袖张力与腰侧牵拉|同款裙装，一臂自然上举|EXACT SAME WOMAN AND DRESS. One arm raised above shoulder, other relaxed; underarm tension folds and diagonal waist-side pull, waist belt and midi hem remain, all hands and feet visible
长袖连衣裙·坐姿铺展|dress seated drape|裙料在大腿与凳沿的铺展|简单凳面，双脚自然落地|EXACT SAME WOMAN AND DRESS. Seated upright on plain backless stool, knees together naturally and feet flat; midi skirt stays covering knees, drapes over thighs and falls past stool edge, hands on lap
长袖连衣裙·屈膝跪坐|dress kneeling drape|膝部顶点与周围堆褶|侧前三分跪坐，裙料完整覆盖|EXACT SAME WOMAN AND DRESS. Kneeling upright with lower legs folded beneath, full opaque midi skirt covers knees and lower legs while fabric gathers around knee contact points; both hands relaxed on thighs, full silhouette
长袖连衣裙·迈步展开|dress walking expansion|跨步带动裙片前后展开|同款裙装，一脚迈出|EXACT SAME WOMAN AND DRESS. Gentle walking stride, midi skirt front panels open in fold volume without high slit, calves and shoes visible naturally below hem, opposite arm swing, no extra garment layers
长袖连衣裙·轻提衣边|dress lightly lifted edge|手指夹点到裙料的放射褶|只轻提侧边少量裙料，裙长仍过膝|EXACT SAME WOMAN AND DRESS standing. One hand gently pinches a small section of side hem and raises it only a few centimeters; radial folds from fingertips, skirt remains well below knees, other arm relaxed, complete feet
长袖连衣裙·侧风摆动|dress side-wind drape|腰部固定与下摆向背风侧偏移|站姿固定，风从画面左侧吹来|EXACT SAME WOMAN AND DRESS standing same as baseline. Wind from IMAGE LEFT to RIGHT pushes skirt lower half and loose sleeve fabric to image right, thin waist belt anchors middle, hem remains below knees, no exposure
长袖连衣裙·转身滞后|dress turning inertia|躯干转向与裙摆滞后的方向差|同款裙装，适度转身而非高速旋转|EXACT SAME WOMAN AND DRESS. Gentle turning step toward image left, shoulders turn first and belted midi skirt trails slightly toward image right, modest skirt movement, all hands/shoes visible, no fast spin or floating pose
''')
for e in CATALOG:
    if e.get('study_group') in ['cotton','dress']:
        group=e['study_group'];e.update(comparison_set='garment-'+group+'-v43',comparison_order=e['study_order'],comparison_baseline='GD001' if group=='cotton' else 'GD009',fixed_conditions=COTTON_BASE if group=='cotton' else DRESS_BASE,changed_condition=e['study_focus'])
        if e['study_order']==7:e['aliases']=['风吹','风力','侧风']
    if e.get('study_group') in ['nose','ear','teeth']:e['aliases']={'nose':['鼻子','鼻部'],'ear':['耳朵','耳廓','耳垂'],'teeth':['牙齿','牙列','露齿']}[e['study_group']]
assert sum(bool(e.get('study_reference')) for e in CATALOG)==80
