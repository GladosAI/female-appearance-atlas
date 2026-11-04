"""Build the expanded fully illustrated edition; partial previews are separate files."""
import sys
from pathlib import Path
sys.pycache_prefix = str(Path(__file__).resolve().parents[2] / '.work/cache/python')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path
from collections import Counter
import copy,json,struct,zipfile,sys
from theme_palettes import apply_theme_palettes
from brand_assets import apply_brand_assets
from image_exports import prepare_image_exports
from project_data import contribution_data, assign_ids, write_json, export_collaboration_data
from catalog_content import CATALOG,CATEGORIES
import expansion_content
import clothing_expansion
import fashion_expansion
import coverage_expansion
import wardrobe_expansion
import era_style_expansion
import hood_hair_expansion
import personal_expansion
import youth_sleep_expansion
import wrist_foot_print_expansion
import cosplay_expansion
import facial_expansion
import hosiery_expansion
import anthro_expansion
import seasonal_expansion
import trend_model_expansion
import wedding_expansion
import costume_hair_expansion
import special_age_expansion
import nun_states_growth_expansion
import life_stage_comparison
import body_stage_cover_expansion
import magical_ninja_expansion
import body_dimensions_expansion
import diverse_roles_expansion
import pose_expansion
import accessory_hairstyle_expansion
import anime_hairtie_expansion
import headphone_expansion
import eye_makeup_expansion
import beauty_expansion_v34
import lips_expansion_v35
import intimate_expansion_v36
import seated_pose_expansion_v37
import fashion_history_v38
import fashion_history_v39
import superhero_expansion_v40
import chinese_fantasy_v41
import hybrid_forms_v42
import details_lighting_v43
import wardrobe_parts_v44
import persona_looks_v45
import persona_looks_v46
import role_style_v47
import presence_gesture_v48
import persona_v49
import persona_v50
import identity_v51
import identity_flex_v52
import scholar_myth_v53
import pose_v54
import photo_poses_v55
import quadruped_v56
import art_styles_v57
import art_styles_v58
import art_styles_v59
import art_styles_v60
import art_styles_v61
import art_styles_v62
import costume_combinations_v63
import costume_combinations_v64
import hair_comparison_v65
from fashion_facets import apply_facets,SHOULDERS
from fashion_docs import write_fashion_docs
from cosplay_docs import COSPLAY_COMBINATIONS,write_cosplay_docs
from facial_docs import write_facial_docs
from latest_docs import write_latest_docs
from anthro_docs import write_anthro_docs
from seasonal_docs import write_seasonal_docs
from layout_docs import finalize_docs
from navigation_v32_docs import build_navigation, write_navigation_docs
from project_readme import write_usage_readme
from camera_docs import write_camera_docs
from visual_narrative_docs import write_visual_narrative_docs
from game_design_docs import write_game_design_docs
from rights_docs import write_rights_docs
from system_examples import prepare_system_examples, example_coverage, write_example_docs
from trend_model_docs import write_trend_model_docs
from wedding_docs import write_wedding_docs
from costume_hair_docs import write_costume_hair_docs
from special_age_docs import write_special_age_docs
from nun_states_growth_docs import write_nun_states_growth_docs
from life_comparison_docs import write_life_comparison_docs
from body_stage_cover_docs import write_body_stage_cover_docs
from magical_ninja_docs import write_magical_ninja_docs
from body_dimensions_docs import write_body_dimensions_docs
from diverse_roles_docs import write_diverse_roles_docs
from pose_docs import write_pose_docs
from accessory_hairstyle_docs import write_accessory_hairstyle_docs
from wearing_reference_docs import write_wearing_reference_docs
from headphone_docs import write_headphone_docs
from eye_makeup_docs import write_eye_makeup_docs
from beauty_v34_docs import write_beauty_v34_docs
from lips_v35_docs import write_lips_v35_docs
from intimate_v36_docs import write_intimate_v36_docs
from history_v38_docs import write_history_v38_docs
from superhero_v40_docs import write_superhero_v40_docs
from chinese_fantasy_v41_docs import write_chinese_fantasy_v41_docs
from hybrid_v42_docs import write_hybrid_v42_docs
from details_v43_docs import write_details_v43_docs
from wardrobe_v44_docs import write_wardrobe_v44_docs
from persona_v45_docs import write_persona_v45_docs
from role_style_v47_docs import write_role_style_v47_docs
from presence_gesture_v48_docs import write_presence_gesture_v48_docs
from persona_v49_docs import write_persona_v49_docs
from persona_v50_docs import write_persona_v50_docs
from identity_v51_docs import write_identity_v51_docs
from identity_flex_v52_docs import write_identity_flex_v52_docs
from scholar_myth_v53_docs import write_scholar_myth_v53_docs
from pose_v54_docs import write_pose_v54_docs
from photo_poses_v55_docs import write_photo_poses_v55_docs
from quadruped_v56_docs import write_quadruped_v56_docs
from costume_comparison_v63_docs import write_costume_comparison_v63_docs
from costume_comparison_v64_docs import write_costume_comparison_v64_docs
from hair_comparison_v65_docs import write_hair_comparison_v65_docs
from catalog_layout import PREFIX,CLOTHING_CATEGORIES

ROOT = _bootstrap.ROOT

