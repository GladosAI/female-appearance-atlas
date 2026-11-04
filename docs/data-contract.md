# 数据契约与项目评估

本项目是多维素材仓库，不设必填部件、不把同类条目强制视为冲突。词条可以是部件、整套搭配、状态、动作或表现方式；这些粒度不同，不能套用统一角色生成流程。

## 维护源与生成物

| 内容 | 维护源 | 生成物 |
| --- | --- | --- |
| 既有编辑词条 | `source/catalog/*.py` | `data/catalog.json` |
| 社区新增素材 | `source/contributions/*.json` | 同上，合并后统一验证 |
| 永久身份 | `source/id-registry.json` | 词条 id，供 URL、外观卡和跨词条引用使用 |
| 扩展类别 | `source/category-extensions.json`（显式前缀与类别定义） | 同一类别表 |
| 主目录 | `source/navigation.json` | `data/navigation.json` |
| 阅读来源 | `source/references.json`（唯一主记录） | `data/references.json` |
| 图页和裁剪 | `source/legacy-illustrations.json`、`source/extra-illustrations.json` | boards、visual、wearing_visual、fullbody_visual |
| 页面 | `tools/templates/` | `index.html` |
| Agent 查询 | 构建后从完整数据提取 | `data/agent-index.jsonl` |

目前完整词条包括大量历次扩展字段。`data/field-inventory.json` 记录实际字段、类型和覆盖量；保留这些字段以维持旧功能，不在一次重构中强行删除或统一语义。`schemas/catalog.schema.json` 约束公共核心，扩展字段继续允许，但新增字段必须说明作用与消费者。

## 公共核心

- `id`：永久、不复用、不随排序/分类而变化。初始 6,963 个已发布编号全部登记；旧记录即使退休仍留在登记表。
- `category`：主归属类别，一个词条只有一个主类别；主题和风格可以跨类别集合。
- `dimension`：类别内细分，不是完整的冲突判断规则。
- `name` / `en` / `aliases`：中文主名、英文和检索别名。别名不是另一个词条。
- `description` / `design_tip`：编辑描述与设计要点；不自动灌入用户导出提示词。
- `related_reading`：references 中存在的来源 ID。相关阅读不自动等于图片来源或图片授权。
- `visual`：主图；可选 `wearing_visual` / `fullbody_visual`。每个 visual 指向有效 board，并具有完整裁剪依据。
- `camera_reference` / `cinematic_reference`：通用视角或镜头语言参考，供拍摄专题与提示词类别消费；不把它们误归为人物配饰。
- `sequence_reference`：主图是同一词条的三格分镜；`sequence_labels` 为三个阶段标题，`sequence_order` 固定为 `left-to-right`。浏览卡片、详情与外观卡展示阶段顺序，提示词仍只导出词条名称。一个网格单元保存完整三格，不能把三格分配给三个词条。
- `visual_language_reference`：漫画单格或影视设计画面的参考，详情使用“画面设计要点”，AI提示词按实际类别列名。`single_panel_reference` 表示每项是一幅独立画面，不与三格顺序字段混用；`comic_panel_reference` 和 `film_design_reference` 分别供对应专题汇集。画中画只属于该单幅内部设计，不新增外部词条或切割成另一项。
- `game_design_reference`：游戏角色原稿方法案例，归属“画风与视觉表现”下四个原稿类别。构建器汇集到游戏设计专题并生成计数；提示词按实际类别列名。一个词条的对照方案、局部图和阶段图都在同一个visual裁剪内，不另设portrait/fullbody或sequence模式。图例不代表已验证的生产图、PSD或三维资产。

visual 的网格坐标从 0 开始。若存在 crop，使用像素矩形 `x,y,width,height,sheet_width,sheet_height`；矩形不得越界，sheet 尺寸必须与图片一致。没有 crop 时用 column/row/columns/rows 均分。不要混用缩略图显示尺寸与原图坐标。

`source_key` 是内部编辑来源的稳定匹配键，默认由原类别、中文名、英文名组合；改名/迁移时显式 stable_id，编号登记随后更新匹配键。ID 的源类别前缀是历史身份，不要求与当前显示类别吻合。

## 当前评估结论

1. 维护源、图片任务、主题文档分散在历次扩展模块，适合渐进收敛，不宜一次改写所有数据。
2. 此前按类别顺序分配编号，已改为登记表锁定旧身份；协作新增采用独立贡献文件，降低编辑同一个 Python 文件的冲突。
3. 来源链接、图片权利、生成任务是三个不同概念。先增加独立权利清单，未知信息不填成确定值。
4. 图像检查分为几何完整性与语义正确性；自动检查前者，人工复核后者。历史姿态/服装图页里的错位不能仅靠 schema 判断。
5. 完整角色捏造流程不作为本次数据结构前提；同类选项只提示“备选或组合”。

## 兼容原则

