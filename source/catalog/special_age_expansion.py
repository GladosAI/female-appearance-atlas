"""Edition 21: special appearance variants and fully clothed female life stages."""
from catalog_content import CATALOG, category, add

SPECIAL_CATEGORIES=['towel_wraps','distressed_outfits','covered_body_views','liquid_stained_outfits','doll_mascot_costumes','prosthetic_styling','plush_holds']
CLOTHING_CATEGORIES=SPECIAL_CATEGORIES[:5]
NEW_CATEGORIES=SPECIAL_CATEGORIES+['female_life_stages']
category('towel_wraps','浴巾裹身','16款成年角色浴巾裹身造型；比较包覆长度、交叠边、固定点、毛圈材质与站姿。',['R05','R11'])
category('distressed_outfits','破损衣物','16款服装破损与旧化参考；按撕裂、磨损、脱线、补片和叠穿内层比较，身体保持完整。',['R05','R11','R63'])
category('covered_body_views','成年遮挡身体视图','16项成年女性遮挡姿态参考：下身穿不透明常规三角裤，双手与前臂在胸前完整遮挡胸部；含全身正面、侧面、背面及斜侧视图。',['R04','R09'])
category('liquid_stained_outfits','液体浸染衣物','32款浸染效果，比较舞台血浆、油漆、咖啡、茶、酒、果汁、乳液色、墨水、泥水、机油与清水的形状、边缘及材质反应。',['R05','R11','R63'])
category('doll_mascot_costumes','人偶与卡通玩偶服','32项人偶与玩偶服：人形人偶主题16项，卡通玩偶服16项；完全封闭、露出真人头部、手持头套等状态分别显示。',['R61','R63'])
category('prosthetic_styling','机械单侧义肢造型','16项单侧机械义肢外观：8项手臂、8项腿部，保留另一侧自然肢体；显示完整连接外壳、衣物关系及关节轮廓。',['R09','R63'])
category('plush_holds','手抱玩偶与尺寸关系','16项成年角色抱玩偶参考，比较小、中、大型毛绒玩偶的相对尺寸、抱持位置、手臂支撑与遮挡关系。',['R04','R63'])
category('female_life_stages','女性各年龄段','32项女性角色年龄阶段创作图例：16个年龄区间各有头部与全身参考，覆盖新生儿到高龄。年龄区间是角色设定标签，外观有个体差异；所有阶段采用适龄完整日常着装。',['R81','R82','R09'])

def block(key,dimension,text,aliases=()):
    lines=[line.strip().split('|') for line in text.strip().splitlines()]
    assert len(lines)==16,(key,dimension,len(lines))
    for name,en,feature in lines:
        add(key,dimension,f'{name}|{en}|{feature}。')
        item_aliases=list(aliases)
        if key=='covered_body_views':
            item_aliases=['半裸','抱胸遮挡','不露点','covered figure reference']
            if '正面' in name:item_aliases+=['全身正面','正面']
            elif '侧面' in name:item_aliases+=['全身侧面','侧面']
            elif '背面' in name:item_aliases+=['全身背面','背面']
            elif '斜前' in name:item_aliases+=['斜前视图']
            else:item_aliases+=['斜后视图']
        if key=='prosthetic_styling':
            item_aliases=['单侧义肢','prosthesis']+(['机械手臂','手臂义肢'] if '臂' in name else ['机械单只腿部','机械腿部','腿部义肢'])
        if key=='plush_holds':
            item_aliases=[a for a in item_aliases if a!='大中小玩偶']
            size='小' if '小' in name else '大' if '大' in name else '中'
            item_aliases+=[size+'玩偶',size+'型玩偶']
        if key=='doll_mascot_costumes' and dimension=='卡通玩偶服封闭与脱头套状态':
            item_aliases=[a for a in item_aliases if a!='头套在手中']
            if '完全封闭' in name:item_aliases+=['完全看不到人','全封闭玩偶服']
            elif '只露头部' in name:item_aliases+=['只看到头部','只露头部']
            else:item_aliases+=['头套在手中','手拿头套']
        if key=='liquid_stained_outfits':
            item_aliases=[a for a in item_aliases if a!='咖啡']
            if '血浆' in name:item_aliases+=['血液','血迹','血染','舞台血浆']
            if '漆' in name:item_aliases+=['油漆','漆渍']
            if '咖啡' in name:item_aliases+=['咖啡','咖啡渍']
        CATALOG[-1].update(added_in='21.0',special_variant_reference=True,adult_only=True,minor_reference=False,
            age_context='成年女性25岁及以上的原创造型参考',outfit_components=feature.split('；'),
            aliases=['特殊外观补充',dimension,*item_aliases],reference_ids=['R63','R05'])
        if key=='covered_body_views':
            CATALOG[-1].update(representation='covered-adult-figure',coverage='opaque-briefs-and-arm-covered-chest',
                view_type='front' if '正面' in name else 'left_profile' if '左侧面' in name else 'right_profile' if '右侧面' in name else 'rear' if '背面' in name else 'front_three_quarter' if '斜前' in name else 'rear_three_quarter',
                reference_ids=['R04','R09'],note='成年人物全身中性视图：胸部由双手和前臂完整遮挡，常规三角裤不透明；检查侧转后仍不露点。')
        if key=='liquid_stained_outfits':
            CATALOG[-1]['note']='仅表现液体浸染衣物的视觉效果；血液题材用舞台血浆模拟，不表现伤口、流血或身体损伤。'
        if key=='prosthetic_styling':
            CATALOG[-1].update(prosthetic_side='left' if '左' in name else 'right',
                prosthetic_limb='arm' if '臂' in name else 'leg',
                note='原创机械义肢外观，单侧义肢与另一侧自然肢体同时可辨；连接处由完整套筒或服装覆盖，不表示医疗适配或内部构造。')
        if key=='doll_mascot_costumes' and dimension=='卡通玩偶服封闭与脱头套状态':
            CATALOG[-1]['mascot_visibility']='fully_enclosed' if '完全封闭' in name else 'head_only' if '只露头部' in name else 'head_held_at_side' if '单臂' in name else 'head_held_in_front'
        if key=='plush_holds':CATALOG[-1]['plush_size']='small' if '小' in name else 'large' if '大' in name else 'medium'

