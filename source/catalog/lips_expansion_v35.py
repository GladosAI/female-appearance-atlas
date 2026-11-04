"""V35: lip morphology, cosmetic color/finish and lip-edge techniques."""
from catalog_content import CATALOG,category,add

NEW_CATEGORIES=['lips','lip_makeup']
category('lips','嘴唇形态与轮廓','16项自然唇形近景，分别比较上下唇厚薄、唇峰唇珠、横向宽度、嘴角与侧面轮廓。中性闭唇减少表情干扰，形态是可组合的绘画特征。',['R03'])
category('lip_makeup','唇妆与唇色','32项上唇妆后的近景，按唇色与表面质感、唇线边界与画法两组浏览；与自然唇形、唇齿动作及完整面妆分开记录。',['R108','R109'])

def block(cid,dimension,text):
    start=len(CATALOG);add(cid,dimension,text)
    assert len(CATALOG)-start==16
    for entry in CATALOG[start:]:
        entry.update(added_in='35.0',lip_reference=True,adult_only=True,minor_reference=False,age_min=25,
            aliases=['嘴唇','唇部','lip','lips']+(['唇形','嘴型'] if cid=='lips' else ['唇妆','口红','lip makeup','lipstick']),
            note='原创成年角色唇部绘画参考。观察可见轮廓、唇峰唇珠、上下唇关系或妆面落色与反光；不将形态标签作为唯一审美标准。唇妆改变可见边界与色泽，结构、表情和光照仍需分别设定。')

