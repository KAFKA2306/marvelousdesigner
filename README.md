# VRChat衣装制作ガイド

Marvelous Designer、Blender、Unity、VRChat向けの衣装制作工程を段階別に整理したMkDocsプロジェクトです。

- 公開サイト: https://kafka2306.github.io/marvelousdesigner/

## 因果・証拠オントロジー

上位システムは `GarmentProductionLearningSystem` です。

```text
要件
→ パターン設計
→ シミュレーション
→ メッシュ整形
→ スキニング
→ Unity統合
→ ポーズ・性能・実動作検証
→ 教材公開
```

操作手順、構造検査、対象モデルへの適合、外観評価、性能評価、Unity上の確認、実動作確認は別の主張として扱います。インポート成功だけで最終品質を証明したことにはしません。対象ソフトウェア、版、入力、設定、期待結果、検証方法が欠ける記述は `require_test` とします。

- [プロジェクト・オントロジー](ontology/project.yaml)
- [共通因果・証拠オントロジー](https://github.com/KAFKA2306/know/blob/main/ontology/causal-evidence-core.yaml)

## 主な教材

- [Tシャツ](https://kafka2306.github.io/marvelousdesigner/garments/t-shirt/)
- [スカート](https://kafka2306.github.io/marvelousdesigner/garments/skirt/)
- [カジュアルウェア](https://kafka2306.github.io/marvelousdesigner/garments/casual-wear/)
- [ワンピース](https://kafka2306.github.io/marvelousdesigner/garments/one-piece/)
- [ドレス](https://kafka2306.github.io/marvelousdesigner/garments/dress/)
- [布物性](https://kafka2306.github.io/marvelousdesigner/physics/fabric-properties/)
- [最適化](https://kafka2306.github.io/marvelousdesigner/physics/optimization/)
- [Unity統合](https://kafka2306.github.io/marvelousdesigner/unity/project-setup/)

## 記述区分

- `VendorDocumentedFact`: 公式文書に基づく事項
- `ExperimentalObservation`: 特定条件で確認した結果
- `Instruction`: 前提、操作、期待結果、検証方法を持つ手順
- `CalculatedValue`: 計算または測定した値
- `AestheticJudgment`: 人間による外観評価
- `CompatibilityClaim`: 対象環境と証拠を伴う互換性主張

## 教材の受入条件

1. 対象ソフトウェアと版の範囲が明示されている。
2. 入力状態と必要アセットが明示されている。
3. 手順が再現可能である。
4. 成功時の観測可能な結果が定義されている。
5. 失敗条件と確認方法が定義されている。
6. 互換性や品質の主張には、対象成果物と検証証拠がある。
7. MkDocsビルドとリンク検査に合格する。

詳細な要求、反証条件、主張型、証拠、判定規則は `ontology/project.yaml` を正とします。