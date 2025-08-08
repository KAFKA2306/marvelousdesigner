# Unity・VRChat SDK設定ガイド

<span class="time-estimate">所要時間: 約45分</span> <span class="difficulty-beginner">初心者向け</span>

**このページの目的**: UnityとVRChat SDK3を正しく設定し、アバター制作・アップロードの準備を完了します。

!!! info "事前準備"
    - [ソフトウェア確認ガイド](software-check.md)が完了していること
    - Unity Hub、Unity 2022.3.22f1、VRChat Creator Companionがインストール済みであること
    - VRChatアカウントを持っていること

## 🎯 今回達成する目標

1. ✅ VRChat Creator Companionを正しく設定する
2. ✅ Unity 2022.3.22f1でVRChatプロジェクトを作成する
3. ✅ VRChat SDK3をインストールする
4. ✅ アバター開発環境を準備する
5. ✅ テスト用のシンプルなアバターをアップロードする

## 🚀 設定手順

### ステップ 1: VRChat Creator Companion (VCC) セットアップ

<div class="step-container">
<div class="step-number">VCCの初期設定</div>

**VCCを起動して初期設定を行います**:

1. **VRChat Creator Companion**を起動
2. 初回起動時に表示される案内に従って進む
3. VRChatアカウントでログインする

**Unity Editorの設定**:
1. **「Settings」** タブをクリック
2. **「Unity Editors」** セクションを確認
3. **Unity 2022.3.22f1** が表示されていることを確認

!!! tip "Unity Editorが認識されない場合"
    1. **「Add Unity Install」** をクリック
    2. Unity 2022.3.22f1のインストール場所を手動で指定
    3. 通常は `C:\Program Files\Unity\Hub\Editor\2022.3.22f1\Editor\Unity.exe`
</div>

<div class="step-container">
<div class="step-number">新規VRChatプロジェクトの作成</div>

**アバター制作用プロジェクトを作成します**:

1. VCCのメイン画面で **「Create New Project」** をクリック
2. **「Avatar」** プロジェクトタイプを選択
3. プロジェクト情報を入力:
   - **Project Name**: `VRChat衣装制作プロジェクト`
   - **Location**: 作成した「VRChat衣装制作/UnityProjects/」フォルダ内
4. **「Create Project」** をクリック

**自動的に行われる処理**:
- Unity Editorが起動します
- VRChat SDK3が自動的にインストールされます
- 必要なパッケージが設定されます

!!! success "プロジェクト作成完了"
    Unity Editorが起動し、VRChatのロゴが表示されたらプロジェクト作成完了です。
</div>

### ステップ 2: Unity Editorの確認と設定

<div class="step-container">
<div class="step-number">Unity Editorの初期確認</div>

**Unity Editorが正常に動作しているか確認します**:

**画面構成の確認**:
- **Scene View** (3D作業画面)
- **Game View** (実行時プレビュー)  
- **Hierarchy** (オブジェクト一覧)
- **Project** (アセット管理)
- **Inspector** (プロパティ設定)

**VRChat SDK3の確認**:
1. 上部メニューバーに **「VRChat SDK」** メニューが表示されているか確認
2. **「VRChat SDK」** → **「Show Control Panel」** をクリック
3. VRChat SDK Control Panelが開くことを確認

!!! warning "VRChat SDKメニューが表示されない場合"
    1. **「Window」** → **「Package Manager」** を開く
    2. **「In Project」** を選択して「VRChat SDK - Avatars」が表示されているか確認
    3. 表示されていない場合は、VCCから再度プロジェクトを作成
</div>

<div class="step-container">
<div class="step-number">Unity Editorの基本設定</div>

**開発しやすい環境に調整します**:

**Layout設定**:
1. 右上の **「Layout」** ドロップダウンから **「2 by 3」** を選択
2. または自分の好みに合わせて調整

**Auto Saveの有効化**:
1. **「Edit」** → **「Preferences」** → **「General」**
2. **「Auto Refresh」** を有効にする

**日本語化（オプション）**:
- Unity 2022では日本語化パッケージが利用可能
- **「Window」** → **「Package Manager」** → **「Unity Registry」** → **「Localization Package」**
</div>

### ステップ 3: VRChat SDK3の詳細設定

<div class="step-container">
<div class="step-number">VRChat Control Panelの設定</div>

**VRChat SDK Control Panelを開いて設定します**:

1. **「VRChat SDK」** → **「Show Control Panel」**
2. **「Authentication」** タブでVRChatアカウントにログイン

**アバター設定の確認**:
1. **「Builder」** タブを選択
2. **「Build & Publish for Windows」** セクションが表示されることを確認

**設定項目**:
- **Publish to VRChat**: VRChatにアップロードする場合に使用
- **Build Only**: テスト用ビルドのみ
- **Test Avatar**: ローカルテスト用

!!! info "Trust Rank について"
    VRChatにアバターをアップロードするには「New User」以上のTrust Rankが必要です。
</div>

### ステップ 4: テスト用アバターでの動作確認

<div class="step-container">
<div class="step-number">シンプルなテストアバターの作成</div>

**基本的なアバターでVRChat統合をテストします**:

**デフォルトアバターの使用**:
1. ProjectウィンドウでVRChat SDK samplesを確認
2. **「VRChat SDK」** → **「Samples」** → **「Avatar Dynamics Robot Avatar」**
3. シーンにロボットアバターをドラッグ&ドロップ