block('towel_wraps','浴巾长度与裹身结构','''
白色及膝浴巾裹身|white knee-length towel wrap|成年女性用不透明白色厚毛圈浴巾从腋下包到膝部；前侧宽幅交叠；双手自然扶住上缘；平底浴室拖鞋
奶油色长浴巾裹身|cream long towel wrap|成年女性用奶油色厚浴巾从腋下裹至小腿；侧面宽交叠；上缘折一道厚边；奶油色拖鞋
浅蓝中长浴巾裹身|pale-blue midi towel wrap|成年女性穿浅蓝不透明浴巾裹身到膝下；左侧厚交叠边可见；双臂在胸前自然扶住；蓝色拖鞋
灰色短浴巾裹身|grey short towel wrap|成年女性用深灰厚浴巾从腋下裹到膝上；下摆仍完整覆盖臀腿上部；一手扶上缘；灰色拖鞋
粉色折边浴巾裹身|pink folded-edge towel wrap|成年女性用浅粉不透明毛圈浴巾裹至膝；胸上缘向外宽折边；交叠边置于身侧；白色拖鞋
墨绿厚浴巾裹身|dark-green thick towel wrap|成年女性用墨绿厚毛圈浴巾包至小腿；厚重布料在腰侧形成竖褶；双手扶住胸前上缘；绿色拖鞋
绑带固定浴巾裹身|belt-fastened towel wrap|成年女性穿米白不透明宽浴巾裹至膝下；同材质布带在腰侧打结固定；上缘完整贴合；米色拖鞋
搭扣固定浴巾裹身|snap-fastened towel wrap|成年女性穿浅灰厚浴巾裹至膝；胸上缘侧面有小型搭扣固定；宽交叠下摆；灰色拖鞋
弹力上缘浴巾裹身|elastic-top towel wrap|成年女性穿奶白不透明及膝浴巾；上缘弹力褶量清楚；前侧宽交叠边；平底拖鞋
肩搭小巾浴巾裹身|shoulder-towel wrap ensemble|成年女性穿白色不透明及膝裹身浴巾；另有小浴巾折叠搭在一侧肩上；双手扶胸前上缘；白色拖鞋
包发巾浴巾裹身|hair-turban towel-wrap ensemble|成年女性穿浅蓝不透明及膝裹身浴巾；另一条白巾包住湿发并在头顶扭结；双手扶上缘；蓝色拖鞋
湿发白巾裹身侧站|wet-hair white-wrap side view|成年女性侧身站立；白色厚浴巾从腋下完整裹至膝；湿发垂在后肩；双手扶胸前上缘；白色拖鞋
浴巾裹身背面参考|towel-wrap rear view|成年女性背面中性站姿；灰蓝厚浴巾上缘横过背部、下摆至膝；侧交叠不张开；双手在胸前固定；灰色拖鞋
浴巾裹身斜前参考|towel-wrap front three-quarter view|成年女性斜前站姿；米白厚浴巾完整包覆至膝下；前侧交叠和布褶可辨；双手扶上缘；米色拖鞋
宽肩体型浴巾裹身|broad-shoulder towel-wrap reference|成年女性自然宽肩体型；深蓝不透明厚浴巾包至膝部；侧边留足交叠量；双手扶上缘；深蓝拖鞋
丰润体型浴巾裹身|fuller-build towel-wrap reference|成年女性自然丰润体型；浅紫不透明厚浴巾包至膝下；腰腹布褶柔和且前侧完整交叠；双手扶上缘；紫色拖鞋
''',['浴巾裹身','裹浴巾','浴巾','towel wrap'])

