"""V28: clothed adult pose studies, annotated with view, support and phase."""
from catalog_content import CATALOG,add
POSE_GROUPS=[]
def group(key,label,text,actors=1,layout='portrait'):
    rows=[line.strip().split('|') for line in text.strip().splitlines()];assert len(rows)==16,(key,len(rows));POSE_GROUPS.append({'id':key,'name':label,'count':16,'actors':actors,'layout':layout})
    for name,en,view,support,phase,recipe in rows:
        add('pose',label,f'{name}|{en}|25岁以上成年女性，完整不透明运动上衣、长裤与平底鞋袜。{view}；{recipe}。主要支撑：{support}；动作阶段：{phase}。')
        CATALOG[-1].update(added_in='28.0',pose_reference=True,pose_expansion_reference=True,pose_group=key,pose_group_name=label,pose_view=view,pose_support=support,pose_phase=phase,pose_focus=recipe,pose_actors=actors,pose_sheet_layout=layout,adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年角色动作创作参考',reference_ids=['R04','R09'],
          note='先观察躯干动作线、重心方向与支撑点，再核对肩髋转动、关节弯曲和四肢遮挡。图例为明确成年角色的完整衣着动作设计；运动中的图是单帧设定，不能把腾空帧当作静态站姿。双人动作分别辨认两个人的手足和接触点。')

