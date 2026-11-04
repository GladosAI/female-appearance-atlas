"""Original hairstyle combinations selected from a text-only comparison."""
from catalog_content import CATALOG,add

# Reference identifiers identify text inspiration only, not checked source images.
GROUPS=[
 ('short1','日常短发·收颈与卷纹',[
  ('薄刘海收颈延长短发','wispy fringe tapered nape short hair','圆润顶发在后颈收窄，颈后保留稍长发尾；额前是稀疏空气刘海。','f009cba9893',['收腰短发','空气刘海','长后颈']),
  ('湿感长斜刘海短波波','wet look long fringe short bob','齐耳短波波带长斜刘海；发束略湿、聚束贴合并有窄高光。','f05f855023c',['湿发感','长刘海','短波波']),
  ('短碎层迷你狼尾发','short layered mini wolf cut','头顶和耳侧为短碎层，后颈保留较长细尾，整体仍是短发。','f192f568573',['迷你狼尾','短狼尾']),
  ('黑发螺旋卷短波波','black spiral curl short bob','下颌附近的短波波由多束小螺旋卷构成，发根与卷梢清楚。','f1648ddafc0',['螺旋烫','短卷发'])]),
 ('short2','日常短发·圆轮廓与刘海',[
  ('细挑染圆润短波波','rounded bob with fine highlights','圆润棕色短波波中穿插细窄暖色挑染发束，染色从发根随发流延伸。','f1e239fc6cc',['圆润短发','挑染']),
  ('长刘海蘑菇短发','mushroom short cut with long fringe','圆润蘑菇轮廓搭及眉长刘海，耳侧和后颈保持短剪。','f14bde4965d',['蘑菇头','长刘海']),
  ('自然微卷迷你波波','naturally wavy mini bob','齐耳迷你波波带轻微不规则弯卷，发尾轻松而不形成密集卷簇。','f124c6f2079',['迷你波波','自然卷短发']),
  ('眉上齐刘海迷你波波','micro blunt bangs mini bob','齐耳圆润迷你波波与明显位于眉上的厚齐刘海组合。','f0d3eaf7f31',['眉上刘海','迷你波波'])]),
 ('short3','日常短发·脸侧与边线',[
  ('修颜层次下颌短波波','face framing layered short bob','短波波在脸旁剪出由颧骨至下颌的轻薄错层，突出包脸轮廓。','f02977ebdcb',['脸周层次','修颜短发']),
  ('前长后短菱形短波波','diamond silhouette inverted short bob','后颈较短、前侧向下颌延长，侧后轮廓饱满并在颈部收窄。','f01adeae4ad',['前下长波波','菱形波波']),
  ('露额挽耳帅气短剪','open forehead ear tucked short cut','顶部前发向后梳并露出额头，一侧别到耳后，耳侧和后颈短收。','f04a2b69497',['帅气短发','挽耳短发','无刘海']),
  ('八字侧刘海流苏波波','curtain fringe tassel bob','下颌线附近平直齐切的流苏波波，搭两侧向外的长八字刘海。','f203a020b0d',['流苏波波','tassel bob','八字刘海'])]),
 ('medium1','中发·刘海与轻层次',[
  ('两用刘海内扣中波波','two way bangs inward curled medium bob','可中分的长侧刘海搭齐肩波波，发尾集中向颈部内扣一卷。','f0ed328cb48',['两用刘海','内扣中发']),
  ('收腰中波波内层染','nipped bob with underlayer dye','锁骨波波在颈部收窄、尾端舒展，深色外层下可见浅色内层染。','f0aa1eb7ff9',['收腰波波','内层挑染']),
  ('韩式轻羽剪中发','korean hush cut medium hair','及肩碎层从脸侧延伸到发尾，层片轻薄，颈侧收窄、发尾略外展。','f121851bf89',['Hush Cut','轻羽剪','韩式层次剪']),
  ('外翻脸侧蝴蝶层次剪','butterfly cut face framing layers','脸侧较短层向外翻开，头顶层与胸前较长后发分层衔接。','f038d46a871',['蝴蝶剪','butterfly cut'])]),
 ('medium2','中发·层次与波卷',[
  ('酒红轻透层次中发','burgundy airy medium layers','深酒红中发的脸侧与发尾分成疏松薄层，保留透气间隙。','f3c4ac5de59',['酒红发','轻透层次']),
  ('中长微卷狼尾层次','wavy medium wolf layers','较短的蓬松顶层与后颈较长发尾相接，整体带松散自然波卷。','f2b40fe4ec2',['狼尾卷发','中长狼尾']),
  ('中发下半段电棒松卷','medium curling iron soft waves','及肩中发上部较顺，下半段形成电棒式松弯，末端卷向可略有变化。','f0b30909a2a',['电棒卷','自然微卷中发']),
  ('厚层次中发渐层手刷染','heavy medium layers with balayage','偏厚重中发层片搭手刷染，深棕发根向暖米色发尾逐渐过渡。','f0e0c59fdc4',['法式手刷染','balayage','厚层次中发'])]),
 ('long','中长发·层次与柔弧',[
  ('两用侧刘海韩式中长层次','two way bangs korean long layers','中分长侧刘海可向两侧梳开，搭脸周至胸前逐渐延长的韩式层次。','f1aae3c630a',['两用刘海','韩式层次']),
  ('颈部收腰S弧中长发','nipped in s curve medium long hair','中长发沿脸侧向颈部内收，再在肩侧外展形成柔和S形弧线。','f1273c36b1d',['S型收腰','收腰中长发']),
  ('薄齐刘海碎层中长发','wispy blunt bangs shaggy long layers','额前薄齐刘海透出少量额头，中长发尾以轻碎层次向外散开。','f23495f9fa3',['空气齐刘海','碎发层次']),
  ('内扣单卷层次碎鬓中长发','one curl layered hair with loose tendrils','巧克力棕中长发的层次发尾向内弯，脸旁留少量细软碎鬓。','f0cf51757a4',['单卷层次','碎发修饰'])]),
]
NEW_ENTRIES=[]
for group,dimension,records in GROUPS:
    for name,en,desc,reference_id,aliases in records:
        add('hair_combinations',dimension,f'{name}|{en}|{desc}')
        CATALOG[-1].update(added_in='65.0',hair_comparison_v65=True,hair_group=group,
          inspiration_reference=reference_id,aliases=aliases,
          note='根据参考库发型名称独立组合并生成图例；未核实参考图片。部分剪裁、发色或刘海已有单独词条。')
        NEW_ENTRIES.append(CATALOG[-1])