block('distressed_outfits','破损位置与叠穿覆盖','''
袖口磨损牛仔夹克|frayed-cuff denim jacket outfit|成年女性穿蓝色牛仔夹克；袖口和领缘轻微磨毛；白色圆领内搭与黑色长裤完整；白色运动鞋
肘部补片旧毛衣|patched-elbow worn sweater outfit|成年女性穿灰色长袖毛衣；肘部磨洞用深灰补片覆盖；蓝色长裤；棕色平底鞋
膝破牛仔裤叠内衬|ripped-knee jeans with lining|成年女性穿白色长袖衬衣和蓝色牛仔长裤；双膝破洞下方有完整灰色布内衬；白色运动鞋
单膝磨破工装裤|single-worn-knee cargo outfit|成年女性穿深绿工装外套与灰色长裤；一侧膝部破口露出完整护膝布片；黑色工作靴
下摆破边长外套|frayed-hem long-coat outfit|成年女性穿深灰长外套；下摆不规则布条仍接在衣缘；高领内搭和长裤完整覆盖；黑色短靴
肩缝脱线衬衣叠内搭|unstitched-shoulder shirt layers|成年女性穿浅蓝长袖衬衣；一侧肩缝少量脱线并露出完整肩部皮肤，内搭主体仍覆盖躯干；深色长裤；黑色平底鞋
袖侧撕裂运动外套|torn-sleeve tracksuit layers|成年女性穿灰色运动外套；一侧袖外缘撕开短口露出深蓝长袖内搭；黑色运动长裤；灰色跑鞋
裙摆撕裂双层连裙|torn-hem double-layer dress|成年女性穿灰紫长袖中长连裙；外裙下摆裂口露出完整不透明内裙；裙腰完整；黑色低跟鞋
背部破口夹克内衬|back-tear jacket lining study|成年女性四分之三背面站姿；棕色夹克后背破口露出完整灰色内衬；黑色长裤；棕色短靴
破边披风完整内衣|frayed-cape layered costume|成年女性穿暗绿破边短披风；灰色长袖衣与黑色长裤完整；布条只在披风边缘；棕色靴
旧化针织开衫搭配|distressed-knit cardigan outfit|成年女性穿米色开衫；袖口和衣下缘有少量松脱针织线；内穿灰色长袖衣和长裤；棕色鞋
磨白开线牛仔套装|worn-seam denim coordinates|成年女性穿浅蓝牛仔外套与长裤；裤侧缝磨白并有短段开线；下方深蓝内衬覆盖；黑色低帮鞋
烧蚀感布边舞台装|scorched-edge stage-clothing effect|成年女性穿灰色长袖外套；黑褐旧化色只在布料下边缘；完整白色内搭和黑色长裤；黑色靴；舞台布料效果
碎边衬衣叠长背心|ragged-shirt long-tank layers|成年女性穿米白破边短袖衬衣；内层深灰长背心完整覆盖躯干；蓝色长裤；白色便鞋
补丁拼接旧工作服|patchwork worn coverall outfit|成年女性穿褐绿长袖连体工装；膝肘有深浅布补片和毛边；腰带完整；棕色工作靴
修补缝线旧旅行装|mended-travel outfit|成年女性穿灰蓝长外套与黑色长裤；肩下和衣摆有清楚的大针脚修补线；高领内搭完整；黑色短靴
''',['破损','破衣','撕裂','磨损','衣物旧化','distressed clothing'])

block('covered_body_views','抱胸遮挡正侧背全身视图','''
标准成年遮胸正面|standard adult covered-chest front|30岁成年女性全身正面中性站姿；仅穿黑色不透明常规三角裤；双手与前臂横抱胸前完整遮挡胸部和乳头；双脚自然落地
标准成年遮胸左侧面|standard adult covered-chest left profile|同类30岁成年女性全身左侧面；仅穿黑色不透明常规三角裤；双手与前臂在胸前完整遮挡、侧面也不露乳头；双脚自然落地
标准成年遮胸背面|standard adult covered-chest rear|同类30岁成年女性全身背面；仅穿黑色不透明三角裤并保持不透明覆盖；双臂仍在身体前方抱胸；双脚自然落地
小个成年遮胸正面|short adult covered-chest front|35岁自然小个体型成年女性全身正面；仅穿深灰不透明常规三角裤；双手与前臂完整遮挡胸部；双脚自然落地
小个成年遮胸右侧面|short adult covered-chest right profile|同类35岁自然小个体型成年女性全身右侧面；仅穿深灰不透明常规三角裤；双手与前臂完整遮挡胸部与乳头；双脚自然落地
小个成年遮胸背面|short adult covered-chest rear|同类35岁自然小个体型成年女性全身背面；深灰不透明三角裤不透明布料覆盖臀部中段；双臂在身体前方抱胸；双脚自然落地
高个成年遮胸正面|tall adult covered-chest front|40岁自然高个体型成年女性全身正面；仅穿深蓝不透明常规三角裤；双手与前臂完整遮挡胸部；双脚自然落地
高个成年遮胸左侧面|tall adult covered-chest left profile|同类40岁自然高个体型成年女性全身左侧面；仅穿深蓝不透明常规三角裤；双手与前臂完整遮挡胸部与乳头；双脚自然落地
高个成年遮胸背面|tall adult covered-chest rear|同类40岁自然高个体型成年女性全身背面；深蓝不透明三角裤不透明布料覆盖臀部中段；双臂在身体前方抱胸；双脚自然落地
丰润成年遮胸正面|fuller adult covered-chest front|45岁自然丰润体型成年女性全身正面；仅穿深棕不透明常规三角裤；双手与前臂完全覆盖胸部；双脚自然落地
丰润成年遮胸右侧面|fuller adult covered-chest right profile|同类45岁自然丰润体型成年女性全身右侧面；仅穿深棕不透明常规三角裤；双手与前臂完全覆盖胸部与乳头；双脚自然落地
丰润成年遮胸背面|fuller adult covered-chest rear|同类45岁自然丰润体型成年女性全身背面；深棕不透明三角裤不透明布料覆盖臀部中段；双臂在身体前方抱胸；双脚自然落地
成年遮胸斜前左视|adult covered-chest front-left view|32岁成年女性全身左斜前中性站姿；仅穿黑色不透明常规三角裤；双手和前臂完整遮挡胸部；双脚自然落地
成年遮胸斜前右视|adult covered-chest front-right view|38岁成年女性全身右斜前中性站姿；仅穿灰色不透明常规三角裤；双手和前臂完整遮挡胸部；双脚自然落地
成年遮胸斜后左视|adult covered-chest rear-left view|42岁成年女性全身左斜后中性站姿；仅穿深蓝不透明三角裤并保持不透明覆盖；双手和前臂保持在胸前遮挡；双脚自然落地
成年遮胸斜后右视|adult covered-chest rear-right view|48岁成年女性全身右斜后中性站姿；仅穿深灰不透明三角裤并保持不透明覆盖；双手和前臂保持在胸前遮挡；双脚自然落地
''',['半裸','抱胸遮挡','不露点','全身正面','全身侧面','全身背面','covered figure reference'])

