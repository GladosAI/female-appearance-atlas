# Contributing

[中文](CONTRIBUTING.md) · **English** · [日本語](CONTRIBUTING.ja.md)

Please search existing entries before adding a new reference. Synonyms normally belong in aliases; create a new entry when its visible structure, way of wearing or expressive purpose differs.

The [contribution form](https://gladosai.github.io/female-appearance-atlas/contribute.html?lang=en) helps find similar entries and prepare a draft JSON plus your original image. It works locally and does not upload or publish anything. Submit those files through an issue or pull request, with authorship, source, permission and known generation details. Unknown model or creation dates should remain unknown.

Translations live in `source/i18n/en.json` and `source/i18n/ja.json`, separate from the canonical catalog. Keep public IDs, category keys, dimension values, image references and personal-card formats unchanged. `messages` uses original Chinese text as keys; `entries` uses permanent entry IDs. A translation's source hash records which original field it matches. Mark drafts honestly; do not label unreviewed text as reviewed.

```sh
python tools/i18n_tools.py --help
python tools/query_atlas.py "ponytail" --lang en
python tools/build_atlas.py --skip-package
python tools/validate_atlas.py
python -m unittest discover -s tests -v
npm run test:browser
```

See [translation maintenance](docs/localization.md) for incremental export/import and coverage checks, and the [full contribution guide](CONTRIBUTING.md) for image/crop and resource-package requirements. Submit changes through a pull request; do not commit original image packs, browser cards, private paths or caches into source history.

Code contributions use MIT. Contributions of content you may license use CC BY-NC 4.0, with third-party exceptions recorded explicitly. Contributors retain their actual rights. A future change allowing commercial use may require separate permission from the affected contributors.
