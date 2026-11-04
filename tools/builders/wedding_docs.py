"""Edition 19 wedding clothing topic, variants and references."""

def write_wedding_docs(root,data):
    text='''# 婚纱与婚服图鉴

第19版新增80项完整婚礼造型：[婚纱32款](../index.html?section=bridal_gowns)、[婚服48套](../index.html?section=wedding_attire)。打开 [婚礼服装总览](../index.html?section=wedding)，也可在“职业、舞台与特殊装扮”中按类别、细分浏览。

| 类别 | 细分 | 数量 |
| --- | --- | ---: |
| 婚纱 | 廓形与裙摆 | 16 |
| 婚纱 | 领袖与头纱搭配 | 16 |
| 婚服 | 中式古风嫁衣灵感 | 16 |
| 婚服 | 现代中式婚服与敬酒礼装 | 16 |
| 婚服 | 其他文化婚服与现代礼装 | 16 |

婚纱重点比较A字、蓬裙、鱼尾、直筒、高腰、茶长、拖尾、领袖与头纱。婚服包含古风创作嫁衣、裙褂、现代秀禾风格、旗袍及裤装，并列出日式、韩式、印度婚礼灵感与现代婚礼礼装。每套标明完整衣物与配饰关系，文化或古风条目注明创作改编语境。

'''
    for cid in data['meta']['wedding_categories']:
        cat=next(c for c in data['categories'] if c['id']==cid)
        text+=f"## {cat['name']}\n\n{cat['guide']}\n\n"
        for b in data['boards']:
            if b.get('category')!=cid:continue
            text+=(f"### {b['dimension']}\n\n![{b['title']}](../{b['image']})\n\n"
                   "| 编号 | 造型 | 衣物与配饰 |\n| --- | --- | --- |\n")
            for e in data['entries']:
                if e['category']==cid and e['dimension']==b['dimension']:
                    text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
            text+='\n'
    text+='''## 参考与创作说明

- [V&A Wedding dress](https://www.vam.ac.uk/collections/wedding-dress)：婚纱、不同文化婚礼服装、头纱与鞋履研究入口。
- [中国丝绸博物馆嫁衣展览研究范围](https://www.chinasilkmuseum.com/xwdtIR/info_9.aspx?itemid=31402&parent=)：近现代婚嫁服装的多种类型。
- [Asian Art Museum hwarot婚礼袍](https://searchcollection.asianart.org/objects/14965/bridal-robe-hwarot)：韩式婚礼袍的袖口、绣纹与轮廓参考。
- [The Met日式婚礼服装研究](https://www.metmuseum.org/ja/essays/japanese-weddings-in-the-edo-period-1615-1868)：小袖、外打挂与头部覆盖的观察语境。
- [本版5张图页提示词](../prompts/image-prompts-v19.json)：内置 imagegen 制作的原创动漫示意，按编号裁切展示。

古风、地域与文化灵感服装是原创角色设计改编。具体历史形制、礼仪与穿着方式可沿参考资料继续研究；本图鉴按可见服装与装饰结构组织。
'''
    (root/'docs/wedding-atlas.md').write_text(text,encoding='utf-8')
