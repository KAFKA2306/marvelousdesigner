# パフォーマンス分析ツール完全活用法

!!! info "ガイド概要"
    **所要時間**: 30分 - 1時間 | **難易度**: 初心者向け | **重要度**: Very Poor脱却の基盤

    Very Poor脱却のためには、まず**どこに問題があるか**を正確に把握することが重要です。このガイドでは、VRChatアバターのパフォーマンス分析に必要なツールとテクニックを詳しく解説します。

## 🔍 パフォーマンス分析の重要性

### なぜ分析が必要なのか？

!!! warning "闇雲な最適化は逆効果"
    **よくある失敗例**:
    - テクスチャを小さくしすぎて見た目が悪化
    - 重要でない部分のポリゴンを削減して効果なし
    - PhysBoneを削除しすぎて不自然な動き

    **正しいアプローチ**: **データに基づいた戦略的最適化**

### 分析で得られるメリット

!!! success "効果的な最適化への道筋"
    - **最大効果のポイント特定**: どこを改善すれば最も効果的か
    - **無駄な作業回避**: 影響の小さい部分に時間をかけない
    - **品質保持**: 見た目を維持しながら軽量化
    - **目標設定**: 具体的数値目標で確実な改善

## 🛠️ 基本分析ツール

### 1. VRChat SDK Control Panel - 基本中の基本

!!! example "SDK Control Panelでの基本分析"

    **アクセス方法**:
    ```
    Unity上部メニュー → VRChat SDK →
    Show Control Panel → Builder タブ
    ```

    **分析手順**:
    ```
    1. 対象アバター選択
    2. Build & Publish ボタンクリック
    3. Performance Ranking 確認
    4. 各項目の詳細数値確認
    ```

#### Performance Rating詳細解読

!!! info "各評価項目の詳細分析"

    **Overall Performance（総合評価）**:
    ```
    Excellent: 緑色 - 全項目が優秀
    Good: 黄緑色 - 軽微な問題あり
    Medium: 黄色 - 要改善項目あり
    Poor: オレンジ色 - 重要な問題あり
    Very Poor: 赤色 - 緊急改善必要
    ```

    **個別項目分析**:
    ```
    Polygon Count: メッシュの複雑さ
    Bounds: アバターのサイズ（通常問題なし）
    Texture Memory: テクスチャが使用するメモリ量
    Bone Count: ボーンの総数
    Light Count: ライト数（通常0）
    Particle System Count: パーティクル数
    Dynamic Bone Components: DynamicBoneまたはPhysBone数
    Dynamic Bone Colliders: コライダー数
    Dynamic Bone Collider Check Count: 衝突判定数
    Animator Memory: アニメーター使用メモリ
    ```

### 2. Unity Stats Window - リアルタイム監視

!!! example "Unity Statsでの詳細監視"

    **表示方法**:
    ```
    Unity → Window → Analysis →
    Frame Debugger または Stats
    → Game View右上の Stats ボタン
    ```

    **重要な監視項目**:
    ```
    Tris（三角ポリゴン数）: 実際の描画ポリゴン数
    Verts（頂点数）: メッシュの頂点総数
    SetPass Calls: 描画コール数（少ない方が良い）
    Batches: 描画バッチ数
    ```

### 3. Unity Profiler - プロ級分析ツール

!!! tip "Profilerでの高度分析"

    **起動方法**:
    ```
    Unity → Window → Analysis → Profiler
    → Play ボタン → アバター動作確認
    ```

    **分析項目**:
    ```
    CPU Usage: プロセッサ使用率
    Memory: メモリ使用状況
    Rendering: 描画パフォーマンス
    Animation: アニメーション負荷
    Physics: 物理演算負荷
    ```

## 📊 実践的分析ワークフロー

### Step 1: 初期状態の記録

!!! example "現状把握のための記録作業"

    **記録テンプレート**:
    ```
    アバター名: ________________
    分析日時: ________________

    === VRChat SDK Analysis ===
    Overall Performance: ________
    Polygon Count: ________ / 20,000
    Texture Memory: _______ MB / 110 MB
    Bone Count: ________ / 200
    PhysBone Components: ________ / 32

    === Unity Stats ===
    Tris: ________
    Verts: ________
    SetPass Calls: ________
    Batches: ________
    ```

    **スクリーンショット保存**: 改善前後の比較用

### Step 2: 問題項目の優先順位付け

