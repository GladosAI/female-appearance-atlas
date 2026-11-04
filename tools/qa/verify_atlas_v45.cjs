// New illustrated character-presence studies, crop geometry and existing-card compatibility.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8')),partial=process.argv.includes('--partial');
const d=read(partial?'.work/previews/catalog-v2-preview.json':'data/catalog.json'),html=fs.readFileSync(path.join(root,partial?'.work/previews/index-v2-preview.html':'index.html'),'utf8'),old=read('.work/verification/persona-v45/before/data/catalog.json');
for(const [key,value] of Object.entries({version:'45.0',last_content_version:'45.0',entry_count:6325,category_count:150,clothing_count:3011,board_count:455,reference_count:173,new_count:56,persona_count:48,coverage_look_count:8,missing_image_count:0,study_count:80,controlled_comparison_count:24}))assert.equal(d.meta[key],value,key);
assert.equal(new Set(d.entries.map(e=>e.id)).size,6325);assert.equal(new Set(d.entries.map(e=>e.name)).size,6325);
const ns=d.entries.filter(e=>e.added_in==='45.0'),boards=d.boards.filter(b=>b.edition===45),nav=JSON.parse(html.match(/<script id="atlas-navigation" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.equal(ns.length,56);assert.equal(boards.length,14);
assert.deepEqual(ns.map(e=>e.id),[['QL',48],['LC',8]].flatMap(([p,n])=>Array.from({length:n},(_,i)=>p+String(i+1).padStart(3,'0'))));
for(const [cid,n] of Object.entries({persona_looks:48,coverage_looks:8})){assert.equal(d.categories.find(c=>c.id===cid).count,n);assert.equal(nav.groups.flatMap(g=>g.categories).filter(c=>c===cid).length,1);assert.equal(nav.category_paths[cid].section,'branch_character_presence')}
assert.equal(d.meta.persona_labels.length,24);for(const label of d.meta.persona_labels)assert.equal(ns.filter(e=>e.persona_tag===label).length,2,label);
for(const label of ['萌','性感','典雅','呆','成熟','幼稚','活泼','冷酷','傲娇','外向','内向','谨慎','高冷'])assert(d.meta.persona_labels.includes(label));
assert(ns.some(e=>e.coverage_kind==='暴露／高露肤'));
for(const e of ns){assert(e.adult_only&&e.age_min>=25&&!e.minor_reference&&e.illustration_recipe);const v=e.visual,r=v.crop,b=boards.find(b=>b.id===v.board);assert(r&&b,e.id);assert(r.x>=0&&r.y>=0&&r.width>0&&r.height>0&&r.x+r.width<=b.width&&r.y+r.height<=b.height);assert.equal(v.aspect,r.width/r.height);assert(fs.existsSync(path.join(root,v.image)));}
for(const b of boards){assert.equal(b.columns,2);assert.equal(b.rows,2);assert.equal(b.items.length,4);assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.column_boundaries.length,3);assert.equal(b.row_boundaries.length,3);const raw=fs.readFileSync(path.join(root,b.image));assert.equal(raw.subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.equal(raw.readUInt32BE(16),b.width);assert.equal(raw.readUInt32BE(20),b.height);for(const item of b.items)assert(ns.some(e=>e.id===item.entry_id&&e.name===item.name));}
for(const e of old.entries)assert.deepEqual(d.entries.find(n=>n.id===e.id),e,e.id+' unexpected change');
for(const b of old.boards)assert.deepEqual(d.boards.find(n=>n.id===b.id),b,b.id+' unexpected change');
for(const c of old.categories)assert.deepEqual(d.categories.find(n=>n.id===c.id),c,c.id+' unexpected change');
assert.deepEqual(d.combinations,old.combinations);assert.deepEqual(d.references,old.references);
for(const e of d.entries)assert(e.related_reading.every(id=>d.references.some(r=>r.id===id)));
for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g))if(!m[1].includes('application/json'))new vm.Script(m[2]);assert(!/__[A-Z][A-Z_]+__/.test(html));
if(!partial){assert.equal(read('prompts/image-prompts-v45.json').length,14);const doc=fs.readFileSync(path.join(root,'docs/character-presence.md'),'utf8');for(const e of ns)assert(doc.includes(e.id)&&doc.includes(e.name));}
const report={passed:true,entries:6325,new_entries:56,personas:24,persona_outfits:48,coverage_outfits:8,new_boards:14,explicit_crops:56,all_existing_entries_boards_categories_references_and_combinations_preserved:true};fs.writeFileSync(path.join(root,'.work/verification/persona-v45/content-report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
