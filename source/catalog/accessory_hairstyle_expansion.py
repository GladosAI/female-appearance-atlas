"""V29: clothing attachments and complete hairstyles with visible worn accessories."""
from catalog_content import CATALOG,category,add
NEW_ACCESSORY_CATEGORIES=['belts','leg_straps','neck_collars','brooches','scarves_neckerchiefs','ribbons','insignia_badges','cords_tassels']
HAIR_CATEGORY='hair_with_accessories'
HAIR_ACCESSORY_GROUPS=[{'id':'clip','name':'佩戴发卡的完整发型','count':16},{'id':'tie','name':'佩戴发绳的完整发型','count':16},{'id':'headband','name':'佩戴发箍的完整发型','count':16},{'id':'pin','name':'佩戴发簪的完整发型','count':16}]
for key,name,guide,refs in [
 ('belts','腰带与腰封','16种腰带和腰封，比较带身宽度、扣头、带环、穿孔、系结、链节与模块固定；通过完整结构与衣着人台展示扣合及佩戴位置。',['R57','R63']),
 ('leg_straps','腿带与腿侧饰带','16种直接佩戴在成年女性裸腿上的时装腿带，包含蕾丝、缎带、丝绒、细皮带、珠链与金属环。比较大腿佩戴位置、层数、结饰和垂坠；以不透明短裙搭配展示饰带与皮肤的接触。',['R63']),
 ('neck_collars','项圈与贴颈饰','16种时装项圈和贴颈饰，比较绒带、缎带、皮带、金属环、珠串、编带与扣合。使用中性服装颈模，完整显示饰物与闭合位置。',['R15']),
 ('brooches','胸针与衣襟扣饰','16种胸针与衣襟扣饰，比较圆片、宝石框、枝叶花形、链连双针、领扣与衣角固定；展示主体、别针或扣座关系。',['R15']),
 ('scarves_neckerchiefs','围巾、领巾与披巾','16种巾类形态和佩戴方式，包含长巾、方巾、三角巾、环巾、小领巾及披肩式围饰；比较长短、包覆范围、绕颈与结位。',['R57','R63']),
 ('ribbons','缎带与服饰结带','16种缎带、织带与结饰，比较带材边缘、折叠、蝴蝶结、玫瑰结、领口结带和腰侧垂带；带尾及固定点完整可见。',['R57','R63']),
 ('insignia_badges','臂章、肩章、胸章与胸牌','臂章、肩章、胸章、胸牌各4种，共16项，比较衣物上的位置、底片、插槽、扣针、夹扣和挂绳。图形均为原创几何标记，胸牌使用空白卡面。',['R63']),
 ('cords_tassels','自系绳饰与身体装饰绳','16种可独立系、绕、绑在头发或身体上的装饰绳，覆盖头部与头发、手腕、手臂、脚踝、腰腹、大腿、小腿和足背。佩戴图显示环绕关系、结位及完整绳尾；按头发、腕臂、腕踝、腰腹和腿部五组筛选。',['R15','R55','R57'])]:
    category(key,name,guide,refs)
category(HAIR_CATEGORY,'佩戴发饰的完整发型','64种实际佩戴发饰的完整发型：发卡、发绳、发箍、发簪各16项。比较发型、发饰落点和固定关系；按需要采用侧面或斜后视角，保留完整头顶、发饰和发尾。',['R55','R15'])

def accessory(cid,dimension,text):
    rows=[line.strip().split('|') for line in text.strip().splitlines()];assert len(rows)==16,(cid,len(rows))
    refs=['R15'] if cid in ['neck_collars','brooches'] else ['R63'] if cid in ['leg_straps','insignia_badges'] else ['R57','R63']
    for name,en,anchor,recipe in rows:
        add(cid,dimension,f'{name}|{en}|{recipe}。佩戴或固定位置：{anchor}。')
        CATALOG[-1].update(added_in='29.0',accessory_expansion_reference=True,accessory_family=cid,accessory_anchor=anchor,accessory_construction=recipe,adult_sizing=True,reference_ids=refs,
          note='原创衣着配饰结构参考，先看完整轮廓，再比较扣合、端点和服装固定位置。颈模与腿模采用中性成年服装尺码并覆盖完整衣料；章牌用原创几何标记或空白卡面，不指定真实机构、级别或身份。')
        if cid=='leg_straps':
            CATALOG[-1].update(adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年角色的时装腿带佩戴参考',bare_leg_styling=True,
              note='腿带直接贴合成年女性大腿皮肤，比较蕾丝边、弹力段、缎带结、珠链垂弧和小扣件；搭配完整不透明短裙。保留真实环绕方向与松紧关系，饰带位于裙摆下方，不穿在裤料外。')
        if cid=='cords_tassels':
            CATALOG[-1].update(adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年角色的独立装饰绳佩戴参考',body_cord_reference=True,self_tied_ornament=True,reference_ids=['R15','R55','R57'],
              note='独立软绳在头发或身体上形成可见的系结装饰；用正面、侧面或背面显示实际绕行与结位。绳结、编股与完整绳尾共同形成轮廓，手臂和双腿保持自然活动姿态。图例用于比较佩戴造型。')

def hairstyle(kind,text):
    dimension=next(g['name'] for g in HAIR_ACCESSORY_GROUPS if g['id']==kind)
    rows=[line.strip().split('|') for line in text.strip().splitlines()];assert len(rows) in (16,32),(kind,len(rows))
    for name,en,view,ornament,anchor,recipe in rows:
        add(HAIR_CATEGORY,dimension,f'{name}|{en}|25岁以上成年女性，完整不透明高领上衣；{view}。{recipe}；佩戴{ornament}，固定在{anchor}，发饰与发束有真实接触，头顶、发饰和发尾完整可见。')
        CATALOG[-1].update(added_in='29.0',styled_hair_reference=True,hair_accessory_kind=kind,hair_accessory_name=ornament,hair_accessory_view=view,hair_accessory_anchor=anchor,hair_arrangement=recipe,adult_only=True,minor_reference=False,age_min=25,age_context='25岁以上成年角色发型与发饰参考',reference_ids=['R55','R15'],
          note='发型与发饰作为同一个完整造型观察。发夹要夹住实际发片，发绳围住束发根部，发箍沿头部弧线穿过发层，簪杆应穿入发髻并有合理入点和露出端。选用能看清固定处的视角，不把发饰画成悬浮物件；发型长度、分缝与发饰位置可用于自己的角色设定。')

