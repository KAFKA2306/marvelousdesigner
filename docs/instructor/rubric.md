# 講師用rubric

各gateは `PASS / REVISE / NOT_TESTED` の3状態です。`NOT_TESTED`をPASSへ補完してはいけません。

| Gate | PASSに必要な証拠 | REVISE例 |
| --- | --- | --- |
| Version context | 使用softwareのexact version | version未記録 |
| Instruction | prerequisite / steps / expected result / verification | 操作だけで検証方法なし |
| Pattern / structure | patternまたはmeshの識別可能な証拠 | 完成画像だけ |
| Simulation observation | input設定とobserved result | 外観感想のみ |
| Unity handoff | artifact revision / import result / Console確認 | import成功だけで完成扱い |
| Fit / pose | target avatarとpose evidence | 1枚の静止画のみ |
| Runtime | target environmentとruntime evidence | Unity Sceneだけで互換性断定 |
| Rights | 使用assetの権利確認、再配布なし | 購入assetを提出物へ同梱 |

## Evidence typeの扱い

### VendorDocumentedFact

公式source URLとsoftware versionまたはdocument dateが必要です。講師の記憶や二次記事だけではこの区分にしません。

### ExperimentalObservation

input artifact、procedure、environment、observed resultを記録します。別環境へ一般化する場合は追加検証が必要です。

### Instruction

prerequisite、steps、expected result、verification methodの4点を確認します。

### CalculatedValue

計算式または測定方法と入力値を確認します。推定を測定値として扱いません。

### AestheticJudgment

見た目・好み・自然さ等の人間評価です。`CompatibilityClaim`の証拠として単独利用しません。

### CompatibilityClaim

target environment、artifact revision、importとruntimeの証拠を必要とします。未検証なら`NOT_TESTED`です。

## Lesson判定

- **PASS:** 当該lessonで必須のgateが全てPASSし、未解決failureが次工程を阻害しない
- **REVISE:** 必須証拠欠落、再現不能、rights不明、またはfailureが残る
- **NOT_TESTED:** 実行・確認していない。失敗と同義ではないが、合格の根拠にもならない

## 最終判定

4回終了時の「完成」は、単なるFBX exportやUnity importではなく、対象artifactについて必要なfit / pose / performance / runtime evidenceが揃った場合だけ付与します。外観品質は別の人間評価として残します。
