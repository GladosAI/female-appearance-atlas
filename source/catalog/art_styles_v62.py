"""Additional comic, illustration, 2.5D and stylized proportion references."""
from catalog_content import CATALOG, add

ENTRIES = [
    ('art_comics','各地漫画与动画表现','彩色平涂漫画画风','flat color comic illustration','清晰墨线和均匀色块构成漫画画面，阴影层次简洁。',['平涂漫画','彩色漫画','平涂']),
    ('art_digital_moods','数字绘画与氛围','韩式幻想厚涂画风','Korean fantasy painterly illustration','柔和厚涂笔触与丰富光色结合，表现韩式幻想角色插画。',['韩式幻想厚涂','韩式厚涂','幻想厚涂']),
    ('art_digital_moods','数字绘画与氛围','暗黑哥特手绘画风','dark gothic hand drawn illustration','以手绘线条、压暗色彩和装饰细节营造哥特氛围。',['暗黑哥特手绘','哥特手绘','dark gothic']),
    ('art_graphic','平面、印刷与拼贴','暖色绘本插画画风','warm storybook illustration','柔软笔触、手工纸感和概括形状共同形成温暖绘本观感。',['绘本插画','童话绘本','storybook']),
    ('art_traditional','传统绘画媒介','水彩绘本插画画风','watercolor picture book illustration','以透明水彩、纸面和留白组织人物故事插画。',['水彩绘本','水彩插画','picture book']),
    ('art_graphic','平面、印刷与拼贴','颗粒肌理插画画风','grain textured editorial illustration','概括色块叠加颗粒纹理，形成平面编辑插画效果。',['颗粒插画','肌理插画','editorial illustration']),
    ('art_comics','各地漫画与动画表现','复古报刊连环漫画','vintage newspaper comic strip','清晰线稿、有限套色和旧报纸纹理形成连环漫画效果。',['报刊漫画','连环漫画','comic strip']),
    ('art_comics','各地漫画与动画表现','黑白笔触漫画画风','black and white brush manga','以浓淡变化的手绘黑墨笔触和排线塑造漫画人物。',['黑白笔触漫画','笔刷漫画','brush manga']),
    ('art_game','2.5D视觉表现','2.5D水彩游戏立绘','2.5D watercolor game character','人物保留三维体积感，同时呈现透明水彩和纸面纹理。',['2.5D水彩','水彩游戏立绘']),
    ('art_game','2.5D视觉表现','2.5D像素三维融合','2.5D pixel art with 3D lighting','用明显像素块表现表面，并以立体光照组织画面。',['2.5D像素','像素三维','pixel 3D']),
    ('art_game','2.5D视觉表现','2.5D分层剪纸画风','2.5D layered paper game art','以可见纸张层次和投影表达角色形状与画面纵深。',['2.5D剪纸','分层剪纸','纸片立体']),
    ('art_game','2.5D视觉表现','2.5D奇幻角色立绘','2.5D fantasy character key art','动漫化造型结合细致材质与柔和立体光影，形成奇幻角色立绘。',['2.5D奇幻','奇幻游戏立绘']),
    ('art_animation','头身比画风','约两头身成人Q版','two head tall adult chibi proportions','头部明显放大，躯干与四肢压缩为约两头身的成人角色Q版形态。',['两头身','2头身','二头身','Q版头身']),
    ('art_animation','头身比画风','约三头身成人卡通','three head tall adult cartoon proportions','保留较大的头部与简化身体，整体约三头身。',['三头身','3头身','Q版头身']),
    ('art_animation','头身比画风','约五头身风格化角色','five head tall stylized proportions','头部相对突出但四肢比Q版更舒展，整体约五头身。',['五头身','5头身','风格化头身']),
    ('art_animation','头身比画风','约八头身写实角色','eight head tall realistic character proportions','头部相对较小、四肢较修长，以约八头身表示理想化写实比例。',['八头身','8头身','写实头身']),
]
NEW_ENTRIES = []
for cid, dim, name, en, desc, aliases in ENTRIES:
    add(cid, dim, f'{name}|{en}|{desc}')
    note = ('图例为风格化成年角色的近似头身对比，不是人体发育或年龄标准；Q版头身在全身图中更直观。' if dim=='头身比画风' else
            '近景与全身图为原创生成的视觉示意，人物和着装可能不同；可与媒介、配色和造型交叉组合。')
    CATALOG[-1].update(added_in='62.0', art_style_reference=True, aliases=aliases,
                       head_proportion_reference=(dim=='头身比画风'), note=note)
    NEW_ENTRIES.append(CATALOG[-1])
