"""Edition 14: original hosiery product and construction references."""
from catalog_content import CATALOG, category, add

LEGACY_HOSIERY_IDS={f'FW{i:03}' for i in range(21,27)}
DENIERS=[6,8,10,12,15,20,25,30,40,50,60,80,100,120,150,200]
DENIER_NOTE='D是纱线线密度，透感还受织法、颜色和拉伸影响；图例是设计示意，不是光学或厚度标定。'

category('hosiery','袜类与袜裤','分开比较D数、袜长、织法、袜口固定、连裤结构与花纹；图例用服装产品和中性腿模展示。',['R66','R67','R68'])

def block(dimension,text):
    start=len(CATALOG);add('hosiery',dimension,text)
    assert len(CATALOG)-start==16,(dimension,len(CATALOG)-start)
    for e in CATALOG[start:]:
        e.update(age_context='成年规格袜类产品参考',hosiery_reference=True)
        e['aliases']=['袜类','袜子','女袜','hosiery']

start=len(CATALOG)
block('丝袜D数与透感参考','''
6D丝袜纱线参考|6 denier hosiery reference|同尺度中性灰小腿模上极轻的黑色薄袜示意，袜口和脚尖完整，附小袜料片。
8D丝袜纱线参考|8 denier hosiery reference|同尺度灰腿模上很薄的黑色细袜示意，灰底仍明显，薄袜边缘清楚。
10D丝袜纱线参考|10 denier hosiery reference|同尺度灰腿模上轻薄黑色丝感袜，薄膜色感可见，小袜料片显示细密织纹。
12D丝袜纱线参考|12 denier hosiery reference|同尺度灰腿模上轻薄黑色袜料，袜口与趾端薄边清楚，作为12D纱线视觉例。
15D丝袜纱线参考|15 denier hosiery reference|同尺度灰腿模上黑色薄丝袜，浅灰底仍可见，脚背与踝弯连续包覆。
20D丝袜纱线参考|20 denier hosiery reference|同尺度灰腿模上黑色丝袜有较清楚覆盖色，膝下袜口、足跟和足尖完整。
25D丝袜纱线参考|25 denier hosiery reference|同尺度灰腿模上黑色细袜有轻柔遮盖，配小幅织纹片；透感是创作示意。
30D丝袜纱线参考|30 denier hosiery reference|同尺度灰腿模上黑色半透袜料，踝部体积仍读得出，小袜料片边完整。
40D丝袜纱线参考|40 denier hosiery reference|同尺度灰腿模上黑色袜料覆盖更浓，足背有克制浅高光，观察过渡与袜口。
50D丝袜纱线参考|50 denier hosiery reference|同尺度灰腿模上偏密黑色丝感袜，整体覆盖深，配织纹片显示连续细织面。
60D丝袜纱线参考|60 denier hosiery reference|同尺度灰腿模上较密黑色袜料，平滑表面与细袜口清楚，脚形以阴影表现。
80D丝袜纱线参考|80 denier hosiery reference|同尺度灰腿模上黑色不透明风格袜，平整覆盖面，足跟和脚尖弧面完整。
100D丝袜纱线参考|100 denier hosiery reference|同尺度灰腿模上密实黑色丝感袜，较厚袜口和均匀细织面；不标称绝对透光率。
120D丝感袜料参考|120 denier silky hosiery reference|同尺度灰腿模上密实深黑袜料，袜口、脚尖及小织纹片展示细密外观。
150D丝感袜料参考|150 denier silky hosiery reference|同尺度灰腿模上高D深黑袜料，厚实边缘与柔和面光，具体透感由织法另定。
200D丝感袜料参考|200 denier silky hosiery reference|同尺度灰腿模上高D密实袜料，轮廓靠面光和折线区分，附独立小织纹片。
''')
for e,d in zip(CATALOG[start:],DENIERS):
    e.update(denier=d,note=DENIER_NOTE)
    e['aliases']+=['丝袜','丝感袜',f'{d}D',f'{d} D',f'{d}den',f'{d} denier','丹尼尔','denier']

