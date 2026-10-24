<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# 王自如（ワン・ズールー）表現分析 第2版 · wangziru-analysis · V2

**構造を学び、癖を真似ません。彼の思考がどう回っているかを研究します。**

[![Version](https://img.shields.io/badge/version-v1.11-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · **日本語** · [Français](README.fr.md) · [Deutsch](README.de.md)

</div>

> **第2版、データ強化版です。** 第1版をより多くの動画データで発展させたものです。本人により近くなった反面、元サンプルへ過学習している可能性があります。より汎用的なオリジナル・レシピ、つまり題材を先に解体し品質ゲートを通してから書くブループリント型ワークフローが欲しければ [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1) を使ってください。両方試すのがおすすめです。

---

## このリポジトリは何か

**このリポジトリはまず研究プロジェクトです。王自如の思考が実際にどう作動するか、表現上の本当の癖は何かを研究します。** AIコーディングアシスタント用の Agent Skill はその研究結論を実行可能にまとめたプロダクト層です。二つの層を分けて読んでください。研究の入口は [`references/thinking-思维运转.md`](references/thinking-思维运转.md) で、すべての結論がコーパスのファイル名とタイムスタンプに遡れます。プロダクトの入口は `SKILL.md` です。どの結論が計測された事実で、どれが翻訳された執筆ルールかは [`METHODOLOGY.md`](METHODOLOGY.md) §9 の証拠グレード表に整理してあります。

### 核心的発見: 彼の頭はどう回っているか

全文は [thinking-思维运转.md](references/thinking-思维运转.md) にあります。要点は五つです。

1. **即興では判断が理由より先に出ることが多い。** 切り抜き25本・72の応答単位のうち、第一文が判定になっているのは72%（はい/いいえ型の質問で90%、開かれた質問で65%）で、89%はメカニズムの説明が続きます。「スマホ業界に未来はある？ もうない。」その後に続くのは主にメカニズムで、形容詞ではありません。以前は「台本動画は証拠が先、即興は逆、だから判断はあらかじめ作られている」と推論しましたが、v1.9で撤回しました。台本動画でも判定を先に出すことが多く（iPhone18 [00:58]）、切り抜きの開始点は編集者が決め、質問の多くは「ある？ない？」型です。「判断の事前製作」は未検証の仮説です。
2. **物差しは在庫。** 判断は動画を横断して呼び出される長期の基準ライブラリから来ます。ファーウェイ動画は iPhone18 動画の三格子物差しを直接再利用しています。基準は反語疑問文の形で現れることも多いです。
3. **譲歩は明示的。** 迷いの分岐を声に出して言い、一つを選び、自分の判断だと印を付けます。「我觉得」は1万字あたり6.5回で、ヘッジ語が確信語の約2.7倍です。確信は定義とナンバリングから生まれ、「絶対に」からは生まれません。
4. **締めの一文は保存形式。** すべての推論連鎖の終点で、判断を引用可能な一文に鋳ます。「口水で溺れ死んだ会社は一社もない」がその例です。
5. **口癖は動画ごとのばらつきが大きい。** 2026年の単独出演の長尺6本で、“对吧” は1万字あたり2.4回から20.0回まで幅があり、9月の2本は71動画ベースの長尺平均（約15回）より多いです。以前の「口癖は衰えている、20.8→3.7」は両端の分母が誤っていてサンプルも重なっていたため、v1.9で撤回しました。確かなのは、口癖では彼を捉えられないことです。同じ人が同じ年で8倍違います。

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="検証中の仮説：台本動画は証拠→判断、即興は判断→メカニズム。前半には反例があり、後半は切り抜き・質問形式・題材によるものかもしれません。"/>
</div>

### 推奨モデル

| 優先度 | モデル | 備考 |
|---|---|---|
| 🥇 **第一選択** | **Gemini 3.8 Flash** | 全 reference ファイルを一つのコンテキストに収められます。論理連鎖が安定し、書き直しの際に元文の人称と事実をよく保ち、コストパフォーマンスが最も良いです |
| 🥈 **第二選択** | **DeepSeek V4 Flash** | 代替です。話し言葉ベースに近い中国語の語感を持ち、2〜3分の短いナレーションで安定し、`tools/` チェッカーとの相性も堅実です |

## 30秒で始める

依存関係はありません。まず彼の実際の発話で AI臭チェッカーを体験してください。これがリポジトリ全体で唯一の実行可能な入口で、残りはすべて Markdownです。

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# 彼の実際の話し言葉、2026年9月の配信クリップです。AI臭は0点、人間の言葉グレードになります
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# AI生成の草稿を入れるとスコアは70を超えます。この差こそ本研究が説明するものです
python tools/ai_flavor_check.py draft.txt --json
```

Claude Code、Codex、Cursor などの AIコーディングアシスタントにスキルを入れると、台本作成、書き直し、コーチングをすぐ使えます。インストールは `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis` の一行です。

> **非公式** · 本リポジトリは表現方法の研究であり、王自如本人およびそのチームとは無関係です。彼の声や肖像を使わず、成果物を彼の名で署名したり本人を装ったりしないでください。

## コーパスと方法論

Bilibili「王自如AI」チャンネルの71動画、約50時間・864,937字が語頻度の基盤です。さらに2026年4月から10月の公式長編7本とサードパーティクリップ25本など、32本の完全書き起こしが `corpus/` にタイムスタンプ付きで公開されており、誰でも本リポジトリの数字を再現できます。研究方法は質的コーディングが中心で、語頻度は検証にのみ使います。サンプリング、収集と書き起こしのコマンド、再現ガイドは [`METHODOLOGY.md`](METHODOLOGY.md) に、研究過程の一次記録は `research/` に公開しています。

## コミュニティ

- **コントリビュート**: 結論の再現と反証、新規コーパスのコーディング、そして即興レイヤーのサンプリングバイアス検証が現在最も重要な未解決問題です。翻訳も歓迎します。[コントリビューションガイド](CONTRIBUTING.md)と[行動規範](CODE_OF_CONDUCT.md)を参照してください
- **姉妹リポジトリ**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1)、第1版、オリジナル・レシピ、ブループリント型ワークフロー

## ライセンス

[CC BY-NC 4.0](LICENSE)。出典を示せば自由に使用・改変・再配布でき、商用利用は禁止です。原文引用はこのライセンスの対象外です。詳細な研究ドキュメントは [README.md](README.md) と [README.en.md](README.en.md) を参照してください。