block('liquid_stained_outfits','舞台与彩色液体浸染','''
血浆点滴白衬衣|stage-blood droplets on white shirt|成年女性穿白色长袖衬衣与黑长裤；衬衣前片少量暗红舞台血浆圆点有大小差异；皮肤与衣物完整；黑色鞋
血浆片状白外套|stage-blood patch on white jacket|成年女性穿白色短外套与灰色内搭长裤；外套下侧一块暗红舞台血浆浸染有柔化边缘；皮肤完整；灰色鞋
血浆拖痕工作衫|stage-blood streaked work shirt|成年女性穿灰色长袖工作衫与黑长裤；袖外侧暗红舞台血浆短拖痕顺布纹延伸；无身体损伤；黑色工作鞋
血浆渗边棉T恤|stage-blood wicking on cotton tee|成年女性穿奶白短袖棉T恤和深蓝长裤；衣前下侧暗红舞台血浆小片外围有浅红渗边；皮肤完整；白色鞋
血浆湿干对比衬衣|wet-dry stage-blood shirt effect|成年女性穿浅灰衬衣与黑长裤；衣片上相邻深红湿色与褐红干色两块布料效果；皮肤完整；黑色鞋
血浆裙摆浸染礼装|stage-blood stained dress hem|成年女性穿深灰不透明长袖及踝连裙；下摆局部暗红舞台血浆浸染顺重力延伸；身体完整；黑色低跟鞋
血浆围裙道具服|stage-blood apron costume|成年女性穿灰色长袖工装与长裤；米白围裙前片带局部暗红舞台血浆染色；身体完整；黑色工作靴
血浆肩下布片装|stage-blood shoulder-panel costume|成年女性穿白色长袖外套与黑长裤；一侧肩下衣片有暗红舞台血浆飞溅点和短流痕；皮肤完整；黑色鞋
蓝漆飞溅工装|blue-paint splattered workwear|成年女性穿米白长袖工装和灰长裤；衣前与袖口有原创蓝色油漆斑点、厚边和小滴；白色工作鞋
黄漆刷痕围裙装|yellow-paint brushed apron outfit|成年女性穿深灰长袖衫和长裤；浅灰围裙前片有黄色不透明油漆刷痕；身体皮肤干净；灰色工作鞋
红漆滴流外套|red-paint drips on jacket|成年女性穿浅蓝短外套与白内搭黑长裤；外套袖侧有鲜红不透明油漆竖向滴流；皮肤干净；黑色鞋
多色漆点工作衫|multicolour paint-speck work shirt|成年女性穿米白宽松长袖衬衣与灰长裤；衣面有蓝黄粉三色小漆点，颜色分区可辨；白色鞋
白漆沾染深色裤装|white-paint stained dark trousers|成年女性穿灰色长袖上衣和深蓝工装长裤；裤前膝下有白色不透明油漆斑；黑色工作靴
绿漆浸边棉外套|green-paint edged cotton jacket|成年女性穿浅灰棉外套与白内搭长裤；衣摆一侧绿色油漆浸染边缘较硬、内部色厚；灰色鞋
粉漆擦抹针织装|pink-paint smeared knit outfit|成年女性穿奶白长袖针织上衣与深灰长裙；袖外侧与下摆有粉色漆料擦抹并留针织纹；白色平底鞋
深漆积边长围裙|dark-paint pooled apron outfit|成年女性穿灰色长袖工装与长裤；米白长围裙下侧深蓝油漆聚成不规则厚边；棕色工作鞋
''',['液体浸染','衣物染色','浸染衣物'])

block('liquid_stained_outfits','饮料与其他液体浸染','''
咖啡圆斑白衬衣|coffee round stain on white shirt|成年女性穿白色长袖衬衣与黑长裤；衣前一块浅棕咖啡圆斑外缘稍深；内搭完整；黑色平底鞋
咖啡顺褶流痕连裙|coffee flow stains on dress|成年女性穿米白长袖中长连裙；前裙局部棕色咖啡流痕随布褶向下；不透明内衬完整；棕色鞋
咖啡袖口浸染外套|coffee-soaked jacket cuff|成年女性穿浅灰外套与白内搭深灰长裤；一侧袖口深棕咖啡浸染有毛细渗边；黑色鞋
咖啡飞溅针织装|coffee-splashed knit outfit|成年女性穿奶白长袖针织衫与深蓝长裤；胸前下侧少量棕色咖啡点沿针织纹扩散；白色便鞋
咖啡半干边界T恤|partly dried coffee tee stain|成年女性穿浅灰短袖T恤与黑长裤；一块棕色咖啡水渍内部浅、边界深；完整不透明内搭；灰色跑鞋
咖啡围裙层次装|coffee-stained apron layers|成年女性穿蓝灰长袖衬衣与长裤；米白长围裙有咖啡点滴及一处浅棕擦痕；棕色工作鞋
咖啡裤侧滴染装|coffee-dripped trouser outfit|成年女性穿白色长袖上衣与米色宽长裤；裤侧有数条棕色咖啡短滴染；布料不透明；白色鞋
咖啡长衣下摆染色|coffee-stained long-shirt hem|成年女性穿米白长衬衣与灰色长裤；衣摆一侧浅棕咖啡浸染边缘不规则；灰色平底鞋
茶水浅金浸染装|tea-water pale-gold stain outfit|成年女性穿奶白长袖衬衣与深蓝长裤；衣片下侧浅金褐茶水色渍边缘柔和；白色鞋
红酒紫红浸染装|red-wine purple stain outfit|成年女性穿浅灰长袖中长连裙；裙前局部紫红酒渍带较深外围；完整不透明内衬；深灰低跟鞋
橙汁橙黄染色装|orange-juice stain outfit|成年女性穿白色短袖上衣与深蓝长裤；衣前下侧橙黄色液体小片浸染与浅色渗边；白色鞋
牛奶白渍深色衣装|milk-like pale stain on dark outfit|成年女性穿深蓝长袖衬衣与灰长裤；衣前下侧不规则奶白色液体干湿斑；衣物不透明；灰色鞋
墨水蓝黑渗染装|blue-black ink-wicking outfit|成年女性穿浅灰长袖工装与黑长裤；袖外侧和前下摆蓝黑墨水点有细分支渗边；黑色工作鞋
泥水裙摆浸染装|mud-water stained skirt outfit|成年女性穿灰蓝长袖上衣与浅灰长裙；裙下摆泥褐色水渍深浅错落并有少量干泥点；棕色短靴
机油深色擦染装|machine-oil stained coverall|成年女性穿米色长袖连体工装；袖口与大腿外侧有深灰机油擦痕和低亮光；身体皮肤完整；黑色工作靴
清水湿斑外套装|clear-water damp-patch jacket|成年女性穿浅蓝长袖棉外套与白内搭黑长裤；衣片有比干布略深的清水湿斑和柔和湿干边界；白色鞋
''',['液体浸染','衣物水渍','咖啡','饮料浸染'])

