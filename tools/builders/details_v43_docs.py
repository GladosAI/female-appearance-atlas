"""Publish local-form studies and controlled face-light/garment-motion sheets."""
from urllib.parse import quote
def write_details_v43_docs(root,data):
    es=[e for e in data['entries'] if e.get('study_reference')]
    paths={'hands':'身体与动作 → 手足、甲面与皮肤细节','nose_ear_teeth':'脸部与表情 → 脸型、五官与视角','skin_details':'身体与动作 → 手足、甲面与皮肤细节','portrait_lighting':'脸部与表情 → 光照与明暗','garment_dynamics':'服装单件与日常穿搭 → 领袖、结构与衣物动态'}
    text='''# 基础局部、脸部光照与衣物动态

[打开本轮80项](../index.html?section=clothing_new) · [生成提示词](../prompts/image-prompts-v43.json)

手部16项，鼻耳牙齿24项，皮肤局部16项，脸部光照8项，衣物动态16项；共五个类别、十组大画格图页。每项可加入外观卡，分类图页可同时观察整组。

局部形态描述自然差异，不作美丑或医学分类。皮肤近景适当放大纹理，实际可见程度受距离与光线影响，图例不用于皮肤诊断。手部和口鼻耳是原创绘画示意，需继续结合实际观察核对。

光照组固定同一原创成年面孔、正面机位、发型、表情和服装，只改变光源。两组衣物分别固定人物和款式，以站姿作基准，比较动作、接触、风和转身；是绘画观察示意，不是光学或布料物理仿真，也不保证所有体积关系完全一致。

'''
    for cid in paths:
        c=next(c for c in data['categories'] if c['id']==cid);group=[e for e in es if e['category']==cid]
        text+=f"## {c['name']} · {len(group)}项\n\n目录：{paths[cid]} → {c['name']}。 [词条](../index.html?section={cid}) · [整组图页](../index.html?section={cid}&view=boards)\n\n"
        for dim in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dim];b=next(b for b in data['boards'] if b.get('edition')==43 and b['dimension']==dim)
            text+=f"### {dim}\n\n[只看本组](../index.html?section={cid}&dimension={quote(dim)})\n\n"
            if subset[0].get('fixed_conditions'):text+=f"固定条件：{subset[0]['fixed_conditions']}。基准：{subset[0]['comparison_baseline']}。\n\n"
            text+=f"图页文件：[查看原图](../{b['image']})。\n\n![{dim}](../{b['image']})\n\n| 编号 | 名称 | 观察点 | 视角与条件 |\n| --- | --- | --- | --- |\n"
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['study_focus']} | {e['study_view']} |\n"
            text+='\n'
    text+='## 资料与图像记录\n\n十张图页通过内置 image_gen 生成并保存在 images/。来源用于手部结构、五官绘画、投影与布料褶皱的延伸阅读，未复制教程图像；皮肤局部为原创纹理示意。\n\n'
    used={r for e in es for r in e['related_reading']}
    for r in data['references']:
        if r['id'] in used:text+=f"- [{r['publisher']} · {r['title']}]({r['url']})：{r['summary']}\n"
    (root/'docs/details-lighting-and-drapery.md').write_text(text,encoding='utf-8')