block('袜长与趾部轮廓','''
浅口隐形船袜|shallow no-show liner socks|一对完整低口船袜产品，袜口绕脚背低处，脚尖与足跟袋连成一体，附灰脚模位置小图。
深口隐形船袜|deep-cut liner socks|一对完整船袜产品，脚背开口比浅口更小，足跟较高，开口边与袜底清楚。
袜后跟防滑小耳短袜|heel-tab ankle socks|一对低帮短袜，后袜口高出一枚软小耳，前袜口低，足尖足跟完整。
贴踝低帮袜|low ankle socks|一对完整袜子只盖至踝骨下侧，弹性薄袜口清楚，脚背不画鞋。
踝上短筒袜|above-ankle socks|一对袜口在踝骨上方的短袜，短筒与完整足部相接，灰腿模作位置参照。
小腿下段袜|lower-calf socks|一对袜筒抵小腿下段，筒与脚跟有连续转折，袜口有清楚窄罗纹。
标准中筒罗纹袜|crew rib-cuff socks|一对袜筒到小腿中段，宽罗纹口、脚跟袋与趾端弧线完整。
小腿高筒袜|high-calf socks|一对袜筒到小腿上段但不到膝，灰腿模膝位可见，袜筒不跨过膝。
膝下长筒袜|below-knee long socks|一对长袜口停在膝盖下方，灰膝位小图显示距离，整条袜筒和足部完整。
贴膝袜口长袜|knee-level cuff socks|一对袜口接近膝部下缘，宽袜口平整，灰腿模显示接近膝位的长度。
膝上窄口长袜|above-knee narrow-cuff socks|一对袜口略过膝位，窄平口，袜筒不延伸至大腿根，中性灰腿模参照。
大腿中段平口长袜|mid-thigh plain-top stockings|一对长袜止于大腿中段，平整加固上缘，无硅胶和吊带，独立产品平铺。
外翻袜口中筒袜|turn-down cuff crew socks|一对中筒袜口向外翻折形成双层边，袜筒、足跟与脚尖完整。
松堆袜筒长袜|slouch-shaft long socks|一对完整长袜在踝上形成连续软堆褶，上口与足部相连，区别无足袜套。
五趾分趾短袜|five-toe ankle socks|一对短袜趾端有五个独立小趾袋，最长为大趾袋，正常五趾结构，产品展示。
拇趾分趾二趾袜|split-toe tabi socks|一对袜子趾端分大拇趾一袋与其他四趾合袋，两袋和足跟、袜口完整。
''')

block('针织材质与日常袜','''
平针棉感中筒袜|plain-knit cotton-look crew socks|一对平针袜产品，柔和不透明表面、窄罗纹口和加固趾跟，织面小图附侧。
细罗纹棉感短袜|fine-rib cotton-look ankle socks|一对短襪表面有细密纵罗纹，袜口接更密罗纹，脚尖与后跟完整。
粗罗纹厚中筒袜|coarse-rib thick crew socks|一对厚中筒袜，粗纵凸纹沿筒和足背走，足跟凸出，厚袜口清楚。
麻花编织长袜|cable-knit long socks|一对不透明长袜，竖向麻花交叉纹清楚，完整袜口与足部，附一小段编织放大。
羊毛感细织袜|fine-knit wool-look socks|一对完整袜子有均匀细织面与少量柔短绒，灰蓝色，外观不能鉴定纤维。
羊绒感绒面袜|cashmere-look fuzzy socks|一对软米色袜子，短绒轮廓和软折边清楚，足跟趾端完整，材质为绘画标签。
厚毛圈家居袜|thick terry house socks|一对厚袜足底与袜口可见密小圈绒，小内翻边展示毛圈面，完整袜体。
细圈绒运动短袜|loop-knit sports ankle socks|一对短袜脚底较厚、足背细织，跟和趾袋有分区接缝，不标称运动性能。
绒毛家居防滑袜|fuzzy non-slip-style house socks|一对短绒袜，一只侧向展示、一只翻底展示原创小点底纹，成品结构参考。
绗格棉感睡眠袜|quilt-pattern soft sleep socks|一对软厚袜表面浅小菱格，宽松袜口与趾跟完整，家居产品外观。
薄针织网区短袜|light-knit mesh-zone ankle socks|一对短袜在足背有小网区、足底连续细织，袜口与两种织法边界清楚。
加固趾跟工作袜|reinforced-toe-heel socks|一对灰色中筒袜，深色加固趾袋与足跟袋有明确分区边，无工作效能声明。
三道横杠运动袜|three-stripe sports crew socks|一对白色中筒袜口下有三条原创新条纹，袜身平织、趾跟完整，无品牌标识。
翻边花口针织袜|scallop-cuff knitted socks|一对不透明短袜，袜口是小圆弧花边，不画成悬空蕾丝圈，袜体完整。
无足罗纹袜套|footless rib-knit leg warmers|一对独立筒形袜套，上下均有开口、不带足袋，中性灰小腿模展示踝上堆褶。
脚背延长袜套|instep-extended leg warmers|一对筒形袜套下缘延长覆脚背，足跟与脚尖留开口，完整边缘和灰脚模参照。
''')

