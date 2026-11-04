"""Additional art media and visual-language references."""
from catalog_content import CATALOG, category, add

GROUPS = [
    ('art_comics', '各地漫画与动画表现', '比较不同漫画出版传统和数字动画的线条、色彩与叙事习惯。', [
        ('美式英雄漫画画风', 'American superhero comic', '粗细变化明显的墨线、强对比阴影和鲜明配色突出角色张力。', ['美漫', '超级英雄漫画']),
        ('欧漫清线画风', 'Franco-Belgian clear line comics', '轮廓线均匀清晰，色块平整，画面叙述明快。', ['欧漫', '清线', 'ligne claire']),
        ('韩漫网络漫画画风', 'Korean webtoon illustration', '细致线条与柔和渐变结合，适合数字屏幕阅读。', ['韩漫', '网络漫画', 'webtoon']),
        ('国漫数字动画画风', 'Chinese animation inspired digital art', '以细致轮廓和丰富数字色彩表现角色，是宽泛的国漫视觉参考。', ['国漫', '中国动画', 'guoman']),
    ]),
    ('art_drawing_media', '彩绘与手绘工具', '通过纸面纹理与笔触比较不同传统绘画工具。', [
        ('彩色铅笔画风', 'colored pencil drawing', '以可见的细线与叠色表现明暗，保留纸面的颗粒感。', ['彩铅', '色铅笔']),
        ('水粉画风', 'gouache painting', '不透明而偏哑光的色层和笔触呈现厚实的平面色彩。', ['水粉', 'gouache']),
        ('丙烯画风', 'acrylic painting', '饱和、不透明的颜料层与较明显的笔触塑造形体。', ['丙烯', '亚克力颜料']),
        ('马克笔时装插画', 'marker fashion illustration', '轮廓线结合半透明马克笔叠色，强调迅速概括的造型。', ['马克笔', '手绘时装', 'marker']),
    ]),
    ('art_digital_moods', '数字绘画与氛围', '比较笔触、线稿与光色气氛；氛围可与具体媒介交叉组合。', [
        ('数字厚涂画风', 'painterly digital illustration', '以明显的数字笔触、色块和虚实边缘塑造体积。', ['数字厚涂', 'painterly']),
        ('二次元半厚涂画风', 'semi painted anime illustration', '保留动漫线稿，同时用较细腻的体积和色彩塑造人物。', ['半厚涂', '二次元半厚涂']),
        ('赛博霓虹画风', 'cyberpunk neon illustration', '以冷暖霓虹边光、暗背景和强烈互补色营造未来都市氛围。', ['赛博朋克', '赛博朋克霓虹', '霓虹', 'cyberpunk']),
        ('暗黑奇幻画风', 'dark fantasy illustration', '运用压暗环境、戏剧性明暗和绘画肌理表现奇幻气氛。', ['暗黑幻想', '暗黑奇幻', 'dark fantasy']),
    ]),
    ('art_craft_3d', '写实三维与手作', '比较三维影像、黏土、羊毛毡与钢笔手绘。', [
        ('写实三维渲染画风', 'photorealistic 3D render', '通过真实感材质、体积光和建模细节塑造三维人物。', ['写实3D', '三维渲染', 'CG']),
        ('黏土定格动画画风', 'clay stop motion character', '圆润手塑形体与可见的黏土表面模拟定格动画偶。', ['黏土', '黏土动画', '定格']),
        ('羊毛毡人偶画风', 'felted wool doll', '以纤维、绒毛和手工缝合细节呈现毛毡人偶质感。', ['羊毛毡', '毡偶', '手作人偶']),
        ('钢笔线描画风', 'pen and ink drawing', '以钢笔轮廓和疏密不同的排线组织人物与明暗。', ['钢笔', '线描', 'pen ink']),
    ]),
]

NEW_ENTRIES = []
for cid, name, guide, entries in GROUPS:
    category(cid, name, guide + ' 配图为原创生成的风格示意。', [])
    for title, en, desc, aliases in entries:
        add(cid, name, f'{title}|{en}|{desc}')
        CATALOG[-1].update(added_in='58.0', art_style_reference=True, aliases=aliases,
                           note='近景与全身图均为原创生成的风格示意；媒介、造型和氛围可以交叉组合。')
        NEW_ENTRIES.append(CATALOG[-1])
