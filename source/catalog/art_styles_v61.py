"""Additional rendering approaches and relative pixel-density studies."""
from catalog_content import CATALOG, add

ENTRIES = [
    ('art_game', '像素尺寸对照', '16×16级像素风', '16 by 16 inspired coarse pixel art', '以极少的像素块和色彩概括人物轮廓，模拟16×16级精灵的粗颗粒视觉。', ['16x16','16×16','16像素','粗像素','像素尺寸']),
    ('art_game', '像素尺寸对照', '32×32级像素风', '32 by 32 inspired pixel art', '像素块仍较醒目，可比极粗档表现更多轮廓和简单明暗。', ['32x32','32×32','32像素','像素尺寸']),
    ('art_game', '像素尺寸对照', '64×64级像素风', '64 by 64 inspired pixel art', '以中等密度像素表现五官和分层色块，轮廓保留明显阶梯。', ['64x64','64×64','64像素','像素尺寸']),
    ('art_game', '像素尺寸对照', '128×128级像素风', '128 by 128 inspired fine pixel art', '以较细的像素块组织人物，能容纳更多色阶与局部细节。', ['128x128','128×128','128像素','细像素','像素尺寸']),
    ('art_animation', '动漫与动画画风', '少年漫画墨线画风', 'shonen action manga ink', '粗细变化的墨线、速度感排线和网点营造动作漫画观感。', ['少年漫画','动作漫画','shonen']),
    ('art_animation', '动漫与动画画风', '复古科幻动画画风', 'retro science fiction cel anime', '以复古动画色块、手绘轮廓和科幻城市光色表现角色。', ['复古科幻','科幻动画','ova']),
    ('art_traditional', '传统绘画媒介', '炭笔素描画风', 'charcoal drawing', '深色炭笔、擦抹和纸面粉末形成粗粝的黑白明暗。', ['炭笔','炭画','charcoal']),
    ('art_traditional', '传统绘画媒介', '油画棒绘画画风', 'oil pastel crayon drawing', '蜡质色块和不规则的粗笔触形成明快的手绘质感。', ['油画棒','蜡笔画','oil pastel']),
    ('art_photography', '摄影与写实影像', '舞台追光摄影风格', 'stage spotlight portrait photography', '以暗背景和集中的舞台光塑造明暗对比；摄影效果为生成模拟。', ['舞台追光','聚光灯摄影','spotlight']),
    ('art_photography', '摄影与写实影像', '雨夜电影摄影风格', 'rainy night cinematic photography', '运用夜雨、湿地反射和霓虹光表现电影感；摄影效果为生成模拟。', ['雨夜','雨夜摄影','电影摄影']),
    ('art_graphic', '平面、印刷与拼贴', '波普艺术漫画画风', 'pop art comic halftone', '使用高饱和色块、粗轮廓与印刷网点表现人物。', ['波普','波普艺术','pop art']),
    ('art_graphic', '平面、印刷与拼贴', '装饰艺术海报画风', 'art deco poster illustration', '以几何、对称和金属色装饰构成海报式画面。', ['装饰艺术','装饰派','art deco']),
    ('art_craft_3d', '写实三维与手作', '球体关节人偶画风', 'ball jointed doll character', '以树脂雕塑质感和手肘、膝部等可见关节表现人偶。', ['球体关节人偶','BJD','关节人偶']),
    ('art_craft_3d', '写实三维与手作', '瓷偶釉面画风', 'glazed porcelain doll', '以光滑釉面、反光和精细雕塑轮廓表现瓷偶。', ['瓷偶','瓷娃娃','porcelain doll']),
    ('art_digital_moods', '数字绘画与氛围', '数字水墨插画画风', 'digital ink wash illustration', '以数字笔刷模拟墨色浓淡、洇染和留白。', ['数字水墨','水墨插画','digital ink']),
    ('art_digital_moods', '数字绘画与氛围', '黑白涂鸦线稿画风', 'monochrome doodle sketch', '以随性手绘轮廓、交错排线和局部涂鸦呈现角色。', ['涂鸦','黑白线稿','doodle']),
]
NEW_ENTRIES = []
for cid, dim, name, en, desc, aliases in ENTRIES:
    if dim=='像素尺寸对照': desc += ' 配图为视觉密度示意，并非对应尺寸的原生素材。'
    add(cid, dim, f'{name}|{en}|{desc}')
    note = ('像素图是生成的密度示意，用16、32、64、128级表示由粗到细；图片本身并非对应尺寸的原生像素素材。' if dim=='像素尺寸对照' else
            '近景和全身图为原创生成的风格示意，人物与着装可能不同；摄影效果为生成模拟。')
    CATALOG[-1].update(added_in='61.0', art_style_reference=True, aliases=aliases, note=note,
                       pixel_density_reference=(dim=='像素尺寸对照'))
    NEW_ENTRIES.append(CATALOG[-1])