block('吊带袜与自持袜结构','''
平口吊带长筒袜|plain-top suspender stockings|一对独立完整长筒袜，上端为无硅胶的平口加固带，旁放一小袜夹成品示意。
蕾丝口吊带长袜|lace-top suspender stockings|一对独立完整长袜，袜口宽蕾丝带可接吊带夹，附小夹扣接点，不画硅胶自持条。
后缝线吊带长袜|back-seam suspender stockings|一对长袜以后侧展示，纵后缝线从袜口到足跟，平口端附吊带夹小图。
对比趾跟吊带袜|contrast-toe-heel suspender stockings|一对薄长袜趾跟深色加固、平口上缘，袜口夹扣与完整足袋可见。
四带吊袜配套|four-strap garter hosiery set|独立产品平铺，腰带连四条吊带及两只完整长襪，每襪前后各一个夹点，附小背面位置图。
六带吊袜配套|six-strap garter hosiery set|独立产品平铺，腰带共六条吊带，两只长袜每只接三夹点，所有夹扣与完整足部清楚。
八带吊袜配套|eight-strap garter hosiery set|独立产品平铺，宽腰带共八条吊带，每只完整长袜有四夹点，不用活人模特。
窄腰带吊带袜套组|narrow-belt suspender hosiery set|独立细腰带、四条窄可调吊带和两只平口长袜组成成品，调节扣与夹端可见。
宽腰带吊带袜套组|wide-belt suspender hosiery set|独立宽软腰带、四条吊带及两只长袜完整平铺，宽腰带上缘和后闭合小图清楚。
交叉后带吊袜套组|cross-back suspender hosiery set|成品以背面平铺示意，四带中的两后带交叉后接两袜后夹点，前带直连，袜子完整。
双硅胶条自持长袜|double-silicone-band stay-up stockings|一对独立长襪内翻一点上口，内侧两条硅胶带清楚，袜口自身固定，无吊袜带。
宽硅胶面自持长袜|wide-silicone-grip stay-up stockings|一对长襪上口内侧一圈宽浅灰硅胶面，一只轻内翻边，完整袜体与足袋。
蕾丝硅胶自持长袜|lace-silicone stay-up stockings|一对长襪上口外面宽原创蕾丝、内侧细硅胶条，小翻口展示内外两层，无吊带。
平滑宽口自持长袜|smooth-wide-top stay-up stockings|一对平滑宽袜口长襪，附内侧防滑条小图，完整足部，上缘不做蕾丝。
吊袜夹扣成品组|finished suspender clip set|四枚完整袜夹与短调节带，展示扣环、橡胶钮和闭合接点，旁有袜口小片，不画人体。
独立调节吊袜腰带|adjustable garter belt product|一件独立成品腰带，四条带、四夹、调节扣和后部闭合清楚，未接袜，属于袜类关联配件。
''')

block('连裤袜与打底袜裤版型','''
标准包足连裤丝袜|standard footed sheer tights|完整连裤袜产品从腰口到两只包足脚尖，细织丝感面，腰部连续，没有独立袜口。
高腰包足连裤袜|high-waist footed tights|完整产品腰口较高且宽，裤身连两腿及包足脚袋，灰中性裤模不显示人体私处。
低腰包足连裤袜|low-rise footed tights|完整产品腰部较低且窄，两腿与两足连续包覆，腰口和臀侧上缘清楚。
宽腰口不透明袜裤|wide-waist opaque tights|完整不透明袜裤，宽平腰边与裤身连成一体，两只包足脚袋完整，不画内衣。
平滑少缝连裤袜|smooth minimal-seam tights|完整袜裤产品裤身表面少缝，腰口与双腿连续，附小腰口接边图，非无缝性能承诺。
加固裤身连裤袜|reinforced-panty tights|完整产品上部织区较密，与腿部细织区有清楚分界，双足包覆，成品平铺无人体。
仿长筒拼区连裤袜|mock-stocking panel tights|完整连裤袜腰至腿连续，上腿薄织、膝上以下深色密织形成仿长袜边，实际没有吊带。
后缝线连裤袜|back-seam tights|完整袜裤以后侧展示，双腿后方纵线延伸至足跟，腰与双足连续包覆。
开趾包跟连裤袜|open-toe footed tights|完整产品腰至腿及足跟连贯，前脚尖为平整开口，附灰脚模脚趾位置小图。
无足连裤袜|footless hosiery tights|完整细织袜裤从腰至踝，双踝开放不带脚袋，腰口与两踝收边清楚。
踩脚连裤袜|stirrup hosiery tights|完整袜裤从腰至踝，双侧脚底各一闭合窄踩脚环，脚跟与脚尖开放，环不可画成鞋。
七分无足袜裤|capri footless hosiery tights|完整袜裤从腰到小腿中段，双裤脚开放，窄收边，附灰腿模位置小图。
不透明贴身打底裤|opaque fitted leggings|完整不透明打底裤，宽腰边、双腿到踝且脚部开放，裤脚不是袜口，普通服装产品。
内绒包足袜裤|fleece-lined footed tights|完整包足袜裤，外面平滑不透明，一处小腰口翻边显示内侧短绒，两脚袋完整。
针织罗纹包足袜裤|rib-knit footed tights|完整不透明针织袜裤，纵罗纹从腰下到足背，腰边与足跟袋清楚。
舞蹈可转换足袋袜裤|convertible-foot dance tights|完整舞蹈袜裤双足袋底部有小可转换开口，附脚底近图，不把开口画在趾端或膝部。
''')

