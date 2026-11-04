"""Persistent cosplay overview, parts index, and appearance-card combinations."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
COSPLAY_COMBINATIONS=[
 ('星盘巡游Cos方案','星盘巡游者Cos套装|星点颊面角色妆|短波波基础假发套|几何尖冠Cos头饰|立体星领Cos饰件|星窗短杖Cos道具|单手持短杖展示姿','蓝白与金；胸前星形、短发和短杖协调'),
 ('冰原骑士Cos方案','冰原披毛骑士Cos套装|露耳短层假发套|开面薄壳Cos头盔|对称腕甲Cos饰件|轻壳圆盾Cos道具|圆盾侧托展示姿','蓝灰与银；肩披与圆盾保持整体轮廓'),
 ('古堡人偶Cos方案','哥特人偶长裙Cos套装|哑光深唇舞台妆|卷发基础假发套|双弧小冠Cos头饰|长裙外叠腰饰Cos件|圆框手镜Cos道具|手镜抬至肩侧姿','黑紫与米白；卷发、冠饰和层裙分配视觉重点'),
 ('蒸汽修械Cos方案','蒸汽修械师Cos套装|露耳短层假发套|钟面小帽Cos头饰|齿轮胸盘Cos饰件|齿轮钥匙Cos道具|挂环道具携带座|正面角色识别站姿','铜棕与深蓝；帽、胸盘与手持物使用同一几何语言'),
 ('赛博夜巡Cos方案','赛博夜巡者Cos套装|科技半脸妆面分区|双色拼接假发套|双侧机械耳盘Cos饰|指背连片Cos手饰|空白数据板Cos道具|侧身肩饰展示姿','黑绿与银；妆面、假发分区和腕部外装呼应'),
 ('机械女仆Cos方案','机械维修女仆Cos套装|圆弧柔眉角色妆|短波波基础假发套|对称腕甲Cos饰件|齿轮钥匙Cos道具|夹口胸饰固定座|单手致意展示姿','黑白与铜金；围裙工具、短发与齿轮道具协调'),
 ('纸扇云游Cos方案','纸扇云游者Cos套装|圆弧柔眉角色妆|盘髻包罩假发件|双弧小冠Cos头饰|肩腰连接飘带Cos件|折扇画面Cos道具|折扇半开呈现姿','蓝白与淡金；冠髻、衣襟与扇面可按同一主题调整'),
 ('朋克鼓手Cos方案','朋克乐队鼓手Cos套装|宽尾刀形眉角色妆|扇状尖束造型假发|双侧机械耳盘Cos饰|齿轮胸盘Cos饰件|空白麦克风Cos道具|单手致意展示姿','黑红与金属色；格纹、尖束假发和舞台道具协调')
]

def write_cosplay_docs(root,data):
    es=[e for e in data['entries'] if e.get('cosplay_reference')]
    new=[e for e in es if e.get('added_in')=='11.0']
    refs={r['id']:r for r in data['references']}
    text=f"# Cosplay角色扮演图鉴\n\n共 {len(es)} 项：本版新增 {len(new)} 项，另接入特殊装扮96项与面具16项。新增内容包括整套服装64套、角色妆面与外观件32项、假发32款、头饰16件、身体装饰32件、手持道具32件、固定与拆分32项，以及展示动作16项。所有条目都有编号图例。\n\n"
    text+='打开 [Cosplay总览](index.html?section=cosplay)。参考按原创角色原型和可组合部件组织；新人物均为成年角色。先确定整套轮廓，再匹配妆面、假发和头饰；选装饰与道具后，核对连接底托和完整展示视角。\n\n'
    text+='## 分类入口\n\n| 分类 | 数量 | 观察重点 |\n| --- | ---: | --- |\n'
    for c in data['categories']:
        group=[e for e in es if e['category']==c['id']]
        if group:text+=f"| [{c['name']}](index.html?section={c['id']}) | {len(group)} | {c['guide']} |\n"
    text+='\n## 组合方案\n\n首页的“组合示例”提供以下8套外观卡组合，可一键加入部件并调整配色。组合使用独立词条；可按角色设计替换或减少装饰。\n\n| 方案 | 配色与重点 | 部件编号 |\n| --- | --- | --- |\n'
    for c in data['combinations']:
        if c.get('cosplay_combo'):text+=f"| {c['name']} | {c['palette']} | {'、'.join(c['entry_ids'])} |\n"
    text+='\n## 图页与词条\n\n配图为内置image_gen生成的原创外观示意。大型外装观察完整轮廓、根部与带具；妆面观察位置与形状；假发观察帽底、发帘、连接根和发尾。固定图展示完成件及装配关系。\n\n'
    for c in data['categories']:
        group=[e for e in es if e['category']==c['id']]
        if not group:continue
        text+=f"### {c['name']}\n\n{c['guide']}\n\n"
        for dimension in dict.fromkeys(e['dimension'] for e in group):
            subset=[e for e in group if e['dimension']==dimension]
            text+=f"#### {dimension}\n\n"
            used={e['visual']['board'] for e in subset}
            for b in data['boards']:
                if b['id'] in used:text+=f"![{b['title']}]({b['image']})\n\n"
            text+='| 编号 | 中文 | English | 可见结构 |\n| --- | --- | --- | --- |\n'
            for e in subset:text+=f"| {e['id']} | {e['name']} | {e['en']} | {e['description']} |\n"
            text+='\n'
    text+='## 延伸资料\n\n'
    for ident in ['R61','R62','R63']:
        r=refs[ident];text+=f"- [{r['title']}]({r['url']})：{r['summary']}\n"
    text+='\n[第11版图页提示词](image-prompts-v11.json) · [全部外观图鉴](atlas.md) · [服装专辑](clothing-atlas.md) · [来源说明](sources.md)\n'
    (root/'docs/cosplay-atlas.md').write_text(text,encoding='utf-8')
