"""Music, fictional screen identities, Japanese retro, street and daytime home outfits."""
from catalog_content import CATALOG,category,add
NEW_CATEGORIES=['idol_outfits','band_outfits','assassin_outfits','japanese_retro_outfits','street_hiphop_outfits','day_home_outfits']
COUNTS={'idol_outfits':8,'band_outfits':12,'assassin_outfits':8,'japanese_retro_outfits':12,'street_hiphop_outfits':12,'day_home_outfits':8}
for cid,name,guide,refs in [
 ('idol_outfits','偶像与歌舞演出造型','8套成年原创偶像服装，比较甜美、元气、清冷、摇滚、国风、未来、复古与成熟歌姬方向；按舞台轮廓、麦克风、发饰与鞋履组织。',['R63']),
 ('band_outfits','乐队与音乐人造型','12套成年原创音乐人搭配，涵盖主唱、吉他、贝斯、鼓手、键盘、弦乐、电子组合、不同音乐风格与排练状态；乐器用于辨认角色，不是演奏姿势教程。',['R63']),
 ('assassin_outfits','杀手与潜行角色装扮','8套影视、游戏与架空杀手、刺客及潜行身份的服装外观；按都市、机能、幻想与古风比较衣层和轮廓，图例为原创虚构角色。',['R63']),
 ('japanese_retro_outfits','日本近现代复古穿搭','12套日本近现代年代灵感造型，比较大正、昭和初中后期及平成初期。逐条注明参考时期；馆藏与研究为延伸阅读，原创图不代表全体日本女性衣着，也不是严格史实复原。',['R174','R176']),
 ('street_hiphop_outfits','街头与嘻哈穿搭','12套街头、嘻哈、复古运动与机能层搭，比较廓形、帽鞋、裤量、夹克与饰品。嘻哈服饰有丰富地区与时期变化，图例是原创穿搭方向。',['R175','R06']),
 ('day_home_outfits','日间居家与家务穿搭','8套日间居家、家务、阅读、轻活动和取件叠穿；以完整内搭、舒适面料与活动余量比较。睡衣与居家夜服另有原类别。',['R06'])]:
    category(cid,name,guide,refs)
NEW_ENTRIES=[];GROUPS=[]

def block(key,cid,title,text):
    GROUPS.append((key,cid,title))
    rows=[line.split('|') for line in text.strip().splitlines()];assert len(rows)==4
    for i,(name,en,desc,recipe) in enumerate(rows,1):
        add(cid,title,f'{name}|{en}|{desc}。')
        e=CATALOG[-1];e.update(role_style_reference=True,role_style_group=key,role_style_order=i,
          added_in='47.0',age_min=25,adult_only=True,minor_reference=False,illustration_recipe=recipe,
          aliases=[title,{'idol_outfits':'偶像','band_outfits':'乐队','assassin_outfits':'杀手','japanese_retro_outfits':'日本复古','street_hiphop_outfits':'街头','day_home_outfits':'居家'}[cid]],
          note='原创25岁以上成年角色的全身服装参考；通过完整衣层、发饰、鞋履和简单手持物表现主题。配图为独立创作，具体舞台、职业和年代款式不等同统一制式或史实复原。')
        NEW_ENTRIES.append(e)

