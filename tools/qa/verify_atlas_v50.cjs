// Validate the twenty new adult-character studies and preserve saved-card IDs.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8')),partial=process.argv.includes('--partial');
const d=read(partial?'.work/previews/catalog-v2-preview.json':'data/catalog.json'),html=fs.readFileSync(path.join(root,partial?'.work/previews/index-v2-preview.html':'index.html'),'utf8'),old=read('.work/verification/persona-v50/before/data/catalog.json');
for(const [k,v] of Object.entries({version:'50.0',last_content_version:'50.0',entry_count:6533,category_count:156,clothing_count:3203,board_count:507,reference_count:177,new_count:20,persona_count:172,persona_v50_new_count:20,missing_image_count:0,study_count:80,controlled_comparison_count:24}))assert.equal(d.meta[k],v,k);
assert.equal(new Set(d.entries.map(e=>e.id)).size,6533);assert.equal(new Set(d.entries.map(e=>e.name)).size,6533);
const ns=d.entries.filter(e=>e.added_in==='50.0'),boards=d.boards.filter(b=>b.edition===50),nav=JSON.parse(html.match(/<script id="atlas-navigation" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.equal(ns.length,20);assert.equal(boards.length,5);assert.deepEqual(ns.map(e=>e.id),Array.from({length:20},(_,i)=>'QL'+(153+i)));
assert.equal(d.categories.find(c=>c.id==='persona_looks').count,172);assert.equal(d.meta.persona_labels.length,86);
for(const label of d.meta.persona_labels)assert.equal(d.entries.filter(e=>e.persona_tag===label).length,2,label);
assert.deepEqual([...new Set(ns.map(e=>e.persona_tag))],['软萌','卡哇伊','千金大小姐','精神异常','邋遢','拘谨','洁癖','病态','反差','占有欲']);
for(const [label,alias] of [['卡哇伊','kawaii'],['千金大小姐','大小姐'],['精神异常','失序表演'],['邋遢','不修边幅'],['拘谨','局促'],['病态','病感造型'],['反差','反差萌'],['占有欲','独占感']])assert(ns.filter(e=>e.persona_tag===label).every(e=>e.keywords.includes(alias)),alias);
assert.equal(nav.groups.flatMap(g=>g.categories).filter(c=>c==='persona_looks').length,1);
for(const e of ns){assert(e.category==='persona_looks'&&e.persona_reference&&e.adult_only&&e.age_min>=25&&!e.minor_reference&&e.illustration_recipe);const v=e.visual,r=v.crop,b=boards.find(b=>b.id===v.board);assert(r&&b,e.id);assert(r.x>=0&&r.y>=0&&r.width>0&&r.height>0&&r.x+r.width<=b.width&&r.y+r.height<=b.height);assert.equal(v.aspect,r.width/r.height);assert(fs.existsSync(path.join(root,v.image)));}
for(const b of boards){assert.equal(b.columns,2);assert.equal(b.rows,2);assert.equal(b.items.length,4);assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.column_boundaries.length,3);assert.equal(b.row_boundaries.length,3);const raw=fs.readFileSync(path.join(root,b.image));assert.equal(raw.subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.equal(raw.readUInt32BE(16),b.width);assert.equal(raw.readUInt32BE(20),b.height);for(const item of b.items)assert(ns.some(e=>e.id===item.entry_id&&e.name===item.name));}
for(const e of old.entries)assert.deepEqual(d.entries.find(n=>n.id===e.id),e,e.id+' unexpected change');
for(const b of old.boards)assert.deepEqual(d.boards.find(n=>n.id===b.id),b,b.id+' unexpected change');
for(const c of old.categories){const n=d.categories.find(n=>n.id===c.id);if(c.id==='persona_looks'){const a={...n},b={...c};for(const k of ['count','guide']){delete a[k];delete b[k]}assert.deepEqual(a,b)}else assert.deepEqual(n,c,c.id+' unexpected change')}
assert.deepEqual(d.combinations,old.combinations);assert.deepEqual(d.references,old.references);assert.deepEqual(d.style_families,old.style_families);
for(const e of d.entries)assert(e.related_reading.every(id=>d.references.some(r=>r.id===id)));
for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g))if(!m[1].includes('application/json'))new vm.Script(m[2]);assert(!/__[A-Z][A-Z_]+__/.test(html));
if(!partial){assert.equal(read('prompts/image-prompts-v50.json').length,5);const doc=fs.readFileSync(path.join(root,'docs/presence-acting-v50.md'),'utf8');for(const e of ns)assert(doc.includes(e.id)&&doc.includes(e.name));}
const report={passed:true,entries:6533,new_entries:20,new_persona_labels:10,persona_labels:86,persona_outfits:172,new_boards:5,explicit_crops:20,all_old_entries_boards_categories_references_combinations_and_styles_preserved:true};fs.writeFileSync(path.join(root,'.work/verification/persona-v50/content-report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
