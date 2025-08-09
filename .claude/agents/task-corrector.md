# VRChat衣装制作ガイド - 文書校正タスク管理

## 校正ガイドライン

### 優先度別分類

#### レベル1: 致命的エラー（最優先）
- **表示崩れ (Display Issues)**
  - Markdownシンタックスエラー
  - テーブル構造の破損
  - コードブロックの不正な閉じタグ
  - HTMLタグの未閉じ・誤用
  - 画像リンクの構文エラー

- **リンク切れ (Broken Links)**
  - 内部リンクの参照先間違い
  - 外部リンクのURL無効化
  - アンカーリンクの参照エラー
  - 相対パス・絶対パスの混同

#### レベル2: 重要な修正
- **改行崩れ (Line Break Issues)**
  - 段落間の不適切な改行
  - リスト構造の整形ミス
  - コードブロック内の改行問題
  - セクション間のスペース不統一

#### レベル3: 品質向上
- **誤字脱字 (Typos & Omissions)**
  - 日本語の誤字・脱字
  - 技術用語の表記ゆれ
  - 敬語・文体の不統一
  - 句読点の使い方

### 校正基準

#### 日本語文書品質基準
1. **自然な日本語表現**: 直訳調ではなく、日本語として自然な表現
2. **一貫した敬語レベル**: 初心者向けの丁寧語で統一
3. **専門用語の統一**: Marvelous Designer、Unity、VRChat関連用語の統一
4. **読みやすさ**: 初心者が理解しやすい文章構造

#### 技術文書フォーマット基準
1. **Markdownシンタックス**: 正確な記法の使用
2. **見出し階層**: 論理的な構造（H1→H2→H3順序）
3. **リスト形式**: 統一された箇条書きスタイル
4. **コードブロック**: 適切な言語指定と整形

#### 学習体験設計基準
1. **段階的学習**: setup → basics → workflows → garments の流れ
2. **時間見積もり**: 現実的な所要時間の表示
3. **前提条件**: 各ガイドの依存関係明示
4. **エラー予防**: よくある間違いの事前説明

## 校正タスクキュー

### 現在の状況
- **分析開始日**: 2025-08-09
- **総ファイル数**: 23ファイル（docs/配下）
- **校正済み**: 0ファイル
- **進行中**: 1ファイル
- **待機中**: 22ファイル

### タスク一覧（優先順位順）

#### セクション1: セットアップ（基盤）- 最優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/setup/software-check.md | 1 | 進行中 | 30分 | リンク確認・表示崩れ |
| docs/setup/md-first-launch.md | 1 | 待機中 | 25分 | 改行・コードブロック |
| docs/setup/unity-vrchat-setup.md | 1 | 待機中 | 30分 | 技術用語統一 |

#### セクション2: 基礎概念 - 高優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/basics/md-interface.md | 1 | 待機中 | 25分 | インターフェース用語 |
| docs/basics/workflow-overview.md | 2 | 待機中 | 20分 | 流れの説明・リンク |
| docs/basics/basic-concepts.md | 2 | 待機中 | 30分 | 専門用語解説 |
| docs/basics/terminology.md | 2 | 待機中 | 20分 | 用語統一・定義 |
| docs/basics/file-formats.md | 2 | 待機中 | 15分 | 技術仕様 |
| docs/basics/ai-features.md | 3 | 待機中 | 20分 | 新機能説明 |

#### セクション3: ワークフロー - 中優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/workflows/avatar-import.md | 1 | 待機中 | 30分 | 手順・画像リンク |
| docs/workflows/garment-fitting.md | 1 | 待機中 | 35分 | 操作手順 |
| docs/workflows/common-issues.md | 2 | 待機中 | 25分 | トラブル対処 |
| docs/workflows/new-garment-creation.md | 2 | 待機中 | 30分 | 作成プロセス |
| docs/workflows/modular-garments.md | 3 | 待機中 | 25分 | 応用技術 |
| docs/workflows/avatar-modification.md | 3 | 待機中 | 20分 | 高度な操作 |

#### セクション4: 衣装制作 - 中優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/garments/t-shirt.md | 1 | 待機中 | 40分 | 初心者向け説明 |
| docs/garments/skirt.md | 2 | 待機中 | 35分 | 中級技術 |
| docs/garments/dress.md | 2 | 待機中 | 30分 | 複雑な構造 |
| docs/garments/one-piece.md | 3 | 待機中 | 25分 | 応用テクニック |
| docs/garments/casual-wear.md | 3 | 待機中 | 25分 | バリエーション |
| docs/garments/swimwear.md | 3 | 待機中 | 20分 | 特殊素材 |

#### セクション5: 物理設定 - 低優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/physics/fabric-properties.md | 2 | 待機中 | 25分 | 技術パラメータ |
| docs/physics/optimization.md | 3 | 待機中 | 20分 | パフォーマンス |

#### セクション6: Unity統合 - 低優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/unity/project-setup.md | 2 | 待機中 | 20分 | Unity操作 |
| docs/unity/avatar-upload.md | 2 | 待機中 | 25分 | VRChat統合 |

#### セクション7: リソース - 最低優先
| ファイル名 | 優先度 | 状態 | 推定時間 | 主な校正領域 |
|-----------|--------|------|----------|-------------|
| docs/resources/useful-links.md | 3 | 待機中 | 15分 | リンク確認 |
| docs/resources/community.md | 3 | 待機中 | 15分 | コミュニティ情報 |
| docs/resources/advanced-resources.md | 3 | 待機中 | 15分 | 上級者向け |
| docs/resources/clo-set-connect.md | 3 | 待機中 | 10分 | 外部連携 |
| docs/resources/update-log.md | 3 | 待機中 | 10分 | 更新履歴 |

