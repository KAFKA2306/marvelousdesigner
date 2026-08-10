# Instructor Cohort Pack

既存の無料教材を、講師が4回授業で運用するための**授業設計・提出・採点パック**です。公開教材そのものは無料のままです。有償PoCの対象は、教材利用権そのものではなく、コホート設定、講師向けレビュー、運営支援を含む検証サービスです。

## 無料公開教材とInstructor Packの境界

| 無料公開 | Instructor Cohort Pack |
| --- | --- |
| 衣装制作の手順・技術解説 | 4回のlesson plan |
| Tシャツ・スカート等の制作ガイド | 学生提出テンプレート |
| 布物性・Unity統合等の技術資料 | 講師採点rubric・failure review |
| 自習向け | 1講師 / 1コホート向け運営 |

Instructor Packは、購入アバター、購入衣装、商用asset、学生成果物の再配布権を含みません。各参加者は利用するassetのライセンスを自分で満たす必要があります。

## 4回構成

1. **Pattern & Evidence** — Tシャツを題材に、パターンと検証記録を作る
2. **Simulation & Fit** — スカートを題材に、simulation結果とfit failureを分離する
3. **Mesh & Unity Handoff** — mesh整理からUnity importまでを検証する
4. **VRChat Runtime Review** — pose / clipping / runtime確認を行い、最終提出を監査する

詳細は[4回lesson plan](lessons.md)、提出は[submission template](submission-template.md)、採点は[rubric](rubric.md)を使います。

## 対象software baseline

このpackのversioned baselineは `cohort-manifest.yaml` を正とします。UnityについてはVRChat公式のCurrent Unity Versionページで **2022.3.22f1** が現在の対応versionとして公開されています。授業開始前にmanifestのsource URLを再確認し、異なる場合は授業を開始せずmanifestを改訂します。

- Marvelous Designer: repository教材のbaseline `2024.2+ / 2025.x`。実際の受講環境のexact versionを開始前に記録する
- Blender: repository教材のbaseline `3.0+`。実際のexact versionを開始前に記録する
- Unity: `2022.3.22f1`
- VRChat SDK: Creator Companionで当該Unity版に対応するinstalled versionを開始前に記録する

## 30分teacher preview

[teacher preview](demo.md)は第1回の短縮版です。デモで確認するのは「学生に何を作らせるか」ではなく、講師が**何を証拠として採点するか**です。

## 評価境界

rubricはREADME / ontologyの区分を維持します。

- `VendorDocumentedFact`: 公式sourceとversion/dateが必要
- `ExperimentalObservation`: 入力・procedure・environment・observed resultが必要
- `Instruction`: prerequisite・step・expected result・verificationが必要
- `CalculatedValue`: 計算または測定の根拠を残す
- `AestheticJudgment`: 人間の外観判断として扱い、互換性の証拠にしない
- `CompatibilityClaim`: target environmentとruntime evidenceが必要

Import成功だけでfit・visual quality・runtime compatibilityを合格にしません。

## PoC記録

実施前の販売・導入実績は0として扱います。実コホートを開始した場合だけ `metrics/instructor-cohort-kpi.json` に、受講人数、提出率、完走状況、講師継続意向と証拠URLを追記します。

## 問い合わせ

PoC相談はGitHub Issueで受け付けます。

[Instructor Cohort Packについて相談する](https://github.com/KAFKA2306/marvelousdesigner/issues/new)
