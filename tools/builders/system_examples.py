"""Coherent character examples, separate from the historical URL archive."""
import copy
import json


def prepare_system_examples(root, entries, legacy):
    source=json.loads((root/'source/system-examples.json').read_text(encoding='utf-8'))
    if source.get('schema')!='female-appearance-system-examples/v1':
        raise ValueError('Unsupported system example source')
    by_id={entry['id']:entry for entry in entries}
    chapters={chapter['id']:chapter for chapter in source['chapters']}
    seen=set()
    cards=copy.deepcopy(source['cards'])
    for card in cards:
        if not card.get('id') or card['id'] in seen:
            raise ValueError('Duplicate/missing system example id')
        seen.add(card['id'])
        if card.get('chapter') not in chapters:
            raise ValueError('Unknown example chapter: '+card['id'])
        ids=card['entry_ids']
        if not 4<=len(ids)<=8 or len(ids)!=len(set(ids)) or any(eid not in by_id for eid in ids):
            raise ValueError('Invalid small reference set: '+card['id'])
        if not all(isinstance(card.get(field),str) and card[field].strip()
                   for field in ['name','description','palette']):
            raise ValueError('Missing character description: '+card['id'])
        card.update(character_example=True,chapter_name=chapters[card['chapter']]['name'])
    archive=[{**card,'archived':True} for card in legacy+source.get('archived_cards',[])]
    archived_ids={card['id'] for card in archive if card.get('id')}
    if archived_ids&seen:raise ValueError('Character example reuses an archived identifier')
    return archive+cards,source


def example_coverage(data,navigation):
    active=[card for card in data['combinations'] if not card.get('archived')]
    entries={entry['id']:entry for entry in data['entries']}
    category_cards={category['id']:[] for category in data['categories']}
    for card in active:
        for cid in {entries[eid]['category'] for eid in card['entry_ids']}:
            category_cards[cid].append(card['id'])
    domains=[]
    for domain in navigation['groups']:
        sections=[{'id':section['id'],'name':section['name'],
                   'covered':any(category_cards[cid] for cid in section['categories'])}
                  for section in domain['sections']]
        domains.append({'id':domain['id'],'name':domain['name'],
                        'category_count':len(domain['categories']),
                        'covered_categories':sum(bool(category_cards[cid]) for cid in domain['categories']),
                        'sections':sections})
    return {'schema':'female-appearance-example-coverage/v1',
            'example_count':len(active),'unique_entries':len({eid for c in active for eid in c['entry_ids']}),
            'min_entries':min(len(c['entry_ids']) for c in active),
            'max_entries':max(len(c['entry_ids']) for c in active),
            'category_count':len(category_cards),'covered_categories':sum(bool(ids) for ids in category_cards.values()),
            'section_count':sum(len(d['sections']) for d in domains),
            'covered_sections':sum(s['covered'] for d in domains for s in d['sections']),
            'domain_count':len(domains),
            'covered_domains':sum(bool(d['covered_categories']) for d in domains),
            'domains':domains,'category_examples':category_cards,
            'uncovered_categories':[cid for cid,ids in category_cards.items() if not ids]}


def write_example_docs(root,data,navigation):
    coverage=example_coverage(data,navigation)
    (root/'data/example-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    entries={entry['id']:entry for entry in data['entries']}
    cards=[card for card in data['combinations'] if not card.get('archived')]
    text=f'''# 系统角色卡

[打开系统示例](../index.html?view=card&card_tab=examples)

{len(cards)} 张具体人物的外观卡，每张 {coverage['min_entries']}—{coverage['max_entries']} 项参考。每张卡围绕一个人物与一个场景选择外貌、服装、表情、姿态、饰物和表现方式；整组通过不同年龄、身份、时代、气质与形态展现多样性。

可按人物题材或关键词查找，打开即查看该角色的图鉴集合。保存为个人外观卡后可以自由修改。角色简介与配色留在备注中，AI提示词仍只导出已勾选词条的中英文名称。

'''
    for chapter in data['example_chapters']:
        text+=f"\n## {chapter['name']}\n\n"
        for card in cards:
            if card['chapter']!=chapter['id']:continue
            text+=f"### [{card['name']}](../index.html?view=card&example={card['id']})\n\n{card['description']}\n\n配色：{card['palette']}\n\n"
            text+='、'.join(f"[{entries[eid]['name']}（{eid}）](../index.html?section={entries[eid]['category']}&entry={eid})" for eid in card['entry_ids'])+'。\n\n'
    text+='## 维护与兼容\n\n维护源为 `source/system-examples.json`。先确定人物身份与当前场景，再选择能共同描述这个人物的参考。多样性通过整组角色体现，统计清单 [example-coverage.json](../data/example-coverage.json) 供维护时观察选材范围；角色设计优先于类别覆盖率。\n\n旧版数字地址与已使用的字符串地址保留原组合，历史卡在数据中标记 `archived`。新角色使用新的稳定ID，不覆盖旧卡的提示词历史。已另存的个人外观卡保持独立。\n'
    (root/'docs/combinations.md').write_text(text,encoding='utf-8')
