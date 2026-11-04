"""Normalize generated document links to the organized offline layout."""
from pathlib import Path
import os, re

def finalize_docs(root):
    root = Path(root)
    locations = {}
    for folder in ['docs', 'data', 'prompts', 'source']:
        for p in (root / folder).iterdir():
            if p.is_file(): locations.setdefault(p.name, p.relative_to(root).as_posix())
    def normalize(text, parent):
        def link(match):
            target = match.group(1)
            if target.startswith(('https:', 'http:', '#', '../', 'data:')): return match.group(0)
            if target.startswith('images/'):
                relative = os.path.relpath(root / target, parent).replace('\\', '/')
            elif target.startswith('index.html'):
                relative = os.path.relpath(root / 'index.html', parent).replace('\\', '/') + target[len('index.html'):]
            elif target in locations:
                relative = os.path.relpath(root / locations[target], parent).replace('\\', '/')
            else: return match.group(0)
            return '(' + relative + ')'
        return re.sub(r'\(([^\s()]+)\)', link, text)
    for p in (root / 'docs').glob('*.md'):
        p.write_text(normalize(p.read_text(encoding='utf-8'), p.parent), encoding='utf-8')
    p = root / 'README.md'
    text = normalize(p.read_text(encoding='utf-8'), root)
    for old, new in sorted(locations.items(), key=lambda x: -len(x[0])):
        text = re.sub(r'(?<![\w/.-])' + re.escape(old) + r'(?![\w.-])', new, text)
    text = text.replace('项目根目录的 Start Appearance Atlas.cmd', '项目 launchers 目录中的 Start Appearance Atlas.cmd')
    text = text.replace('## 文件', '## 浏览入口\n\n从 [图鉴总目录](index.html?view=directory) 或 [文字总目录](docs/directory.md) 开始。92个类别按12个主题排列；服装单件、整套穿搭、历史服饰、职业装扮、配饰及幻想部件分别浏览。风格标签与交叉专题另列，可继续按细分、关键词和风格筛选。\n\n## 文件')
    text += '''\n## 目录用途\n\n| 目录 | 内容 |\n| --- | --- |\n| docs/ | 完整图鉴、服装与各专题文档 |\n| data/ | 页面使用的词条、图页、来源与组合 JSON |\n| images/ | 图鉴插图、原始生成版本和实物照片 |\n| prompts/ | 各版图页提示词 |\n| source/ | 图片任务、映射、参考输入和词条源代码 |\n| tools/ | 构建入口、图片登记、模板和当前检查工具 |\n| .work/ | 预览、缓存、锁和历次验证记录，不进入离线包 |\n\n构建：`python tools/build_atlas.py`。图片任务：`python tools/prepare_image_jobs.py`。当前页面检查：`node tools/qa/verify_atlas_v17.cjs`。\n\n最新离线包统一存放在项目 `outputs/packages/current/`；整理前的第17版包及旧版本位于 `outputs/packages/history/`。图鉴 index.html 地址保留，浏览器中已保存的外观卡可继续使用。\n'''
    p.write_text(text, encoding='utf-8')
