"""Build a public, bounded material audit report from committed evidence."""
import json
from html import escape
from pathlib import Path
from rights_audit import summary


def write_brand_preview(root, review):
    options = json.loads((root/'assets/brand/options/manifest.json').read_text(encoding='utf-8'))
    active = json.loads((root/'assets/brand/active.json').read_text(encoding='utf-8'))
    brands = [asset for asset in review['assets'] if asset['kind'] == 'project-brand-asset']
    historical = [asset for asset in brands if not asset['path'].startswith(active['directory'] + '/')]
    options.append({'id': active['id'], 'name': '现用 · ' + active['name'],
                    'description': '当前采用的标志，放在这里对照。',
                    'directory': active['directory'], 'mark': active['directory'] + '/logo.svg'})
    cards = []
    for option in options:
        directory = option['directory']
        files = sorted(asset['path'] for asset in brands if Path(asset['path']).parent.as_posix() == directory)
        relative = lambda name: escape(Path(name).relative_to('assets/brand').as_posix(), quote=True)
        links = ''.join(f'<li><a href="{relative(name)}" target="_blank" rel="noopener">{escape(Path(name).name)}</a></li>' for name in files)
        previews = ''.join(f'<a class="sample {theme}" href="{relative(image)}" target="_blank" rel="noopener" aria-label="{escape(option["name"],quote=True)}，查看{label}图稿"><img src="{relative(image)}" alt="{escape(option["name"],quote=True)}，{label}背景"><span>{label}</span></a>'
                           for theme, label, image in [('light', '浅色', option['mark']), ('dark', '深色', directory + '/favicon-dark.svg')])
        cards.append(f'<article><h2>{escape(option["name"])}</h2><div class="samples">{previews}</div><p>{escape(option["description"])}</p><details><summary>相关文件 · {len(files)}</summary><ul>{links}</ul></details></article>')
    text = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo 草案预览 · 女性之美</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f0e9;color:#392f2b;font:15px/1.6 system-ui,"Microsoft YaHei",sans-serif}main{max-width:1240px;margin:auto;padding:30px 28px 36px}header{margin-bottom:24px}h1{font-size:28px;margin:0 0 6px}header p{margin:6px 0;color:#6f6259}.note{padding:11px 15px;background:#fffaf2;border-left:3px solid #ab825a;border-radius:4px}a{color:#805d40;text-underline-offset:3px}.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}article{min-width:0;background:#fffdf9;border:1px solid #dfd4c7;border-radius:14px;padding:15px}h2{font-size:17px;margin:0 0 12px}.samples{display:grid;grid-template-columns:1fr 1fr;gap:8px}.sample{height:154px;position:relative;display:flex;align-items:center;justify-content:center;border:1px solid #e0d7cd;border-radius:9px;padding:9px 7px 27px;text-decoration:none}.light{background:#faf7f2}.dark{background:#202c28;border-color:#202c28}.sample img{max-width:100%;max-height:112px;object-fit:contain}.sample span{position:absolute;bottom:5px;font-size:11px;color:#8b7b6d}.dark span{color:#c7d6ce}article p{font-size:13px;color:#75695f;min-height:42px;margin:12px 0 8px}details{font-size:12px;border-top:1px solid #e9e0d6;padding-top:9px}summary{cursor:pointer;color:#876545}ul{padding-left:19px;margin-bottom:0}li{overflow-wrap:anywhere}footer{font-size:13px;color:#75695f;margin-top:22px}.sample:hover{outline:2px solid #ad875f;outline-offset:2px}a:focus-visible,summary:focus-visible{outline:3px solid #ad875f;outline-offset:3px}
