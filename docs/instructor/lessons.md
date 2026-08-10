# 4回lesson plan

各回90分を標準枠とします。所要時間は実績値ではなく授業設計上の目安です。講師は授業前に `cohort-manifest.yaml` のsoftware baselineと使用assetの権利を確認してください。

## Lesson 1 — Pattern & Evidence

**Prerequisite:** software確認済み、再配布可能または受講者自身が利用権を持つavatar、Tシャツ教材を閲覧できること。

**Target software/version:** cohort manifest参照。

**Learning outcome:** 2D pattern → sewing → simulationの因果を説明し、操作結果と外観判断を別々に記録できる。

**Exercise:** [Tシャツ教材](../garments/t-shirt.md)を使い、前後身頃と袖のpatternを作り、縫製してsimulationする。

**Submission artifact:** pattern screenshot、simulation screenshot、使用software exact version、1件以上の`ExperimentalObservation`。

**Pass:** prerequisite・手順・観測結果が揃い、patternとsimulationの証拠が同一提出に紐づく。

**Fail / revise:** screenshotのみで手順・versionが不明、または「見た目が良い」だけをsimulation成功の根拠にする。

**Common failure:** sewing edgeの対応間違い、patternの左右非対称、初期衝突。

## Lesson 2 — Simulation & Fit

**Prerequisite:** Lesson 1合格または同等のpattern / sewing / simulation証拠。

**Target software/version:** cohort manifest参照。

**Learning outcome:** 布設定・simulation状態・fit判断を分離し、再現可能な修正理由を残せる。

**Exercise:** [スカート教材](../garments/skirt.md)と[布物性](../physics/fabric-properties.md)を参照し、1つのfit failureを特定して修正前後を比較する。

**Submission artifact:** before/after画像、変更した設定、観測したfailure、修正後の観測。

**Pass:** 変更した入力と観測結果の対応が明示され、`AestheticJudgment`を`CompatibilityClaim`として扱っていない。

**Fail / revise:** 設定値だけ、または「自然になった」だけで検証方法がない。

**Common failure:** collision margin不足、布物性の変更とpattern変更を同時に行い原因が判別不能。

## Lesson 3 — Mesh & Unity Handoff

**Prerequisite:** simulation済みgarmentと、受講者が利用権を持つavatar / project。

**Target software/version:** cohort manifest参照。UnityはVRChat対応versionを厳守する。

**Learning outcome:** export / mesh preparation / Unity importを段階別に確認し、import成功を完成と誤認しない。

**Exercise:** [Unity project設定](../unity/project-setup.md)と[FBX→VRChat workflow](../unity/fbx-to-vrchat-complete-guide.md)を参照し、garmentをUnityへ渡す。

**Submission artifact:** exported artifact識別子、mesh確認、Unity import screenshot、Console error有無、target avatar記録。

**Pass:** importの再現手順と結果があり、次工程のpose/runtime検証が未実施なら`CompatibilityClaim`を確定しない。

**Fail / revise:** FBXが読み込めたことだけを「VRChat対応」と記載する。

**Common failure:** scale / axis不整合、material参照欠落、weight / bone対応不足。

## Lesson 4 — VRChat Runtime Review

**Prerequisite:** Lesson 3のUnity handoffが合格し、VRChat SDKで検証できるprojectがある。

**Target software/version:** cohort manifest参照。

**Learning outcome:** pose、clipping、performance、runtimeを別gateとして監査し、最終claimの証拠をまとめられる。

**Exercise:** 複数poseで衣装を確認し、Console / SDK validation / runtime確認を行う。問題があれば「合格」に丸めず修正対象として記録する。

**Submission artifact:** pose evidence、SDK validation結果、runtime evidence、final review checklist、未解決項目。

**Pass:** target environmentとartifact revisionが識別され、fit / pose / runtime evidenceが揃う。未検証項目は未検証のまま残す。

**Fail / revise:** static screenshotのみ、target environment不明、または未確認項目を推測でPASSにする。

**Common failure:** 特定poseのみの貫通、expression / animation時の変形、SDK validation warningの見落とし。
