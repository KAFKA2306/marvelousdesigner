# VRChat衣装制作ガイド

**公開サイト:** https://kafka2306.github.io/marvelousdesigner/

Marvelous Designer、Blender、Unity、VRChatを使い、衣装のパターン設計から実動作確認までを段階別に学ぶためのMkDocs教材です。

操作方法だけでなく、各工程で何を入力し、何を確認し、どの状態なら次へ進めるかを明示します。FBXが出力できた、Unityへインポートできたというだけでは完成扱いにしません。

## 制作の流れ

```text
衣装要件を決める
  → 2Dパターンを設計
  → 布シミュレーション
  → メッシュを整理
  → UV・マテリアル・法線を調整
  → リトポロジーとスキニング
  → Unityへ統合
  → ポーズ・貫通・性能を検証
  → VRChat内で実動作確認
  → 教材・成果物を公開
```

## 主な教材

### 衣装別

- [Tシャツ](https://kafka2306.github.io/marvelousdesigner/garments/t-shirt/)
- [スカート](https://kafka2306.github.io/marvelousdesigner/garments/skirt/)
- [カジュアルウェア](https://kafka2306.github.io/marvelousdesigner/garments/casual-wear/)
- [ワンピース](https://kafka2306.github.io/marvelousdesigner/garments/one-piece/)
- [ドレス](https://kafka2306.github.io/marvelousdesigner/garments/dress/)

### 技術別

- [布物性](https://kafka2306.github.io/marvelousdesigner/physics/fabric-properties/)
- [最適化](https://kafka2306.github.io/marvelousdesigner/physics/optimization/)
- [Unityプロジェクト設定](https://kafka2306.github.io/marvelousdesigner/unity/project-setup/)

## この教材で区別する情報

- `VendorDocumentedFact` — ソフトウェア公式資料に記載された仕様
- `ExperimentalObservation` — 特定条件で実際に確認した結果
- `Instruction` — 前提、操作、期待結果、検証方法を持つ手順
- `CalculatedValue` — 計算または測定した値
- `AestheticJudgment` — 人間による外観評価
- `CompatibilityClaim` — 対象環境と証拠を伴う互換性主張

機械可読な定義:

- [プロジェクト・オントロジー](ontology/project.yaml)
- [共通因果・証拠オントロジー](https://github.com/KAFKA2306/know/blob/main/ontology/causal-evidence-core.yaml)

## 教材の受入条件

1. 対象ソフトウェアとバージョンが書かれている
2. 開始時の状態と必要アセットが分かる
3. 手順を別の環境でも再実行できる
4. 成功時に観測できる結果が定義されている
5. 失敗条件と確認方法が書かれている
6. 互換性や品質の主張に対象成果物と検証証拠がある
7. MkDocsビルドとリンク検査を通過する

## ローカル確認

リポジトリ内の設定を正として依存関係を導入し、MkDocsの開発サーバーを起動します。

```bash
git clone https://github.com/KAFKA2306/marvelousdesigner.git
cd marvelousdesigner
pip install -r requirements.txt
mkdocs serve
```

依存関係やコマンドが変更されている場合は、`pyproject.toml`、`requirements.txt`、`Taskfile.yml`のうち実在する設定を優先してください。

## 注意

- ソフトウェアのUIや機能はバージョンによって変わります
- 対象アバターごとに体型、ボーン、シェイプキー、規約が異なります
- インポート成功は外観品質、動作品質、販売品質の証明ではありません
- 購入アセットやアバターデータの再配布は各ライセンスに従ってください

**README最終監査:** 2026-08-01
