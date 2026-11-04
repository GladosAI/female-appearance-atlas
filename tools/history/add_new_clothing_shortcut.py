from pathlib import Path
p=Path(__file__).resolve().parent/'atlas_template.html'
s=p.read_text(encoding='utf-8')
if 'data-category="clothing_new"' not in s:
    s=s.replace('<div class="jump"><button data-category="clothing">','<div class="jump"><button data-category="clothing_new">本次新增服装 · 464 条</button><button data-category="clothing">')
    s=s.replace("cat==='clothing'?clothingCategories.has(e.category):e.category===cat","cat==='clothing'?clothingCategories.has(e.category):cat==='clothing_new'?e.added_in==='3.0':e.category===cat")
    s=s.replace("category==='clothing'?'服装专辑 · __CLOTHING_COUNT__ 条':C.get(category).name","category==='clothing'?'服装专辑 · __CLOTHING_COUNT__ 条':category==='clothing_new'?'本次新增服装 · 464 条':C.get(category).name")
    s=s.replace("category==='clothing'?'按版型","(category==='clothing'||category==='clothing_new')?'按版型")
    s=s.replace('<option value="clothing">服装专辑 · __CLOTHING_COUNT__</option>','<option value="clothing">服装专辑 · __CLOTHING_COUNT__</option><option value="clothing_new">本次新增服装 · 464</option>')
    p.write_text(s,encoding='utf-8')
print('New-clothing shortcut added.')
