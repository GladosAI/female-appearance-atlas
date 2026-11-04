"""Publish composite-body silhouettes and connection notes."""
from urllib.parse import quote
def write_hybrid_v42_docs(root,data):
    es=[e for e in data['entries'] if e.get('hybrid_reference')]
    text='''# 半人形与复合躯体

[打开32项全身图](../index.html?section=hybrid_body_forms) · [兽娘、福瑞与幻想形态](../index.html?section=branch_anthro_shapes) · [提示词](../prompts/image-prompts-v42.json)

主目录：幻想形态与Cosplay → 兽娘、福瑞与幻想形态 → 半人形与复合躯体。

四组各8项：蛇尾；鱼尾与水生；四足兽体与鸟身；节肢、触腕与特殊基体。采用宽画格展示全身，保留尾尖、尾鳍、蹄爪和根枝。观察顺序为人形部分截止位置 → 腰部连接 → 下身体积 → 支撑点与运动方向 → 服装开口和附属结构。

图例为原创成年幻想身体方案，上身穿完整普通衣物，下身呈现幻想鳞片、被毛、甲壳等结构。与国风妖女组保留人类双腿、以衣物和局部异化表达身份的款式分开收录；可在设计时组合两者的衣饰。

这里的名字是创作检索标签，不是现实人类体型或残障分类，也不是对各文化神话、宗教形象及真实动物解剖的统一定义。蛇尾可参考拉弥亚、那伽等不同题材阅读，但不把不同传统的身份视为完全相同。节肢与触腕连接是架空推演，附肢数量和布局须随具体方案核对。

'''
    for dim in dict.fromkeys(e['dimension'] for e in es):
        group=[e for e in es if e['dimension']==dim];b=next(b for b in data['boards'] if b.get('edition')==42 and b['dimension']==dim)
        text+=f"## {dim}\n\n[只看本组](../index.html?section=hybrid_body_forms&dimension={quote(dim)})\n\n![{dim}](../{b['image']})\n\n| 编号 | 形态 | 连接 | 支撑与轮廓 |\n| --- | --- | --- | --- |\n"
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['hybrid_connection']} | {e['hybrid_support']} |\n"
        text+='\n'
    text+='## 阅读与图像记录\n\n四张图页通过内置 image_gen 生成，保存在 images/，逐格对应HY001—HY032；提示词保留每项连接和肢体要求。以下资料用于理解美人鱼、半人马和蛇人等艺术题材，未复制其图像，图中原创服装和扩展形态不代表文献中的全部版本。\n\n'
    used={r for e in es for r in e['related_reading']}
    for r in data['references']:
        if r['id'] in used:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/hybrid-body-forms.md').write_text(text,encoding='utf-8')
