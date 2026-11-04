"""V36: additional themed intimate-apparel ensembles on neutral adult tailoring forms."""
from catalog_content import CATALOG,add

GROUPS=['复古礼装与浪漫主题','幻想节庆与舞台主题','都市职业与材质主题']

def block(dimension,text):
    start=len(CATALOG);add('intimate_costumes',dimension,text)
    assert len(CATALOG)-start==16
    for entry in CATALOG[start:]:
        entry.update(added_in='36.0',intimate_theme_reference=True,special_expansion=True,adult_only=True,minor_reference=False,age_min=25,
            presentation='neutral-adult-tailoring-form',age_context='成年尺码服装人台',
            aliases=['情趣','情趣主题','情趣装扮','主题内衣','主题成衣','intimate apparel',dimension],
            outfit_components=entry['description'].split('；'),reference_ids=['R13','R63'],
            note='原创主题成衣设计，使用中性灰成年尺码服装人台展示。观察主题轮廓、胸衣与连体衣裁片、短裙短裤和配饰搭配；蕾丝与透明罩层下面保留不透明成衣衬底。复古、职业和幻想元素均为舞台灵感改编。')

block(GROUPS[0],'''
洛可可缎带主题胸衣|rococo-ribbon bustier ensemble|浅粉不透明缎面胸衣与奶油白高腰灯笼短裤；胸前小蝴蝶结与层叠短罩裙；蕾丝袖套、颈饰和低跟鞋
巴洛克金纹主题胸衣|baroque-gold brocade bustier ensemble|黑金不透明织纹胸衣与黑色高腰短裤；腰侧两片金纹裙摆；金边短披肩、头饰和黑色鞋
维多利亚高领主题礼装|Victorian-inspired high-collar ensemble|奶油白不透明高领蕾丝衬裙与黑色收腰胸衣；长袖蕾丝覆层保留白色衬底；小发梳、黑色长袜与系带鞋
爱德华泡袖主题成衣|Edwardian-inspired puff-sleeve ensemble|象牙白泡袖短衬衣叠粉棕不透明胸衣；同色高腰灯笼短裤；花边长袜、窄领结与低跟鞋
装饰艺术几何主题套装|art-deco geometric intimate-apparel set|祖母绿不透明几何拼片胸衣与高腰短裤；金色扇形绣纹和窄短罩裙；几何头带、腕饰与绿金鞋
黑白歌剧燕尾主题装|black-white opera-tail ensemble|白色不透明连体成衣配黑色长燕尾背片；黑白翻领与前襟扣；小礼帽、长手套和黑色鞋
羽饰卡巴莱主题胸衣|feather-trim cabaret bustier ensemble|酒红不透明胸衣和同色高腰平口短裤；腰侧短流苏和小型羽饰头箍；长手套、长袜与黑色鞋
爵士流苏主题短裙|jazz-fringe slip-dress ensemble|深蓝不透明吊带短衬裙；裙外分层银色短流苏随下摆垂落；几何发带、短手套和细带鞋
银幕缎袍主题礼装|old-screen satin-robe ensemble|香槟色不透明长吊带衬裙；外罩宽袖长缎袍，领缘为柔软羽毛感饰边；缎带腰结与同色鞋
新娘头纱主题衬裙|bridal-veil slip ensemble|象牙白不透明宽肩带短衬裙与衬底蕾丝腰片；短头纱垂至肩后；白色手套、长袜和浅色鞋
黑玫瑰哥特主题胸衣|black-rose gothic bustier ensemble|黑色不透明胸衣与高腰短裤；暗红玫瑰绣片、黑色短蕾丝罩裙；尖形小发饰、长手套与黑鞋
宫廷假领袖套主题装|court-collar and cuff ensemble|宝蓝不透明连体成衣与独立白色褶边假领；同色腰侧短裙片；白色宽袖套、珍珠扣与蓝色鞋
红黑荷叶边主题成衣|red-black ruffle intimate-apparel set|红色不透明收腰胸衣配黑色高腰短裤；一侧斜落红黑荷叶裙片；小花发梳、袖口花边与黑色鞋
香槟褶边浪漫主题装|champagne-ruffle romantic ensemble|香槟米色不透明胸衣与高腰短裤；胸口和短罩裙有细密同色褶边；细缎带发箍、薄袖套与浅色鞋
珍珠点缀轻礼装|pearl-accent intimate evening ensemble|灰紫不透明长线胸衣与高腰短裤；腰侧小裙片以小珍珠点缀；珍珠肩带装饰、腕饰和灰紫鞋
宝石夜宴罩衫主题装|jewel-evening overdress ensemble|深酒红不透明吊带连体衣；外罩黑色开襟长袖网纱罩裙；领口宝石扣、窄缎带腰饰与低跟鞋
''')
block(GROUPS[1],'''
月夜女巫主题套装|moonlit-witch intimate-apparel ensemble|深紫不透明胸衣与高腰短裤；月牙扣短披肩和尖顶软帽；条纹长袜、短手套与紫黑鞋
蝙蝠翼主题连体装|bat-wing themed bodysuit ensemble|黑色不透明高领连体成衣；腰后接小型蝙蝠翼背饰与锯齿短裙片；尖耳头饰、袖套与黑色鞋
小恶魔角尾主题装|little-devil horn-and-tail ensemble|暗红不透明胸衣与高腰短裤；黑色短尾裙和服装假尾饰；小角发箍、长手套与红黑鞋
云羽天使主题成衣|cloud-feather angel ensemble|白色不透明连体成衣与柔白短罩裙；背部小型白羽翼和圆环头饰；白色腕饰、长袜与浅色鞋
森林精灵叶片主题装|forest-elf leaf-panel ensemble|墨绿不透明叶片拼缝胸衣与高腰短裤；腰侧叶形短裙片；叶冠、护腕式袖饰和绿色短靴
花瓣妖精主题成衣|petal-fairy intimate-apparel ensemble|玫瑰粉不透明胸衣和高腰短裤；大花瓣形短罩裙；小花冠、半透明蝶翼背饰与花瓣腕饰
蝶翼舞台主题套装|butterfly-wing stage ensemble|蓝紫不透明几何连体成衣；腰侧短纱裙下面有完整衬底；对称蝶翼背饰、触角头饰和蓝紫鞋
冰晶雪后主题礼装|ice-crystal snow-queen ensemble|冰蓝不透明胸衣与高腰短裤；银白短罩裙和高领短披肩；冰晶头冠、白色长手套与浅蓝鞋
星占师月相主题装|star-reader moon-phase ensemble|午夜蓝不透明连体成衣；金色星月刺绣与不对称短披片；小月冠、金边袖套和深蓝鞋
幻海鳞片主题成衣|fantasy-sea scale-panel ensemble|青绿不透明鳞片纹胸衣与高腰短裤；腰侧叠片像短鱼尾裙摆；贝壳形小发梳、腕饰和青绿鞋
火鸟羽片舞台主题装|firebird feather-panel stage ensemble|橙红不透明胸衣与高腰短裤；金橙羽片形腰侧短裙；小羽冠、金色腕饰与橙红鞋
狐耳和风主题套装|fox-ear Japanese-inspired ensemble|白红不透明交领连体成衣；腰封和两侧短裙片；宽袖短罩衫、狐耳头箍与白红鞋
独角兽幻彩主题装|iridescent-unicorn themed ensemble|珍珠白不透明连体成衣；淡粉淡蓝拼片与幻彩短罩裙；小独角头箍、腕饰和珍珠白鞋
南瓜节庆主题成衣|pumpkin-festival intimate-apparel set|橙色不透明收腰胸衣与黑色高腰短裤；橙黑波浪短裙片；南瓜小帽、条纹长袜和黑色鞋
圣诞礼结主题成衣|holiday-velvet bow ensemble|深红不透明丝绒连体成衣与短罩裙；白色绒边和正面大礼结；软帽、白手套与红色短靴
新年盘扣主题套装|new-year knot-button ensemble|红金不透明立领连体成衣与金边腰侧短裙片；正面小盘扣和独立短披肩；结形发饰、腕饰与红鞋
''')
block(GROUPS[2],'''
空乘领巾主题成衣|flight-attendant scarf ensemble|海军蓝不透明连体成衣与短铅笔裙片；短翻领外套、斜系领巾和小帽；肤色不透明连裤袜与黑鞋
女警制服主题套装|police-inspired intimate-apparel set|深蓝不透明胸衣与高腰短裤；短肩章外套和无字银色胸牌；小檐帽、黑色长袜与短靴，不带执法器具
护士简洁主题连体装|nurse-inspired bodysuit ensemble|白色不透明立领连体成衣与小围裙片；红色细滚边和无标志软帽；白色短手套、长袜与白鞋，不带医疗器具
秘书条纹主题成衣|secretary-pinstripe ensemble|灰色细条纹胸衣与高腰短裤；白色不透明前胸衬片、假领与细领带；眼镜配件、小裙片和黑鞋
酒店礼宾主题套装|hotel-concierge themed ensemble|酒红不透明连体成衣与金边短马甲；对称装饰扣和小礼宾帽；白色袖口、短手套与酒红鞋
复古飞行主题成衣|retro-aviator themed ensemble|棕色不透明仿皮胸衣与高腰短裤；短飞行夹克和米色围巾；飞行帽顶放护目镜，配棕色短靴
方格赛车主题套装|checker-racing themed ensemble|黑白不透明拉链连体成衣；腰侧方格拼片和短外套；黑白腕饰、短袜与赛车风短靴
海盗三角帽主题成衣|pirate-tricorn intimate-apparel set|酒红不透明胸衣与黑色高腰短裤；不对称腰侧裙片和短外套；三角帽、长袜与黑靴，不带武器
西部牛仔流苏主题装|western-denim fringe ensemble|靛蓝不透明牛仔胸衣与高腰短裤；棕色短马甲与腰侧软流苏；牛仔帽、腕饰与棕色靴
摇滚拉链主题成衣|rock-zipper intimate-apparel set|黑色不透明仿皮胸衣与高腰短裤；短机车夹克、银色拉链与平头饰钉；小腕饰、长袜与黑色靴
赛博灯带主题连体装|cyber-light-strip bodysuit ensemble|深灰不透明高领连体成衣；蓝紫细灯带沿裁片走向分区；小肩部装饰片、腕饰与灰黑短靴
未来银箔主题成衣|futurist-silver lame ensemble|银色不透明金属织物胸衣与高腰短裤；几何腰侧小裙片；银色长手套、头箍与银黑鞋
透明罩衣叠穿主题装|clear-overcoat layered ensemble|黑色不透明高领连体成衣；外穿透明PVC短罩衣，拉链和衣缘可辨；黑色高腰短裙片、腕饰与短靴
丝绒拼缝主题套装|velvet-seam intimate-apparel set|墨绿不透明丝绒长线胸衣与高腰短裤；金色明线沿裁片边缘走向；短披肩、长手套和绿色鞋
绸带礼盒主题成衣|ribbon-gift themed ensemble|浅粉不透明连体成衣与短罩裙；宽缎带作为衣身缝制装饰，胸前和腰侧有大蝴蝶结；袖口小结与浅粉鞋
运动弹力主题套装|athletic-stretch themed ensemble|黑橙不透明弹力拉链连体成衣与高腰短裤层；运动裁片、侧条纹和短夹克；腕带、短袜与橙黑鞋
''')

