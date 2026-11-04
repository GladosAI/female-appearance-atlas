"""V37: cross-legged seating, half-kneels, crouches and rise transitions."""
from catalog_content import CATALOG,add

DIMENSION='坐姿、蹲跪与起身'
SHEET_TOPICS=['交腿与多样坐姿','单膝跪与起身过渡']

def block(topic,text):
    rows=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(rows)==16
    for name,en,view,support,phase,recipe in rows:
        add('pose',DIMENSION,f'{name}|{en}|25岁以上成年女性，完整不透明运动上衣、长裤与平底鞋袜。{view}；{recipe}。主要支撑：{support}；动作阶段：{phase}。')
        CATALOG[-1].update(added_in='37.0',seated_pose_reference=True,pose_reference=True,pose_expansion_reference=True,
            pose_group='sit_crouch_rise',pose_group_name=DIMENSION,pose_sheet_topic=topic,
            pose_view=view,pose_support=support,pose_phase=phase,pose_focus=recipe,pose_actors=1,pose_sheet_layout='portrait',
            adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年角色动作创作参考',
            aliases=['坐蹲跪起身扩充'],reference_ids=['R04','R09'],
            note='先找清楚椅面、地面、脚底、膝部和手掌的接触点，再比较左右腿的前后遮挡。二郎腿的膝上交叠与四字腿的脚踝搭膝分开记录；单膝跪保留一膝触地、另一脚落地的区别。起身是运动中的单帧，视角、重心与支撑关系按角色设计需要调整。')