accessory('belts','腰带带身与扣合结构','''
窄皮针扣腰带|narrow leather prong-buckle belt|腰部裤袢|完整细皮带成松弧，矩形针扣、带孔、固定带环和削尖带尾清楚
宽皮双针腰带|wide double-prong leather belt|腰部外层|宽皮带配双针矩形扣，两排孔位与宽带环完整可见
圆环穿绕腰带|double-ring threading belt|腰部裤袢|完整织带与两个圆金属环，带尾绕回两环间，边缘和尾端清晰
滑扣织带腰带|webbing slider-buckle belt|腰部裤袢|平织带配矩形滑扣，平整金属压片、可调带尾与止尾片完整
快插扣机能腰带|side-release utility belt|腰部外层|宽织带与塑料插扣两半扣合，左右调节端和一个扁工具挂环
编织皮条腰带|braided leather waist belt|腰部裤袢|三股扁皮条交编，素面针扣、皮革包端与窄带环清楚
金属链节腰带|metal chain-link waist belt|腰部外层|一圈较宽扁链，龙虾扣与短延长链，末端小圆片，无文字
细链双层腰饰|double-drape fine-chain waist belt|腰部外层|上层细链环腰，下层短弧链在一侧垂落，侧扣与连接环可见
布面系结腰带|fabric tie-waist belt|腰部衣料|宽软布带以平结固定，两条完整短垂尾，边缘有缝线
长尾缎面腰带|long-tailed satin waist sash|腰部礼装外层|宽缎面腰带系成侧结，两条一长一短的完整带尾，有正常布褶
宽片叠搭腰封|overlap-panel waist cincher belt|腰部外层|宽弧形完整腰封，前面两片交叠，侧面小扣带，后面为连贯带身
多段弹力腰带|elastic-panel waist belt|腰部外层|中央素面扣片与左右弹力织带段，接缝和带身纹理清楚
双排带身腰带|parallel double-strap waist belt|腰部外层|上下两条平行细皮带，通过两枚短连接片固定，扣头各自独立
模块挂片腰带|modular tab utility belt|腰部外层|宽织腰带带三个独立扁挂片，插扣、穿带槽与带尾完整
斜垂副带腰饰|diagonal-drop auxiliary waist belt|腰部外层|主腰带闭合，侧边一条短副带斜垂到另一侧连接环，完整端点
盘扣布腰封|knotted-button fabric waist sash|腰部衣料|素色宽布腰封以前方两组绳结盘扣固定，扣环和包边明确
''')
accessory('leg_straps','裸腿佩戴与装饰造型','''
窄蕾丝弹力腿环|narrow lace elastic thigh garter|裸腿大腿中段|25岁以上成年女性的裸露大腿上佩戴一圈窄黑蕾丝弹力腿环，花纹镂空和细波浪边清楚，完整不透明短裙遮盖骨盆
宽蕾丝花边腿带|wide floral-lace thigh garter|裸腿大腿中段|一圈较宽黑色花卉蕾丝贴合成年大腿皮肤，上下两条扇形花边，保留镂空纹理，裙摆位于腿带上方
缎带蝴蝶结腿带|satin-bow thigh garter|裸腿大腿外侧|窄浅色弹力缎带直接环绕成年裸腿，外侧一枚酒红缎面蝴蝶结，两条短尾完整，裙摆上方有明显间隔
双层缎面腿带|double-satin thigh garter|裸腿大腿中段|上下两圈细缎面饰带直接贴合成年裸腿，外侧一个短连接结，层间露出皮肤，不透明短裙完整
丝绒细带腿环|slim velvet thigh garter|裸腿大腿中段|一圈深紫细丝绒环带直接佩戴于成年大腿皮肤，外侧小椭圆扣，绒面和弹力接头清楚
细皮针扣腿带|slim leather buckle thigh garter|裸腿大腿中段|一圈细黑软皮带环绕成年裸腿，外侧小银色针扣、带孔和短带尾，搭配完整不透明短裙
双细带圆环腿饰|double-strap ring thigh garter|裸腿大腿外侧|两圈平行细黑饰带贴在成年大腿皮肤上，在外侧连接一个小圆金属环，层数和穿环点清楚
三环连接装饰腿带|triple-ring decorative thigh garter|裸腿大腿中段|三圈等距细饰带环绕成年裸腿，以外侧一条短竖片连接，带间有清楚皮肤间隔，无口袋或器械
细链垂弧腿饰|draped fine-chain thigh garter|裸腿大腿外侧|一圈细黑软带贴合成年裸腿，两枚小连接环之间垂一条细金属链，链弧自然落于大腿外侧
双珠链腿环|double-pearl-chain thigh garter|裸腿大腿中段|两圈细小珍珠串轻贴成年大腿皮肤，外侧小金属连接片，珠串之间保持窄间距
蕾丝珠坠腿带|lace-and-pearl-drop thigh garter|裸腿大腿外侧|一圈黑色窄蕾丝腿带直接贴合成年裸腿，外侧小结下垂一枚短珍珠坠，镂空与连接环清楚
玫瑰结饰腿环|ribbon-rose thigh garter|裸腿大腿外侧|一圈柔软深红缎带环绕成年裸腿，外侧一朵小缎带玫瑰结和两条短尾，完整饰物不越出画格
交叉缎带腿饰|crossed-satin thigh garter|裸腿大腿外侧|上下两圈窄缎带之间有两条短带在大腿外侧交叉成小X，所有带身直接贴合成年皮肤，皮肤间隔明显
金属心形环腿带|heart-ring thigh garter|裸腿大腿外侧|一圈细黑弹力带连接外侧圆钝心形金属环，环下无长链，贴合成年裸腿并保留完整短裙
波浪边弹力腿带|scallop-edged elastic thigh garter|裸腿大腿中段|浅色平整弹力腿环上下有细波浪包边，直接贴合成年大腿皮肤，外侧一枚小蝴蝶结，带宽和边缘清楚
单侧垂带腿饰|short-drop-tab thigh garter|裸腿大腿外侧|一圈细黑软皮腿带贴合成年裸腿，外侧圆环下垂两条长短不同的短装饰带，完整带端在膝上，不连接腰部
''')
accessory('neck_collars','项圈带身与扣件','''
黑绒细带项圈|narrow velvet fashion choker|贴颈位置|窄黑绒带围绕成年尺码中性灰衣颈模，后侧小扣与延长链完整
宽缎面贴颈圈|wide satin ribbon choker|贴颈位置|宽浅蓝缎带平贴颈模，后方扁扣，前面素净，缎面折光清楚
软皮针扣项圈|soft leather buckle choker|贴颈位置|窄棕软皮带配侧后方小针扣、孔位与带环，佩戴于衣料颈模外
扁铆钉时装项圈|flat-stud fashion choker|贴颈位置|黑皮窄带均匀排列小扁圆铆钉，侧后小扣，无尖刺或附加链条
中心圆环贴颈饰|small-center-ring fashion choker|贴颈位置|两侧柔软织带连接前方一个小圆金属装饰环，后方调节扣完整
中心宝石框项圈|center-stone fashion collar|贴颈位置|深绿窄布带中央为小椭圆包框饰石，带身平顺，侧后扣合清楚
单排细珠项圈|single-row bead choker|贴颈位置|一排小圆珠贴颈排列，两端细线连接小扣与短延长链
双排珠串贴颈饰|double-row bead fashion collar|贴颈位置|两排等径小珠由两侧短连接片固定，背后小扣，圈径和层次明确
编织带贴颈圈|woven-band choker|贴颈位置|扁平交编织带围绕颈模，前部无坠饰，后端短金属压片扣
蕾丝衬底贴颈饰|lined-lace fashion choker|贴颈位置|窄花边覆在完整不透明衬底带上，后侧短缎带系结，边缘纹理清楚
蝴蝶结贴颈饰|bow-front ribbon choker|贴颈位置|细缎面颈带前方固定小蝴蝶结，两条短垂尾，背后小扣
扇褶布边项圈|pleated-edge fabric collar|贴颈位置|柔软窄颈带下缘有一圈短扇褶布边，后方钩扣，不遮住颈模主体
开口金属颈环|open-ended metal neck ring|颈根部|弧形素面金属颈环前方小开口，两端圆头，颈模外轮廓完整
铰链闭合颈环|hinged metal fashion collar|颈根部|薄宽金属环分两片，以一侧铰链和另一侧暗扣闭合，表面素净
链节贴颈圈|flat-chain fashion choker|贴颈位置|一圈扁椭圆链节贴合成年颈模，侧后龙虾扣和短延长链
细带短坠贴颈饰|short-drop ribbon choker|贴颈位置|深紫细织带前方一枚小水滴坠饰，连接环清楚，后扣完整
''')
accessory('brooches','胸针轮廓与衣襟固定','''
圆片素面胸针|round-disc pin brooch|胸前衣料|圆形薄金属片正面与小型侧后视扣针示意，闭合针尖藏入扣座
椭圆框石胸针|oval bezel-stone brooch|胸前衣料|椭圆包框饰石，金属边框和背部横针扣座清楚
方形叠片胸针|layered-square brooch|胸前衣料|三片错位素面方框叠合，背部别针固定结构以小侧视显示
几何三角胸针|geometric triangular brooch|胸前衣料|细金属三角框内一片小色块，背部针扣，尖角为圆钝造型
环形开口胸针|open-ring fastening brooch|披巾衣角|开口金属环与可转动针杆，浅灰布角穿过环内，针杆固定布料
叶片单枝胸针|single-leaf branch brooch|衣襟侧边|一根弧枝连两片叶形金属片，细背针与枝干走向对应
双叶交叠胸针|overlapping-leaf brooch|胸前衣料|两枚不同大小叶形饰片交叠，叶脉刻纹与后针扣清晰
花瓣叠层胸针|layered-petal floral brooch|胸前衣料|三层原创花瓣组成小花，中央圆珠，背部固定底座和针扣
布花圆底胸针|fabric-flower pin brooch|外套衣襟|层叠布花缝在圆形硬底片上，小背针完整可见
珍珠簇胸针|pearl-cluster brooch|胸前衣料|大小小珠组成紧凑扇形簇，细金属支架和背部横针
新月星片胸针|crescent-and-star brooch|胸前衣料|原创新月框与小星片连接，简洁钝边金属，背针不外露
蝴蝶双翼胸针|butterfly-wing brooch|胸前衣料|原创对称蝴蝶形金属饰片，轻微折起双翼与小背针底座
垂链水滴胸针|chain-drop brooch|胸前衣料|一枚圆盘别针下接短链和水滴饰片，连接环和垂坠方向清楚
双针短链衣襟饰|twin-pin lapel chain ornament|左右衣襟|两个小圆别针之间连两条短弧链，分别固定在浅灰双襟布片上
衣角夹扣胸饰|clip-on garment-corner ornament|披巾衣角|扁弧饰片背后为夹扣，夹住一角折叠布料，夹口与弹片关系可见
领口结扣胸针|neckline-knot pin ornament|领口中央|小型绳结状金属饰件居中，后方别针横向固定在两片衣领交汇处
''')
accessory('scarves_neckerchiefs','巾类形态与围系方式','''
窄长缎面围巾|narrow long satin scarf|颈部或肩部|一条完整窄长缎面巾松弧展开，两端平切，显示带宽和柔软折光
宽长羊毛围巾|wide wool scarf|颈肩部|完整宽长软毛巾轻折一回，两端短流苏，织纹和厚度清楚
大方巾对角展开|large square scarf diagonal display|颈肩部|完整大方巾以对角折成三角，素色包边与两个尖角可见
小方形领巾|small square neckerchief|衬衣领口|小方巾完整平展并一角轻翻，边缘卷缝和方形轮廓清楚
三角领巾围饰|triangular neckerchief|颈前部|三角软巾在成年灰衣颈模后系结，前方三角片自然垂于上胸
闭合环形围巾|closed-loop infinity scarf|颈肩部|一圈完整闭合柔软针织环巾松套灰衣颈模，接缝与环圈连续
轻薄长披巾|lightweight long shoulder scarf|肩部|轻薄完整长巾搭在灰衣肩模上，两端在前方自然垂下并完整可见
宽幅厚披巾|wide thick shoulder wrap|双肩与上背|厚软宽巾覆盖灰衣肩模，前方两片交叠，布边与短流苏清楚
小领巾平结系法|small neckerchief square-knot styling|领口前部|小方巾折成窄带在颈模前方系短平结，两枚短尖尾对称垂下
侧结三角领巾|side-knot triangular neckerchief|颈侧部|三角领巾在颈模侧面系结，一段三角布在前胸，另一小尾朝侧下方
单绕长围巾佩戴|single-wrap long-scarf styling|颈肩部|长巾松绕灰衣颈模一圈，两条长短不同的完整巾尾垂在胸前
双绕短尾围巾|double-wrap short-tail scarf|颈肩部|针织长巾松绕颈模两层，两个短尾从前方垂落，层次不混为一团
穿环垂尾围巾|loop-through folded scarf|颈前部|长巾对折成环，两个尾端穿过折环，在灰衣颈模前形成清晰穿环结
胸针固定披巾|brooch-fastened shoulder scarf|肩前部|完整披巾覆灰衣双肩，在一侧肩前用小圆针扣固定，两端自然下垂
水手式领巾围饰|sailor-style neckerchief accessory|衬衣领口前部|窄长三角领巾从后领绕至前胸，前方打小结，双短尾完整，灰色衣领可见
领口长飘带围饰|long-tail neckline scarf tie|领口中央|轻薄长巾在灰衣领口打小结，一长一短细尾垂至胸下，固定点清晰
''')
accessory('ribbons','带材边缘与服饰结带','''
单面亮缎装饰带|single-face satin ribbon|服装缝边或结饰|完整短缎带以一段翻折展示光亮正面与哑光背面，两个切口完整
双面缎纹装饰带|double-face satin ribbon|服装结饰|一条完整光滑缎带松弯成S形，两面都有缎面折光，窄织边清楚
罗纹织带饰条|grosgrain decorative ribbon|服装饰边|平整带身有细密横向罗纹，末端一角翻折，完整卷边和切口
丝绒窄装饰带|narrow velvet ribbon|衣领或袖口|完整窄丝绒带松折，短绒方向与柔软厚度可见，两端不裁切
半透明罩层结带|sheer-over-solid decorative ribbon|衣物外层装饰|一条浅色薄纱罩层带叠在不透明窄带上，两个独立带端完整，纯产品展示
金属线镶边织带|metallic-edge woven ribbon|服装饰边|平织窄带两侧有细金属线边，带身浅弧展开，边缘连续
双色包边缎带|contrast-edge satin ribbon|服装结饰|浅蓝缎面带以深色细包边勾出两侧，松折时包边保持连续
波浪齿边饰带|scallop-edge decorative ribbon|袖口或衣边|完整扁带两侧呈小圆弧波浪齿边，局部轻翻显示厚度
双环短尾蝴蝶结|two-loop short-tail ribbon bow|胸前或腰侧|两枚对称结环和两个短燕尾组成完整蝴蝶结，中心扎带可见
四环叠层蝴蝶结|four-loop layered ribbon bow|衣领或腰侧|两大两小四个结环叠合，中心固定带与两条短尾清楚
单环不对称结带|single-loop asymmetric ribbon knot|肩侧或腰侧|一枚大结环配两条长短不同带尾，中心结有真实穿绕关系
长尾胸前结带|long-tail chest ribbon bow|衬衣领口前部|一枚小蝴蝶结缝在灰色衣领交汇处，两条完整长带尾垂下
腰侧双尾结饰|side-waist double-tail ribbon ornament|腰侧衣料|扁平结饰固定在灰色布腰带侧面，两条不同宽度短尾自然下垂
缎带玫瑰结饰|ribbon-rosette garment ornament|胸前或肩侧|一条缎带卷折成紧凑玫瑰形，背面小圆布底片和缝合点明确
扇褶圆章结饰|pleated-ribbon rosette ornament|胸前衣料|窄带折成圆形扇褶，中央素面圆片，下方两条短带尾，原创无文字
领口交叉结带|crossed neckline ribbon tie|衬衣领口|两条缎带从衣领内侧穿出并在前胸交叉，由小布环固定，带端完整
''')
accessory('insignia_badges','臂章肩章胸章与胸牌','''
圆片缝附臂章|round sewn-on sleeve patch|上臂外侧|灰色长袖衣料外侧缝一枚圆形布章，原创双圆线几何图案与缝线明确
盾形粘附臂章|shield-shaped removable sleeve patch|上臂外侧|灰色袖片上一枚圆钝盾形布章，侧边轻揭显示背部贴合底片，原创几何色块
环袖织带臂章|around-sleeve band insignia|上臂外侧|宽织带完整环绕灰色衣袖，外侧小平扣和无字矩形色块，带身不悬浮
竖片口袋臂章|vertical pocket-flap sleeve badge|上臂外侧|灰色衣袖小袋翻盖上固定窄长几何布牌，扣片与上缘缝线清楚
单扣平片肩章|single-button flat epaulette|肩部衣料|灰色衬衣肩部平贴一条窄布肩片，靠领端单圆扣，外端缝入肩缝
套筒式软肩章|slip-on fabric shoulder tab|肩部衣料|灰色肩带上套一个短软布套筒，原创几何条纹，侧口与套入方向可见
短流苏礼仪肩章|short-fringe costume epaulette|肩部衣料|原创小弧形肩片固定在灰色衣肩，外缘一排短流苏，不含真实军衔图案
扣夹式硬片肩章|clip-mounted costume shoulder plate|肩部衣料|小型圆钝硬片饰章贴合灰色衣肩，下缘扣夹和几何浮片，固定结构完整
圆盘扣针胸章|round pin-back chest badge|胸前衣料|素面圆盘带原创单线几何标记，背针扣座以小侧面结构显示
矩形插槽胸章|rectangular slot-mounted chest insignia|胸前衣料|小矩形板章插在灰色衣服短布槽内，原创三块色片，插槽上下缘清楚
双针链连胸章|linked twin-pin chest badge|胸前衣料|两个原创小几何章分别以针扣固定在灰布上，中间短弧链连接，完整端点
绶带叠片胸章|ribbon-mounted costume chest emblem|胸前衣料|一段折叠短绶带下接圆钝几何片，背部别针固定在灰衣上，无真实勋章图样
夹扣空白胸牌|clip-on blank name badge|胸前衣料|完整横向空白卡壳夹在灰色衣袋口，顶部转轴夹扣与卡壳边框清楚
别针式空白胸牌|pin-back blank name badge|胸前衣料|圆角长方空白名牌固定在灰衣上，小型侧后视显示闭合别针，不生成姓名
磁扣式空白胸牌|magnetic-back blank name badge|胸前衣料|薄圆角空白牌与一块分离的小后夹片放在灰色衣料两侧，成对关系清楚
挂绳卡套胸牌|lanyard blank-card badge|颈下至胸前|灰色高领衣颈模佩戴闭合扁挂带，下端小旋转夹连透明空白卡套，整条挂带完整
''')
accessory('cords_tassels','头发与身体的独立系绑装饰','''
自系绕额头部绳饰|self-tied cord head ornament|头部发际与侧发|成年女性侧前视角，独立赭红细编绳沿发际绕过头部，在耳上侧发处形成小结和两条短尾，绳位于发层表面，完整绳饰可见
独立编绳绕辫装饰|independent braid-wrapping cord|头发单辫|成年女性斜后视角，棕色单辫外有一根金色独立软绳螺旋交绕，在辫尾系一枚小结并露出完整短尾，整条辫发可见
自系交绕盘髻绳饰|self-tied crisscross bun cord|头发盘髻外层|成年女性斜后视角，独立酒红软绳在低盘髻外形成交叉装饰，结位在髻侧，两条短绳尾自然下垂，完整发髻可见
单圈腕部结绳装饰|single-loop tied wrist cord|手腕|成年女性一只自然放松的手与手腕近景，独立深红编绳松贴腕部一圈，外侧小结配两条短尾，手指与完整绳饰均可见
多圈手腕绕绳装饰|multi-wrap wrist cord ornament|手腕|成年女性一只自然放松的手腕，独立浅金软绳在腕部形成三条相邻的松贴平行圈，结在外侧，绳尾完整，不连接另一只手
上臂双圈自系绳饰|self-tied double-loop upper-arm cord|上臂外侧|成年女性侧面上臂，独立赭红软绳形成两条有间隔的环绕圈，在外侧交汇成小结，两条短尾落在臂侧，手臂自然放松
脚踝侧结独立绳饰|side-tied ankle cord ornament|脚踝外侧|成年女性自然站姿的单侧脚踝与完整足部，独立金色细编绳绕踝后在外侧打小结，短尾及细小坠珠清晰，脚趾自然平放
腰部平行侧结绳饰|parallel-loop side-knot waist cord|腰侧|成年女性完整不透明灰色上衣和深色裙装，独立赭红软绳松绕腰部形成相邻平行圈，侧面小结配两条完整垂尾，绳子直接绕在衣着外层
腰腹双圈交叉绳饰|crossed double-loop waist cord|腰腹前侧|成年女性完整灰色上衣外，独立金色软绳形成两道有间隔的环腰圈，在前腹斜向交叉并以一枚小结汇合，绳尾完整
腰侧垂弧结绳装饰|side-draped tied waist cord|腰侧至髋侧|成年女性完整上衣与深色裙装，独立酒红软绳松绕腰部，另一段同材绳在侧面形成短垂弧，小结与短流苏在外侧清楚可见
高马尾缠根独立绳饰|independent cord-wrapped high ponytail|头发高马尾根部|成年女性斜后面完整不透明高领上衣，高马尾根部外独立金色软绳形成短螺旋缠绕，根侧小结和两条短尾可见，完整马尾与头顶均在画面内
前臂间隔绕绳装饰|spaced forearm cord ornament|前臂外侧|成年女性单只自然放松的前臂和完整手部，独立酒红软绳松贴前臂形成三道有间隔的平行圈，外侧小结与两条短尾清晰，不连接其他肢体
脚踝双圈坠珠绳饰|double-loop beaded ankle cord|脚踝外侧|成年女性一只正常平放的完整足部，独立金色软绳在单侧脚踝形成松贴双圈，外侧小结下两条短尾各带一枚小珠，脚趾和脚跟完整可见
大腿双圈结绳装饰|double-loop thigh cord ornament|大腿外侧|成年女性完整不透明短裙下方的裸腿，独立酒红软绳在同一侧大腿形成两条有间隔的松贴环圈，外侧小结和两条短尾清楚
小腿螺旋自系绳饰|self-tied spiral calf cord ornament|小腿外侧|成年女性单腿从膝下至完整足部，独立金色软绳沿小腿形成两段有间隔的斜向螺旋环绕，在小腿外侧打结，两个短绳尾完整，站姿自然
足背绕踝结绳装饰|instep-and-ankle tied cord ornament|足背与脚踝|成年女性正常站姿的一只完整足部与脚踝，独立赭红细软绳在足背形成小交叉并绕到脚踝外侧，外侧小结和两条短尾可见，脚趾完整平放
''')
for entry,region,view,knot in zip(CATALOG[-16:],
 ['头发','头发','头发','腕臂','腕臂','腕臂','腕踝','腰腹','腰腹','腰腹','头发','腕臂','腕踝','腿部','腿部','腕踝'],
 ['斜前面','斜后面','斜后面','手腕外侧近景','手腕外侧近景','上臂侧面','脚踝外侧','正侧面','正面','斜侧面','斜后面','前臂外侧','脚踝外侧','大腿外侧','小腿外侧','足背斜上面'],
 ['耳上侧发','辫尾','发髻侧面','手腕外侧','手腕外侧','上臂外侧','脚踝外侧','腰侧','前腹','腰侧','马尾根侧','前臂外侧','脚踝外侧','大腿外侧','小腿外侧','脚踝外侧']):
    assert entry['category']=='cords_tassels'
    entry.update(dimension=region+'绳饰',cord_region=region,cord_view=view,cord_knot_anchor=knot)
