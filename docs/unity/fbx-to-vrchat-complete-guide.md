# FBXからVRChatまでの実行ワークフロー

!!! note "このページの役割"
    Marvelous Designerから出力した衣装をUnityへ取り込み、VRChat SDKで**現在値を測定 → 最悪指標を特定 → 修正 → 再測定**するための短い実行ガイドです。

    Performance Rankの数値は変わり得るため、**VRChat公式を正準**とします。最終確認: 2026-09-07。

[VRChat公式 Performance Ranks を確認 →](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/){ .md-button .md-button--primary }
[VRChat公式 Avatar Optimization Tips →](https://creators.vrchat.com/avatars/avatar-optimizing-tips/){ .md-button }

## まずやること

1. FBXをUnityへimportする。
2. VRChat SDKのBuilderを開き、Avatar Performanceの現在値を確認する。
3. **最も悪いRankになっている指標を1つ選ぶ**。
4. その指標だけを先に修正する。
5. Buildをやり直し、SDK Builderで再測定する。
6. 最後にVRChat内で外観と動作を確認する。

!!! warning "成功判定"
    FBX importやBuild成功だけでは完成ではありません。SDK BuilderでPerformance Rankを再確認し、VRChat内で衣装の外観・動作を確認してから次へ進みます。

## 現行Performance Rankの主要値

### PC

| 指標 | Excellent | Good | Medium | Poor |
| --- | ---: | ---: | ---: | ---: |
| Triangles | 32,000 | 70,000 | 70,000 | 70,000 |
| Texture Memory | 40 MB | 75 MB | 110 MB | 150 MB |
| Skinned Meshes | 1 | 2 | 8 | 16 |
| Basic Meshes | 4 | 8 | 16 | 24 |
| Material Slots | 4 | 8 | 16 | 32 |
| PhysBones Components | 4 | 8 | 16 | 32 |
| PhysBones Affected Transforms | 16 | 64 | 128 | 256 |
| PhysBones Colliders | 4 | 8 | 16 | 32 |
| Contacts | 8 | 16 | 24 | 32 |
| Bones | 75 | 150 | 256 | 400 |

!!! info "PCの目標"
    VRChat公式は **Goodを目標** と案内しています。Trianglesは70,000を超えると、この指標だけでVery Poorになります。表にない指標もRankへ影響するため、SDK Builderと公式表を必ず確認してください。

### Mobile / Quest / Android / iOS

| 指標 | Excellent | Good | Medium | Poor |
| --- | ---: | ---: | ---: | ---: |
| Triangles | 7,500 | 10,000 | 15,000 | 20,000 |
| Texture Memory | 10 MB | 18 MB | 25 MB | 40 MB |
| Skinned Meshes | 1 | 1 | 2 | 2 |
| Basic Meshes | 1 | 1 | 2 | 2 |
| Material Slots | 1 | 1 | 2 | 4 |
| Animators | 1 | 1 | 1 | 2 |
| Bones | 75 | 90 | 150 | 150 |
| PhysBones Components | 0 | 4 | 6 | 8 |
| PhysBones Affected Transforms | 0 | 16 | 32 | 64 |
| PhysBones Colliders | 0 | 4 | 8 | 16 |
| Contacts | 2 | 4 | 8 | 16 |

!!! warning "MobileはPCより厳しい"
    MobileではVery Poorを通常表示できず、Avatar Componentにはハード上限もあります。Lights、Cloths、Physics Colliders、Physics Rigidbodies、Audio Sourcesなど、Mobileでは無効になる項目もあります。PCの合格値をそのままMobileへ流用しないでください。

## 指標別の直し方

### Trianglesが悪い

- 見えない面や不要な衣装パーツを削除する。
- Marvelous Designer側のmesh密度を見直す。
- 形状を壊さない範囲でretopologyする。
- 修正後、SDK BuilderでTrianglesを再測定する。

### Material Slotsが悪い

- 未使用slotを削除する。
- 同じ見た目・同じshader設定のmaterialを統合する。
- texture atlas化できる部分をまとめる。
- 「materialファイル数」ではなく、VRChatが評価する**Material Slots**をSDK Builderで確認する。

### Texture Memoryが悪い

- 大きすぎるtextureを縮小する。
- 不要なalpha channelや重複textureを削除する。
- Unity import設定のcompressionを確認する。
- 単純な解像度目標ではなく、SDK BuilderのTexture Memory実測値で判断する。

### PhysBones / Contactsが悪い

- 不要なcomponentを削除する。
- 影響transformとcolliderの範囲を絞る。
- Mobileではcomponent hard limitも公式表で確認する。

## 衣装制作からの判定ゲート

| 工程 | 入力 | 次へ進める条件 |
| --- | --- | --- |
| Marvelous Designer | 完成したpattern / simulation | 破綻・重大な貫通がなくFBXを書き出せる |
| Unity import | FBX / textures | scale、rig、materialsを意図どおり確認できる |
| VRChat SDK | Unity avatar | Builderで現在のPerformance指標を測定できる |
| Optimization | 最悪指標 | 修正後の再測定で改善を確認できる |
| Runtime | build済みavatar | VRChat内で外観・動作を確認できる |

## PCとMobileを同時に作る場合

1. まずSDK BuilderでPC版を測る。
2. Mobile targetへ切り替え、同じavatarのMobile指標を測る。
3. PCの値をMobileの合格条件として使わない。
4. Mobile非対応shader/componentを除去または置換する。
5. 両方をそれぞれbuildし、実機またはVRChat runtimeで確認する。

## 公式値の扱い

このページの表は作業中の判断を速くするための抜粋です。**完全な項目、例外、hard limit、将来の変更はVRChat公式ページを優先**してください。

- [Avatar Performance Ranking System](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)
- [Avatar Optimization Tips](https://creators.vrchat.com/avatars/avatar-optimizing-tips/)

数値がこの教材と公式で異なる場合は、公式値を採用してください。

## 完了チェック

- [ ] SDK Builderで現在値を確認した
- [ ] 最悪指標を特定した
- [ ] その指標を修正した
- [ ] Build後に同じ指標を再測定した
- [ ] PC / Mobileの対象platformを混同していない
- [ ] VRChat内で衣装の外観と動作を確認した
- [ ] 数値判断時にVRChat公式Performance Ranksを再確認した

次は [アバターアップロード](avatar-upload.md) へ進みます。
