"""V31: headphones, earphones and communications headsets shown worn."""
from catalog_content import CATALOG,category,add

CATEGORY='headphones'
category(CATEGORY,'耳机与耳麦佩戴','32种耳机、耳塞与耳麦的成年角色佩戴参考，比较耳罩包耳或压耳、耳塞入耳、耳夹与耳挂的固定方式，以及头梁、后颈带、麦克风和线缆走向。小型耳机附同一耳部放大图；造型与幻想款另行标明。',['R102','R103','R104','R105'])
GROUPS=[{'id':'headband','name':'头戴与佩戴方式','count':8},{'id':'professional','name':'专业耳麦与造型款','count':8},{'id':'earbuds','name':'耳塞与入耳佩戴','count':8},{'id':'open_ear','name':'开放式与单耳通讯','count':8}]

ROWS='''
包耳封闭式耳机|closed-back over-ear headphones|斜前面|头顶头梁与双耳周围|大椭圆厚耳垫完整包住耳廓，封闭外壳和可调滑杆清楚，头梁压在头顶|headband
小耳罩压耳式耳机|compact on-ear headphones|斜侧面|头顶与耳廓表面|小圆耳垫压在外耳表面，耳廓边缘露出，细头梁与小罩尺寸区别于包耳式|headband
网罩开放式大耳机|open-back grille headphones|侧面略前|头顶与双耳周围|大耳罩外侧为可见细金属网格，双叉支架连接头梁，耳垫包耳；开放指外壳结构|headband
双梁悬挂式耳机|suspension-headband headphones|斜前面|柔性内头带与外框|一条柔性宽内头带贴住头顶，上方另有两根细框架拱梁，圆耳罩在两侧|headband
复古海绵压耳耳机|retro foam-pad headphones|斜侧面|细金属头梁与耳廓|极细金属头梁、橙色薄海绵圆耳垫与简洁塑料连接件，细耳机线自然垂下|headband
折叠铰链便携耳机|hinged portable headphones|斜侧面|头顶与耳上铰链|中号耳罩正常戴在耳上，头梁两端的折叠铰链和旋转接头外露，不画成收纳状态|headband
DJ单耳监听戴法|single-cup DJ monitoring wear|斜前面|一耳罩贴耳与另一耳罩抬起|旋转头梁斜跨头顶，一侧耳罩紧贴耳部，另一侧耳罩转向头后；无手遮住结构|headband
双耳罩挂颈戴法|headphones resting around neck|正面略侧|颈后头梁与锁骨两侧|耳机从耳上取下挂在颈部，两个耳罩朝前置于锁骨两侧，头梁绕颈后，两耳完整露出|headband
电竞双耳麦克风耳机|gaming headset with boom mic|斜前面|头顶双耳与嘴侧|厚耳罩、简单几何灯条与短鹅颈麦克风，麦头停在嘴角旁，正常成人耳机无品牌|professional
广播监听通话耳麦|broadcast monitoring headset|斜侧面|头梁双耳与嘴侧|黑色大包耳监听罩和粗稳麦杆，泡棉麦头位于嘴边留有间隙，单侧螺旋线向肩下走|professional
航空通话耳麦|aviation communication headset|斜前面|头顶双耳与面颊外侧|宽软头垫、双金属支架、浅灰厚耳罩与泡棉麦头，可见独立导线在肩前垂下|professional
头盔导轨通讯耳麦|helmet-rail communication headset|斜侧面|头盔侧导轨与双耳|中性深色无标志头盔，两侧导轨短支臂固定耳罩，不用头顶头梁；下颌带与嘴侧麦杆清楚|professional
舞台入耳监听与耳麦|stage in-ear monitors with cheek mic|侧面略前|耳内监听塞与耳后麦挂|透明小型入耳监听塞由细线绕耳后，另有肤色细麦挂从耳后沿面颊至嘴角，两者为不同部件|professional
猫耳装饰头戴耳机|cat-ear decorated headphones|斜前面|真实耳罩与头梁上装饰|普通包耳耳机的头梁上有两枚小三角猫耳装饰，发型和真实人耳正常，没有生物兽耳|professional
科幻机械耳罩装置|fictional mechanical earcup headset|斜侧面|耳罩支架与头顶弧梁|原创科幻耳罩由头顶硬弧梁固定，外罩有分层机械片、短天线与延伸杆，耳罩和皮肤接触关系明确；幻想设计|professional
针织保暖音频耳罩|knit audio earmuff headphones|斜前面|针织头梁与双耳罩|针织包覆头梁与毛绒圆耳罩，罩侧有小音频控制钮和短接线，明确是带音频单元的保暖耳机|professional
有线平头耳塞|wired flat-head earbuds|侧面略前|耳甲腔与向下线缆|圆盘形小耳塞靠在耳甲腔，没有硅胶套或深插导管，细线从耳塞底部自然下垂|earbuds
硅胶套入耳耳塞|silicone-tip in-ear earphones|侧面略前|耳道入口与向下线缆|小入耳壳体坐在耳甲处，软硅胶套只在入口接触耳道，细线从底部下垂，不把耳塞画成耳环|earbuds
长柄真无线耳塞|stem-style true wireless earbuds|侧面略前|耳甲腔与耳垂前方|白色小耳塞主体固定在耳中，短直柄沿耳垂前方朝下，没有任何外接线缆|earbuds
豆形真无线耳塞|bean-shaped true wireless earbuds|侧面略前|耳甲腔内部|紧凑深色豆形壳贴在耳甲腔内，没有长柄、耳挂或线，触控小面板露在外侧|earbuds
鲨鱼鳍稳固运动耳塞|wingtip sport earbuds|侧面略前|耳甲腔上缘与耳道入口|小耳塞外有柔软短弧形稳固翼，翼嵌在耳甲腔上缘内而不是挂到整只耳朵外面|earbuds
外耳挂运动入耳耳机|earhook sport in-ear earbuds|侧面略后|上耳根外侧与耳道入口|入耳塞配独立粗软耳挂，耳挂绕过上耳根延伸到耳后，硅胶入耳端仍坐在耳道入口|earbuds
颈挂线缆式耳塞|neckband earphones worn in ears|斜侧面|颈后软带与双耳|轻薄U形电子颈带绕过颈后，左右各一条短线连接已戴入两耳的小耳塞，线不绕喉打结|earbuds
绕耳线舞台监听塞|over-ear-cable in-ear monitors|侧面略后|耳甲腔与耳后线缆|半透明定形监听塞填合耳甲，细线从耳塞上方先绕过耳根再从耳后下垂，导线不穿过耳朵|earbuds
后颈带骨传导耳机|rear-band bone-conduction headphones|侧面略后|耳前颧侧与后颈弧带|两枚小振动单元贴在耳前颧侧皮肤，细弧带绕耳上方接到后颈，耳道入口完全开放|open_ear
耳挂开放式气传导耳机|open-ear air-conduction earhooks|侧面略前|耳后支座与耳道外前方|软挂绕过耳根，细长扬声器悬在耳道外侧前方，不插耳道、不贴到颧骨；耳口可见|open_ear
耳夹开放式耳机|cuff-style open-ear earbuds|侧面略后|耳廓边缘前后两侧|柔性C形连接桥绕住耳廓边缘，小前扬声器与较大后电池分置耳前耳后，耳道开放|open_ear
圆盘夹耳式耳机|disc-shaped clip-on headphones|侧面略前|外耳表面与耳后夹扣|薄圆盘耳罩贴外耳表面，小弹性耳后夹扣固定，没有头梁；细线在耳下可见|open_ear
镜腿扬声器音频眼镜|audio glasses with temple speakers|斜侧面|鼻梁与双耳上方镜腿|普通透明镜片眼镜配明显加厚镜腿，耳前镜腿下侧有小扬声孔，耳朵与耳道不被罩住|open_ear
长柄单耳蓝牙耳麦|single-ear Bluetooth headset|侧面略前|单侧耳内与耳后小挂|一侧小耳塞由细耳挂固定，窄长麦杆顺面颊伸向嘴侧，另一只耳朵无设备，没有头梁|open_ear
单耳头梁通话耳麦|mono headband communication headset|斜前面|一侧耳垫与另一侧头垫|细头梁跨头顶，一侧小耳罩压耳并有麦杆，另一侧仅小软头垫贴太阳穴上方，另一耳空出|open_ear
双耳轻型客服耳麦|lightweight dual-ear office headset|斜前面|头顶细梁与双耳小垫|轻薄头梁与两枚小软耳垫，纤细麦杆从一侧伸到嘴角旁，细线沿肩部向下，不画成大电竞罩|open_ear
'''

