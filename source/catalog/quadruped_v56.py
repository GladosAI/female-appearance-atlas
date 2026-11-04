"""Complete animal bodies with four grounded feet; distinct from upright anthro."""
from catalog_content import CATALOG, category, add

CID = 'quadruped_forms'
NEW_ENTRIES = []
category(CID, '完全动物体态与四足装饰',
         '完整动物头颈、横向躯干与四条动物腿，四足着地，仅增加帽子、发结、领巾或短披饰；不含人形上身、人手或直立人形骨盆。与双足福瑞及半人马分别浏览。', ['R69'])

for name, en, kind, description in [
    ('四足小马·牛仔帽与领巾', 'quadrupedal pony with western hat and scarf', 'pony',
     '浅褐小马保留完整马头、横向马躯、深棕鬃尾和四条马腿，四只蹄分开着地；仅戴棕色牛仔帽与蓝色小领巾'),
    ('四足小马·鬃结与短披饰', 'quadrupedal pony with mane bow and short capelet', 'pony',
     '奶油色小马保留完整马头、横向马躯、栗色波浪鬃尾和四条马腿，四只蹄着地；鬃毛系小蝶结，肩背有不遮腿的紫色短披饰'),
    ('四足狐狸·领巾装饰', 'quadrupedal fox with neck bandana', 'fox',
     '赤褐狐狸保留自然长吻、横向躯干、蓬松白尖尾和四条动物腿，四只爪足分别着地；仅在颈部系青色领巾'),
    ('四足猫·颈部缎带结', 'quadrupedal cat with neck ribbon bow', 'cat',
     '灰色虎斑猫保留猫头、横向猫躯、弯曲长尾与四条猫腿，四只爪足清楚着地；颈部仅有酒红缎带结')
]:
    add(CID, '完整动物体态·四足着地', f'{name}|{en}|{description}。')
    CATALOG[-1].update(
        added_in='56.0', quadruped_reference=True, animal_body_plan='complete_quadruped',
        stance='four_feet_grounded', body_orientation='horizontal_animal_trunk', species_reference=kind,
        human_upper_body=False, human_hands=False, anthro_reference=True,
        aliases=['四足', '四脚', '四脚着地', '完全动物形态', '完全动物体态', '动物装饰', '福瑞', 'furry', 'quadruped'] + (['小马', '马形'] if kind == 'pony' else []),
        note='原创四足动物幻想角色外观示意。只复用完整动物体态、四足支撑和少量装饰，不是任何原作角色的官方造型，不据此推定原角色物种细节、配色、年龄或性格。此类别独立于原有L1—L8双足对照，不修改原档位含义。')
    NEW_ENTRIES.append(CATALOG[-1])
