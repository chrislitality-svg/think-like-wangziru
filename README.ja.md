<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# 王自如（ワン・ズールー）的表現分析 第2版 · wangziru-analysis · V2

**構造を学び、癖を真似ない — 彼の思考がどう回っているかを研究します。**

[![Version](https://img.shields.io/badge/version-v1.7-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B71.04M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Stars](https://img.shields.io/github/stars/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/stargazers)
[![Forks](https://img.shields.io/github/forks/chrislitality-svg/wangziru-analysis-skill-v2?style=social)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/network/members)

[简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · **日本語** · [Français](README.fr.md) · [Deutsch](README.de.md)

</div>

> **第2版（V2）— データ強化版**: 第1版（オリジナル・レシピ）をより多くの動画データで発展させた版で、本人により近い反面、元サンプルへ過学習している可能性があります。より汎用的なオリジナル・レシピ（ブループリント先行ワークフロー）は [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1) を使ってください。両方試すのをおすすめします。

---

## このリポジトリは何か

**このリポジトリはまず研究プロジェクトです: 王自如の思考が実際にどう作動するか、彼の表現上の本当の癖は何か。** AIコーディングアシスタント用の Agent Skill（`SKILL.md` — 台本作成 / 書き直し / コーチング）は、その研究結論を実行可能に要約したプロダクト層です。研究の入口は [`references/thinking-思维运转.md`](references/thinking-思维运转.md)（すべての結論にコーパス出典とタイムスタンプ付き）、プロダクトの入口は `SKILL.md`。どの結論が計測された事実で、どれが翻訳された執筆ルールかは [`METHODOLOGY.md`](METHODOLOGY.md) §9 の証拠グレード表で区別できます。

### 核心的発見: 彼の頭はどう回っているか

1. **判断が言語に先立つ。** 即興で問われれば、判定は最初の一拍で遅延ゼロに落ちる（「スマホ業界に未来はある？ — もうない。」）。その後に言葉が補うのは常にメカニズムであって形容詞ではない。台本のある動画では順序が反転する（証拠→判断）。一つの頭脳、二つの出力モード — 判断はあらかじめ作られたもので、その場の推論ではない。
2. **物差しは在庫。** 判断は動画を横断して呼び出される長期の基準ライブラリから来る（ファーウェイ動画が iPhone18 動画の三格子物差しを直接再利用）。基準は反語疑問文の形で現れることも多い。
3. **譲歩は明示的。** 迷いの分岐を声に出して言い、一つを選び、自分の判断だと印を付ける（"我觉得" 1万字あたり6.5回；ヘッジ語が確信語の約2.7倍 — 確信は定義とナンバリングから来る）。
4. **締めの一文は保存形式。** すべての推論連鎖の終点で、判断を引用可能な一文に鋳る（「口水で溺れ死んだ会社は一社もない」）。
5. **口癖は衰えている。** "对吧" は71動画ベースの1万字あたり20.8回から2026年コーパスの3.7回に低下。彼の口癖を真似ることは、彼が捨てつつある部分を真似ること。彼の連続性は作動の順序にあり、どの単一語にもない。

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="一つの頭脳、二つの順序 — 台本動画は証拠→判断、即興は判断→メカニズム"/>
</div>

### 推奨モデル

| 優先度 | モデル | 備考 |
|---|---|---|
| 🥇 **第一選択** | **Gemini 3.8 Flash** | 全 reference ファイルを一つのコンテキストに収められる長いコンテキスト、安定した論理連鎖、書き直し時の人称・事実の保存、コストパフォーマンス最高 |
| 🥈 **第二選択** | **DeepSeek V4 Flash** | 代替: 話し言葉ベースに近い中国語の語感、2–3分の短いナレーションで安定、`tools/` チェッカーとの相性も堅実 |

## 30秒で始める

依存関係ゼロ — 彼の実際の発話で AI臭（AI 味）チェッカーを体験してください:

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# 彼の実際の話し言葉（2026-09 配信クリップ）で検査: AI臭 ≈ 11 期待値（人間の言葉グレード）
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# AI生成の草稿を入れるとスコアは70+に跳ねる — その差こそ本研究が説明するもの
python tools/ai_flavor_check.py draft.txt --json
```

AIコーディングアシスタント（Claude Code / Codex / Cursor など）へのスキールインストール: `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

> **非公式** · 本リポジトリは表現方法の研究であり、王自如本人およびそのチームとは無関係です。彼の声や肖像を使用せず、成果物に彼の名で署名したり本人を装ったりしないでください。

## コーパスと方法論

- **コーパス**: Bilibili「王自如AI」チャンネル **71動画**（約50時間、864,937字）+ 2026年4–10月の公式長編7本・サードパーティクリップ25本など **32本の完全書き起こしを公開**（`corpus/`、タイムスタンプ付き）。誰でも本リポジトリの数字を再現できます。
- **方法論**: 質的コーディング（問答連鎖）を主軸に、語頻度は検証専用。サンプリング・収集・書き起こしコマンド・再現ガイドは [`METHODOLOGY.md`](METHODOLOGY.md)、研究過程の一次記録は `research/` に公開。

## コミュニティ

- **コントリビュート**: 結論の再現・反証、新規コーパスのコーディング、即興レイヤーのサンプリングバイアス検証（最優先の未解決問題）、翻訳 — [コントリビューションガイド](CONTRIBUTING.md) / [行動規範](CODE_OF_CONDUCT.md)
- **姉妹リポジトリ**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1)（第1版 · オリジナル・レシピ · ブループリント型ワークフロー）

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=chrislitality-svg/wangziru-analysis-skill-v2&type=Date)](https://star-history.com/#chrislitality-svg/wangziru-analysis-skill-v2&Date)

この研究が役に立ったら Star をお願いします ⭐

</div>

## ライセンス

[CC BY-NC 4.0](LICENSE): 出典表示の下で自由に使用・改変・再配布可能、商用利用は禁止。原文引用はこのライセンスの対象外です。詳細な研究ドキュメント（中国語・英語）は [README.md](README.md) / [README.en.md](README.en.md) を参照してください。
