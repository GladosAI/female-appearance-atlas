from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]/'image-jobs.json';jobs=json.loads(p.read_text(encoding='utf-8'))
marker='Edition 4 fashion clarification:'
for j in jobs:
    if j.get('edition')!=4 or marker in j['prompt']:continue
    if j['category']=='fashion_outfits':
        extra='All models are clearly adult women aged 25+ with mature faces and adult body proportions. Depict the specified wearable fashion coordinate, showing the fabrics, layered garments and accessories. Gothic fashion must retain specific contemporary/romantic/tailored differences, not become generic witches. British-inspired coordinates show the stated tweed, tailoring, country or adult-academic clothing. Lolita here means Japanese fashion: adults in coordinated full petticoat-supported knee-length or longer dresses, opaque blouses, lace trims and appropriate accessories, not school uniforms or lingerie. Punk coordinates use abstract original imagery without brand names, slogans or hateful symbols. Style is expressed by silhouette and construction, not solely changing color.'
    else:
        extra='Prioritize clearly observable shoulder construction. Off-the-shoulder/Bardot means BOTH shoulder caps are uncovered and a horizontal neckline lies BELOW them. Cold shoulder means intact neckline/straps PLUS cutout windows at the shoulder caps. One shoulder covers only one shoulder. Strapless has NO neck or shoulder straps; opaque structured garment covers the torso. Halter support wraps around the NECK while shoulders remain exposed. Ordinary sleeveless and dropped shoulder are NOT substitutes. Mature adult women, nonsexual neutral catalog poses.'
    j['prompt']+='\n'+marker+' '+extra
p.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Fashion-reference sheets:',sum(j.get('edition')==4 for j in jobs))
