"""Keep offline image export sources current; PNG fallback needs no dependencies."""
import base64,hashlib,json

def prepare_image_exports(root,data):
    images=sorted({e[k]['image'] for e in data['entries'] for k in ['visual','wearing_visual','fullbody_visual'] if e.get(k)})
    index_path=root/'data/image-export-index.json'
    index=json.loads(index_path.read_text(encoding='utf-8')) if index_path.exists() else {}
    (root/'images/export-data').mkdir(parents=True,exist_ok=True)
    result={}
    for image in images:
        content=(root/image).read_bytes();fingerprint=hashlib.sha256(content).hexdigest()
        old=index.get(image,{})
        if old.get('source_sha256')!=fingerprint or not (root/old.get('file','missing')).is_file():
            suffix=(root/image).suffix.lower()
            mime={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif'}.get(suffix,'image/png')
            file='images/export-data/'+hashlib.sha256(image.encode()).hexdigest()[:12]+'-'+fingerprint[:12]+'.js'
            encoded='data:'+mime+';base64,'+base64.b64encode(content).decode('ascii')
            script='(globalThis.__atlasImageData ||= Object.create(null))['+json.dumps(image)+']='+json.dumps(encoded)+';\n'
            (root/file).write_text(script,encoding='utf-8')
            old={'source_sha256':fingerprint,'mime':mime,'file':file}
        result[image]=old
    index_path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {image:record['file'] for image,record in result.items()}
