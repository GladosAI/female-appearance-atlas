"""V25: original adult magical-heroine and ninja costume design families."""
from catalog_content import CATALOG,category,add
NEW_CATEGORIES=['magical_girl_outfits','ninja_outfits']
category('magical_girl_outfits','魔法少女装扮','32套原创魔法少女题材服装，按基础变身礼装与主题进阶礼装整理；比较领袖、胸饰、裙摆、手套、靴袜、头饰与小型法具。题材名称不限定角色年龄，图例采用明确成年角色。',['R63','R04'])
category('ninja_outfits','忍者装扮','32套原创忍者服装，比较交领布衣、裤装、头巾面罩、束袖束腿、护具、腰包与季节外层；历史灵感、舞台和架空幻想分别标记，不把戏剧化造型当作统一史实。',['R93','R63'])

def block(cid,dimension,text,aliases):
    lines=[line.strip().split('|') for line in text.strip().splitlines()];assert len(lines)==16
    for name,en,recipe in lines:
        add(cid,dimension,f'{name}|{en}|25岁以上明确成年女性；{recipe}。')
        CATALOG[-1].update(added_in='25.0',adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年原创角色装扮参考',
          stage_family_reference=True,stage_family=cid,magical_ninja_reference=True,outfit_components=recipe.split('；'),aliases=aliases+[dimension],
          reference_ids=['R63','R04'] if cid=='magical_girl_outfits' else ['R93','R63'],
          note='原创成年角色服装设计。按衣物、头饰、鞋袜及道具固定点拆分，整体和细节可自由组合；不复刻具体作品人物。忍者条目中的舞台或幻想部分不声明史实复原。')

block('magical_girl_outfits','魔法少女·基础变身礼装','''
魔法少女圆领泡袖礼装|round-collar puff-sleeve magical heroine|浅粉不透明圆领泡袖上衣；高腰双层及膝上短裙内置完整安全短裤；胸前原创菱形宝石结；白色不透明袜裤与踝靴
魔法少女水手领礼装|sailor-collar magical heroine costume|青绿不透明短袖水手领上衣；同色及膝上百褶裙内置完整短裤；胸前橙色几何结饰；不透明袜裤与短靴
魔法少女立领长袖装|stand-collar long-sleeve magical heroine|淡紫不透明立领长袖上衣；银灰腰带；同色及膝上A字裙与内层短裤；完整长手套、不透明袜裤及短靴
魔法少女方领叠裙装|square-neck layered-skirt magical heroine|深蓝不透明适度方领泡袖上衣；浅灰交叠裙片与内层及膝上裙裤；小型胸针；不透明袜裤和中筒靴
魔法少女短披肩礼装|capelet magical heroine costume|奶白高领短袖完整内裙；浅蓝短披肩在领下固定；裙摆到膝上且内置完整短裤；发箍、不透明袜裤与白靴
魔法少女胸饰缎结装|ribbon-brooch magical heroine dress|酒红不透明圆领短袖连衣裙；胸前大缎结和原创圆形胸饰；两层及膝上裙摆与内置短裤；不透明袜裤、短手套和踝靴
魔法少女束腰背心装|waistcoat magical heroine ensemble|浅灰不透明长袖衬衣；蓝色短背心与高腰裙裤；领口小领结；几何发卡、不透明袜裤与短靴
魔法少女灯笼袖礼装|lantern-sleeve magical heroine costume|薄荷绿不透明灯笼长袖上衣；白色高腰及膝上裙与完整内层短裤；腰侧小型结饰；发箍、不透明袜裤和短靴
魔法少女长手套裙装|long-glove magical heroine ensemble|紫色不透明高圆领短袖上衣；同色及膝上圆裙内置短裤；完整长手套；宝石发梳、不透明袜裤与中筒靴
魔法少女短裤变身装|shorts-based magical heroine costume|天蓝不透明短袖立领上衣；白色高腰短裤外叠前后短裙片；腰侧小圆包；短手套、不透明袜裤与运动短靴
魔法少女连体长裤装|trouser magical heroine suit|深蓝不透明长袖连体裤；白色几何胸饰和腰带；短肩披；发箍、完整手套与踝靴
魔法少女长裙礼装|long-skirt magical heroine costume|淡紫不透明圆领长袖上衣；及踝双层长裙；胸前小型菱形饰片；发梳、完整手套与白靴
魔法少女斗篷变身装|short-cloak magical heroine costume|奶白不透明长袖上衣与完整及膝裙裤；浅蓝短斗篷在肩上扣合；几何发饰；不透明袜裤和中筒靴
魔法少女几何星饰装|geometric-star magical heroine costume|深绿不透明高领泡袖上衣；白色及膝上百褶裙和内层短裤；原创五角几何星胸饰与发卡；不透明袜裤、短手套和踝靴
魔法少女持短杖礼装|short-wand magical heroine outfit|淡粉不透明长袖连衣裙；及膝上双层裙摆内置短裤；一手在身侧持小型菱形头短法杖；不透明袜裤与短靴
魔法少女持书礼装|book-bearing magical heroine outfit|蓝灰不透明圆领长袖上衣；紫色高腰及膝上裙裤；腰带与小书袋，一手托无文字小书；不透明袜裤、手套和短靴
''',['魔法少女','变身礼装','魔法少女服','magical girl','magical heroine'])

