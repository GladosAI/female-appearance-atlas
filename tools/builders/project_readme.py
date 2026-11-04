import json


def write_usage_readme(root):
    data=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
    navigation=json.loads((root/'data/navigation.json').read_text(encoding='utf-8'))
    meta=data['meta']
    package=json.loads((root/'package.json').read_text(encoding='utf-8'))
    repository=package['repository']['url'].removeprefix('git+').removesuffix('.git')
    text=f'''# 女性之美

**女性角色外观图鉴**

面向游戏、动漫和角色创作的可检索素材仓库。内容版 {meta['version']}：{meta['entry_count']:,} 个配图词条、{meta['board_count']} 张图页、{meta['category_count']} 个类别、{len(navigation['groups'])} 个领域。支持检索、筛选、外观卡收藏、同类参考排列与 AI 提示词导出；不规定角色必填部件或自动生成流程。

> **代码采用[MIT](LICENSE)；项目有权授权的图鉴文字、数据、提示词、AI配图与Logo采用[CC BY-NC 4.0](CONTENT-LICENSE)，仅非商业使用。** 六张Met馆藏照片等第三方例外保留原许可。范围见[LICENSE-SCOPE.md](LICENSE-SCOPE.md)，详见[素材说明](NOTICE.md)与[当前许可决策](docs/licensing-proposal.md)。当前未授予商用或广告盈利镜像例外。

[源码仓库]({repository}) · [版本与资源包]({repository}/releases) · [问题反馈]({repository}/issues)

首个图片及离线复制资源包将在首次Release提供。直接下载源码不包含图鉴原图；网页在线阅览地址将在部署后公布。

## 浏览与使用

完整离线包解压后双击 **index.html**，保留 images 目录。也可在此目录运行 `python -m http.server 8000`，浏览 http://127.0.0.1:8000/ 。普通浏览不需要 Node 或 AI 接口。

[打开总目录](index.html?view=directory) · [完整分类表](docs/directory.md) · [检索说明](docs/find-and-browse.md) · [视角与拍摄图鉴](index.html?section=branch_camera_viewpoints) · [游戏角色原稿方法](index.html?section=branch_game_character_design)

目录按“领域 → 分组 → 类别 → 细分”组织，风格作为筛选条件，画风独立归类。外观卡可保存多张；图鉴连续排列，个人卡默认最新加入在前，可切换按类别排序，不显示独立分类区块。提示词方案在当前浏览器留存，可恢复勾选与手动修改，不上传用户数据。

[系统角色卡](docs/combinations.md) 围绕具体人物与场景搭配，可按题材、精选角色或关键词查找，并另存编辑。整组通过不同年龄、身份、时代、气质、形态与画风展现多样性。维护源为 `source/system-examples.json`；旧链接与已另存的个人卡继续保留。

| 领域 | 类别 | 词条 |
| --- | ---: | ---: |
'''
    for group in navigation['groups']:
        text+=f"| [{group['name']}](index.html?section={group['scope']}) | {group['category_count']} | {group['count']} |\n"
    text+=f'''
## 开发与贡献

Python 3.10+ 构建器只用标准库；Node 22+ / npm 用于浏览器检查和图片优化。源码包不携带大图片资源包，无图片时可先进行文字、数据和页面协作。

```sh
git clone {repository}.git
cd female-appearance-atlas
npm ci
python tools/validate_atlas.py --metadata-only
python -m unittest discover -s tests -v
```

获取并解压图片包后：

```sh
python tools/build_atlas.py --skip-package
python tools/validate_atlas.py
npx playwright install chromium
npm run test:browser
```

[贡献指南](CONTRIBUTING.md) · [维护与镜像](GOVERNANCE.md) · [社区协作](CODE_OF_CONDUCT.md) · [独立构建](docs/development.md) · [数据契约与评估](docs/data-contract.md) · [Agent 查询](docs/agent-query.md) · [隐私与安全](SECURITY.md) · [变更记录](CHANGELOG.md)

## 发布与在线阅览

```sh
python tools/release_atlas.py web --image-mode webp --output dist/web-preview
python tools/release_atlas.py packages --output dist/release-review
```

在线预览将数据独立缓存并压缩配图，明确标注预览质量；原图版和离线原图保留。三个离线ZIP分别为源码、图片和本地复制数据，解压到同一位置即可。完整说明见 [部署与成本](docs/deployment.md)。这些命令只产生本地待审文件，不会自动发布或购买服务；公开前执行 `python tools/validate_atlas.py --release`。

## 数据与文件

`source/catalog/` 保存历史编辑源，新增贡献在 `source/contributions/`，`source/id-registry.json` 锁定已发布编号。`source/navigation.json` 保存主目录；`tools/templates/` 保存页面；`data/` 和大部分专题文档由构建器生成。`source/rights-review.json` 记录素材审核状态。

`.work/`、`dist/`、`node_modules/`、图片原图和离线图片读取数据不提交到源码仓库。不要只改生成的 index.html，也不要以新排序重排旧编号。
'''
    (root/'README.md').write_text(text,encoding='utf-8')