group('standing_balance','站姿、倚靠与重心变化','''
并脚窄站|narrow parallel-foot stance|正面|双脚脚底|静止|双脚平行靠近，膝自然伸直，双臂在体侧放松
宽距平行站姿|wide parallel-foot stance|正面|双脚脚底|静止|两脚比肩稍宽，髋部位于两脚之间，双臂自然下垂
丁字步站姿|T-position relaxed stance|斜前面|前后两脚|静止|一脚横向放在另一脚后侧，形成小幅丁字脚位，双膝放松
交叉脚踝站姿|crossed-ankle standing pose|正面|后侧主承重脚|静止|两腿在脚踝附近轻交叉，前脚尖点地，双臂自然垂落
前脚点地后腿承重|front toe-touch weight shift|侧面|后侧整脚|重心后移|后腿承重，另一脚向前轻点脚尖，躯干保持自然直立
双脚提踵站姿|two-foot heel-rise stance|侧面|双前脚掌|提踵最高点|两脚跟同时抬起，身体向上延伸，手臂稍张开保持平衡
双手插袋松站|hands-in-pockets relaxed stance|斜前面|双脚脚底|静止|双手放入运动长裤两侧口袋，肩部放松，一膝轻屈
背靠墙单脚贴墙|wall lean with raised foot|侧面|背部与一脚脚底|静止|背部轻靠短墙面，一脚站地，另一膝弯曲且鞋底轻贴墙
肩靠墙侧支撑|shoulder-supported wall lean|斜前面|外侧肩与双脚|静止|一侧肩部轻靠墙，双脚离墙少许，手臂自然垂落
单手扶墙转髋|one-hand wall-supported turn|斜侧面|一手掌与双脚|缓慢转向|一只手掌平扶墙，肩部相对稳定，髋部小幅转向外侧
双前臂搭栏休息|both-forearms railing rest|背面|双前臂与双脚|静止|完整背面，双前臂搭在腰高栏杆上，上身略向前倾
单肘撑矮台站姿|one-elbow low-counter lean|斜前面|单前臂与双脚|静止|一侧前臂和肘部搭在矮台上，身体轻侧倾，另一手自然垂下
双手撑腰轻后伸|hands-on-lower-back gentle extension|侧面|双脚脚底|伸展中段|双手掌放在后腰两侧，胸廓轻抬，上身小幅后伸，避免过度弓腰
抬臂转头远望|raised-arm distant look|斜侧面|双脚脚底|观察|一前臂轻抬至额前，头转向远处，双脚保持稳定，另一臂下垂
重心前移探身|forward weight-shift lean|侧面|前后两脚|前移中段|前膝轻屈，上身从踝髋关系向前探，后脚跟稍轻，双臂微张
背手抬头站姿|hands-behind-back upward look|斜侧面|双脚脚底|静止|双手在背后轻搭，肩部舒展，头略抬，颈部自然延伸
''')
group('arms_gestures','手臂、手势与上肢动作','''
单臂水平平举|single-arm horizontal raise|正面|双脚脚底|抬臂终点|一臂向身体侧方水平伸展，另一臂下垂，肩不耸起
双臂水平张开|both-arms horizontal spread|正面|双脚脚底|展开终点|双臂向两侧平举到肩高，手掌自然张开，躯干直立
双臂上举伸展|both-arms overhead stretch|正面|双脚脚底|伸展终点|两臂向上斜举，肘轻微弯曲，手掌分开，完整手指不出画面
单臂屈肘过头|one-elbow overhead bend|斜前面|双脚脚底|抬臂终点|一臂举过头后屈肘，另一手轻扶上举侧肘部，肩线自然
双手交握举头顶|clasped-hands overhead reach|正面|双脚脚底|伸展终点|双手在头顶上方交握，两肘略弯，躯干保持自然伸展
单手搭后脑|single-hand behind-head pose|侧面|双脚脚底|静止|一手掌轻放后脑，肘向外张，另一臂垂落，头颈不扭折
双手抱后脑|both-hands behind-head pose|斜前面|双脚脚底|静止|双掌轻搭后脑，两肘向外展开，肩部放松而不是挺腰
双手捂耳站姿|both-hands covering-ears stance|正面|双脚脚底|接触终点|双手掌覆盖两侧耳朵，肘向侧前方展开，头略低
单手遮光看远处|hand shading-eyes pose|斜前面|双脚脚底|观察|一手掌平放额前遮光，目光向远处，另一手放在体侧
双手拢嘴呼喊|cupped-hands calling pose|正面|双脚脚底|呼喊中段|两手在嘴前拢成开放喇叭形，两肘向外，上身轻向前
双掌上翻耸肩|open-palms shrugging gesture|正面|双脚脚底|手势终点|双肘弯曲贴近腰侧，掌心向上，肩部轻耸，五指自然展开
单掌介绍手势|single-palm presenting gesture|斜前面|双脚脚底|介绍中段|一臂向侧前方伸出且掌心向上，另一手在身前自然弯曲
双手向前推掌|both-palms forward press|侧面|前后两脚|推掌终点|双掌在胸前高度向前伸出，两肘未锁死，前膝轻屈
双臂前伸取物准备|both-arms reaching-forward preparation|斜侧面|双脚脚底|伸手中段|两臂向前伸至肩高，双掌相对留出间距，上身微前倾，无道具
单手挽起袖口|one-hand sleeve-adjusting gesture|斜前面|双脚脚底|整理中段|一手捏住另一侧前臂袖口并轻上拉，手与衣物接触明确
单臂跨胸舒展|cross-body arm stretch|正面|双脚脚底|舒展终点|一臂水平横跨胸前，另一前臂托住其肘外侧，躯干不过度扭转
''',layout='landscape')
group('sit_crouch_rise','坐姿、蹲跪与起身','''
椅边前倾坐姿|chair-edge forward-lean sit|侧面|坐骨与双脚|静止|坐在简洁椅面前缘，上身前倾，两前臂轻搭大腿
椅背放松后靠|backrest-supported relaxed sit|侧面|座面、椅背与双脚|静止|背部靠椅背，骨盆留在座面上，两脚平放地面，双手在腿上
反坐椅抱靠背|reverse-chair backrest sit|斜前面|座面与双脚|静止|面对椅背反向坐在椅上，两前臂搭在低靠背顶端，双腿位于椅两侧
椅上并膝侧移坐|knees-together sideways chair sit|斜前面|坐骨与双脚|静止|坐稳椅面，双膝并拢向一侧倾斜，两脚仍触地，躯干轻回正
长凳横坐手撑凳|sideways bench sit with hand support|斜侧面|坐骨、一手与双脚|静止|横坐短长凳，一手撑在身侧凳面，双腿在同侧自然垂下
地面双腿侧屈坐|floor side-folded-leg sit|斜前面|坐骨与一侧手掌|静止|双腿弯曲收向身体同侧，一手撑地，肩髋自然错开
地面分腿长坐|floor long-sit with separated legs|正面|坐骨与双手|静止|双腿向前伸直并小幅分开约肩宽，两手在身侧撑地，完整长裤覆盖
地面单腿屈膝坐|one-knee-bent floor sit|斜前面|坐骨与一手掌|静止|一腿向前伸出，另一膝弯曲向上，单手撑在身体后侧
双手撑地后坐|rear-hand-supported floor sit|侧面|双掌、坐骨与双脚|静止|双膝弯曲，双掌放在身后撑地，躯干轻向后倾而非悬空
深蹲环膝姿态|deep squat with arms-around-knees|斜侧面|双脚脚底|深蹲终点|双脚自然分开，髋部下降，双臂松环膝前，脚跟尽量着地
脚跟抬起低蹲|heel-raised low crouch|侧面|双前脚掌|低蹲终点|膝髋充分屈曲，脚跟抬起，双臂向前轻伸以平衡
单膝跪地伸手取物|one-knee-kneel reach toward object|侧面|一膝与另一脚|伸手中段|一膝触地，另一脚踩地，躯干轻前倾，一手伸向近处小盒
双膝高跪姿态|upright high-kneeling pose|侧面|双膝与小腿前侧|静止|双膝触地，上半身与大腿基本竖直，臀部离开脚跟，双手放在体侧
半蹲准备落座|half-squat preparing-to-sit|侧面|双脚脚底|落座前一刻|椅子在身后，髋向后移、双膝弯曲，臀部尚未触及座面
扶膝从低蹲起身|hands-on-knees rising-from-crouch|斜侧面|双脚与双手扶膝|起身中段|两手扶在膝上方大腿处，髋部从低位上升，双膝仍弯曲
椅上前移起身|forward-transfer chair-rise pose|侧面|双脚与一手扶椅|起身中段|双脚收近椅前，上身前移，臀部刚离座，一手轻扶座边
''')
group('lying_ground','卧姿、休息与地面动作','''
仰卧双臂放身侧|supine rest arms-at-sides|侧上方全身|背部与双腿|静止|在薄垫上完整平躺，双腿伸直，双臂放在体侧，头颈自然
仰卧双膝弯曲|supine rest with both-knees-bent|侧面全身|背部与双脚|静止|背部贴薄垫，双膝向上弯曲，双脚踩垫，手臂放体侧
仰卧单膝弯曲|supine rest with one-knee-bent|侧上方全身|背部与一脚|静止|一腿伸直，另一膝弯曲脚掌着垫，双手在体侧，四肢完整
仰卧双臂上伸|supine overhead-arm rest|侧上方全身|背部与双腿|伸展终点|完整平躺在薄垫上，两臂沿头顶方向平放，双腿自然伸直
侧卧自然并腿|side-lying straight-leg rest|侧面全身|身体一侧|静止|肩、髋和双腿侧卧在薄垫上，双腿自然并拢，双臂放身前
侧卧枕前臂|side-lying forearm-as-pillow|侧面全身|身体一侧与前臂|静止|一侧前臂折于头下做小支撑，另一手放身前，双腿伸直略错开
侧卧屈膝抱枕|side-lying bent-knee pillow-hold|侧上方全身|身体一侧|静止|侧卧且双膝轻屈，双臂抱一个小枕，完整衣着，非夸张蜷缩
俯卧双臂叠枕|prone rest on folded-forearms|侧上方全身|躯干前侧与双腿|静止|在薄垫上俯卧，双前臂叠在头前，脸侧转搭于前臂，双腿伸直
俯卧前臂撑起|prone forearm-supported torso|侧面全身|双前臂与躯干下部|抬头中段|两肘在肩下撑垫，上半身轻抬，髋和腿仍在垫上，无夸张弓腰
俯卧屈单膝|prone one-knee-flexed pose|侧上方全身|躯干前侧与一条腿|静止|俯卧且一膝自然屈曲、小腿略抬，另一腿伸直，前臂叠放在头前
侧卧单肘半撑|side-lying low-elbow support|侧面全身|单前臂、同侧髋与双腿|抬身中段|侧卧时一肘和前臂撑起肩胸，髋部仍接触垫子，双腿并拢
双手双膝四点支撑|hands-and-knees four-point support|侧面全身|双掌与双膝|静止|双掌置于肩下、双膝置于髋下，背部自然平直，头颈延续躯干
仰卧双肘撑起准备|supine-to-elbow-supported rise|侧面全身|双前臂、骨盆与双腿|坐起准备|从仰卧抬起头肩，用双前臂撑垫，双腿伸直，尚未完全坐起
侧卧撑地坐起|side-lying to seated push-up|侧面全身|一掌、一前臂与侧髋|起身中段|由侧卧把一掌放在胸前撑垫，上身抬起，双腿保持屈曲以准备侧坐
仰卧翻向侧卧|supine-to-side rolling pose|侧上方全身|背侧与侧髋|翻身中段|一侧肩已离垫，躯干和骨盆向同侧转，双膝微弯，手臂随转动移动
侧坐缓慢躺下|side-sit lowering-to-rest|侧面全身|一前臂、侧髋与双腿|躺下中段|由地面侧坐缓慢下降到前臂支撑，头肩尚未落垫，双腿自然收向一侧
''',layout='landscape')
group('locomotion_phases','行走、跑动与跳跃阶段','''
慢走正面承重帧|front-view slow-walk support frame|正面|前侧承重脚|行走承重中期|前脚接地承重，另一脚离地向前摆，双臂自然交替摆动
慢走背面摆腿帧|back-view walking swing frame|背面|单侧脚底|行走摆腿中期|完整背面，单腿支撑，另一腿向前摆，肩髋有小幅反向转动
踏上一级台阶|ascending single-step frame|侧面|高处前脚与低处后脚|上阶中段|前脚踩在一级矮台上，身体向高处移，后脚跟抬起，台阶完整可见
走下一级台阶|descending single-step frame|侧面|高处后脚|下阶中段|后脚仍在高处矮台，前脚伸向低处尚未落地，膝部自然弯曲
侧向并步移动|side-step closing-foot frame|正面|外侧脚底|侧移中段|一脚向侧方迈出承重，另一脚靠近但尚未并拢，两臂小幅平衡
交叉换步移动|cross-step weight-transfer frame|正面|后侧脚底|换步中段|一腿从另一腿前方交叉迈出，肩髋保持自然转动，不把腿拧结
踮脚轻走|tiptoe quiet-walk frame|侧面|一侧前脚掌|行走中段|前脚掌接地且脚跟抬起，另一脚轻摆向前，双臂在体侧平衡
行走脚跟初触地|heel-contact walking frame|侧面|前脚跟与后前脚掌|初始接地|前腿伸向前方且脚跟刚落地，后脚准备蹬离，双臂反向摆动
慢跑双脚腾空帧|jogging airborne frame|侧面|腾空，无地面接触|腾空中期|前膝抬起、后腿屈曲，双脚离地，双臂屈肘交替摆
慢跑单脚落地帧|jogging single-foot landing frame|侧面|前侧单脚|触地缓冲|前脚接地且膝轻屈，后腿收起，躯干自然前倾
冲刺后腿蹬地帧|sprint rear-leg push-off frame|侧面|后侧前脚掌|蹬地末段|后腿向后伸出蹬地，前膝前提，双臂用力交替摆动
冲刺腾空跨步帧|sprint airborne stride frame|侧面|腾空，无地面接触|腾空中期|两腿前后分开跨步，前膝屈曲、后腿伸展，躯干前倾，双脚悬空
双脚起跳伸展帧|two-foot jump extension frame|侧面|双前脚掌将离地|起跳末段|膝髋从屈曲伸展，两臂向上摆，双脚尖仍轻触地面
跳跃最高点收膝|jump-apex bent-knee frame|斜侧面|腾空，无地面接触|最高点|双脚明显离地，双膝适度收起，双臂展开保持平衡
双脚落地缓冲帧|two-foot jump-landing cushion|侧面|双脚脚底|落地缓冲|双脚同时落地，膝髋弯曲吸收下落，上身轻前倾，两臂伸前平衡
侧跳单脚着地帧|lateral-hop single-foot landing|正面|外侧单脚|侧跳落地|身体向一侧移动后由外侧脚着地，支撑膝轻屈，另一脚抬离地面
''')
group('daily_objects','日常持物与操作','''
双手捧杯站姿|two-hand cup-holding stance|斜前面|双脚；双手承杯|静止|双手在腹前捧一只普通杯，手指自然包覆杯壁，肘靠近躯干
单手举杯饮水|single-hand drinking-from-cup|侧面|双脚；单手握杯|饮水中段|一手将杯口送到嘴边，头轻抬，另一手放松，无倾倒液体
双手平端托盘|two-hand level-tray carry|斜前面|双脚；双掌承托盘|静止|双手从托盘两侧下方平托，托盘上只有一个小杯，前臂接近水平
单臂夹书站姿|book-tucked-under-one-arm stance|斜前面|双脚；一前臂夹书|静止|一本合拢素面书夹在一侧前臂与躯干间，另一臂放松
单手调整肩背包|one-hand shoulder-bag adjustment|斜侧面|双脚；肩带与单手|整理中段|一手抓住肩上背包带向上提整，背包自然贴背，另一手下垂
屈膝俯身提箱|bent-knee suitcase lift|侧面|双脚；单手握箱柄|提起初段|双膝轻屈、髋向后移，一手握身侧小硬箱把手，箱底刚离地
侧身拉行李箱走|side-view rolling-suitcase walk|侧面|承重脚与箱轮|行走中段|一手在身后握伸缩拉杆，小行李箱轮接地，另一臂向前摆
双手抱纸箱站姿|two-arm box-holding stance|斜前面|双脚；双前臂承箱|静止|双臂从小纸箱底部承托，纸箱贴近腹前，不遮住头和腿
双臂端洗衣篮|two-arm laundry-basket hold|斜前面|双脚；双手握篮缘|静止|双手从两侧握住浅洗衣篮，篮中少量折叠布料，重量靠近身体
双手握扫把扫地|two-hand broom-sweeping pose|侧面|双脚；双手握扫柄|扫动中段|两手分开握扫柄，扫头接地并朝身体前侧，躯干小幅转动
侧身擦拭桌面|side-view tabletop wiping|侧面|双脚；一掌扶桌|擦拭中段|一手在桌面上推擦布，另一手轻扶桌边，上身前倾，桌子不遮住脚
坐姿键盘打字|seated keyboard-typing pose|侧面|座面与双脚|操作中段|坐在简椅前对低桌键盘，双前臂平稳、手指靠近键面，屏幕只画小轮廓
坐姿伏案书写|seated desk-writing pose|斜侧面|座面与双脚|书写中段|一手握笔触纸，另一手按住素面纸页，前臂搭桌边，头轻低
侧身推开门扇|side-view opening-door pose|侧面|双脚；单手触门把|开门中段|一手握普通门把推动窄门扇，躯干随手臂轻转，完整门框只保留必要线条
抬臂取高处书本|overhead shelf-book reach|侧面|双脚脚底；一手握书|取物中段|一臂伸向略高于头的低书架层，手握一本书书脊，另一手在下方准备承接
弯腰拾起小物|bent-knee small-object pickup|斜侧面|双脚脚底|拾物中段|一手扶大腿，另一手伸向脚边小盒，膝髋自然弯曲，小盒尚接地
''')
group('emotion_body','情绪肢体与交流姿态','''
开心胸前拍手|happy chest-level clapping pose|正面|双脚脚底|拍手接触帧|双掌在胸前轻拍合拢，双肘自然弯曲，肩部放松，脸带自然微笑
兴奋小跳举臂|excited small-hop raised-arms|正面|腾空，无地面接触|小跳最高点|双脚离地少许，双肘屈曲向上举，身体自然伸展，表情高兴
失落垂肩站姿|disappointed slumped-shoulder stance|侧面|双脚脚底|静止|肩部下垂、头略低，双臂松垂，背部只轻微弯曲
局促身前绞手|uneasy hands-held-in-front pose|正面|双脚脚底|静止|双手在腹前轻握绞动，两肘靠近身体，双脚靠拢，头稍低
紧张攥住衣角|nervous gripping-shirt-hem pose|斜前面|双脚脚底|抓握终点|双手分别轻攥上衣两侧下摆，肩部略收，视线偏向一旁
害羞缩肩背手|shy drawn-shoulders hands-behind-back|斜前面|双脚脚底|静止|双手在身后轻握，肩部略内收，头侧低，一脚尖轻点地
生气叉腰前倾|angry hands-on-hips forward-lean|斜前面|双脚脚底|表达终点|双手叉腰、两肘外张，上身小幅前倾，眉线收紧但不夸张扭曲
拒绝挥掌侧转|refusing palm-out half-turn|斜前面|双脚脚底|手势终点|一掌在肩前朝外表示拒绝，躯干轻侧转，另一手放在体侧
惊讶后缩抬双手|surprised recoil with raised-hands|侧面|后侧主承重脚|后缩中段|头肩向后缩、双掌抬到胸前，前脚轻抬，不把关节弯向反面
惊恐护头低蹲|startled head-covering crouch|斜侧面|双脚脚底|低蹲终点|双膝弯曲下蹲，双前臂护在头两侧，脊背自然弯曲，无伤害场景
悲伤抹眼角|sad eye-wiping body pose|斜前面|双脚脚底|接触终点|一手轻触眼角，头稍低，另一臂在体侧，肩线下沉
哭泣抱臂自护|crying self-comfort arm-hold|斜前面|双脚脚底|静止|双臂交叉轻抱上臂，肩部收起，头低，完整衣着，无夸张扭身
疲惫弯腰扶膝|tired forward-bend hands-on-thighs|侧面|双脚；双掌扶大腿|休息|髋膝轻屈，上身前倾，两掌支在膝上方大腿处，头自然下垂
急切探身招手|eager forward-lean beckoning|斜前面|前后两脚|招手中段|上身向前探，一前臂抬起朝自己方向招手，另一手放体侧
得意扬下巴站姿|confident chin-raised stance|斜前面|双脚脚底|静止|下巴轻抬，肩部自然展开，一手轻搭腰侧，另一臂放松
礼貌鞠躬致意|polite bowing greeting pose|侧面|双脚脚底|鞠躬中段|双脚稳定，上身从髋部向前倾约三十度，双手在腹前轻叠，头颈顺躯干
''')
group('paired_interaction','双人互动与协作','''
双人握手问候|two-adult-women handshake greeting|斜前面双人全身|两人各自双脚|握手接触帧|A与B面对面，一侧手在两人中间相握，另一臂各自放松，四只手归属清楚
双人碰拳鼓励|two-adult-women fist-bump|斜前面双人全身|两人各自双脚|碰拳接触帧|两人面向彼此，各伸一只松握拳在中间相碰，另一手各自放松
双人击掌庆祝|two-adult-women high-five|斜前面双人全身|两人各自双脚|击掌接触帧|两人各抬一臂，在头部上方两掌相触，另两只手放松，身体保持稳定
双人并肩交谈|two-adult-women side-by-side conversation|斜前面双人全身|两人各自双脚|静止|两人并肩站立，头略转向彼此，A用单手小幅介绍，B自然倾听
双人侧身倾听|two-adult-women listening conversation|斜侧面双人全身|两人各自双脚|静止|A自然说话且一掌上翻，B头轻侧倾面对A，双方保持一步距离
伸手邀请同伴同行|two-adult-women open-hand invitation|斜前面双人全身|两人各自双脚|邀请手势终点|A向B伸出一只开放手掌，B抬一手准备回应，两手尚未接触
双人递交书本|two-adult-women book handover|斜侧面双人全身|两人各自双脚；两人手托书|交接接触帧|A从两侧递一本合拢小书，B从下方接住，同一本书位于两人中间
双人接过纸箱|two-adult-women small-box handover|斜侧面双人全身|两人各自双脚；四手承箱|交接接触帧|A和B站稳，一只小纸箱位于两人中间，双方各两手承托，手臂不穿箱
双人合力抬箱|two-adult-women shared box carry|斜前面双人全身|两人各自双脚；四手承箱|抬起静止帧|两人站在中等箱子的两端，各用双手托底，箱子离地且膝轻屈
一手扶肩安慰同伴|two-adult-women shoulder-comfort gesture|斜前面双人全身|两人各自双脚|接触终点|A站在B侧前方，一手轻搭B肩部；B头稍低，另一侧手臂各自放松
双人并肩侧拥抱|two-adult-women friendly side-hug|正面双人全身|两人各自双脚|拥抱接触帧|两人并肩，一侧手臂各绕对方肩背，另两臂在外侧放松，完整衣着
双人正面轻拥抱|two-adult-women friendly front-hug|斜后方双人全身|两人各自双脚|拥抱接触帧|两人成年女性面对面自然轻拥，手掌搭在对方上背，双腿各自独立，无亲吻
搀扶同伴慢走|two-adult-women assisted walking|斜前面双人全身|两人各自脚底与前臂接触|慢走中段|A轻扶B一侧前臂，两人同向小步走，B自己脚底承重，无伤口或急救场景
扶起地面坐姿同伴|two-adult-women hand-assisted floor-rise|斜侧面双人全身|A双脚；B一脚一膝与一手|起身中段|A稳定站立并伸一手，B由地面单膝姿一手握A手、一脚踩地起身，不悬吊身体
双人同步并肩行走|two-adult-women synchronized walk|斜前面双人全身|两人各自承重脚|行走中段|A与B并肩向前行走，各自一脚承重，双臂自然摆动且不交叉到对方身上
双人背对背警戒|two-adult-women back-to-back watch|斜侧面双人全身|两人各自双脚|静止|两人背对背站立但不完全靠压，面朝相反方向，双臂各自轻屈在身前，无武器
''',actors=2,layout='landscape')
group('sport_adventure','运动、舞蹈与冒险动作','''
弓步热身定格|forward-lunge warm-up pose|侧面|前后两脚|弓步终点|前膝弯曲、后腿向后伸，躯干基本直立，双手轻搭髋部
侧弓步伸展定格|side-lunge stretch pose|正面|双脚脚底|侧移终点|一膝向侧方弯曲，另一腿自然伸展，双手置于屈膝侧大腿上
单脚抓踝舒展|standing quadriceps ankle-hold|侧面|单侧脚底；单手握另一脚踝|伸展终点|一腿站立，另一膝屈曲向后，一手轻握后侧脚踝，另一臂前伸平衡
单腿前伸平衡|single-leg forward-reach balance|侧面|单侧脚底|平衡终点|一腿支撑，躯干从髋前倾，另一腿向后适度抬起，双臂向前伸展
舞蹈提膝准备位|dance raised-knee preparation|斜前面|单侧脚底|提膝终点|一膝提至髋前，支撑腿轻伸，双臂形成柔和开放弧线，仍穿运动长裤
舞蹈横跨步定格|dance side-stride pose|正面|外侧承重脚|跨步中段|一脚向侧方迈出，另一脚轻点地，双臂朝相反对角展开
舞蹈双臂圆弧位|dance rounded-arm standing pose|正面|双脚前掌与脚底|静止|双臂在头前上方形成开放圆弧，两手不接触，双脚小幅错开，肩部放松
舞蹈单脚转位准备|dance single-foot turn preparation|斜前面|单侧前脚掌|转身准备|一脚前掌承重且脚跟抬起，另一膝轻屈收近支撑腿，双前臂在身前成弧
徒手防御架势定格|unarmed defensive guard pose|斜侧面|前后两脚|静止|前后脚错开、双膝轻屈，双前臂抬在脸前下方，握拳自然，无对手与武器
前拳伸出定格|single-forward-punch pose study|侧面|前后两脚|伸拳终点|一拳向前伸到肩高但肘未锁死，另一拳收近躯干，肩髋轻转，无击中对象
抬膝防护定格|raised-knee guarded balance|斜侧面|单侧脚底|提膝终点|一膝抬向身前，双前臂护在胸前，另一腿稳稳支撑，无对手或伤害
侧步闪避定格|side-step evasive body pose|正面|外侧主承重脚|侧移中段|重心移向一侧屈膝腿，上身轻偏，另一脚准备跟进，双臂自然平衡
单手撑越矮台|one-hand low-vault pose study|侧面|一手掌与近侧脚|越台中段|一掌撑在腰下高度矮台，另一腿屈膝抬过台面，仍有一脚接地，不作高难度腾空
攀梯上行定格|ladder-climbing upward frame|侧面|双手与两脚分别接梯档|上攀中段|小型稳固梯子仅三到四档，一脚高一脚低，双手握不同梯档，完整梯脚可见
低位攀岩四点支撑|low-rock four-contact climbing pose|斜背面|双手与双脚接矮岩点|移动准备|矮岩面上四肢分别接不同支点，一膝弯曲较深，身体近岩面，头手脚全部可见
前倾水平飞行姿态|forward horizontal fantasy-flight pose|侧面全身|幻想腾空，无地面支撑|飞行中段|身体斜向前水平伸展，一臂前伸、一臂侧后展开，双腿自然向后延伸，无翅膀和光效
''',layout='landscape')
