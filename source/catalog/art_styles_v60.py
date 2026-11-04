"""Additional distinct art styles across animation, art media, and photography."""
from catalog_content import CATALOG, add

ENTRIES = [
    ('art_animation', '动漫与动画画风', '复古少女漫画画风', 'vintage shojo manga', '纤细线条、醒目睫毛、网点和花卉装饰突出浪漫漫画感。', ['少女漫画', '少女漫', 'shojo']),
    ('art_animation', '动漫与动画画风', '欧美二维卡通画风', 'western 2D cartoon', '以夸张表情、简化造型和清晰粗线表现二维动画角色。', ['欧美卡通', '二维卡通', '西方动画']),
    ('art_game', '游戏与数字角色画风', '单色一位像素画风', '1-bit monochrome pixel art', '只使用黑白像素和棋盘式抖动表达轮廓与灰阶。', ['1bit', '1-bit', '黑白像素', '单色像素']),
    ('art_craft_3d', '写实三维与手作', '三维赛璐璐渲染', '3D cel shaded toon rendering', '三维体积结合清晰的分层阴影和卡通轮廓线。', ['卡通渲染', '三渲二', 'toon shading', '3D赛璐璐']),
    ('art_traditional', '传统绘画媒介', '工笔重彩人物画', 'Chinese gongbi painting', '细致勾线与层叠设色构成工整人物画，保留绢纸质感。', ['工笔', '重彩', '工笔人物']),
    ('art_traditional', '传统绘画媒介', '浮世绘木版画风', 'ukiyo-e woodblock illustration', '平面设色、轮廓线及纸张和木版纹理形成版画观感。', ['浮世绘', '日本木版画', 'ukiyoe']),
    ('art_traditional', '传统绘画媒介', '印象派绘画画风', 'impressionist painting', '以短促松散笔触、邻近色和自然光变化塑造人物。', ['印象派', '印象主义', 'impressionism']),
    ('art_graphic', '平面、印刷与拼贴', '新艺术装饰画风', 'art nouveau illustration', '流动的植物曲线、装饰边框与柔和珠宝色构成画面。', ['新艺术', '新艺术运动', 'art nouveau']),
    ('art_photography', '摄影与写实影像', '黑色电影摄影风格', 'film noir portrait photography', '以黑白、强烈侧光和深暗阴影营造戏剧性影像；示例为生成模拟。', ['黑色电影', '黑色电影摄影', 'film noir']),
    ('art_photography', '摄影与写实影像', '街头时尚摄影风格', 'street fashion editorial photography', '以城市街景、自然光和抓拍感表现人物穿搭；示例为生成模拟。', ['街拍', '街头时尚摄影', 'street style']),
    ('art_photography', '摄影与写实影像', '柔焦梦幻写真风格', 'dreamy soft focus photography', '柔和低反差、散射光与轻微朦胧感构成梦幻影像；示例为生成模拟。', ['柔焦', '梦幻写真', 'soft focus']),
    ('art_photography', '摄影与写实影像', '红外伪彩摄影风格', 'false color infrared photography', '以非自然色彩与浅色或红色植被模拟红外伪彩影像；示例为生成模拟。', ['红外摄影', '红外伪彩', 'infrared']),
    ('art_game', '游戏与数字角色画风', '体素角色画风', 'voxel character art', '以可见的立方体积木构成三维人物和阶梯状轮廓。', ['体素', '方块角色', 'voxel']),
    ('art_graphic', '平面、印刷与拼贴', '彩绘玻璃画风', 'stained glass illustration', '用铅条轮廓将彩色半透明玻璃片分隔成装饰性图像。', ['彩绘玻璃', '教堂玻璃', 'stained glass']),
    ('art_drawing_media', '彩绘与手绘工具', '蓝色圆珠笔画风', 'blue ballpoint pen drawing', '以蓝色圆珠笔的细线和多层排线表现人物明暗。', ['圆珠笔', '蓝色圆珠笔', 'ballpoint']),
    ('art_animation', '动漫与动画画风', '欧美三维动画电影画风', 'western stylized 3D animation film', '以夸张面部比例和圆润的三维材质表现动画电影角色。', ['欧美动画电影', '三维动画电影', '3D动画电影']),
]
NEW_ENTRIES = []
for cid, dimension, name, en, desc, aliases in ENTRIES:
    add(cid, dimension, f'{name}|{en}|{desc}')
    CATALOG[-1].update(added_in='60.0', art_style_reference=True, aliases=aliases,
                       note='近景和全身图为原创生成的风格示意，人物与着装可能存在差异；摄影效果为生成模拟。')
    NEW_ENTRIES.append(CATALOG[-1])
