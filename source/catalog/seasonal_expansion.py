"""Edition 17: curated original everyday ensembles for all four seasons."""
from catalog_content import CATALOG, category, add

SEASONS=[('spring','春','spring_outfits','SV'),('summer','夏','summer_outfits','SM'),('autumn','秋','autumn_outfits','AU'),('winter','冬','winter_outfits','WI')]
SEASONAL_CATEGORIES=[s[2] for s in SEASONS]
for key,cn,cat,prefix in SEASONS:
    category(cat,cn+'季日常穿搭',cn+'季原创整套搭配，按通勤城市、休闲校园、运动出游、裙装叠穿比较；记录衣物层次、材质、鞋履与包袋。季节是创作主题，实际可按地域和气候增减层次。',['R05','R06'])

def block(season,topic,text):
    cn,cat=next((s[1],s[2]) for s in SEASONS if s[0]==season)
    lines=[l.strip().split('|') for l in text.strip().splitlines()]
    assert len(lines)==16,(season,topic,len(lines))
    for name,en,recipe,styles in lines:
        title=name if name.startswith(cn+'季') else cn+'季'+name
        english=en if en.startswith(season+'-') or en.startswith(season+' ') else season+' '+en
        add(cat,cn+'季·'+topic,f'{title}|{english}|{recipe}。成年女性日常整套造型，衣物、鞋履与包袋共同构成参考。')
        e=CATALOG[-1]
        e.update(season=season,season_name=cn+'季',seasonal_reference=True,age_context='成年女性日常服装参考',outfit_context=topic,outfit_components=recipe.split('；'),styles=styles.split(',') if styles else [])
        if name=='一字肩棉裙日常':e['shoulder_type']='bardot'
        if name=='细吊带裙棉T叠穿':e['shoulder_type']='thin_strap'
        if name=='挂脖裙轻外搭装':e['shoulder_type']='halter'
        e['aliases']=['日常穿搭','日常服装','四季穿搭',cn+'季穿搭',cn+'装',season,'everyday outfit','seasonal outfit',topic]

