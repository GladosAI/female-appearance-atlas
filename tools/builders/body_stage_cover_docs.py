"""V24 adult body, stage-costume and worn face-cover references."""
def write_body_stage_cover_docs(root,data):
    entries=[e for e in data['entries'] if e.get('added_in')=='24.0']
    text='# 成年体型、舞台装扮与面部覆盖物\n\n第24版新增144项，9张图页：成年体型与体态32项，四类舞台与特殊装扮64项，面部覆盖物48项。全部为25岁以上成年角色参考。\n\n'
    text+='[体型与比例](index.html?section=body) · [体操](index.html?section=gymnastics_outfits) · [啦啦队](index.html?section=cheer_outfits) · [死神](index.html?section=reaper_costumes) · [维密风格秀场](index.html?section=runway_lingerie) · [面部覆盖物](index.html?section=face_overlays)\n\n'
    text+='## 正面与侧身成对索引\n\n卡片和详情中的“正面＋侧身对照”可同时查看同一标签的两种视角。健身型、梨形等是整体轮廓，贫胸／丰胸、翘臀／平臀是局部体积，肩部与脊背标签是绘画姿态；这些轴可以在自己的角色中组合。\n\n| 标签 | 正面 | 侧身 |\n| --- | --- | --- |\n'
    bodies=[e for e in entries if e.get('body_shape_reference')]
    for e in bodies:
        if e['body_shape_view']!='front':continue
        side=next(x for x in bodies if x['body_shape_key']==e['body_shape_key'] and x['body_shape_view']=='side')
        text+=f"| {e['paired_shape_label']} | {e['id']} | {side['id']} |\n"
    text+='\n体型与体态采用不透明长袖运动上衣和完整长裤，图片不作健康或美丑判断。维密风格是原创成年内衣秀场灵感：不透明有衬里胸衣、普通包覆三角裤／短裤／连体衣和舞台背饰，不复制真人、品牌标志或具体成套造型。体操和啦啦队图例只说明衣物结构，不声明赛事合规。\n\n'
    text+='口罩、半面／整面呼吸器与装饰面具按用途语境和结构分组。此处是佩戴外观参考；防护效果、适用环境和认证不能由图例推定。原有 [面具与面部装扮](index.html?section=masks) 继续作为部件与主题入口，本次增加的是清楚呈现遮挡和固定方式的佩戴图。\n\n'
    for dim in dict.fromkeys(e['dimension'] for e in entries):
        group=[e for e in entries if e['dimension']==dim];used={e['visual']['board'] for e in group}
        text+=f'## {dim}\n\n'
        for b in data['boards']:
            if b['id'] in used:text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 名称 | 可见结构 |\n| --- | --- | --- |\n'
        for e in group:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='配图由内置 imagegen 生成，原图保存于 images 目录。参见 [第24版提示词](image-prompts-v24.json)、[本版新增索引](fashion-guide.md)、[面部图鉴](facial-atlas.md) 和 [来源说明](sources.md)。\n'
    (root/'docs/body-stage-cover-atlas.md').write_text(text,encoding='utf-8')
