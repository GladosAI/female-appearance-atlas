"""Persistent hosiery overview and the current illustrated addition index."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path
from hosiery_expansion import DENIER_NOTE

def write_hosiery_docs(root,data):
    root=Path(root)
    entries=[e for e in data['entries'] if e.get('hosiery_reference')]
    additions=[e for e in entries if e['category']=='hosiery']
    refs={r['id']:r for r in data['references']}
    dimensions=list(dict.fromkeys(e['dimension'] for e in additions))
    intro=f"# 袜类、丝袜与袜裤图鉴\n\n共 {len(entries)} 项，覆盖 {len(dimensions)} 个细分，包含基础袜型、D数、袜长、织纹、固定结构、袜裤、装饰与幻想主题，每项均有对应图例。\n\n"
    intro+='打开 [袜类总览](index.html?section=socks)，也可查看 [袜类新增分类](index.html?section=hosiery)。选择细分，或搜索20D、吊带袜、自持袜、袜裤、踩脚、五趾、袜套等词。\n\n'
    intro+='## D数、透感与结构\n\n'
    intro+=f"{DENIER_NOTE} D（denier，丹尼尔）数值对应9000米纱线的克重。低D到高D图页采用同尺度灰腿模与黑色袜料比较大致外观；相邻D数可能外观接近，不能凭图鉴识别真实产品D数。\n\n"
    intro+=f"[纱线单位说明]({refs['R66']['url']}) · [透感、织法、颜色与拉伸说明]({refs['R67']['url']})\n\n"
    intro+='吊带长袜是两只分开的袜子，由腰带吊带及夹扣连接；自持长袜用袜口内侧固定结构，本图示硅胶条型。连裤袜有相连的裤身与两腿。无足袜裤脚踝开放；踩脚袜裤在足弓下保留环；无足袜套是单独的腿筒。袜料的D数、袜长、表面光泽与花纹可以分别组合。\n\n'
    intro+='## 分类索引\n\n| 细分 | 细分数量 | 比较重点 |\n| --- | ---: | --- |\n'
    focus={
        '基础袜型与袜套':'袜长、包足与无足轮廓',
        '丝袜D数与透感参考':'D数与袜料边缘，透感另记',
        '袜长与趾部轮廓':'袜口相对踝、小腿、膝、大腿的位置',
        '针织材质与日常袜':'织纹、圈绒、毛感与袜套开口',
        '吊带袜与自持袜结构':'夹点、带数、调节扣与硅胶内侧',
        '连裤袜与打底袜裤版型':'腰口、裤身、脚袋与足底开口',
        '网眼花纹与装饰袜':'网眼大小、图案方向与装饰连接',
        '袜面图案与边口设计':'印花、刺绣、拼缝与袜口',
        '运动、舞蹈与分区袜型':'局部开口、织片分区与足部包覆',
        '鞋袜叠穿与佩戴对照':'袜口、鞋口与脚踝的遮挡关系',
        '图案与拼接袜裤':'织纹连续性、图案转折与拼色边界',
        '主题装饰与幻想袜型':'主题饰件、布料边缘与固定点',
    }
    for dim in dimensions:
        tip=focus.get(dim,'袜长、材质、结构与穿着效果')
        intro+=f"| {dim} | {sum(e['dimension']==dim for e in additions)} | {tip} |\n"
    intro+='\n图页由内置image_gen制作，包含服装产品、成人规格腿模与成年人物穿着示意；材质名称是绘画与成品结构参考。\n\n'
    def illustrated(group):
        text='';shown=set()
        for dim in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dim]
            text+=f"## {dim} · {len(subset)} 项\n\n"
            ids={e['visual']['board'] for e in subset}
            for board in data['boards']:
                if board['id'] in ids and board['id'] not in shown:
                    shown.add(board['id']);text+=f"![{board['title']}]({board['image']})\n\n"
            text+='| 编号 | 名称 | English | 可见特征 |\n| --- | --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
            text+='\n'
        return text
    new_ids={e['id'] for e in additions}
    ordered=additions+[e for e in entries if e['id'] not in new_ids]
    ending='## 参考入口\n\n'
    for key in ['R66','R67','R68']:
        r=refs[key];ending+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    ending+='\n[第14版图页提示词](image-prompts-v14.json) · [完整服装专辑](clothing-atlas.md) · [全部外观图鉴](atlas.md) · [来源说明](sources.md)\n'
    (root/'docs/socks-atlas.md').write_text(intro+illustrated(ordered)+ending,encoding='utf-8')
