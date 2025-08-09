# VRChat衣装制作完全ガイド

## ようこそ！あなたもVRChatの素敵な衣装が作れます

**「私にもできるかな...？」** そんな不安を感じていませんか？

大丈夫です。このガイドは**完全に初めての方**のために作られています。プログラミングの知識も、3Dモデリングの経験も必要ありません。一歩ずつ、丁寧に進めていけば、必ずあなたの理想の衣装が完成します。

<div class="step-container">
<div class="step-number">✨ あなたが作れるようになるもの</div>

<ul>
<li><strong>ドレス</strong>: エレガントなフォーマルドレスから可愛いカジュアルワンピースまで</li>
<li><strong>Tシャツ</strong>: シンプルなものから個性的なデザインまで</li>
<li><strong>スカート</strong>: フレアスカート、プリーツスカート、ミニからロングまで</li>
<li><strong>カジュアル服</strong>: 普段着からおしゃれ着まで幅広く</li>
<li><strong>ワンピース</strong>: 一体型の美しいシルエット</li>
<li><strong>水着</strong>: 体にフィットする特殊な衣装</li>
</ul>

<p>そして何より、<strong>VRChat内で美しく動く衣装</strong>を作ることができます！</p>
</div>

## このガイドの特徴

### 🎯 完全初心者向け
- **ゼロから始められる**: 前提知識は一切不要
- **日本語で分かりやすく**: 専門用語も丁寧に説明
- **失敗を恐れない**: 間違えても大丈夫な方法を教えます

### ⏰ 現実的な時間設定
- **初回体験**: 2-3時間（既存の服をあなたのアバターに合わせる）
- **T-シャツ制作**: 4-6時間（基本的なオリジナル衣装）
- **ドレス制作**: 8-12時間（複雑な衣装）

### 🛠 最新ソフトウェア対応
- **Marvelous Designer 2025**: <span class="software-version">最新版対応</span>
- **Unity 2022.3.22f1**: <span class="software-version">VRChat推奨</span>
- **VRChat SDK3**: <span class="software-version">v3.8.2対応</span>

## 学習の進め方

### 📚 推奨学習パス

=== "初心者向け（推奨）"

    **段階1: 基礎準備（1日目）**

    1. [ソフトウェア確認](setup/software-check.md) <span class="time-estimate">15分</span>
    2. [Marvelous Designer初回起動](setup/md-first-launch.md) <span class="time-estimate">30分</span>
    3. [基本インターフェース理解](basics/md-interface.md) <span class="time-estimate">45分</span>

    **段階2: 初回成功体験（2日目）**

    4. [アバターの読み込み](workflows/avatar-import.md) <span class="time-estimate">30分</span>
    5. [既存衣装のフィッティング](workflows/garment-fitting.md) <span class="time-estimate">2時間</span>

    **段階3: オリジナル制作（3-4日目）**

    6. [Tシャツ作成](garments/t-shirt.md) <span class="difficulty-beginner">初心者</span> <span class="time-estimate">4-6時間</span>
    7. [物理設定の基本](physics/fabric-properties.md) <span class="time-estimate">1時間</span>

    **段階4: VRChat展開（5日目）**

    8. [Unity統合](unity/project-setup.md) <span class="time-estimate">1時間</span>
    9. [VRChatアップロード](unity/avatar-upload.md) <span class="time-estimate">1時間</span>

=== "急いでいる方向け"

    **最短ルート（1-2日）**

    1. [ソフトウェア確認](setup/software-check.md) ✅
    2. [既存衣装フィッティング](workflows/garment-fitting.md) ✅
    3. [Unity統合＋アップロード](unity/project-setup.md) ✅

    *まずは既存の服を使って一度完成させてから、オリジナル制作に挑戦しましょう*

## よくある不安と回答

??? question "「私にもできるかな...？」"
    **もちろんできます！** このガイドは完全初心者の方々と一緒に作り上げました。一つずつ確実に進めば、必ず完成させることができます。

??? question "「どのくらい時間がかかる？」"
    **最初の衣装（フィッティング）**: 2-3時間
    **オリジナルTシャツ**: 4-6時間
    **複雑なドレス**: 8-12時間

    慣れてくると、同じ作業が半分の時間でできるようになります。

??? question "「失敗したら怖い...」"
    **失敗は学習の一部です！** このガイドでは「失敗しても大丈夫な方法」と「元に戻す方法」を必ず説明しています。安心して挑戦してください。

??? question "「ソフトウェアが難しそう...」"
    **最初は誰でも難しく感じます。** でも、このガイドでは「最初に覚える必要最小限の機能」から始めて、段階的にスキルアップできるよう設計されています。

??? question "「VRChatで他の人に見られるのが恥ずかしい...」"
    **プライベートワールドでテストできます！** 最初は誰にも見られない環境で練習して、自信がついてから公開すれば大丈夫です。

## 準備するもの

### ✅ 必須ソフトウェア（無料期間あり）
- [Marvelous Designer](https://www.marvelousdesigner.com/) - 衣装制作メインソフト
- [Unity Hub](https://unity.com/download) - VRChat統合用
- [VRChat Creator Companion](https://vcc.docs.vrchat.com/) - SDK管理

### 📁 必要ファイル
- **VRChatアバターのFBXファイル** ← あなたが持っているもの
- **衣装のPZIPファイル** ← あなたが持っているもの

!!! info "ファイルについて"
    FBXファイルとPZIPファイルは、あなたがすでに持っているとのことですので、新しく準備する必要はありません。

### 💻 推奨PC環境
- **OS**: Windows 10/11 (64bit)
- **メモリ**: 16GB以上推奨
- **グラフィック**: DirectX 11対応
- **ストレージ**: 10GB以上の空き容量

## コミュニティとサポート

### 🌟 日本語コミュニティ
- [VRChat衣装制作 Discord](resources/community.md#discord)
- [Marvelous Designer 日本語フォーラム](resources/community.md#forum)
- [YouTube チュートリアル集](resources/useful-links.md#youtube)

### 📚 追加リソース
- [有用なリンク集](resources/useful-links.md)
- [よくある質問FAQ](workflows/common-issues.md)
- [上級者向けリソース](resources/advanced-resources.md)

---

## さあ、始めましょう！

<div class="step-container">
<div class="step-number">🚀 最初の一歩</div>

<p><strong>準備はできましたか？</strong> まずは<a href="setup/software-check/">ソフトウェアの確認</a>から始めて、あなたのVRChat衣装制作の旅をスタートしましょう！</p>

<p><strong>不安や疑問があっても大丈夫。</strong> 一歩ずつ、一緒に進んでいきます。</p>

<p><a href="setup/software-check/" class="md-button md-button--primary">ソフトウェア確認に進む →</a></p>
</div>

---

<div class="progress-checklist">
<h4>📋 学習進捗チェックリスト</h4>

- [ ] ソフトウェア確認完了
- [ ] Marvelous Designer起動成功
- [ ] アバター読み込み成功
- [ ] 既存衣装フィッティング完了
- [ ] 初回Unity統合完了
- [ ] VRChatアップロード成功
- [ ] オリジナルTシャツ完成
- [ ] 物理設定理解
- [ ] より複雑な衣装に挑戦

*チェックボックスの状態は自動的に保存されます*
</div>

!!! tip "学習のコツ"
    **一度に全部理解しようとしないでください。** 一つの段階をクリアしてから次に進む方が、結果的に早く上達できます。焦らず、楽しみながら学習を進めましょう！