block('lips','自然唇形与正侧面轮廓','''
均衡中等厚唇|balanced medium lips|正面中性闭唇，上下唇厚度接近，下唇稍饱满，唇峰弧度适中，作为本页基准。
上下轻薄唇|thin upper and lower lips|正面中性闭唇，上下唇红区域均较窄，闭口线清楚，宽度与基准接近。
上下饱满唇|full upper and lower lips|正面中性闭唇，上下唇红区域都较厚且圆润，保留自然唇缘和唇峰。
上薄下丰唇|thin upper full lower lip|正面中性闭唇，上唇明显轻薄，下唇中央厚实，形成清楚的上下厚度差。
上丰下薄唇|full upper thin lower lip|正面中性闭唇，上唇红区域更厚，下唇偏窄，上下比例与上一项相反。
清晰双峰弓唇|defined cupid-bow lips|正面中性闭唇，上唇双峰清楚，中间V形凹口明确，唇缘边界利落。
圆弧柔峰唇|soft rounded cupid-bow lips|正面中性闭唇，上唇双峰转折圆缓，中间凹口浅，形成柔和连续弧线。
平缓上缘唇|flat upper-lip outline|正面中性闭唇，上唇顶部较平，双峰与中央凹口都不明显，下唇弧线自然。
中央唇珠明显唇|prominent central lip tubercle|正面中性闭唇，上唇中央有小而清楚的圆润唇珠，闭口线中央轻轻向下弯。
横向舒展宽唇|wide horizontal lips|正面中性闭唇，嘴角间距明显宽于基准，唇厚中等，不能用微笑拉宽来代替。
小口紧凑唇|compact narrow lips|正面中性闭唇，嘴角间距较窄，唇缘集中在中央，厚度中等，表情不撅嘴。
自然微翘嘴角唇|naturally upturned lip corners|正面静止闭唇，嘴角末端轻轻上翘，脸颊保持放松，区别于主动微笑。
自然微垂嘴角唇|naturally downturned lip corners|正面静止闭唇，嘴角末端略向下，眉眼不参与，不将轮廓画成悲伤表情。
侧面浅凸唇|subtle-projection lips in profile|严格侧面中性闭唇，鼻底到下巴完整入画，上下唇体积较浅，唇尖轻微前凸。
侧面圆润丰唇|rounded full lips in profile|严格侧面中性闭唇，鼻底到下巴完整入画，上下唇均圆润向前，侧面体积清楚。
侧面下唇略前唇|lower-lip-forward profile|严格侧面中性闭唇，鼻底到下巴完整入画，下唇轻微超过上唇前缘，轮廓自然克制。
''')
block('lip_makeup','唇色与表面质感','''
裸米杏缎光唇|beige-apricot satin lips|正面中等唇形均匀涂裸米杏色，反光柔和，唇缘清楚，保留细微唇纹。
玫瑰豆沙柔雾唇|dusty-rose soft-matte lips|正面中等唇形为低饱和玫瑰豆沙色，表面细腻柔雾，无镜面亮斑。
蜜桃珊瑚水润唇|peach-coral dewy lips|正面中等唇形为暖蜜桃珊瑚色，有薄薄水润光泽与自然透色感。
冷调莓粉亮泽唇|cool berry-pink glossy lips|正面中等唇形为冷调莓粉色，下唇有清楚亮泽反射，保持粉紫底色。
经典正红丝绒唇|classic red velvet lips|正面中等唇形均匀正红，覆盖完整，表面呈细腻丝绒哑光，边缘清楚。
砖红陶土哑光唇|terracotta brick-red matte lips|正面中等唇形为带橘棕调的砖红陶土色，哑光饱和覆盖，区别于纯正红。
焦糖肉桂棕唇|caramel-cinnamon brown lips|正面中等唇形为温暖肉桂焦糖棕，柔和缎光，不变成深巧克力色。
深梅紫浆果唇|deep plum-berry lips|正面中等唇形为深梅紫与莓果色，唇峰与边界清楚，缎光反射克制。
透明裸色润唇|clear natural lip sheen|正面自然粉棕唇，仅覆透明薄亮泽，保留原本唇色、唇纹与边缘。
柔雾漫反射唇|soft-matte lip finish|与后续质感对照使用相同玫瑰红色和相同唇形，表面均匀柔雾，没有高亮反光点。
奶油缎光质感唇|creamy satin lip finish|相同玫瑰红色与唇形，下唇有宽而柔的微光反射，介于哑光和明显亮泽之间。
镜面唇釉质感唇|mirror-gloss lip lacquer|相同玫瑰红色与唇形，表面有清晰条状镜面反射，亮度集中而边缘锐利。
透明果冻质感唇|translucent jelly lip finish|相同玫瑰红色与唇形，唇色更透，呈薄透果冻光泽，可隐约看出自然唇纹。
细珠光珍珠唇|fine pearlescent lip finish|相同玫瑰红色与唇形，表面有细密柔和珠光，形成均匀珍珠光感而非大颗闪片。
金属箔光质感唇|metallic foil lip finish|相同玫瑰红色与唇形，出现连续金属反光带，偏玫瑰铜色，区别于水亮唇釉。
微闪亮片点缀唇|micro-glitter accented lips|相同玫瑰红色与唇形，少量微小亮片分散在唇面，单个反光点可辨，唇缘干净。
''')
block('lip_makeup','唇线边界与画法','''
顺原唇缘全涂|true-outline full lip fill|正面闭唇，玫瑰红色均匀覆盖自然唇红区，唇线与原边缘重合，双峰清楚。
柔焦晕边唇妆|soft blurred lip edge|正面闭唇，玫瑰红色由中央向唇缘轻柔晕开，唇缘与肤色之间没有清晰硬线。
内深外浅渐变唇妆|inner-dark gradient lips|正面微留细缝，深莓红集中在内侧口缝，向外唇缘逐渐变成浅粉。
外深内浅渐变唇妆|outer-dark ombre lips|正面闭唇，深棕红围绕外唇缘，中央浅裸粉，深浅连续过渡，区别于内深渐变。
唇线笔同色勾边|matching lip-liner definition|正面闭唇，红棕色细唇线沿原唇缘描出，内侧填同色，边缘更利落。
深唇线浅唇色|dark liner with lighter center|正面闭唇，深巧克力棕细线围住唇缘，内侧为浅米裸唇色，留有明确色差。
中央局部轻扩唇|central subtle overlining|正面闭唇，仅上唇弓中央和下唇中央略超出自然边缘着色，嘴角保持原位，幅度克制。
内收缩小唇缘|inset reduced lip border|正面闭唇，自然唇缘外圈被近肤色轻柔弱化，红色可见边缘向内收，嘴宽适当缩小。
圆化唇峰画法|rounded cupid-bow makeup|正面闭唇，以柔玫瑰色填浅上唇双峰之间的凹口，形成较圆的上唇弧。
强调双峰唇线|sharpened cupid-bow liner|正面闭唇，正红唇线上缘强调两个清晰尖峰与中央V口，下唇弧线完整。
上深下浅双色唇|dark-upper light-lower lips|正面闭唇，上唇深莓紫、下唇浅玫瑰粉，上下唇色块分明，形态不改变。
左右拼色创意唇|left-right split-color lips|正面闭唇，左半边珊瑚红、右半边冷莓紫，中央竖向分界清楚，上下两唇保持同侧配色。
下唇中央点亮|lower-lip center gloss accent|正面闭唇，整体柔雾玫瑰色，只在下唇中央加小范围透明亮泽，其他唇面保持哑光。
薄透染色唇妆|sheer stained-lip makeup|正面闭唇，浅莓色像薄层染色贴在唇面，细纹和底色可见，无厚涂边界与大反光。
浅色珠光覆涂|pearlescent topcoat lips|正面闭唇，裸粉底色上叠浅香槟珠光，中央反光略强、边缘仍保留粉色底色。
深肤暖棕唇线组合|warm-brown lip combo on deep skin|深棕肤色成年正面近景，深暖棕唇线、较浅焦糖中央与薄亮泽层自然衔接。
''')

LIP_ALIASES={
    'defined cupid-bow lips':['M形唇','M唇','弓形唇'],
    'soft rounded cupid-bow lips':['圆润花瓣唇'],
    'full upper and lower lips':['厚唇','丰唇'],
    'thin upper and lower lips':['薄唇'],
    'compact narrow lips':['小口唇形','樱桃小口'],
    'prominent central lip tubercle':['唇珠'],
    'inner-dark gradient lips':['咬唇妆','内渐变唇'],
    'outer-dark ombre lips':['外渐变唇','ombre lips'],
    'mirror-gloss lip lacquer':['镜面唇釉','玻璃唇'],
    'translucent jelly lip finish':['果冻唇'],
    'dark liner with lighter center':['深色唇线','浅色唇心'],
}
for entry in CATALOG:
    if entry.get('lip_reference'):entry['aliases']+=LIP_ALIASES.get(entry['en'],[])

def reclassify_gaze_and_laughter(entries,categories):
    """Move published EX entries after identifier assignment so saved cards remain valid."""
    cats={c['id']:c for c in categories}
    for entry in entries:
        if entry.get('beauty_kind')=='gaze_laugh':
            entry['category']='face_emotions'
            entry['category_name']=cats['face_emotions']['name']
