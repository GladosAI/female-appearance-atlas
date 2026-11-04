"""Persistent adult face/acting index and user-requested term coverage."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
REQUESTED_FACE_TERMS='困倦、生病、重感冒、轻感冒、流鼻涕、流鼻血、黑眼圈、脸红、苍白、眼妆哭花、呆滞、痛苦、挣扎、捂脸、抿嘴唇、咬嘴唇、咬牙切齿、张大嘴、吐舌头、流口水、闭眼亲吻、撒娇、眼罩、单眼罩、含着棒棒糖、抽烟、气鼓鼓、绷带、脸上有脏东西、在吃东西、打哈欠、半人半机器、电子义眼、吹泡泡糖、两眼放光、惊吓、捂嘴、惊讶捂嘴、捂嘴笑、两手压着脸蛋、俏皮、渴求、狡猾、焦虑、剪刀手遮眼、咬手指、挠头、喊叫、炎热、冷冻、大汗、流汗、期待、着急、迫不及待、唱歌、撅嘴、哼、挑逗、吓唬、憋气、异瞳、扶镜框、崩溃、阴沉着脸、板着脸、困惑、眩晕、潮红、魅惑、勾引'.split('、')+['睡眠','昏迷','长眠','口罩','防毒面具','一般面具']

REQUESTED_FACE_TERMS+=['许愿','祈祷','乞求','行礼']

def write_facial_docs(root,data):
    es=[e for e in data['entries'] if e.get('facial_reference')]
    new=[e for e in es if e['category'] in data['meta']['facial_new_categories']]
    refs={r['id']:r for r in data['references']}
    counts={key:sum(e['category']==key for e in new) for key in data['meta']['facial_new_categories']}
    text=f"# 面部表情、状态与互动图鉴\n\n共 {len(es)} 项，包含面部六类专题 {len(new)} 项及兽脸与其他脸型、五官、表情、眼部、局部标记和妆面参考。面部六类专题包含状态{counts['face_states']}项、情绪{counts['face_emotions']}项、口部{counts['mouth_actions']}项、手部互动{counts['face_hands']}项、妆痕覆盖{counts['face_overlays']}项及眼部改造{counts['face_augments']}项。每个词条均有图例。\n\n"
    text+='打开 [面部总览](index.html?section=facial)，使用细分筛选或搜索潮红、挑逗、魅惑、勾引、困惑、眩晕、困倦、睡眠、昏迷、长眠、感冒、捂嘴、吃东西、假眼、口罩、防毒面具、一般面具等关键词。人物按成年绘画参考；先保留角色的固定脸型与五官位置，再改变眼睑、眉线、嘴角、口型和手势。病中词条是剧情表演与画面强度标签；眩晕是剧情外观表演；旋纹、星点和旋环是动画提示符。冷冻、发光和机械脸是幻想造型。睡眠、昏迷与长眠图例为非血腥剧情标签，不能只凭面容作真实状态判断。\n\n'
    text+='## 面部专题分类\n\n| 类别 | 数量 | 观察要点 |\n| --- | ---: | --- |\n'
    for c in data['categories']:
        group=[e for e in new if e['category']==c['id']]
        if group:text+=f"| [{c['name']}](index.html?section={c['id']}) | {len(group)} | {c['guide']} |\n"
    text+='\n## 按动作组合\n\n一帧可以组合一个情绪、一个口部动作和一个手势，再加汗泪、污痕或覆盖物。捂嘴笑与惊讶捂嘴共用遮挡动作，但眉眼不同；气鼓鼓与憋气都可鼓腮，但眉、眼和嘴角不同。异瞳比较虹膜颜色；眼睛放光比较反光与目光；电子义眼比较镜面、外壳和接缝。\n\n'
    text+='## 图页与词条\n\n图例由内置image_gen制作。人物头像按成年人表现；口部动作保留脸部上下文，手势图展示手腕和正常指位。保持自身角色脸型后，可沿说明调整表演幅度。\n\n'
    shown=set()
    order=sorted(data['categories'],key=lambda c:(c['id'] not in data['meta']['facial_new_categories'],[x['id'] for x in data['categories']].index(c['id'])))
    for c in order:
        group=[e for e in es if e['category']==c['id']]
        if not group:continue
        text+=f"### {c['name']} · {len(group)} 项\n\n"
        for dimension in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dimension];text+=f"#### {dimension}\n\n"
            used={e['visual']['board'] for e in subset}
            for b in data['boards']:
                if b['id'] in used and b['id'] not in shown:
                    shown.add(b['id']);text+=f"![{b['title']}]({b['image']})\n\n"
            text+='| 编号 | 中文 | English | 可见特征 |\n| --- | --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
            text+='\n'
    text+='## 延伸资料\n\n'
    for ident in ['R03','R64','R65','R69','R70','R72']:
        r=refs[ident];text+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    text+='\n[第12版面部图页](image-prompts-v12.json) · [第13版困惑眩晕图页](image-prompts-v13.json) · [第15版潮红与含蓄表演图页](image-prompts-v15.json) · [第16版兽脸及兽型图页](image-prompts-v16.json) · [Cosplay专题](cosplay-atlas.md) · [全部外观图鉴](atlas.md) · [来源说明](sources.md)\n'
    (root/'docs/facial-atlas.md').write_text(text,encoding='utf-8')