!!! example "改善効果の高い順序で分析"

    **Priority 1: 最大効果項目**
    ```
    1. Polygon Count が Very Poor
       → 最優先でメッシュ最適化

    2. Texture Memory が Very Poor
       → テクスチャ圧縮・サイズ削減

    3. PhysBone Components が Very Poor
       → PhysBone統合・削減
    ```

    **Priority 2: 中程度効果項目**
    ```
    4. Bone Count が Very Poor
       → 不要ボーン削除

    5. SetPass Calls が高い
       → マテリアル統合
    ```

### Step 3: 詳細分析の実行

#### ポリゴン数分析

!!! example "ポリゴン数の内訳分析"

    **メッシュ別ポリゴン数調査**:
    ```
    1. Hierarchy で各メッシュ選択
    2. Inspector → Mesh Filter → Mesh情報確認
    3. 各部位のポリゴン数記録
    ```

    **一般的な分布例**:
    ```
    髪の毛: 8,000-15,000 ポリゴン (35-40%)
    顔: 2,000-4,000 ポリゴン (10-15%)
    体: 3,000-6,000 ポリゴン (15-20%)
    衣装: 5,000-12,000 ポリゴン (25-35%)
    アクセサリー: 1,000-3,000 ポリゴン (5-10%)
    ```

    **削減効果予測**:
    ```
    髪の毛50%削減 → 4,000-7,500ポリゴン削減
    衣装30%削減 → 1,500-3,600ポリゴン削減
    アクセサリー削除 → 1,000-3,000ポリゴン削減
    ```

#### テクスチャメモリ分析

!!! example "テクスチャ使用量の詳細分析"

    **テクスチャサイズ調査**:
    ```
    1. Project View → Filter: Texture2D
    2. 各テクスチャ選択
    3. Inspector → Import Settings確認
    4. Max Size と Compression確認
    ```

    **メモリ使用量計算**:
    ```
    RGBA32 (非圧縮): Width × Height × 4 bytes
    DXT1 (圧縮): Width × Height × 0.5 bytes
    DXT5 (圧縮): Width × Height × 1 bytes

    例: 1024×1024 RGBA32 = 4MB
        1024×1024 DXT5 = 1MB
        512×512 DXT5 = 0.25MB
    ```

    **削減効果予測**:
    ```
    1024→512 サイズ削減: メモリ1/4削減
    非圧縮→DXT5: メモリ1/4削減
    重複テクスチャ統合: 個数分削減
    ```

#### PhysBone分析

!!! example "PhysBone構成の詳細分析"

    **PhysBone棚卸し**:
    ```
    1. Hierarchy → PhysBone検索
    2. 各PhysBoneの設定確認
    3. 影響範囲と必要性評価
    ```

    **分類と優先度**:
    ```
    必須（残す）:
    - 髪の毛メイン: 3-5個
    - スカート/ドレス: 1-2個

    検討（統合可能）:
    - サブ髪パーツ: 統合候補
    - アクセサリー揺れ: 削除候補

    不要（削除）:
    - 装飾品の細かい揺れ
    - 見えない部分のPhysBone
    ```

## 📋 分析結果の活用戦略

### 分析結果からの最適化計画

!!! example "データに基づいた最適化ロードマップ"

    **改善効果シミュレーション**:
    ```
    現状: Very Poor (45,000ポリゴン, 180MB)

    Phase 1: 髪の毛最適化
    → 予想: 30,000ポリゴン (-15,000)

    Phase 2: テクスチャ圧縮
    → 予想: 45MB (-135MB)

    Phase 3: PhysBone統合
    → 予想: 15個PhysBone (-13個)

    最終予想: Good (30,000ポリゴン, 45MB, 15個)
    ```

### 進捗追跡システム

!!! tip "改善進捗の可視化"

    **進捗記録テンプレート**:
    ```
    日付: ________
    作業内容: ________

    改善前: Overall ______
    改善後: Overall ______

    ポリゴン数: _____ → _____
    テクスチャ: _____ → _____
    PhysBone: _____ → _____

    次回作業: ________
    ```

## 🔧 高度分析テクニック

### カスタム分析スクリプト

