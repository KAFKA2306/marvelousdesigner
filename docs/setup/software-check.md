# ソフトウェア確認ガイド

<span class="time-estimate">所要時間: 約15分</span> <span class="difficulty-beginner">初心者向け</span>

**このページの目的**: VRChat衣装制作に必要なソフトウェアがすべて正しくインストールされているかを確認します。

!!! info "始める前に"
    このガイドでは、Marvelous Designer、Unity、Blenderがすでにインストール済みであることを前提としています。まだインストールしていない場合は、各ソフトウェアの公式サイトからダウンロードしてください。

## 📋 確認チェックリスト

### ✅ Marvelous Designer（最重要）

<div class="step-container">
<div class="step-number">ステップ 1: バージョン確認</div>

1. **Marvelous Designerを起動**してください
2. 起動できない場合は[トラブルシューティング](#marvelous-designer起動トラブル)を確認
3. 上部メニューの **「ヘルプ」** → **「Marvelous Designerについて」** をクリック
4. バージョン情報を確認してください

**推奨バージョン**:

- <span class="software-version">2025.x</span>（最新版）
- <span class="software-version">2024.2</span> 以上（動作確認済み）

!!! warning "古いバージョンをお使いの場合"
    2024.0より古いバージョンでは、このガイドの一部の機能が使用できない可能性があります。可能であれば最新版への更新をお勧めします。
</div>

<div class="step-container">
<div class="step-number">ステップ 2: ライセンス確認</div>

1. Marvelous Designerが正常に動作していることを確認
2. 体験版をご利用の場合は、残り日数を確認
3. **「File」** → **「New Project」** で新規プロジェクトが作成できることを確認

**ライセンス状況**:
- ✅ **正規ライセンス**: 制限なく使用可能
- ⚠️ **体験版**: 30日間の制限あり（学習には十分）
- ❌ **期限切れ**: ライセンス更新が必要
</div>

### ✅ Unity Hub と Unity Editor

<div class="step-container">
<div class="step-number">ステップ 3: Unity Hub確認</div>

1. **Unity Hub**を起動してください
2. 左側メニューから **「インストール」** を選択
3. インストールされているUnityのバージョンを確認

**必要バージョン**:

- <span class="software-version">Unity 2022.3.22f1</span>（**VRChat推奨**）
- または <span class="software-version">Unity 2022.3.x</span> シリーズの最新版

!!! tip "Unity 2022.3.22f1が無い場合"
    1. Unity Hub上部の **「インストール」** をクリック
    2. **「エディターをインストール」** を選択
    3. **「推奨リリース」** から2022.3.22f1を探してインストール
    4. インストール時に **「Android Build Support」** と **「iOS Build Support」** も一緒にインストールすることをお勧めします（VRChat向けの将来的な開発に対応）
</div>

### ✅ VRChat Creator Companion（VCC）

<div class="step-container">
<div class="step-number">ステップ 4: VCC確認</div>

1. **VRChat Creator Companion**を起動してください
   - インストールしていない場合: [VCC公式サイト](https://vcc.docs.vrchat.com/)からダウンロード
2. 画面上部に表示されるバージョン情報を確認
3. **「Settings」** → **「Unity Editors」** でUnity 2022.3.22f1が認識されているか確認

**確認ポイント**:
- ✅ VCCが正常に起動する
- ✅ Unity 2022.3.22f1が認識されている
- ✅ インターネット接続が正常（SDK更新のため）
</div>

### ✅ 補助ソフトウェア

<div class="step-container">
<div class="step-number">ステップ 5: その他の確認</div>

**Blender**:
1. Blenderを起動してバージョン確認
2. <span class="software-version">Blender 3.0</span> 以上推奨
3. 今回のガイドでは直接使用しませんが、高度な編集作業で必要になる場合があります

**テキストエディタ（推奨）**:
- メモ帳やVS Codeなど、設定ファイルを編集できるソフト
</div>

## 📁 ファイルとフォルダの準備

<div class="step-container">
<div class="step-number">ステップ 6: 作業フォルダ作成</div>

1. デスクトップまたはドキュメントフォルダに **「VRChat衣装制作」** フォルダを作成
2. その中に以下のサブフォルダを作成してください:

```
VRChat衣装制作/
├── Avatars/          (FBXファイル保存用)
├── Garments/         (PZIPファイル保存用)
├── UnityProjects/    (Unityプロジェクト用)
├── Exports/          (完成品保存用)
└── References/       (参考画像・資料用)
```
</div>

<div class="step-container">
<div class="step-number">ステップ 7: 手持ちファイルの確認</div>

お手持ちのファイルを確認してください:

**アバターファイル**（.fbx）:
- ✅ ファイルサイズが適切（通常1MB〜50MB程度）
- ✅ 拡張子が「.fbx」であることを確認
- ✅ ファイルが破損していない（ダブルクリックで開けるか確認）

**衣装ファイル**（.pzip）:
- ✅ 拡張子が「.pzip」または「.zip」であることを確認
- ✅ Marvelous Designer用のファイルであることを確認

!!! tip "ファイルの準備"
    手持ちのファイルを作成したフォルダにコピーしておくと、作業がスムーズに進みます。
</div>

## 🔧 トラブルシューティング

### Marvelous Designer起動トラブル

??? question "「Marvelous Designerが起動しない」"
    **考えられる原因と対処法**:

    1. **ライセンスの問題**
       - ライセンスが有効か確認
       - インターネット接続を確認
       - 体験版の期限をチェック

    2. **システム要件不足**
       - Windows 10/11（64bit）が必要
       - メモリ8GB以上推奨（16GB以上が理想的）
       - DirectX 11対応グラフィックカードが必須

    3. **インストールの問題**
       - 管理者権限で実行してみる
       - アンチウイルスソフトの除外設定を確認
       - 再インストールを検討

??? question "「画面が真っ白になる」"
    **対処法**:

    1. グラフィックドライバの更新
    2. 設定ファイルのリセット
    3. 互換性モードでの起動

### Unity関連トラブル

??? question "「Unity 2022.3.22f1が見つからない」"
    **対処法**:

    1. Unity Hub経由で正確なバージョンをインストール
    2. [Unity Archive](https://unity.com/releases/editor/archive)から直接ダウンロード
    3. インストール時は必ず「Visual Studio Community」も一緒にインストール

??? question "「VCCでUnityが認識されない」"
    **対処法**:

    1. VCCを再起動
    2. Unity Hubを管理者権限で実行
    3. Unity Editorを一度起動してからVCCを確認

## ✅ 確認完了チェックリスト

すべて確認できたら、以下にチェックを入れてください:

<div class="progress-checklist">
<h4>ソフトウェア確認完了</h4>

- [ ] Marvelous Designer 2024.2以上が正常に起動する
- [ ] Unity 2022.3.22f1がインストールされている
- [ ] VRChat Creator Companionが正常に動作する
- [ ] 作業用フォルダ構造を作成した
- [ ] FBXファイル（アバター）の状態を確認した
- [ ] PZIPファイル（衣装）の状態を確認した
- [ ] Blenderが正常に動作する（参考確認）
</div>

---

## 🚀 次のステップ

すべての確認が完了したら、次は実際にMarvelous Designerを使い始めましょう！

[Marvelous Designer初回起動ガイドに進む →](md-first-launch.md){ .md-button .md-button--primary }

!!! success "お疲れ様でした！"
    基本的な環境確認が完了しました。何かトラブルがあった場合は、[よくある問題と対処法](../workflows/common-issues.md)も参照してください。
