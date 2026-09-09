# VRChat衣装制作完全ガイド

## まず15分で制作環境を確認する

Marvelous Designerで衣装を作り、Unityへ取り込み、VRChat内で外観と動作を確認するまでの実行ガイドです。初めての場合は、制作を始める前に必要なソフトウェアとファイルが揃っているか確認してください。

[最初の15分：ソフトウェア確認に進む →](setup/software-check.md){ .md-button .md-button--primary }
[完成までの流れを見る →](#学習の進め方){ .md-button }

!!! info "完成の判定"
    UnityへのimportやBuild成功だけでは完成ではありません。VRChat SDKで状態を確認し、最後にVRChat内で衣装の外観と動作を確認します。

<div class="step-container">
<div class="step-number">このガイドで作るもの</div>

<ul>
<li><strong>最初の成功体験</strong>: 手持ちのアバターと衣装を使ったフィッティング</li>
<li><strong>オリジナル制作</strong>: Tシャツなどの基本衣装</li>
<li><strong>VRChatへの展開</strong>: Unity統合、SDK確認、VRChat内での最終確認</li>
</ul>
</div>

## 学習の進め方

### 推奨学習パス

=== "初心者向け（推奨）"

    **段階1: 基礎準備**

    1. [ソフトウェア確認](setup/software-check.md)
    2. [Marvelous Designer初回起動](setup/md-first-launch.md)
    3. [基本インターフェース理解](basics/md-interface.md)

    **段階2: 初回成功体験**

    4. [アバターの読み込み](workflows/avatar-import.md)
    5. [既存衣装のフィッティング](workflows/garment-fitting.md)

    **段階3: オリジナル制作**

    6. [Tシャツ作成](garments/t-shirt.md)
    7. [物理設定の基本](physics/fabric-properties.md)

    **段階4: VRChat展開**

    8. [Unity統合](unity/project-setup.md)
    9. [VRChatアップロード](unity/avatar-upload.md)
    10. [Performance Rankを測定して確認](unity/fbx-to-vrchat-complete-guide.md)

=== "最短で一度完成させる"

    1. [ソフトウェア確認](setup/software-check.md)
    2. [既存衣装フィッティング](workflows/garment-fitting.md)
    3. [Unity統合](unity/project-setup.md)
    4. [VRChatアップロード](unity/avatar-upload.md)
    5. [Performance RankとVRChat内の外観・動作を確認](unity/fbx-to-vrchat-complete-guide.md)

## 準備するもの

- Marvelous Designer
- Unity Hub
- VRChat Creator Companion
- 制作対象のVRChatアバター
- フィッティングから始める場合は、利用条件を満たした衣装データ

ソフトウェアの対応versionや導入方法は固定値をここで覚えず、[ソフトウェア確認](setup/software-check.md)から現在の確認手順へ進んでください。

## 困ったとき

- [よくある問題](workflows/common-issues.md)
- [有用なリンク集](resources/useful-links.md)
- [VRChat Performance Rankの確認手順](unity/fbx-to-vrchat-complete-guide.md)

---

## 制作を始める

最初は環境確認から進めます。確認が終わったら、上の推奨学習パスに沿って最初のフィッティングまで進んでください。

[最初の15分：ソフトウェア確認に進む →](setup/software-check.md){ .md-button .md-button--primary }