block('magical_girl_outfits','魔法少女·主题与进阶礼装','''
花瓣主题魔法少女装|petal-themed magical heroine|浅紫不透明泡袖连衣裙；及膝上花瓣形叠裙内置完整短裤；原创小花发卡和胸饰；不透明袜裤、短手套与白靴
蝶翼饰魔法少女装|butterfly-backpiece magical heroine|天蓝不透明高圆领无袖上衣；白色及膝上裙裤；完整长手套与背部小型蝶形舞台背饰、肩带固定；不透明袜裤与短靴
星轨主题魔法少女装|star-orbit magical heroine costume|深蓝不透明长袖及膝连衣裙；裙缘少量原创星轨刺绣；小型星形发饰和腰包；不透明袜裤、短手套与踝靴
水波主题魔法少女装|wave-themed magical heroine costume|青绿不透明圆领短袖上衣；银灰及膝上波浪叠裙与完整内层短裤；水滴形胸针；不透明袜裤和中筒靴
火焰主题魔法少女装|flame-themed magical heroine costume|暖橙不透明立领短袖上衣；酒红及膝上锯齿裙片覆在完整裙裤外；原创火焰形发卡；不透明袜裤、手套和短靴
冰晶主题魔法少女装|ice-crystal magical heroine costume|灰蓝不透明高领长袖及膝连衣裙；几何冰晶形白色衣缘；小型几何冠状发箍；不透明袜裤、长手套与中筒靴
雷电主题魔法少女装|lightning-themed magical heroine costume|深紫不透明圆领短袖上衣；灰白高腰裙裤；黄色折线胸饰和发卡；不透明袜裤、短手套与运动靴
森林主题魔法少女装|forest-themed magical heroine costume|深绿不透明圆领长袖上衣；米白及膝上叶片叠裙内置短裤；原创叶形发梳和胸针；不透明袜裤和棕色短靴
机械主题魔法少女装|mechanical magical heroine costume|蓝灰不透明高领长袖连体长裤；原创轻量肩饰、腕套与腰扣；几何头箍；完整运动靴，无机械裸露身体
偶像主题魔法少女装|idol-inspired magical heroine outfit|酒红不透明泡袖圆领上衣；黑白及膝上分层裙与内层短裤；小型原创发结和腰饰；不透明袜裤、短手套与踝靴
和风改编魔法少女装|Japanese-inspired magical heroine outfit|淡紫不透明交领短衣；白色高腰及膝裙裤；袖口短披片和结带，不是巫女制服；几何发簪、不透明袜裤和短靴
中式改编魔法少女装|Chinese-inspired magical heroine outfit|青绿不透明交领长袖短上衣；米白及膝上百褶裙内置完整短裤；小型原创玉形胸饰与发簪；不透明袜裤和短靴
暗色礼装魔法少女装|dark-ceremonial magical heroine costume|深灰不透明高领长袖连衣裙；紫色及膝双层裙摆；小型黑色发箍和几何胸饰；不透明袜裤、完整手套与中筒靴
骑士主题魔法少女装|knight-inspired magical heroine outfit|米白不透明长袖及膝裙裤装；原创银色小肩甲和护腕；浅蓝短披风；不透明袜裤与靴，双手自然下垂无武器
冬季保暖魔法少女装|winter magical heroine ensemble|奶白不透明长袖连衣裙；蓝色及膝裙摆；短保暖披肩与围领；发箍、手套、不透明厚袜裤和保暖靴
进阶长披风魔法少女装|advanced long-mantle magical heroine|深蓝不透明立领长袖上衣与完整长裤；银白前开长披风；原创小几何冠状发箍；完整手套与长靴，背部不加额外翅膀
''',['魔法少女','进阶礼装','主题魔法少女','magical girl','magical heroine'])