def build(partial=False, package=True, image_exports=True, check_assets=True):
    categories=copy.deepcopy(CATEGORIES);entries=copy.deepcopy(CATALOG);counts=Counter()
    category_extensions_path=ROOT/'source/category-extensions.json'
    category_extensions=json.loads(category_extensions_path.read_text(encoding='utf-8')) if category_extensions_path.exists() else []
    prefixes=list(PREFIX)
    for category_extension in category_extensions:
        category_extension=copy.deepcopy(category_extension);prefix=category_extension.pop('prefix')
        if category_extension['id'] in {category['id'] for category in categories} or prefix in prefixes:
            raise ValueError('Category extension reuses an existing ID or prefix')
        categories.append(category_extension);prefixes.append(prefix)
    cats={c['id']:c for c in categories}
    contributions=contribution_data(ROOT)
    if contributions['categories']:
        raise ValueError('New categories need a reviewed source/category-extensions.json and navigation change.')
    entries.extend(contributions['entries'])
    registry=assign_ids(ROOT,entries,categories,prefixes)
    for e in entries:
        k=e['category'];counts[k]+=1;e.setdefault('origin','editorial')
        if e.get('anime_hairtie_reference'):e['anime_hairtie_keywords']=e.get('aliases',[])+[e['hair_tie_motif_name']]
        e['category_name']=cats[k]['name'];e['keywords']=[e['name'],e['en'],e['dimension']];e['related_reading']=e.pop('reference_ids',cats[k]['source_ids']);e['design_tip']=e.pop('note','') or cats[k]['guide'];e['search_query']=e['en']+' character design reference'
    for e in entries:
        if e.get('anime_hairtie_reference'):e['keywords']=list(dict.fromkeys(e['keywords']+e['anime_hairtie_keywords']))
        if e.get('art_style_reference'):e['keywords']=list(dict.fromkeys(e['keywords']+e.get('aliases',[])))
    # Published IDs are assigned before moving entries between display categories.
    lips_expansion_v35.reclassify_gaze_and_laughter(entries,categories)
    wardrobe_parts_v44.reclassify_legacy_parts(entries,categories)
    counts=Counter(e['category'] for e in entries)
    # Refresh category copy after entry tips are resolved so prior saved entries stay stable.
    cats['female_life_stages']['guide']='按年龄顺序并排比较正面与侧身，观察完整衣着下的躯干、四肢和姿态变化。16个阶段各有两种视角；站姿使用统一示意标尺与脚底基线，婴幼儿卧姿另组。原有面容、全身与尺寸设定可切换到全部词条查看。'
    cats['body']['guide']='默认并排比较成年角色的正面与侧身，切换罩杯、身高、肩宽、腰围与臀围，所有数值以厘米标明；尺寸是虚构角色设定，罩杯采用注明来源的日系华歌尔参考表。全部词条保留健身型、梨形、高低肩等轮廓与体态参考。'
    # Historical entry design tips remain unchanged.
    cats['pose']['guide']='共300项基础体态与动作参考，含镜头摆姿、俏皮与礼服、椅面沙发与地面构图、行走避让、舞台唱歌、手机与穿戴操作、家务、门窗、运动、施法与双人互动。卡片标明视角、动作阶段和主要支撑；原有坐蹲跪起身48项保留。另有24项柔韧姿态与48项摄影摆姿单列。'
    cats['fashion_history']['guide']='96项女装历史与地域对照，分为原有中国、欧洲、近现代三组，以及中国时段补充、日本与朝鲜半岛、南亚西亚及其他地域三组。卡片标明参考年代、地域和衣物结构；日韩各自查看同线相邻款式，地域选编只作并列参照，不构成文化之间的演化链。'
    cats['face_overlays']['guide']='妆痕泪汗、污迹、眼罩绷带，以及口罩、防毒面具与一般面具的成年佩戴图例；比较覆盖区域、眼窗、滤盒和固定带。装饰面具与呼吸防护器分开标记。'
    cats['face_states']['guide']='以眼睑、眉线、嘴角、肤色和汗滴表现疲劳、病中与环境状态；另有睡眠、昏迷、长眠剧情表演各16项。后者是非血腥角色设定，不能凭面部外观判断真实意识或生命状态。'
    cats['hair_with_accessories']['guide']='96种佩戴发饰的完整发型，发绳48项，发卡、发箍与发簪各16项。新增32项比较组绳长带结、两侧蝶结、侧鬓缠绳与额前冲天揪，展示扎根和完整发尾。'
    cats['hair_accessories']['guide']='64种发饰均提供物件结构图与成年角色佩戴图；按箍带、发夹、簪梳、发圈分组，比较头部位置、比例与固定关系。'
    cats['eyewear']['guide']='16种眼镜均提供物件结构图与成年角色佩戴图；比较框形、镜片、鼻梁、镜腿、夹片与头带如何贴合面部。'
    cats['hair_surface']['guide']='78项发质与发色参考，比较发丝粗细、轻重蓬松、光泽、卷纹、自然色阶与细致染色；新增32项，发质与颜色分开观察。'
    cats['expression']['guide']='76项基础表情、日常微表情与完整妆面参考；凝视与憋笑在“情绪与眉眼联动”中浏览，唇部近景见“唇妆与唇色”。妆容组合看色区、边缘和质感。'
    cats['art_game']['guide']='比较游戏原画、像素、三维角色与立绘。像素尺寸对照以16、32、64、128级模拟由粗到细的视觉效果，配图不是相应尺寸的原生像素素材。'
    cats['art_animation']['guide']='比较动漫的线条、色块、人物比例与视觉语言；“头身比画风”提供风格化成年角色全身对照，比例是近似示意。'
    cats['face_emotions']['guide']='144项情绪与目光表演参考，按眉峰、眼睑、视线、嘴角与头部方向比较。包括新增归入的凝视8项、憋笑8项，可按细分直接浏览。'
    cats['intimate_costumes']['guide']='64套成年尺码主题成衣，使用中性灰服装人台比较裁片、材质与配饰。保留原16套，新增复古礼装与浪漫、幻想节庆与舞台、都市职业与材质三组各16套；每个主题一套图例。'
    assert len({e['id'] for e in entries})==len(entries)
    assert len({e['name'] for e in entries})==len(entries)
    by_id={e['id']:e for e in entries}
    style_families=apply_facets(entries)
    for e in entries:
        if e['shoulder_type']:e['related_reading']=list(dict.fromkeys(e['related_reading']+['R26']))
        for family in style_families:
            if family['id'] in e['styles']:e['related_reading']=list(dict.fromkeys(e['related_reading']+family['source_ids']))
    for c in categories:c['count']=counts[c['id']]
    for c in categories:c['group']='clothing' if c['id'] in CLOTHING_CATEGORIES else 'appearance'
    refs=json.loads((ROOT/'source/references.json').read_text(encoding='utf-8'))
    refs_by_id={reference['id']:reference for reference in refs}
    if len(refs_by_id)!=len(refs):raise ValueError('Duplicate canonical reference IDs')
    for reference in contributions['references']:
        if reference['id'] in refs_by_id:raise ValueError('Contributions cannot overwrite an existing reference: '+reference['id'])
        refs_by_id[reference['id']]=reference
    refs=list(refs_by_id.values())
    legacy=json.loads((ROOT/'source/legacy-illustrations.json').read_text(encoding='utf-8'))
    extras=json.loads((ROOT/'source/extra-illustrations.json').read_text(encoding='utf-8')) if (ROOT/'source/extra-illustrations.json').exists() else []
    extras.extend(contributions['boards'])
    jobs=json.loads((ROOT/'source/image-jobs.json').read_text(encoding='utf-8'));order={j['id']:i for i,j in enumerate(jobs)}
    new_clothing_ids={e['id'] for j in jobs if j.get('edition')==3 for e in j['entries']}
    for e in entries:
        if e['id'] in new_clothing_ids:e['added_in']='3.0'
    v4_ids={e['id'] for j in jobs if j.get('edition')==4 for e in j['entries']}
    for e in entries:
        if e['id'] in v4_ids:e['added_in']='4.0'
    v5_ids={e['id'] for j in jobs if j.get('edition')==5 for e in j['entries']}
    for e in entries:
        if e['id'] in v5_ids:e['added_in']='5.0'
    v6_ids={e['id'] for j in jobs if j.get('edition')==6 for e in j['entries']}
    for e in entries:
        if e['id'] in v6_ids:e['added_in']='6.0'
    v7_ids={e['id'] for j in jobs if j.get('edition')==7 for e in j['entries']}
    for e in entries:
        if e['id'] in v7_ids:e['added_in']='7.0'
    v8_ids={e['id'] for j in jobs if j.get('edition')==8 for e in j['entries']}
    for e in entries:
        if e['id'] in v8_ids:e['added_in']='8.0'
    v9_ids={e['id'] for j in jobs if j.get('edition')==9 for e in j['entries']}
    for e in entries:
        if e['id'] in v9_ids:e['added_in']='9.0'
    v10_ids={e['id'] for j in jobs if j.get('edition')==10 for e in j['entries']}
    for e in entries:
        if e['id'] in v10_ids:e['added_in']='10.0'
    v11_ids={e['id'] for j in jobs if j.get('edition')==11 for e in j['entries']}
    for e in entries:
        if e['id'] in v11_ids:e['added_in']='11.0'
    v12_ids={e['id'] for j in jobs if j.get('edition')==12 for e in j['entries']}
    for e in entries:
        if e['id'] in v12_ids:e['added_in']='12.0'
    v13_ids={e['id'] for j in jobs if j.get('edition')==13 for e in j['entries']}
    for e in entries:
        if e['id'] in v13_ids:e['added_in']='13.0'
    v14_ids={e['id'] for j in jobs if j.get('edition')==14 for e in j['entries']}
    for e in entries:
        if e['id'] in v14_ids:e['added_in']='14.0'
    v15_ids={e['id'] for j in jobs if j.get('edition')==15 for e in j['entries']}
    for e in entries:
        if e['id'] in v15_ids:e['added_in']='15.0'
    v16_ids={e['id'] for j in jobs if j.get('edition')==16 for e in j['entries']}
    for e in entries:
        if e['id'] in v16_ids:e['added_in']='16.0'
    v17_ids={e['id'] for j in jobs if j.get('edition')==17 for e in j['entries']}
    for e in entries:
        if e['id'] in v17_ids:e['added_in']='17.0'
    v18_ids={e['id'] for j in jobs if j.get('edition')==18 for e in j['entries']}
    for e in entries:
        if e['id'] in v18_ids:e['added_in']='18.0'
    v19_ids={e['id'] for j in jobs if j.get('edition')==19 for e in j['entries']}
    for e in entries:
        if e['id'] in v19_ids:e['added_in']='19.0'
    v20_ids={e['id'] for j in jobs if j.get('edition')==20 for e in j['entries']}
    for e in entries:
        if e['id'] in v20_ids:e['added_in']='20.0'
    v21_ids={e['id'] for j in jobs if j.get('edition')==21 for e in j['entries']}
    for e in entries:
        if e['id'] in v21_ids:e['added_in']='21.0'
    v22_ids={e['id'] for j in jobs if j.get('edition')==22 for e in j['entries']}
    for e in entries:
        if e['id'] in v22_ids:e['added_in']='22.0'
    v23_ids={e['id'] for j in jobs if j.get('edition')==23 for e in j['entries']}
    for e in entries:
        if e['id'] in v23_ids:e['added_in']='23.0'
    v24_ids={e['id'] for j in jobs if j.get('edition')==24 for e in j['entries']}
    for e in entries:
        if e['id'] in v24_ids:e['added_in']='24.0'
    v25_ids={e['id'] for j in jobs if j.get('edition')==25 for e in j['entries']}
    for e in entries:
        if e['id'] in v25_ids:e['added_in']='25.0'
    v26_ids={e['id'] for j in jobs if j.get('edition')==26 for e in j['entries']}
    for e in entries:
        if e['id'] in v26_ids:e['added_in']='26.0'
    v27_ids={e['id'] for j in jobs if j.get('edition')==27 for e in j['entries']}
    for e in entries:
        if e['id'] in v27_ids:e['added_in']='27.0'
    v28_ids={e['id'] for j in jobs if j.get('edition')==28 for e in j['entries']}
    for e in entries:
        if e['id'] in v28_ids:e['added_in']='28.0'
    v29_ids={e['id'] for j in jobs if j.get('edition')==29 for e in j['entries']}
    for e in entries:
        if e['id'] in v29_ids:e['added_in']='29.0'
    v30_ids={e['id'] for j in jobs if j.get('edition')==30 and j.get('role')!='wearing_reference' for e in j['entries']}
    for e in entries:
        if e['id'] in v30_ids:e['added_in']='30.0'
    v31_ids={e['id'] for j in jobs if j.get('edition')==31 for e in j['entries']}
    for e in entries:
        if e['id'] in v31_ids:e['added_in']='31.0'
    latest_ids={e['id'] for j in jobs if j.get('edition')==65 and j.get('role')!='fullbody_reference' for e in j['entries']}
    for e in entries:
        if e['id'] in latest_ids:e['added_in']='65.0'
        e['cosplay_reference']=e['category'].startswith('cosplay_') or e['category'] in ['special_costumes','masks']
        if e['cosplay_reference']:e['keywords']=list(dict.fromkeys(e['keywords']+['Cosplay','cos','coser','角色扮演']))
    for e in entries:
        e['facial_reference']=e['category'] in lips_expansion_v35.NEW_CATEGORIES or e['category'] in eye_makeup_expansion.NEW_CATEGORIES or e['category'] in facial_expansion.NEW_FACE_CATEGORIES or e['category'] in ['face','features','expression','face_views','eyes','anthro_heads'] or e['id'] in ['SK009','SK010','SK013'] or (e['category']=='body_art' and (int(e['id'][2:])<=16 or 25<=int(e['id'][2:])<=28)) or (e['category']=='cosplay_looks' and int(e['id'][2:])<=28)
    for e in entries:e['hosiery_reference']=e['category']=='hosiery' or e['id'] in hosiery_expansion.LEGACY_HOSIERY_IDS
    for e in entries:
        e['anthro_reference']=e['category'] in anthro_expansion.ANTHRO_CATEGORIES or e['id'] in anthro_expansion.LEGACY_ANTHRO_IDS or bool(e.get('hybrid_reference')) or bool(e.get('quadruped_reference'))
        if e['category'] in anthro_expansion.ANTHRO_CATEGORIES or e.get('quadruped_reference'):e['keywords']=list(dict.fromkeys(e['keywords']+e.get('aliases',[])))
    extras.sort(key=lambda b:order.get(b['id'],9999))
    boards=legacy+extras
    for b in boards:
        if check_assets:assert (ROOT/b['image']).exists(),b['id']
        for i,item in enumerate(b['items']):
            e=by_id[item['entry_id']];assert item['name']==e['name'],item
            field='wearing_visual' if b.get('role')=='wearing_reference' else 'fullbody_visual' if b.get('role')=='fullbody_reference' else 'visual'
            e[field]={'board':b['id'],'image':b['image'],'column':i%b['columns'],'row':i//b['columns'],'columns':b['columns'],'rows':b['rows'],'label':item['label'],'aspect':(b['width']/b['columns'])/(b['height']/b['rows'])}
            if b.get('column_boundaries') and b.get('row_boundaries'):
                col=i%b['columns'];row=i//b['columns'];xs=b['column_boundaries'];ys=b['row_boundaries']
                rect={'x':xs[col],'y':ys[row],'width':xs[col+1]-xs[col],'height':ys[row+1]-ys[row],'sheet_width':b['width'],'sheet_height':b['height']}
                e[field]['crop']=rect;e[field]['aspect']=rect['width']/rect['height']
    dimension_path=ROOT/'source/body-dimension-figures.json'
    dimension_bounds={r['id']:r for r in json.loads(dimension_path.read_text(encoding='utf-8'))} if dimension_path.exists() else {}
    for e in entries:
        if e.get('body_dimension_reference'):
            if not partial:assert e['id'] in dimension_bounds,e['id']+' dimension figure missing'
            if e['id'] in dimension_bounds:
                r=dimension_bounds[e['id']];assert r['x']>=0 and r['y']>=0 and r['x']+r['width']<=r['sheet_width'] and r['y']+r['height']<=r['sheet_height']
                e['dimension_figure']={k:v for k,v in r.items() if k not in ['id','pixels','axis']}
    figure_path=ROOT/'source/life-stage-figures.json' 
    figure_bounds={r['id']:r for r in json.loads(figure_path.read_text(encoding='utf-8'))} if figure_path.exists() else {}
    for e in entries:
        if e.get('comparison_reference'):
            if not partial:assert e['id'] in figure_bounds,e['id']+' comparison figure missing'
            if e['id'] in figure_bounds:
                r=figure_bounds[e['id']];assert r['x']>=0 and r['y']>=0 and r['x']+r['width']<=r['sheet_width'] and r['y']+r['height']<=r['sheet_height']
                e['comparison_figure']={k:v for k,v in r.items() if k not in ['id','pixels']}
        assert all(i in refs_by_id for i in e['related_reading'])
        if e['id']=='HS001':e['design_tip']='图例展示长直发与齐刘海，实际长度在全身或背面图中另行标注。'
        if e['id']=='CN027':e['design_tip']='图例采用短上衣与长裙的飞天幻想变体；需要完整高腰衣裙时，可延长上衣并与裙腰衔接。'
        if e['id']=='CN032':e['design_tip']='图例是偏短裙变体；可延长至膝下，保留裙撑、盘扣与布衫层次。'
        if e['id'] in {'SS001','SS002','SS003','SS015','SS016'}:e['design_tip']='图例展示取下头盔后的服装状态；画完整密封方案时需补画头盔与颈部锁环的连接。舱内、舱外和科幻方案分别理解。'
        if e['name']=='裙撑轮廓礼服':e['design_tip']='正面示意用于整体风格；后部裙撑突出量要另画侧面与背面，并核对实物。'
        if e['id']=='TO053':e['design_tip']='图例采用领缘较宽、接近肩端的船领变体；收窄横向领口即可增加肩部覆盖。'
        if e['id']=='OP053':e['design_tip']='图例展示覆领较低的变体；需要包住完整上肩时，应上移领缘并另画肩部支撑。'
        if e['id'] in {'FO033','FO040'}:e['design_tip']='图例采用短裙变体；膝长款可延长底裙，保留肩披、腰封与外裙固定点。'
    missing=[e['id'] for e in entries if not e.get('visual')]
    if not partial:assert not missing, 'Missing images: '+','.join(missing)
    combos=json.loads((ROOT/'source/legacy-combinations.json').read_text(encoding='utf-8'))
    extra_combos=[
        ('山路摄影师','报童帽|短款礼服外套|工装裤|相机硬包|胸前相机架|自然行走','灰棕与雾蓝；携行固定点明确'),
        ('溪谷登山向导','登山向导装|框架登山包|护耳冬帽|雪地保暖靴|扶杖站立','暗绿与橙；装备重量影响姿态'),
        ('星盘首饰匠','辫尾盘髻|蝴蝶结领衬衫|阔腿裤|宽硬手镯|星盘仪器|手指托下巴','紫灰与铜金；首饰只保留局部重点'),
        ('书店讲师','成熟成人柔和外观|露耳侧发|校园成人讲师装|托特手提袋|短珠链|直坐','海军蓝与米白；头部与书册为识别点'),
        ('海岸救援员','救援行动装灵感|救生浮力背心装|医护工作帽|硬壳药箱|防晒泳装|伸手指向','橙色与石墨；优先明确防护与工具'),
        ('弓术教练','左右并行贴头辫|运动体格|骑术训练装|前臂护甲|肩背箭袋|拉弓','棕与森林绿；动作中保留握持与带具关系'),
        ('花园礼仪官','花形盘辫|布花领饰|披风一体礼服|面纱礼帽|星月甲面|双手身前交叠','奶白与鼠尾草；远近景分别保留头饰和甲面细节'),
        ('黎明潜水员','短法杖|全长潜水服|潜水袜靴|腕部显示装置|发尾散束|回头','雾蓝与青白银；湿发与装备分区清楚')
    ]
    extra_combos+=COSPLAY_COMBINATIONS
    names={e['name']:e for e in entries}
    # Correct shorthand to canonical names.
    extra_combos=[(n,k.replace('防晒泳装','长袖防晒泳装'),p) for n,k,p in extra_combos]
    for name,part_names,palette in extra_combos:
        parts=part_names.split('|');combos.append({'name':name,'description':'、'.join(parts),'palette':palette,'entry_ids':[names[x]['id'] for x in parts]})
    combos+=identity_v51.make_identity_combinations(entries)
    combos+=identity_flex_v52.make_v52_combinations(entries)
    combos+=scholar_myth_v53.make_v53_combinations(entries)
    cosplay_combo_names={n for n,_,_ in COSPLAY_COMBINATIONS}
    for c in combos:
        if c['name'] in cosplay_combo_names:c['cosplay_combo']=True
    combos,example_source=prepare_system_examples(ROOT,entries,combos)
    illustrated=sum('visual' in e for e in entries)
    meta={'title':'女性之美','subtitle':'女性角色外观图鉴','date':'2026-10-14','version':'3.0','entry_count':len(entries),'category_count':len(categories),'clothing_count':sum(counts[k] for k in CLOTHING_CATEGORIES),'clothing_categories':CLOTHING_CATEGORIES,'illustrated_count':illustrated,'board_count':len(boards),'reference_count':len(refs),'museum_image_count':6,'combination_count':len(combos),'missing_image_count':len(missing),'scope':'覆盖常见外貌、服饰、职业与幻想创作部件；视角、成年年龄表现与配色为独立创作参考分类；青少年服装按校园、日常和活动另列。','provenance':'词条独立编排；动漫图为 AI 生成的创作示意，六张实物照片另有原始馆藏记录。相关阅读是延伸入口，不代表每项均为文献引用。'}
    meta.update(version='65.0',layout_version='32.0',last_content_version='65.0',date='2026-10-31',new_count=len(latest_ids),style_family_count=len(style_families),shoulder_count=sum(bool(e['shoulder_type']) for e in entries),hair_count=sum(e['category'].startswith('hair_') and e['category']!='hair_accessories' for e in entries),hooded_cloak_count=sum(bool(e.get('hooded_cloak')) for e in entries))
    release_path=ROOT/'source/content-release.json'
    if release_path.exists():
        release=json.loads(release_path.read_text(encoding='utf-8'))
        meta.update(version=release['version'],last_content_version=release['version'],date=release['date'],new_count=sum(e.get('added_in')==release['version'] for e in entries))
    meta['camera_reference_count']=sum(bool(e.get('camera_reference')) for e in entries)
    meta['cinematic_reference_count']=sum(bool(e.get('cinematic_reference')) for e in entries)
    meta['visual_language_reference_count']=sum(bool(e.get('visual_language_reference')) for e in entries)
    meta['game_design_reference_count']=sum(bool(e.get('game_design_reference')) for e in entries)
    meta['combination_count']=sum(not card.get('archived') for card in combos)
    meta['legacy_combination_count']=sum(bool(card.get('archived')) for card in combos)
    meta['example_version']=example_source['version']
    camera_category_ids={entry['category'] for entry in entries if entry.get('camera_reference')}
    meta['camera_categories']=[c['id'] for c in category_extensions if c['id'] in camera_category_ids]
    meta['scholar_myth_v53_new_count']=sum(bool(e.get('scholar_myth_v53_reference')) for e in entries)
    meta['scholar_myth_v53_counts']={cid:counts[cid] for cid in scholar_myth_v53.NEW_CATEGORIES}
    meta['identity_flex_v52_new_count']=sum(bool(e.get('identity_flex_v52_reference')) for e in entries)
    meta['flexibility_count']=sum(bool(e.get('flexibility_reference')) for e in entries)
    meta['kungfu_clown_counts']={cid:counts[cid] for cid in ['kungfu_outfits','clown_outfits']}
    meta['identity_count']=sum(bool(e.get('identity_reference')) for e in entries)
    meta['identity_kinds']=list(dict.fromkeys(e['identity_kind'] for e in entries if e.get('identity_reference')))
    meta['identity_categories']=identity_v51.NEW_CATEGORIES
    meta['persona_v50_new_count']=sum(bool(e.get('persona_v50_reference')) for e in entries)
    meta['presence_v49_new_count']=sum(bool(e.get('presence_v49_reference')) for e in entries)
    meta['presence_gesture_new_count']=sum(bool(e.get('presence_gesture_reference')) for e in entries)
    meta['gesture_extension_count']=sum(bool(e.get('gesture_reference')) for e in entries)
    meta['role_style_new_count']=sum(bool(e.get('role_style_reference')) for e in entries)
    meta['role_style_counts']={cid:counts[cid] for cid in role_style_v47.NEW_CATEGORIES}
    meta['persona_count']=sum(bool(e.get('persona_reference')) for e in entries)
    meta['persona_labels']=list(dict.fromkeys(e['persona_tag'] for e in entries if e.get('persona_reference')))
    meta['coverage_look_count']=sum(bool(e.get('coverage_reference')) for e in entries)
    meta['wardrobe_part_count']=sum(bool(e.get('wardrobe_part_reference')) for e in entries)
    meta['shoe_sock_glove_counts']={cid:counts[cid] for cid in ['footwear','hosiery','gloves']}
    meta['fashion_history_count']=sum(bool(e.get('fashion_history_reference')) for e in entries)
    meta['study_count']=sum(bool(e.get('study_reference')) for e in entries)
    meta['study_categories']=details_lighting_v43.NEW_CATEGORIES
    meta['study_groups']=[{'id':kind,'category':cid,'name':name,'count':sum(e.get('study_group')==kind for e in entries)} for kind,cid,name in details_lighting_v43.GROUPS]
    meta['controlled_comparison_count']=sum(bool(e.get('study_reference') and e.get('comparison_set')) for e in entries)
    meta['hybrid_count']=sum(bool(e.get('hybrid_reference')) for e in entries)
    meta['hybrid_groups']=[{'id':kind,'name':name,'count':sum(e.get('hybrid_group')==kind for e in entries)} for kind,name in hybrid_forms_v42.GROUPS]
    meta['chinese_fantasy_count']=sum(bool(e.get('chinese_fantasy_reference')) for e in entries)
    meta['chinese_fairy_count']=counts['chinese_fairy_outfits']
    meta['chinese_demoness_count']=counts['chinese_demoness_outfits']
    meta['superhero_count']=sum(bool(e.get('superhero_reference')) for e in entries)
    meta['superhero_silhouette_count']=sum(e.get('superhero_kind')=='silhouette' for e in entries)
    meta['superhero_original_count']=sum(bool(e.get('superhero_reference')) for e in entries)
    meta['fashion_history_tracks']=fashion_history_v38.TRACKS+fashion_history_v39.TRACKS
    meta['fashion_history_extension_count']=sum(bool(e.get('fashion_history_extension')) for e in entries)
    meta['seated_pose_count']=sum(bool(e.get('seated_pose_reference')) for e in entries)
    meta['intimate_theme_count']=sum(bool(e.get('intimate_theme_reference')) for e in entries)
    meta['intimate_costume_count']=counts['intimate_costumes']
    meta['lip_count']=sum(bool(e.get('lip_reference')) for e in entries)
    meta['lip_categories']=lips_expansion_v35.NEW_CATEGORIES
    meta['beauty_expansion_count']=sum(bool(e.get('beauty_expansion_reference')) for e in entries)
    meta['special_costume_categories']=[*costume_hair_expansion.SPECIAL_CATEGORIES,'special_costumes',*special_age_expansion.SPECIAL_CATEGORIES,'nun_costumes',*body_stage_cover_expansion.NEW_CATEGORIES,*magical_ninja_expansion.NEW_CATEGORIES,*diverse_roles_expansion.NEW_CATEGORIES,*superhero_expansion_v40.NEW_CATEGORIES,*chinese_fantasy_v41.NEW_CATEGORIES]
    meta['special_costume_categories']+=['idol_outfits','band_outfits','assassin_outfits']
    meta['special_costume_count']=sum(e['category'] in meta['special_costume_categories'] for e in entries)
    meta['special_new_count']=sum(bool(e.get('special_variant_reference') or e.get('stage_family_reference') or e.get('superhero_reference') or e.get('chinese_fantasy_reference')) and e.get('added_in')==meta['version'] for e in entries)
    meta['accessory_expansion_count']=sum(bool(e.get('accessory_expansion_reference')) for e in entries)
    meta['special_new_count']+=sum(bool(e.get('role_style_reference')) and e['category'] in ['idol_outfits','band_outfits','assassin_outfits'] and e.get('added_in')==meta['version'] for e in entries)
    meta['anime_hairtie_count']=sum(bool(e.get('anime_hairtie_reference')) for e in entries)
    meta['hair_tie_motifs']=anime_hairtie_expansion.MOTIFS
    meta['eye_makeup_count']=sum(bool(e.get('eye_makeup_reference')) for e in entries)
    meta['eye_makeup_categories']=eye_makeup_expansion.NEW_CATEGORIES
    meta['headphone_count']=sum(bool(e.get('headphone_reference')) for e in entries)
    meta['headphone_groups']=headphone_expansion.GROUPS
    meta['wearing_reference_count']=sum('wearing_visual' in e for e in entries)
    meta['wearing_reference_categories']=['hair_accessories','eyewear']
    meta['styled_hair_count']=sum(bool(e.get('styled_hair_reference')) for e in entries)
    meta['accessory_expansion_categories']=accessory_hairstyle_expansion.NEW_ACCESSORY_CATEGORIES
    meta['hair_accessory_groups']=accessory_hairstyle_expansion.HAIR_ACCESSORY_GROUPS
    meta['photo_pose_count']=counts['photo_poses']
    meta['photo_pose_groups']=photo_poses_v55.GROUPS
    meta['pose_v54_new_count']=sum(bool(e.get('pose_v54_reference')) for e in entries)
    meta['pose_count']=counts['pose']
    meta['pose_expansion_count']=sum(bool(e.get('pose_expansion_reference')) for e in entries)
    meta['pose_groups']=[{**g,'count':sum(e.get('pose_group')==g['id'] for e in entries)} for g in pose_expansion.POSE_GROUPS+pose_v54.POSE_GROUPS]
    meta['diverse_role_count']=sum(bool(e.get('diverse_role_reference')) for e in entries)
    meta['diverse_role_kind_count']=len({e['role_kind'] for e in entries if e.get('diverse_role_reference')})
    meta['magical_ninja_count']=sum(bool(e.get('magical_ninja_reference')) for e in entries)
    meta['body_dimension_count']=sum(bool(e.get('body_dimension_reference')) for e in entries)
    meta['body_dimension_case_count']=len({e['dimension_case'] for e in entries if e.get('body_dimension_reference')})
    meta['body_shape_count']=sum(bool(e.get('body_shape_reference')) for e in entries)
    meta['stage_family_count']=sum(bool(e.get('stage_family_reference')) for e in entries)
    meta['face_cover_count']=sum(bool(e.get('face_cover_reference')) for e in entries)
    meta['nun_count']=sum(bool(e.get('nun_reference')) for e in entries)
    meta['story_state_count']=sum(bool(e.get('story_state_reference')) for e in entries)
    meta['growth_count']=sum(bool(e.get('growth_reference')) for e in entries)
    meta['adult_measurement_count']=sum(bool(e.get('adult_measurement_reference')) for e in entries)
    meta['life_stage_comparison_count']=sum(bool(e.get('comparison_reference')) for e in entries)
    meta['life_stage_count']=sum(bool(e.get('life_stage_reference')) for e in entries)
    meta['life_stage_categories']=['female_life_stages']
    meta['hair_state_count']=sum(bool(e.get('hair_state_reference')) for e in entries)
    meta['wedding_count']=sum(bool(e.get('wedding_reference')) for e in entries)
    meta['wedding_categories']=wedding_expansion.NEW_CATEGORIES
    meta['trend_model_count']=sum(bool(e.get('trend_model_reference')) for e in entries)
    meta['trend_model_categories']=trend_model_expansion.NEW_CATEGORIES
    meta['cosplay_count']=sum(bool(e.get('cosplay_reference')) for e in entries)
    meta['hosiery_count']=sum(bool(e.get('hosiery_reference')) for e in entries)
    meta['denier_values']=hosiery_expansion.DENIERS
    meta['facial_count']=sum(bool(e.get('facial_reference')) for e in entries)
    meta['anthro_count']=sum(bool(e.get('anthro_reference')) for e in entries)
    meta['anthro_categories']=[*anthro_expansion.ANTHRO_CATEGORIES,*hybrid_forms_v42.NEW_CATEGORIES,quadruped_v56.CID]
    meta['quadruped_count']=sum(bool(e.get('quadruped_reference')) for e in entries)
    meta['anthro_levels']=anthro_expansion.LEVELS
    meta['facial_new_categories']=facial_expansion.NEW_FACE_CATEGORIES
    meta['seasonal_count']=sum(bool(e.get('seasonal_reference')) for e in entries)
    meta['seasonal_categories']=seasonal_expansion.SEASONAL_CATEGORIES
    meta['seasons']=[{'id':key,'name':cn+'季','category':cat,'count':counts[cat]} for key,cn,cat,prefix in seasonal_expansion.SEASONS]
    data={'meta':meta,'categories':categories,'entries':entries,'boards':boards,'references':refs,'combinations':combos,'style_families':style_families,'shoulder_types':[{'id':k,'name':v[0]} for k,v in SHOULDERS.items()]}
    data['example_chapters']=example_source['chapters']
    data['image_exports']=prepare_image_exports(ROOT,data) if image_exports else {}
    navigation=build_navigation(ROOT,data)
    data['example_coverage']=example_coverage(data,navigation)
    if not partial:
        from validate_atlas import validate
        errors=validate(data,navigation,ROOT,assets=check_assets,registry=registry)
        if errors:raise ValueError('Catalog validation failed: '+'; '.join(errors[:20]))
    template=(ROOT/'tools/templates/atlas_template.html').read_text(encoding='utf-8')
    for filename,placeholder in [('browse_v32.css','__BROWSE_STYLES__'),('browse_v32.html','__BROWSE_HTML__'),('browse_v32.js','__BROWSE_SCRIPT__'),('body_dimensions.css','__BODY_DIMENSION_STYLES__'),('body_dimensions.html','__BODY_DIMENSION_HTML__'),('body_dimensions.js','__BODY_DIMENSION_SCRIPT__'),('theme_palette.css','__THEME_STYLES__'),('theme_palette.js','__THEME_SCRIPT__'),('brand.css','__BRAND_STYLES__'),('brand.js','__BRAND_SCRIPT__'),('card_library.css','__CARD_LIBRARY_STYLES__'),('card_library.html','__CARD_LIBRARY_HTML__'),('card_library.js','__CARD_LIBRARY_SCRIPT__'),('subdivision_navigation.css','__SUBDIVISION_STYLES__'),('subdivision_navigation.js','__SUBDIVISION_SCRIPT__')]:
        template=template.replace(placeholder,(ROOT/'tools/templates'/filename).read_text(encoding='utf-8'))
    for suffix,placeholder in [('css','__CARD_SYNTHESIS_STYLES__'),('html','__CARD_SYNTHESIS_HTML__'),('js','__CARD_SYNTHESIS_SCRIPT__')]:
        template=template.replace(placeholder,(ROOT/f'tools/templates/card_synthesis.{suffix}').read_text(encoding='utf-8'))
    for suffix,placeholder in [('css','__IMAGE_EXPORT_STYLES__'),('js','__IMAGE_EXPORT_SCRIPT__')]:
        template=template.replace(placeholder,(ROOT/f'tools/templates/image_export.{suffix}').read_text(encoding='utf-8'))
    template=apply_theme_palettes(ROOT,template)
    template=template.replace('__LOADING_SCRIPT__',(ROOT/'tools/templates/lazy_thumbnails.js').read_text(encoding='utf-8'))
    template=template.replace('__CONTENT_MAJOR__',meta['version'].split('.')[0])
    template=apply_brand_assets(ROOT,template)
    template=template.replace('__NAVIGATION_DATA__',json.dumps(navigation,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
    replacements={'__CLOTHING_COUNT__':str(meta['clothing_count']),'__ATLAS_DATA__':json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'),'__ENTRY_COUNT__':str(len(entries)),'__ILLUSTRATED_COUNT__':str(illustrated),'__BOARD_COUNT__':str(len(boards)),'__REFERENCE_COUNT__':str(len(refs)),'__READING_COUNT__':str(len(refs)-6),'__COMBO_COUNT__':str(meta['combination_count']),'__CATEGORY_COUNT__':str(len(categories)),'__DOMAIN_COUNT__':str(len(navigation['groups'])),'__SECTION_COUNT__':str(navigation['section_count'])}
    for old,new in replacements.items():template=template.replace(old,new)
    for key,value in {'__NEW_COUNT__':meta['new_count'],'__STYLE_COUNT__':meta['style_family_count']}.items():template=template.replace(key,str(value))
    if partial:
        (ROOT/'.work/previews/catalog-v2-preview.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (ROOT/'.work/previews/index-v2-preview.html').write_text(template,encoding='utf-8')
        print(json.dumps({'preview_entries':len(entries),'image_checks':check_assets}));return data
    (ROOT/'index.html').write_text(template,encoding='utf-8')
    for fname,obj in [('data/catalog.json',data),('data/illustrations.json',boards),('data/references.json',refs),('data/combinations.json',combos),('data/navigation.json',navigation)]:
        (ROOT/fname).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_json(ROOT/'source/id-registry.json',registry)
    export_collaboration_data(ROOT,data,navigation)
    for edition in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]:
        ids={j['id'] for j in jobs if j.get('edition')==edition}
        prompt_set=[{'id':b['id'],'prompt':b['prompt'],'image':b['image'],**({k:b[k] for k in ['edit_prompt','reference_image','edit_history'] if k in b})} for b in extras if b['id'] in ids]
        (ROOT/f'prompts/image-prompts-v{edition}.json').write_text(json.dumps(prompt_set,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_docs(data)
    write_fashion_docs(ROOT,data)
    write_cosplay_docs(ROOT,data)
    write_facial_docs(ROOT,data)
    write_latest_docs(ROOT,data)
    write_anthro_docs(ROOT,data)
    write_seasonal_docs(ROOT,data)
    write_trend_model_docs(ROOT,data)
    write_wedding_docs(ROOT,data)
    write_costume_hair_docs(ROOT,data)
    write_special_age_docs(ROOT,data)
    write_nun_states_growth_docs(ROOT,data)
    write_life_comparison_docs(ROOT,data)
    write_body_stage_cover_docs(ROOT,data)
    write_magical_ninja_docs(ROOT,data)
    write_body_dimensions_docs(ROOT,data)
    write_diverse_roles_docs(ROOT,data)
    write_pose_docs(ROOT,data)
    write_accessory_hairstyle_docs(ROOT,data)
    write_wearing_reference_docs(ROOT,data)
    write_headphone_docs(ROOT,data)
    write_eye_makeup_docs(ROOT,data)
    write_beauty_v34_docs(ROOT,data)
    write_lips_v35_docs(ROOT,data)
    write_intimate_v36_docs(ROOT,data)
    write_history_v38_docs(ROOT,data)
    write_superhero_v40_docs(ROOT,data)
    write_chinese_fantasy_v41_docs(ROOT,data)
    write_hybrid_v42_docs(ROOT,data)
    write_details_v43_docs(ROOT,data)
    write_wardrobe_v44_docs(ROOT,data)
    write_persona_v45_docs(ROOT,data)
    write_role_style_v47_docs(ROOT,data)
    write_presence_gesture_v48_docs(ROOT,data)
    write_persona_v49_docs(ROOT,data)
    write_persona_v50_docs(ROOT,data)
    write_identity_v51_docs(ROOT,data)
    write_identity_flex_v52_docs(ROOT,data)
    write_scholar_myth_v53_docs(ROOT,data)
    write_pose_v54_docs(ROOT,data)
    write_photo_poses_v55_docs(ROOT,data)
    write_quadruped_v56_docs(ROOT,data)
    write_costume_comparison_v63_docs(ROOT,data)
    write_costume_comparison_v64_docs(ROOT,data)
    write_hair_comparison_v65_docs(ROOT,data)
    write_camera_docs(ROOT,data)
    write_visual_narrative_docs(ROOT,data)
    write_game_design_docs(ROOT,data)
    write_rights_docs(ROOT)
    write_example_docs(ROOT,data,navigation)
    write_navigation_docs(ROOT,data,navigation)
    finalize_docs(ROOT)
    write_usage_readme(ROOT)
    archive=_bootstrap.PACKAGE
    if package:
        from release_atlas import package_legacy
        package_legacy(ROOT,archive)
    print(json.dumps({key:meta[key] for key in ['version','entry_count','category_count','board_count','reference_count']},ensure_ascii=False))
    if package:print('Archive bytes:',archive.stat().st_size)
    return data

def write_docs(data):
    m=data['meta'];es=data['entries'];boards=data['boards'];refs=data['references']
    navigation=build_navigation(ROOT,data)
    by_category={c['id']:c for c in data['categories']}
    cats=[{**by_category[cid],'name':navigation.get('category_labels',{}).get(cid,by_category[cid]['name'])} for group in navigation['groups'] for cid in group['categories']]
    intro=f'''# 女性之美

**女性角色外观图鉴**

面向游戏与动漫角色设计。服装专辑包含 {m['clothing_count']} 条服装、护甲与套装参考。画风领域覆盖动画、游戏、摄影模拟、绘画和印刷等96种表现参考，并可切换全身图与人像近景。共 {len(navigation['groups'])} 个领域、{navigation['section_count']} 个分组、{m['category_count']} 个类别和 {m['entry_count']} 个词条，每个词条均有可点击图例。包含 {len(boards)} 张分类图页、六张服饰实物照片、{len(refs)} 个参考入口与 {m['combination_count']} 套造型组合。

打开 [可搜索图鉴](index.html) 查看卡片，按中文、英文、编号或描述搜索，并可将词条加入外观卡。发型、服饰和身体外观分开组织；头部视角、成年年龄表现与配色单列为创作参考，避免混作天然外貌分类。

## 分类索引

完整入口见 [图鉴总目录](directory.md)，下表与图文详表按各领域依次排列。

| 主题 | 类别 | 配图词条数 | 组合要点 |
| --- | --- | ---: | --- |
'''
    group_by_category={cid:group for group in navigation['groups'] for cid in group['categories']}
    for c in cats:intro+=f"| {group_by_category[c['id']]['name']} | [{c['name']}](#{c['id']}) | {c['count']} | {c['guide']} |\n"
    intro+='''
## 图文详表

原创生成示意图按编号与词条对应；画风中的写真是生成的模拟影像，并非实际拍摄。历史、地域和护甲造型为灵感改编。真实脸型和体型连续变化，动漫图用于比较可见形态，不作为人体测量标准。

'''
    previous_group=None
    for c in cats:
        group=group_by_category[c['id']]
        if group['id']!=previous_group:
            intro+=f"## {group['name']}\n\n{group['note']}\n\n"
            previous_group=group['id']
        intro+=f"<a id=\"{c['id']}\"></a>\n\n### {c['name']}\n\n{c['guide']}\n\n"
        relevant=sorted({e['visual']['board'] for e in es if e['category']==c['id']})
        for bid in relevant:
            b=next(x for x in boards if x['id']==bid)
            intro+=f"![{b['title']}]({b['image']})\n\n"
        intro+='| 编号 | 中文 | English | 可见特征 |\n| --- | --- | --- | --- |\n'
        for e in es:
            if e['category']==c['id']:intro+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
        intro+='\n'
        reading=[r for r in refs if r['id'] in c['source_ids']]
        if reading:intro+='相关阅读：'+'、'.join(f"[{r['title']}]({r['url']})" for r in reading)+'。\n\n'
    intro+='''## 角色组合与交付

参见 [新增服装与外观专辑](fashion-guide.md)、[外观卡模板](character-template.md)、[组合示例](combinations.md)、[来源说明](sources.md) 和 [第 31 版图页提示词](image-prompts-v31.json)。

每个角色固定身高、头身比、发际线、五官位置和标记位置，再决定换装和变身部件。做游戏素材时检查三视图、黑色剪影、头像缩略图、关节活动以及发束、披风和配饰的独立运动范围。
'''
    (ROOT/'docs/atlas.md').write_text(intro,encoding='utf-8')
    clothing='# 女性角色服装专辑 · 第 31 版\n\n'
    clothing+=f"共 {m['clothing_count']} 条服装、护甲与套装参考。第36版增加48种情趣主题成衣，情趣类别现有64套。第27版增加32种职业舞台与奇幻身份各2套，共64套。服装含 64 套原创角色原型Cos服；第25版增加魔法少女与忍者装扮各32套；第24版体操、啦啦队、死神与维密风格秀场装扮共64套继续提供；保留第22版修女装扮32套；此前的浴巾裹身、破损衣物、成年遮挡视图、液体浸染、人偶与玩偶服等参考；第 20 版的128套特殊装扮继续保留，包含女扮男装、僵尸与吸血鬼、囚犯与匪徒、特种部队、情趣主题及湿水衣物；婚纱32款、婚服48套继续保留；潮流、时尚与模特穿搭96套以及四季日常穿搭原有256套继续保留，并新增32套；兽娘与福瑞等外观专题继续提供，支持 {m['style_family_count']} 种风格标签。历史款按年代与地域区分。单件款式与完整套装分列；每项均有中英文名称、可见结构说明和图例。\n\n"
    clothing+='印花另见 [图案与排列](index.html?section=clothing_prints)、[印花视觉风格](index.html?section=print_styles) 和 [本版图文专辑](fashion-guide.md)；布样与首饰未计入完整服装数量。\n\n'
    clothing+='打开 [服装专辑](index.html?section=clothing) 直接筛选；使用 [全部图鉴](index.html) 查看外貌部件。\n\n| 类别 | 词条数 | 类型 |\n| --- | ---: | --- |\n'
    clothing_cats=[c for c in cats if c['id'] in CLOTHING_CATEGORIES]
    ensembles={'uniforms','sports','fantasy_outfits','historical_outfits','stage_outfits','layered_outfits','fashion_outfits','chinese_outfits','opera_outfits','special_costumes','space_suits','military_outfits','wizard_outfits','priestess_outfits','early20c_outfits','sleepwear','schoolwear','youthwear','cosplay_outfits','nun_costumes',*seasonal_expansion.SEASONAL_CATEGORIES}
    for c in clothing_cats:
        kind='整套方案' if c['id'] in ensembles or c['id'] in wedding_expansion.NEW_CATEGORIES or c['id'] in costume_hair_expansion.SPECIAL_CATEGORIES or c['id'] in special_age_expansion.CLOTHING_CATEGORIES else '单件、套装与改编' if c['id'] in {'traditional','armor'} else '单件版型'
        clothing+=f"| {c['name']} | {c['count']} | {kind} |\n"
    clothing+='\nAI 图为原创创作示意；历史、地域和专业防护样式用于角色视觉设计，具体构造可沿相关阅读核对。\n\n'
    for c in clothing_cats:
        clothing+=f"## {c['name']}\n\n{c['guide']}\n\n"
        used={e['visual']['board'] for e in es if e['category']==c['id']}
        for b in boards:
            if b['id'] in used:clothing+=f"![{b['title']}]({b['image']})\n\n"
        clothing+='| 编号 | 款式 | English | 可见结构 |\n| --- | --- | --- | --- |\n'
        for e in es:
            if e['category']==c['id']:clothing+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
        clothing+='\n'
    (ROOT/'docs/clothing-atlas.md').write_text(clothing,encoding='utf-8')
    source=f"# 女性之美 · 来源与图片说明\n\n内容版 {m['version']}，共{m['entry_count']}个词条。以下阅读链接与照片保留各自核对日期，不代表全部资料在本次构建时重新核验。配图生成与图片权利是不同记录，许可状态见 [素材说明](../NOTICE.md) 和 [许可提案](licensing-proposal.md)，待审清单见 source/rights-review.json。\n\n"
    for r in refs:
        source+=f"## {r['id']} {r['title']}\n\n[{r['publisher']}]({r['url']}) · {r['kind']}\n\n{r['summary']}\n\n图片处理：{r['rights']}。\n\n"
        if r.get('access_note'):source+=r['access_note']+'\n\n'
        if r.get('image'):source+=f"![{r['title']}]({r['image']})\n\n年代：{r['date']}；地域：{r['culture']}；材质：{r['medium']}；馆藏编号：{r['object_number']}。\n\n"
    source+='''## 原创分类图

使用内置 image_gen 工具，未使用 CLI/API 回退。第 1 版五张图的提示词在 [image-prompts.json](image-prompts.json)，第 2 版扩充在 [image-prompts-v2.json](image-prompts-v2.json)，第 3 版服装扩充在 [image-prompts-v3.json](image-prompts-v3.json)，第 4 版服装款式与风格扩充在 [image-prompts-v4.json](image-prompts-v4.json)，第 5 版新增分类配图在 [image-prompts-v5.json](image-prompts-v5.json)，第 6 版帽袋与服装扩充在 [image-prompts-v6.json](image-prompts-v6.json)，第 7 版年代与现代风格扩充在 [image-prompts-v7.json](image-prompts-v7.json)，第 8 版兜帽斗篷、特殊装扮与头发扩充在 [image-prompts-v8.json](image-prompts-v8.json)，第 9 版配饰、彩绘与日常服装扩充在 [image-prompts-v9.json](image-prompts-v9.json)，第 10 版腕饰、足部与印花扩充在 [image-prompts-v10.json](image-prompts-v10.json)，第 11 版 Cosplay 专题配图在 [image-prompts-v11.json](image-prompts-v11.json)，第 12 版面部专题配图在 [image-prompts-v12.json](image-prompts-v12.json)，第 13 版困惑与眩晕配图在 [image-prompts-v13.json](image-prompts-v13.json)，第 14 版袜类专题配图在 [image-prompts-v14.json](image-prompts-v14.json)，第 15 版潮红与含蓄情绪配图在 [image-prompts-v15.json](image-prompts-v15.json)，第 16 版兽娘与福瑞配图在 [image-prompts-v16.json](image-prompts-v16.json)，第 17 版四季日常穿搭配图在 [image-prompts-v17.json](image-prompts-v17.json)。第 18 版潮流、时尚与模特穿搭提示词在 [image-prompts-v18.json](image-prompts-v18.json)。第 19 版婚纱与婚服提示词在 [image-prompts-v19.json](image-prompts-v19.json)。第 20 版特殊装扮与头发状态提示词在 [image-prompts-v20.json](image-prompts-v20.json)。第 21 版特殊外观与女性年龄阶段提示词在 [image-prompts-v21.json](image-prompts-v21.json)。第 22 版修女、剧情状态与尺寸设定提示词在 [image-prompts-v22.json](image-prompts-v22.json)。第23版年龄阶段正面与侧身对照提示词在 [image-prompts-v23.json](image-prompts-v23.json)。第24版成年体型、舞台装扮与面部覆盖物提示词在 [image-prompts-v24.json](image-prompts-v24.json)。第25版魔法少女与忍者装扮提示词在 [image-prompts-v25.json](image-prompts-v25.json)。第26版成年尺寸并排对照提示词在 [image-prompts-v26.json](image-prompts-v26.json)。第27版多类型职业、舞台与奇幻身份装扮提示词在 [image-prompts-v27.json](image-prompts-v27.json)。第28版体态与动作扩充提示词在 [image-prompts-v28.json](image-prompts-v28.json)。第29版衣着配饰与发饰完整发型提示词在 [image-prompts-v29.json](image-prompts-v29.json)。第30版发绳与佩戴补图提示词在 [image-prompts-v30.json](image-prompts-v30.json)。第31版耳机佩戴提示词在 [image-prompts-v31.json](image-prompts-v31.json)。第33版眼部彩妆提示词在 [image-prompts-v33.json](image-prompts-v33.json)。第34版发质发色、表情与妆容提示词在 [image-prompts-v34.json](image-prompts-v34.json)。所有图页与编号映射见 [illustrations.json](illustrations.json)。页面仅裁切显示原图对应格子，原图完整保存在 images 目录。

传统服饰与护甲图是设计灵感，历史考据以具体时期和实物记录为准。公共领域实物照片共六张，其使用标识来自各件 Met 馆藏页面。外部图像检索按钮是查询入口，不代表搜索结果已经核验。
'''
    (ROOT/'docs/sources.md').write_text(source,encoding='utf-8')
    combo='# 女性角色外观组合示例\n\n每组为原创场景造型方案，配色可自由调整。外貌部件不代表固定性格。\n\n'
    by_id={e['id']:e for e in es}
    for i,c in enumerate(data['combinations'],1):
        combo+=f"## {i} {c['name']}\n\n{c['description']}。\n\n配色与重点：{c['palette']}。\n\n部件："+'、'.join(by_id[x]['name']+'（'+x+'）' for x in c['entry_ids'])+'。\n\n'
    (ROOT/'docs/combinations.md').write_text(combo,encoding='utf-8')
    readme=f'''# 女性之美

**女性角色外观图鉴**

第 17 版：服装专辑 {m['clothing_count']} 条；全部 {m['entry_count']} 个词条，{m['category_count']} 个大类，{m['entry_count']} 个对应图例，{len(boards)} 张分类图页，六张实物照片，{len(refs)} 个参考入口，{m['combination_count']} 套组合示例。

双击 index.html 或项目根目录的 Start Appearance Atlas.cmd。首页提供四季日常穿搭总览，共 {m['seasonal_count']} 套，按通勤城市、休闲校园、运动出游及裙装叠穿浏览；兽娘与福瑞按8档程度及部件浏览；面部、袜类及其他专题继续提供；Cosplay、服装、配饰、足部与印花等主题继续保留；支持 {m['style_family_count']} 种风格筛选，服装按常规类别浏览，常用别名也可检索。每个词条均有图；支持图页筛选、详情放大、前后词条切换与外观卡导入导出。

## 文件

| 文件 | 内容 |
| --- | --- |
| index.html | 离线图鉴与外观卡 |
| directory.md | 12个主题与全部{m['category_count']}类的总目录 |
| atlas.md | 完整图文详表 |
| clothing-atlas.md | 服装、护甲与套装专辑 |
| hair-atlas.md | 全部头发部件与完整造型组合 |
| cosplay-atlas.md | Cosplay总览、部件与搭配示例 |
| facial-atlas.md | 面部表情、状态、互动与眼部改造 |
| socks-atlas.md | 丝袜D数、吊带袜、短长袜与袜裤完整专题 |
| anthro-atlas.md | 兽娘与福瑞8档对照、兽脸、耳尾爪足与物种原型 |
| seasonal-atlas.md | 春夏秋冬288套日常穿搭与层次索引 |
| fashion-guide.md | 本版新增内容索引 |
| catalog.json | 所有词条、图像和类别数据 |
| illustrations.json | 全部分类图页与编号映射 |
| navigation.json | 主题、分类归属、交叉专题与文档入口 |
| images | 所有动漫图与六张实物照片 |
| character-template.md | 角色设定与美术交付模板 |
| combinations.md | {m['combination_count']} 套组合示例 |
| references.json 与 sources.md | 参考资料和图片使用说明 |
| image-prompts.json、image-prompts-v2.json、image-prompts-v3.json、image-prompts-v4.json、image-prompts-v5.json、image-prompts-v6.json、image-prompts-v7.json、image-prompts-v8.json、image-prompts-v9.json、image-prompts-v10.json、image-prompts-v11.json、image-prompts-v12.json、image-prompts-v13.json、image-prompts-v14.json、image-prompts-v15.json、image-prompts-v16.json、image-prompts-v17.json | 十七版内置 image_gen 提示词 |

配图是词条编号对应的动漫创作示意；视角、成年年龄表现和配色是额外创作参考分类。历史与地域服饰图为灵感改编。外观卡保存在当前浏览器，可导出 JSON 长期保存。旧版部件编号保留，已导出的外观卡可继续导入。

解压时保留完整文件夹与 images 子目录。更新源数据后运行 python tools/build_atlas.py 重新生成，生成器会检查每个词条都有配图。第 1 版备份在项目 outputs/packages/history 目录的 female-appearance-atlas-v1.zip。
'''
    (ROOT/'README.md').write_text(readme,encoding='utf-8')

if __name__=='__main__':build(partial='--partial' in sys.argv)
