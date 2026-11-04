"""Create supplementary wearing sheets without adding duplicate catalog entries."""
from pathlib import Path
import sys,json
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
root=_bootstrap.ROOT
entries={e['id']:e for e in json.loads((root/'source/expanded-entries.json').read_text(encoding='utf-8'))}
rules=[
 ('hair_accessories',1,16,'发箍与发带佩戴',[
 '侧面：齿梳发箍从耳后沿头顶弧线压入后梳发根，小齿与发流接触',
 '斜前面：宽缎面包布发箍实际贴合头顶，两脚藏在耳后',
 '斜前面：软垫隆起发箍位于齐刘海后方，内弧贴头',
 '斜前面：中央扭结布箍贴住头弧，扭结是箍面的一部分',
 '斜前面：单侧短尾蝶结固定在贴头弧箍的一侧，箍脚在耳后',
 '斜侧面：双轨细箍两条轨道平行贴头弧，端点位于耳后',
 '斜前面：细波浪金属箍顺头弧插在顶发内层，不跨过眼睛',
 '斜前面：链节在柔性箍骨表面，内层贴合头发，耳后端点合理',
 '斜前面：一排小珠沿真实头箍排列，珠根接在头箍上',
 '斜前面：布花簇在发箍单侧，另一侧箍骨沿头部延伸',
 '斜前面：完整蕾丝衬底软发带绕过头部，发层从带侧露出',
 '斜前面：两条软布带在额上交叉，环绕到脑后，额前有完整发际线',
 '斜后面：头巾带环绕头部后打结，两个长尾完整留在肩上，不画成松脱布条',
 '斜侧面：运动针织宽发带沿发际绕头，露出高丸子与耳部',
 '斜后面：环形编绳发带贴合发层，脑后调节结与完整短尾可见',
 '斜前面：细链额饰沿发际绕行，中央小垂饰位于额上，眼睛不被覆盖']),
 ('hair_accessories',17,32,'发卡与发夹佩戴',[
 '斜侧面：按压弹片发卡闭合夹住耳上真实发片，未处于空中张开状态',
 '斜后面：长方背夹横向夹合两侧汇拢的半扎束，弹簧夹条藏在发束后',
 '斜前面：两枚小一字夹交叉夹住同一侧发片，夹脚沿发流',
 '侧面：单枚波纹一字夹贴住侧发，波纹与平直夹片真实夹合',
 '斜侧面：短双齿侧夹夹住耳上小发束，饰面和发片接触',
 '侧面：鸭嘴夹闭合固定侧刘海，细夹体沿发流，尾端铰接可见',
 '斜侧面：鳄鱼齿口夹闭合咬住一侧发片，局部放大齿口接触发片',
 '斜后面：大齿抓夹实际闭合包住法式扭发，齿口在发束两侧',
 '斜后面：小圆壳抓夹固定后脑半扎点，下半齐肩发披散',
 '斜后面：蝶形抓夹两翼是按柄，两组抓齿夹住实际半扎发束',
 '背面略侧：三角空框背夹固定两侧后拢发片，后夹条真正夹住发束',
 '斜后面：布结横条发卡固定半扎束，布结下可见部分横条夹体',
 '斜后面：圆盘转扣发卡固定后脑低位半扎点，发束从扣体下连续垂落',
 '斜前侧面：小型包布磁夹片夹在单侧发片上，两片贴合，贴发不悬浮',
 '斜侧面：短珠链侧夹固定耳上发片，珠链完整垂在侧发外，不遮眼',
 '斜后面：梳齿侧插发卡插入一侧低盘髻上缘，饰面露在发层外']),
 ('hair_accessories',33,48,'发簪发钗与梳饰佩戴',[
 '斜后面：圆头素簪横斜穿入低盘髻，簪头与短露出端分别在髻两侧',
 '斜后面：U形双叉插入同一竖向扭髻，U顶露在上端',
 '斜后面：两根平行发钗杆从同侧进入高髻，饰头和露出端清楚',
 '斜后面：螺旋盘发针旋在圆髻内，仅顶部露出；放大入髻处，原图为单杆装饰变体',
 '斜侧后面：叶形簪扁杆穿入侧低髻，叶片饰头位于髻外',
 '斜后面：月形簪弯杆穿过低卷髻，月形饰头露在侧上方',
 '斜后面：花头簪插入辫盘髻，小短链自然垂落且不穿过头部',
 '斜后面：珠顶双链步摇改编插在高髻侧边，两挂点与完整短链可见',
 '斜后面：环顶发簪横穿扁盘髻，完整圆环饰头在发层外',
 '斜后面：枝形发簪杆插入松卷低髻，短枝饰头位于发层外',
 '斜后面：薄饰板贴在盘髻表面，独立长杆穿过板孔并固定发束',
 '斜后面：珠边横梳的梳齿插入低髻上缘，横弧珠边露出',
 '斜后面：镂空宽弧梳的短齿插入盘髻边缘，宽弧饰板贴合头部曲面',
 '斜侧后面：细齿花梳插入法式竖髻侧边，小花簇和齿根可辨',
 '斜后面：低盘髻外罩发网，簪杆穿过网边圈及髻根，发网贴住发团',
 '斜后面：原创折叠叉骨盘发夹合拢固定低髻，后扣和饰面在髻外可见']),
 ('hair_accessories',49,64,'发圈与固定件佩戴',[
 '斜后面：无接缝细圈围绕高马尾根部，放大图显示圈体围住真实发束',
 '斜后面：宽扁弹力圈平贴短低马尾根，带面平整，发束在圈内收拢',
 '斜后面：米色布褶甜甜圈发圈扎低马尾，褶布在弹力内圈外侧',
 '斜后面：大蝶结固定在弹圈外，弹圈真正围住半扎束根',
 '斜后面：布圈扎根并接两条长飘带，带尾完整留在肩部范围',
 '斜侧后面：双珠绳扣圈围束低马尾根，两珠在外侧相扣且绳圈可见',
 '斜后面：电话线螺旋圈围成连续闭环抱住半扎束，放大细连续线圈',
 '斜后面：钩端弹绳只绕高马尾根，小钩固定在绳圈内，放大钩与圈接触，无游离垂钩',
 '斜后面：小滑扣调整低马尾发绳圈，短止端完整，滑扣和发束直接接触',
 '斜后面：软管包芯发圈围束根部，布管表面包住实际弹性内圈',
 '斜后面：花形布团在弹圈外侧，中央弹圈扎住高丸子髻根',
 '斜后面：小珠链在弹力圈外作为装饰，实际弹性段围住低尾束根',
 '斜后面：金属壳套筒是发圈外的短开合壳，发束从中央连续穿出，放大壳与圈',
 '斜后面：原创双环连接件用两个相邻上下圈固定同一条低马尾的相邻两段，短连接片在同一尾束旁，不连接左右双马尾',
 '斜侧后面：包布发尾扣扣住侧辫末端，下方短发尾自然散开，放大侧扣',
 '斜后面：丝巾绕在低马尾发圈外打结，两条短巾尾完整，放大丝巾结与弹圈']),
 ('eyewear',1,16,'眼镜与镜片佩戴',[
 '斜前面：细金属圆框眼镜，完整圆镜圈，透明镜片后眼睛清楚，鼻托落在鼻梁两侧',
 '斜前面：粗黑板材方框，镜圈厚、方角明确，镜腿从铰链延伸到耳上',
 '斜前面：横向椭圆镜框，椭圆镜片明显宽于高，鼻梁与镜腿贴合',
 '斜前面：猫眼框外上角明显上扬，双眼在透明镜片后，保持鼻梁支点',
 '斜前面：六边形镜圈有清楚六段直边，镜腿接在两侧，透明镜片',
 '斜前面：眉线框上缘厚、下缘为细金属圈，鼻梁连接完整',
 '斜前面：上半框条固定镜片，下缘透明细线，不画成完整金属下框',
 '斜前面：全无框眼镜只有透明镜片及小孔固定件，鼻梁和镜腿可见',
 '斜前面：透明水滴飞行镜片与双鼻梁，细金属镜圈，双眼可见',
 '斜前面：较小圆形深色太阳镜，窄桥细腿，完整镜片均匀较暗',
 '斜前面：较大的方形深色墨镜，粗板材框和宽镜腿，明显方形轮廓',
 '斜前面：镜片从上深下浅平顺渐变，下部双眼轮廓可见，镜圈固定完整',
 '斜前面略侧：普通眼镜上有一层翻起的深色太阳夹片，小夹点、内层透明镜片和外层夹片均可见',
 '侧前面：运动镜片弧面包向面侧，鼻托贴合、镜腿沿两侧延伸到耳后',
 '斜前面：单枚圆形单片眼镜嵌在一侧眼眶，细链从下缘完整垂到衣领附近，另一眼无遮挡',
 '斜前面略侧：双目护目镜软边贴脸，两片镜片独立，弹性头带绕到脑后，在侧面可见'])]