block('ninja_outfits','忍者·布装与行动装备','''
藏蓝交领忍者装|navy crossover ninja costume|藏蓝不透明交领长袖布衣与完整长裤；束袖束腿、窄腰带与软底靴；同色头巾和下半脸布面罩；历史灵感改编
炭灰开放面口忍者装|open-face charcoal ninja costume|炭灰高领长袖短衣与长裤；开放面口软头套露出完整脸部；束腕束腿、布腰带与软靴；原创舞台装
头巾半面罩忍者装|headwrap-and-mask ninja ensemble|深蓝不透明交领长袖衣与长裤；独立头巾和鼻口下半脸布面罩；腰侧小布袋、束腿与软靴
高领长袖忍者装|high-collar long-sleeve ninja outfit|深灰不透明高领长袖短衣与完整长裤；无头套且脸部露出；窄布腰带、完整手套、束腿与平底靴
短外褂叠穿忍者装|short-overjacket ninja ensemble|深蓝完整长袖内衣与长裤；外叠灰色前开短褂；独立头巾、布腰带与束腿靴
长外衣忍者装|long-coat ninja costume|炭灰不透明高领长袖及膝外衣；内搭完整深蓝长裤；窄腰带、软头巾与短靴；前开外衣不遮脚
束袖布带忍者装|bound-sleeve cloth ninja outfit|墨绿不透明交领长袖短衣与长裤；上臂及袖口用窄布带收束；头巾、布腰带、束腿和软靴
短披肩忍者装|capelet ninja ensemble|深蓝不透明高领长袖上衣与长裤；灰色短肩披；下半脸布面罩、完整手套、腰带和靴
护前臂忍者装|forearm-guard ninja costume|灰黑不透明长袖短衣与完整长裤；双前臂轻型护片；开放面口头套、束腿与软底靴
护小腿忍者装|shin-guard ninja costume|深蓝不透明交领长袖衣与完整长裤；双小腿原创分片护具；头巾、完整手套、窄腰带与靴
胸前携行带忍者装|chest-rig ninja outfit|深灰不透明高领长袖短衣和长裤；胸前两条细携行带接小型软袋；布头巾、束腕束腿与短靴
腰侧小包忍者装|belt-pouch ninja costume|墨绿不透明交领长袖衣与长裤；腰带连接两只小软包；开放面口软头套、束腿与靴
斜挎布包忍者装|crossbody-bag ninja ensemble|藏蓝不透明长袖短衣与完整长裤；胸前斜挎窄带接腰侧小布包；头巾、腕带、束腿和软靴
短护裙忍者裤装|short-overpanel ninja trousers outfit|炭灰不透明高领长袖衣与完整长裤；腰间两片短护裙覆在裤外；面罩、完整手套与靴
袖套叠穿忍者装|detached-over-sleeve ninja outfit|深蓝完整不透明长袖内衣与长裤；外叠窄袖套和短背心；开放面口头巾、布腰带、束腿与靴
训练布衣忍者装|ninja training-cloth ensemble|灰蓝不透明交领长袖训练衣与完整宽松长裤；简洁束腕束腿；腰带和软靴；无面罩，脸部完整露出
''',['忍者','女忍者','忍装束','ninja','kunoichi'])

