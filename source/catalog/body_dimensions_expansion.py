"""Controlled fictional adult body dimensions, with paired clothed orthographic views."""
from catalog_content import CATALOG,add

CASES=[]
for i,cup in enumerate('ABCDEFGH'):
    CASES.append(dict(key='cup_'+cup.lower(),label=f'{cup}75 罩杯对照',axis='cup',cup=cup,height=165,shoulder=38,bust=85+2.5*i,under=75,waist=70,hip=94))
for key,label,axis,value in [('height_150','身高150 cm','height',150),('height_180','身高180 cm','height',180),('shoulder_34','肩宽34 cm','shoulder',34),('shoulder_44','肩宽44 cm','shoulder',44),('waist_62','腰围62 cm','waist',62),('waist_88','腰围88 cm','waist',88),('hip_86','臀围86 cm','hip',86),('hip_110','臀围110 cm','hip',110)]:
    case=dict(key=key,label=label,axis=axis,cup='C',height=165,shoulder=38,bust=90,under=75,waist=70,hip=94);case[axis]=value;CASES.append(case)
for view,cn in [('front','正面'),('side','侧面')]:
    for order,c in enumerate(CASES):
        metrics=f"身高{c['height']}cm；肩宽{c['shoulder']}cm；胸围{c['bust']:g}cm；下胸围{c['under']}cm；腰围{c['waist']}cm；臀围{c['hip']}cm；日系华歌尔表参考{c['cup']}75；上下胸围差{c['bust']-c['under']:g}cm"
        add('body','成年尺寸对照·'+cn,f"{c['label']}·{cn}|adult body dimension {c['key']} {view}|25岁以上成年虚构角色，{cn}直立；完整灰色不透明长袖运动上衣与长裤。{metrics}。同一组仅改变指定尺寸维度，图形为近似轮廓示意。")
        CATALOG[-1].update(added_in='26.0',body_dimension_reference=True,dimension_case=c['key'],dimension_label=c['label'],dimension_axis=c['axis'],dimension_order=order,dimension_view=view,
          age_min=25,adult_only=True,minor_reference=False,age_context='25岁以上成熟女性虚构角色尺寸设定',height_cm=c['height'],shoulder_width_cm=c['shoulder'],bust_cm=c['bust'],underbust_cm=c['under'],waist_cm=c['waist'],hip_cm=c['hip'],
          cup_letter=c['cup'],cup_difference_cm=c['bust']-c['under'],band_size_cm=75,bra_size=c['cup']+'75',cup_system='JP-Wacoal-cm',measurement_basis='fictional-character-setting',reference_ids=['R94'],aliases=['成年尺寸','体型对比','罩杯',c['cup']+'75',c['cup']+'杯','75'+c['cup'],'三围'],
          note='数值为原创成年角色的尺寸设定，并非真人测量、医学标准或理想身材。图形表现近似的完整衣着轮廓，不可从图片反推真人围度。罩杯按日系华歌尔参考表的上下胸围差标示，并同时保留下胸围；字母不能跨尺码体系或底围单独比较容量。正侧视图对应同一组设定。')
