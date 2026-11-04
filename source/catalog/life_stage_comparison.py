"""V23: clothed chronological front/profile studies, without body-type variants."""
from catalog_content import CATALOG, add
from special_age_expansion import STAGES

STATURES=[52,66,78,98,118,136,152,162,165,165,165,164,162,159,156,152]
OBSERVATIONS=[
 '头颈与四肢保持新生儿关系，屈肢平卧，躯干短小',
 '较新生儿四肢更舒展，仍保留婴儿圆润轮廓与较短颈部',
 '幼儿躯干与四肢继续伸长，保持幼儿腹部与四肢的自然圆润',
 '幼儿躯干较短、腹部自然圆润，手臂和腿部尚短',
 '儿童四肢比幼儿更长，肩带与躯干轮廓平直，保持儿童体态',
 '儿童四肢继续伸长，腰胯过渡平缓，与成年躯干关系有区别',
 '青春期过渡示例，四肢伸长，肩躯干关系逐步变化，衣物自然覆盖，不做局部发育分级',
 '青春期后段示例，整体骨架与躯干关系继续趋于成年，保持适龄普通衣着与中性站姿',
 '青年成年骨架与四肢关系形成，躯干轮廓自然，站姿平稳',
 '成年稳定阶段示例，肩部、躯干、骨盆和四肢轮廓连贯自然',
 '成熟成年阶段，保持相近骨架，软组织轮廓稍柔和，避免突然改为另一种体型',
 '中年阶段示例，躯干侧面与腰腹转折稍平缓，站姿舒适',
 '中年后段示例，腹背与上臂轮廓自然放松，肩颈姿态变化轻微',
 '年长阶段示例，背部与肩颈关系略变化，重心稳定，不把年长等同疾病',
 '高龄前段示例，躯干侧面轻度前倾，膝部自然，灰发与个人面容保留',
 '高龄阶段示例，肩背与颈部姿态变化更清楚但不过度驼背，保持稳定完整站姿',
]
for view,dimension in [('front','年龄阶段并排对照·正面'),('side','年龄阶段并排对照·侧面')]:
    for order,(stage,label,low,high,group,en,face,body) in enumerate(STAGES):
        infant=low<2
        pose=('安全平卧在平坦浅色垫面，头颈有支撑；正面采用俯视完整卧姿' if view=='front' else '安全平卧在平坦浅色垫面，头颈有支撑；侧面采用完整卧姿侧视') if infant else ('正面平视，自然直立，双臂略离躯干并放松下垂，完整头顶至鞋底' if view=='front' else '严格朝画面右侧的全身90度侧身，头、肩、骨盆、膝与足的侧向关系清楚，双臂自然下垂，完整头顶至鞋底')
        clothes='普通不透明灰色长袖包脚连体衣' if infant else '普通不透明浅灰色圆领长袖棉质上衣、深灰直筒长裤和平底鞋；普通合身程度，不是紧身衣，也不堆叠宽大外套'
        name=label+('正面阶段对照' if view=='front' else '侧身阶段对照')
        add('female_life_stages',dimension,f'{name}|{en} chronological {view} comparison|{pose}；{clothes}；{OBSERVATIONS[order]}。')
        CATALOG[-1].update(added_in='23.0',life_stage_reference=True,comparison_reference=True,comparison_view=view,comparison_order=order,
          comparison_kind='recumbent' if infant else 'standing',comparison_stature_cm=STATURES[order],comparison_observation=OBSERVATIONS[order],
          age_stage=stage,age_range=label,age_min=low,age_max=high,life_stage_group=group,view_type='comparison_'+view,
          adult_only=low>=18,minor_reference=low<18,age_context=label+'；完整适龄普通衣着的中性阶段对照',
          aliases=['女性年龄阶段','身体成长对照','身体发育状态','年龄并排','侧身' if view=='side' else '正面',label,group],reference_ids=['R81','R86','R87'],
          note='观察完整衣着下的躯干、四肢和姿态变化。年龄及标尺为原创角色示例，不是平均体型或医学发育分级；青春期时序与各阶段体态均存在个体差异。婴幼儿卧姿单独比较，不能把卧长与站立图形混排。')

assert sum(bool(e.get('comparison_reference')) for e in CATALOG)==32