block('ninja_outfits','忍者·环境与幻想改编','''
雨披忍者装|rain-cape ninja costume|深灰不透明长袖短衣与完整长裤；外披及腰短防雨披风和开放面帽兜；完整手套、腰带与防雨靴
冬季保暖忍者装|winter ninja ensemble|藏蓝不透明保暖长袖短衣和完整长裤；短围领、头巾与手套；束腿外有保暖脚踝包覆和靴
雪地浅色忍者装|snow-field pale ninja costume|灰白不透明高领长袖上衣与完整长裤；浅灰头巾下半脸布面罩；简洁腰带、手套与保暖靴；原创环境改编
林地深绿忍者装|forest-green ninja costume|墨绿不透明交领长袖布衣和完整长裤；无图案头巾与面罩；腰侧布袋、束腕束腿和棕色靴
沙地米色忍者装|sand-colour ninja costume|米灰不透明高领长袖上衣与完整长裤；同色包头布和下半脸围巾；布腰带、小袋与短靴；原创改编
城巷便装忍者装|urban-disguise ninja outfit|深灰普通长袖短外套与完整深蓝长裤；灰色薄围巾和小型斜挎布包；平底短靴；无面罩、无武器；原创旅装改编
旅途斗篷忍者装|travel-cloak ninja ensemble|藏蓝不透明交领长袖衣与完整长裤；灰色前开短斗篷；头巾、腰侧小包、束腿与软靴
山路束腿忍者装|mountain-path ninja costume|深绿不透明长袖布衣与完整较宽长裤；小腿以长布带收束；普通软布帽、腰带、完整手套和软底靴
竹笠主题忍者装|woven-hat ninja ensemble|深灰不透明交领长袖布衣与长裤；头戴浅色圆锥编织笠、脸部仍露出；下半脸布面罩、腰带、束腿与靴；舞台改编
护甲背心忍者装|armour-vest ninja costume|深蓝完整长袖内衣与长裤；外加原创灰色轻型分片护甲背心；开放面头套、护腕与护腿靴
狐面道具忍者装|fox-mask-prop ninja costume|藏蓝不透明交领长袖布衣与长裤；原创小型白色狐面道具系在头侧、不遮脸；腰包、束腿与软靴
仪式披肩忍者装|ceremonial-shoulder-cloth ninja look|深紫不透明高领长袖上衣与完整长裤；灰色短肩布与几何腰扣；软头巾、护腕和靴；原创架空仪式装
轻装束腰忍者装|lightweight belted ninja outfit|深灰不透明交领长袖短衣与完整贴合长裤；宽布腰带和两个小软袋；短面罩、完整手套、束腿与靴
未来机能忍者装|future-tech ninja costume|灰黑不透明高领长袖连体长裤；原创几何护肩护腕和腰侧软包；半面软罩、完整手套与平底靴；无发光眼睛
幻想披风忍者装|fantasy-mantle ninja costume|深蓝不透明长袖交领衣与完整长裤；前开长披风在肩部扣合；开放面软头套、腰带、护腕和靴
舞台红黑忍者装|red-black stage ninja costume|深灰不透明高领长袖上衣和完整长裤；暗红短外褂与布腰带；额部无字软头带、下半脸面罩、束腿和靴；原创戏剧配色
''',['忍者','女忍者','幻想忍者','环境忍者装','ninja','kunoichi'])

assert sum(bool(e.get('magical_ninja_reference')) for e in CATALOG)==64
