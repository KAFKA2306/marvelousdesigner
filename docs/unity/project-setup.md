# Unity統合プロジェクト設定ガイド

!!! note "ガイド情報"
    **所要時間**: 約60分 | **難易度**: 初心者向け | **重要度**: 必須（VRChat実用化）

**このページの目的**: Marvelous Designerで制作した衣装をUnityに統合し、VRChatアバターとして使用するための基盤を構築します。

!!! success "このガイドで実現すること"
    - ✅ 制作した衣装をVRChatで実際に着用可能に
    - ✅ Unity + VRChat SDK3での実践的な作業体験
    - ✅ アバター制作の完全なワークフロー理解
    - ✅ 自分だけのカスタムアバターの完成

!!! info "事前準備"
    - [Unity・VRChat SDK設定](../setup/unity-vrchat-setup.md)が完了済み
    - Marvelous Designerで衣装（Tシャツなど）を制作済み
    - 衣装がFBX形式でエクスポート済み
    - VRChatアカウントでログイン可能

## 🎯 統合の全体像

### ワークフロー概要

!!! info "Marvelous Designer → Unity → VRChat の流れ"

    **1. Marvelous Designer段階**（完了済み）
    - アバター読み込み
    - 衣装制作・フィッティング
    - FBX形式エクスポート

    **2. Unity統合段階**（今回実施）
    - プロジェクト設定
    - アバターと衣装の統合
    - VRChat SDK3設定

    **3. VRChat展開段階**（次のステップ）
    - ビルド・テスト
    - アップロード・公開
    - VRChat内での確認

## 🚀 ステップ1: Unity プロジェクト準備

### VCCプロジェクトの確認

!!! example "ステップ 1-1: プロジェクト状況確認"

    **既存プロジェクトの確認**:
    1. **VRChat Creator Companion** を起動
    2. 以前作成したプロジェクト「VRChat衣装制作プロジェクト」を確認
    3. **「Open Project」** をクリックしてUnityで開く

    **新規プロジェクト作成の場合**:
    1. VCCで **「Create New Project」** → **「Avatar」** 選択
    2. プロジェクト名: 「VRChat_Garment_Integration」
    3. 保存場所: 「VRChat衣装制作/UnityProjects/」フォルダ

!!! example "ステップ 1-2: プロジェクト構造の整理"

    **フォルダ構造の作成**:

    Projectウィンドウで以下のフォルダを作成：
    ```
    Assets/
    ├── Avatars/           (元のアバターFBX)
    ├── Garments/          (MD制作衣装FBX)
    ├── Materials/         (マテリアル)
    ├── Textures/          (テクスチャ)
    ├── Scenes/           (作業シーン)
    └── Prefabs/          (完成アバタープレファブ)
    ```

    **フォルダ作成方法**:
    1. Projectウィンドウで右クリック
    2. **「Create」** → **「Folder」**
    3. 各フォルダ名を入力

## 📁 ステップ2: ファイルのインポート

### アバターファイルのインポート

!!! example "ステップ 2-1: 元アバターの読み込み"

    **オリジナルアバター（FBX）のインポート**:
    1. エクスプローラーで元のアバターFBXファイルを選択
    2. Unity の **「Assets/Avatars/」** フォルダにドラッグ&ドロップ
    3. インポート完了まで待機（30秒〜1分程度）

    **インポート設定の確認**:
    1. インポートされたFBXファイルを選択
    2. **Inspector** でインポート設定を確認：
       - **「Rig」** タブ: Animation Type が **「Humanoid」**
       - **「Materials」** タブ: Extract Materials が適切に設定

!!! example "ステップ 2-2: 衣装ファイルのインポート"

    **Marvelous Designer制作衣装のインポート**:
    1. MDでエクスポートした衣装FBXファイルを選択
    2. Unity の **「Assets/Garments/」** フォルダにドラッグ&ドロップ
    3. インポート設定で以下を確認：
       - **Scale Factor**: 1
       - **Convert Units**: チェック
       - **Import Materials**: チェック

!!! warning "ファイルパスの注意"
    日本語やスペースを含むパスは避けてください。エラーの原因となります。

### テクスチャとマテリアルの処理