for line in ROWS.strip().splitlines():
    name,en,view,anchor,recipe,group=line.split('|')
    dimension='头戴、专业耳麦与造型款' if group in ['headband','professional'] else '耳塞、开放式与单耳通讯'
    add(CATEGORY,dimension,f'{name}|{en}|{recipe}。')
    refs=['R102'] if name=='后颈带骨传导耳机' else ['R103'] if name in ['绕耳线舞台监听塞','舞台入耳监听与耳麦'] else ['R104'] if name=='耳夹开放式耳机' else ['R105'] if group in ['professional','open_ear'] and '麦' in name else []
    CATALOG[-1].update(added_in='31.0',headphone_reference=True,headphone_group=group,headphone_view=view,headphone_anchor=anchor,headphone_construction=recipe,headphone_detail_inset=group in ['earbuds','open_ear'] or name=='舞台入耳监听与耳麦',adult_only=True,minor_reference=False,age_min=25,
        reference_ids=refs,note='成年角色的耳机佩戴造型参考。先确认耳罩、耳塞或耳挂与耳廓的真实接触位置，再画头梁、支架、麦杆和线缆；侧发拨开露出设备，小型耳机的放大图对应同一侧耳部。舞台、职业与幻想外形用于角色设计，不按外观推断音质、降噪或防护性能。')
assert len([e for e in CATALOG if e.get('headphone_reference')])==32
