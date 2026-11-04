"""Requested specific visual looks, appended to existing art categories."""
from catalog_content import CATALOG, add

ENTRIES = [
    ('art_photography', '摄影与写实影像', '日韩杂志画报', 'Japanese Korean fashion magazine editorial', '以精致时尚造型、棚拍布光和杂志画报构图呈现角色；示例为生成的摄影模拟。', ['日韩', '日杂', '韩杂', '杂志画报']),
    ('art_photography', '摄影与写实影像', '复古胶片写真', 'vintage color film photography', '以暖调褪色、柔和反差和可见颗粒模拟彩色胶片，区别于即时成像边框。', ['复古胶片', '胶片写真', '35mm', '胶卷']),
    ('art_game', '游戏与数字角色画风', '2.5D游戏原画立绘', '2.5D game character key art', '结合动漫化五官与丰富体积塑造、材质光影，呈现二维插画和三维感之间的视觉效果。', ['2.5D', '2.5d游戏', '游戏原画立绘']),
    ('art_animation', '动漫与动画画风', '日系二次元插画', 'Japanese anime illustration', '以日式动漫人物比例、清晰线条和丰富上色呈现角色插画。', ['日系', '二次元', '日系插画']),
    ('art_animation', '动漫与动画画风', '新海诚感动画电影', 'atmospheric Japanese animated film inspired lighting', '用通透天空、层次云彩与逆光表现抒情动画电影氛围；为原创视觉特征示意。', ['新海诚', '动画电影', '天空', '电影光影']),
    ('art_craft_3d', '写实三维与手作', '3D次世代角色渲染', 'next generation 3D game character render', '强调细致几何、肤质和服装材质的实时游戏角色渲染观感。', ['3D次世代', '次世代', '次世代游戏']),
    ('art_craft_3d', '写实三维与手作', '3D潮玩手办质感', '3D designer collectible vinyl figure', '用塑胶高光、雕塑轮廓和玩具比例表现潮玩手办。', ['潮玩', '手办', '玩具质感', 'vinyl toy']),
    ('art_game', '游戏与数字角色画风', '角色设定集立绘·纯白底', 'character design sheet illustration white background', '以纯白背景和清晰轮廓展示角色的服装与整体造型，强调设定集立绘的可读性。', ['角色设定集立绘', '角色设定集立绘（纯白底）', '角色设定集立绘(纯白底)', '纯白底', '白底立绘', '角色设定集']),
]
NEW_ENTRIES = []
for cid, dimension, name, en, desc, aliases in ENTRIES:
    add(cid, dimension, f'{name}|{en}|{desc}')
    CATALOG[-1].update(added_in='59.0', art_style_reference=True, aliases=aliases,
                       note='近景与全身图为原创生成的表现示意，人物、服装和构图并非同一角色的严格转面；摄影效果为模拟影像。')
    NEW_ENTRIES.append(CATALOG[-1])