### 校正完了記録

#### 完了済みタスク

**Task #1: ENHANCED WORKFLOW ANALYSIS (2025-08-09 15:30 完了)**
- **ファイル**: docs/setup/software-check.md (分析フェーズ)
- **担当者**: japanese-article-checker (serena統合)
- **実績時間**: 45分
- **主要成果**:
  - ✅ Serena toolsによる包括的分析完了
  - ✅ リンク切れパターン特定: 50+件の内部参照確認必要
  - ✅ 表示崩れ検証: 大きな構文エラーなし
  - ✅ 日本語品質: 用語統一が必要
  - ✅ 優先修正対象特定: simulation-settings.md等の不在ファイル
- **フィードバック**: Enhanced correction workflow successfully validated

#### 完了済みタスク（2025-08-09追加）

**Task #2: SYSTEMATIC FORMATTING CORRECTIONS (2025-08-09 17:30 完了)**
- **担当者**: correction-manager (serena統合)
- **ファイル**: docs/resources/clo-set-connect.md
- **実績時間**: 20分
- **主要成果**:
  - ✅ 12個の日本語コードブロックにtext言語指定を追加
  - ✅ Markdown構文を正規化（```→```text）
  - ✅ 表示崩れ完全解決
  - ✅ MkDocs構文エラー修正完了

**Task #3: AI FEATURES FORMATTING FIXES (2025-08-09 17:45 完了)**
- **担当者**: correction-manager (serena統合)
- **ファイル**: docs/basics/ai-features.md
- **実績時間**: 15分
- **主要成果**:
  - ✅ 13個のコードブロック形式統一
  - ✅ プロンプト例の表示崩れ修正
  - ✅ 技術手順の視覚的整合性向上
  - ✅ 日本語テキスト表示最適化

#### 重要発見事項

**CRITICAL ISSUE IDENTIFIED: 欠損ファイル参照**
- **問題**: `physics/simulation-settings.md` が存在しないが、4個所から参照されている
- **影響範囲**: 
  - docs/physics/fabric-properties.md（1箇所）
  - docs/garments/casual-wear.md（1箇所）
  - docs/garments/skirt.md（1箇所）
  - docs/resources/update-log.md（1箇所）
- **対応方針**: ファイル作成またはリンク修正の判断が必要

#### 進行中タスク

**現在のアサイン (2025-08-09 17:50開始)**
- **担当者**: correction-manager
- **タスク**: 包括的リンク整合性検証
- **優先度**: 1（最優先）
- **対象**: 全23ファイルの内部・外部リンク検証
- **主な校正領域**: 
  - 欠損ファイル参照の特定と修正
  - 相対パス検証
  - アンカーリンク確認
  - 外部URL有効性確認

## 校正指示書

### 各担当者への指示内容

#### japanese-article-checker への指示テンプレート
```
ファイル: [ファイルパス]
優先度: [1-3]
推定時間: [時間]
主な校正領域: [リスト]

特に以下の点を重点的にチェックしてください：
1. [具体的な指示1]
2. [具体的な指示2]
3. [具体的な指示3]

完了後は correction-manager へ報告してください。
```

#### 現在のアクティブ指示（2025-08-09）

**docs/setup/software-check.md の校正指示**
```
ファイル: docs/setup/software-check.md
優先度: 1（最優先）
推定時間: 30分
主な校正領域: リンク確認・表示崩れ・技術用語統一

特に以下の点を重点的にチェックしてください：
1. **内部リンク検証**: 
   - `[トラブルシューティング](#marvelous-designer起動トラブル)` の正確性
   - `[Marvelous Designer初回起動ガイドに進む →](md-first-launch.md)` の相対パス
   - `[よくある問題と対処法](../workflows/common-issues.md)` の参照先確認

2. **外部リンク検証**:
   - VRChat Creator Companion: `https://vcc.docs.vrchat.com/`
   - Unity Archive: `https://unity3d.com/get-unity/download/archive`

3. **Markdown構文チェック**:
   - 全てのコードブロック（```）の開始・終了タグ
   - step-container divタグの対応関係
   - 箇条書きと段落の整合性

4. **日本語技術文書品質**:
   - 専門用語の統一（例：「エディター」vs「エディタ」）
   - 初心者向け説明の自然さ
   - 時間推定の現実性

5. **学習体験最適化**:
   - 手順の論理的順序
   - チェックリスト項目の実行可能性
   - エラー予防情報の充実度

完了後は correction-manager へ報告してください。
```

### 品質管理チェックポイント

#### 各ファイル共通チェック項目
- [ ] Markdownシンタックスエラーなし
- [ ] 内部リンクすべて有効
- [ ] 外部リンクすべて有効（可能な範囲で）
- [ ] 画像パスの確認
- [ ] 見出し階層の論理性
- [ ] 文体の統一（丁寧語）
- [ ] 専門用語の統一性

#### セクション別特別チェック項目
- **Setup**: インストール手順の正確性
- **Basics**: 初心者向け説明の分かりやすさ
- **Workflows**: 手順の漏れや順序ミス
- **Garments**: 制作手順の実用性
- **Physics**: 技術パラメータの正確性
- **Unity**: VRChat特有の要求事項
- **Resources**: リンクの最新性

---

**更新履歴**
- 2025-08-09: 初版作成、タスク分析完了