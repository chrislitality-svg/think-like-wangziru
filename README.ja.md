<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# 王自如（ワン・ズールー）式思考 第2版 · wangziru-analysis

**答えを先に、理由をはっきり、突っ込まれても崩れない。AIに一言伝えるだけで、問題の分析、台本の作成、原稿の手直し、一つのテーマをとことん話し合う相手までこなします。**

[![Version](https://img.shields.io/badge/version-v1.12-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · **日本語** · [Français](README.fr.md) · [Deutsch](README.de.md)

</div>

> **第2版です。** より多くの動画データで磨いたため彼の説明の仕方に近づきましたが、元のサンプルに寄りすぎている可能性もあります。先に構成案を作ってから書く汎用版が欲しい場合は第1版 [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1) をどうぞ。両方試す価値があります。

---

## このリポジトリは何か

Claude Code、Codex、Cursor などの AI ツールに入れるスキルです。入れたあとはコマンドを覚える必要はなく、AI に一言伝えるだけで使えます。

このスキルは、王自如が一つの物事をはっきり説明するやり方で AI に内容を作らせます。答えを先に言い、理由を言い、物事が実際にどう動いているかを説明し、例外と代償を先に示します。読者が王自如を知らなくても、理解し、覚え、人に伝えられる文章になります。

この方法は印象で作ったものではありません。彼の動画 32 本を一字ずつ書き起こし、段落ごとに読みました。スキルの中のやり方にはすべて彼の元の言葉とタイムスタンプが付いていて、自分で確かめられます。

## 使い方：一言伝えるだけ

スキルの指示は中国語で書かれているため、中国語で頼むと一番よく動きます。出力の言語を AI に指定することもできます。

| こう言うと | こうなります | 例 |
|---|---|---|
| 用王自如 skill 分析一下：现在给孩子报编程班还值不值？（子どものプログラミング教室、まだ通わせる価値はある？を分析して） | そのまま共有できる短い分析文。最初の段落に答え、続いて判断基準、理由、例外、アドバイス | [例 05](examples/05-分析-孩子要不要学编程.md) |
| 用王自如的方式写一篇 2 分钟口播：为什么收藏了那么多干货还是没进步（2分の台本：ノウハウをあれだけ保存したのに、なぜ上達しないのか） | そのまま読める台本と、論理を確かめるための「問い・答え・根拠」の3行 | [例 06](examples/06-写稿-收藏了那么多干货为什么没进步.md) |
| 我想和王自如聊聊要不要辞职创业，你来当王自如（退職して起業すべきか王自如と話したい、王自如役をやって） | やり取りの対話。毎回、判断と理由があります。AI は彼のやり方で考えていると明言し、本人を名乗らず、彼の経験を作り上げません | [例 07](examples/07-对谈-30岁要不要辞职创业.md) |
| 这是我的逐字稿，王自如帮我改一下：（贴上稿子）（私の原稿を直して） | 一番大事な問題を一つか二つ、直した全文、変更の説明。あなたの話し方と事実はそのまま残します | [例 08](examples/08-改稿-年轻人要不要考公.md) |

インストールは一行です：`git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

## 方法はどこから来たか：彼の頭はどう回っているか

以下の5点は要約です。原文の出典、反例、まだ確定していない点は [thinking-思维运转.md](references/thinking-思维运转.md) にあります。

1. **答えが先、理由はあと。** 配信で質問されると、たいてい最初の一文で答えます。「スマホ業界に未来はある？ もうない。」それから理由を話します。はい/いいえで答える質問で最も目立ちますが、開かれた質問でもほとんど同じです。
2. **ほぼ毎回、理由を言う。** 結論だけを投げることはまれです。理由はたいてい計算、ユーザー側の矛盾、物理的な限界、もう過ぎてしまった時機で、形容詞に頼ることはまれです。
3. **自分の物差しを使い、繰り返し持ち出す。** Huawei の動画では、2週間前に iPhone を評価したときの三つの基準、つまり体感が大きいか、よく使うか、お金に見合うかをそのまま使いました。こうした使い回しはまだ二回しか確認できず、習慣と言い切るには早すぎます。
4. **迷いを口に出し、どちらかを選ぶ。** 西貝（シーベイ）の騒動について「問題は埋もれるのか、遅れて出るのか、出ないのか？ 遅れて出るだけだ」と話しました。可能性を並べ、どれが自分の考えかを示します。台本のある動画では「必ず」「絶対」をあまり言わず、配信ではもっと言います。
5. **口癖は彼のトレードマークではない。** 同じ年でも “对吧”（でしょ？）は、ある動画では1万字あたり2回、別の動画では20回です。口癖を真似ても彼らしくはなりません。

以前は、彼の判断はすべて事前にでき上がっていて、その場で取り出しているだけだと考えていました。証拠が十分ではないため、今は検証すべき仮説として扱っています。

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="配信で質問されたときの彼のよくある順序：答えが先、理由、本当に例外があるときだけ譲歩、言えることがあれば一言で締める"/>
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

Claude Code、Codex、Cursor などの AIコーディングアシスタントにスキルを入れると、分析、台本作成、対話、原稿の手直しをすぐ使えます。インストールは `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis` の一行です。

> **非公式** · 本リポジトリは表現方法の研究であり、王自如本人およびそのチームとは無関係です。彼の声や肖像を使わず、成果物を彼の名で署名したり本人を装ったりしないでください。

## コーパスと方法論

Bilibili「王自如AI」チャンネルの71動画、約50時間・864,937字が語頻度の基盤です。さらに2026年4月から10月の公式長編7本とサードパーティクリップ25本など、32本の完全書き起こしが `corpus/` にタイムスタンプ付きで公開されており、誰でも本リポジトリの数字を再現できます。研究方法は質的コーディングが中心で、語頻度は検証にのみ使います。サンプリング、収集と書き起こしのコマンド、再現ガイドは [`METHODOLOGY.md`](METHODOLOGY.md) に、研究過程の一次記録は `research/` に公開しています。

## コミュニティ

- **コントリビュート**: 結論の再現と反証、新規コーパスのコーディング、そして即興レイヤーのサンプリングバイアス検証が現在最も重要な未解決問題です。翻訳も歓迎します。[コントリビューションガイド](CONTRIBUTING.md)と[行動規範](CODE_OF_CONDUCT.md)を参照してください
- **姉妹リポジトリ**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1)、第1版、オリジナル・レシピ、ブループリント型ワークフロー

## ライセンス

[CC BY-NC 4.0](LICENSE)。出典を示せば自由に使用・改変・再配布でき、商用利用は禁止です。原文引用はこのライセンスの対象外です。詳細な研究ドキュメントは [README.md](README.md) と [README.en.md](README.en.md) を参照してください。