保留旧 URL、已发布 ID、外观卡导入格式；新增可选字段不提升主版本。删除/改名字段、改变单位、改变身份规则等不兼容修改需要迁移程序和变更记录。生成数据的版本与网页功能版本可独立说明，不为纯界面改动伪造新增素材数量。

参考来源现以 `source/references.json` 为唯一主记录；历史分组 references 文件只保留溯源，不再覆盖它。新增社区来源合并前检查重复编号。

内容版本与发布日期现在由 `source/content-release.json` 维护；新增类别的显式前缀在 `source/category-extensions.json` 登记，再同步主导航。

程序版本和所用图片资源标签由 `source/app-release.json` 维护，程序版本必须与 `package.json` 一致。`source/resource-packs.json`保存可复用图片/离线读取资源的版本、公开下载地址、字节数和SHA-256。界面或检索程序更新不提升内容版本，也不要求重新上传未变化的大资源包。

在线构建的 `build-info.json` 与 `release-manifest.json.build` 记录程序版、内容版、图片资源版、源码提交及是否有未提交修改。反馈入口仅使用这些公共版本信息和规范词条链接，不附带当前外观卡、搜索历史或本机路径。脱离Git的源码构建将提交记录为null，不借用外层其他仓库的提交。

在线首载索引仅含浏览、检索、筛选、对照和名称型提示词所需字段。完整介绍与维护扩展字段按九个领域拆为带内容哈希的JS，打开详情时加载；同一领域复用已加载数据，失败可重试。`tools/web_delivery.py`维护索引字段契约，新增页面字段时须判断应进入首载索引还是详情分包，并检查对应功能。原始 `data/catalog.json` 和离线双击版保持完整，不把精简索引当作公共编辑数据。

## 许可范围与素材证据

`source/license-policy.json`独立记录代码MIT与项目编辑内容、AI图像、品牌图形的CC BY-NC 4.0非商业许可，包含正文路径、正文校验值、许可范围及所有者决策证据。六张馆藏照片等第三方例外保留原条件。代码MIT不能代替内容授权，商业使用没有预先获准。

`source/rights-review.json`逐文件记录`sha256`、`provenance`、`evidence_ids`与发布状态。`pending-owner-license`和`needs-input-review`都不能作为已放行素材；`cleared`需要非空许可、具体证据，以及与文件哈希和许可都一致的上游依据。`source/rights-evidence.json`提供公共证据，`source/rights-provenance.json`记录当前图页与已声明输入路径。私有生成目录和联网核验缓存不写入公共绝对路径。

来源核验、针对性图像复核和最终对外授权分别记录；不能把哈希对应当成所有输入都无第三方权利问题。当前生成模型未知时保留null，文件修改时间不冒充实际生成时间。检查工具`tools/audit_materials.py`可离线查询审核状态；`tools/validate_atlas.py --release`同时检查代码范围、内容许可和逐项发布状态。

所有者对生成结果的补充说明以`owner-result-clarification`证据单列，不混同为对外许可。撤销过度标记时，在对应资产的`review_decision`保留原状态、修正后状态、理由和证据编号；查询工具显示这些字段供人工追溯，发布验证仍以当前`status`和许可证据为准。

本次所有者非商业授权以`owner-license-decision`登记；每个项目资产另有`owner-asset-license-grant`，包含`asset`路径、`local_sha256`、`license`及`authorization`决策编号。发布验证核对对应关系，不允许将所有者项目授权用于第三方素材，也不因许可已选就跳过图片哈希或逐项证据。历史`review_decision`不覆盖后来有效的许可决策。

个人外观卡的 `selected` 保留加入顺序（早到晚），新加入或移除后重新加入的编号追加到末尾。加入时间倒序显示使用该顺序反向投影；类别排序仅改变显示，不能把排序结果写回 `selected`。系统示例保留其编排顺序。

## 系统示例

维护源是 `source/system-examples.json`。每张角色卡包含稳定 `id`、人物题材 `chapter`、具体人物简介 `description`、配色 `palette`、检索标签 `tags` 和少量 `entry_ids`。所选参考围绕同一个人物与场景；人物之间的差异用于展现库的广度。统计覆盖率仅供维护观察，不作为补齐角色部件的规则。简介与配色不会自动进入AI提示词，另存后保留在个人卡备注中。

`data/combinations.json` 保留历史数字示例和已使用的字符串示例，以 `archived: true` 标记。当前人物角色卡带 `character_example: true`，主列表只展示活跃角色。`meta.combination_count` 统计活跃卡，归档数量单列。新人物分配新ID，链接与提示词历史使用同一ID；旧链接和旧历史继续有效，已另存的个人外观卡保持独立。源文件 `archived_cards` 保留过去的参考合集，不重新分配其ID。

`example_chapters` 用于人物题材筛选，`example_coverage` 及 `data/example-coverage.json` 统计实际涉及的领域、分组与类别，并列出未覆盖类别。覆盖统计由所选词条计算；新增内容后应检查空缺，不把全覆盖作为永久成立的假设。
