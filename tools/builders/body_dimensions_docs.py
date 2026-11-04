"""Document the adult dimension comparison and exact fictional values."""
def write_body_dimensions_docs(root,data):
    es=[e for e in data['entries'] if e.get('body_dimension_reference') and e['dimension_view']=='front']
    text='# 成年女性尺寸与罩杯对照\n\n第26版：16组虚构成年角色尺寸，各有正面、侧身，共32幅。打开 [体型与比例](index.html?section=body)，默认显示尺寸并排对照；切换罩杯、身高、肩宽、腰围与臀围，选择2至4列，每列可更换案例。原有轮廓与姿态在“全部参考词条”中。\n\n'
    text+='所有尺寸单位为厘米。正面、侧身按相同示意身高标尺与脚底基线排列，数值由页面文字和表格准确显示。图像为生成的近似衣着轮廓，不是从图上反推的真人测量；胸腰臀为周长，标线仅定位测量层位，肩宽为直线宽度。所有新增尺寸与罩杯图仅采用25岁以上成年角色。\n\n'
    text+='## 罩杯标法\n\n使用 [华歌尔官方日系表](https://store.wacoal.jp/size/chart/size5131.html)：完整尺码为罩杯字母＋底围，例如 C75。A至H名义上下胸围差约为10、12.5、15、17.5、20、22.5、25、27.5 cm；本组底围固定75，便于比较同一条件下的近似轮廓。不同底围的同字母不能直接视为相同容量，也不在本页进行跨国家或品牌换算。\n\n'
    text+='## 尺寸设定一览\n\n| 案例 | 身高 | 肩宽 | 胸围 | 下胸围 | 腰围 | 臀围 | 日系参考尺码 | 差值 | 正面／侧面编号 |\n| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |\n'
    for e in es:
        side=next(s for s in data['entries'] if s.get('dimension_case')==e['dimension_case'] and s.get('dimension_view')=='side')
        text+=f"| {e['dimension_label']} | {e['height_cm']} | {e['shoulder_width_cm']} | {e['bust_cm']:g} | {e['underbust_cm']} | {e['waist_cm']} | {e['hip_cm']} | {e['bra_size']} | {e['cup_difference_cm']:g} | {e['id']}／{side['id']} |\n"
    text+='\n## 完整图页\n\n'
    for b in data['boards']:
        if any(x['entry_id'] in {e['id'] for e in data['entries'] if e.get('body_dimension_reference')} for x in b['items']):text+=f"![{b['title']}]({b['image']})\n\n"
    text+='图片由内置 imagegen 生成，完整原图保存于 images 目录，提示词见 [第26版提示词](image-prompts-v26.json)。\n'
    (root/'docs/body-dimensions-atlas.md').write_text(text,encoding='utf-8')