block('doll_mascot_costumes','人形人偶与材料装扮','''
瓷质关节人偶主题装|porcelain-joint adult doll costume|成年比例女性人偶造型；奶白高领长袖连裙与深色鞋；脸和手呈光滑瓷面；腕部圆形玩偶关节装饰完整连接
木质提线人偶主题装|wooden-marionette adult doll costume|成年比例女性人偶造型；棕色高领长袖衣与直筒长裤；手腕肘部木纹圆轴完整连接；棕色鞋；无悬吊绳场景
布面缝线人偶主题装|cloth-seam adult doll costume|成年比例女性人偶造型；米色布面脸手与外缝线；灰蓝长袖连裙；黑色平底鞋；眼睛为布偶印刷图形
发条背饰人偶主题装|wind-up adult doll costume|成年比例女性人偶造型；深棕长袖上衣与中长裙；小发条装饰以背带固定；棕色系带靴
球形膝关节人偶装|ball-knee adult doll costume|成年比例女性人偶造型；深蓝高领长袖上衣与膝下裙；完整光滑球形膝关节和小腿外壳可辨；深蓝鞋
纸板拼片人偶主题装|cardboard-panel adult doll costume|成年女性穿灰色长袖内衣与长裤；外覆奶白纸板形胸肩与裙片；连接带可见；灰色短靴
橱窗模特人偶装|display-mannequin adult costume|成年比例女性橱窗人偶造型；浅灰无细节面部与手；米色长袖西装和长裤；黑色平底鞋；关节完整
复古服装人偶主题装|vintage-dressed adult doll costume|成年比例女性人偶造型；暗红高领泡袖中长连裙；手腕光滑接缝；小发帽与黑色系带靴
补丁布偶人形装|patchwork adult cloth-doll costume|成年女性穿灰绿长袖连体服；袖口和膝部缝接不同布补片；布面圆领罩头露出成年脸；黑色布鞋
金属铰链人偶主题装|metal-hinge adult doll costume|成年比例女性机械人偶造型；灰白高领连体制服；肘腕和膝部外部铰链完整衔接；灰色短靴
软胶面具人偶主题装|vinyl-mask adult doll costume|成年女性穿浅蓝长袖上衣与长裙；脸部佩戴原创成年面容软胶人偶面罩；拟真肤色表面与人偶服装配合；白色鞋
陶土纹理人偶主题装|clay-texture adult doll costume|成年比例女性人偶造型；米褐陶土质感面手与完整腕部接缝；深绿长袖连裙；棕色平底鞋
透明外壳机械人偶装|clear-shell mechanical adult doll costume|成年比例女性机械人偶造型；不透明灰色高领连体制服；局部透明肩肘外壳内是简化机械块；白色靴
织物娃娃裙人偶装|textile-doll dress costume|成年女性穿奶白长袖上衣与灰紫中长裙；圆领布质罩头露出成年面孔；袖缘缝线与纽扣装饰；棕色鞋
黑白舞台木偶装|black-white adult puppet stage costume|成年比例女性人偶造型；黑白高领长袖连体服；肘膝白色圆关节片接合完整；黑色平底鞋
瓷面彩绘人偶主题装|painted-porcelain adult doll costume|成年比例女性人偶造型；奶白瓷面上有原创细花卉彩绘；浅蓝长袖中长礼裙；白手套和白色鞋
''',['人偶','人形玩偶','舞台人偶','doll costume'])

