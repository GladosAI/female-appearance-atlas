# 独立开发与验证

Python 3.10+ 可构建和查询；页面浏览不需要 Python/Node。Node 22+ 及 npm 仅用于浏览器检查、WebP 预览和离线图片读取数据优化。

1. 获取源码并把对应版本的图片资源包解压到同一目录，确保 `images/` 中有原图。普通代码/文字贡献可暂不获取图片包。
2. 执行 `npm ci`；浏览器测试前执行 `npx playwright install chromium`（Linux CI 使用 `--with-deps`）。默认用 Playwright 管理的 Chromium；需要已有浏览器时设置 `ATLAS_BROWSER_EXECUTABLE`。
3. `python tools/build_atlas.py --skip-package` 生成本地页面与数据。构建器只使用 Python 标准库；Node 缺席时离线图片读取源可用原始 PNG 生成，体积可能更大。
4. `python tools/validate_atlas.py` 检查全目录；`python -m unittest discover -s tests -v` 运行数据规则测试；`npm run test:browser` 检查页面工作流。
5. `python -m http.server 8000` 后浏览 `http://127.0.0.1:8000/`；也保留直接双击 index.html 的方式。

无图片包时：`python tools/validate_atlas.py --metadata-only` 可检查提交的数据关系。不能据此声称本地图片存在或裁剪已人工验收。完整构建要求原图存在，失败时不要把缺图断言关闭。

`tools/qa/` 中较早的版本专项脚本保留作回归资料，部分断言对应旧数量；默认 CI 运行当前工作流测试，不把全部历史专项混成一条命令。

根目录、用户名和浏览器安装目录不得写死；产物只写到本项目 `.work/` 和 `dist/`。`--skip-package` 避免每次编辑都压缩几 GB 文件。所有本地验证结果保存在 `.work/`，不纳入 Git。

无图片包也可以运行 `python tools/build_atlas.py --check-generated`，从维护源在内存中重建并核对已生成的数据与页面；此检查不读取原图。`source/character-research*.json` 是可选的外部工作区协作快照，不参与构建，也不进入独立源码包。

`.gitattributes`将普通程序和文档统一为LF；`data/`、`assets/brand/`、图片和两份许可正文按原始字节保存。这些文件参与数据清单或来源哈希核验，不能由Git自动转换换行；修改生成数据后应重新构建对应清单。测试会在临时Git仓库中模拟两种换行设置的检出，确认哈希不变。
