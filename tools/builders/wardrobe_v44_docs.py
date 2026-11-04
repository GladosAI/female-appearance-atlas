"""Readable index and saved image/prompt paths for the shoe/sock/glove expansion."""
from urllib.parse import quote
def write_wardrobe_v44_docs(root,data):
    text='''# 鞋履、袜类与手套扩充与裁切修正

[进入本分组](../index.html?section=branch_shoes_hosiery) · [本轮96项](../index.html?section=clothing_new) · [图像提示词与原图路径](../prompts/image-prompts-v44.json)

新增鞋履48项、袜类24项、手套24项，使用内置 image_gen 生成12张八格图页。每格保留完整鞋尖、鞋跟、靴筒、袜口、袖口和指尖。原有图页依据实际分隔线校正裁切，不再假设所有画格等高。

原FW021–FW027移至袜类，FW028–FW032移至手套；原编号、名称和外观卡引用保留。鞋履、袜类、手套现在各有独立入口。图片是原创成年尺码服饰示意，运动、工具与幻想款描述造型结构；D数不单独决定透感。

'''
    for cid in ['footwear','hosiery','gloves']:
        cat=next(c for c in data['categories'] if c['id']==cid)
        text+=f"## {cat['name']} · {cat['count']}项\n\n[浏览全部](../index.html?section={cid})\n\n"
        for b in [b for b in data['boards'] if b.get('edition')==44 and b['category']==cid]:
            text+=f"### {b['dimension']}\n\n[本组词条](../index.html?section={cid}&dimension={quote(b['dimension'])}) · [原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
            for item in b['items']:
                e=next(e for e in data['entries'] if e['id']==item['entry_id'])
                text+=f"- {e['id']} · **{e['name']}**：{e['description']}\n"
            text+='\n'
    text+='## 延伸阅读\n\n'
    for r in data['references']:
        if r['id'] in ['R172','R173','R56','R68']:
            text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/shoes-hosiery-gloves.md').write_text(text,encoding='utf-8')