!!! info "効率的な一括分析"

    **Unity Editor拡張での自動化**:
    ```csharp
    // 簡単な分析情報表示例
    [MenuItem(\"Tools/Avatar Analysis\")]
    static void AnalyzeAvatar()
    {
        GameObject avatar = Selection.activeGameObject;

        // メッシュ情報収集
        MeshRenderer[] renderers = avatar.GetComponentsInChildren<MeshRenderer>();
        int totalTris = 0;

        foreach(MeshRenderer renderer in renderers)
        {
            MeshFilter filter = renderer.GetComponent<MeshFilter>();
            if(filter && filter.sharedMesh)
                totalTris += filter.sharedMesh.triangles.Length / 3;
        }

        Debug.Log($\"Total Triangles: {totalTris}\");
    }
    ```

### 外部分析ツール連携

!!! tip "より詳細な分析のために"

    **VRCAvatar Optimizer統合**:
    ```
    1. GitHub: anatawa12/AvatarOptimizer
    2. Analysis機能での詳細レポート
    3. 最適化前後の自動比較
    ```

    **Blender連携分析**:
    ```
    1. FBXエクスポート
    2. Blenderでメッシュ分析
    3. 詳細なポリゴン分布確認
    4. 最適化シミュレーション
    ```

## ⚠️ 分析時の注意点とトラブルシューティング

### よくある分析ミス

??? question "「数値は良いのにVery Poorのまま」"
    **隠れた問題の発見**:

    **チェック項目**:
    ```
    1. Dynamic Bone Collider Check Count
       → 衝突判定数が異常に高い

    2. Particle System Count
       → 隠れたパーティクルシステム

    3. Light Count
       → アバターに付いているライト

    4. Bounds Size
       → アバターサイズが異常に大きい
    ```

### Unity表示と実際の差異

??? warning "「Unityでは問題ないのにVRChatでVery Poor」"
    **VRChat特有の計算方法**:

    **対処法**:
    ```
    1. VRChat SDK最新版を使用
    2. Unity 2022.3.22f1指定バージョン使用
    3. Build & Test機能でVRChat内テスト
    4. Statistics Windowでの再確認
    ```

## 📊 分析結果のデータベース化

### 改善履歴の記録

!!! example "継続的改善のためのデータ蓄積"

    **改善データベース例**:
    ```
    アバター: Sample Avatar v1.0

    === 2025-01-15 分析結果 ===
    Overall: Very Poor
    Polygon: 45,000 (Very Poor)
    Texture: 180MB (Very Poor)
    PhysBone: 28 (Poor)

    === 改善アクション ===
    1. Mantis LOD Editor 50%削減実行
    2. テクスチャ512×512統一
    3. PhysBone髪部分統合

    === 2025-01-16 結果 ===
    Overall: Good
    Polygon: 22,500 (Good)
    Texture: 35MB (Good)
    PhysBone: 12 (Excellent)

    改善効果: 50%軽量化成功
    ```

## 🎯 分析精度向上のコツ

### 環境統一の重要性

!!! warning "一貫した分析環境の維持"

    **推奨環境設定**:
    ```
    Unity: 2022.3.22f1 (VRChat推奨版)
    VRChat SDK: 最新版 (v3.8.2以降)
    プロジェクト設定: Linear Color Space
    Quality Settings: Ultra
    ```

### 複数条件での検証

!!! tip "様々な状況での分析"

    **分析パターン**:
    ```
    1. 静止状態での分析
    2. アニメーション中の分析
    3. 表情変化時の分析
    4. PhysBone動作時の分析
    ```

## 🌟 次のステップ

### 分析結果を活用した最適化

!!! success "分析完了後の具体的行動"

    **推奨学習順序**:
    1. **[Very Poor脱却実践](very-poor-escape.md)**: 分析結果に基づいた最適化実行
    2. **[モバイル対応最適化](mobile-compatibility.md)**: Quest/Pico向け詳細分析
    3. **[プロ向け分析技術](../advanced/professional-techniques.md)**: より高度な分析手法

### 分析技術の向上

!!! example "継続的スキルアップ"

    **発展学習項目**:
    - カスタム分析ツール開発
    - 自動化スクリプト作成
    - コミュニティでの知見共有
    - 新しい分析手法の研究

---

!!! success "データドリブンな最適化の実現"
    このガイドで習得した分析技術により、**感覚に頼らない科学的なアバター最適化**が可能になります。正確な現状把握から始まる効率的な改善で、確実にVery Poor脱却を達成しましょう。

**関連リンク**:
- [Very Poor脱却実践ガイド](very-poor-escape.md){ .md-button .md-button--primary }
- [モバイル完全対応](mobile-compatibility.md){ .md-button }
- [最新最適化ツール活用](../tools/avatar-optimizer.md){ .md-button }