block(SHEET_TOPICS[0],'''
翘二郎腿正面坐姿|front-view knee-over-knee seated pose|正面|坐骨、座面与左脚脚底|静止|坐在简洁椅上，右大腿跨过左大腿，右膝叠在左膝上方；左脚平放地面，右小腿自然垂下，双手放在上侧膝部
翘二郎腿侧面坐姿|side-view knee-over-knee seated pose|左侧面|坐骨、座面与右脚脚底|静止|坐在简洁椅上，左大腿跨过右大腿，左膝叠在右膝上方；右脚踩地，上侧脚悬空，躯干自然直立
翘二郎腿后靠坐姿|backrest-supported crossed-knee sit|斜前面|座面、椅背与下侧脚|静止|右膝跨叠左膝，背部放松靠住椅背；左脚着地，右脚自然悬垂，一前臂搭扶手，另一手放腿上
四字腿脚踝搭膝坐|figure-four ankle-over-knee seated pose|斜前面|座面与左脚脚底|静止|右脚踝搭在左膝上方，右膝向外侧打开，腿形呈四字；左脚平放地面，双手在腿上，不画成双膝交叠
脚踝交叉并膝坐|ankle-crossed knees-together sit|正面|座面与双前脚掌|静止|双膝并拢向前，小腿在脚踝处交叉；两只鞋尖轻触地面，膝部不交叠，双手叠放腿上
椅上单腿抱膝坐|one-knee-hug chair sit|斜侧面|座面、椅上一脚与地面一脚|静止|一脚收上椅面，双臂轻抱该侧抬起的膝部；另一脚踩在地面，臀部稳定留在座面
椅上盘腿坐姿|cross-legged chair-seat sit|斜前面|坐骨与椅面|静止|两腿都收在宽椅面上，小腿在身前交叉；双膝自然放低，双手轻搭两膝，鞋与脚完整入画
高凳双脚悬垂坐|high-stool feet-dangling sit|侧面|坐骨与高凳座面|静止|坐在高于普通椅面的高凳上，两条小腿向下垂落；双脚离地且没有踩横档，双手扶凳缘
椅边单脚前伸坐|chair-edge one-leg-extended sit|斜前面|座面、左脚与右脚跟|静止|左膝自然弯曲且左脚踩地，右腿斜向前伸、右脚跟触地；坐骨在椅前缘，双手轻搭座面两侧
长凳两侧跨坐|straddling a narrow bench|斜前面|座面与双脚脚底|静止|骑跨窄长凳，两条腿分别落在凳子左右两侧，双脚稳稳着地；躯干直立，双手在身前轻扶凳面
地面盘坐正面姿态|front-view cross-legged floor sit|正面|坐骨与小腿外侧|静止|在薄垫上盘坐，两小腿在身前交叉，双膝向两侧自然放低；双手放在膝上，背部自然伸展
地面抱双膝坐姿|floor sit hugging both knees|斜侧面|坐骨与双脚脚底|静止|坐在地面，两膝抬起靠近胸前，两脚仍踩地；双臂松抱小腿前侧，头部自然朝前
台阶并腿坐姿|knees-together seated step pose|斜前面|高一级台阶座面与低一级脚底|静止|坐在上一级宽台阶边缘，双膝并拢，双脚放在低一级台阶；一手撑在身侧阶面，另一手放腿上
沙发扶手侧倚坐|sofa-armrest supported side-lean sit|斜前面|座垫、单侧前臂与双脚|静止|臀部坐稳简洁沙发座垫，一侧前臂轻靠扶手，上身小幅侧倚；双腿斜向同侧，双脚着地
地面坐姿回身支撑|seated floor turn with rear-hand support|斜后侧面|坐骨、单手掌与一脚|转身中段|双腿一前一后屈起，前侧脚踩地；上身回转，一手撑在身后地面，另一手搭前侧膝，手脚不重叠成一团
地面合足屈膝坐|soles-together bent-knee floor sit|正面|坐骨与双脚外侧|静止|坐在薄垫上，两脚脚底相对靠近身前，双膝向两侧适度打开；双手轻扶脚踝，保持长裤完整覆盖
''')
block(SHEET_TOPICS[1],'''
单膝跪正面直身|front-view upright half-kneel|正面|左膝、左小腿与右脚脚底|静止|左膝触地，右脚在身前踩地且右膝弯曲；躯干保持直立，双手自然放在身侧，左右腿支撑清楚
单膝跪侧面直身|side-view upright half-kneel|左侧面|右膝、右小腿与左脚脚底|静止|右膝触地，左脚向前踩地、左小腿接近竖直；躯干与头部自然直立，手臂放松垂落
单膝跪双手扶前腿|half-kneel hands-on-front-thigh pose|斜前面|后侧膝、前脚与双手扶大腿|静止|一膝触地，另一脚向前踩地；双手轻搭前侧大腿、上身小幅前倾，后膝仍清楚贴地
单膝跪回身观察|half-kneeling torso-turn pose|斜后侧面|后侧膝与前脚脚底|转身中段|保持一膝触地、一脚向前踩地，下肢不挪动；上身与头转向侧后方，一手轻扶前腿，另一臂自然下垂
单膝跪抬手招呼|half-kneeling raised-hand greeting|斜前面|后侧膝与前脚脚底|抬臂终点|保持一膝跪地，另一脚在前稳定踩地；一臂屈肘举到肩旁、掌心朝前，另一手放前腿上
单膝跪系鞋带|half-kneel tying a shoe|侧面|后侧膝与前脚脚底|系鞋中段|一膝触地，另一脚在前；躯干弯向前鞋，双手在该鞋鞋带处操作，背部与头部随前倾但不遮住支撑腿
双膝跪坐脚跟正面|front-view heel-sitting kneel|正面|双膝、小腿与脚背|静止|两膝触地、小腿向后折叠，臀部落在两脚跟上；双手放在大腿上，区别于臀部悬起的高跪
双膝跪坐脚跟侧面|side-view heel-sitting kneel|侧面|双膝、小腿与脚背|静止|双膝跪地，小腿和脚背沿地面向后，臀部清楚坐在脚跟上；躯干自然直立，双手放在大腿前侧
单手撑地平衡低蹲|one-hand floor-supported low crouch|斜前面|双脚脚底与一手掌|低蹲终点|双膝弯曲、髋部降低，一手掌撑在两脚前方地面辅助平衡；另一手轻搭大腿，两只脚保持清楚
侧伸腿不对称低蹲|side-leg-extended low crouch|正面|屈膝侧脚底、伸腿侧脚跟与一手|低蹲终点|重心降低到一侧屈膝腿上，另一腿斜向侧方伸出、脚跟触地；一手轻撑身前地面，躯干不夸张扭转
椅旁扶座低蹲|chair-seat-supported crouch|侧面|双脚与一手扶椅面|低蹲终点|在椅子侧前方蹲低，一手掌扶在椅面边缘，另一手放在大腿；双膝弯曲，臀部不接触椅面
单膝跪前移准备起身|half-kneel forward-transfer preparation|侧面|后侧膝与前脚脚底|起身准备|一膝仍触地，前脚稳稳踩地；上身向前侧大腿上方前移，双手扶前侧大腿，髋部尚未明显升高
单膝跪起身抬膝|rising-from-half-kneel knee-lift frame|侧面|前脚脚底与后前脚掌|起身中段|髋部开始上升，后侧膝已离地少许，后脚以前脚掌撑地；前腿仍屈膝，躯干自然前倾
侧坐扶地转单膝|side-sit to supported half-kneel|斜侧面|一手掌、后侧膝与前脚|起身准备|从地面侧坐转向单膝姿，一掌在身侧撑地，前脚落地、另一膝触地；臀部刚抬离地面，手脚位置分开
椅上起身将站直|chair-rise near-upright frame|侧面|双脚脚底|起身后段|臀部已明显高于椅面，双膝仍有小幅弯曲，躯干接近直立；双臂自然垂落，椅子留在身后作阶段参照
双臂前伸离椅起身|chair-rise with arms-reaching-forward|侧面|双脚脚底|离座中段|双脚收近椅前，躯干前倾且臀部刚离开椅面；双臂向前平伸作平衡，不扶椅子，双膝仍弯曲
''')

for entry in CATALOG:
    if not entry.get('seated_pose_reference'):continue
    if 'knee-over-knee' in entry['en'] or 'crossed-knee' in entry['en']:entry['aliases']+=['翘二郎腿','二郎腿','翘腿','膝上交腿']
    if 'figure-four' in entry['en']:entry['aliases']+=['四字腿','4字腿','脚踝搭膝']
    if 'half-kneel' in entry['en']:entry['aliases']+=['单膝跪','半跪','一膝跪地']
    if 'heel-sitting' in entry['en']:entry['aliases']+=['跪坐','正坐','臀部坐脚跟']