new=[]
for category,first,last,title,instructions in rules:
    prefix='HR' if category=='hair_accessories' else 'EG';es=[entries[prefix+f'{i:03}'] for i in range(first,last+1)];assert len(es)==len(instructions)==16
    ident='wear-'+prefix.lower()+f'{first:03}-'+prefix.lower()+f'{last:03}'
    prompt='V30 SUPPLEMENTARY WEARING REFERENCE, not loose products. Portrait1024x1536, EXACT4 columns by4 rows,16 cells in row-major order. Thin straight grey grid lines at x256/512/768 and y384/768/1152. Exact small item IDs at upper left, no other text. Same polished professional anime technical illustration on ivory background. Every cell shows the exact named accessory actually WORN by a clearly MATURE ADULT woman age25-40, natural adult head proportions, complete opaque plain grey high-neck clothing. Main view is a large complete head/shoulder or head-to-hair-end portrait; full crown, accessory and every hair/cord/chain end fit inside cell. No chibi or childlike face, no school uniform. Actual contact at roots/temples/nose/ears must be readable, not tiny accessory icons or floating isolated products. One small circular detail inset may magnify the SAME actual attachment when needed, not another head. Follow exact named front/side/rear view. Do not hide back clips or pins behind a front face. Hair bands and eye frames follow curvature, clips close around hair, pin shafts enter HAIR BUN not flesh. Glasses bridge rests on nose, temples reach ears, lenses aligned to eyes with appropriate occlusion and subtle reflections. No logos, extra unrelated accessories or famous-character resemblance. Existing construction descriptions may describe an open product; MAIN wearing view must show closed/fastened use.\nOrdered cells:\n'
    for i,(e,wear) in enumerate(zip(es,instructions)):
        prompt+=f"Cell{i+1}, label {e['id']}: {e['name']} / {e['en']}. Wearing target: {wear}. Product structure context only: {e['description']}\n"
    prompt+='Critical: show16 distinct correct accessories actually worn, including physical fastening and complete ends, without crossing cell boundaries.'
    new.append(dict(id=ident,edition=30,role='wearing_reference',category=category,dimension=title,title=title+' · 佩戴参考',columns=4,rows=4,entries=[{k:e[k] for k in ['id','name','en']} for e in es],image='images/'+ident+'.png',prompt=prompt))
p=root/'source/image-jobs.json';jobs=json.loads(p.read_text(encoding='utf-8'));assert not any(j['id'] in {n['id'] for n in new} for j in jobs)
p.write_text(json.dumps(jobs+new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(root/'source/wearing-reference-jobs-v30.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'supplemental_jobs':len(new),'existing_entries_covered':sum(len(j['entries']) for j in new)}))