hairstyle('clip','''
一字夹侧别精灵短发|bobby-pin side-tucked pixie haircut|斜侧面|两枚金属一字夹|耳上侧发|耳上精灵短发，偏分前发向耳后收拢，两枚一字夹平行夹住实际侧发片
交叉细夹锁骨直发|crossed-pins collarbone straight hair|斜前面|两枚细一字夹|一侧太阳穴后方|锁骨长直发，薄齐刘海，两枚细夹交叉成小X固定一侧前发
长条背夹半扎波浪发|barrette half-up wavy hairstyle|斜后面|长方弹簧背夹|后脑半扎汇合处|胸上长波浪发，两侧发片向后合拢，横向背夹夹住汇合发束
大齿抓夹法式扭发|claw-clip French-twist hairstyle|斜后面|大齿抓夹|后脑竖向扭束处|中长发在后脑向上扭卷，抓夹两侧齿实际咬合发束，少量发尾露在夹顶
小抓夹半扎短发|small-claw half-up bob hairstyle|斜后面|小圆壳抓夹|后脑上部半扎点|齐肩短波波，上半部发束以小抓夹固定，下半部自然披散
双侧对称夹齐耳发|paired-clips ear-length bob|正面略侧|左右短发卡|两侧耳上|齐耳圆波波，中分无厚刘海，两枚短卡分别固定左右耳上侧发
鸭嘴夹固定侧刘海|duckbill-clipped side-bang hairstyle|侧面|细长鸭嘴发夹|额侧前发|及肩直发，长斜刘海向侧后收拢，鸭嘴夹沿发流固定前发片
金属三角夹半扎长发|triangle-barrette half-up long hair|斜后面|镂空三角背夹|后脑半扎点|及腰直发，两侧细发片后拢，三角背夹横向扣在交汇处，完整发尾可见
珍珠侧夹长波浪发|pearl-side-clip long waves|斜前面|细珠排侧夹|一侧耳上|胸下松波浪，偏分前发一侧收耳后，小珍珠排夹紧贴耳上发片
蝴蝶小夹分区短发|small-butterfly-clips sectioned bob|斜前面|两枚小蝴蝶夹|额角两小发束|下巴短波波，额角两束发向后轻扭，各以一枚小蝴蝶夹固定
圆盘扣夹低半扎发|round-lock-clip low half-up hair|斜后面|圆盘转扣发卡|后脑下部半扎点|锁骨直发，上半发片低位后拢，圆盘扣夹固定中央发束，下发自然下垂
弧形背夹侧拢长发|curved-barrette side-gathered hair|斜后面|弧形横背夹|一侧后脑|胸长波浪发向一侧轻收拢，弧形夹沿后脑弧线扣住发片
双齿侧夹层次短发|two-prong-side-clip layered short hair|侧面|双齿短侧夹|耳后上方|层次耳下短发，侧发上提后以双齿夹夹住，短发尾保持完整轮廓
布结背夹半扎卷发|fabric-bow-barrette half-up curls|斜后面|布结横条发卡|后脑半扎汇合处|胸长松卷发，两侧发束汇在后脑，发卡夹体在布结下方可见
香蕉夹竖束马尾|banana-clip vertical ponytail|斜后面|长弧香蕉发夹|后脑竖向束发根|中长直发沿后脑竖向汇拢，长弧夹两侧齿闭合，马尾从夹中向下展开
三枚短夹偏分中发|three-short-clips side-part hair|斜前面|三枚短直发卡|一侧前发片|齐肩偏分中发，一侧前发向耳后铺平，三枚短夹按发流平行固定
''')
hairstyle('tie','''
细弹力绳高马尾|thin-elastic high ponytail|斜后面|细弹力发绳|头后上方马尾根|肩胛长直发高扎，细黑弹力绳围住真实束根形成两道紧邻圈，扎根收拢而马尾向下自然展开；附同一扎根的局部放大图
棉布褶圈低马尾|cotton-scrunchie low ponytail|斜后面|棉布褶发圈|后颈上方马尾根|肩胛长波浪低马尾，米色棉布褶圈包住束根，内侧收紧、外侧布褶松软；附扎根放大图，发束从发圈中央连续穿出
无缝粗圈中马尾|seamless-fabric-tie mid ponytail|斜后面|无缝粗弹力发圈|后脑中位束根|肩胛长直发中位扎起，棕色粗布圈绕束根两圈并轻压发束，圈体有布面纹理；附真实固定处放大图
缎带结发绳高双尾|ribbon-elastic high twin tails|背面略侧|两枚独立缎带结发绳|左右高位束根|两条肩胛长高双马尾，左右各自以细弹力圈扎根，酒红缎带结附在圈外，短飘尾完整；放大一侧弹力圈与结饰的连接
小橡皮筋低双辫|mini-elastic low twin braids|背面略侧|两枚小弹力橡皮筋|左右辫尾|左右低三股辫各至肩胛上方，两个辫尾分别有一枚小黑橡皮筋绕紧，筋下留完整短发尾；附一侧辫尾固定点放大图
电话线圈半扎发|spiral-coil half-up hairstyle|斜后面|电话线螺旋发圈|后脑半扎束根|锁骨长松卷发半扎成小尾，半透明浅棕螺旋圈围住束根，连续卷曲线圈随束根变形；放大图可见连续细弹性线圈，不画成多颗圆珠
毛圈发绳高马尾|terry-fabric-tie high ponytail|斜后面|毛圈弹力发绳|高马尾束根|肩胛长直发高扎，深蓝毛圈布面弹力绳围住束根，有细小绒圈纹理；附同一固定点放大图，完整马尾自然下垂
扁平发绳短低尾|flat-elastic short low ponytail|斜后面|扁平弹力发绳|后颈短尾束根|锁骨长直发扎成短低尾，浅棕扁平织面弹力带围住束根，带面平整、无游离滑扣；附扎根放大图
小号布圈半丸子|mini-scrunchie half-bun hairstyle|斜后面|小号棉布褶发圈|后脑半丸子根|及肩发上半卷成小丸子，浅米小布圈固定髻根，下半发披散；放大图显示布圈位于髻根，未将整颗发髻套成空环
丝绒发圈低盘髻|velvet-scrunchie low bun|斜侧后面|丝绒布褶发圈|后颈低髻根|中长发盘成紧凑低髻，酒红丝绒圈贴住髻根，绒面布褶柔软；附髻根放大图，丝绒圈与发团有实际接触
罗纹发圈中马尾|ribbed-fabric-tie mid ponytail|斜后面|罗纹织面弹力发圈|后脑中位束根|肩胛长松卷中马尾，浅棕罗纹织面圈包住束根，细密平行罗纹沿布面延伸；附固定点放大图
细皮筋分段泡泡尾|mini-elastic segmented ponytail|背面略侧|四枚独立细橡皮筋|马尾根与三处分段点|肩胛长低马尾，根部与三处分段点各有一枚细橡皮筋，发段在圈间轻蓬，每圈均收紧实际发束；放大其中一处分段点
大号缎圈高团子|large-satin-scrunchie high bun|斜后面|大号缎面布褶发圈|头顶高髻根|长发盘成高团子，浅金大缎面圈在髻根形成有光泽布褶，发团位于圈内上方；附髻根放大图，完整头顶与发圈均可见
丝巾结发圈低马尾|scarf-scrunchie low ponytail|斜后面|附丝巾短尾的布褶发圈|后颈束根|肩胛长直发低扎，米蓝布褶圈围住束根，窄丝巾结连接在圈外，两条短巾尾完整；附圈体、巾结与发束接触的放大图
独立双发圈低双尾|separate-elastics low twin tails|背面略侧|两枚独立普通弹力发圈|左右低位束根|两条齐肩短低双马尾，左右各有独立浅棕弹力圈，后颈中央无连接带；放大一侧扎根，显示圈体围住真实发束
编绳结束辫侧低尾|braided-cord braid-end tie|斜侧后面|细编绳结发绳|单辫末端|侧三股辫至肩胛上方，辫尾用浅色细编绳结扎住，绳下留完整松散发尾和两条短绳尾；附绳结固定辫尾的放大图
''')
for entry,family in zip(CATALOG[-16:],['thin_elastic','cotton_scrunchie','seamless_fabric','ribbon_elastic','mini_elastic','spiral_coil','terry_elastic','flat_elastic','mini_scrunchie','velvet_scrunchie','ribbed_fabric','segmented_elastics','satin_scrunchie','scarf_scrunchie','paired_elastics','braided_cord']):
    assert entry['hair_accessory_kind']=='tie'
    entry.update(hair_tie_detail_inset=True,hair_tie_structure_family=family,structure_reference_urls=['https://www.scunci.com.au/elastics','https://www.scunci.com.au/scrunchies','https://invisibobble.com/products/original-crystal-clear-2023'],
      note='按实物常见的弹力圈、布褶圈、电话线圈和独立结绳结构设计。主图保留完整发型，局部放大图显示同一束根或辫尾：圈体真正环绕发束，发束在固定点收拢，再向外自然展开。布褶包在弹性圈外，螺旋线圈保持连续，不以饰物遮住不合理连接。左右双尾分别固定。')