block('spring','通勤与城市','''
短风衣直裤通勤|short-trench straight-trouser commute|白棉衬衫与米色短风衣；海军蓝直筒西裤；棕色乐福鞋；结构手提包|minimal
长风衣九分裤通勤|long-trench ankle-trouser commute|细条纹衬衫与敞襟长风衣；九分锥形裤；低跟系带鞋；窄肩托特包|british
无领西装阔裤通勤|collarless-blazer wide-trouser commute|圆领薄针织与无领短西装；垂坠阔腿裤；方头平底鞋；矩形肩包|minimal
双排扣西装烟管裤|double-breasted cigarette-trouser outfit|平领衬衣与轻薄双排扣西装；烟管裤；细带低跟鞋；小手提公文包|minimal
衬衫针织背心通勤|shirt knit-vest commute|白色长袖衬衫叠V领针织背心；褶裥西裤；乐福鞋；软皮托特包|preppy
开衫衬衫直裙通勤|cardigan shirt straight-skirt commute|浅蓝衬衫与及腰细针开衫；膝下直筒裙；低跟鞋；小肩包|retro
轻西装衬衫裙通勤|light-blazer shirtdress commute|系腰棉衬衫长裙外搭轻西装；裙摆及小腿；便鞋；简洁手提包|minimal
长马甲锥裤通勤|long-waistcoat tapered-trouser commute|立领衬衫外搭过臀长马甲；锥形裤；尖头低跟鞋；硬壳方包|minimal
短夹克小直裙通勤|short-jacket slim-midi commute|薄圆领针织与短箱形夹克；膝下小直裙；玛丽珍鞋；链带小包|french_girly
套头针织阔裤通勤|light-pullover wide-trouser commute|浅燕麦色细针套头衫；深灰垂坠阔腿裤；软底乐福鞋；帆布皮边托特包|minimal
卷袖衬衫腰带裤|rolled-shirt belted-trouser outfit|宽松棉衬衫卷至前臂；高腰直筒裤配细腰带；系带便鞋；腋下包|minimal
轻猎装城市穿搭|light-safari urban outfit|薄棉工装衬衣外搭四袋猎装；直筒卡其裤；棕色踝鞋；邮差包|british
立领夹克褶裤通勤|stand-collar jacket pleated trousers|白色薄针织与轻立领夹克；单褶九分裤；德比鞋；方形背包|minimal
格纹西装半裙通勤|checked-blazer skirt commute|奶油色衬衫与小格纹轻西装；纯色中长A裙；便鞋；简洁肩包|british
衬衣肩搭针织城市装|shirt shoulder-knit city outfit|浅色棉衬衣与肩搭薄针织衫；高腰直腿牛仔裤；芭蕾平底鞋；小托特包|retro
轻针织套装城市装|fine-knit coordinated city outfit|细针开衫内搭同色圆领背心；同面料直筒长裙；低跟鞋；软手提包|minimal
''')
block('spring','休闲与校园','''
牛仔夹克白T休闲|denim-jacket white-tee casual|白棉T恤与短牛仔夹克；直筒牛仔裤；白色运动鞋；帆布托特包|streetwear
棒球夹克卫裤休闲|varsity-jacket jogger casual|圆领T恤与无标志棒球夹克；束脚卫裤；运动鞋；小斜挎包|streetwear
连帽卫衣工装裤|hoodie cargo-trouser casual|薄棉连帽卫衣；宽工装裤；帆布鞋；双肩背包|streetwear
圆领卫衣直筒裤|crew-sweat straight-trouser casual|纯色圆领卫衣露短衬衣下摆；直筒棉裤；运动鞋；斜挎邮差包|streetwear
条纹T开衫牛仔裤|striped-tee cardigan jeans|横条纹长袖T恤与短开衫；浅蓝牛仔裤；帆布鞋；帆布肩袋|preppy
Polo针织学院裤装|knit-polo campus trousers|薄长袖针织Polo；宽松褶裤；乐福鞋与短袜；学院双肩包|preppy
衬衣马甲百褶裙|shirt vest pleated-skirt casual|白衬衣叠短针织马甲；膝下百褶裙；便鞋与短袜；书本托特包|preppy
短开衫背带裤|short-cardigan dungarees|棉长袖T恤与短开衫；宽腿牛仔背带裤；帆布鞋；小布包|streetwear
格衬T恤休闲|check-overshirt tee casual|敞襟格纹薄衬衫叠白T恤；直筒深色牛仔裤；便鞋；软背包|grunge
轻飞行夹克宽裤|light-bomber wide-pants casual|薄圆领T恤与轻飞行夹克；宽腿棉裤；运动鞋；饺子斜挎包|streetwear
拉链卫衣学院裙|zip-hoodie campus-skirt outfit|浅色棉内搭与拉链薄卫衣；及膝A字裙；运动鞋与短袜；双肩包|preppy
亨利领牛仔休闲|henley denim casual|长袖棉亨利领上衣；九分直腿牛仔裤；低帮帆布鞋；长带邮差包|minimal
薄开衫阔裤书店装|light-cardigan bookshop outfit|圆领棉衫与长薄开衫；软垂阔腿裤；平底鞋；装书帆布包|mori
轻工装夹克休闲|light-chore jacket casual|条纹内搭与浅色棉工装夹克；直筒工装裤；系带鞋；双肩包|streetwear
针织领衫背带裙|collared-knit pinafore casual|薄领口针织上衣；及膝宽肩带背带裙；玛丽珍鞋与短袜；小手提包|girly
衬衣宽袖卫衣叠穿|shirt wide-sweatshirt layers|立领衬衣叠宽袖短卫衣；深色直筒长裤；运动鞋；校园托特包|preppy
''')
block('spring','运动与出游','''
薄风衣步行装|light-windbreaker walking outfit|圆领T恤与薄连帽风衣；直筒活动长裤；步行鞋；斜挎小包|techwear
拼色运动夹克装|color-panel track-jacket outfit|无标志拼色运动夹克与棉内搭；运动长裤；运动鞋；轻量双肩包|streetwear
卫衣骑行休闲装|hoodie cycling-casual outfit|薄拉链卫衣与圆领内搭；束口休闲裤；运动鞋；贴身斜挎包|streetwear
郊游工装马甲装|utility-vest picnic outfit|长袖棉衫叠轻工装马甲；宽直工装裤；系带鞋；小双肩包|techwear
雨天短壳外套装|rain-day short-shell outfit|立领内搭与短连帽雨壳；收脚长裤；短雨靴；带拉链斜挎包|techwear
长雨衣直裤装|long-raincoat straight-pants outfit|棉衬衣外搭膝长雨衣；窄直长裤；中筒雨靴；手提防雨袋|techwear
郊游针织背心装|knit-vest spring-trip outfit|浅色棉衬衣叠针织背心；直筒牛仔裤；运动鞋；帆布背包|preppy
摄影口袋外套装|pocket-jacket photography outfit|纯色T恤与多口袋轻外套；褶裥长裤；步行鞋；相机肩包|techwear
城市散步衬衫装|overshirt city-walk outfit|棉T恤与敞襟长衬衫；九分宽裤；帆布鞋；小斜挎包|minimal
公园轻抓绒装|light-fleece park outfit|圆领内搭外罩薄抓绒；直筒活动长裤；系带运动鞋；轻背包|techwear
露营棉猎装搭配|cotton-safari camp casual|立领衬衫与棉猎装外套；宽工装裤；踝帮系带鞋；帆布背包|british
春季慢跑套装|light-jogging ensemble|长袖运动衫与敞襟薄运动外层；束脚运动裤；跑步鞋；小腰包|streetwear
旅行连体裤外套装|travel-jumpsuit jacket outfit|长袖棉连体裤与短夹克；裤脚九分；运动鞋；肩挎旅行包|minimal
郊游半拉链卫衣装|half-zip picnic outfit|半拉链薄卫衣；浅色直筒工裤；运动鞋；卷口小背包|techwear
海边薄衬衣长裤装|coastal-light-shirt trousers|条纹棉内搭与薄长衬衣；宽腿棉长裤；帆布便鞋；编织托特包|boho
雨后公园软壳装|park-softshell casual|薄针织内搭与轻软壳外套；直筒长裤；系带活动鞋；小双肩包|techwear
''')
block('spring','裙装与轻叠穿','''
花裙牛仔外套装|floral-dress denim layers|小碎花膝下茶裙与短牛仔外套；平底鞋；编织手提包|cottagecore
衬衫裙细腰带装|belted-cotton shirtdress|长袖棉衬衫裙配细腰带；裙摆及小腿；乐福鞋；小托特包|minimal
开衫点纹连裙装|cardigan dotted-dress outfit|袖口及腕的薄开衫与细点纹连衣裙；膝下裙摆；玛丽珍鞋；小肩包|retro
针织上衣伞裙装|light-knit circle-skirt outfit|细针长袖上衣；高腰膝下伞裙；平底便鞋；小桶包|girly
亚麻混纺长裙装|linen-blend long-skirt outfit|宽袖棉衬衣与薄短马甲；亚麻混纺长裙；系带平底鞋；帆布肩袋|mori
短夹克衬衫裙装|cropped-jacket shirtdress|及腰箱形夹克叠浅色衬衫裙；裙摆及膝下；踝鞋；方肩包|minimal
裙裤针织春日装|culotte light-knit outfit|薄V领针织内搭棉圆领衫；宽裙裤；便鞋；大托特包|minimal
领结衬衣A裙装|bow-shirt A-skirt outfit|小领结棉衬衣与短开衫；膝长A字裙；玛丽珍鞋；细带手提包|girly
连裙针织背心装|dress knit-vest layers|棉长袖衬衫连裙外叠针织背心；裙摆及小腿；便鞋；书本托特包|preppy
卷袖罩衫长裙装|rolled-overshirt maxi outfit|棉圆领衫外搭卷袖薄罩衫；直筒长裙；帆布鞋；软肩包|mori
小方领开衫裙装|square-neck cardigan skirt|不透小方领长袖上衣与短开衫；细褶中长裙；低跟鞋；小手提包|french_girly
轻围裹连裙装|light-wrap everyday dress|棉质围裹式长袖连裙配内层；裙摆膝下；芭蕾鞋；小肩包|retro
短背心宽袖裙装|short-vest wide-sleeve dress|宽袖长连裙外搭短棉马甲；裙摆及踝上；系带便鞋；编织肩袋|boho
格纹半裙开衫装|checked-skirt cardigan outfit|圆领棉内搭与细针开衫；小格纹膝下半裙；乐福鞋；手提布包|preppy
卫衣直筒长裙装|sweatshirt straight-maxi outfit|轻棉圆领卫衣；直筒针织长裙；运动鞋；饺子包|streetwear
薄长外套连裙装|light-long-coat dress outfit|简洁圆领长袖连裙外罩轻长外套；及小腿裙摆；低跟踝鞋；矩形肩包|minimal
''')