**VRChat Avatar Descriptorの確認**:
1. Hierarchyでアバターを選択
2. InspectorでVRChat Avatar Descriptorコンポーネントを確認
3. **View Position**（視点位置）が設定されていることを確認

!!! tip "カスタムアバターを使用したい場合"
    お持ちのFBXファイルも同様にドラッグ&ドロップで追加できますが、最初はテスト用アバターで動作確認することをお勧めします。
</div>

<div class="step-container">
<div class="step-number">Build & Testでローカルテスト</div>

**作成したアバターをローカルでテストします**:

1. VRChat SDK Control Panelの **「Builder」** タブを開く
2. **「Build & Test」** をクリック
3. ビルド処理が開始されます

**ビルド完了後**:
1. VRChatが自動的に起動します（インストールされている場合）
2. ローカルテスト用のワールドが開きます
3. 作成したアバターが使用可能になります

!!! success "テスト成功！"
    VRChatでアバターを確認できれば、基本的な統合環境の構築完了です。
</div>

### ステップ 5: プロジェクト構造の理解

<div class="step-container">
<div class="step-number">フォルダ構造の整理</div>

**効率的な作業のために、プロジェクト構造を理解しましょう**:

**推奨フォルダ構造**:
```
Assets/
├── Avatars/           (アバターファイル)
├── Materials/         (マテリアル)  
├── Textures/          (テクスチャ)
├── Garments/          (Marvelous Designerからの衣装)
├── Prefabs/           (プレファブ)
└── Scenes/            (シーン)
    └── AvatarSetup.unity
```

**フォルダを作成する方法**:
1. Projectウィンドウで右クリック
2. **「Create」** → **「Folder」**
3. 上記の名前でフォルダを作成

!!! tip "プロジェクト管理のコツ"
    ファイルが増えてくると管理が大変になります。最初からフォルダ分けを心がけましょう。
</div>

## 🔧 トラブルシューティング

### VCC関連トラブル

??? question "「VCCでプロジェクトが作成できない」"
    **対処法**:
    
    1. **権限の問題**:
       - VCCを管理者権限で実行
       - ウイルス対策ソフトの除外設定を確認
    
    2. **パスの問題**:
       - 日本語が含まれないパスを使用
       - パスが長すぎないか確認
    
    3. **ネットワークの問題**:
       - インターネット接続を確認
       - ファイアウォール設定を確認

??? question "「Unity Editorが認識されない」"
    **対処法**:
    
    1. Unity Hubから正確なバージョン（2022.3.22f1）をインストール
    2. VCCの Settings → Unity Editors で手動追加
    3. 複数のUnityバージョンがインストールされている場合は整理

### Unity関連トラブル

??? question "「VRChat SDKメニューが表示されない」"
    **対処法**:
    
    1. **Package Managerの確認**:
       - Window → Package Manager
       - In Project で VRChat SDK - Avatars が表示されているか確認
    
    2. **再インポート**:
       - Assets → Reimport All
       - しばらく時間がかかりますが完了を待つ
    
    3. **プロジェクトの再作成**:
       - VCCから新しいプロジェクトを作成し直す

??? question "「ビルドが失敗する」"
    **対処法**:
    
    1. **コンソールエラーの確認**:
       - Window → General → Console でエラーメッセージを確認
    
    2. **よくあるエラーと対処**:
       - Missing script: 破損したコンポーネントを削除
       - Path too long: より短いパスに移動
       - Shader error: 使用しているシェーダーを確認

## ✅ 完了チェックリスト

全て完了したら、Unity・VRChat統合環境の準備完了です:

<div class="progress-checklist">
<h4>Unity・VRChat SDK設定完了</h4>

- [ ] VRChat Creator Companionが正常に動作する
- [ ] Unity 2022.3.22f1でVRChatプロジェクトを作成できた
- [ ] VRChat SDK3が正しくインストールされている
- [ ] VRChat SDK Control Panelが開ける
- [ ] VRChatアカウントでログインできた
- [ ] テスト用アバターでBuild & Testが成功した
- [ ] プロジェクトフォルダ構造を理解した
- [ ] VRChatでローカルテストができた
</div>

## 🌟 次のステップ

Unity・VRChat統合環境の準備ができました！

次は実際にMarvelous Designerで衣装制作を始めましょう:

[Marvelous Designer基本インターフェースを学ぶ →](../basics/md-interface.md){ .md-button .md-button--primary }

または、すぐに実践に移りたい場合は:

[アバター読み込みガイドに進む →](../workflows/avatar-import.md){ .md-button }

## 📚 参考情報

### VRChat開発に役立つリソース

- **VRChat Creator Docs**: [https://creators.vrchat.com/](https://creators.vrchat.com/)
- **VRChat SDK Release Notes**: [https://creators.vrchat.com/releases/](https://creators.vrchat.com/releases/)
- **Unity Learn**: [https://learn.unity.com/](https://learn.unity.com/)

### コミュニティ

- **VRChat 日本語コミュニティ**: [Discord招待リンク](../resources/community.md#discord)
- **Unity 日本語フォーラム**: [Unity Forum Japan](https://forum.unity.com/)

!!! success "環境構築完了！"
    お疲れ様でした！これでVRChat衣装制作に必要な全ての基本環境が整いました。次はいよいよ実際の衣装制作に入ります！