!!! example "ステップ 2-3: テクスチャの整理"

    **テクスチャファイルの確認**:
    1. インポートした際に自動生成された **「Materials」** と **「Textures」** を確認
    2. 自動生成されたファイルを適切なフォルダに移動
    3. 不要なテクスチャは削除して整理

    **マテリアル設定の基本調整**:
    1. **「Assets/Materials/」** 内のマテリアルファイルを選択
    2. Inspector で以下を確認・調整：
       - **Shader**: Standard または VRChat対応シェーダー
       - **Albedo**: 基本色の設定
       - **Rendering Mode**: Opaque（不透明）が基本

## 🎭 ステップ3: シーンでの統合作業

### シーンの準備

!!! example "ステップ 3-1: 作業シーンの設定"

    **新規シーンの作成**:
    1. **「File」** → **「New Scene」** → **「Basic (Built-in)」**
    2. **「File」** → **「Save As」** で「AvatarSetup」として保存
    3. 保存場所: **「Assets/Scenes/」**

    **シーン内のセットアップ**:
    1. 不要なデフォルトオブジェクトを削除（Main Camera以外）
    2. **Main Camera** の位置を調整（アバターが見やすい位置）
    3. **「Window」** → **「Lighting」** → **「Settings」** でライティング調整

### アバターの配置と統合

!!! example "ステップ 3-2: アバターの配置"

    **元アバターの配置**:
    1. **「Assets/Avatars/」** からアバターFBXをシーンにドラッグ&ドロップ
    2. Transformで位置を原点（0, 0, 0）に設定
    3. アバターが正しく表示されることを確認

    **衣装の配置**:
    1. **「Assets/Garments/」** から衣装FBXをシーンにドラッグ&ドロップ
    2. アバターと同じ位置（0, 0, 0）に配置
    3. 衣装がアバターに重なるように表示されることを確認

!!! example "ステップ 3-3: オブジェクト階層の構築"

    **適切な親子関係の設定**:
    1. **Hierarchy** でアバターのルートオブジェクトを選択
    2. 衣装オブジェクトをアバターの子オブジェクトとして配置：
       - 衣装をドラッグしてアバターの下にドロップ
    3. 階層構造例：
    ```
    Avatar_Root
    ├── Armature (ボーン構造)
    ├── Body (元の体メッシュ)
    └── Tshirt (追加した衣装)
        ├── Mesh
        └── Materials
    ```

## ⚙️ ステップ4: VRChat SDK3 設定

### Avatar Descriptorの設定

!!! example "ステップ 4-1: VRChat Avatar Descriptorの追加"

    **Avatar Descriptorコンポーネントの追加**:
    1. Hierarchyでアバターのルートオブジェクトを選択
    2. **Inspector** で **「Add Component」** をクリック
    3. **「VRC Avatar Descriptor」** を検索して追加

    **基本設定の入力**:
    1. **View Position** の設定：
       - アバターの目の位置にViewボール（緑の球）を移動
       - X: 0, Y: 1.6〜1.8, Z: 0 程度が一般的
    2. **Lip Sync** の設定：
       - **「Jaw Bone」** を設定（通常は頭のボーン）

!!! example "ステップ 4-2: アバターレイヤーの設定"

    **Playable Layersの基本設定**:
    1. **「VRChat SDK」** → **「Show Control Panel」**
    2. Control Panelで **「Builder」** タブを選択
    3. 基本的にはデフォルト設定のままで OK

    **Expression ParametersとMenu（オプション）**:
    - 衣装の切り替え機能が不要な場合はデフォルトのまま
    - 高度な機能は後で学習する項目

### ボーン構造の統合とリギング

!!! example "ステップ 4-3: 衣装とアバターのボーン統合"

    **ボーンウェイトの確認**:
    1. 衣装オブジェクトを選択
    2. **Inspector** で **「Skinned Mesh Renderer」** コンポーネント確認
    3. **Root Bone** がアバターのルートボーンを参照していることを確認

    **手動でのボーン参照設定**（必要に応じて）:
    1. 衣装の **「Skinned Mesh Renderer」** を選択
    2. **「Root Bone」** にアバターのRootボーンを設定
    3. **「Bones」** 配列が正しく設定されていることを確認

