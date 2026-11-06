# 貢献ガイド

[中文](CONTRIBUTING.md) · [English](CONTRIBUTING.en.md) · **日本語**

追加前に既存項目を検索してください。通常、同義語は別名に追加します。見た目の構造、着用方法、表現目的に明確な違いがある場合は、新しい項目として提案できます。

[素材の貢献フォーム](https://gladosai.github.io/female-appearance-atlas/contribute.html?lang=ja) では、近い項目を調べ、草稿JSONと元画像を用意できます。処理はローカルで行い、自動アップロードや公開はしません。作者、出典、許諾、分かる範囲の生成記録を添えて、Issueまたはプルリクエストで提出してください。モデルや実際の制作日が不明なら、不明のまま記録します。

翻訳は正規カタログとは別に、`source/i18n/en.json` と `source/i18n/ja.json` に保存します。公開ID、カテゴリキー、細分の値、画像参照、個人カードの形式を変更しないでください。`messages` のキーは中国語の原文、`entries` のキーは永久項目IDです。原文ハッシュで対応する文章の版を確認します。確認していない訳文は草稿として扱ってください。

```sh
python tools/i18n_tools.py --help
python tools/query_atlas.py "ツインテール" --lang ja
python tools/build_atlas.py --skip-package
python tools/validate_atlas.py
python -m unittest discover -s tests -v
npm run test:browser
```

差分のエクスポート・インポートと網羅率の確認は [翻訳の保守手順](docs/localization.md)、画像・切り抜き・配布リソースの条件は [詳細な貢献ガイド](CONTRIBUTING.md) を参照してください。変更はプルリクエストで提出します。元画像パック、ブラウザ内の個人カード、個人用パス、キャッシュはソース履歴にコミットしないでください。

コードの貢献はMITです。許諾できる文章や画像などの素材はCC BY-NC 4.0で受け入れ、第三者素材の例外は明記します。実際に保有する権利は貢献者に残ります。将来、商用利用を許可する変更には、対象の貢献者から別途許諾が必要になる場合があります。
