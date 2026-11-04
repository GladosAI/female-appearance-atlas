"""Original outfit combinations informed by a separate clothing-gallery audit."""
from catalog_content import CATALOG, add

# Each record describes a combination, not a claim that its individual garments are new.
# Reference IDs point to inspiration only; the atlas contains independently generated artwork.
GROUPS = [
 ('spring1','spring_outfits','春季·轻叠穿与短裙补充',[
  ('春日荷叶领风衣牛仔裙','ruffle knit trench denim skirt','荷叶一字领针织衫、粉色牛仔短裙、敞穿长风衣；白色长袜、运动鞋与草帽。','SPR-0001'),
  ('春日短牛仔外套百褶裙','denim jacket peplum pleated skirt','蝴蝶结荷叶边上衣、短牛仔夹克与浅蓝中长百褶裙；短袜与运动鞋。','SPR-0095'),
  ('春日领结衬衣裙裤装','ribbon blouse jacket tailored skort','领结衬衣、短牛仔夹克与浅色裙裤；米色连裤袜与乐福鞋。','SPR-0003'),
  ('春日碎花连裙开衫装','floral midi dress cardigan sneakers','碎花中长连衣裙配短针织开衫；浅色袜裤与白运动鞋。','SPR-0131')]),
 ('spring2','spring_outfits','春季·轻叠穿与短裙补充',[
  ('春日蕾丝吊带开衫直裤','lace camisole cardigan straight jeans','蕾丝领吊带内搭配燕麦色长开衫、浅色直筒牛仔裤与平底鞋。','SPR-0013'),
  ('春日领结衬衫裙凉鞋装','tie neck shirt dress sandals','浅绿领结系腰衬衫裙、米色薄袜裤与凉鞋，搭配小斜挎包。','SPR-0016'),
  ('春日碎花吊带双层短裙','floral camisole double layer jacket skirt','碎花吊带与短开衫叠穿，外加短夹克、百褶短裙及白色短袜。','SPR-0098'),
  ('春日蕾丝短夹克长裙装','lace trim jacket long skirt','蕾丝边短夹克配不透内搭与深灰长裙，搭凉鞋。','SPR-0241')]),
 ('summer1','summer_outfits','夏季·轻层搭与短裙补充',[
  ('夏日条纹衬衫牛仔短裤','striped shirt camisole denim bermuda','卷袖条纹衬衫内搭蕾丝领吊带，配及膝牛仔短裤、薄黑袜裤与乐福鞋。','SUM-0203'),
  ('夏日黑针织蕾丝裙短靴','black knit lace midi skirt boots','黑色短袖针织、白色蕾丝中裙与短靴，配皮质肩包。','SUM-0243'),
  ('夏日开襟棉衬牛仔短裤','open cotton shirt tank denim shorts','罗纹背心外罩敞开的白棉衬衫，配牛仔短裤与平底凉鞋。','SUM-0034'),
  ('夏日荷叶碎花裙草帽装','ruffle floral summer dress sun hat','浅色荷叶边碎花连衣裙、短袜与凉鞋，加宽檐草帽。','SUM-0050')]),
 ('summer2','summer_outfits','夏季·轻层搭与短裙补充',[
  ('夏日蝴蝶结吊带牛仔装','bow camisole jeans lace socks','蝴蝶结吊带上衣配蓝色直筒牛仔裤、蕾丝边短袜及白色运动鞋。','SUM-0016'),
  ('夏日薄卫衣蕾丝短裤装','light hoodie lace shorts tights','轻薄灰色拉链卫衣与黑色蕾丝边短裤，配黑袜裤和短靴。','SUM-0211'),
  ('夏日碎花裙短开衫凉鞋装','floral dress short cardigan sandals','小碎花中长连衣裙叠短开衫，搭配短袜和平底凉鞋。','SUM-0105'),
  ('夏日衬衣褶裥短裤袜裤装','shirt pleated shorts tights','白衬衣与深色褶裥短裤，配黑色连裤袜、乐福鞋与斜挎包。','SUM-0174')]),
 ('autumn1','autumn_outfits','秋季·材质混搭与短裙补充',[
  ('秋日开衫皮短裙长筒靴','cropped cardigan leather skirt tall boots','陶土色短开衫内搭吊带，配酒红皮质短裙、长筒针织袜和棕色长靴。','AUT-0018'),
  ('秋日蕾丝衬衣皮裙开衫','lace blouse leather skirt cardigan','象牙白蕾丝边衬衣、深色皮质A字短裙、敞穿开衫与深色袜裤。','AUT-0034'),
  ('秋日开衫百褶裙羊毛大衣','cardigan pleated skirt wool coat','针织开衫与吊带内搭，配橄榄色百褶裙、敞穿羊毛大衣和乐福鞋。','AUT-0114'),
  ('秋日领结针织裙皮夹克','bow knit dress leather jacket','领结针织短连衣裙外搭短皮夹克，脚穿麂皮短靴。','AUT-0099')]),
 ('autumn2','autumn_outfits','秋季·材质混搭与短裙补充',[
  ('秋日高领皮裙长大衣','turtleneck leather skirt long coat','高领针织衫、深色皮质短裙与长羊毛大衣，配黑袜裤与低跟靴。','AUT-0011'),
  ('秋日衬衣毛衣开衫牛仔装','shirt sweater cardigan layered denim','浅色衬衣叠细针毛衣与开衫，下配蓝色直筒牛仔裤和短靴。','AUT-0163'),
  ('秋日缎面吊带牛仔短外套','satin camisole cropped jacket jeans','缎面吊带配短夹克、深色牛仔裤、短靴与挺括肩包。','AUT-0239'),
  ('秋日领结衬衣麂皮短裙','tie blouse suede mini skirt boots','领结衬衣、麂皮A字短裙与不透袜裤，配棕色长靴及小蝴蝶结。','AUT-0066')]),
 ('winter1','winter_outfits','冬季·毛绒与裙装补充',[
  ('冬日毛领羽绒灯芯绒长裙','fur collar puffer corduroy skirt','毛领羽绒短外套叠奶油高领，配墨绿灯芯绒长裙、毛绒贝雷帽与冬靴。','WIN-0001'),
  ('冬日高领棉夹克短裙装','turtleneck quilted jacket wool skirt','奶油高领、羊毛短裙与短绗缝夹克，配深色厚袜裤及低靴。','WIN-0016'),
  ('冬日毛绒外套红褶裙装','plush jacket red pleated skirt','针织套头衫搭红色百褶短裙、毛绒短外套、黑色厚袜裤与冬靴。','WIN-0065'),
  ('冬日蕾丝针织羊毛裤装','lace yoke knit sherpa trousers','蕾丝饰边针织衫配羊毛长裤、羊羔绒夹克及短靴。','WIN-0081')]),
 ('winter2','winter_outfits','冬季·毛绒与裙装补充',[
  ('冬日丝绒吊带皮裙层搭','velvet camisole leather skirt winter layer','丝绒吊带叠开衫和夹克，搭深灰皮质短裙、保暖袜裤与短靴。','WIN-0033'),
  ('冬日蝴蝶结毛绒短裙装','ribbon turtleneck fuzzy skirt winter','领口小蝴蝶结高领针织、毛绒短裙、棉夹克、厚袜裤与麂皮靴。','WIN-0028'),
  ('冬日针织中裙毛呢大衣','knit midi dress wool coat warm boots','针织中长连衣裙叠长毛呢大衣，配围巾与毛绒衬里冬靴。','WIN-0049'),
  ('冬日绞花针织毛绒短外套','cable knit corduroy skirt plush coat','绞花针织衫搭灯芯绒裙、毛绒短外套、厚袜裤与冬靴。','WIN-0011')]),
 ('resort','swimwear','泳装与度假叠穿补充',[
  ('金属细腰带泳装度假装','belted one piece swimsuit resort','不透连体泳装配细金属腰带、宽檐帽、墨镜与平底凉鞋。','SWM-0008'),
  ('系结花纹纱笼泳装度假装','one piece swimsuit floral sarong','不透连体泳装外系花纹纱笼，配草帽、编织包与凉鞋。','SWM-0004'),
  ('波点荷叶中裙海边衬衣装','polka dot ruffle skirt resort shirt','亚麻短袖衬衣掖入波点荷叶边中裙，配凉鞋与编织小包。','SWM-0013'),
  ('荷叶短裤棉衬度假装','ruffle shorts cotton shirt resort','棉质排扣衬衣与荷叶边短裤，配凉鞋、宽檐帽和编织托特包。','SWM-0003')]),
 ('party','fashion_outfits','夜宴与都市束腰搭配',[
  ('蕾丝吊带缎面中裙晚装','lace camisole satin midi skirt evening','蕾丝边吊带上衣配缎面中裙、小手包与浅口鞋。','PTY-0005'),
  ('领结丝绒短裙夜宴装','bow velvet short dress evening','深色领结丝绒短连衣裙配不透袜裤与浅口鞋。','PTY-0008'),
  ('层纱短礼裙长手套晚装','layered tulle party dress gloves','层叠薄纱短礼裙，配缎面长手套与低跟鞋。','PTY-0007'),
  ('蕾丝中长礼裙袜裤晚装','lace midi party dress tights','有不透内衬的蕾丝中长礼裙，配薄袜裤、低跟鞋与细项链。','PTY-0016')]),
 ('sleep','sleepwear','吊带与短裤居家套装补充',[
  ('蕾丝吊带荷叶短裤软开衫','lace camisole ruffle shorts cardigan','成年居家穿搭：宽松蕾丝边吊带、不透明荷叶短睡裤、柔软开衫与拖鞋；人台示意。','LNG-0001'),
  ('滚边长罩袍短裤睡衣','contrast piping sleep shorts robe','成年居家穿搭：宽松上衣与滚边及膝睡裤，外罩轻薄开襟睡袍；人台示意。','LNG-0002'),
  ('蕾丝边吊带短裤长开衫','lace camisole shorts long cardigan socks','成年居家穿搭：不透明蕾丝边吊带与睡裤，叠长针织开衫及及膝袜。','LNG-0062'),
  ('短缎面罩袍短袖短裤套装','short satin robe short sleeve pajamas','成年居家穿搭：宽松短缎面罩袍内穿短袖上衣与短睡裤，配软短袜；人台示意。','LNG-0075')]),
 ('corset','fashion_outfits','夜宴与都市束腰搭配',[
  ('衬衣叠束腰百褶裙长袜装','corset over blouse pleated skirt boots','不透明束腰式上衣叠衬衫，配百褶短裙、长袜和短靴。','SXY-0034'),
  ('高领贴身针织裙袜裤装','high neck fitted knit dress hosiery','高领贴身针织短连衣裙配薄袜裤和低跟鞋。','SXY-0001'),
  ('丝绒短礼裙长手套袜裤装','velvet short dress long gloves tights','不透明丝绒短礼裙，搭长缎面手套、薄袜裤与跟鞋。','SXY-0023'),
  ('系带束腰裙荷叶罩裙装','lace up structured dress ruffle overskirt','不透明系带束腰连衣裙配独立荷叶罩裙、手套、短靴与小礼帽。','SXY-0022')]),
]

NEW_ENTRIES = []
for group, cid, dimension, entries in GROUPS:
    for name, en, desc, reference_id in entries:
        add(cid, dimension, f'{name}|{en}|{desc}')
        CATALOG[-1].update(added_in='63.0', outfit_combination_v63=True, outfit_group=group,
                           inspiration_reference=reference_id,
                           note='参考服装库的搭配结构重新设计并独立生成图例；此项强调整套搭配，部分单品在图鉴中已有独立词条。')
        seasons={'spring_outfits':('spring','春季'),'summer_outfits':('summer','夏季'),
                 'autumn_outfits':('autumn','秋季'),'winter_outfits':('winter','冬季')}
        if cid in seasons:
            season, cn = seasons[cid]
            CATALOG[-1].update(season=season, season_name=cn, seasonal_reference=True,
                               age_context='成年女性日常服装参考', outfit_context=dimension,
                               outfit_components=[desc], aliases=[cn+'穿搭','四季穿搭','日常穿搭'])
        if reference_id=='SPR-0001': CATALOG[-1]['shoulder_type']='bardot'
        NEW_ENTRIES.append(CATALOG[-1])
