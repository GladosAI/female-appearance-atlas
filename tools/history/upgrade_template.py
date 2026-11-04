"""Upgrade the atlas browser for the complete illustrated vocabulary."""
from pathlib import Path
p=Path(__file__).resolve().parent/'atlas_template.html'
s=p.read_text(encoding='utf-8')
if '__ENTRY_COUNT__' not in s:
    s=s.replace('582','__ENTRY_COUNT__').replace('88','__ILLUSTRATED_COUNT__')
    s=s.replace('示意总图 <span class="count">5</span>','分类图页 <span class="count">__BOARD_COUNT__</span>')
    s=s.replace('实物与来源 <span class="count">19</span>','实物与来源 <span class="count">__REFERENCE_COUNT__</span>')
    s=s.replace('组合示例 <span class="count">24</span>','组合示例 <span class="count">__COMBO_COUNT__</span>')
    s=s.replace('DESIGN REFERENCE COLLECTION / 01','DESIGN REFERENCE COLLECTION / 02')
    s=s.replace('<strong>__ILLUSTRATED_COUNT__</strong><span>动漫示意</span>','<strong>__CATEGORY_COUNT__</strong><span>细分类别</span>')
    s=s.replace('<strong>6</strong><span>实物图像</span>','<strong>__BOARD_COUNT__</strong><span>分类图页</span>')
    s=s.replace('<span>分类词条</span>','<span>配图词条</span>')
    s=s.replace('有示意图 <span>__ILLUSTRATED_COUNT__</span>','按图页排列')
    s=s.replace('全部词条 <span>__ENTRY_COUNT__</span>','按类别排列')
    s=s.replace('aria-label="词条范围"','aria-label="排列方式"')
    s=s.replace('<h2>五张分类总图</h2>','<h2>__BOARD_COUNT__ 张分类图页</h2>')
    s=s.replace('__ILLUSTRATED_COUNT__ 个典型示例为新增 AI 创作示意。','每个词条均对应一幅 AI 创作示意。')
    s=s.replace('13 个入口 · 核验','__READING_COUNT__ 个入口 · 核验')
    s=s.replace('<h2>24 套原创组合示例</h2>','<h2>__COMBO_COUNT__ 套原创组合示例</h2>')
    s=s.replace('每张图的中文标签与对应词条可以单独查看。','每个图例都对应词条编号，可以单独查看。')
    s=s.replace('典型外观示意','完整外观图鉴')
    s=s.replace('mode=\'illustrated\'','mode=\'all\'',1)
    s=s.replace("const key='female-appearance-atlas-v1';","const key='female-appearance-atlas-v1';\nlet currentEntryId=null,currentFilteredIds=D.entries.map(e=>e.id);const categoryOrder=new Map(D.categories.map((c,i)=>[c.id,i]));")
    s=s.replace("D.entries.filter(e=>(category==='all'||e.category===category)&&(mode==='all'||e.visual))","D.entries.filter(e=>(category==='all'||e.category===category)&&($('dimension-filter').value==='all'||e.dimension===$('dimension-filter').value))")
    old_sort="if(mode==='illustrated')arr.sort((a,b)=>D.boards.findIndex(x=>x.id===a.visual.board)-D.boards.findIndex(x=>x.id===b.visual.board)||(a.visual.row*a.visual.columns+a.visual.column)-(b.visual.row*b.visual.columns+b.visual.column));"
    new_sort="arr.sort((a,b)=>mode==='illustrated'?((a.visual?D.boards.findIndex(x=>x.id===a.visual.board):9999)-(b.visual?D.boards.findIndex(x=>x.id===b.visual.board):9999)||(a.visual?a.visual.row*a.visual.columns+a.visual.column:9999)-(b.visual?b.visual.row*b.visual.columns+b.visual.column:9999)):(categoryOrder.get(a.category)-categoryOrder.get(b.category)||a.id.localeCompare(b.id,undefined,{numeric:true})));currentFilteredIds=arr.map(e=>e.id);"
    assert old_sort in s;s=s.replace(old_sort,new_sort)
    s=s.replace('所有词条均附中英文名称、形态说明与检索词。未配独立插图的词条可从详情进入参考阅读。','所有词条均附对应图例、中英文名称、形态说明与检索词。可按类别细分或切换图页顺序。')
    s=s.replace("${mode==='illustrated'?'此分类可能尚无独立示意图；切换“全部词条”查看文字详表。':'试试较短的中文或英文关键词。'}","试试较短的中文或英文关键词，或取消细分筛选。")
    s=s.replace("function changeCategory(next){category=next;limit=72;mode='all';navigate('terms')}","function changeCategory(next){category=next;limit=72;mode='all';const dims=[...new Set(D.entries.filter(e=>category==='all'||e.category===category).map(e=>e.dimension))];$('dimension-filter').innerHTML='<option value=\"all\">全部细分</option>'+dims.map(x=>'<option value=\"'+esc(x)+'\">'+esc(x)+'</option>').join('');$('dimension-filter').value='all';navigate('terms')}")
    s=s.replace("function showDetail(id){const e=E.get(id);if(!e)return;","function showDetail(id){const e=E.get(id);if(!e)return;currentEntryId=id;")
    s=s.replace('<button class="close" id="close-dialog"','<button class="small-btn" id="prev-detail" aria-label="上一词条">← 上一项</button><button class="small-btn" id="next-detail" aria-label="下一词条">下一项 →</button><button class="close" id="close-dialog"')
    s=s.replace("function showBoard(id){const b=D.boards.find(x=>x.id===id);if(!b)return;","function showBoard(id){const b=D.boards.find(x=>x.id===id);if(!b)return;currentEntryId=null;")
    s=s.replace('原创幻想分类；请根据设定自行建立结构参考。','独立创作参考分类；可根据设定调整形态。')
    s=s.replace(' · <a href="image-prompts.json" target="_blank">示意图提示词</a>',' · <a href="image-prompts-v2.json" target="_blank">新增图页提示词</a>')
    s=s.replace('<select id="mobile-category"','<select id="dimension-filter" aria-label="细分维度" class="dimension-filter"><option value="all">全部细分</option></select><select id="mobile-category"')
    s=s.replace('<div class="board-list" id="board-list"></div>','<div class="tools"><select id="board-category" class="dimension-filter" aria-label="筛选图页分类"></select></div><div class="board-list" id="board-list"></div>')
    s=s.replace("$('board-list').innerHTML=D.boards.map(b=>", "function renderBoards(){const cat=$('board-category').value;const bs=D.boards.filter(b=>cat==='all'||b.items.some(x=>E.get(x.entry_id).category===cat));$('board-list').innerHTML=bs.map(b=>")
    needle="</div></article>`).join('');\n$('museum-grid')"
    assert needle in s;s=s.replace(needle,"</div></article>`).join('');}\n$('board-category').innerHTML='<option value=\"all\">全部图页 · __BOARD_COUNT__</option>'+D.categories.map(c=>'<option value=\"'+c.id+'\">'+esc(c.name)+'</option>').join('');$('board-category').addEventListener('change',renderBoards);renderBoards();\n$('museum-grid')",1)
    s=s.replace("updateCounts();renderTerms();", "$('dimension-filter').addEventListener('change',()=>{limit=72;renderTerms()});function stepDetail(direction){if(!currentEntryId)return;let ids=currentFilteredIds.includes(currentEntryId)?currentFilteredIds:D.entries.map(e=>e.id);const i=ids.indexOf(currentEntryId);showDetail(ids[(i+direction+ids.length)%ids.length])}$('prev-detail').addEventListener('click',()=>stepDetail(-1));$('next-detail').addEventListener('click',()=>stepDetail(1));$('detail-dialog').addEventListener('keydown',ev=>{if(ev.key==='ArrowLeft'){ev.preventDefault();stepDetail(-1)}if(ev.key==='ArrowRight'){ev.preventDefault();stepDetail(1)}});updateCounts();changeCategory('all');")
    s=s.replace('.tools{display:flex;','.dimension-filter{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:9px;padding:10px;font-size:12px;max-width:220px}.tools{display:flex;')
    p.write_text(s,encoding='utf-8')
    print('Template upgraded.')
else:print('Template already upgraded.')

wrapper=p.parent/'build_atlas.py'
wrapper.write_text('"""Build the complete expanded atlas; refuses missing illustrations."""\nfrom build_atlas_v2 import build\nimport sys\nif __name__ == "__main__":\n    build(partial="--partial" in sys.argv)\n',encoding='utf-8')
