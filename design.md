# VRChat衣装制作ガイド - 設計ドキュメント

## システム設計概要

### アーキテクチャ
```
GitHub Repository
├── mkdocs.yml (MkDocs設定)
├── docs/ (日本語ドキュメント)
│   ├── index.md (ホーム)
│   ├── setup/ (環境設定)
│   ├── basics/ (基礎知識)
│   ├── workflows/ (作業手順)
│   ├── garments/ (衣装別ガイド)
│   ├── physics/ (物理設定)
│   ├── unity/ (Unity統合)
│   └── resources/ (リソース・参考資料)
└── assets/ (必要に応じて画像等)
```

## ユーザージャーニー設計

### フェーズ1: 準備段階（完全初心者）
1. **環境確認**: ソフトウェアのインストール状況確認
2. **基本概念理解**: VRChat衣装制作の全体像把握
3. **Marvelous Designer起動**: 初回起動と基本界面理解

### フェーズ2: 基礎学習（操作習得）
1. **インターフェース学習**: MD主要ツールの理解
2. **基本操作習得**: パターン作成、アバター読み込み
3. **シンプル衣装練習**: Tシャツなど基本形状での練習

### フェーズ3: 実践制作（衣装作成）
1. **アバター準備**: FBXインポートとセットアップ
2. **既存衣装フィット**: PZIPファイルの活用
3. **新規衣装制作**: 段階的な複雑さの衣装制作

### フェーズ4: 統合・公開（VRChat展開）
1. **物理設定最適化**: 布のダイナミクス調整
2. **Unity統合**: VRChat SDK3でのセットアップ
3. **アップロード**: VRChatへの最終展開

## ドキュメント構造詳細設計

### 1. ホーム (index.md)
**目的**: 初心者の不安を解消し、学習の道筋を示す

**内容構成**:
```markdown
# VRChat衣装制作完全ガイド

## このガイドについて
- 完全初心者向けの説明
- 必要な前提知識（なし）
- 学習にかかる時間の目安

## 学習の進め方
1. [環境設定] → 2. [基礎知識] → 3. [実践制作] → 4. [VRChat統合]

## よくある質問
- Marvelous Designerって何？
- どのくらい時間がかかる？
- 失敗しても大丈夫？
```

### 2. 環境設定 (setup/)
**ファイル構成**:
- `software-check.md`: インストール済みソフト確認
- `md-first-launch.md`: Marvelous Designer初回起動
- `unity-vrchat-setup.md`: Unity + VRChat SDK3確認

### 3. 基礎知識 (basics/)
**ファイル構成**:
- `md-interface.md`: Marvelous Designer画面説明
- `basic-concepts.md`: 3Dモデリング基本概念
- `workflow-overview.md`: 制作工程全体像
- `file-formats.md`: ファイル形式の理解
- `terminology.md`: 専門用語集（日本語）

### 4. 作業手順 (workflows/)
**ファイル構成**:
- `avatar-import.md`: アバターのインポート手順
- `garment-fitting.md`: 既存衣装のフィッティング
- `new-garment-creation.md`: 新規衣装制作の基本手順
- `common-issues.md`: よくある問題と対処法

### 5. 衣装別ガイド (garments/)
**ファイル構成**:
- `t-shirt.md`: Tシャツ（初心者向け）
- `skirt.md`: スカート（フレア・プリーツ）
- `dress.md`: ドレス（シンプル・複雑）
- `casual-wear.md`: カジュアル服
- `one-piece.md`: ワンピース
- `swimwear.md`: 水着（特殊素材）

**各ガイドの統一構造**:
```markdown
# [衣装名]の作り方

## 難易度レベル
## 必要時間目安
## 準備するもの

## ステップ1: パターン設計
## ステップ2: アバターへの配置
## ステップ3: シミュレーション実行
## ステップ4: 調整と最適化
## ステップ5: エクスポート準備

## この衣装特有のポイント
## 次のステップ（より高度な技術）
```

### 6. 物理設定 (physics/)
**ファイル構成**:
- `fabric-properties.md`: 布の物理特性設定
- `simulation-settings.md`: シミュレーション詳細設定
- `collision-detection.md`: 衝突検出の調整
- `optimization.md`: パフォーマンス最適化

### 7. Unity統合 (unity/)
**ファイル構成**:
- `project-setup.md`: Unityプロジェクトセットアップ
- `vrchat-sdk3.md`: VRChat SDK3の設定
- `avatar-upload.md`: アバターアップロード手順
- `testing.md`: VRChat内でのテスト方法

### 8. リソース (resources/)
**ファイル構成**:
- `useful-links.md`: 有用なリンク集
- `community.md`: コミュニティ情報
- `advanced-resources.md`: 上級者向けリソース
- `update-log.md`: ガイドの更新履歴

## MkDocs設定設計

