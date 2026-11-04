# Agent 与脚本查询

无需 API key、网络或图像辨识。所有查询都针对已有编辑词条。

```sh
python tools/query_atlas.py --list domains
python tools/query_atlas.py --list categories
python tools/query_atlas.py "缎带" --category hair_with_accessories --limit 10
python tools/query_atlas.py --id AH020 --full
python tools/query_atlas.py "ponytail" --format csv
python tools/query_atlas.py --domain hair_design --limit 100 --offset 100 --format jsonl
```

默认查询 `data/agent-index.jsonl`，返回总数、分页位置、编号、中英文名、所属目录、别名、图片矩形和详情地址。多个词需要同时匹配；不使用语义模型，不声称识别图像。`--full` 才读取完整描述和扩展字段。最大每页 1000 项，默认20项，避免一次将完整目录放进模型上下文。

机器可读文件：`data/manifest.json`（版本、长度、SHA-256）、`schemas/catalog.schema.json`（核心结构）、`data/field-inventory.json`（扩展字段现状）。详情 URL 使用稳定 entry ID；本地文件图片路径均相对图鉴根目录。

协作时先查近义名和英文别名，再提出差异；需要精确图像特征时查询词条描述并由人工复核图片。不要将“检索到名称”当作“图片已正确绘制”。