@media(max-width:900px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:480px){main{padding:22px 14px}.grid{gap:10px}article{padding:11px}.sample{height:124px;padding:5px 4px 23px}.sample img{max-height:91px}h2{font-size:15px}h1{font-size:24px}}
</style></head><body><main><header><h1>Logo 草案预览</h1>
'''
    text += f'<p>{len(options)-1}套未采用方案 · {len(historical)}个图像文件（含尺寸与配色变体） · 附现用标志作对照</p>'
    text += '<p class="note">旧Logo草案的额外排查已结束。保留现有方案，后续出现具体侵权线索时再针对性处理。</p></header><div class="grid">'
    text += ''.join(cards)
    text += '</div><footer>点击图稿可查看原文件；展开“相关文件”可查看各尺寸及配色。<br><a href="../../docs/material-rights-audit.md">素材审核说明</a> · <a href="../../index.html">返回图鉴</a></footer></main></body></html>\n'
    (root/'assets/brand/history-preview.html').write_text(text, encoding='utf-8')


def write_rights_docs(root):
    path = root/'source/rights-review.json'
    evidence_path = root/'source/rights-evidence.json'
    if not evidence_path.exists():
        return
    review = json.loads(path.read_text(encoding='utf-8'))
    evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
    write_brand_preview(root, review)
    result = summary(review)
    ai_assets = [asset for asset in review['assets'] if asset['kind'] in {'ai-catalog-declaration','ai-generated-reference'}]
    ai_matched = sum(asset.get('provenance',{}).get('status')=='generated-file-match' for asset in ai_assets)
    photos = [asset for asset in review['assets'] if asset['kind'] == 'third-party-museum-photo']
    brands = [asset for asset in review['assets'] if asset['kind'] == 'project-brand-asset']
    dated_ai = sum(bool(asset.get('generated_at')) for asset in ai_assets)
    active_brands = sum(asset['path'].startswith('assets/brand/beauty-profile/') for asset in brands)
    historical_brands = len(brands) - active_brands
    text = f'''# 素材来源与权利审核

核验日期：{review['audit']['checked']}。本轮覆盖当前清单 {result['assets']} 个资产记录，内容版 {review['audit']['catalog_version']}。

代码采用MIT；项目有权授权的编辑内容、AI配图和品牌图形现采用CC BY-NC 4.0，仅非商业使用，见[许可范围](../LICENSE-SCOPE.md)与[素材许可正文](../CONTENT-LICENSE)。来源核验和对外授权分别记录；第三方例外保留原条件，生成记录不保证独占版权。

## 本轮核验结果

| 项目 | 结果 |
| --- | --- |
| 现用AI图页 | 清单共{len(ai_assets)}张，{ai_matched}张与本会话生成目录中的文件SHA-256相符；模型名称未知时保留null |
| 最初五张总图 | 初始提示词已在prompts/image-prompts.json找回；不伪造生成日期或输入记录 |
| 馆藏照片 | {len(photos)}张；核对官方API的isPublicDomain、作品页、官方图像与本地缩放/重编码图的对应关系 |
| 项目Logo与图标 | {len(brands)}个文件；其中{active_brands}个是现用标志及导出文件，{historical_brands}个是未采用的旧Logo草案及导出文件 |
| 配图编辑链 | 检查序列化记录中的输入路径、文件存在性和生成文件匹配；未记录的历史输入不作“从未使用外部图”的保证 |
| 针对性图像复核 | 角色名、品牌名或作者名触发的6张AI图页、6张馆藏图及当前标志；没有宣称逐张视觉审查全部图页 |
| 字体与依赖 | 没有分发字体文件；系统字体名仅作为CSS回退。构建/测试依赖及许可见THIRD_PARTY_NOTICES.md |

'''
    text += '资产状态统计：' + '、'.join(f'{key} {value}项' for key,value in result['status'].items()) + '。\n\n'
    text += f'''{ai_matched}张图页的字节来源已经确认；这不等于每张图的所有输入、人物近似性和在所有地区的权利都已获得法律保证。本轮以文件、维护记录、现有输入链、公开来源和针对性复核为边界。

## 名称与生成图像的复核说明

2026-11-03，所有者补充确认了以下生成结果。结合已进行的针对性图像复核，修正此前仅由检索名、主题名或通用元素产生的过度标记；这些名称不作为图片身份或复用原画的证据。

- AH065—AH096：三叶、小圆、Lain等是检索参考入口。图例展示另行生成的人物和发绳结构；所有者确认生成结果与这些角色无关。撤销由这些入口引出的额外输入复核标记，保留检索别名。
- SH001—SH016：图例是另行生成的人物、服装和徽记；所有者确认其与版权超级英雄形象完全不同。披风、护腕、面罩等通用元素本身不构成复用某个角色的依据；撤销此前要求独立复审或重做的结论。
- VF001—VF016与XA006：“维密风格”“新海诚感”是主题或风格入口，图例是生成示意，并非品牌官方图片或影片原画。本轮未观察到品牌字样或具体影片画面的直接复制，不把名称本身作为图片复用的依据。

上述三张图页此前的额外复核标记已撤销。随后，所有者决定项目素材先仅非商业使用，现有项目图页、Logo与图标均已按具体文件哈希登记CC BY-NC 4.0授权，状态为`cleared`；六张馆藏照片保留CC0。此前的撤销记录作为历史过程保留，不冒充当时已经选定许可。

