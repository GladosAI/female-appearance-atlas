"""Document the V35 lip close-ups and the stable-ID expression relocation."""
def write_lips_v35_docs(root,data):
    es=[e for e in data['entries'] if e.get('lip_reference')]
    text='''# 嘴唇形态、唇妆与唇色

第35版新增48项原创成年角色唇部近景，分为3张16格图页。自然唇形观察结构，唇妆观察颜色、边缘与反光；口部动作和完整面妆另有目录。

- [嘴唇形态与轮廓](../index.html?section=lips)：脸部与表情 → 脸型、五官与视角 → 嘴唇形态与轮廓，16项。
- [唇妆与唇色](../index.html?section=lip_makeup)：脸部与表情 → 眼妆与唇妆 → 唇妆与唇色，32项。
- [凝视与憋笑](../index.html?section=face_emotions)：已移至“情绪与眉眼联动”，保留EX029—EX044原编号与原图，已有外观卡中的这些词条继续可用。
- [唇齿动作](../index.html?section=mouth_actions) · [完整面妆](../index.html?section=expression) · [生成提示词](../prompts/image-prompts-v35.json)

'''
    for dim in dict.fromkeys(e['dimension'] for e in es):
        group=[e for e in es if e['dimension']==dim]
        board=next(b for b in data['boards'] if group[0]['id'] in {item['entry_id'] for item in b['items']})
        text+=f"## {dim}\n\n![{board['title']}](../{board['image']})\n\n| 编号 | 名称 | 可见特征 |\n| --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='## 图像与参考\n\n通过内置 image_gen 生成3张原创图页，保存在 images/，每格按编号与词条对应。自然唇形主要使用同一中性闭口视角；最后3项为侧面。唇妆以固定近景比较，质感组尽量保持同色，以减少颜色与反光之间的干扰。图像为绘画示意，实际唇形、肤色和光照会形成连续差异。\n\n'
    for r in data['references']:
        if r['id'] in ['R108','R109']:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/lips-and-lip-makeup.md').write_text(text,encoding='utf-8')
