"""Prepare original character-in-scene prompts; register only visually reviewed image grids."""
import argparse
import hashlib
import json
from pathlib import Path
import struct

ROOT=Path(__file__).resolve().parents[1]
def read(relative):return json.loads((ROOT/relative).read_text(encoding='utf-8'))
def write(relative,value):
    path=ROOT/relative;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def prepare():
    plan=read('source/scene-plan-v71.json');entries=[];jobs=[]
    for category in plan['categories']:
        assert len(category['entries'])%4==0
        for index,row in enumerate(category['entries']):
            name,en,description,note,direction=row
            entries.append({'stable_id':category['prefix']+str(index+1).zfill(3),'category':category['id'],
                'dimension':category['groups'][index//4],'name':name,'en':en,'description':description,
                'note':note,'aliases':['人物场景','场景参考','环境与人物','character in environment',name.removesuffix('场景')],
                'reference_ids':[],'origin':'editorial','added_in':'71.0','scene_reference':True})
        for offset in range(0,len(category['entries']),4):
            codes=[category['prefix']+str(i+1).zfill(3) for i in range(offset,offset+4)]
            prompt='''Use case: illustration-story. Asset type: original character-in-environment scene atlas for female game, animation and film character design.
Canvas: LANDSCAPE 3:2 contact sheet. EXACTLY TWO columns and TWO rows of rectangular landscape panels, read top-left, top-right, bottom-left, bottom-right. Four independent scenes. Thin continuous dark dividers at the canvas midpoint, no broad gutters. Each panel stays entirely inside its own rectangle.
Art direction: detailed polished anime and semi-realistic cinematic environment concept illustration, expressive original adult characters, coherent perspective, carefully drawn natural hands, restrained clean outlines, attractive readable colors and lighting. This is a setting-and-activity atlas: the environment must be identifiable AND at least one prominent adult woman must actively belong in it. Main woman roughly 45-75 percent of panel height, shown full-body or medium-wide as appropriate, never a tiny distant silhouette. Vary women across panels in face, hairstyle, skin tone and everyday body shape. All human figures are adults.
Composition: foreground, middle ground and background establish a useful place. Hands actually touch the relevant objects; feet and seats have plausible support. Clothing matches the location and activity. Do not replace a scene with a detached fashion cutout, portrait crop, empty room, generic gradient or white studio backdrop. Do not add inset diagrams. Preserve the complete intended action and environmental landmarks within each panel.
No known characters, franchises, company logos, celebrity likenesses or readable private information. Only each panel's exact ID in small legible type at its own top-left; no other captions or text.
Specific panels:
'''
            for slot,(code,row) in enumerate(zip(codes,category['entries'][offset:offset+4]),1):
                prompt+=f'Panel {slot}, exact label "{code}": {row[4]}\n'
            jobs.append({'id':'scene-v71-'+category['prefix'].lower()+'-'+str(offset//4+1),
                'category':category['id'],'dimension':category['groups'][offset//4],
                'title':category['name']+' · '+category['groups'][offset//4],
                'image':'images/sheet-scenes-'+category['prefix'].lower()+'-'+str(offset//4+1)+'-v71.png',
                'columns':2,'rows':2,'edition':71,'entries':[{'id':code,'name':row[0],'en':row[1]} for code,row in zip(codes,category['entries'][offset:offset+4])],
                'prompt':prompt,'declared_inputs':[]})
    write('source/scene-prompts-v71.json',{'schema':'female-appearance-scene-prompts/v1','tool':'built-in image_gen','model':None,'jobs':jobs})
    write('prompts/image-prompts-v71.json',jobs)
    return plan,entries,jobs


def register():
    plan,entries,jobs=prepare()
    review=read('source/scene-review-v71.json');approved={item['board_id']:item for item in review['boards']}
    boards=[]
    for job in jobs:
        item=approved[job['id']]
        assert item['environment_and_people_checked'] and item['labels_and_bounds_checked'],job['id']
        raw=(ROOT/job['image']).read_bytes();assert raw[:8]==b'\x89PNG\r\n\x1a\n'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],job['id']+' changed after review'
        width,height=struct.unpack('>II',raw[16:24])
        for field,size,count in [('column_boundaries',width,2),('row_boundaries',height,2)]:
            bounds=item[field];assert len(bounds)==count+1 and bounds[0]==0 and bounds[-1]==size and all(a<b for a,b in zip(bounds,bounds[1:]))
            job[field]=bounds
        boards.append({**{k:job[k] for k in ['id','category','dimension','title','image','columns','rows','edition','column_boundaries','row_boundaries','prompt']},
            'width':width,'height':height,'origin':'Original AI-generated character-in-scene illustration; built-in image_gen',
            'generation_tool':'built-in image_gen','generated_on':item['recorded_on'],'qa_status':'image_cells_checked',
            'items':[{'entry_id':e['id'],'label':e['id'],'name':e['name']} for e in job['entries']]})
    extensions=read('source/category-extensions.json')
    for category in plan['categories']:
        definition={'id':category['id'],'prefix':category['prefix'],'name':category['name'],'source_ids':[],
          'guide':'原创人物场景参考。观察环境用途、前中后景、人物活动与道具接触，以及透视、尺度和光照关系。人物与着装是案例，可按角色设定替换；历史与幻想场景为创作灵感。'}
        old=next((c for c in extensions if c['id']==category['id']),None)
        if old:assert old==definition
        else:
            assert not any(c['prefix']==definition['prefix'] for c in extensions)
            extensions.append(definition)
    write('source/category-extensions.json',extensions)
    navigation=read('source/navigation.json');group=next(g for g in navigation['groups'] if g['id']=='art_styles')
    cats=[c['id'] for c in plan['categories']]
    section={'id':'scene_character_design','name':'场景与人物活动','categories':cats}
    old=next((s for s in group['sections'] if s['id']==section['id']),None)
    if old:assert old==section
    else:group['sections'].insert(2,section)
    group['categories']=[category for section in group['sections'] for category in section['categories']]
    group['note']='按画风、媒介与视觉语言浏览；包括场景与人物活动、游戏角色原稿、漫画单格、影视分镜与关键帧，以及视角和镜头语言。'
    navigation['search_aliases']['场景']=['环境','人物场景','场景图例','背景','地点','environment','scene']
    document={'name':'场景与人物活动','path':'docs/scenes-with-characters.md'}
    if not any(d.get('path')==document['path'] for d in navigation['documents']):navigation['documents'].append(document)
    write('source/navigation.json',navigation)
    write('source/contributions/scenes-v71.json',{'schema':'female-appearance-contribution/v1','entries':entries,'boards':boards,'references':[]})
    old_jobs=read('source/image-jobs.json');own={j['id'] for j in jobs}
    write('source/image-jobs.json',[j for j in old_jobs if j['id'] not in own]+jobs)
    write('source/scene-prompts-v71.json',{'schema':'female-appearance-scene-prompts/v1','tool':'built-in image_gen','model':None,'jobs':jobs})
    write('prompts/image-prompts-v71.json',jobs)
    print(json.dumps({'entries':len(entries),'boards':len(boards),'categories':len(cats)}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('action',choices=['prompts','register']);args=parser.parse_args()
    if args.action=='register':register()
    else:
        _,entries,jobs=prepare();print(json.dumps({'entries':len(entries),'boards':len(jobs)}))
