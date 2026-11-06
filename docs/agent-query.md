# Agent 与脚本查询

无需 API key、网络或图像辨识。所有查询都针对已有编辑词条。

```sh
python tools/query_atlas.py --list domains
python tools/query_atlas.py --list categories
python tools/query_atlas.py "缎带" --category hair_with_accessories --limit 10
python tools/query_atlas.py --id AH020 --full
python tools/query_atlas.py "ponytail" --format csv
python tools/query_atlas.py --domain hair_design --limit 100 --offset 100 --format jsonl
python tools/query_atlas.py "ポニーテール" --lang ja --limit 10
python tools/query_atlas.py --id AH020 --lang en --full
python tools/query_atlas.py --list categories --lang ja
```

默认查询 `data/agent-index.jsonl`，返回总数、分页位置、编号、中英文名、所属目录、别名、图片矩形和详情地址。多个词需要同时匹配；不使用语义模型，不声称识别图像。`--full` 才读取完整描述和扩展字段。最大每页 1000 项，默认20项，避免一次将完整目录放进模型上下文。

`--lang zh|en|ja` 选择结果的显示语言，默认中文。检索同时匹配三语名称和检索别名，并归一化全角、半角等兼容字符。翻译通过 `source/i18n/` 读取，不修改公共编辑数据。英文或日文输出保留 `source_name`、原目录名和稳定 `category` / `dimension`，使用 `dimension_label` 显示翻译后的细分名；`name_locale`、`description_locale` 与 `translation_fallback` 说明回退情况。详情链接保留原编号并附加 `lang`。

译文缺失或对应原文已变化时，名称优先回退已有英文，再回退中文；简介与设计要点可回退英文翻译，最后显示原文。回退不表示已完成该语言翻译。翻译覆盖、原文哈希校验与增量任务见[多语言维护](localization.md)。

机器可读文件：`data/manifest.json`（版本、长度、SHA-256）、`schemas/catalog.schema.json`（核心结构）、`data/field-inventory.json`（扩展字段现状）。详情 URL 使用稳定 entry ID；本地文件图片路径均相对图鉴根目录。

协作时先查近义名和英文别名，再提出差异；需要精确图像特征时查询词条描述并由人工复核图片。不要将“检索到名称”当作“图片已正确绘制”。
