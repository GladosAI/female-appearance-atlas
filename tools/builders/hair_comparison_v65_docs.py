"""Audit text-based hairstyle selection without copying reference images."""
from pathlib import Path

# Representative source ID -> comparable existing/new elements; not a claim of identical artwork.
COVERED={
 'f31fd3f3647':'HC004、HS067','f092482c5fb':'HN002、HS014','f13732eb704':'HC006、HS074',
 'f17b470cc0c':'HC005、HC016','f595f590337':'HC007、HS013','f2199e525ae':'HZ035',
 'f0a31815789':'HB001、HC009、HS001','f02920397d9':'HC009、HS067',
 'f2584d75c0e':'HC006、HC017、HS067','f0937d9bc47':'HC008、HC017、HS076',
 'f000a1c4200':'HC008、HC016、HS012','f128f44ea0b':'HC026、HS015',
 'f02c3400e4b':'HC008、HS052','f00caf968d5':'HC010、HC017、HS071',
 'f2ae7b5cb88':'HC017、HS074','f0bab310679':'HS004、HC011','f0457e14faa':'HC019、HS070',
 'f0f60d4ec73':'HC011、HB001、HS001','f042429bfb7':'HC011、HS002',
 'f09ab713d45':'HC017、HB012、HS067','f134ec4bbeb':'HC017、HS052、HS013',
 'f069bb87789':'HC017、HS028','f0b815b84f1':'HN079、HS019',
 'f13d55ef133':'HN080、HS076、HB002','f029a34a679':'HC035、HC019',
 'f1f629b1bc9':'HB005、HS002',
}

def write_hair_comparison_v65_docs(root,data):
    root=Path(root);entries=[e for e in data['entries'] if e.get('hair_comparison_v65')]
    text='''# 人像发型词条对照与原创补充

对照参考项目的 1,499 条人像记录，仅使用发长、发型名称等文字；其中 755 条为标准基础款且没有更明确的发型名称，无法只凭词条判断具体发型。其余 744 条按发长和名称合并为 50 类：本次挑选 24 种剪裁、卷度、刘海或染色的完整组合，另外 26 类主要为颜色变体或可用已有及本次新增元素表达的相近造型。

这些判断是文字层面的覆盖判断，不代表原图视觉相同，也不代表现有示意图已涵盖所有可能造型。本次没有查看参考项目的图片；新增示意图由内置 imagegen 独立生成。每类只列一个代表参考编号，重复记录与原始图片均未导入。

[完整发型与造型组合](../index.html?section=hair_combinations) · [全部头发](../index.html?section=hair) · [生成提示词](../prompts/image-prompts-v65.json)

## 原创补充 · 24 项

| 编号 | 发型 | 参考词条编号 |
| --- | --- | --- |
'''
    for e in entries:text+=f"| {e['id']} | {e['name']} | {e['inspiration_reference']} |\n"
    text+='\n## 相近造型或组成元素 · 26 类\n\n下方编号指向可组合或相近的图鉴元素；并非声明有完全一致的成品图。\n\n| 参考词条代表编号 | 可参考的图鉴编号 |\n| --- | --- |\n'
    for ref,ids in COVERED.items():text+=f'| {ref} | {ids} |\n'
    (root/'docs/hair-comparison-v65.md').write_text(text,encoding='utf-8')
