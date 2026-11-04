"""Ten fictional identity archetypes in paired adult character looks."""
from catalog_content import CATALOG,CATEGORIES,category,add
NEW_CATEGORIES=['identity_status','identity_duties','identity_classic']
for cid,name,guide in [
 ('identity_status','地位与家世','反派千金、落魄千金、女王与亡国公主，各两套成年原创造型。用家徽、冠饰、衣料、随身物和姿态表达架空故事身份及处境。'),
 ('identity_duties','使命与职业身份','圣女、女管家与女总裁，各两套成年原创造型；比较使命、职责、礼装与行动装束。均为角色设计方案，不等于真实职业统一制式。'),
 ('identity_classic','经典人设与双重身份','文学系、三无系和双重身份，各两套成年原创造型。经典人设观察书册、妆发、表情与动作；双重身份把同一人物的公开与隐藏身份并排展示。')]:
    category(cid,name,guide,['R63'])
NEW_ENTRIES=[];GROUPS=[]
KINDS={
 'villainess':('identity_status','反派千金',['恶役千金','恶役大小姐','反派大小姐','villainess'],['HT008','NK006','GL010','BC002']),
 'fallen_heiress':('identity_status','落魄千金',['落难千金','失势贵族','fallen heiress'],['HT019','PN007','BC006']),
 'queen':('identity_status','女王',['女皇','女帝','女君主','queen'],['HT012','NK007','BC002']),
 'exiled_princess':('identity_status','亡国公主',['流亡公主','逃亡公主','exiled princess'],['HT019','PN007','BE001']),
 'saintess':('identity_duties','圣女',['祈愿圣女','巡礼圣女','saintess'],['HT026','PN010','HG053']),
 'butler':('identity_duties','女管家',['女执事','女性管家','female butler'],['HT012','GL001','GE012']),
 'executive':('identity_duties','女总裁',['女企业家','公司掌舵者','female executive'],['HT015','WT003','EG008']),
 'literary':('identity_classic','文学系',['文学少女','书卷系','文学青年','literary archetype'],['HT019','EG001','GE013']),
 'kuudere_silent':('identity_classic','三无系',['三无少女','无口','寡言角色','emotionally restrained archetype'],['HB001','WT001']),
 'double_identity':('identity_classic','双重身份',['双面身份','隐藏身份','秘密身份','double identity'],['HT002','EG001','GL003','GE021'])}

def pair(key,character,text):
    cid,label,aliases,parts=KINDS[key];GROUPS.append((key,cid,label,character))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==2
    for i,(name,en,desc,recipe) in enumerate(rows,1):
        add(cid,label,f'{label}·{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(identity_reference=True,identity_kind=label,identity_pair=key,identity_order=i,identity_character_design=character,identity_components=parts,
          added_in='51.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[label,'身份','经典设定','经典人设','代表造型',*aliases],
          note='成年原创角色的身份与故事造型参考；同一图页的两套方案保持人物面容和标志性饰物一致。身份由角色设定、服装、道具与表演共同说明，可将整套参考与相关部件加入外观卡。')
        NEW_ENTRIES.append(e)

