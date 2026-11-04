"""Publish chronological routes and clearly separated regional selections."""
from urllib.parse import quote

def write_history_v38_docs(root,data):
    es=[e for e in data['entries'] if e.get('fashion_history_reference')]
    tracks=data['meta']['fashion_history_tracks']
    text='''# 女装历史与演变

[打开配图词条](../index.html?section=fashion_history) · [传统、国风与年代](../index.html?section=branch_history_culture) · [第38版提示词](../prompts/image-prompts-v38.json) · [第39版提示词](../prompts/image-prompts-v39.json)

第39版继续增加48项，本专题现有96项、六个分组，各16项。保留原有中国、欧洲与近现代三组，新增中国时段补充、日本与朝鲜半岛及其他地域选编。卡片标明参考年代、地域与结构观察点。

中国和欧美组按各自时间线观察。日韩组包含两条并行路线，详情中的相邻参照只显示日本或朝鲜半岛各自的服装。地域选编按区域提供并列参照，年代用于定位，不表示国家、族群或文化之间存在先后替代关系。搜索和名称排序会改变展示顺序。

这些是以史料与服装研究为基础的原创轮廓示意，人物、配色及部分细节为创作推演，不是某件文物的精确复原。部分内层为保持完整覆盖而作调整。年代为参考区间，不一定是起源年代；地域、族群、阶层、礼服与日装存在差异，服装会并行、延续和复兴。这里只选取部分样式，不代表全球女装全史。

观察顺序建议：先看整套衣物的体积与腰线，再看衣领、袖型、开合和裙裤；比较宽度时区分裙撑方向、布料垂坠与姿态差异。

'''
    for t in tracks:
        group=[e for e in es if e['history_track']==t['id']]
        b=next(b for b in data['boards'] if group[0]['id'] in {x['entry_id'] for x in b['items']})
        text+=f"## {t['name']}\n\n{t['scope']}。 [只看这条时间线](../index.html?section=fashion_history&dimension={quote(t['name'])})\n\n![{b['title']}](../{b['image']})\n\n| 编号 | 年代与地域 | 名称 | 形制与演变观察 |\n| --- | --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['history_period']} · {e['history_region']} | {e['name']} | {e['history_silhouette']}；{e['history_change']}。{'参照范围：'+e['history_line_name']+'。' if e.get('history_line_name') else ''} |\n"
        text+='\n'
    text+=f"## 资料与图像来源\n\n{len(tracks)}张图页通过内置 image_gen 生成，保存在 images/，按FH001—FH{len(es):03}逐格对应。每项的相关阅读可进一步核对形制；下列来源作为研究入口与术语依据，部分细节和配色是结合材料所作的示意推演。\n\n"
    used={r for e in es for r in e['related_reading']}
    for r in data['references']:
        if r['id'] in used:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/womens-fashion-history.md').write_text(text,encoding='utf-8')
