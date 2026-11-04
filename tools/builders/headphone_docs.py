"""Build the headphones wearing reference topic."""
def write_headphone_docs(root,data):
    entries=[e for e in data['entries'] if e.get('headphone_reference')]
    text='# 耳机与耳麦佩戴图鉴\n\n32项原创成年角色佩戴参考，归于“帽包、发饰与首饰 → 耳机与耳麦佩戴”。比较接触位置、固定方式和外轮廓；小型耳机附同一侧耳部放大图。包耳、压耳、入耳、开放式与专业耳麦分别命名；科幻与猫耳装饰款不作为真实产品说明。\n\n[进入耳机佩戴类别](index.html?section=headphones) · [本版提示词](image-prompts-v31.json)\n\n'
    for dimension in dict.fromkeys(e['dimension'] for e in entries):
        group=[e for e in entries if e['dimension']==dimension]
        text+='## '+dimension+'\n\n'
        used={e['visual']['board'] for e in group}
        for b in data['boards']:
            if b['id'] in used:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 名称 | 视角与佩戴位置 | 可见结构 |\n| --- | --- | --- | --- |\n'
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['headphone_view']} · {e['headphone_anchor']} | {e['description']} |\n"
        text+='\n'
    text+='## 结构参考\n\n以下官方资料用于核对佩戴关系。图鉴配图由内置image_gen独立生成，未复制产品照片，不按外观标注声学性能。\n\n'
    for r in data['references']:
        if r['id'] in ['R102','R103','R104','R105']:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/headphone-atlas.md').write_text(text,encoding='utf-8')
