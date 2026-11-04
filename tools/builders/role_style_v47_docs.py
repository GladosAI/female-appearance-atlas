"""Six outfit topics are placed in their existing primary branches."""
from urllib.parse import quote

def write_role_style_v47_docs(root,data):
    paths={
      'idol_outfits':'职业、主题与历史服装 → 舞台、竞技与秀场',
      'band_outfits':'职业、主题与历史服装 → 舞台、竞技与秀场',
      'assassin_outfits':'职业、主题与历史服装 → 主题装扮与人偶服',
      'japanese_retro_outfits':'职业、主题与历史服装 → 传统、国风与年代',
      'street_hiphop_outfits':'服装单件与日常穿搭 → 日常搭配与造型方向',
      'day_home_outfits':'服装单件与日常穿搭 → 贴身、居家与泳装'}
    text='''# 偶像、音乐人、杀手、年代、街头与居家穿搭

[分类总目录](../index.html?view=directory) · [图像提示词与原图路径](../prompts/image-prompts-v47.json)

新增6类、60套完整配图，均为25岁以上原创成年角色。偶像与乐队按演出身份归舞台；杀手与刺客按虚构角色归主题装扮；年代造型归历史文化；街头与嘻哈归整套穿搭；日间居家归居家分组。每个类别只有一个主要目录路径，可以与现有服饰部件和外观卡组合。

“邵和”按“昭和”整理，同时提供大正与平成初期相邻时期的灵感款。大正为1912—1926年，昭和为1926—1989年；图例逐项标明参考年代，西式款参考同期馆藏轮廓作原创转译，不把一个年代或馆藏当作全体日本女性的穿衣方式。[V&A 的二十世纪和服研究](https://www.vam.ac.uk/blog/projects/fashion-kimono)说明了大正与昭和的阶段、材质与纹样变化；[KCI 的1980年代馆藏](https://www.kci.or.jp/en/archives/digital_archives/1980s/)提供年代轮廓的对照入口。

街头与嘻哈包含宽廓形、牛仔、运动、工装及层搭方向。[FIT 的嘻哈服饰展](https://www.fitnyc.edu/museum/exhibitions/hip-hop-style.php)展示了嘻哈服饰的多样发展及女性造型变化；本轮服装是独立设计，不复制品牌图样。

| 类别 | 项数 | 目录位置 |
| --- | ---: | --- |
'''
    for cid,location in paths.items():
        c=next(c for c in data['categories'] if c['id']==cid)
        text+=f"| [{c['name']}](../index.html?section={cid}) | {c['count']} | {location} |\n"
    for cid,location in paths.items():
        c=next(c for c in data['categories'] if c['id']==cid)
        text+=f"\n## {c['name']}\n\n{c['guide']}\n\n[浏览本类](../index.html?section={cid})\n\n"
        for b in [b for b in data['boards'] if b.get('edition')==47 and b['category']==cid]:
            route=f"../index.html?section={cid}"+(f"&dimension={quote(b['dimension'])}" if cid!='japanese_retro_outfits' else '')
            text+=f"### {b['dimension']}\n\n[浏览词条]({route}) · [原图](../{b['image']})\n\n![{b['title']}](../{b['image']})\n\n"
            for item in b['items']:
                e=next(e for e in data['entries'] if e['id']==item['entry_id'])
                text+=f"- {e['id']} · **{e['name']}**：{e['description']}\n"
            text+='\n'
    (root/'docs/roles-retro-street-home.md').write_text(text,encoding='utf-8')
