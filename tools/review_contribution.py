"""Review a new contribution draft without changing IDs, images or authorization records."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import unicodedata
from urllib.parse import urlparse


def review_proposal(payload,catalog,registered,prefixes,image=None):
    errors=[];warnings=[];related=[];verified=False
    if not isinstance(payload,dict) or payload.get('schema')!='female-appearance-contribution/v1':
        return {'valid':False,'errors':['不是支持的贡献文件格式'],'warnings':[],'related':[],'image_hash_verified':False}
    entries=payload.get('entries');boards=payload.get('boards')
    if not isinstance(entries,list) or not entries or not isinstance(boards,list) or not boards:
        return {'valid':False,'errors':['贡献需要词条与图页列表'],'warnings':[],'related':[],'image_hash_verified':False}
    category_ids={c['id'] for c in catalog['categories']}
    normalize=lambda value:unicodedata.normalize('NFKC',str(value)).casefold().strip()
    ids=[]
    for entry in entries:
        if not isinstance(entry,dict):errors.append('词条必须为对象');continue
        identifier=entry.get('stable_id','');category=entry.get('category')
        if not isinstance(category,str):errors.append('类别必须为字符串');category=''
        if not isinstance(identifier,str) or not re.fullmatch(r'[A-Z][A-Z0-9_]*\d{3,}',identifier):errors.append('无效的建议编号');continue
        elif identifier in registered:errors.append('编号已经登记，不能用于新词条：'+identifier)
        elif category in prefixes and not re.fullmatch(re.escape(prefixes[category])+r'\d{3,}',identifier):errors.append('编号前缀不属于所选类别：'+identifier)
        if category not in category_ids:errors.append('未知类别：'+str(category))
        for field in ['name','en','description','dimension']:
            if not isinstance(entry.get(field),str) or not entry[field].strip():errors.append('缺少词条字段：'+field)
        if identifier in ids:errors.append('贡献文件中重复编号：'+str(identifier))
        ids.append(identifier)
        name,en=normalize(entry.get('name','')),normalize(entry.get('en',''))
        for old in catalog['entries']:
            if name and (name in normalize(old['name']) or normalize(old['name']) in name) or en and en==normalize(old['en']):
                if old['id'] not in related:related.append(old['id'])
                if name==normalize(old['name']) and en==normalize(old['en']):errors.append('同名同英文词条已存在：'+old['id'])
    existing_boards={b['id'] for b in catalog.get('boards',[])};mapped=set();board_ids=set()
    for board in boards:
        if not isinstance(board,dict):errors.append('图页必须为对象');continue
        name=board.get('id','');relative=board.get('image','')
        if not isinstance(name,str) or not re.fullmatch(r'[A-Za-z0-9_-]+',name):errors.append('无效的图页编号');continue
        elif name in existing_boards or name in board_ids:errors.append('图页编号已使用：'+name)
        board_ids.add(name)
        if not isinstance(relative,str):relative=''
        path=PurePosixPath(relative)
        if path.is_absolute() or '..' in path.parts or '\\' in relative or ':' in relative or path.parts[:1]!=('images',) or path.suffix.lower() not in {'.png','.jpg','.jpeg','.webp'}:
            errors.append('图页必须使用images目录内的相对图片路径')
        for field in ['width','height','columns','rows']:
            if type(board.get(field)) is not int or board[field]<=0:errors.append('无效的图页尺寸或网格：'+field)
        items=board.get('items',[])
        if not isinstance(items,list):errors.append('图页items必须为列表');continue
        for item in items:
            entry_id=item.get('entry_id') if isinstance(item,dict) else None
            if not isinstance(entry_id,str) or entry_id not in ids:errors.append('图页引用了贡献中不存在的词条：'+str(entry_id))
            else:mapped.add(entry_id)
    if set(ids)-mapped:errors.append('有词条没有图页映射')
    submission=payload.get('submission',{})
    if not isinstance(submission,dict):submission={}
    if submission.get('status')!='pending-review':errors.append('贡献文件应标记为pending-review，不能自行标为审核通过')
    for field in ['author','license']:
        if not isinstance(submission.get(field),str) or not submission[field].strip():errors.append('缺少有效的署名或授权说明：'+field)
    method=submission.get('creation_method');license_id=submission.get('license')
    if not isinstance(method,str) or method not in {'original','ai-generated','third-party'}:errors.append('缺少有效的来源方式')
    if not isinstance(license_id,str) or license_id not in {'CC-BY-NC-4.0','CC0-1.0','other'}:errors.append('未知的授权说明')
    source=submission.get('source_url')
    if source is not None and not isinstance(source,str):errors.append('来源链接必须为字符串');source=None
    if source or method=='third-party' or license_id!='CC-BY-NC-4.0':
        try:
            parsed=urlparse(source or '')
            if parsed.scheme not in {'http','https'} or not parsed.hostname:raise ValueError()
        except ValueError:errors.append('缺少有效的公开来源或授权依据链接')
    if license_id=='other' and (not isinstance(submission.get('rights_note'),str) or not submission['rights_note'].strip()):errors.append('其他授权需要补充说明')
    asset=submission.get('image',{})
    if not isinstance(asset,dict):asset={}
    digest=asset.get('sha256','')
    if not isinstance(digest,str) or not re.fullmatch('[0-9a-f]{64}',digest) or type(asset.get('bytes')) is not int or asset['bytes']<=0:
        errors.append('缺少有效的图片SHA-256或字节数')
    if image is not None:
        if len(boards)!=1:errors.append('--image仅用于单张配图的贡献文件')
        elif image.is_file():
            actual=hashlib.sha256(image.read_bytes()).hexdigest()
            verified=actual==digest and image.stat().st_size==asset.get('bytes')
            if not verified:errors.append('原图与贡献记录的哈希或大小不同')
        else:errors.append('找不到提供的原图文件')
    else:warnings.append('未提供原图，尚未核对图片哈希')
    if related:warnings.append('找到近似词条，请说明视觉差异')
    warnings.append('此检查不会批准素材权利或图片语义；仍须维护者审核')
    return {'valid':not errors,'errors':errors,'warnings':warnings,'related':related[:10],'image_hash_verified':verified}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('proposal',type=Path);parser.add_argument('--image',type=Path);args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    catalog=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
    registry=json.loads((root/'source/id-registry.json').read_text(encoding='utf-8'))
    raw=(root/'assets/contribution-index.js').read_text(encoding='utf-8')
    index=json.loads(raw.removeprefix('window.ATLAS_CONTRIBUTION=').rstrip(';\n'))
    result=review_proposal(json.loads(args.proposal.read_text(encoding='utf-8')),catalog,
                           {r['id'] for r in registry['entries']},{c['id']:c['prefix'] for c in index['categories']},args.image)
    print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['valid'] else 1)


if __name__=='__main__':main()