### mkdocs.yml 構成
```yaml
site_name: VRChat衣装制作完全ガイド
site_description: Marvelous DesignerとUnityを使ったVRChat衣装制作の完全初心者向けガイド
site_url: https://username.github.io/vrchat-garment-guide

theme:
  name: material
  language: ja
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - toc.integrate
    - search.highlight
  palette:
    - scheme: default
      primary: pink
      accent: pink

nav:
  - ホーム: index.md
  - 環境設定:
    - ソフトウェア確認: setup/software-check.md
    - MD初回起動: setup/md-first-launch.md
    - Unity設定: setup/unity-vrchat-setup.md
  - 基礎知識:
    - インターフェース: basics/md-interface.md
    - 基本概念: basics/basic-concepts.md
    - 工程全体: basics/workflow-overview.md
    - ファイル形式: basics/file-formats.md
    - 用語集: basics/terminology.md
  - 作業手順:
    - アバター読み込み: workflows/avatar-import.md
    - 衣装フィッティング: workflows/garment-fitting.md
    - 新規衣装制作: workflows/new-garment-creation.md
    - よくある問題: workflows/common-issues.md
  - 衣装別ガイド:
    - Tシャツ: garments/t-shirt.md
    - スカート: garments/skirt.md
    - ドレス: garments/dress.md
    - カジュアル服: garments/casual-wear.md
    - ワンピース: garments/one-piece.md
    - 水着: garments/swimwear.md
  - 物理設定:
    - 布の特性: physics/fabric-properties.md
    - シミュレーション: physics/simulation-settings.md
    - 衝突検出: physics/collision-detection.md
    - 最適化: physics/optimization.md
  - Unity統合:
    - プロジェクト設定: unity/project-setup.md
    - VRChat SDK3: unity/vrchat-sdk3.md
    - アップロード: unity/avatar-upload.md
    - テスト: unity/testing.md
  - リソース:
    - 有用リンク: resources/useful-links.md
    - コミュニティ: resources/community.md
    - 上級リソース: resources/advanced-resources.md
    - 更新履歴: resources/update-log.md

plugins:
  - search
  - git-revision-date-localized:
      type: date
      locale: ja

markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - md_in_html
```

## コンテンツ戦略

### 1. 段階的複雑性
- **レベル1**: Tシャツ（基本形状、単純な操作）
- **レベル2**: スカート（プリーツ、フレア技術）
- **レベル3**: ドレス（複合パーツ、高度なフィッティング）
- **レベル4**: 水着（特殊素材、タイトフィット）

### 2. 反復学習パターン
各衣装で共通の学習パターンを適用:
1. **概念説明** → 2. **実践操作** → 3. **問題解決** → 4. **応用発展**

### 3. エラー対策設計
- **予防的説明**: よくあるミスを事前に警告
- **段階的チェックポイント**: 各段階での確認項目
- **バックトラック手順**: 失敗時の復旧方法

## 技術実装計画

### フェーズ1: 基盤構築
1. MkDocsサイト基本構造作成
2. 必須ページ（ホーム、基礎知識）の作成
3. 最新ソフトウェア情報の調査・反映

### フェーズ2: コア機能実装
1. 基本ワークフロー（Tシャツ）のドキュメント化
2. Marvelous Designer基本操作ガイド作成
3. Unity統合の基本手順作成

### フェーズ3: コンテンツ拡張
1. 各衣装タイプ別ガイドの作成
2. 物理設定の詳細解説
3. トラブルシューティング情報の追加

### フェーズ4: 品質向上
1. ユーザーテストに基づく改善
2. リンク集の充実
3. 継続的な最新情報のアップデート

## 品質保証計画

### 技術的品質
- 各手順の検証テスト実施
- 最新バージョンでの動作確認
- リンク切れの定期チェック

### ユーザビリティ品質  
- 初心者による実際のテスト
- 理解しにくい部分の特定と改善
- ナビゲーションの最適化

### コンテンツ品質
- 日本語表現の自然性確認
- 専門用語の統一性確保
- 段階的学習の効果測定

## 成功指標

### 定量指標
- ドキュメント完読率
- 各セクションでの離脱率
- GitHub上での活用状況

### 定性指標
- 初心者が独力で完成させられる割合
- ユーザーからのフィードバック内容
- コミュニティでの評価

## 将来拡張計画

### 短期追加項目
- よくある質問（FAQ）セクション
- 動画チュートリアルリンク集
- コミュニティ作品ギャラリー

### 中期追加項目
- 高度な技術（テクスチャペイント等）
- 他ソフトウェアとの連携
- パフォーマンス最適化手法

### 長期追加項目
- マルチ言語対応（英語版）
- インタラクティブな学習機能
- AIアシスタント統合

---

*この設計ドキュメントは、VRChat衣装制作ガイドの技術的・構造的設計を定義しており、実装フェーズでの指針となります。*