block('summer','通勤与城市','''
短袖衬衫阔裤通勤|short-shirt wide-pants commute|挺括短袖棉衬衫；轻薄阔腿西裤；乐福鞋；结构托特包|minimal
亚麻西装直裤通勤|linen-blazer straight-trouser commute|圆领棉内搭与轻亚麻西装；同色直筒长裤；便鞋；小公文包|minimal
无袖衬衣伞裙通勤|sleeveless-shirt circle-skirt commute|不透无袖棉衬衣；膝下伞裙；低跟鞋；细带肩包|retro
薄开衫直裙通勤|summer-cardigan straight-skirt commute|短袖圆领上衣与细针薄开衫；膝下直裙；方头平底鞋；手提包|minimal
Polo衫褶裤城市装|polo pleated-trouser city outfit|短袖针织Polo；轻薄单褶长裤；软乐福鞋；大托特包|preppy
五分袖衬衫裙通勤|elbow-sleeve shirtdress commute|系腰五分袖棉衬衫裙；裙摆及小腿；低跟鞋；小方包|minimal
薄马甲宽裤通勤|light-waistcoat wide-trouser commute|短袖棉衫外叠薄长马甲；宽腿长裤；乐福鞋；窄手提包|minimal
条纹衬衫九分裤|striped-shirt ankle-trousers|细条纹卷袖衬衣；九分锥形裤；低跟便鞋；软肩包|british
短西装背心连裙装|short-blazer sleeveless-dress commute|不透宽肩带膝下连裙与薄短西装；便鞋；结构手提包|minimal
棉麻上衣直裙装|cotton-linen top straight-skirt|棉麻圆领短袖上衣；侧摆小开衩膝下直裙；平底鞋；小托特包|minimal
短袖西装短裤通勤|short-sleeve blazer tailored-shorts|白T叠短袖薄西装；及膝西装短裤；乐福鞋；矩形肩包|minimal
系腰衬衣阔裤装|waist-tie shirt wide-trousers|短袖系腰棉衬衣；轻垂阔腿裤；低跟鞋；手提软包|retro
不透连体裤通勤|opaque-summer jumpsuit commute|有领短袖棉质连体裤配细腰带；直筒裤腿；平底便鞋；小公文包|minimal
小方领长裙城市装|square-neck summer-city dress|不透小方领短袖连裙；及小腿平整裙摆；系带低跟鞋；小腋下包|french_girly
冷气房针织裤装|indoor-cardigan summer trousers|短袖棉衫外搭可脱薄针织开衫；直筒棉长裤；便鞋；大托特包|minimal
棉麻套装城市装|cotton-linen summer coordinates|短袖箱形棉麻上衣；同料宽腿长裤；平底凉鞋；简洁肩包|minimal
''')
block('summer','休闲与校园','''
白T牛仔短裤休闲|white-tee denim-shorts casual|宽松白棉T恤；中长度牛仔短裤；帆布鞋与短袜；小斜挎包|streetwear
条纹T直筒牛仔装|striped-tee straight-jeans casual|短袖横条纹T恤；直筒浅蓝牛仔裤；运动鞋；帆布托特包|preppy
短袖格衬宽裤装|short-check shirt loose-pants|短袖敞襟格衬与棉背心；宽棉长裤；帆布鞋；小背包|grunge
宽T百慕大短裤|loose-tee bermuda casual|无标志宽T恤；及膝百慕大短裤；运动鞋；饺子斜挎包|streetwear
Polo百褶裙休闲|polo pleated-skirt casual|短袖Polo；及膝百褶裙；帆布鞋与短袜；书本托特包|preppy
棉背心长衬衫装|cotton-tank long-overshirt|不透宽肩带棉背心与敞襟薄长衬衫；直筒长裤；便鞋；软肩袋|minimal
短袖衬衫背带裤|short-shirt dungarees casual|短袖棉衬衣；宽腿牛仔背带裤；帆布鞋；大背包|preppy
运动T束口裤装|sport-tee drawcord-pants casual|普通短袖运动T恤；轻薄束口长裤；运动鞋；小斜挎包|streetwear
针织短袖九分裤|short-knit ankle-pants casual|细针短袖圆领衫；宽九分棉裤；平底鞋；小托特包|minimal
泡袖衬衣牛仔装|puff-shirt denim casual|不透小泡袖棉衬衣；直筒牛仔裤；玛丽珍鞋；小肩包|girly
宽短袖马甲裤装|wide-tee vest trousers|宽短袖T叠轻短工装马甲；直筒工装长裤；运动鞋；双肩包|streetwear
领口滚边休闲装|piped-collar casual coordinates|无标志滚边短袖衫；宽松膝长短裤；便鞋；轻托特包|preppy
短袖亨利领休闲|short-henley casual outfit|短袖棉亨利领上衣；九分直筒裤；帆布鞋；邮差包|minimal
轻拉链罩衫裤装|light-zip overshirt casual|圆领棉T与轻薄拉链罩衫；宽工装裤；运动鞋；小背包|techwear
短开衫背心宽裤|short-cardigan tank wide-pants|不透宽肩带背心外搭短袖薄开衫；垂坠宽裤；平底凉鞋；布肩袋|minimal
夏季学院裙裤装|summer-campus culotte outfit|短袖棉衬衫配小领带；及膝宽裙裤；乐福鞋与短袜；大学书包|preppy
''')
block('summer','运动与出游','''
夏季步行短袖装|summer-walking short-sleeve outfit|宽松短袖活动衫；轻薄直筒裤；步行运动鞋；小腰包|streetwear
跑步T运动短裤|running-tee shorts outfit|普通运动短袖T恤；中长运动短裤；跑步鞋与短袜；轻腰包|streetwear
骑行休闲衬衫装|cycling-casual summer shirt|短袖棉衬衣与轻背心内搭；束口九分裤；运动鞋；贴身斜挎包|minimal
海边亚麻宽裤装|seaside-linen wide-trouser outfit|宽肩带不透内搭与亚麻长袖衬衫；棉麻宽裤；平底凉鞋；编织托特包|boho
城市旅游短裤装|city-travel shorts outfit|短袖宽T与敞襟轻衬衣；及膝棉短裤；运动鞋；拉链小背包|streetwear
园游罩衫半裙装|garden-trip overshirt skirt|棉短袖内搭与薄罩衫；轻棉中长半裙；便鞋；编织手提袋|cottagecore
口袋衬衫徒步休闲|pocket-shirt trail casual|短袖双袋活动衬衣；轻直筒工装裤；系带活动鞋；小双肩包|techwear
夏雨短壳长裤装|summer-rain shell trousers|短袖T恤与薄连帽雨壳；九分直裤；短雨靴；拉链肩袋|techwear
海港条纹短裤装|harbor-striped shorts outfit|短袖条纹上衣；及膝宽棉短裤；帆布便鞋；大布托特包|preppy
度假棉连体短裤|holiday-cotton short-jumpsuit|普通有领短袖棉连体短裤；裤口及大腿中部；平底凉鞋；编织桶包|cottagecore
野餐宽衬衣裤装|picnic-wide-shirt trousers|卷袖宽棉衬衣；高腰棉麻直裤；帆布鞋；装野餐物的帆布包|mori
活动马甲短裤装|utility-vest summer shorts|短袖T叠薄多袋马甲；及膝工装短裤；运动鞋；卷口背包|techwear
薄运动外套网球休闲|light-track tennis-casual outfit|普通短袖运动上衣与薄运动外套；及膝运动褶裙；运动鞋；小运动包|streetwear
海风薄针织长裙装|sea-breeze light-knit maxi|不透短袖内搭外罩细针薄开衫；长棉半裙；平底凉鞋；编织肩包|boho
旅行T棉麻裙裤|travel-tee linen culottes|短袖棉T恤；轻棉麻宽裙裤；便鞋；小双肩包|minimal
湖畔薄连帽罩衫|lakeside-light hooded outfit|不透圆领内搭与薄连帽罩衫；宽直活动长裤；系带鞋；轻斜挎包|techwear
''')
block('summer','裙装与清凉层次','''
棉碎花茶裙日常|cotton-floral tea-dress outfit|不透短袖小碎花茶裙；膝下收腰裙摆；平底凉鞋；编织手提包|cottagecore
宽肩带连裙罩衫|wide-strap dress overshirt|不透宽肩带长连裙与卷袖薄棉罩衫；平底鞋；小肩包|minimal
细吊带裙棉T叠穿|thin-strap dress tee layers|不透细吊带及小腿连裙内搭短袖棉T；帆布鞋；小托特包|girly
一字肩棉裙日常|off-shoulder cotton casual dress|不透一字肩短袖棉连裙；膝下松裙摆；平底凉鞋；小桶包|boho
围裹半裙短袖装|wrap-midi short-sleeve outfit|不透棉短袖圆领上衣；重叠前片中长围裹裙；便鞋；软肩包|minimal
亚麻背带裙棉衫|linen-pinafore cotton-tee outfit|短袖棉衫；亚麻宽肩带中长背带裙；平底凉鞋；帆布手提袋|mori
泡袖方领连裙装|puff-square-neck summer dress|不透小方领泡袖棉连裙；及小腿A字裙摆；玛丽珍鞋；小方包|girly
短袖针织直裙装|short-knit straight-skirt outfit|细针短袖上衣；不透膝下直筒裙；方头平底鞋；小腋下包|minimal
条纹衬衣棉长裙|striped-shirt cotton-maxi outfit|卷袖细条纹衬衫；纯色棉长裙；便鞋；编织肩袋|retro
抽褶领长裙装|gathered-neck summer maxi|不透宽抽褶领短袖长连裙；腰侧细系带；平底凉鞋；软托特包|cottagecore
短袖衬衣褶裙装|short-shirt fine-pleat skirt|简洁短袖衬衣；细褶膝下半裙；低跟鞋；手提小包|preppy
棉T牛仔中长裙|cotton-tee denim-midi outfit|棉短袖T恤；前扣中长牛仔裙；帆布鞋；帆布肩袋|streetwear
挂脖裙轻外搭装|halter-dress light-layer outfit|不透挂脖膝下连裙外搭敞襟轻衬衣；平底凉鞋；编织小包|boho
短袖围裹连裙装|short-sleeve wrap-dress casual|不透短袖围裹连裙配稳固内片；小腿长度裙摆；便鞋；小肩包|retro
薄针织背心半裙|fine-knit vest skirt layers|短袖棉T外叠薄针织背心；棉质膝下A裙；平底鞋；书本托特包|preppy
五分袖口袋连裙|elbow-sleeve pocket-dress outfit|不透五分袖宽松口袋连裙；小腿长度裙摆；帆布鞋；大布手提袋|minimal
''')