## “早期生成元数据”具体指什么

它指之前制作图页时保存的生成记录，不是另一批来源不明的旧图片。记录分散在`source/image-jobs.json`、`prompts/image-prompts.json`和图页维护源中，核对结果汇总于`source/rights-provenance.json`。

- 现用{len(ai_assets)}张图页均已匹配到本会话生成文件，提示词位置也已登记。
- 其中{len(ai_assets)-dated_ai}张的准确生成日期未被结构化记录；{dated_ai}张有日期记录。未记录的具体模型名称保持`null`，不根据文件修改时间倒推。
- 历史对话中没有序列化保存的输入方式不作补写。这里是记录完整性的边界，不能据此判定已经使用未经授权的原图。
- 旧表述“账号合同”指生成时账号适用的服务条款版本，并非认定有合同缺失或必须为每张图补交一份合同。当前公开条款作为通用参考，不冒充已核实的历史账号合同。

## “未采用的Logo草案”具体指什么

此前的“历史品牌候选”专指本项目早期试做、后来未采用的Logo与标签图标，不是服装品牌素材，也不是图鉴配图。

- 旧文件位于`assets/brand/`根目录和`assets/brand/options/`，包括花瓣、蝴蝶、月亮、女字、书页、眼睛等候选方案，以及各自的PNG、SVG、ICO尺寸和配色导出；共{historical_brands}个图片文件，不是{historical_brands}套设计。
- 当前采用“头肩侧影”，位于`assets/brand/beauty-profile/`，由`assets/brand/active.json`指定，共{active_brands}个现用图片文件。
- “未采用”仅表示使用状态，不代表侵权；本轮没有记录这些草案侵权的具体证据。旧Logo草案与当前标志同样按CC BY-NC 4.0登记非商业授权。
- 所有者于2026-11-03决定结束本项额外排查，保留现有草案；不将穷尽全互联网的相似性检索作为本项完成或项目开放的前提。后续出现具体投诉、相似对象或其他明确线索时再针对性核查和修改。本项不再列为待办。
- 旧方案未用于图鉴主页面的Logo或标签图标。原文件保留，可在[Logo草案预览](../assets/brand/history-preview.html)中查看全部方案、浅深色效果与各尺寸文件。

## 馆藏照片核验

'''
    text += '| 文件 | 状态 | 官方作品页 | 本地与上游对应 |\n| --- | --- | --- | --- |\n'
    for asset in photos:
        p = asset['provenance']
        text += f"| {asset['path']} | {asset['status']} / {asset['license']} | [Met {p['object_id']}]({p['object_url']}) | 同一作品照片的缩放/重编码副本；不宣称原始字节一致 |\n"
    text += '''
Met的公开访问政策将其开放的公有领域作品图片按CC0提供；此处保留每张具体对象的API证据，未把所有馆藏图片笼统认定为CC0。

## 证据与机器检查

- [逐项资产记录](../source/rights-review.json)：每个文件的哈希、来源核验、使用依据、发布状态与输入链。
- [公共证据索引](../source/rights-evidence.json)：官方条款、生成文件核对、馆藏API摘录和针对性复核范围。
- [生成与输入来源索引](../source/rights-provenance.json)：现用图页及其已记录输入的可追溯信息；不含个人绝对路径。
- [许可决策](../source/license-policy.json)：代码MIT与素材CC BY-NC 4.0分开登记；商业使用未获授权，第三方例外保留原条件。
- 逐项非商业授权证据以所有者决策为依据，绑定文件路径与SHA-256；以后新增文件不能仅凭同目录或生成工具条款自动放行。
- 本地收据与上游核验缓存保存在私有.work中，不打包到公开源码；公开记录保留文件哈希与可核查的上游链接。
- 已记录的历史输入图不因出现在索引中而自动纳入分发包；其本地存在状态是本次核验时的记录。

验证器检查路径、哈希、证据编号及已放行素材的许可依据。给文件手动填入cleared而没有证据不能通过。`--release`仍会拦住未决定的内容许可和未放行素材；不会因为根目录出现MIT LICENSE就把整库判断为可发布。

## 核验参考

'''
    for record in evidence['records']:
        if record.get('url') and record.get('kind') == 'official-policy':
            text += f"- [{record['title']}]({record['url']})；核对日期 {record['checked']}。\n"
    (root/'docs/material-rights-audit.md').write_text(text,encoding='utf-8')
