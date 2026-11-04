"""Browsable source-linked expansion index."""
from urllib.parse import quote

def write_scholar_myth_v53_docs(root,data):
    text='''# 学术、环境、地域文化与神话拟人扩充

[本轮64项](../index.html?section=clothing_new) · [完整目录](directory.md) · [生成提示词与原图路径](../prompts/image-prompts-v53.json)

新增8个类别、64项配图、16张系统示例外观卡。采用内置 image_gen 制作16张原创四格图页，每项有独立实测裁剪。图为成年角色外观设计示意。

## 分类与取舍

| 内容 | 目录归属 | 数量 |
| --- | --- | ---: |
| 学术、书呆子、博士、科研 | 职业与户外作业 → 学术、书卷气与科研身份 | 12 |
| 丛林、雨林、沙漠、荒原 | 职业与户外作业 → 丛林、沙漠与环境行装 | 8 |
| 原始、史前幻想 | 传统、国风与年代 → 史前与原始幻想装束 | 4 |
| 牛仔、西部与牧场 | 传统、国风与年代 → 西部牛仔与牧场造型 | 4 |
| 萨米、因纽特、马普切、毛利 | 传统、国风与年代 → 原住民族与地域文化服饰参考 | 4 |
| 北欧现代、户外与维京结构 | 传统、国风与年代 → 北欧日常、户外与历史灵感 | 8 |
| 美杜莎、雅典娜、维纳斯与其他神话拟人 | 魔法、仪式与幻想身份 → 经典神话与拟人化形象 | 16 |
| 水、凝胶、金属、墨、熔流等 | 兽娘、福瑞与幻想形态 → 液态、流体与凝胶人形 | 8 |

博士学位礼袍与博士日常研究工作分开；科研覆盖实验、计算、生态田野与天文观测。书呆子是服装、携物与表演标签，不能依据外貌推断学历或能力。原始一词收在虚构史前材料语言中；当代原住民族分别标注族群与地区，不与史前混为一类。

萨米服饰有地区和家族差异，本图为简化结构示意；因纽特组显示女性阿毛提的后帽、后背空间与衣摆；马普切组侧重包裹织裙与固定针；毛利凯塔卡组为素面细纤维披衣与边饰，区别于羽毛披衣。具体细节请结合下列原始馆藏查证，不作为复原图纸。

美杜莎保留蛇发和人类双腿，既有蛇尾女仍在复合躯体类别。雅典娜、维纳斯、阿耳忒弥斯和芙蕾雅为原本女性神祇的造型改编；奥丁、雷神两项明确是女性化重设计。翼冠女武神属于幻想图像，不作维京时代实物头盔。日月、春、海洋及凤凰、独角兽、狮鹫、石像鬼另列拟人组。液态形态以轮廓、边缘和表面质感区分。

## 参考入口

'''
    for r in data['references']:
        if int(r['id'][1:])>=178:text+=f"- [{r['title']}]({r['url']}) — {r['publisher']}。{r['summary']}\n"
    text+='\n## 配图图集\n\n';by_id={e['id']:e for e in data['entries']}
    for b in [b for b in data['boards'] if b.get('edition')==53]:
        ids={x['entry_id'] for x in b['items']};example=next(i for i,c in enumerate(data['combinations'],1) if c.get('added_in')=='53.0' and set(c['entry_ids'])==ids)
        text+=f"### {b['dimension']}\n\n[浏览这一组](../index.html?section={b['category']}&dimension={quote(b['dimension'])}) · [系统示例外观卡](../index.html?view=card&example={example}) · [原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
        for item in b['items']:
            e=by_id[item['entry_id']];text+=f"- **{e['id']} · {e['name']}**：{e['description']}\n"
        text+='\n'
    (root/'docs/scholar-environments-and-myth-v53.md').write_text(text,encoding='utf-8')