block('autumn','通勤与城市','''
羊毛西装直裤通勤|wool-blazer straight-pants commute|薄高领针织与轻羊毛西装；直筒西裤；乐福鞋；硬边托特包|minimal
中长风衣褶裤通勤|mid-trench pleated-trouser commute|长袖棉衬衣与中长风衣；单褶西裤；德比鞋；方形公文包|british
针织开衫西装裙|knit-cardigan tailored-skirt outfit|圆领衬衣与中厚针织开衫；膝下西装直裙与不透袜裤；低跟踝靴；肩包|retro
粗花呢短外套裙|tweed-cropped jacket midi|薄针织与粗花呢短外套；膝下A字裙与不透袜裤；便鞋；小手提包|british
高领针织阔裤通勤|turtleneck wide-trouser commute|轻羊毛高领针织；厚垂坠阔腿裤；低跟鞋；大软托特包|minimal
衬衣绒马甲通勤|shirt cord-vest commute|白棉衬衣与灯芯绒短马甲；直筒西裤；乐福鞋；小公文包|retro
短大衣烟管裤装|short-coat cigarette-trousers|细针高领衫与短羊毛大衣；烟管裤；低跟踝靴；小方包|minimal
长马甲针织直裙|long-vest knit-midi commute|高领针织内搭与长羊毛马甲；中长直裙与不透袜裤；踝靴；肩包|minimal
皮夹克棉衬衣通勤|leather-jacket shirt commute|棉衬衣与简洁短皮夹克；宽西装长裤；便鞋；结构手提包|minimal
格纹长外套通勤|check-long-coat commute|薄圆领针织与轻格纹长外套；直筒西裤；低跟踝靴；长带肩包|british
西装针织连裙装|blazer knit-dress commute|高领膝下针织连裙与轻西装；不透袜裤；低跟鞋；硬边手提包|minimal
双层衬衣褶裙通勤|layered-shirt pleated-skirt commute|棉衬衣叠短细针毛衣；中长百褶裙与不透袜裤；乐福鞋；托特包|preppy
短绗缝夹克直裤|short-quilted jacket trousers|薄针织与短格状绗缝外套；直筒西裤；踝鞋；小肩包|british
绒面夹克城市装|suede-jacket urban outfit|薄亨利领内搭与绒面短夹克；宽直长裤；低跟踝靴；软桶包|retro
针织套装秋日通勤|autumn-knit coordinates commute|中厚针织开衫与同色内搭；同料直筒长裙；不透袜裤与便鞋；肩包|minimal
敞襟大衣背心裤装|open-coat vest trousers|棉衬衣叠薄针织背心外罩轻大衣；高腰阔腿裤；乐福鞋；大托特包|preppy
''')
block('autumn','休闲与校园','''
格衬牛仔学院装|check-shirt denim-campus outfit|长袖格衬叠圆领棉T；直腿牛仔裤；帆布鞋；大学双肩包|preppy
针织毛衣灯芯绒裤|sweater corduroy casual|中厚圆领针织毛衣；灯芯绒直裤；便鞋；软邮差包|retro
连帽卫衣牛仔夹克|hoodie denim-jacket casual|薄连帽卫衣与宽牛仔夹克；深色直筒牛仔裤；运动鞋；背包|streetwear
棒球夹克百褶裙|varsity-jacket pleated-skirt casual|棉衬衣与无标志棒球夹克；及膝百褶裙和不透袜裤；运动鞋；斜挎包|preppy
衬衣针织背心学院|shirt knit-vest campus casual|长袖棉衬衣叠厚针织背心；宽褶裤；乐福鞋与厚短袜；书包|preppy
抓绒夹克工装裤|fleece-jacket cargo trousers|圆领棉内搭与抓绒拉链夹克；直筒工装裤；系带鞋；双肩包|techwear
开衫深牛仔休闲|cardigan dark-jeans casual|纯色长袖衫与中厚针织开衫；深蓝直筒牛仔裤；帆布鞋；小托特包|minimal
拉链卫衣运动裤|zip-hoodie track-trouser casual|棉T与拉链卫衣；宽运动长裤；运动鞋；饺子包|streetwear
灯芯绒衬衫宽裤|cord-overshirt wide-trousers|圆领内搭与敞襟灯芯绒衬衣；宽棉长裤；便鞋；软背包|retro
半拉链针织学院装|half-zip knit-campus outfit|棉内搭与半拉链领针织毛衣；九分宽西裤；乐福鞋与短袜；书本包|preppy
轻皮夹克休闲装|light-leather jacket casual|长袖棉上衣与短皮夹克；直筒牛仔裤；系带踝靴；斜挎肩包|streetwear
针织衬衣背带裤|knit-shirt dungarees casual|长袖薄针织上衣；灯芯绒宽背带裤；便鞋；帆布托特包|mori
厚衬衫夹克休闲|shacket everyday casual|圆领棉衫外搭厚格纹衬衫夹克；宽直长裤；运动鞋；小背包|grunge
羊羔绒马甲卫衣|fleece-vest hoodie casual|薄棉卫衣与羊羔绒马甲；直筒活动长裤；运动鞋；轻斜挎包|streetwear
高领短卫衣裙装|turtleneck sweatshirt skirt|薄高领内搭叠短圆领卫衣；膝下A裙与不透袜裤；运动鞋；大学托特包|preppy
针织Polo休闲裤|autumn-knit polo trousers|长袖中厚针织Polo；宽直灯芯绒裤；软底便鞋；邮差包|retro
''')
block('autumn','运动与出游','''
抓绒软壳出游装|fleece-softshell trip outfit|薄活动衫与抓绒内层外搭轻软壳；直筒活动裤；系带鞋；背包|techwear
半拉链卫衣徒步休闲|half-zip trail casual|半拉链卫衣与薄工装外层；束口活动长裤；步行鞋；卷口背包|techwear
摄影工装马甲秋装|autumn-photography vest outfit|棉长袖衬衣叠多口袋马甲；灯芯绒直裤；系带踝鞋；相机肩包|techwear
雨天长壳直裤装|autumn-rain long-shell outfit|薄针织与及膝连帽雨壳；窄直长裤；中筒雨靴；拉链斜挎包|techwear
郊游绗缝马甲装|quilted-vest picnic outfit|针织毛衣与绗缝马甲；直筒工裤；踝帮系带鞋；小背包|british
公园针织夹克装|park-knit jacket outfit|长袖棉衫与厚拉链针织夹克；活动长裤；步行鞋；小腰包|streetwear
露营灯芯绒外套|corduroy-camp casual|薄高领上衣与灯芯绒工装外套；宽棉工裤；系带鞋；帆布背包|retro
秋季运动套装|autumn-track ensemble|拉链运动夹克与长袖活动内搭；同款运动长裤；运动鞋；运动肩包|streetwear
旅行轻棉服裤装|light-padded travel outfit|棉衬衣与轻薄棉服；直筒长裤；步行鞋；小旅行包|minimal
观景风衣牛仔装|scenic-trench denim outfit|针织内搭与中长风衣；直筒牛仔裤；踝靴；斜挎相机包|british
林间针织工裤装|woodland-knit cargo outfit|长袖棉内搭与高领针织外层；宽工装裤；系带踝鞋；帆布双肩包|mori
单车夹克束裤装|bicycle-jacket cuffed-pants|棉卫衣与短活动夹克；收脚长裤；运动鞋；贴身腰包|streetwear
落叶公园长外套|leaf-park long-jacket outfit|圆领棉衫外罩轻长工装外套；直筒长裤；运动鞋；软背包|techwear
湖边薄羽绒马甲|lakeside-light down-vest|薄针织与轻羽绒马甲；活动直裤；步行鞋；小背包|techwear
雨后工装罩裙装|rain-after utility-overdress|长袖棉衫叠工装背带中长裙外搭短壳；不透袜裤与短雨靴；斜挎包|techwear
山城夹克旅行装|hill-city jacket-travel outfit|半拉链针织内搭与轻棉夹克；宽活动长裤；系带鞋；拉链背包|techwear
''')
block('autumn','裙装与温差叠穿','''
厚开衫碎花长裙|thick-cardigan floral-maxi outfit|长袖碎花连裙与厚针织开衫；不透袜裤；系带踝靴；编织肩袋|cottagecore
高领衫背带裙装|turtleneck pinafore layers|薄高领针织内搭；灯芯绒膝下背带裙；不透袜裤与便鞋；软手提包|mori
针织毛衣百褶裙|sweater pleated-midi outfit|中厚圆领毛衣；膝下百褶裙；不透袜裤与低跟踝靴；小肩包|preppy
风衣中长衬衫裙|trench-midi shirtdress layers|长袖棉衬衫连裙外罩风衣；不透袜裤；乐福鞋；大托特包|british
短皮夹克针织裙|leather-jacket knit-skirt outfit|薄高领上衣与短皮夹克；直筒针织长裙；不透袜裤与踝靴；小斜挎包|streetwear
绒面A裙衬衣装|suede A-skirt shirt outfit|棉衬衣与细针短开衫；膝下绒面A裙；不透袜裤与便鞋；软肩包|retro
粗花呢裙套装|tweed-midi everyday coordinates|薄圆领内搭与粗花呢短外套；同料膝下A裙；不透袜裤与低跟鞋；小手提包|french_girly
格纹围裹裙装|checked-wrap autumn skirt|高领针织衫；重叠格纹膝下围裹裙；不透袜裤与踝靴；小桶包|british
羊毛马甲衬衫裙|wool-vest shirtdress outfit|棉长袖衬衫裙叠短羊毛马甲；不透袜裤；乐福鞋；书本包|preppy
短绗缝外套长裙|short-quilted jacket maxi|长袖针织内搭与短绗缝外套；厚棉长裙；不透袜裤与系带鞋；帆布托特包|mori
牛仔长裙开衫装|denim-maxi cardigan outfit|薄高领上衣与长针织开衫；直筒牛仔长裙；不透袜裤与踝鞋；大肩包|retro
针织连裙衬衣叠层|knit-dress shirt layers|长袖棉衬衣内搭不透宽肩带针织长裙；不透袜裤与便鞋；小手提包|preppy
薄大衣褶裙装|light-coat pleated-skirt outfit|薄圆领针织与敞襟轻羊毛大衣；膝下褶裙；不透袜裤与低跟踝靴；肩包|minimal
短毛衣长衬衫裙|short-sweater long-shirtdress|浅色长袖衬衫裙叠及腰短毛衣；不透袜裤；便鞋；帆布托特包|preppy
织纹上衣裙裤装|textured-knit culotte outfit|中厚织纹针织上衣；羊毛混纺宽裙裤；厚短袜与系带踝鞋；小桶包|mori
连裙披肩秋日装|dress shoulder-wrap autumn outfit|不透长袖膝下连裙与厚针织肩披；不透袜裤；低跟踝靴；小软肩包|boho
''')

