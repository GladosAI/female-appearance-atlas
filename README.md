# 女性之美

**女性角色外观图鉴**

面向游戏、动漫和角色创作的可检索素材仓库。内容版 74.0：7,241 个配图词条、722 张图页、211 个类别、9 个领域。支持检索、筛选、外观卡收藏、同类参考排列与 AI 提示词导出；不规定角色必填部件或自动生成流程。

> **代码采用[MIT](LICENSE)；项目有权授权的图鉴文字、数据、提示词、AI配图与Logo采用[CC BY-NC 4.0](CONTENT-LICENSE)，仅非商业使用。** 六张Met馆藏照片等第三方例外保留原许可。范围见[LICENSE-SCOPE.md](LICENSE-SCOPE.md)，详见[素材说明](NOTICE.md)与[当前许可决策](docs/licensing-proposal.md)。当前未授予商用或广告盈利镜像例外。

[在线阅览](https://gladosai.github.io/female-appearance-atlas/) · [源码仓库](https://github.com/GladosAI/female-appearance-atlas) · [版本与资源包](https://github.com/GladosAI/female-appearance-atlas/releases) · [问题反馈](https://github.com/GladosAI/female-appearance-atlas/issues)

无需下载即可[在线浏览图鉴](https://gladosai.github.io/female-appearance-atlas/)；当前程序版 **0.4.2**，内容版 **74.0**。需要原图或离线使用时，从[Releases](https://github.com/GladosAI/female-appearance-atlas/releases/latest)获取以下资源包。程序更新复用明确标记版本的图片资源，不必重复下载未变化的图片。

| 下载 | 内容与用途 |
| --- | --- |
| [源码与页面](https://github.com/GladosAI/female-appearance-atlas/releases/latest/download/female-appearance-atlas-source.zip) | 必需，含index.html、程序、词条数据、文档与许可 |
| [图片资源](https://github.com/GladosAI/female-appearance-atlas/releases/download/v74.0/female-appearance-atlas-images.zip) | 必需，含图鉴原图；资源版v74.0 |
| [离线图片读取数据](https://github.com/GladosAI/female-appearance-atlas/releases/download/v74.0/female-appearance-atlas-offline-copy.zip) | 本地双击时导出图片所需；资源版v74.0；通过HTTP访问可省略 |
| [SHA-256校验清单](https://github.com/GladosAI/female-appearance-atlas/releases/latest/download/CHECKSUMS.json) | 核对三个ZIP的大小与完整性 |

## 浏览与使用

将三个ZIP解压到**同一个目标目录**，合并同名的`female-appearance-atlas`文件夹；打开该文件夹中的**index.html**，保留同层的`images/`目录。也可只获取源码与图片包，在该文件夹运行`python -m http.server 8000`后浏览http://127.0.0.1:8000/。普通浏览不需要Node或AI接口。

[打开总目录](index.html?view=directory) · [完整分类表](docs/directory.md) · [检索说明](docs/find-and-browse.md) · [视角与拍摄图鉴](index.html?section=branch_camera_viewpoints) · [游戏角色原稿方法](index.html?section=branch_game_character_design) · [场景与人物活动](index.html?section=branch_scene_character_design)

目录按“领域 → 分组 → 类别 → 细分”组织，风格作为筛选条件，画风独立归类。外观卡可保存多张；图鉴连续排列，个人卡默认最新加入在前，可切换按类别排序，不显示独立分类区块。提示词方案在当前浏览器留存，可恢复勾选与手动修改，不上传用户数据。

[系统角色卡](docs/combinations.md) 围绕具体人物与场景搭配，可按题材、精选角色或关键词查找，并另存编辑。整组通过不同年龄、身份、时代、气质、形态与画风展现多样性。维护源为 `source/system-examples.json`；旧链接与已另存的个人卡继续保留。

| 领域 | 类别 | 词条 |
| --- | ---: | ---: |
| [头发与发型](index.html?section=topic_hair_design) | 8 | 531 |
| [脸部与表情](index.html?section=topic_face_design) | 19 | 834 |
| [身体与动作](index.html?section=topic_body_design) | 13 | 734 |
| [服装单件与日常穿搭](index.html?section=topic_everyday) | 29 | 1967 |
| [职业、主题与历史服装](index.html?section=topic_role_costumes) | 58 | 1508 |
| [配饰与随身物品](index.html?section=topic_accessory_design) | 25 | 646 |
| [幻想形态与Cosplay](index.html?section=topic_fantasy_design) | 16 | 464 |
| [材质、纹样与配色](index.html?section=topic_surface_design) | 4 | 183 |
| [画风与视觉表现](index.html?section=topic_art_styles) | 39 | 374 |

## 开发与贡献

无需编程即可使用[在线贡献表单](https://gladosai.github.io/female-appearance-atlas/contribute.html)：查找近似词条、预览本机图片、填写来源后，导出贡献JSON与命名后的原图。建议编号不预留名额，素材和授权由维护者审核。也可离线打开[contribute.html](contribute.html)。

Python 3.10+ 构建器只用标准库；Node 22+ / npm 用于浏览器检查和图片优化。源码包不携带大图片资源包，无图片时可先进行文字、数据和页面协作。

```sh
git clone https://github.com/GladosAI/female-appearance-atlas.git
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

[贡献指南](CONTRIBUTING.md) · [素材质量记录](docs/material-quality.md) · [维护与镜像](GOVERNANCE.md) · [社区协作](CODE_OF_CONDUCT.md) · [独立构建](docs/development.md) · [数据契约与评估](docs/data-contract.md) · [Agent 查询](docs/agent-query.md) · [隐私与安全](SECURITY.md) · [变更记录](CHANGELOG.md)

## 发布与在线阅览

```sh
python tools/release_atlas.py web --image-mode webp --output dist/web-preview
python tools/release_atlas.py packages --output dist/release-review
```

在线站点使用免费 GitHub Pages，数据独立缓存，配图使用 WebP 预览版；原图保留在 Release。`.github/workflows/pages.yml` 在发布正式 Release 后校验图片包、构建和检查在线版，再部署；也可在 Actions 中手动运行。上述本地命令不执行部署或购买服务。三个离线ZIP解压到同一位置即可。完整说明见 [部署与成本](docs/deployment.md)，公开前执行 `python tools/validate_atlas.py --release`。

## 数据与文件

`source/catalog/` 保存历史编辑源，新增贡献在 `source/contributions/`，`source/id-registry.json` 锁定已发布编号。`source/navigation.json` 保存主目录；`tools/templates/` 保存页面；`data/` 和大部分专题文档由构建器生成。`source/rights-review.json` 记录素材审核状态。

`.work/`、`dist/`、`node_modules/`、图片原图和离线图片读取数据不提交到源码仓库。不要只改生成的 index.html，也不要以新排序重排旧编号。
