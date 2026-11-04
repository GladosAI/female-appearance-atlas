// Check complete quadruped body plans without changing any prior meanings or IDs.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const partial=process.argv.includes('--partial'),d=read(partial?'.work/previews/catalog-v2-preview.json':'data/catalog.json');
const html=fs.readFileSync(path.join(root,partial?'.work/previews/index-v2-preview.html':'index.html'),'utf8');
const old=read('.work/verification/quadruped-v56/before/catalog.json');
for(const [k,v] of Object.entries({version:'56.0',entry_count:6781,category_count:172,board_count:578,new_count:4,quadruped_count:4,anthro_count:180,photo_pose_count:48,pose_count:300,missing_image_count:0}))assert.equal(d.meta[k],v,k);
const ns=d.entries.filter(e=>e.added_in==='56.0');
assert.deepEqual(ns.map(e=>e.id),['QF001','QF002','QF003','QF004']);
assert.equal(new Set(d.entries.map(e=>e.id)).size,d.entries.length);
for(const e of ns){assert.equal(e.category,'quadruped_forms');assert.equal(e.animal_body_plan,'complete_quadruped');assert.equal(e.stance,'four_feet_grounded');assert.equal(e.human_upper_body,false);assert.equal(e.human_hands,false);assert(e.anthro_reference&&e.quadruped_reference);assert(e.keywords.includes('四脚着地'));const v=e.visual,r=v.crop;assert(r&&r.width===768&&r.height===512);assert(r.x>=0&&r.y>=0&&r.x+r.width<=1536&&r.y+r.height<=1024)}
assert.equal(ns.filter(e=>e.species_reference==='pony').length,2);
for(const e of old.entries)assert.deepEqual(d.entries.find(n=>n.id===e.id),e,e.id+' changed');
for(const b of old.boards)assert.deepEqual(d.boards.find(n=>n.id===b.id),b,b.id+' changed');
for(const c of old.categories)assert.deepEqual(d.categories.find(n=>n.id===c.id),c,c.id+' changed');
assert.deepEqual(d.meta.anthro_levels,old.meta.anthro_levels);assert.deepEqual(d.combinations,old.combinations);assert.deepEqual(d.references,old.references);
const nav=JSON.parse(html.match(/<script id="atlas-navigation" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.equal(nav.groups.flatMap(g=>g.categories).filter(c=>c==='quadruped_forms').length,1);
assert(nav.groups.flatMap(g=>g.sections).find(s=>s.id==='anthro_shapes').categories.includes('quadruped_forms'));
const b=d.boards.find(b=>b.id==='quadruped-v56-complete-animal');assert.equal(b.qa_status,'visually_reviewed');assert.equal(b.items.length,4);
const png=fs.readFileSync(path.join(root,b.image));assert.equal(png.readUInt32BE(16),1536);assert.equal(png.readUInt32BE(20),1024);
assert(!/__[A-Z][A-Z_]+__/.test(html));for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g))if(!m[1].includes('application/json'))new vm.Script(m[2]);
if(!partial){assert.equal(read('prompts/image-prompts-v56.json').length,1);const doc=fs.readFileSync(path.join(root,'docs/quadruped-forms-v56.md'),'utf8');for(const e of ns)assert(doc.includes(e.id)&&doc.includes(e.name))}
const report={passed:true,partial,entries:d.entries.length,new_entries:4,new_boards:1,pony_references:2,explicit_crops:4,old_6777_entries_577_boards_171_categories_unchanged:true,old_bipedal_levels_unchanged:true};
fs.writeFileSync(path.join(root,'.work/verification/quadruped-v56/content-report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
