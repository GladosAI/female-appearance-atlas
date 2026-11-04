"""Compact role taxonomy: two outfit references per identity."""
from urllib.parse import quote
def write_diverse_roles_docs(root,data):
    es=[e for e in data['entries'] if e.get('diverse_role_reference')]
    text='# 更多职业、舞台与奇幻身份装扮\n\n第27版新增 **32种身份，每种2套，共64套配图**。按4个类别组织，每类8种，选择“细分”即可只看某一种的两套结构。打开 [职业、舞台与特殊装扮总目录](index.html?section=topic_role_costumes)。\n\n'
    text+='全部采用25岁以上成年原创角色。服装主体、头饰、手套、鞋靴与携行道具均在词条中拆分；同种两套比较实际衣物结构与层次，不只更换颜色。专业和文化题材均为角色设计灵感，具体情境另行标明。\n\n'
    for cid in dict.fromkeys(e['category'] for e in es):
        cat=next(c for c in data['categories'] if c['id']==cid);entries=[e for e in es if e['category']==cid]
        text+=f"## [{cat['name']}](index.html?section={cid}) · 8种／16套\n\n{cat['guide']}\n\n| 类型 | 两套图例 | 查看 |\n| --- | --- | --- |\n"
        for kind in dict.fromkeys(e['dimension'] for e in entries):
            pair=[e for e in entries if e['dimension']==kind]
            text+=f"| {kind} | {'；'.join(e['id']+' '+e['name'] for e in pair)} | [2套对照](index.html?section={cid}&dimension={quote(kind)}) |\n"
        text+='\n'
        for b in data['boards']:
            if any(i['entry_id'] in {e['id'] for e in entries} for i in b['items']):text+=f"![{b['title']}]({b['image']})\n\n"
        text+='| 编号 | 名称 | 衣物与配饰 |\n| --- | --- | --- |\n'
        for e in entries:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
        text+='\n'
    text+='配图由内置 imagegen 生成，完整原图保存于 images 目录；提示词见 [第27版提示词](image-prompts-v27.json)。延伸阅读：[V&A 戏剧与表演收藏](https://www.vam.ac.uk/collections/theatre-performance)。\n'
    (root/'docs/diverse-roles-atlas.md').write_text(text,encoding='utf-8')
