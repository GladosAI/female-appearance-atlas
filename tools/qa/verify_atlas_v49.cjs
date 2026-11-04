// Validate new costumes, navigation, crops and published-data compatibility.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8')),partial=process.argv.includes('--partial');
const d=read(partial?'.work/previews/catalog-v2-preview.json':'data/catalog.json'),html=fs.readFileSync(path.join(root,partial?'.work/previews/index-v2-preview.html':'index.html'),'utf8'),old=read('.work/verification/persona-v49/before/data/catalog.json');
for(const [k,v] of Object.entries({version:'49.0',last_content_version:'49.0',entry_count:6513,category_count:156,clothing_count:3183,board_count:502,reference_count:177,new_count:32,persona_count:152,presence_v49_new_count:32,coverage_look_count:8,missing_image_count:0,special_new_count:0,study_count:80,controlled_comparison_count:24}))assert.equal(d.meta[k],v,k);
assert.equal(new Set(d.entries.map(e=>e.id)).size,6513);assert.equal(new Set(d.entries.map(e=>e.name)).size,6513);
const ns=d.entries.filter(e=>e.added_in==='49.0'),boards=d.boards.filter(b=>b.edition===49),nav=JSON.parse(html.match(/<script id="atlas-navigation" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.equal(ns.length,32);assert.equal(boards.length,8);assert.deepEqual(ns.map(e=>e.id),[['QL',129,152],['FS',265,268],['TR',65,68]].flatMap(([p,a,b])=>Array.from({length:b-a+1},(_,i)=>p+String(a+i).padStart(3,'0'))));
for(const [cid,n] of Object.entries({persona_looks:152,traditional:68,fashion_outfits:268,face_hands:64}))assert.equal(d.categories.find(c=>c.id===cid).count,n,cid);
assert.equal(d.meta.persona_labels.length,76);for(const label of d.meta.persona_labels)assert.equal(d.entries.filter(e=>e.persona_tag===label).length,2,label);
assert.deepEqual([...new Set(ns.filter(e=>e.persona_reference).map(e=>e.persona_tag))],['圣洁','妖艳','清冷','病娇','厌世','疏离','天真','保持距离','空灵','肃穆','颓靡','倦怠']);
assert(ns.filter(e=>e.persona_tag==='保持距离').every(e=>e.keywords.includes('保持隔离')));assert.equal(ns.filter(e=>e.styles.includes('jirai')).length,4);
assert.equal(d.style_families.find(s=>s.id==='jirai').count,old.style_families.find(s=>s.id==='jirai').count+4);
assert(ns.filter(e=>e.category==='traditional').every(e=>e.related_reading.includes('R177')));
for(const cid of ['persona_looks','traditional','fashion_outfits'])assert.equal(nav.groups.flatMap(g=>g.categories).filter(c=>c===cid).length,1);
for(const e of ns){assert(e.adult_only&&e.age_min>=25&&!e.minor_reference&&e.illustration_recipe);const v=e.visual,r=v.crop,b=boards.find(b=>b.id===v.board);assert(r&&b,e.id);assert(r.x>=0&&r.y>=0&&r.width>0&&r.height>0&&r.x+r.width<=b.width&&r.y+r.height<=b.height);assert.equal(v.aspect,r.width/r.height);assert(fs.existsSync(path.join(root,v.image)));}
for(const b of boards){assert.equal(b.columns,2);assert.equal(b.rows,2);assert.equal(b.items.length,4);assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.column_boundaries.length,3);assert.equal(b.row_boundaries.length,3);const raw=fs.readFileSync(path.join(root,b.image));assert.equal(raw.subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.equal(raw.readUInt32BE(16),b.width);assert.equal(raw.readUInt32BE(20),b.height);for(const item of b.items)assert(ns.some(e=>e.id===item.entry_id&&e.name===item.name));}
for(const e of old.entries)assert.deepEqual(d.entries.find(n=>n.id===e.id),e,e.id+' unexpected change');
for(const b of old.boards)assert.deepEqual(d.boards.find(n=>n.id===b.id),b,b.id+' unexpected change');
for(const c of old.categories){const n=d.categories.find(n=>n.id===c.id);if(['persona_looks','traditional','fashion_outfits'].includes(c.id)){const a={...n},b={...c};delete a.count;delete b.count;if(c.id==='persona_looks'){delete a.guide;delete b.guide}assert.deepEqual(a,b)}else assert.deepEqual(n,c,c.id+' unexpected change')}
assert.deepEqual(d.combinations,old.combinations);for(const r of old.references)assert.deepEqual(d.references.find(n=>n.id===r.id),r);
for(const e of d.entries)assert(e.related_reading.every(id=>d.references.some(r=>r.id===id)));
for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g))if(!m[1].includes('application/json'))new vm.Script(m[2]);assert(!/__[A-Z][A-Z_]+__/.test(html));
if(!partial){assert.equal(read('prompts/image-prompts-v49.json').length,8);const doc=fs.readFileSync(path.join(root,'docs/presence-styles-v49.md'),'utf8');for(const e of ns)assert(doc.includes(e.id)&&doc.includes(e.name));}
const report={passed:true,entries:6513,new_entries:32,new_persona_outfits:24,persona_labels:76,persona_outfits:152,new_jirai_outfits:4,new_geiko_outfits:4,new_boards:8,explicit_crops:32,all_old_entries_boards_references_and_combinations_preserved:true};fs.writeFileSync(path.join(root,'.work/verification/persona-v49/content-report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
