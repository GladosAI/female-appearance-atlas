"""Document original V34 beauty references and retain the exact prompt provenance."""
def write_beauty_v34_docs(root,data):
    entries=[e for e in data['entries'] if e.get('beauty_expansion_reference')]
    text='# 第34版 · 发质发色、表情与妆容\n\n2026-10-17 新增96项原创成年角色参考，分为6张16格图页：发质16项、发色16项、凝视与憋笑16项、日常微表情16项、日常完整妆16项、风格与创意妆16项。\n\n[发质与发色](../index.html?section=hair_surface) · [凝视与憋笑](../index.html?section=face_emotions) · [表情与妆容](../index.html?section=expression) · [生成提示词](../prompts/image-prompts-v34.json)\n\n'
    for kind in dict.fromkeys(e['beauty_kind'] for e in entries):
        group=[e for e in entries if e['beauty_kind']==kind]
        board=next(b for b in data['boards'] if group[0]['id'] in {item['entry_id'] for item in b['items']})
        text+='## '+board['title']+'\n\n!['+board['title']+'](../'+board['image']+')\n\n| 编号 | 名称 | 可见特征 |\n| --- | --- | --- |\n'
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='## 图像与提示记录\n\n使用内置 image_gen 生成，未使用 CLI/API 回退。每个图例为原创成年角色示意，不对应固定人物或唯一标准。提示词、格子编号与图像路径记录在第34版提示词文件，原图保存于 images/。\n'
    (root/'docs/beauty-expansion-v34.md').write_text(text,encoding='utf-8')
