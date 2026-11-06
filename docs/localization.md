# 中、英、日多语言维护

图鉴使用同一份中文编辑数据和同一批图片。英文、日文作为按编号匹配的翻译层维护，不复制整套目录，不重新分配词条编号，也不翻译用于筛选和旧链接匹配的原始值。

界面语言与AI提示词输出语言分别设置。个人外观卡名称、备注和已经手动编辑的提示词属于用户内容，切换界面语言不能将它们覆盖成翻译文本。图片内部已有的文字、历史生成提示词和专题Markdown不因界面切换自动变成对应语言。

## 翻译文件

维护源为 `source/i18n/en.json` 和 `source/i18n/ja.json`，结构见 `schemas/localization.schema.json`：

```json
{
  "schema": "female-appearance-i18n/v1",
  "locale": "ja",
  "messages": {"发型": "ヘアスタイル"},
  "entries": {"AH020": {"name": "リボン付きヘアゴムのハイツインテール"}},
  "source_hashes": {"AH020": {"name": "原中文字段的SHA-256"}},
  "review": {"AH020": {"name": "draft"}}
}
```

示例中的哈希说明不是有效值；实际值由工具按原字段UTF-8字节生成。`messages` 的键是确切原文，适用于界面标签、目录名和细分名。`entries` 以永久编号为键，支持名称、简介、设计要点及可选检索别名。不要把翻译写回 `source/catalog/` 中的中文主名或永久编号登记表。

`source/i18n/messages.json` 保存当前界面和目录的原文清单，覆盖率以这份清单为依据；没有该清单的旧维护环境才使用两份语言包原文键的并集。含 `{count}`、`{name}` 等占位符的翻译必须保留原占位符，验证会拒绝遗漏、改名或重复。

每个字段分别记录原文哈希，某项简介修改不会让整库名称失效。已有翻译的原文发生变化时，验证会报告 `stale translation`；应复核并更新对应译文和哈希，不能只把旧译文重新标成已审核。

`draft` 表示翻译草案，包括自动翻译初稿；只有明确完成语言和术语复核的字段才记为 `reviewed`。自动导入不会把草案升级为已审核；没有当前原文哈希的字段不能标记为已审核。覆盖率、原文是否过期、是否语言复核是不同指标。

界面文案的复核状态记录在可选的 `message_review` 中，键仍为确切原文。导出、导入会保留状态；覆盖率报告分别显示词条与界面文案的草稿和复核数量。`reviewed` 可来自明确记录的AI语言校订，不代表专业人工翻译；当前批次的方式和范围见语言包 `translation_provenance`，未复核的长篇译文继续保持 `draft`。

## 查看与增量更新

以下命令只读本机JSON，不调用翻译服务，不识图，不需要API密钥：

```sh
python tools/i18n_tools.py check
python tools/i18n_tools.py report
python tools/i18n_tools.py report --locale ja
python tools/i18n_tools.py export --locale ja --output .work/ja-translation-tasks.json
```

默认仅导出缺失、原文变化或尚未建立原文哈希的字段。使用 `--field name` 可以先处理名称；使用 `--all` 导出当前译文供语言复核。任务文件保留编号、字段、原文与原文哈希，维护者填写 `translation`，并按实际情况保留 `draft` 或改为 `reviewed`。

```sh
python tools/i18n_tools.py import .work/ja-translation-tasks.json --locale ja
python tools/i18n_tools.py check
python tools/build_atlas.py --skip-package
```

导入先验证整份任务，拒绝未知编号、重复任务、受保护字段和原文漂移，全部通过后才写入翻译维护源。空白翻译保持缺失；导入不改中文目录、素材来源、图片裁剪或个人外观卡。贡献翻译通过同样的PR和非商业编辑内容许可流程审核。

## 回退与检索

缺少日文名时回退到已有英文名，再回退到中文主名。缺少日文简介或设计要点时可使用已有英文翻译，最后显示原中文。没有译文的回退不会计入“已翻译”或“已审核”。旧图片上的中文标签不会被误报成已经翻译。

三种语言的名称与别名可交叉检索；原编号、中文、已有英文入口继续有效。全角和半角等兼容字符通过NFKC归一化匹配，不以机器推断替代具体术语。中文传统服饰、日式服饰和幻想设定等容易混淆的词，语言复核应结合词条语境，必要时查看图例。

Agent可使用 `python tools/query_atlas.py "ポニーテール" --lang ja`，用 `--full` 读取当前语言的详细说明。结果同时保留 `source_name` 等原文、稳定 `category` / `dimension` 和带语言参数的详情地址。具体用法见 [Agent查询](agent-query.md)。

## 发布检查

```sh
python tools/i18n_tools.py check
python tools/i18n_tools.py report
python tools/validate_atlas.py
python -m unittest discover -s tests -v
npm run test:browser
```

发布说明应引用实际覆盖率与审核状态，不能仅凭语言选择器存在就宣称全部内容已完成专业翻译。浏览器验证需覆盖本地双击、HTTP、旧URL、三语检索、细分筛选、外观卡和提示词历史；检查英文和日文长标签在手机端换行、键盘焦点及错误提示。