pair('villainess','Same clearly adult27 woman in BOTH cells: pale warm skin, long glossy dark auburn half-up waves, hazel almond-shaped eyes, mature oval face, distinctive small emerald oval neck jewel. Keep identical face, hair color and jewel across both looks.','''
夜宴绛紫礼裙装|villainess plum evening look|绛紫高领层叠礼裙、长手套与祖母绿颈饰；半扎卷发，手持合拢折扇，抬颏侧睨|Opaque deep-plum high-neck long-sleeve ankle layered formal dress, restrained black lace edging, emerald oval neck jewel, long black gloves and closed low heels; one CLOSED folding fan lightly at waist, tiny superior closed-mouth smile, one outer brow raised and sideward measuring gaze, full standing adult, fictional aristocratic antagonist, no weapon or horror makeup
日间黑金议事装|villainess black-gold daytime look|黑金短外套、完整奶白衬衣与长裙；同款绿宝石饰物与折扇，手势收敛、目光锐利|Opaque black fitted jacket with narrow antique-gold trim over ivory high-collar blouse, full charcoal calf-length skirt, emerald oval jewel fixed at collar, short dark gloves and closed low shoes; closed folding fan held in one hand, other lightly on own hip, composed sharp assessing eyes and small controlled half-smile, same adult character as left
''')
pair('fallen_heiress','Same clearly adult28 woman in BOTH cells: warm light skin, chestnut single low braid, green eyes, mature oval face, small oval leaf-engraved silver locket. Keep identical face, braid and locket.','''
修补旧礼裙装|fallen heiress repaired formal look|褪蓝旧礼裙、细小修补与叶纹旧吊坠；发辫仍整齐，双手轻叠，保留端正站姿|Faded opaque dusty-blue long-sleeve ankle formal dress with small neatly repaired cuff seam and modest hem wear, silver oval leaf-engraved locket, plain closed brown flats; neat single braid and hands softly overlapped at waist, dignified upright posture with restrained wistful eyes, no torn exposure or dirt caricature
朴素旅装留族徽|fallen heiress plain travel look|原色衬衣、深棕长裙与旧外披；保留同一吊坠，挎简朴布包，眼神坚定|Opaque undyed linen long-sleeve blouse, brown full ankle skirt, worn gray short wool cloak with small leaf-shaped clasp and the SAME silver oval locket, plain cloth shoulder bag and flat brown lace-up boots; one hand lightly on bag strap, proud restrained gaze and small firm closed lips, stable traveling stance
''')
pair('queen','Same clearly adult38 woman in BOTH cells: medium-brown skin, dark hair in a smooth low formal bun, deep brown eyes, mature composed angular face, small blue oval gem brooch. Keep same face, bun and brooch.','''
王冠披肩加冕装|queen crown-and-mantle ceremonial look|小型王冠、深蓝长礼服与金缘披肩；蓝宝石胸针、挺直肩线与平静直视|Small refined gold crown clearly on head, opaque navy high-neck long-sleeve ankle court dress, gold-edged pale mantle, blue oval brooch and closed navy low heels; hands calmly overlapped before waist, straight grounded shoulders and authoritative peaceful direct gaze, original fantasy queen without real heraldry
冠饰收敛议政装|queen restrained governing look|低矮冠饰、炭灰长外套与完整长裤；保留蓝宝石胸针，持薄册，神态专注|Low gold circlet instead of tall crown, charcoal long tailored coat over opaque ivory high-neck top and full navy trousers, SAME blue oval brooch, closed dark low shoes; one plain closed thin document folio held at side, other hand makes small measured open-palm explanatory gesture, attentive commanding calm gaze
''')
pair('exiled_princess','Same clearly adult27 woman in BOTH cells: light olive skin, long silver-gray hair in ONE low braid, soft gray eyes, mature oval face, one small oval gold locket. Keep same adult face, braid and locket.','''
简冠旧宫廷礼装|exiled princess former-court look|简洁银冠、雾蓝宫廷长裙与金色旧吊坠；双手护住吊坠，神态沉静而警觉|Small understated silver circlet, opaque smoke-blue long-sleeve ankle court dress with sparse faded silver edging, small oval gold locket and closed low silver shoes; both hands gently hold locket at upper sternum over fabric, composed wary eyes and quiet level lips, full-body standing adult princess, no distressed injury
兜帽斗篷逃亡装|exiled princess hooded travel look|深灰兜帽斗篷叠完整便装、长裤与靴；相同发辫与吊坠仍可见，身体侧转回看|Gray hooded travel cloak with hood DOWN so face and silver-gray braid remain fully visible, opaque taupe covered tunic, narrow simple belt, full charcoal trousers and brown lace-up boots; SAME gold oval locket visible above tunic, one hand holds cloak edge at waist, body quarter-turned with alert look back, no weapons or chase scene
''')
pair('saintess','Same clearly adult29 woman in BOTH cells: warm light skin, honey-blonde crown braid, amber eyes, mature serene oval face, small gold crescent pendant. Keep same face, crown braid and crescent pendant.','''
白金祈愿仪式装|saintess ivory prayer look|白金封闭领口长礼裙、细缘披肩与月形吊坠；冠状发辫、胸前合十，目光安宁|Opaque ivory high-neck long-sleeve ankle dress with fine gold edging, pale cream shoulder mantle, small gold crescent pendant, crown braid and closed white low shoes; hands pressed together at upper sternum with natural fingers and complete wrists, gently lowered peaceful eyes, original fantasy ritual identity with no real religious emblem
浅蓝巡礼行装|saintess pale-blue pilgrimage look|浅蓝短披肩、白色完整内搭与长裙、平底靴；保留月形吊坠，提小灯，姿态温和|Opaque white high-neck long-sleeve top and full calf-length ivory skirt, pale-blue short shoulder cape, small gold crescent pendant and flat lace-up travel boots; holding ONE small unlit brass lantern by handle at side, other hand softly open at waist, compassionate attentive gaze, original adult fantasy pilgrim outfit
''')
pair('butler','Same clearly adult32 woman in BOTH cells: olive skin, neat dark low bun, gray-green eyes, mature straight oval face, small silver chain watch at waist. Keep same face, bun and watch.','''
燕尾马甲执事装|female butler tailcoat look|黑色燕尾外套、白衬衣与灰马甲、长裤；白手套、腰链表与钥匙束，站姿笔直|Opaque black formal tailcoat over crisp white high-collar shirt and gray waistcoat, full black trousers, small black necktie, white cotton gloves, silver waist watch chain and tiny key ring at belt, black closed Oxford shoes; one hand rests over opposite wrist before waist, precise upright stance and composed attentive gaze, female household steward, no maid apron
长外套事务管家装|female butler long-coat working look|炭灰长外套叠完整衬衣马甲与直裤；同款腰链表、手套与薄账册，眉眼专注|Charcoal calf-length tailored long coat over opaque ivory shirt and dark gray waistcoat, full charcoal trousers, same small silver waist watch chain, thin white gloves and closed flat Oxford shoes; holding ONE small plain closed account ledger in one hand at side, other hand adjusts glove cuff, focused courteous neutral expression, no readable text
''')
pair('executive','Same clearly adult35 woman in BOTH cells: medium-brown skin, sleek dark French-twist updo, brown eyes, mature defined oval face, slim rectangular gold wristwatch. Keep same face, updo and watch.','''
深蓝商务掌舵装|female executive navy business look|深蓝西装、完整奶白衬衣与宽腿裤；细腕表、文件夹与克制手势，目光坚定|Navy fitted blazer over opaque ivory collared blouse, full navy wide tailored trousers, slim rectangular gold wristwatch and closed low heels; ONE slim plain document folio held against side, free hand makes a small deliberate palm-up explaining gesture, confident clear direct gaze and composed neutral mouth, no logos or text
浅灰长马甲会谈装|female executive gray meeting look|浅灰长马甲叠完整白衬衣与深色中裙；保留腕表，小手袋、无框眼镜与从容姿态|Pale-gray long tailored waistcoat over opaque white high-neck blouse, charcoal calf-length straight skirt, SAME slim rectangular gold watch, subtle rimless eyeglasses and black closed low heels; small structured handbag held loosely at side, relaxed grounded shoulders and composed attentive half-smile, polished adult leader rather than uniform
''')
pair('literary','Same clearly adult26 woman in BOTH cells: warm light skin, long dark single low braid, brown eyes, mature soft oval face, thin round metal reading glasses. Keep same face, braid and glasses.','''
针织抱书阅读装|adult literary reader knit look|燕麦针织、白色完整衬衣与深棕长裙；圆框眼镜、单辫、抱书，目光柔和专注|Opaque oatmeal fine-knit cardigan over covered ivory blouse, full brown calf-length skirt, thin round metal glasses, one dark low braid and flat brown closed loafers; holding ONE plain closed book gently against lower torso with both hands, warm thoughtful eyes and small relaxed closed lips, adult literary-reader styling, no school insignia or text
围巾手记行走装|adult literary journal travel look|烟绿短外套、奶白内搭与深色长裤；同款眼镜发辫、细围巾和手记本，神态沉静|Smoke-green casual short jacket over opaque ivory crewneck, full charcoal straight trousers, oatmeal thin scarf, SAME round glasses and single dark low braid, flat closed lace-up shoes; ONE plain small closed journal and simple pen held at waist, quiet inquisitive gaze slightly to side and small gentle smile, adult reader outside a library
''')
pair('kuudere_silent','Same clearly adult28 woman in BOTH cells: light olive skin, straight black chin-length bob with blunt bangs, dark gray eyes, mature oval face, plain slim round silver watch. Keep identical face, bob, bangs and watch.','''
极简衬裙静立装|silent restrained minimal skirt look|灰白衬衣与深蓝中长裙；齐刘海短发、极简腕表，双臂自然垂落，眉唇少变化|Opaque pale-gray neat collared long-sleeve blouse, navy calf-length straight skirt, plain slim round silver watch and black flat closed shoes; straight black chin-length bob with blunt bangs, both arms naturally at sides, still balanced upright stance, calm low-motion level brows, relaxed closed lips and steady neutral eyes, quiet fictional emotionally restrained character, not vacant horror or a medical diagnosis
深蓝针织持包裤装|silent restrained navy-knit look|深蓝高领针织与灰色直裤；保持同一短发与腕表，单手持包，目光平静|Opaque navy high-neck fine knit top, full gray straight trousers, SAME slim round silver watch, simple black small handbag and closed black low shoes; identical dark blunt-bang chin bob, one hand loosely holds handbag at side and other arm relaxed, motion-minimal calm neutral face and steady gaze, relaxed mouth with no dramatic sadness or anger
''')
pair('double_identity','MANDATORY identical clearly adult30 woman in BOTH cells: olive skin, dark brown hair tied in the SAME neat low ponytail, hazel eyes, mature oval face, tiny silver stud earrings. Exact same face, skin tone, age, hair color and ponytail, recognizable as the SAME PERSON. Left is her public daytime office identity, right is her hidden nighttime courier-agent identity. No face mask.','''
公开身份日间职员装|double identity public office look|浅灰开衫、完整白衬衣与深色直裤；圆框眼镜、低马尾和普通托特包，神态温和低调|PUBLIC DAYTIME role: pale-gray cardigan over opaque white collared shirt, full navy straight trousers, thin round glasses, plain canvas tote and flat brown loafers, SAME dark low ponytail and tiny silver studs; shoulders gently relaxed, small friendly closed-mouth smile and modest attentive gaze, no visible tactical gear or insignia
隐藏身份夜间联络装|double identity hidden courier-agent look|深墨短夹克、完整高领内搭与机能长裤；摘下眼镜，同一低马尾与银耳钉，耳麦、露指手套，目光警觉|HIDDEN NIGHTTIME role: dark charcoal fitted short utility jacket over opaque black high-neck top, full dark utility trousers, thin black fingerless gloves, small plain belt pouch, tiny discreet earpiece and closed flat black ankle boots; NO glasses, exact SAME olive adult face, dark low ponytail and tiny silver earrings as left, alert focused eyes and firm composed lips, one hand lightly near earpiece, no weapons, violence or realistic insignia
''')

assert len(NEW_ENTRIES)==20 and len(GROUPS)==10

def make_identity_combinations(entries):
    by_id={e['id']:e for e in entries};out=[]
    palettes={'villainess':'绛紫、黑金与祖母绿','fallen_heiress':'褪蓝、原色与旧银','queen':'深蓝、炭灰与金','exiled_princess':'雾蓝、深灰与旧金','saintess':'白金与浅蓝','butler':'黑、白与炭灰','executive':'深蓝、浅灰与金','literary':'燕麦、深棕与烟绿','kuudere_silent':'灰白与深蓝','double_identity':'日间浅灰与夜间深墨'}
    for key,(cid,label,aliases,parts) in KINDS.items():
        es=[e for e in entries if e.get('identity_pair')==key];assert len(es)==2
        ids=[e['id'] for e in es]+parts;assert all(i in by_id for i in ids)
        out.append({'name':'身份设定·'+label,'description':'两套身份造型与可选搭配部件；'+('同一人物的公开与隐藏身份。' if key=='double_identity' else '可比较衣物、标志饰物、表情与姿态。'),'palette':palettes[key],'entry_ids':ids,'identity_example':True,'identity_kind':label,'added_in':'51.0'})
    return out