hairstyle('headband','''
细硬发箍短波波|thin-hard-headband bob hairstyle|斜前面|窄硬发箍|耳后至头顶弧线|下巴短波波，发箍将前发轻推向后，箍脚位于耳后，前额留少量碎发
宽缎发箍长波浪|wide-satin-headband long waves|斜前面|宽缎面包布发箍|头顶部弧线|胸长大波浪，宽浅蓝发箍贴合头弧，发束从箍边自然向后流动
软垫发箍齐刘海中发|padded-headband fringed shoulder hair|斜前面|软垫隆起发箍|头顶部弧线|齐肩直发配薄齐刘海，软垫发箍位于刘海后方而非悬在发顶
扭结发箍锁骨卷发|twist-knot-headband collarbone curls|斜前面|中央扭结发箍|头顶前侧弧线|锁骨长松卷，中央布扭结在头箍顶端，两侧箍脚埋入耳后发层
珍珠发箍低盘发|pearl-headband low updo|斜侧面|单排珍珠发箍|前顶头弧|低盘髻配偏分前发，一排小珍珠沿细箍弧线排列，侧面可见低髻
花簇侧箍半扎发|side-flower-headband half-up hair|斜前面|花簇侧饰发箍|一侧耳上与头弧|胸长半扎波浪发，花簇位于头箍侧部，箍体沿头顶实际贴合
双轨细箍贴颈短发|double-track-headband short crop|斜侧面|双轨细弧发箍|前顶至耳后|贴颈短碎发，两条平行细箍穿过顶发，将前发自然往后收
波浪金属箍中分发|wavy-metal-headband middle-part hair|斜前面|波浪金属发箍|顶发内层|齐肩中分直发，波浪细金属箍顺着头弧插入发层，前侧留两束鬓发
运动宽发带高丸子|sport-headband high bun|斜侧面|运动止滑宽发带|前额发际外沿|成年运动式高丸子，宽织发带沿发际环绕并盖住少量发根，髻与带分开可见
针织发带短卷发|knitted-headband short curls|斜前面|宽针织软发带|前额至后脑|耳下短卷发，针织发带环绕头部，顶发和短卷尾露在带外
交叉软带侧辫发|crossed-soft-headband side braid|斜前面|交叉前额弹力发带|发际上方至后脑|胸长侧辫，软带在前上方交叉，侧发束和辫尾完整可见
蕾丝发箍双低髻|lace-headband twin low buns|斜前面|蕾丝软带发箍|前顶头弧|双低丸子与薄刘海，窄蕾丝发箍位于刘海后，左右髻对称且固定清楚
侧结短尾箍及肩发|side-bow-headband shoulder hair|斜前面|侧结短尾发箍|一侧耳上与头弧|及肩内扣发，发箍侧面一枚小结和两条短尾，箍脚合理藏在耳后
环形编绳带半披发|braided-headband half-down hairstyle|斜前面|环形编绳发带|头顶弧线与后脑|胸长直发半披，细编绳发带顺头弧穿过顶发，后方固定而不勒过眼睛
小齿梳箍后梳中发|toothed-headband swept-back hair|斜侧面|窄硬齿梳发箍|前顶发根|中长直发向后梳，箍内小梳齿插入前顶发层，侧面展示发流被固定的关系
细链发箍高马尾|fine-chain-headband high ponytail|斜前面|链节软骨发箍|前顶头弧|高马尾配两侧短鬓，一条细链包覆在实际软骨箍上，沿头弧延伸到耳后
''')
hairstyle('pin','''
木素簪低盘髻|wooden-pin low coiled bun|斜后面|单杆圆头木簪|后颈低髻内|长发卷成紧凑低髻，一根木簪斜穿髻心，圆头与少量簪尾在两侧可见
金属U簪法式扭髻|U-pin French-twist updo|斜后面|双叉U形发簪|后脑竖向扭髻|中长发竖向扭卷，U簪两腿插入同一发髻，弧形簪头露在上端
双杆发钗高髻|double-prong high-bun updo|斜后面|双杆平行发钗|头后上方高髻|长发盘成高髻，两根平行杆从一侧穿入，饰头和外露杆端清楚
叶形簪低侧髻|leaf-pin low-side bun|斜侧后面|扁杆叶形簪|一侧后颈低髻|侧低髻配偏分长鬓，叶形簪斜向插入髻根，叶头面向外侧
月形簪卷束盘发|crescent-pin rolled updo|斜后面|曲杆月形簪|后脑卷束处|长发分束卷成低盘发，月形簪头露在发髻外侧，弯杆穿过发片
花头簪双辫盘髻|flower-pin braided bun|斜后面|花头短垂链簪|辫盘髻外侧|两条细辫盘成后脑低髻，花头簪插入髻心，小短链自然下垂，不穿过头部
圆环顶簪交片髻|ring-top-pin folded updo|斜后面|几何环顶发簪|后脑交片盘髻|长发交叠成扁盘髻，环顶簪横斜穿入，完整环形饰头与簪尾可见
枝形簪松卷盘发|branch-pin loose-curl updo|斜后面|分叉枝形发簪|后脑松卷髻内|自然松卷发盘成低髻，短枝形簪从侧上方插入，枝头均在发层外
螺旋针圆团髻|spiral-pin round-bun hairstyle|斜后面|螺旋旋入盘发针|圆髻上侧|中长发卷成圆团髻，一枚短螺旋盘发针顶部可见，针身顺髻层旋入而不悬空
珠顶短链簪高盘发|pearl-top-chain-pin high updo|斜后面|珠顶双链发簪|高盘髻侧部|长发盘成高髻，珠顶簪横穿侧髻，两条短细链垂在髻侧，饰头与发束连接合理
横梳珠边低扭髻|pearl-comb low-twist updo|斜后面|横梳珠边盘发饰|后脑低扭髻上缘|中长发低扭成髻，小横梳齿插入髻上缘，珠边露在发层外且不漂浮
花梳侧插法式髻|flower-comb French-updo hairstyle|斜侧后面|细齿侧插花梳|竖向扭髻侧边|法式竖髻，小花梳从一侧插入并固定发片，花簇与部分梳齿根清楚
扁簪盘卷及肩发|flat-pin shoulder-length rolled bun|斜后面|扁杆素面发簪|后颈小卷髻|及肩发向内卷成小低髻，扁簪横向穿入，短发尾自然收在髻内
交叉双簪高盘发|crossed-two-pins high updo|斜后面|两根圆头素簪|高髻两侧|长发高盘，两根素簪在髻内以不同方向交叉固定，外露头尾不刺入皮肤
发网簪组合礼仪髻|hairnet-and-pin formal updo|斜后面|簪杆发网组合饰|低盘髻外层|光顺低髻外包细发网，素簪穿过发网边缘与髻根，网面贴合发团
小冠形簪半扎盘发|small-crown-pin half-up bun|斜后面|原创小冠形簪饰|后脑半扎髻内|胸长直发上半盘成小髻，下半完整披散，小冠形簪头露在髻顶，簪杆穿入发髻
''')
