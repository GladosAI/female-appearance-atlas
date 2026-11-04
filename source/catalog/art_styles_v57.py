"""Art rendering references: media and visual language, not clothing styles."""
from catalog_content import CATALOG, category, add

GROUPS = [
    ('art_animation', '动漫与动画画风', '动画、漫画式线条和上色；观察轮廓、色块与人物比例。', [
        ('赛璐璐动画上色', 'cel shading', '清晰轮廓配合少量边界明确的平涂阴影，强调动画色块。', ['赛璐璐', '赛璐璐上色', 'cel']),
        ('复古赛璐珞动画', 'retro hand painted cel animation', '柔和旧片色调与颗粒质感，模拟手绘动画胶片的观感。', ['复古动画', '90年代动画']),
        ('轻小说插画画风', 'light novel illustration', '细致线稿、层叠亮部与柔和渐变，强调出版插画的精致光感。', ['轻小说', '轻小说插画']),
        ('Q版动漫画风', 'chibi anime', '放大头身比例并简化五官与形体，以清晰轮廓突出可爱感。', ['Q版', 'SD', '二头身']),
    ]),
    ('art_game', '游戏与数字角色画风', '比较像素、三维角色、原画和立绘的造型语言。', [
        ('像素游戏画风', 'pixel art game', '以可辨认的方形像素、阶梯边缘和有限色板组织人物。', ['像素', '点阵', '像素画', 'pixel art']),
        ('风格化三维游戏角色', 'stylized 3d game character', '立体建模感明显，形体适度概括，材质与光照具有体积感。', ['3D', '三维', '游戏建模']),
        ('游戏概念原画', 'painterly game concept art', '笔触、虚实边缘和整体明暗服务于角色设计与氛围设定。', ['游戏原画', '概念设计', 'concept art']),
        ('视觉小说角色立绘', 'visual novel character sprite', '人物正面或近正面、轮廓清楚，适合表情与姿态差分。', ['视觉小说', 'galgame', '立绘']),
    ]),
    ('art_photography', '摄影与写实影像', '以摄影光线、黑白、棚拍和即时成像区分影像观感。配图均为生成的模拟摄影效果。', [
        ('自然光写真人像', 'natural light portrait photography', '以窗边柔光、肤色层次和自然镜头景深模拟人像写真。', ['写实', '写真', '摄影', '人像摄影', '写真人像写真', '写实人像写真']),
        ('黑白胶片写真', 'black and white film portrait', '以黑白灰影调和颗粒组织形象，去除色彩信息。', ['黑白摄影', '胶片', '黑白写真']),
        ('时尚棚拍写真', 'studio fashion photography', '使用简洁背景与可控制的柔光，突出脸部轮廓和造型。', ['棚拍', '时尚摄影', '影棚写真']),
        ('即时成像写真', 'instant film portrait', '低反差、偏暖的褪色调和轻微颗粒模拟即时成像照片。', ['拍立得', '即时成像', '宝丽来']),
    ]),
    ('art_traditional', '传统绘画媒介', '以水彩、油画、素描和水墨比较材料肌理与笔触。', [
        ('水彩绘画画风', 'watercolor painting', '透明色层、水渍边缘和纸面纹理共同塑造人物。', ['水彩', '水彩画']),
        ('厚涂油画画风', 'impasto oil painting', '不透明色层与可见厚笔触，呈现画布与颜料质感。', ['油画', '厚涂', '油彩']),
        ('石墨素描画风', 'graphite pencil drawing', '以铅笔线条、灰阶和排线表现形体与明暗。', ['素描', '铅笔画', '石墨']),
        ('中国水墨人物画', 'Chinese ink wash portrait', '通过墨色浓淡、笔锋和留白表现人物，并保留纸面感。', ['水墨', '国画', '墨画']),
    ]),
    ('art_graphic', '平面、印刷与拼贴', '比较矢量色块、网点、版画线条和纸张拼贴。', [
        ('扁平矢量插画', 'flat vector illustration', '形状边缘清楚，以概括色块和有限色板构成面部。', ['矢量', '扁平', 'vector']),
        ('丝网印刷画风', 'screen print illustration', '有限套色叠印，色块与印刷网点呈现海报质感。', ['丝网印刷', '丝印', '网点']),
        ('木刻版画画风', 'woodcut engraving', '以黑白反差和刻线、排线模拟木刻版印效果。', ['木刻', '版画', '雕版']),
        ('剪纸拼贴画风', 'torn paper collage', '用可见的纸片边缘和分层色纸形状拼出人物。', ['拼贴', '剪纸', '纸艺']),
    ]),
    ('art_mixed', '漫画、干画与实验数字画', '观察网点、粉彩、喷绘和多边形等不同图像语言。', [
        ('粉彩绘画画风', 'pastel chalk illustration', '干性粉笔的柔软颗粒、擦抹痕与纸面底色共同构成画面。', ['粉彩', '粉笔画', '色粉']),
        ('黑白漫画网点画风', 'black and white manga screentone', '黑色线稿结合密度不同的网点表达灰阶和阴影。', ['漫画', '网点纸', '黑白漫画', '日式黑白漫画网点']),
        ('数字喷绘画风', 'digital airbrush painting', '边缘柔和的连续渐变与细腻光晕模拟喷枪和数字喷绘。', ['喷绘', '喷枪', 'airbrush']),
        ('低多边形三维画风', 'low poly 3d', '由明显的三角形平面构成面部与头发，保留分面轮廓。', ['低多边形', 'low poly', '低模']),
    ]),
]

NEW_ENTRIES = []
for cid, name, guide, entries in GROUPS:
    category(cid, name, guide + ' 图例是原创生成的风格示意，摄影类并非真实拍摄。', [])
    for title, en, desc, aliases in entries:
        add(cid, name, f'{title}|{en}|{desc}')
        CATALOG[-1].update(added_in='57.0', art_style_reference=True, aliases=aliases,
                           note='以同类人像构图示意表现手法；实际风格可以交叉组合，摄影类图例是生成的模拟影像。')
        NEW_ENTRIES.append(CATALOG[-1])
