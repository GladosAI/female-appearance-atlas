# 一起完善女性之美

欢迎补充素材、修正名称和翻译、改善配图与裁剪、改进检索与可访问性。图鉴提供可自由挑选的参考，不规定完整角色需要哪些部件。

## 先确认是否已收录

```sh
python tools/query_atlas.py "ribbon" --category hair_with_accessories
python tools/query_atlas.py --id AH020 --full
python tools/query_atlas.py --list categories
```

先查名称、英文、别名和所属细分。普通同义词优先加 aliases；视觉结构、穿着方式或表达有明显区别再新增词条。

## 提交素材

1. 先用 Issue 说明词条名称、现有近似编号、差异与合适目录，避免多位贡献者重复制作。
2. 复制 `source/contributions/example.json.example`，保存为新的 `.json` 文件。普通新增只需补 entries 和 boards；已有类别的名称、guide 和默认阅读来源会由构建器填充。
3. 为词条分配未使用的 `stable_id`，编号前缀应沿用所属类别；检查 `source/id-registry.json`。PR 冲突时只调整未发布的新编号，旧编号不能复用。新类别另开讨论，并同步导航和编号前缀。
4. 图片放入图片资源包；提交相对路径、尺寸、网格、准确边界和词条映射。不要在主源码仓库提交原图、离线复制 sidecar、ZIP、个人外观卡或缓存。提交方式可采用资源附件和 SHA-256 清单；维护者审核后纳入下一版图片包。
5. 补充来源、生成工具/模型（已知时）、日期、提示词位置、参考图来源及使用许可。未知就写未知，不以“AI 生成”代替权利说明。无需上传私人生成工具目录。
6. 运行构建、数据验证与相应测试，在 PR 中说明通过的检查及尚需人工核实的项目。

图像必须与词条特征相符、关键结构完整且裁剪不跨格。不同视角不强制逐条制作；通用方向、机位和景别优先复用“画风与视觉表现”中的视角与拍摄图鉴。年代、文化和幻想改编请明确语境。

## 修改现有内容

系统示例维护在 `source/system-examples.json`。每张写清楚一位具体人物的身份、场景与气质，再选择能共同表达她的发型、服装、表情、动作、饰物和画风。参考数量保持精简，整组通过不同角色展现多样性。角色设计优先于类别覆盖率，避免为了补齐统计而加入无关参考。保留已发布的示例字符串ID与归档链接；更换成另一个人物时分配新ID，保留用户原来的提示词历史。

历史编辑数据在 `source/catalog/`。改名时给该原始字典添加 `stable_id: "原编号"`，避免被识别为新增；后续移动分类也如此。既有 ID 登记保留，删除的词条也不回收编号。更改核心字段或外观卡格式时提供迁移说明。

## 提交前检查

```sh
python tools/build_atlas.py --skip-package
python tools/validate_atlas.py
python -m unittest discover -s tests -v
npm ci
npx playwright install chromium
npm run test:browser
```

无图片包时可执行 `python tools/validate_atlas.py --metadata-only`，但不能宣称完成图片验收。公开发布另运行 `python tools/validate_atlas.py --release`，许可或素材权利仍待审核时应失败。

## 贡献许可与审核

代码贡献按[MIT](LICENSE)接纳；有权授权的素材与编辑内容贡献按[CC BY-NC 4.0](CONTENT-LICENSE)接纳，仅供非商业使用。提交时明确作者、生成或参考来源、适用许可及第三方例外；不能将其他人的作品仅凭上传就改为项目许可。范围见[LICENSE-SCOPE.md](LICENSE-SCOPE.md)。

贡献者保留实际拥有的权利，不要求转让版权；提交贡献不自动授予维护者日后任意放开商用的权限。未来若为已有社区贡献增加商业许可，需取得对应授权。当前没有广告镜像或其他商用例外。

AI Agent 产生的提交同样需要人工核对权利、分类和图片。维护者通过 PR 审核接纳贡献；任何协作者都不能因为自动测试通过就跳过素材审核。