!!! info "Marvelous Designer 2025のリギング機能"
    **Avatar Riggerによる自動ウェイト設定**:
    - MD2025では **「Avatar Rigger」** 機能により体のボーンウェイトが衣装に自動コピー
    - **「EveryWear Toolkit」** で自動リトポロジーとリギングを実行
    - Unityは最大8ジョイントまでサポート、MDで影響ジョイント数を指定可能

    **IKジョイントマッピング**:
    - Daz 3D、Mixamo、Character Creator、MetaHumansに対応
    - 肩、肘、手首、骨盤、膝、足首などの主要関節を自動認識
    - より自然で滑らかな動作を実現

!!! warning "ウェイト転送時の注意点"
    - 脇の下や股間部分で不適切なボーンにマッピングされる場合がある
    - アバターが標準Aポーズでない場合は特に注意が必要
    - 必要に応じて事前にタイトフィットバージョンで作業後、最終版に置き換える

## 🧪 ステップ5: テストと品質確認

### Scene View でのテスト

!!! example "ステップ 5-1: Unity内でのテスト"

    **見た目の確認**:
    1. **Scene View** でアバターを色々な角度から確認
    2. 衣装が正しくアバターにフィットしているか確認
    3. 不自然な貫通や浮きがないかチェック

    **Animation Controllerでの動作テスト**（オプション）:
    1. **「Window」** → **「Animation」** → **「Animator」**
    2. 基本的な動作でアバターが正常に動くか確認

### VRChat SDK Build & Test

!!! example "ステップ 5-2: SDK内蔵テスト機能の使用"

    **Build & Test の実行**:
    1. VRChat SDK Control Panel の **「Builder」** タブ
    2. **「Build & Test」** をクリック
    3. ビルドプロセスが開始されます

    **エラー確認と対処**:
    - エラーが表示された場合は内容を確認
    - よくあるエラー：ポリゴン数過多、マテリアル設定
    - **Console Window** で詳細エラーを確認

!!! success "テスト成功の確認"
    VRChatが起動し、ローカルテストワールドで衣装を着用したアバターが表示されれば成功です。

## 🎨 ステップ6: 最終調整と最適化

### 見た目の微調整

!!! example "ステップ 6-1: マテリアルとテクスチャの調整"

    **色と質感の調整**:
    1. **「Assets/Materials/」** 内のマテリアルを選択
    2. **Inspector** で以下を調整：
       - **Albedo Color**: 基本色の微調整
       - **Metallic**: 金属感（通常は0）
       - **Smoothness**: 表面の滑らかさ
       - **Normal Map**: 凹凸感（高度な設定）

    **VRChat最適化**:
    1. 不要な高解像度テクスチャを削除
    2. マテリアル数を最小限に抑制
    3. VRChat推奨シェーダーの使用を検討

### パフォーマンス最適化

!!! example "ステップ 6-2: VRChat性能評価"

    **Performance評価の確認**:
    1. VRChat SDK Control Panel でアバターを選択
    2. **「Performance」** 情報を確認：
       - **Triangle Count**: 20,000未満（PC）、7,500未満（Quest）
       - **Material Count**: 最小限に
       - **Mesh Count**: 統合可能であれば統合

    **最適化の実施**:
    - 必要に応じてポリゴン数削減
    - テクスチャサイズの調整
    - 不要なボーンの削除

## 💾 ステップ7: プレファブ化と保存

### 完成アバターのプレファブ作成

!!! example "ステップ 7-1: プレファブとして保存"

    **プレファブの作成**:
    1. Hierarchyでアバター全体を選択
    2. **「Assets/Prefabs/」** フォルダにドラッグ&ドロップ
    3. プレファブ名: 「MyAvatar_withGarments」など分かりやすい名前

    **バージョン管理**:
    1. 異なるバリエーションごとに別プレファブを作成
    2. 命名規則例：
       - `MyAvatar_Tshirt_v1`
       - `MyAvatar_Casual_v1`
       - `MyAvatar_Formal_v1`

### プロジェクトファイルの保存

