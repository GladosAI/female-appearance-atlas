"""Persistent illustrated four-season everyday outfit reference."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path

def write_seasonal_docs(root,data):
    root=Path(root);entries=[e for e in data['entries'] if e.get('seasonal_reference')]
    ids={e['id'] for e in entries};boards=[b for b in data['boards'] if any(x['entry_id'] in ids for x in b['items'])]
    text=f"# 春夏秋冬日常穿搭图鉴\n\n共 {len(entries)} 套原创整套穿搭，{len(boards)} 张图页，每套有图。各季数量见下方索引。人物按成年女性日常衣着参考；校园场景为成年大学生与成人学院风。\n\n"
    text+='[四季日常总览](index.html?section=seasonal) · [春季](index.html?section=spring_outfits) · [夏季](index.html?section=summer_outfits) · [秋季](index.html?section=autumn_outfits) · [冬季](index.html?section=winter_outfits)\n\n'
    text+='## 季节与组合索引\n\n| 季节 | 数量 | 外层与材质观察 |\n| --- | ---: | --- |\n'
    notes={'spring':'薄风衣、轻夹克、棉衬衣、细针开衫与长短叠层。','summer':'短袖、棉麻、轻长裤、短裤、裙装与可脱薄罩衫。','autumn':'中厚针织、灯芯绒、轻羊毛、绗缝马甲与温差叠穿。','winter':'厚针织、羊毛呢、棉服、羽绒、厚袜裤及帽围巾手套。'}
    for season in data['meta']['seasons']:text+=f"| [{season['name']}](index.html?section={season['category']}) | {season['count']} | {notes[season['id']]} |\n"
    text+='\n季节是创作整理主题，可按地区与气候增减层次。室内套装、普通雨天外层与雪景造型分别标注；这里的运动出游造型用于角色绘画，未对商品或装备性能作评级。\n\n'
    text+='## 绘画与搭配记录\n\n先记录内搭、外层与下装，再比较腰线、外套长度、裙裤松量、袜与鞋的衔接和包带位置。换色时保留主要材质与轮廓；描绘叠层时让领口、袖口与下摆保持合理连接。各套可与现有发型、首饰、帽子、包袋和兽娘部件组合。\n\n'
    for season in data['meta']['seasons']:
        group=[e for e in entries if e['season']==season['id']]
        text+=f"## {season['name']} · {len(group)} 套\n\n{notes[season['id']]}\n\n"
        for dimension in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dimension];text+=f"### {dimension}\n\n"
            used={e['visual']['board'] for e in subset}
            for board in boards:
                if board['id'] in used:text+=f"![{board['title']}]({board['image']})\n\n"
            text+='| 编号 | 穿搭 | English | 衣物、鞋履与包袋 |\n| --- | --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
            text+='\n'
    text+='## 延伸参考\n\n'
    for r in data['references']:
        if r['id'] in ['R05','R06']:text+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    text+='\n整套方案独立编排，插图由内置 image_gen 制作，未复制教程或商品图片。\n\n[第17版配图提示词](image-prompts-v17.json) · [完整服装专辑](clothing-atlas.md) · [全部图鉴](atlas.md)\n'
    (root/'docs/seasonal-atlas.md').write_text(text,encoding='utf-8')