block('winter','通勤与城市','''
羊毛长大衣直裤|long-wool coat straight-trousers|薄高领内搭叠羊毛毛衣与及膝厚大衣；加厚直筒西裤；踝靴；围巾手套与托特包|minimal
双排扣大衣阔裤|double-coat wide-pants commute|高领针织与双排扣长大衣；厚垂坠阔腿裤；低跟靴；围巾与结构手提包|british
短羽绒西裤通勤|short-puffer tailored-trousers|高领上衣叠薄毛衣与短羽绒；厚直筒西裤；踝靴；针织帽与公文包|minimal
长羽绒针织裙通勤|long-puffer knit-midi commute|高领针织膝下连裙与长羽绒；厚不透袜裤；中筒靴；围巾手套与肩包|minimal
粗花呢大衣直裙|tweed-coat straight-skirt commute|衬衣叠细针毛衣与粗花呢大衣；膝下厚直裙；厚不透袜裤与靴；托特包|british
高领马甲长大衣|turtleneck vest long-coat layers|高领长袖内搭叠针织背心与厚长大衣；厚褶裤；踝靴；围巾与方包|preppy
绗缝长外套通勤|long-quilted coat commute|薄内搭与中厚针织叠长绗缝外套；直筒厚长裤；系带踝靴；手套与肩包|minimal
立领羊毛外套裤装|stand-collar wool-jacket trousers|高领针织与厚立领羊毛外套；加厚锥裤；低跟踝靴；围巾与小公文包|minimal
短呢外套羊毛裙|short-wool jacket wool-midi|衬衣叠薄毛衣与短呢外套；厚羊毛膝下裙；厚不透袜裤与中筒靴；手提包|retro
大衣西装叠穿通勤|overcoat-blazer winter commute|棉衬衣叠薄西装外罩厚大衣；厚直筒西裤；系带踝鞋；手套与托特包|minimal
绒里皮夹克直裤|lined-leather jacket commute|薄高领上衣与绒里皮夹克；加厚直裤；低跟踝靴；围巾与结构肩包|retro
冬季针织套装大衣|winter-knit coordinates overcoat|高领针织上衣与同料长半裙外罩厚大衣；厚不透袜裤与靴；小手提包|minimal
羊毛斗篷直裤通勤|wool-cape everyday commute|高领厚毛衣与长袖内层外罩有臂口羊毛斗篷；厚直筒裤；靴；手套与肩包|british
连帽大衣城市装|hooded-wool city outfit|高领针织与厚连帽呢大衣；加厚宽长裤；系带靴；围巾与托特包|minimal
毛领棉服西裤装|collar-padded tailored-trousers|薄内搭与毛衣外罩人工绒领棉服；厚锥形西裤；踝靴；手套与方肩包|minimal
长毛衣腰带大衣|long-knit belted-coat outfit|长高领针织与系腰厚羊毛大衣；厚直筒长裤；低跟靴；围巾与软肩包|retro
''')
block('winter','休闲与校园','''
短羽绒卫衣牛仔装|short-puffer hoodie denim|薄内搭与连帽卫衣叠短羽绒；加厚直筒牛仔裤；系带靴；针织帽与背包|streetwear
长棉服卫裤休闲|long-padded coat jogger casual|长袖内搭与棉卫衣叠长棉服；加厚束脚卫裤；运动鞋；围巾与斜挎包|streetwear
羊羔绒夹克灯芯绒|fleece-jacket corduroy casual|高领针织与厚羊羔绒夹克；加厚灯芯绒直裤；便鞋与厚袜；背包|retro
针织毛衣牛仔长裤|thick-knit jeans everyday|薄高领内搭与厚圆领毛衣外搭短呢外套；厚直筒牛仔裤；系带靴；围巾与托特包|preppy
棒球棉夹克学院装|padded-varsity campus outfit|长袖衬衣叠针织背心与棉棒球夹克；厚宽西裤；厚袜与系带鞋；书包|preppy
长羽绒连帽校园装|long-puffer hoodie campus|薄内搭与连帽卫衣外罩长羽绒；厚直裤；踝靴；针织帽手套与大学背包|streetwear
加厚格纹衬衣外套|thick-check shacket casual|高领长袖衫与中厚针织叠绒里格纹衬衣外套；厚直裤；靴；斜挎包|grunge
高领抓绒厚裤装|turtleneck-fleece thick-trousers|高领内搭与厚抓绒夹克；加厚直筒长裤；系带鞋；针织帽与小背包|techwear
绗缝马甲厚毛衣|quilted-vest thick-sweater outfit|长袖内搭与厚针织毛衣叠长绗缝马甲；厚灯芯绒裤；踝靴；手套与托特包|retro
短羊毛夹克卫裤|short-wool jacket sweatpants|薄内搭与圆领卫衣外搭短呢夹克；厚束口长裤；运动鞋；围巾与饺子包|streetwear
冬季背带裤叠穿|winter-dungarees layers|高领毛衣与厚灯芯绒背带裤外罩短棉服；系带靴；针织帽与帆布背包|mori
长开衫棉服休闲|long-cardigan padded-coat layers|薄内搭与长厚开衫外搭短棉服；厚直筒裤；踝靴；围巾与软肩包|mori
滚边呢外套学院装|piped-wool campus outfit|衬衣叠针织背心与滚边厚呢外套；膝下厚褶裙；厚不透袜裤与靴；书包|preppy
半拉链毛衣厚裤|half-zip sweater thick-pants|长袖内搭与半拉链厚毛衣外搭羽绒马甲；加厚直裤；靴；围巾与小背包|streetwear
皮夹克牛仔装|winter-lined leather denim|高领毛衣与厚绒里皮夹克；加厚直腿牛仔裤；系带靴；针织帽与肩包|streetwear
毛绒短外套学院裙|faux-fur cropped campus skirt|高领内搭与毛绒短外套；膝下厚A裙；厚不透袜裤与中筒靴；大学托特包|girly
''')
block('winter','运动与出游','''
长壳抓绒出游装|long-shell fleece trip outfit|长袖内搭与抓绒中层外罩长连帽壳；厚活动长裤；系带靴；帽手套与背包|techwear
短羽绒活动长裤|short-puffer activity-trousers|长袖内搭与针织中层外罩短羽绒；厚活动直裤；踝帮鞋；针织帽与腰包|techwear
公园棉服装|winter-park padded outfit|薄高领与厚卫衣叠连帽棉服；加厚束脚裤；系带靴；围巾手套与斜挎包|streetwear
旅行长羽绒装|travel-long puffer ensemble|高领针织与长羽绒；加厚直筒长裤；踝靴；帽围巾手套与旅行肩包|minimal
冬雨壳棉层装|winter-rain shell padded-layers|长袖内搭与薄棉中层外罩连帽雨壳；厚长裤；中筒雨靴；手套与拉链背包|techwear
雪景绗缝外套装|snow-scene quilted-coat outfit|高领针织与厚绗缝长外套；加厚活动裤；宽底冬靴；针织帽围巾与小背包|techwear
摄影羽绒马甲装|winter-photography down-vest|长袖内搭与厚毛衣叠厚羽绒马甲；厚工装裤；系带靴；帽手套与相机包|techwear
郊游羊羔绒棉服|fleece-lined picnic coat|薄高领与长袖衬衣叠绒里棉夹克；厚直筒工裤；靴；围巾与帆布背包|retro
冬季运动外层装|winter-track outer-layer outfit|长袖运动内搭与厚运动夹克；加厚运动长裤；运动鞋；针织帽与运动包|streetwear
湖岸长棉服穿搭|lakeside-long padded outfit|高领毛衣与过膝棉服；厚直筒长裤；踝靴；围巾手套与小背包|minimal
山城大衣装|winter-hill-city coat outfit|高领针织与连帽厚呢外套；厚宽长裤；系带靴；帽围巾与斜挎相机包|british
棉猎装工裤冬装|padded-safari winter outfit|长袖内搭与针织中层叠棉猎装；厚工装裤；踝靴；手套与双肩包|british
层叠抓绒马甲装|layered-fleece vest winter|高领衫与厚抓绒叠轻棉马甲；加厚直裤；系带鞋；围巾帽与斜挎包|techwear
冬季旅行软壳装|winter-travel softshell outfit|长袖内搭与厚抓绒中层叠软壳外套；厚直筒活动裤；踝靴；手套与背包|techwear
连帽羽绒连体裤装|hooded-puffer coverall layers|长袖内搭与普通厚棉连体长裤外罩短羽绒；系带靴；帽围巾与肩挎旅行包|streetwear
厚派克外套出游|thick-parka trip ensemble|高领内搭与厚针织中层外罩长派克棉服；厚收脚裤；冬靴；手套与小背包|techwear
''')
block('winter','裙装与室内外层次','''
高领针织裙大衣|turtleneck-knit dress overcoat|高领厚针织膝下连裙与长羊毛大衣；厚不透袜裤；中筒靴；围巾手套与肩包|minimal
羊毛长裙短羽绒|wool-maxi short-puffer outfit|高领毛衣与短羽绒；羊毛长裙；厚不透袜裤与踝靴；针织帽与托特包|mori
绒面半裙长棉服|suede-midi long-padded coat|薄高领上衣与厚开衫外罩长棉服；膝下绒面裙；厚不透袜裤与靴；肩包|retro
衬衫裙毛衣呢大衣|shirtdress sweater wool-coat|长袖厚棉衬衫裙叠短毛衣外罩厚大衣；厚不透袜裤与中筒靴；围巾与手提包|preppy
格纹褶裙厚外套|checked-pleated skirt winter coat|高领内搭与厚圆领针织叠呢外套；羊毛格纹膝下褶裙；厚袜裤与靴；托特包|british
粗花呢裙棉外套|tweed-skirt padded-coat outfit|薄高领毛衣与长棉外套；膝下粗花呢A裙；厚不透袜裤与靴；小公文包|french_girly
灯芯绒背带裙冬装|winter-cord pinafore layers|长袖高领毛衣与厚灯芯绒中长背带裙外罩短棉服；厚袜裤与靴；针织帽与背包|mori
长针织开衫裙套装|long-cardigan skirt coordinates|长袖高领内搭与长厚开衫外搭呢外套；同料针织长裙；厚袜裤与靴；肩包|minimal
短羊毛外套伞裙|short-wool jacket circle-skirt|高领毛衣与厚短羊毛外套；膝下厚伞裙；厚不透袜裤与中筒靴；手套与小包|retro
长羽绒直筒半裙|long-puffer straight-skirt outfit|薄高领与厚针织叠长羽绒；羊毛膝下直裙；厚不透袜裤与靴；围巾与托特包|minimal
毛绒外套针织裙|faux-fur coat knit-dress|长袖厚针织膝下连裙与人工毛绒外套；厚袜裤；踝靴；围巾与小肩包|girly
围裹羊毛裙大衣|wrap-wool skirt overcoat|薄高领衫与厚毛衣外罩长呢大衣；重叠羊毛中长围裹裙；厚袜裤与靴；手提包|british
冬季针织裙裤装|winter-knit culotte layers|长袖内搭与厚毛衣外搭短羽绒；羊毛混纺宽裙裤；厚袜裤与中筒靴；围巾与小背包|minimal
厚背心连裙大衣|thick-vest dress overcoat|棉长袖衬衫连裙叠厚针织背心外罩呢大衣；厚袜裤与靴；手套与书本托特包|preppy
长棉裙羊羔绒装|cotton-maxi fleece winter|高领厚针织与羊羔绒夹克；厚棉中长裙；厚不透袜裤与系带靴；针织帽与布肩袋|mori
冬季室内开衫裙装|winter-indoor cardigan skirt|高领细针内搭与中厚开衫；羊毛混纺膝下直裙；厚袜裤与便鞋；软托特包，出门加长大衣|minimal
''')

assert sum(e.get('seasonal_reference',False) for e in CATALOG)==256