!!! example "ステップ 7-2: Unity プロジェクトの保存"

    **シーンとプロジェクトの保存**:
    1. **「File」** → **「Save Scene」** で現在の作業を保存
    2. **「File」** → **「Save Project」** でプロジェクト全体を保存
    3. 定期的なバックアップを推奨

## ✅ 統合完了チェック

!!! note "Unity統合完了チェックリスト"

    **ファイル統合**:
    - [ ] 元アバターFBXが正常にインポート済み
    - [ ] 衣装FBXが正常にインポート済み
    - [ ] テクスチャとマテリアルが適切に設定済み
    - [ ] フォルダ構造が整理されている

    **Unity設定**:
    - [ ] アバターと衣装がシーン内で正しく表示
    - [ ] VRChat Avatar Descriptorが設定済み
    - [ ] View Positionが適切に設定済み
    - [ ] ボーン構造が正しく統合されている

    **品質確認**:
    - [ ] Build & Test でエラーがない
    - [ ] VRChat Performance評価が適切な範囲
    - [ ] 衣装のフィット感が良好
    - [ ] プレファブとして保存済み

## 🔧 トラブルシューティング

### よくある統合問題

??? question "「衣装が表示されない」"
    **対処法**:

    1. **マテリアル設定の確認**:
       - マテリアルが「Missing」になっていないか
       - Shader が適切に設定されているか

    2. **スケール問題**:
       - アバターと衣装のスケールが一致しているか
       - Transform のScale値を確認

    3. **インポート設定**:
       - FBXインポート時の設定を再確認
       - 必要に応じて再インポート

??? question "「衣装がアバターと一緒に動かない」"
    **対処法**:

    1. **ボーン設定の確認**:
       - Skinned Mesh Renderer のRoot Boneが正しく設定されているか
       - Bones配列がアバターのボーン構造を参照しているか

    2. **親子関係の確認**:
       - 衣装オブジェクトがアバターの子オブジェクトになっているか
       - 階層構造が適切か

??? question "「Build & Test でエラーが出る」"
    **対処法**:

    1. **Console確認**:
       - Window → General → Console でエラー詳細を確認
       - エラーメッセージに従って対処

    2. **VRChat SDK更新**:
       - VCCでSDKが最新版か確認
       - 必要に応じて更新

    3. **アバター設定確認**:
       - Avatar Descriptor の設定を再確認
       - 必須項目が全て設定されているか

## 🌟 次のステップ

Unity統合が完了しました！

制作した衣装がUnity内で正しく表示され、VRChat SDK3の設定も完了しています。

**次の重要なステップ**:

[VRChatアップロードとテスト →](avatar-upload.md){ .md-button .md-button--primary }

または、品質をさらに向上させたい場合：

[衣装物理学・ダイナミクス設定 →](../physics/fabric-properties.md){ .md-button }

## 📚 学習成果の確認

### このガイドで習得したスキル

**🔄 統合ワークフロー**
- Marvelous Designer → Unity の連携理解
- FBXファイルの適切な扱い方
- Unity プロジェクト構造の管理

**⚙️ 技術スキル**
- VRChat SDK3 の基本設定
- Avatar Descriptor の設定方法
- ボーン構造とSkinned Mesh の理解

**🎨 品質管理**
- マテリアルとテクスチャの最適化
- VRChat Performance基準の理解
- プレファブ管理とバージョン管理

**🧪 テストスキル**
- Unity Scene View でのテスト手法
- VRChat SDK Build & Test の活用
- エラー対処とデバッグ方法

!!! success "Unity統合完了！"
    素晴らしい成果です！あなたが制作した衣装が、今やVRChatで使用できる実用的なアバターとなりました。次はいよいよVRChatでの実際の動作確認とアップロードです！

## 💡 応用と発展

### 統合技術の応用

**複数衣装の管理**:
- 異なる衣装パターンのプレファブ作成
- 衣装切り替え機能の実装（上級）
- レイヤード（重ね着）システム

**品質向上のテクニック**:
- LOD（Level of Detail）の設定
- アニメーションオーバーライド
- カスタムシェーダーの適用

これらの高度な技術は、基本をマスターしてからの挑戦項目です！
