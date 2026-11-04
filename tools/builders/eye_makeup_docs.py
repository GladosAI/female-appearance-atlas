"""Eye makeup illustrated topic using the same canonical entry and crop mapping."""
def write_eye_makeup_docs(root,data):
    es=[e for e in data['entries'] if e.get('eye_makeup_reference')]
    text='# 眼影、眼线与完整眼妆\n\n48项原创成年角色彩妆参考：眼影16项、眼线16项、完整眼妆16项。目录路径为“脸部与表情 → 眼妆与唇妆”。眼影和眼线采用单眼近景，组合妆采用双眼近景；自然棕色虹膜减少妆色比较中的干扰。\n\n[打开眼部分类](index.html?section=branch_makeup_detail) · [眼影](index.html?section=eyeshadow) · [眼线](index.html?section=eyeliner) · [完整眼妆](index.html?section=eye_makeup) · [生成提示词](image-prompts-v33.json)\n\n'
    for c in data['categories']:
        group=[e for e in es if e['category']==c['id']]
        if not group:continue
        text+=f"## {c['name']}\n\n{c['guide']}\n\n"
        for b in data['boards']:
            if b.get('category')==c['id']:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 名称 | 位置与质感 | 可见特征 |\n| --- | --- | --- | --- |\n'
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['makeup_placement']} · {e['makeup_finish']} | {e['description']} |\n"
        text+='\n'
    text+='## 参考与图像说明\n\n使用内置image_gen生成原创示意，图页与编号逐格对应。官方资料用于术语和结构核对，未复制品牌图片。眼部形态与肤色会影响实际视觉效果。\n\n'
    for r in data['references']:
        if r['id'] in ['R106','R107']:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/eye-makeup-atlas.md').write_text(text,encoding='utf-8')
