"""Cross-category editorial labels and common search vocabulary."""
FAMILIES=[
 ('gothic','哥特',['goth','gothic','哥特式','哥特风'], '高领、蕾丝、绒面、尖形饰件、剪裁与叠层可组合；传统、浪漫、工业与赛博方向分别观察。',['R22']),
 ('british','英伦',['British style','English country','英式','英国风','英伦风'], '宽泛审美标签；乡村粗花呢、学院针织、城市风衣与正式剪裁可分别组织。',['R25','R06']),
 ('lolita','洛丽塔时尚',['Lolita','萝莉塔','Lolita fashion','lo娘','洛丽塔'], '以有支撑的蓬裙、布衫、蕾丝与头饰等形成整套协调；甜系、古典、哥特与混搭款分开观察。',['R23']),
 ('punk','朋克',['punk','punk style','朋克风'], 'DIY拼接、磨损、格纹、皮革、金属件与不对称剪裁按具体部件组织。',['R24']),
 ('preppy','学院',['preppy','学院风','学院派'], '衬衣、针织背心、滚边外套与裙裤搭配，成人日常学院造型。',['R06']),
 ('dark_academia','暗黑学院',['dark academia','暗黑学院风','复古学院'], '深棕、深灰、粗花呢、羊毛与复古衬衣组合，标签用于整理原创搭配。',['R06']),
 ('mori','森系',['mori','mori kei','森女风','森系风'], '自然色、松量、针织与亚麻叠层，重点是软材质与长短层次。',['R06']),
 ('cottagecore','田园',['cottagecore','田园风','乡村田园'], '布裙、抽褶、围裙和植物印花用于田园场景，具体地域服饰另行核对。',['R06']),
 ('boho','波西米亚',['boho','bohemian','波西米亚风'], '刺绣、钩织、围裹、长裙、宽裤与编织配饰可组合；图例为原创搭配。',['R06']),
 ('minimal','极简',['minimal','minimalist','极简风','性冷淡风'], '以轮廓、面片与材质差异为重点，减少装饰密度。',['R06']),
 ('retro','复古优雅',['retro','vintage','复古风','优雅复古'], '按不同剪影与材质组织复古改编，具体时代以实物研究为准。',['R06','R07']),
 ('streetwear','街头',['streetwear','hip hop','街头风','嘻哈'], '宽松量、运动元素、叠层与工具袋按比例组织，不使用品牌标识。',['R06']),
 ('techwear','机能',['techwear','机能风','功能服'], '防雨层、可拆袋、扣带与关节拼片要有可说明的用途。',['R06']),
 ('cyberpunk','赛博朋克',['cyberpunk','赛博','赛博风'], '原创未来都市穿搭；技术分区、设备固定点与局部光色形成识别。',['R06']),
 ('steampunk','蒸汽朋克',['steampunk','steam punk','蒸汽幻想'], '复古剪裁与原创机械设备结合，仪表和带具的位置要有构造理由。',['R22','R06']),
 ('chinese','国风',['中国风','中国传统','中式风格','Chinese-inspired'], '按具体形制、朝代改编、戏曲行头和架空国风分别组织；国风是创作检索标签。',['R27','R28','R29','R30']),
 ('jirai','地雷系',['jirai','jirai kei','地雷风','地雷女装','地雷系服装','地雷系'], '黑粉、黑白等配色配合大领结、荷叶边、蕾丝与厚底鞋；按实际衣裙结构识别。',['R41','R47']),
 ('ryousangata','量产型',['ryousangata','ryosan','量产系','量産型','量产型女装'], '浅色领结衬衫、收腰裙、软针织、饰扣与玛丽珍鞋等组合；与地雷系存在重叠。',['R47']),
 ('girly','甜美少女系',['girly','girly fashion','甜美系','少女系','ガーリー'], '成年甜美穿搭标签；圆领、泡袖、小结饰、针织与柔软裙装按比例组合。',['R47']),
 ('french_girly','法式少女系',['French girly','フレンチガーリー','法式少女','法式甜美'], '现代穿搭标签；黑白奶油色、滚边短外套、贝雷帽与细领结组合，并非法国历史服制。',['R47']),
 ('fairy_kei','妖精系',['fairy kei','fairy-kei','フェアリー系','粉彩妖精系'], '粉彩、复古玩具感原创图案、宽卫衣、软纱裙、条纹袜与轻量饰件；名称是服装风格。',['R42']),
 ('decora','缀饰系',['decora','デコラ','装饰系','缀饰风','原宿缀饰'], '彩色发夹、手链、项链与挂件密集叠加，DIY拼接与鲜色衣裙形成装饰分区。',['R43']),
 ('gyaru','辣妹系',['gyaru','ギャル','日系辣妹','辣妹风'], '子风格很多；观察蓬卷发、妆容、甲饰与牛仔、豹纹、平台鞋等组合，图例为原创改编。',['R44']),
 ('hime_gyaru','姬辣妹系',['hime gyaru','hime-gyaru','姫ギャル','姬系辣妹','公主辣妹'], '姬辣妹原创方向：玫瑰、结饰、蕾丝、贴腰短裙与高体积卷发，按具体裙型区分洛丽塔搭配。',['R44']),
 ('visual_kei','视觉系',['visual kei','ヴィジュアル系','视觉摇滚','V系'], '音乐舞台与街头穿搭灵感：夸张发型、强妆、深色剪裁、不对称叠层和原创带扣。',['R45']),
 ('grunge','Grunge做旧风',['grunge','垃圾摇滚风','颓废风','做旧风'], '旧感格衬、宽针织、牛仔、补片与不匹配叠层，磨损指服装质感。',['R46']),
 ('yume_kawaii','梦かわ',['yume kawaii','yume-kawaii','ゆめかわいい','梦可爱','梦幻可爱系'], '粉彩、云星、渐变与软毛绒等服装图案和材质的原创组合。',['R47']),
 ('yami_kawaii','病かわ',['yami kawaii','yami-kawaii','やみかわいい','病可爱','病可爱系'], '粉黑对比、抽象裂心与缎带图案的原创穿搭，用衣物图案表达视觉主题。',['R47']),
 ('tenshi','天使系',['tenshi kaiwai','tenshi','天使界隈','天使系女装','白蓝系'], '白与水蓝的现代宽松运动、轻机能穿搭；名称用于服装检索，图例不需要翅膀。',['R48']),
 ('y2k','Y2K千禧风',['Y2K','千禧风','千禧辣妹','2000s inspired'], '当代千禧灵感改编：短上衣、喇叭裤、金属色、运动套装与小肩包，避免概括所有年代服饰。',['R46'])
]
SHOULDERS={
 'bardot':('一字肩／露双肩',['一字肩','露肩','露双肩','Bardot','off shoulder','off-the-shoulder']),
 'cold_shoulder':('挖肩／肩窗',['挖肩','露肩袖','冷肩','开肩','cold shoulder','cold-shoulder']),
 'one_shoulder':('单肩／斜肩',['单肩','斜肩','露单肩','one shoulder','one-shoulder']),
 'strapless':('抹胸／无肩带',['抹胸','无肩带','露肩','strapless','bandeau']),
 'halter':('挂脖／挂颈',['挂脖','挂颈','绕颈','露肩','halter','halterneck']),
 'thin_strap':('细吊带',['细吊带','细肩带','吊带','spaghetti strap']),
 'detached_sleeve':('分离袖露肩',['分离袖','露肩','detached sleeve']),
 'cross_strap':('交叉带开肩',['交叉肩带','交叉挂脖','开肩','露肩','cross halter'])
}
EXISTING_SHOULDERS={
 '单肩斜裁上衣':'one_shoulder','单肩礼服':'one_shoulder','挂颈上衣':'halter',
 '挂颈领':'halter','吊带长裙':'thin_strap','衬裙式连衣裙':'thin_strap',
 '开肩袖':'cold_shoulder','挂颈宽腿连体裤':'halter','肩覆领晚礼服':'bardot'
}
EXISTING_STYLES={
 '哥特灵感':['gothic'],'甜系洛丽塔时尚':['lolita'],'古典洛丽塔时尚':['lolita'],
 '朋克灵感':['punk'],'蒸汽幻想':['steampunk'],'学院灵感':['preppy'],
 '机能装备':['techwear'],'街头层搭':['streetwear'],'未来都市':['cyberpunk'],
 '暗色古典叠裙装':['gothic'],'格纹马甲学院成人装':['preppy','dark_academia'],
 '城市机车裙装':['punk'],'机械街头背心装':['techwear','streetwear'],
 '书店复古马甲装':['dark_academia'],'花园宽帽裙装':['cottagecore']
}
def apply_facets(entries):
    families={k:{'id':k,'name':name,'aliases':aliases,'guide':guide,'source_ids':sources} for k,name,aliases,guide,sources in FAMILIES}
    for e in entries:
        styles=list(dict.fromkeys(e.get('styles',[])+EXISTING_STYLES.get(e['name'],[])))
        e['styles']=styles
        aliases=list(e.get('aliases',[]))
        for style in styles:
            assert style in families,style
            f=families[style];aliases += [f['name']]+f['aliases']
        for required,words in [({'gothic','lolita'},['哥特洛丽塔','gothic lolita','gothic-lolita']),({'punk','lolita'},['朋克洛丽塔','punk lolita']),({'gothic','punk'},['哥特朋克','goth punk']),({'british','preppy'},['英伦学院','British preppy'])]:
            if required<=set(styles):aliases+=words
        if 'lolita' in styles:
            for word,en in [('甜系','sweet'),('古典','classic'),('田园','country'),('和风','Japanese-inspired'),('中式','Chinese-inspired')]:
                if word in e['name']:aliases += [word+'洛丽塔',en+' lolita']
        e['shoulder_type']=e.get('shoulder_type') or EXISTING_SHOULDERS.get(e['name'])
        if e['shoulder_type']:
            label,words=SHOULDERS[e['shoulder_type']];e['shoulder_name']=label
            aliases += ['露肩','肩部开口','裸肩']+words
            if e['category']=='tops':aliases+=['露肩上衣','露肩上装','露肩衣',words[0]+'上衣']
            if e['category']=='onepiece' and any(word in e['en'].lower() for word in ['dress','gown']):aliases+=['露肩连衣裙','露肩裙',words[0]+'连衣裙',words[0]+'裙']
            if e['shoulder_type']=='bardot':aliases+=['一字领','offshoulder']
        e['keywords']=list(dict.fromkeys(e['keywords']+aliases))
    for f in families.values():
        f['count']=sum(f['id'] in e['styles'] for e in entries)
        f['clothing_count']=sum(f['id'] in e['styles'] and e['category']!='style' for e in entries)
    return list(families.values())