block('doll_mascot_costumes','卡通玩偶服封闭与脱头套状态','''
白熊玩偶服完全封闭|fully enclosed white-bear mascot suit|成年女性穿完整白熊卡通玩偶服；大圆熊头套、厚熊掌和脚套全覆盖；完全看不到真人头与皮肤；正常站姿
白熊玩偶服只露头部|white-bear suit human head visible|成年女性穿白熊厚玩偶身体、熊掌和脚套；真人成年头部从圆领口露出；没有头套在画面内；仅头部可见
白熊头套单臂抱持|white-bear mascot head held at side|成年女性穿白熊玩偶身体与厚脚套；真人头部露出；单臂把独立大熊头套抱在身侧；另一手自然扶托
白熊头套双手抱持|white-bear mascot head held in both hands|成年女性穿白熊玩偶身体与厚脚套；真人头部露出；双手在腰前抱完整熊头套；手套为厚熊掌形
橘猫玩偶服完全封闭|fully enclosed orange-cat mascot suit|成年女性穿完整橘猫卡通玩偶服；大猫头套、厚猫掌、脚套和短尾都属于衣服；完全看不到真人与皮肤
橘猫玩偶服只露头部|orange-cat suit human head visible|成年女性穿橘猫厚玩偶身体与脚套；真人成年头部从圆领口露出；画面无猫头套；仅头部可见
橘猫头套单臂抱持|orange-cat mascot head held at side|成年女性穿橘猫玩偶身体与脚套；真人头部露出；单臂把完整大猫头套抱在身侧；另一手扶托
橘猫头套双手抱持|orange-cat mascot head held in both hands|成年女性穿橘猫玩偶身体与脚套；真人头部露出；双手在腰前抱完整猫头套；厚手套与衣袖相接
白兔玩偶服完全封闭|fully enclosed white-rabbit mascot suit|成年女性穿完整白兔卡通玩偶服；长兔耳头套、圆掌和脚套完整覆盖；完全看不到真人与皮肤；兔耳也在格内
白兔玩偶服只露头部|white-rabbit suit human head visible|成年女性穿白兔厚玩偶身体、圆掌和脚套；真人成年头部从领口露出；画面无兔头套；仅头部可见
白兔头套单臂抱持|white-rabbit mascot head held at side|成年女性穿白兔玩偶身体与脚套；真人头部露出；单臂把长耳兔头套抱在身侧；头套耳尖完整可见
白兔头套双手抱持|white-rabbit mascot head held in both hands|成年女性穿白兔玩偶身体与脚套；真人头部露出；双手在腰前抱完整长耳兔头套；兔耳不遮住真人脸
绿蛙玩偶服完全封闭|fully enclosed green-frog mascot suit|成年女性穿完整绿蛙卡通玩偶服；原创圆蛙头套与厚手脚套完整覆盖；完全看不到真人与皮肤；正常站姿
绿蛙玩偶服只露头部|green-frog suit human head visible|成年女性穿绿蛙厚玩偶身体与手脚套；真人成年头部从圆领口露出；画面无蛙头套；仅头部可见
绿蛙头套单臂抱持|green-frog mascot head held at side|成年女性穿绿蛙玩偶身体与脚套；真人头部露出；单臂把原创大蛙头套抱在身侧；另一手扶托
绿蛙头套双手抱持|green-frog mascot head held in both hands|成年女性穿绿蛙玩偶身体与脚套；真人头部露出；双手在腰前抱完整蛙头套；独立头套和颈部开口均可辨
''',['卡通玩偶服','人穿玩偶服','玩偶头套','头套在手中','mascot suit'])

block('prosthetic_styling','机械单侧肢体与外壳','''
左前臂机械义肢日常装|left-forearm prosthesis everyday look|成年女性穿灰色短袖上衣与黑长裤；仅左肘以下为完整银灰机械义肢和五指手；右臂自然；黑色鞋
右前臂机械义肢外套装|right-forearm prosthesis jacket look|成年女性穿卷袖蓝色夹克与长裤；仅右前臂为深灰机械义肢和五指手；完整套筒连接在肘下；左臂自然；白色鞋
左全臂机械义肢造型|left-full-arm prosthesis look|成年女性穿完整高领无袖上衣与黑长裤；仅左臂从完整肩部外套筒连接至五指机械手；右臂自然；黑色鞋
右全臂机械义肢造型|right-full-arm prosthesis look|成年女性穿完整高领无袖灰衫与蓝色长裤；仅右臂有完整肩套筒、机械肘和五指手；左臂自然；白色鞋
左仿生外壳前臂义肢|left-biopanel forearm prosthesis|成年女性穿白色短袖衬衣与灰长裤；仅左前臂为米白流线外壳义肢，五指轮廓清楚；右臂自然；灰色鞋
右工业风前臂义肢|right-industrial forearm prosthesis|成年女性穿深绿短袖工装与黑长裤；仅右前臂为深灰分片机械义肢，外部关节和五指手完整；左臂自然；黑色靴
左轻量全臂义肢外观|left-lightweight full-arm prosthesis|成年女性穿米灰高领无袖上衣与长裤；仅左臂为完整浅灰外壳义肢、机械肘与五指手；右臂自然；白色鞋
右科幻全臂义肢外观|right-sci-fi full-arm prosthesis|成年女性穿深灰高领无袖上衣与长裤；仅右臂为完整黑白几何机械义肢和五指手；左臂自然；黑色鞋
左小腿机械义肢日常装|left-below-knee prosthesis everyday look|成年女性穿灰色短袖上衣与及膝短裤；仅左膝下为完整银灰机械小腿与脚部；右腿自然穿鞋；左脚外壳有鞋形轮廓
右小腿机械义肢日常装|right-below-knee prosthesis everyday look|成年女性穿白色短袖衬衣与及膝短裤；仅右膝下为完整黑灰机械小腿与脚部；左腿自然穿鞋；连接套筒覆盖完整
左大腿机械义肢造型|left-above-knee prosthesis look|成年女性穿深蓝短袖上衣与不透明及大腿中段短裤；仅左侧有完整上段套筒、机械膝、小腿与脚；右腿自然穿鞋
右大腿机械义肢造型|right-above-knee prosthesis look|成年女性穿灰色短袖上衣与不透明及大腿中段短裤；仅右侧有完整上段套筒、机械膝、小腿与脚；左腿自然穿鞋
左白色外壳小腿义肢|left-white-shell lower-leg prosthesis|成年女性穿米白短袖上衣与灰色及膝短裤；仅左膝下为奶白流线外壳义肢与完整脚形；右腿自然穿白鞋
右工业外壳小腿义肢|right-industrial lower-leg prosthesis|成年女性穿深绿短袖工装与及膝短裤；仅右膝下为深灰外壳和完整机械脚；左腿自然穿黑色靴；完整连接无创口
左科幻全腿义肢外观|left-sci-fi full-leg prosthesis|成年女性穿黑色短袖上衣与不透明及大腿中段短裤；仅左侧为完整浅灰上段套筒、机械膝小腿与脚；右腿自然穿鞋
右简洁全腿义肢外观|right-minimal full-leg prosthesis|成年女性穿灰蓝短袖上衣与不透明及大腿中段短裤；仅右侧为完整黑灰上段套筒、机械膝小腿与脚；左腿自然穿鞋
''',['机械单只腿部','机械手臂','手臂义肢','腿部义肢','单侧义肢','prosthesis'])

