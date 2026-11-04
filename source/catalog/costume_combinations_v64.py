"""Original outfits selected from the text-only comparison."""
from catalog_content import CATALOG, add

# Each reference ID records the text-only inspiration, not a visual match.
GROUPS = [
 ('spring','spring_outfits','春季·轻盈裙装与裙裤',[
  ('雪纺蝴蝶结上衣中裙装','chiffon bow blouse midi skirt','浅蓝无袖雪纺蝴蝶结上衣与飘逸中裙，搭颈链、小包和凉鞋。','SPR-0020'),
  ('蓝衬衫裙裤短袜凉鞋装','blue blouse skort ankle socks sandals','浅蓝衬衫搭深色裙裤、白色短袜、凉鞋、小包与帽子。','SPR-0059')]),
 ('summer','summer_outfits','夏季·牛仔与清凉叠穿',[
  ('灰衬衫牛仔长裙凉鞋装','grey shirt denim maxi skirt sandals','灰色短袖衬衫搭蓝色牛仔长裙、黑色凉鞋、肩包与银色项链。','SUM-0183'),
  ('波点衬衫吊带牛仔裤装','polka dot shirt camisole jeans','黑白波点衬衫敞穿于不透明吊带上衣外，配直筒牛仔裤与凉鞋。','SUM-0205'),
  ('蝴蝶结吊带牛仔短裙蕾丝袜','bow camisole denim miniskirt lace socks','蝴蝶结吊带上衣搭蓝色牛仔短裙、蕾丝边白短袜与凉鞋。','SUM-0116')]),
 ('autumn','autumn_outfits','秋季·大衣与材质混搭',[
  ('衬衫短裙长大衣蝴蝶结装','shirt dress long coat bow','系腰短款衬衫裙搭敞穿米色长大衣、短袜、鞋和小蝴蝶结。','AUT-0042'),
  ('红色连衣裙丝袜丝巾装','red dress tights neck scarf loafers','红色短袖连衣裙搭黑色连裤袜、乐福鞋、小包与领间丝巾。','AUT-0082'),
  ('蕾丝衬衣灯芯绒长裤装','lace blouse corduroy trousers loafers','象牙白蕾丝边衬衣搭棕色灯芯绒长裤、黑色乐福鞋与肩包。','AUT-0235')]),
 ('winter','winter_outfits','冬季·丝绒与毛绒叠穿',[
  ('丝绒吊带毛绒大衣长裤装','velvet camisole fluffy coat trousers','红色不透明丝绒吊带叠穿高领针织，配棕色系腰长裤、毛绒大衣和靴子。','WIN-0085')]),
 ('resort','swimwear','度假·长裤与泳装罩裙',[
  ('碎花长裤开衫凉鞋度假装','floral trousers cardigan resort outfit','浅色上衣与薄荷绿碎花长裤，配薄开衫、凉鞋、项链和托特包。','SWM-0001'),
  ('泳衣蝴蝶结罩裙遮阳帽装','swimsuit bow wrap skirt sun hat','不透明连体泳衣搭腰侧蝴蝶结系裹裙、遮阳帽、包与凉鞋。','SWM-0021')]),
 ('sleep','sleepwear','居家·荷叶边吊带睡衣',[
  ('荷叶吊带蕾丝短裤睡衣','ruffle camisole lace sleep shorts','宽松不透明淡紫荷叶边吊带睡衣上衣与蕾丝边睡裤，搭白色短袜与小发结。','LNG-0018')]),
 ('evening','fashion_outfits','夜宴·缎面与束腰裙装',[
  ('缎面短礼裙碎花长袜装','satin cocktail dress floral stockings','象牙白不透明缎面短礼裙搭碎花过膝长袜、低跟鞋与小手包。','SXY-0016'),
  ('束腰短裙蕾丝短袜发箍装','structured dress lace socks headband','不透明短裙外叠束腰式上身，搭蕾丝边短袜、发箍与低跟短靴。','SXY-0078')]),
]
NEW_ENTRIES=[]
for group,cid,dimension,entries in GROUPS:
    for name,en,desc,reference_id in entries:
        add(cid,dimension,f'{name}|{en}|{desc}')
        CATALOG[-1].update(added_in='64.0',outfit_combination_v64=True,outfit_group=group,
          inspiration_reference=reference_id,note='根据参考词条的文字搭配独立设计并生成配图；未核实参考图片，部分单品已有独立词条。')
        seasons={'spring_outfits':('spring','春季'),'summer_outfits':('summer','夏季'),
                 'autumn_outfits':('autumn','秋季'),'winter_outfits':('winter','冬季')}
        if cid in seasons:
            season,cn=seasons[cid]
            CATALOG[-1].update(season=season,season_name=cn,seasonal_reference=True,
              age_context='成年女性日常服装参考',outfit_context=dimension,
              outfit_components=[desc],aliases=[cn+'穿搭','四季穿搭','日常穿搭'])
        NEW_ENTRIES.append(CATALOG[-1])