THEME_ALIASES={
    'moonlit-witch intimate-apparel ensemble':['魔女','万圣节','witch'],
    'bat-wing themed bodysuit ensemble':['蝙蝠','万圣节'],
    'little-devil horn-and-tail ensemble':['恶魔','万圣节','devil'],
    'pumpkin-festival intimate-apparel set':['万圣节','万圣节南瓜','Halloween'],
    'holiday-velvet bow ensemble':['圣诞','Christmas'],
    'bridal-veil slip ensemble':['新娘','婚纱','bridal'],
    'flight-attendant scarf ensemble':['空姐','空乘','stewardess'],
    'police-inspired intimate-apparel set':['女警','警服'],
    'secretary-pinstripe ensemble':['秘书','办公室','OL'],
    'clear-overcoat layered ensemble':['PVC罩衣','透明外套'],
    'cyber-light-strip bodysuit ensemble':['赛博','灯带','未来都市'],
}
THEME_STYLES={
    'rococo-ribbon bustier ensemble':['retro'],
    'baroque-gold brocade bustier ensemble':['retro'],
    'Victorian-inspired high-collar ensemble':['retro','gothic'],
    'Edwardian-inspired puff-sleeve ensemble':['retro'],
    'art-deco geometric intimate-apparel set':['retro'],
    'black-white opera-tail ensemble':['retro'],
    'feather-trim cabaret bustier ensemble':['retro'],
    'jazz-fringe slip-dress ensemble':['retro'],
    'old-screen satin-robe ensemble':['retro'],
    'black-rose gothic bustier ensemble':['gothic'],
    'court-collar and cuff ensemble':['retro'],
    'new-year knot-button ensemble':['chinese'],
    'retro-aviator themed ensemble':['retro'],
    'rock-zipper intimate-apparel set':['punk'],
    'cyber-light-strip bodysuit ensemble':['cyberpunk'],
}
for entry in CATALOG:
    if entry.get('intimate_theme_reference'):
        entry['aliases']+=THEME_ALIASES.get(entry['en'],[])
        entry['styles']=THEME_STYLES.get(entry['en'],[])