block('plush_holds','玩偶尺寸与抱持支撑','''
双手抱小熊玩偶|holding a small bear plush|成年女性穿灰色高领长袖衣与深蓝长裤；双手在胸前抱小熊毛绒玩偶；玩偶约为人物身高六分之一；白色鞋
双臂抱中熊玩偶|holding a medium bear plush|成年女性穿灰色高领长袖衣与深蓝长裤；双臂在腹胸前抱中熊毛绒玩偶；玩偶约为人物身高三分之一；白色鞋
双臂抱大熊玩偶|holding a large bear plush|成年女性穿灰色高领长袖衣与深蓝长裤；双臂支撑大熊毛绒玩偶躯干；玩偶约为人物身高五分之三；脚和人物脸均可见
双手抱小兔玩偶|holding a small rabbit plush|成年女性穿米白长袖衣与黑长裤；双手在腹前抱小型长耳兔玩偶；玩偶约为人物身高六分之一；灰色鞋
双臂抱中兔玩偶|holding a medium rabbit plush|成年女性穿米白长袖衣与黑长裤；双臂抱中型长耳兔玩偶；玩偶约为人物身高三分之一；兔耳不挡脸；灰色鞋
双臂抱大兔玩偶|holding a large rabbit plush|成年女性穿米白长袖衣与黑长裤；双臂支撑大型长耳兔玩偶；玩偶约为人物身高五分之三；全部耳尖与脚都可见
双手抱小猫玩偶|holding a small cat plush|成年女性穿灰蓝长袖衣与深灰长裤；双手抱小橘猫毛绒玩偶；玩偶约为人物身高六分之一；白色鞋
双臂抱中猫玩偶|holding a medium cat plush|成年女性穿灰蓝长袖衣与深灰长裤；双臂抱中橘猫毛绒玩偶；玩偶约为人物身高三分之一；白色鞋
双臂抱大猫玩偶|holding a large cat plush|成年女性穿灰蓝长袖衣与深灰长裤；双臂托住大橘猫毛绒玩偶的腹部；玩偶约为人物身高五分之三；人物脸与脚可见
双手抱小熊猫玩偶|holding a small panda plush|成年女性穿深绿长袖衣与黑长裤；双手在胸前抱小熊猫毛绒玩偶；玩偶约为人物身高六分之一；黑色鞋
双臂抱中熊猫玩偶|holding a medium panda plush|成年女性穿深绿长袖衣与黑长裤；双臂抱中熊猫毛绒玩偶；玩偶约为人物身高三分之一；黑色鞋
双臂抱大熊猫玩偶|holding a large panda plush|成年女性穿深绿长袖衣与黑长裤；双臂托住大熊猫毛绒玩偶；玩偶约为人物身高五分之三；人物脸和双脚可见
双手抱星星小玩偶|holding a small star plush|成年女性穿灰色长袖衣与蓝长裤；双手抱小型软星星玩偶；玩偶约为人物身高六分之一；白色鞋
双臂抱圆鲸中玩偶|holding a medium whale plush|成年女性穿米白长袖衣与灰长裤；双臂横抱中型圆鲸毛绒玩偶；玩偶长约为人物身高三分之一；灰色鞋
双臂抱萝卜大玩偶|holding a large carrot plush|成年女性穿灰蓝长袖衣与黑长裤；双臂斜抱大型软萝卜玩偶；玩偶长约为人物身高五分之三；人物脸与双脚可见
单臂抱中狗玩偶|holding a medium dog plush at side|成年女性穿深灰长袖衣与蓝长裤；一臂从下方托住中型毛绒小狗、另一手扶侧面；玩偶约为人物身高三分之一；白色鞋
''',['手抱玩偶','抱玩偶','抱毛绒玩具','大中小玩偶','plush hold'])

