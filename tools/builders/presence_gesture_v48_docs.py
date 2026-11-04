"""A paired index of new full-body presence and hand/face interactions."""
from urllib.parse import quote
def write_presence_gesture_v48_docs(root,data):
    text='''# 气质造型与许愿、祈祷、乞求、行礼

[分类总目录](../index.html?view=directory) · [气质全部](../index.html?section=persona_looks) · [手部与面部互动](../index.html?section=face_hands) · [提示词与原图路径](../prompts/image-prompts-v48.json)

新增16种气质、32套全身造型；许愿、祈祷、乞求、行礼各4幅，共16幅手势表演。全部采用25岁以上成年角色，使用内置 image_gen 生成12张四格图页。第48版完成时，气质类共64种、128套；手部与面部互动共64项。

新增气质：清新、素朴、禁欲、野性、妩媚、端丽、热血、好胜、机敏、专注、好奇、乖巧、笨拙、冒失、戏谑、毒舌。每种两套，可对比衣物、发型、表情与姿态；这些是创作标签，不根据外貌推断真实人格。禁欲以封闭剪裁和克制姿态表示，野性以粗纹材质、松散发束与站姿表示。

手势页把愿望、祈愿、请求与致礼分别组织。许愿侧重期待感，祈祷侧重静心与俯首，乞求强调眉眼恳切与身体轻前倾，行礼比较颔首、交手俯首、扶帽檐和提裙欠身。它们是通用角色表演，具体礼仪因场合而异。

许愿、祈祷和乞求采用腰上近景，完整保留手掌、手腕与脸部；行礼页保留头部至膝下，让躯干前倾和屈膝能被读懂。比较手掌朝向、拇指与四指的遮挡、手与下颏的间隙，再观察眉峰、眼睑、唇线与头部方向。全身体态类别原有的“礼貌鞠躬致意”继续保留。

'''
    for cid in ['persona_looks','face_hands']:
        cat=next(c for c in data['categories'] if c['id']==cid)
        text+=f"## {cat['name']}\n\n"
        for b in [b for b in data['boards'] if b.get('edition')==48 and b['category']==cid]:
            text+=f"### {b['dimension']}\n\n[原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
            for item in b['items']:
                e=next(e for e in data['entries'] if e['id']==item['entry_id'])
                text+=f"- [{e['id']} · **{e['name']}**](../index.html?section={cid}&dimension={quote(e['dimension'])})：{e['description']}\n"
            text+='\n'
    (root/'docs/presence-gestures-v48.md').write_text(text,encoding='utf-8')
