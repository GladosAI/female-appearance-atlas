"""Illustrated adult female anthro morphology index and tier comparison guide."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path
from anthro_expansion import ANTHRO_CATEGORIES, LEVELS

def write_anthro_docs(root,data):
    root=Path(root)
    entries=[e for e in data['entries'] if e.get('anthro_reference')]
    new=[e for e in entries if e['category'] in ANTHRO_CATEGORIES]
    refs={r['id']:r for r in data['references']}
    hybrids=[e for e in entries if e.get('hybrid_reference')]
    text=f"# 兽娘与福瑞外观图鉴\n\n共 {len(entries)} 项，包含兽化专题 {len(new)} 项、复合躯体 {len(hybrids)} 项，完整四足动物4项，以及已有16项自然耳角、尾翼、鳞毛和瞳孔参考。程度对照、兽脸毛纹、自然耳尾与爪足、物种原型各32项，每项有图。\n\n"
    text+='[完全动物体态与四足装饰](../index.html?section=quadruped_forms)保留完整动物头颈与横向躯干，四脚着地；小马、狐狸与猫仅配少量装饰。它与BS016双足马型、HY017人形上身半人马分别归类，不修改L1—L8含义。\n\n'
    text+='[半人形与复合躯体](../index.html?section=hybrid_body_forms)展示蛇尾、鱼尾、四足兽体、节肢和触腕等下身结构，不套用双足兽化程度分档。\n\n'
    text+='打开 [兽娘与福瑞总览](index.html?section=anthro)，或 [程度对照](index.html?section=anthro_levels)、[兽脸与毛纹](index.html?section=anthro_heads)、[耳尾与肢体](index.html?section=anthro_parts)、[物种原型](index.html?section=anthro_species)。搜索兽化1档至兽化8档或L1至L8，可看对应的猫、狐、狼、兔四种比较例。\n\n'
    text+='## 8档创作对照\n\n这些是本图鉴的形态标签，不是生物比例、演化顺序或福瑞社群的统一标准。兽脸、手足、被毛、体态可以分别选择，例如采用完整狐头，同时保留人形操作手与跖行足。\n\n'
    text+='| 档位 | 名称 | 本档观察重点 |\n| --- | --- | --- |\n'
    for level in LEVELS:text+=f"| L{level['id']} | {level['name']} | {level['guide']} |\n"
    text+='\n程度图用相近的普通外套与长裤对照，按自然兽化部位区分。兽耳、尾、翼和毛爪属于角色的幻想身体形态；[Cosplay专题](cosplay-atlas.md)中的发箍、挂尾、假毛、翼架属于穿戴部件。两者可在设计中组合，连接方式应明确。\n\n'
    text+='## 组合时记录\n\n记录头脸与吻部、耳的位置及数量、被毛/鳞羽区域、操作手的指型、足部接地方式、尾翼根部及服装开口。趾行图突出抬高的踝跟与趾部支撑，避免把膝画成反向折弯。鸟足、分蹄、单蹄及拟人四指/五指手分别标注；这里的双足与操作手是角色创作改编，不能当真实动物的解剖标准。\n\n'
    text+='鳞羽、水生、昆虫与龙、狮鹫等作为拟人形态拓展单列，保留可识别的种类特征；不给每种角色都套猫耳与猫尾。物种特征不决定角色的性格或行为。直立及半人形图采用成年女性幻想角色与普通完整服装；完整四足图保留动物身体，仅配少量饰物，不套用人类身体或年龄。\n\n'
    shown=set()
    order=sorted(data['categories'],key=lambda c:(c['id'] not in ANTHRO_CATEGORIES,[x['id'] for x in data['categories']].index(c['id'])))
    for category in order:
        group=[e for e in entries if e['category']==category['id']]
        if not group:continue
        text+=f"## {category['name']} · {len(group)} 项\n\n"
        for dimension in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dimension];text+=f"### {dimension}\n\n"
            ids={e['visual']['board'] for e in subset}
            for board in data['boards']:
                if board['id'] in ids and board['id'] not in shown:
                    shown.add(board['id']);text+=f"![{board['title']}]({board['image']})\n\n"
            text+='| 编号 | 名称 | English | 可见特征 |\n| --- | --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
            text+='\n'
    text+='## 参考入口\n\n'
    for key in ['R69','R70','R71','R72','R163','R164','R165']:
        r=refs[key];text+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    text+='\n配图由内置image_gen独立制作，未复制参考教程图像。\n\n[第16版图页提示词](image-prompts-v16.json) · [全部外观图鉴](atlas.md) · [面部专题](facial-atlas.md) · [来源说明](sources.md)\n'
    (root/'docs/anthro-atlas.md').write_text(text,encoding='utf-8')
