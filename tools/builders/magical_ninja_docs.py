"""V25 costume family entry points and complete illustrated index."""
def write_magical_ninja_docs(root,data):
    entries=[e for e in data['entries'] if e.get('magical_ninja_reference')]
    text='# 魔法少女与忍者装扮图鉴\n\n第25版新增64套：魔法少女32套、忍者32套，共4张图页，全部采用明确成年原创角色。\n\n'
    text+='打开 [魔法少女装扮](index.html?section=magical_girl_outfits)、[忍者装扮](index.html?section=ninja_outfits) 或 [职业、舞台与特殊装扮总目录](index.html?section=topic_role_costumes)。两个类别各有两组16套细分，图例均可查看详情并加入外观卡。\n\n'
    text+='魔法少女是服装题材名称，图例采用成年角色。基础组比较领口、袖型、裙裤、手套、袜靴、胸饰和法具；主题与进阶组比较花瓣、星轨、元素、机械、偶像、文化改编和冬季层次。忍者按布装、束袖束腿、头巾面罩、护具和软包组织，另有环境与幻想改编；不把全部原创套装宣称为史实。\n\n'
    for cid in ['magical_girl_outfits','ninja_outfits']:
        cat=next(c for c in data['categories'] if c['id']==cid);text+=f"## {cat['name']} · 32套\n\n{cat['guide']}\n\n"
        group=[e for e in entries if e['category']==cid]
        for dim in dict.fromkeys(e['dimension'] for e in group):
            es=[e for e in group if e['dimension']==dim];ids={e['visual']['board'] for e in es};text+=f'### {dim}\n\n'
            for board in data['boards']:
                if board['id'] in ids:text+=f"![{board['title']}]({board['image']})\n\n"
            text+='| 编号 | 名称 | 服装与配饰结构 |\n| --- | --- | --- |\n'
            for e in es:text+=f"| {e['id']} | {e['name']} | {e['description']} |\n"
            text+='\n'
    text+='配图由内置 imagegen 生成，完整原图保存于 images 目录。参见 [第25版提示词](image-prompts-v25.json)、[特殊装扮总览](special-costumes-atlas.md)、[伊贺流忍者博物馆：装束与伪装语境](https://www.iganinja.jp/en/about/igaryu.html) 和 [来源说明](sources.md)。\n'
    (root/'docs/magical-ninja-atlas.md').write_text(text,encoding='utf-8')