block('idol_core','idol_outfits','偶像·基础舞台方向','''
元气偶像棒球褶裙装|energetic idol varsity-stage outfit|奶白短夹克、珊瑚圆领内搭与及膝褶裙；缎带高马尾、运动短靴和手持麦克风|Adult25 woman, brown ribbon high ponytail, ivory varsity jacket with coral trim over opaque coral crewneck, charcoal knee-length pleated skirt, white ankle sneakers; one plain microphone at side, small cheerful wave, energetic smile
甜美偶像花边舞台装|sweet idol ruffle-stage outfit|雾粉短外套、完整内搭与层叠及膝裙；小蝴蝶结、短袜和圆头鞋，手持麦克风|Adult25 woman, dark curled half-up hair with small rose bows, opaque dusty-pink fitted short jacket over ivory blouse with covered neckline, layered knee-length skirt with subtle ruffle trim, ankle socks and round closed shoes; plain microphone at waist, soft bright smile, adult proportions
清冷偶像银蓝长裤装|cool idol silver-blue stage outfit|银灰短外套、蓝色高领内搭与宽腿长裤；耳返、金属发夹和低跟鞋|Adult28 olive-skinned woman, dark sleek bob with one silver hair clip, silver-gray structured jacket over opaque ice-blue high-neck top, matching full wide trousers and silver low heels; small in-ear monitor, poised still standing, calm direct gaze
摇滚偶像皮衣裙裤装|rock idol leather-layer stage outfit|黑皮衣、红色圆领与格纹裙叠不透明长裤；短靴、小链饰和麦克风|Adult25 medium-brown-skinned woman with short dark curls, black biker jacket over opaque red crewneck, short dark-red plaid overskirt worn over full opaque black trousers, boots and one short decorative chain; holds plain microphone at side, confident small smile
''')
block('idol_theme','idol_outfits','偶像·主题与歌姬方向','''
国风偶像盘扣层裙装|Chinese-inspired idol layered outfit|盘扣短上衣、内搭与青白及膝层裙；流苏发饰、短靴与小型耳麦|Adult25 woman, long dark half-up hair with one small teal tassel ornament, opaque ivory standing-collar short jacket with original simple knot buttons, teal layered knee-length skirt and opaque leggings, white ankle boots; small headset microphone, graceful open hand, original modern Chinese-inspired stage costume
未来偶像几何长裤装|futuristic idol geometric trouser outfit|白紫几何拼片长袖上装与完整长裤；发光感装饰边、耳麦和厚底鞋|Adult28 deep-brown-skinned woman with sculpted short dark hair, opaque white-and-violet geometric long-sleeve top and full straight trousers, pale decorative trim with subtle reflective effect, white platform sneakers and small headset; one hand lifted gently, original futuristic pop costume, no armor or logos
复古歌姬亮片中裙装|retro vocalist sequin-midi outfit|深蓝亮片长袖上衣与奶油中长裙；侧分卷发、珍珠耳饰和细跟鞋|Adult30 woman, brown side-part sculpted shoulder waves, opaque navy sequined long-sleeve top with modest neckline, cream calf-length skirt, pearl drop earrings and closed heels; plain microphone at waist, poised warm smile, retro-inspired stage costume not a named historical uniform
成熟歌姬披肩礼裙装|mature vocalist shawl-gown outfit|酒红不透明长礼裙与薄披肩；低盘发、银色耳坠和闭口鞋，持麦站立|Adult30 woman, dark low updo, opaque burgundy ankle gown with modest draped neckline and matching light shawl, silver drop earrings, closed heels; holds a single plain microphone with both hands at waist, confident restrained singing expression, no open-mouth closeup
''')
block('band_members','band_outfits','乐队·核心成员','''
乐队主唱皮衣长裤装|band vocalist leather-and-trouser outfit|黑皮衣、灰圆领和完整长裤；松散卷发、短靴与手持麦克风|Adult28 woman with loose dark shoulder curls, black leather jacket over opaque gray tee, charcoal full straight trousers and boots; one plain microphone held at side, free hand relaxed, assured front-facing stance, original rock vocalist
电吉他手牛仔层搭装|electric guitarist denim-layer outfit|牛仔夹克、白内搭与黑直裤；小型电吉他用肩带挂在腰侧，完整鞋履|Adult28 olive-skinned woman with dark chin-length bob, blue denim jacket over opaque white tee, black full trousers and low boots; one compact original electric guitar on a strap across waist, neck angled slightly down to fit cell, hands resting naturally on instrument, no playing demonstration or logos
贝斯手长马甲造型|bass player long-waistcoat outfit|黑长马甲叠棕色衬衣与直裤；四弦贝斯挂在腰侧，低位马尾|Adult28 deep-brown-skinned woman with long low braid, black long waistcoat over opaque brown rolled-sleeve shirt, charcoal full trousers and boots; one compact four-string electric bass on strap at hip, neck angled within cell, hands gently hold instrument without performing, no logo
鼓手背心工装裤造型|drummer tank-and-cargo outfit|灰色完整背心、橄榄工装裤和运动鞋；普通护腕，一手持两根鼓棒|Adult28 woman with short dark pixie cut, opaque gray high-neck sleeveless top, olive full cargo trousers, simple wristbands and sneakers; two plain wooden drumsticks held together in one hand at side, other hand relaxed, no drum kit, lively balanced stance
''')
block('band_genres','band_outfits','乐队·风格与编制','''
朋克乐队格纹夹克装|punk-band plaid jacket outfit|暗红格纹短夹克与黑色完整内搭、长裤；短发、短链和厚底靴|Adult28 woman with asymmetrical dark bob, dark-red plaid cropped jacket over opaque black crewneck, full charcoal trousers, short decorative chain and chunky boots; small confident side glance, hands relaxed at hips, original punk band look, no text or gang symbols
金属乐队长外衣造型|metal-band long-coat outfit|黑色长外衣与高领、完整长裤；少量银扣、长靴与深色眼妆|Adult30 medium-brown-skinned woman with long dark waves, opaque black long coat over covered high-neck top, full black trousers and closed boots, sparse silver clasps and smoky eye makeup; still composed stance, no weapons or spikes, original metal music costume
爵士小编制西装造型|jazz ensemble tailored outfit|奶白西装、深蓝衬衣和长裤；低盘发、牛津鞋与简洁耳饰|Adult30 woman with dark low bun, ivory trouser suit over opaque navy blouse, black flat Oxford shoes, small earrings; one plain microphone held gently at waist, warm poised smile, original small-jazz-ensemble look
独立民谣绒面层搭装|indie folk suede-layer outfit|棕色绒面马甲、奶白长袖与中长裙；小型木吉他斜挂，平底鞋|Adult28 woman with long brown braid, camel suede waistcoat over opaque ivory long-sleeve blouse, olive calf-length skirt and flats; compact small-body acoustic guitar on strap at waist, neck angled slightly upward within frame, hands rest naturally, gentle quiet smile, no branding
''')
block('band_more','band_outfits','音乐人·键盘、电子与排练','''
键盘手卷袖衬衣造型|keyboardist rolled-sleeve outfit|浅蓝卷袖衬衣与黑色宽裤；紧凑便携键盘抱在腰侧，低跟鞋|Adult28 woman with neat dark bob, opaque pale-blue rolled-sleeve shirt, black full wide trousers and low shoes; one compact portable 25-key keyboard held vertically beside hip with both hands naturally supporting it, not playing, no logos
电子组合耳机层搭装|electronic act headphone outfit|紫灰短夹克与完整黑内搭、长裤；头戴耳机、小耳麦和厚底运动鞋|Adult28 olive-skinned woman with short dark slick hair, violet-gray short jacket over opaque black high-neck top, full black trousers and chunky sneakers; over-ear headphones resting around neck and small headset microphone, calm focused standing pose, no console or extra props
弦乐组合提琴裤装|string ensemble violin outfit|黑色衬衣、灰色长裤与细腰带；一手持小提琴颈，一手持琴弓，平底皮鞋|Adult28 deep-brown-skinned woman with braided updo, opaque black long-sleeve blouse, gray full tailored trousers, slim belt and black flat shoes; holds one violin by neck near hip in one hand, bow lowered in other hand, no active playing, elegant calm stance
乐队日常排练宽衫装|band rehearsal loose-shirt outfit|宽松素色衬衫、圆领内搭与牛仔长裤；耳机挂颈、帆布鞋，神态放松|Adult28 woman with loose brown low bun, open loose muted teal shirt over opaque white crewneck, full dark jeans and canvas shoes; plain headphones around neck, hands casually in pockets, relaxed rehearsal styling, no music room background
''')
block('assassin_urban','assassin_outfits','杀手·都市与近未来','''
都市杀手极简西装装扮|fictional assassin minimalist suit|炭黑西装、灰色高领与完整长裤；低盘发、短手套和小型硬包，站姿克制|Adult30 woman with sleek dark low bun, charcoal tailored suit over opaque gray high-neck top, full trousers, short gloves and closed low heels; holds one small closed hard handbag, poised still stance, fictional screen assassin costume, NO weapons, no action or real tactics
雨夜主题杀手长风衣装|fictional assassin raincoat costume|深灰长风衣叠完整内搭与长裤；短靴、小型斜挎包和深色帽，面部可见|Adult30 olive-skinned woman with dark bob, dark-gray long trench over opaque black crewneck, full trousers and ankle boots, small closed crossbody bag and simple brimmed hat; face clearly visible, neutral standing on ivory studio background, fictional noir assassin fashion, no rain scene or weapon
潜行角色高领连体装|fictional stealth-role jumpsuit|墨蓝不透明高领长袖连体裤；软质短外披、窄腰带和完整手套靴|Adult28 deep-brown-skinned woman with short dark curls, opaque midnight-blue high-neck long-sleeve full jumpsuit, short soft capelet, narrow belt, full gloves and flat boots; simple stylized costume panels, neutral upright pose, no tools, weapons, tactical demonstration or masking instructions
近未来杀手机能外衣装|futuristic assassin utility-coat costume|灰紫短机能外衣与完整长裤；少量几何包袋、耳侧饰件和短靴|Adult28 woman with silver-gray chin-length bob, gray-violet structured utility short coat over opaque dark top, full trousers, small geometric closed belt pouches and flat boots, tiny ear-side decorative device; original futuristic assassin costume, no weapon or operation, clear adult face
''')
block('assassin_fantasy','assassin_outfits','刺客·幻想与古风','''
宫廷刺客短披肩装|fantasy court-assassin capelet costume|深绿短披肩、米白立领上装与黑色长裤；袖扣、短手套和低跟靴|Adult28 woman with dark braided updo, forest-green short capelet over opaque ivory standing-collar blouse, full black trousers, short gloves and low boots; one original small metal clasp, composed full standing, fictional court-assassin costume, no weapon or assassination action
沙漠幻想刺客层袍装|fantasy desert-assassin layered robe|米褐层袍罩完整内衣裤；头巾、腰带与包覆靴，脸部和双手清楚可见|Adult28 brown-skinned woman, sand-beige layered long robe over opaque taupe long-sleeve top and full trousers, loosely wrapped headscarf with full face visible, simple belt and covered flat boots; neutral relaxed standing, original desert fantasy costume, no real cultural uniform or weapon
古风斗篷刺客裤装|Chinese-fantasy assassin cloak outfit|墨色短斗篷、灰色交领上衣与长裤；束袖、布带和长靴，低束发|Adult28 woman with long dark low ponytail, ink-black short cloak over opaque gray cross-collar long-sleeve top, full black trousers, simple fabric cuff ties and flat boots; original Chinese-fantasy assassin clothing, face visible, no sword, knife, combat or historical-uniform claim
礼服伪装杀手主题装|fictional assassin formal-disguise costume|黑色长袖不透明礼裙与短外套；银耳钉、手拿硬包和闭口鞋，目光平静|Adult30 woman with dark sculpted waves, opaque black long-sleeve calf-length evening dress with modest neckline, short fitted jacket, small silver studs, closed heels and small closed clutch; calm level gaze and hands at waist, fictional screen assassin disguise costume, no concealed weapon or operational details
''')
block('japan_early','japanese_retro_outfits','大正与昭和初期灵感','''
大正末和洋折衷羽织袴装|Taisho-inspired haori-hakama outfit|参考1910—1920年代和洋折衷轮廓；条纹和装上衣、深色袴、短羽织与系带短靴|Adult25 Japanese woman with dark low bun, original striped kimono-style upper layer with correctly left-over-right front, dark plum full-length hakama, navy short haori, brown lace-up ankle boots; modest adult ceremonial styling inspired by Japan1910s–1920s, not a schoolchild or strict historical reconstruction, full standing
昭和早期几何铭仙和装|early Showa-inspired graphic kimono outfit|参考1920年代末—1930年代；原创几何纹和装、窄色块羽织与简洁腰带|Adult28 Japanese woman with dark low updo, original bold indigo-and-cream geometric meisen-inspired kimono with correctly left-over-right closure and wide sash, muted wine haori, white tabi socks and plain zori; Japan late1920s–1930s inspiration, fabric motifs original, no exact historical replication
昭和初期摩登连衣裙装|early Showa-inspired modern dress outfit|参考1930年代都市洋装轮廓；小翻领及小腿连衣裙、窄腰带与圆沿帽|Adult28 Japanese woman with dark finger-wave bob, opaque muted teal calf-length dress with small lapel collar, softly shaped waist and narrow belt, small round-brim hat and closed low heels;1930s Japan urban modern-girl-inspired styling, original interpretation, poised full standing
昭和战后衬衣长裙装|postwar Showa-inspired blouse-and-skirt outfit|参考1940年代末—1950年代初的简洁轮廓；奶白衬衣、深色中长裙和针织外搭|Adult28 Japanese woman with neat dark low waves, opaque ivory button blouse, dark-blue calf-length A-line skirt, plain brown knit cardigan and flat closed shoes; simple late1940s–early1950s Japan-inspired everyday styling, original studio costume not a universal social-history claim
''')
block('japan_middle','japanese_retro_outfits','昭和中期洋装灵感','''
昭和五十年代束腰伞裙装|1950s Showa-inspired full-skirt outfit|参考1950年代国际洋装轮廓；合体开衫、收腰伞裙、短项链与圆头低跟鞋|Adult28 Japanese woman with softly curled dark bob, opaque cream fitted cardigan over closed-neck blouse, muted rose calf-length full skirt with defined waist, small plain bead necklace and round-toe low heels;1950s silhouette interpreted for Japanese retro character design, no claim all women dressed this way
昭和六十年代A线裙装|1960s Showa-inspired A-line dress|参考1960年代；蓝白色块A线及膝裙、低跟鞋和简洁手提小包|Adult28 Japanese woman with dark sculpted short bob, opaque blue-and-white color-block knee-length A-line shift dress with modest high neckline, white low block heels and small box handbag;1960s retro silhouette, original studio fashion study
昭和六十年代套裙造型|1960s Showa-inspired skirt suit|参考1960年代；短西装、及膝直裙、小翻领衬衣与闭口鞋|Adult30 Japanese woman with tidy dark bob, pale gray-blue short jacket and matching knee-length straight skirt, opaque ivory small-collar blouse, closed low heels and small structured handbag;1960s clean suit silhouette, restrained adult styling
昭和七十年代喇叭裤装|1970s Showa-inspired flared-trouser outfit|参考1970年代；长领衬衣、针织背心、喇叭长裤与包覆厚底鞋|Adult28 Japanese woman with long dark center-part hair, opaque cream long-point-collar shirt, ocher knit vest, dark-brown full flared trousers and covered block-heel shoes;1970s international silhouette interpreted for Japanese retro character design, no branding
''')
block('japan_late','japanese_retro_outfits','昭和末期与平成初期灵感','''
昭和七十年代花纹长裙装|1970s Showa-inspired printed maxi outfit|参考1970年代；原创小花长袖衬衣裙、细腰带、针织披肩与短靴|Adult28 Japanese woman with softly waved dark long hair, opaque brown-and-cream original small-floral long-sleeve ankle shirtdress, slim belt, plain knitted shoulder shawl and low boots;1970s nostalgic everyday silhouette, studio full body
昭和八十年代宽肩套装|1980s Showa-inspired broad-shoulder suit|参考1980年代；宽肩短西装、高腰及膝裙、素色完整内搭与闭口鞋|Adult30 Japanese woman with dark sculpted shoulder waves, muted teal broad-shoulder tailored jacket over opaque cream blouse, high-waist knee-length straight skirt, closed pumps and small plain handbag;1980s tailored silhouette, original interpretation without logos
平成初期短夹克长裙装|early Heisei-inspired jacket-and-maxi outfit|参考1990年代前半；短夹克、白圆领内搭与长直裙，系带短靴与小包|Adult28 Japanese woman with dark chin-length bob, charcoal cropped zip jacket over opaque white crewneck, gray ankle-length straight skirt, black lace-up ankle boots and small shoulder bag;early1990s original Japanese retro-inspired outfit, no school uniform
平成初期街头层搭装|early Heisei-inspired street layers|参考1990年代前半；格纹衬衣、宽松T恤、完整直筒牛仔裤与运动鞋|Adult28 Japanese woman with dark low ponytail, loose muted-red plaid overshirt over opaque white tee, full blue straight jeans and white sneakers, small canvas shoulder bag;early1990s casual-layer silhouette, natural adult standing, original fashion illustration
''')
block('street_daily','street_hiphop_outfits','街头·滑板、工装与层搭','''
滑板街头宽衫长裤装|skate-street loose-shirt outfit|宽松图形T恤与完整直筒牛仔裤；针织帽、低帮帆布鞋和斜挎小包|Adult25 woman with dark chin-length bob under plain knit beanie, opaque oversized ivory tee with a small original abstract geometric motif and no text, full blue straight jeans, canvas low-top shoes and small crossbody bag; relaxed standing, no skateboard needed
涂鸦灵感夹克工装|graffiti-inspired street utility outfit|原创彩块夹克、黑圆领与工装长裤；平檐帽、运动鞋与简短饰链|Adult28 medium-brown-skinned woman with short dark curls under plain flat-brim cap, colorful original abstract-panel utility jacket over opaque black tee, full charcoal cargo trousers, sneakers and one short chain; casual confident standing, no brand logos or spray tools
街头牛仔长裙叠穿装|street denim-maxi layered outfit|宽衬衣、完整背心内搭与牛仔长裙；软帽、小包和厚底鞋|Adult28 woman with loose brown low braid, open loose sage overshirt over opaque ivory crewneck tank, full ankle denim skirt, plain soft bucket hat, small shoulder bag and chunky closed sneakers; relaxed slight weight shift, complete full body
都市工装马甲宽裤装|urban utility-vest street outfit|多袋短马甲叠灰色长袖与宽直长裤；小耳机、运动鞋和帆布包|Adult28 olive-skinned woman with short dark pixie cut, muted olive multi-pocket short vest over opaque gray long-sleeve crewneck, cream full wide trousers and sneakers; compact headphones around neck and small canvas tote, neutral street fashion pose, no military insignia
''')
block('hiphop_sport','street_hiphop_outfits','嘻哈·复古运动与宽廓形','''
嘻哈宽球衣牛仔装|hip-hop oversized-jersey outfit|宽松无号码球衣、完整长袖内搭与宽腿牛仔裤；素色帽、圈耳环和高帮鞋|Adult28 deep-brown-skinned woman with dark braids, oversized navy-and-cream basketball-style jersey without number or logos over opaque full-sleeve tee, full wide blue jeans, plain cap, medium hoop earrings and high-top sneakers; relaxed upright fashion stance
嘻哈复古运动套装|hip-hop retro tracksuit outfit|紫绿复古拼色完整运动套装；头巾、小项链与包覆运动鞋，神态自然|Adult28 woman with dark short curly hair and small plain headband, opaque violet-and-teal retro color-block full tracksuit with zipped jacket, one simple short necklace and sneakers; easy standing with one hand in pocket, original hip-hop sportswear inspiration, no stereotypes or logos
街舞风宽风衣裤装|street-dance windbreaker outfit|橘白宽松防风外套与完整宽裤；轻便腰包、运动鞋，站立小幅屈肘|Adult25 medium-brown-skinned woman with dark high ponytail, orange-and-ivory loose windbreaker over opaque tee, full charcoal baggy trousers, small waist bag and sneakers; standing balanced with loosely bent elbows, no difficult dance pose
复古棒球夹克嘻哈装|varsity-jacket hip-hop outfit|深绿棒球夹克与白色圆领、宽腿裤；无字帽、短链和厚底鞋|Adult28 olive-skinned woman with long dark braid under plain cap, dark-green varsity jacket with ivory sleeves and no letters, opaque white tee, full tan wide trousers, short plain chain and chunky sneakers; relaxed side-facing stance, no real team identity
''')
block('street_tech','street_hiphop_outfits','街头·机能、运动与极简混搭','''
机能街头灰黑层搭装|technical street gray-black layers|灰黑多层短外衣、完整高领和宽长裤；几何小包与包覆运动鞋|Adult28 woman with silver-gray dark-root bob, gray-black layered short shell jacket over opaque high-neck top, full wide dark trousers, two small closed geometric fashion bags and black sneakers; clean neutral upright stance, fashion techwear no weapon or tactical instructions
运动街头褶裙裤装|sport-street pleat-over-trouser outfit|运动短夹克与及膝褶裙叠完整直裤；棒球帽、腰包与运动鞋|Adult25 woman with dark high ponytail through plain baseball cap, cobalt short sports jacket over opaque cream tee, charcoal knee-length pleated overskirt over full black straight trousers, small waist pouch and sneakers; playful relaxed standing
极简街头长衫宽裤装|minimal street long-shirt outfit|长款白衬衫、深色完整内搭与宽直裤；小挎包、短项链和低帮鞋|Adult28 deep-brown-skinned woman with short dark natural hair, long open ivory shirt over opaque black crewneck, full charcoal wide straight trousers, small crossbody bag and flat white sneakers; balanced relaxed stance, simple layered street silhouette
层次街头卫衣长裙装|layered street hoodie-maxi outfit|米灰完整连帽衫与蓝色长裙；外搭短马甲，针织帽和厚底鞋呼应|Adult28 olive-skinned woman with dark chin-length hair under gray beanie, opaque oatmeal hoodie, short charcoal open vest, navy ankle-length skirt and chunky closed sneakers; hands relaxed at sides, coordinated soft street layers, no logos
''')
block('home_daily','day_home_outfits','居家·日间舒适与家务','''
薄棉居家圆领裤装|daytime cotton home outfit|奶白棉质圆领长袖与蓝灰直裤；软底拖鞋，发绳简单束发，双手自然放松|Adult28 woman with brown low loose ponytail, opaque ivory cotton long-sleeve crewneck and blue-gray full soft straight trousers, simple flat closed-toe house slippers; relaxed upright standing with arms at sides, daytime loungewear not nightwear or lingerie
针织居家长开衫装|knit cardigan home outfit|浅褐长开衫、完整圆领内搭与针织宽裤；软底鞋和小发夹，轻扶袖口|Adult28 deep-brown-skinned woman with short natural curls and small plain clip, tan long cardigan over opaque cream crewneck, charcoal full knit wide trousers and flat closed house shoes; one hand lightly touches cuff, cozy adult daytime home styling
家务围裙衬衣长裤装|housework apron-and-trousers outfit|浅绿卷袖衬衣、棉布围裙与完整长裤；头发收拢，软底防滑鞋，手持干净布巾|Adult28 olive-skinned woman with dark low bun, opaque sage rolled-sleeve shirt and full beige trousers, plain ivory cotton apron and flat closed house shoes; holds one folded clean cloth at side, practical neutral standing, no kitchen background or cleaning chemicals
凉夏居家衬衫短裤装|summer daytime home shorts outfit|轻薄但不透明的蓝色短袖衬衣与及膝棉短裤；平底拖鞋，姿态放松|Adult28 woman with brown shoulder-length hair tucked behind ears, opaque pale-blue loose short-sleeve button shirt with normal covered neckline, ivory knee-length cotton shorts and flat house slippers; relaxed standing, normal adult proportions, no transparency or sexual pose
''')
block('home_activity','day_home_outfits','居家·冬日、阅读与轻活动','''
冬日绗缝居家外套装|winter quilted home outfit|浅粉绗缝短外套、圆领内搭与完整软裤；厚底室内鞋和低位发圈|Adult30 woman with brown low bun secured with plain scrunchie, dusty-pink quilted short home jacket over opaque cream crewneck, full gray soft trousers and warm closed house slippers; hands lightly clasped, cozy daytime winter home styling
阅读居家衬衫长裙装|reading-at-home shirt-and-skirt outfit|奶白软衬衣、浅紫中长裙与针织披肩；眼镜、小书本和软底鞋，站立捧书|Adult30 woman with dark shoulder waves, thin reading glasses, opaque ivory soft blouse, muted lavender calf-length skirt and knitted gray shoulder shawl, flat closed house shoes; holds one closed plain book at waist, calm standing, no readable text
轻活动居家运动裤装|light-activity home outfit|宽松长袖运动衫与完整弹力长裤；普通发带、平底软鞋，轻抬手臂舒展|Adult28 medium-brown-skinned woman with tied-back dark curls and plain headband, opaque loose sage long-sleeve sports top, full charcoal stretch trousers and flat soft closed shoes; small standing shoulder stretch with one hand gently at opposite elbow, no contortion or yoga mat
门口取件居家叠穿装|home doorstep layered outfit|完整棉T恤与长裤外加针织短外套；简洁发夹、小布袋和包覆休闲鞋|Adult28 olive-skinned woman with dark bob and small hair clip, opaque white cotton tee and full navy soft straight trousers, oatmeal short knit jacket, flat slip-on closed shoes; carries small plain cloth bag, natural standing ready to step out, daytime home layers, no package logos
''')

periods=['1910—1920年代','1920年代末—1930年代','1930年代','1940年代末—1950年代初','1950年代','1960年代','1960年代','1970年代','1970年代','1980年代','1990年代前半','1990年代前半']
for i,e in enumerate([e for e in NEW_ENTRIES if e['category']=='japanese_retro_outfits']):
    era='大正' if i==0 else '平成初期' if i>=10 else '昭和'
    dim='大正时期' if i==0 else '平成初期' if i>=10 else '昭和初期与战后' if i<=3 else '昭和中期' if i<=7 else '昭和后期'
    e.update(reference_period=periods[i],era_name=era,region='日本',chronology_order=i+1,dimension=dim)
    e['aliases'] = ['日本复古',era,periods[i]]
    if era=='昭和':e['aliases'].append('邵和')
    e['note']='日本近现代年代灵感的原创角色造型。大正、昭和与平成初期分别标注，西式款按同期馆藏轮廓作创作转译；相关阅读不证明每个细节均为日本普遍穿法。'
assert len(NEW_ENTRIES)==60 and len(GROUPS)==15
assert all(sum(e['category']==cid for e in NEW_ENTRIES)==n for cid,n in COUNTS.items())
