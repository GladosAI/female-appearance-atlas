# 女性之美 · 品牌图形

正式标志为用户选定的「01 头肩侧影」：以流动长发、侧脸外缘与颈肩姿态呈现女性美感，面部五官留白。页面将标志与「女性之美／女性角色外观图鉴」组合展示。

`active.json` 指定当前标志。正式文件位于 `beauty-profile/`：

- `source.png`：选定方案的透明原始图稿，1254 × 1254，保留生成结果的原始字节。
- `generation-prompts.json`：生成提示记录；当前选定项为 `beauty_profile`。
- `logo.svg`：嵌入透明位图并使用颜色滤镜的 SVG 展示文件，可随页面配色变色；不包含描摹的矢量轮廓。
- `logo.png`：512 × 512 的透明图稿。
- `favicon.svg`：自动适配系统明暗的标签图标。
- `favicon-light.svg`、`favicon-light-linen.svg`、`favicon-dark.svg`、`favicon-dark-forest.svg`：四套配色对应的标签图标。
- `favicon.ico`：含 16、32、48、256 像素图层的兼容图标。
- `favicon-16.png`、`favicon-32.png`、`favicon-48.png`：常用标签图标尺寸。
- `apple-touch-icon.png`：180 × 180 的设备收藏图标。
- `icon-192.png`、`icon-512.png`：快捷方式图标。
- `release.json`：来源校验值、配色和导出格式记录。

选定原稿 SHA256：`f85b2a3b3b72b6d801eb3870b6f19f91ec9437879d5b9ad148af7a1282625f67`。

页面已移除候选切换区。根目录中的旧版图稿与 `options/` 为历史草案，当前页面不再引用，也不再读取旧的 Logo 选择记录。四套页面配色与默认跟随系统的设置继续保留。

[Logo草案预览](history-preview.html)集中展示7套未采用方案及现用标志，提供浅深色背景与原文件链接，由`tools/builders/rights_docs.py`随图鉴构建生成。“未采用”仅指使用状态；此前审核没有记录这些草案侵权的具体证据。

所有者已决定结束旧Logo草案的额外排查，保留现有方案，不以全网相似性检索为前提；后续有具体侵权线索时再针对性处理。
当前项目有权授权的Logo、图标及旧草案已采用CC BY-NC 4.0，仅非商业使用；正文与范围见根目录`CONTENT-LICENSE`和`LICENSE-SCOPE.md`。不授予冒充官方或暗示背书的权利。

修改配色后，在图鉴根目录运行 `node tools/builders/brand_assets.cjs` 重新导出图标，再运行 `python tools/build_atlas.py` 更新页面和离线包。导出工具使用 sharp，可从本地依赖或 Codex 工作区依赖加载。