# Stage ranges are editorial character settings, never an age-estimation system.
STAGES=[
    ('newborn','新生儿0—1个月',0,1/12,'婴幼儿','newborn baby girl','圆润头部、稀疏细发、眼睑自然，采用轻度写实婴儿脸而非成年脸缩小','闭合长袖连体衣包覆躯干四肢与脚，平躺在简洁浅色软垫上，头颈有平稳支撑'),
    ('infant','婴儿约6个月',.5,.5,'婴幼儿','six-month-old baby girl','圆润面颊、短细发和自然婴儿五官，颈肩由画面下方软垫承托','宽松长袖包脚连体衣，安全半躺在简洁软垫上，双手自然放在身体旁'),
    ('one_year','幼儿约1岁',1,1,'婴幼儿','one-year-old girl','幼儿圆润面颊与短细发，五官保持幼儿比例，普通圆领衣缘可见','宽松长袖上衣与长裤袜鞋，坐在低软垫上，头大身短的幼儿作画比例自然'),
    ('three_years','幼儿约3岁',3,3,'婴幼儿','three-year-old girl','圆润幼儿脸与柔软短发，眼鼻口清楚，普通圆领衣缘可见','宽松长袖T恤与长裤运动鞋，稳稳站立，四肢和手脚采用幼儿比例'),
    ('six_years','儿童约6岁',6,6,'儿童','six-year-old girl','儿童面部轮廓与自然短发，普通高圆领衣缘，表情平静','普通宽松卫衣、长裤与运动鞋，站姿自然，头身关系采用儿童创作比例'),
    ('nine_years','儿童约9岁',9,9,'儿童','nine-year-old girl','儿童脸部略拉长但仍保留儿童五官关系，自然侧分发，普通圆领衣缘','普通长袖衬衣外加宽松开衫、长裤和运动鞋，手脚体积与儿童比例一致'),
    ('twelve_years','青少年12—14岁',12,14,'青少年','girl aged twelve to fourteen','青少年自然脸型与普通短发，五官表现克制，高圆领日常上衣衣缘可见','宽松长袖卫衣与直筒长裤、平底运动鞋，中性站姿，不强调身体曲线'),
    ('fifteen_years','青少年15—17岁',15,17,'青少年','girl aged fifteen to seventeen','青少年自然五官与齐肩发，高圆领日常上衣衣缘，避免成人浓妆','宽松高圆领长袖上衣与直筒长裤、运动鞋，头身比例自然，中性站姿'),
    ('young_adult','青年成人18—24岁',18,24,'成人','young adult woman aged eighteen to twenty-four','明确成年五官，面部结构自然且保留柔和肤质，普通圆领衣缘','普通长袖衬衣、直筒长裤与平底鞋，成年骨架与自然中性站姿'),
    ('adult_25','成人25—34岁',25,34,'成人','adult woman aged twenty-five to thirty-four','明确成人面部结构和自然皮肤细节，发型简单，普通高圆领衣缘','普通高圆领长袖上衣、长裤和平底鞋，自然成年体型与放松站姿'),
    ('adult_35','成人35—44岁',35,44,'成人','adult woman aged thirty-five to forty-four','自然成人面部体积与轻微个体肤质变化，不用浓重皱纹强行标龄','普通长袖上衣与宽松开衫、直筒长裤和平底鞋，体态自然'),
    ('adult_45','成人45—54岁',45,54,'成人','adult woman aged forty-five to fifty-four','自然成人眼周与口周纹理轻度可辨，深色发可保留，普通衣领','普通长袖衬衣与长裤和平底鞋，保留多样体型中的一种自然站姿'),
    ('adult_55','成人55—64岁',55,64,'成人','adult woman aged fifty-five to sixty-four','自然眼周与口周纹理，少量灰发可混入，面部神态平静，完整普通衣领','长袖针织上衣与直筒长裤、平底便鞋，站姿稳定，不把年龄等同虚弱'),
    ('older_65','年长成人65—74岁',65,74,'年长成人','older woman aged sixty-five to seventy-four','灰发与深发混合，眼周口周自然纹理和面颊体积变化，普通衣领','普通长袖衬衣外加开衫、长裤和平底鞋，站姿可挺拔，双手自然放置'),
    ('older_75','年长成人75—84岁',75,84,'年长成人','older woman aged seventy-five to eighty-four','银灰发与自然面部褶纹并存，保留个人五官和温和平静表情，普通衣领','普通长袖上衣与开衫、宽松长裤和平底鞋，重心稳定，手部纹理自然'),
    ('older_85','高龄成人85岁及以上',85,None,'年长成人','elderly woman aged eighty-five or older','白灰发与较清楚的自然褶纹，头颈比例完整，保留个人面容而非统一衰老符号','完整长袖日常衣物、长裤与平底鞋，舒适站姿和稳定重心，不强制配拐杖')
]
for view,dimension in [('portrait','年龄阶段头部与面容'),('fullbody','年龄阶段全身与体态')]:
    for ident,label,low,high,group,en,face,body in STAGES:
        minor=low<18
        name=label+('头部参考' if view=='portrait' else '全身参考')
        feature=face if view=='portrait' else body
        add('female_life_stages',dimension,f'{name}|{en} {view} reference|{feature}。年龄区间是角色设定，外观仅为一种原创作画示例。')
        CATALOG[-1].update(added_in='21.0',life_stage_reference=True,age_min=low,age_max=high,
            age_range=label,age_stage=ident,life_stage_group=group,view_type=view,minor_reference=minor,
            adult_only=not minor,age_context=label+'；适龄完整日常着装',
            aliases=['女性各年龄段','女性年龄阶段','年龄图鉴',group,label,'female life stages'],reference_ids=['R81','R82','R09'],
            note='年龄数字为创作设定标签，不能仅凭面容精确判断年龄；身高、肤质、发色与体态均有个体差异。所有年龄使用完整适龄日常着装，图例不是生长或健康评估标准。')

assert sum(bool(e.get('special_variant_reference')) for e in CATALOG)==144
assert sum(bool(e.get('life_stage_reference')) for e in CATALOG)==32