block('网眼花纹与装饰袜','''
细菱网长袜|fine-diamond fishnet stockings|一对长襪有小菱形网眼沿筒与足部转，袜口实织，不是布面印刷格线。
粗菱网长袜|large-diamond fishnet stockings|一对长襪有清楚大菱形开放网眼，袜口与趾端实织，完整袜体。
双层错网长袜|layered-offset mesh stockings|一对长襪两层小网格错位叠合，局部放大显示前后两层，完整足部。
蕾丝织花长袜|lace-knit floral stockings|一对长襪筒面有原创新花枝镂空织纹，足袋连续、上口平整，不复制品牌花纹。
点点薄丝袜|micro-dot sheer hosiery|一对薄长襪上均匀小点，点图案随腿模体积转，袜口和两只足袋清楚。
竖条薄丝袜|vertical-stripe sheer hosiery|一对薄长襪上细竖条从袜口到足背，条纹沿曲面，脚尖完整。
横条针织中筒袜|horizontal-stripe crew socks|一对中筒袜有数条横向配色带，袜口、趾袋、足跟保持完整。
学院菱格长袜|argyle long socks|一对不透明膝下袜，有原创交叠菱格与细斜线，袜口和两足完整。
棋盘格中筒袜|checkerboard crew socks|一对中筒袜筒与足背有黑白棋盘单元，曲面网格转折清楚，趾跟独立。
小心形图案长袜|small-heart motif stockings|一对长襪上稀疏原创小心形图案，足部连续包覆，袜口窄边完整。
星点图案连裤袜|star-motif tights|完整连裤袜产品从腰到双足，原创新星点散布，腰口和裤身连续。
双色左右异色袜|two-color mismatched socks|一对完整中筒袜左右不同色，各自袜口、趾与跟完整，不把两袜连成裤子。
侧边窄缎带长袜|side-ribbon long socks|一对不透明长襪外侧固定窄缎带，小结接在袜筒上缘，不画吊袜腰带。
荷叶袜口长袜|ruffle-top long socks|一对不透明长襪口接一圈短荷叶边，边缘与袜身有实际连接，完整足袋。
闪线混织薄袜|metallic-thread hosiery socks|一对薄中筒襪有少量细亮线混入织面，颜色与织纹连贯，不用整片镜面金属。
双色踝部拼接袜|two-tone ankle-panel socks|一对中筒袜足部与筒部不同色，在踝处清楚拼接线，趾跟完整，普通袜品参考。
''')

# Specific aliases attach only to real constructions.
for e in CATALOG:
    if e['category']!='hosiery':continue
    if '吊带袜' in e['dimension']:
        if 'suspender' in e['en'] or 'garter' in e['en']:e['aliases']+=['吊带袜','吊袜带','吊袜','suspender stockings','garter']
        if 'stay-up' in e['en']:e['aliases']+=['自持袜','硅胶袜','免吊带长袜','hold-ups','stay-ups']
    if e['dimension']=='连裤袜与打底袜裤版型':e['aliases']+=['袜裤','袜裤版型','pantyhose']
    if 'tights' in e['en']:e['aliases']+=['连裤袜','连裤丝袜','tights']
    if 'leggings' in e['en']:e['aliases']+=['打底裤','打底袜裤','leggings']
    if 'fishnet' in e['en']:e['aliases']+=['网袜','渔网袜','fishnet']
