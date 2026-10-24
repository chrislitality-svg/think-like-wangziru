<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# 왕쯔루(王自如)식 사고 제2판 · wangziru-analysis

**답부터 말하고, 이유를 분명히 하고, 반문에도 버틴다. AI에게 한 문장만 말하면 문제를 분석하고, 원고를 쓰고, 원고를 고치고, 한 가지 주제를 끝까지 함께 이야기해 줍니다.**

[![Version](https://img.shields.io/badge/version-v1.12-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · **한국어** · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

</div>

> **제2판입니다.** 더 많은 영상 데이터로 다듬어서 그의 설명 방식에 더 가깝지만, 원래 표본에 더 붙어 있을 수도 있습니다. 개요를 먼저 만든 뒤 쓰는 범용 버전이 필요하면 제1판 [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1)을 쓰세요. 둘 다 써 볼 만합니다.

---

## 이 저장소는 무엇인가

Claude Code, Codex, Cursor 같은 AI 도구에 설치하는 스킬입니다. 설치한 뒤에는 명령어를 배울 필요 없이 AI에게 한 문장만 말하면 됩니다.

이 스킬은 AI가 왕쯔루가 한 가지 일을 분명하게 설명하는 방식으로 내용을 만들게 합니다. 답을 먼저 말하고, 이유를 말하고, 그 일이 실제로 어떻게 돌아가는지 설명하고, 예외와 대가를 먼저 밝힙니다. 독자가 왕쯔루를 몰라도 이해하고, 기억하고, 다른 사람에게 전할 수 있는 글이 나옵니다.

이 방법은 인상에 기대지 않았습니다. 그의 영상 32편을 한 글자씩 받아 적고 단락마다 읽었습니다. 스킬 안의 모든 방법에는 그의 원래 말과 타임스탬프가 붙어 있어 직접 확인할 수 있습니다.

## 사용법: 한 문장만 말하세요

스킬 지침은 중국어로 쓰여 있어 중국어로 요청할 때 가장 잘 작동합니다. 원하는 출력 언어를 AI에게 따로 말해도 됩니다.

| 이렇게 말하면 | 이런 결과가 나옵니다 | 예시 |
|---|---|---|
| 用王自如 skill 分析一下：现在给孩子报编程班还值不值？ (아이 코딩 학원, 아직 보낼 만한가 분석해 줘) | 바로 공유할 수 있는 짧은 분석 글. 첫 단락에 답, 이어서 판단 기준, 이유, 예외, 조언 | [예시 05](examples/05-分析-孩子要不要学编程.md) |
| 用王自如的方式写一篇 2 分钟口播：为什么收藏了那么多干货还是没进步 (2분짜리 원고: 꿀팁을 그렇게 저장했는데 왜 늘지 않을까) | 바로 읽을 수 있는 원고와, 논리를 점검할 수 있게 질문·답·근거 세 줄 | [예시 06](examples/06-写稿-收藏了那么多干货为什么没进步.md) |
| 我想和王自如聊聊要不要辞职创业，你来当王自如 (퇴사하고 창업할지 왕쯔루와 이야기하고 싶어, 네가 왕쯔루 역을 해 줘) | 주고받는 대화. 매 턴에 판단과 이유가 있습니다. AI는 그의 방식으로 생각하고 있다고 밝히며, 본인을 사칭하거나 그의 경험을 지어내지 않습니다 | [예시 07](examples/07-对谈-30岁要不要辞职创业.md) |
| 这是我的逐字稿，王自如帮我改一下：（贴上稿子） (내 원고를 고쳐 줘) | 가장 중요한 문제 한두 개, 고친 전문, 수정 설명. 당신의 말투와 사실은 그대로 둡니다 | [예시 08](examples/08-改稿-年轻人要不要考公.md) |

설치는 한 줄입니다: `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis`

## 방법은 어디서 왔나: 그의 사고는 어떻게 굴러가는가

아래 다섯 가지는 요약입니다. 원문 출처, 반례, 아직 확정되지 않은 부분은 [thinking-思维运转.md](references/thinking-思维运转.md)에 있습니다.

1. **답부터, 이유는 그다음.** 라이브에서 질문을 받으면 대개 첫 문장에 답을 줍니다. "휴대폰 업계에 미래가 있나? 없어." 그다음에 이유를 말합니다. 예/아니오 질문에서 가장 뚜렷하지만 열린 질문도 대부분 그렇습니다.
2. **거의 매번 이유를 말한다.** 결론만 던지는 일은 드뭅니다. 이유는 보통 계산, 사용자의 모순, 물리적 한계, 이미 지나간 시기이고, 형용사에 기대는 일은 드뭅니다.
3. **자기 기준을 쓰고, 다시 꺼내 쓴다.** 화웨이 영상에서 2주 전 아이폰을 평가하며 말한 세 가지 기준, 즉 체감이 큰가, 자주 쓰는가, 값어치가 있는가를 그대로 가져왔습니다. 이런 재사용은 아직 두 번밖에 보지 못해 습관이라고 단정하기는 이릅니다.
4. **망설임을 소리 내어 말하고, 한쪽을 고른다.** 시베이(西贝) 논란에 대해 "문제가 묻힐까, 늦게 터질까, 아예 안 터질까? 늦게 터질 뿐이다."라고 말했습니다. 가능성을 늘어놓고 어느 쪽이 자기 생각인지 밝힙니다. 대본 영상에서는 "반드시", "절대"를 잘 쓰지 않고, 라이브에서는 더 자주 씁니다.
5. **입버릇은 그의 상징이 아니다.** 같은 해에도 "对吧"(그렇죠?)는 어떤 영상에서는 만 자당 2번, 어떤 영상에서는 20번 나옵니다. 입버릇을 따라 해서는 그처럼 되지 않습니다.

예전에는 그의 판단이 모두 미리 정해져 있고 현장에서 꺼내 쓰는 것이라고 생각했습니다. 근거가 충분하지 않아 지금은 검증할 가설로만 둡니다.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="라이브에서 질문을 받았을 때 그의 흔한 순서: 답부터, 이유, 진짜 예외가 있을 때만 양보, 할 말이 있으면 한 문장으로 마무리"/>
</div>

### 추천 모델

| 우선순위 | 모델 | 비고 |
|---|---|---|
| 🥇 **1순위** | **Gemini 3.8 Flash** | 모든 reference 파일을 한 컨텍스트에 담을 수 있습니다. 논리 사슬이 안정적이고 수정 시 원문의 인칭과 사실을 잘 보존하며 가성비가 가장 좋습니다 |
| 🥈 **2순위** | **DeepSeek V4 Flash** | 대안입니다. 구어 기준에 가까운 중국어 감각을 가지고 2~3분 짧은 구술에서 안정적이며 `tools/` 검사기와의 호환도 견고합니다 |

## 30초 시작하기

의존성이 없습니다. 먼저 그의 실제 발화로 AI맛 검사기를 체험해 보세요. 이것이 저장소 전체에서 유일한 실행 가능한 입구이고 나머지는 전부 Markdown입니다.

```bash
git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git
cd wangziru-analysis-skill-v2

# 그의 실제 구술, 2026년 9월 라이브 클립입니다. AI맛 0점, 사람 말 등급이 나옵니다
python tools/ai_flavor_check.py "corpus/clips-jachzhu/2026-09-22-聊西贝事件的根源-1m11s.txt"

# AI 생성 초안을 넣으면 점수가 70을 넘습니다. 이 격차가 연구가 설명하는 대상입니다
python tools/ai_flavor_check.py draft.txt --json
```

Claude Code, Codex, Cursor 같은 AI 코딩 어시스턴트에 스킬을 설치하면 분석, 원고 작성, 대화, 원고 수정을 바로 쓸 수 있습니다. 설치는 `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis` 한 줄입니다.

> **비공식** · 본 저장소는 표현 방법 연구로 왕쯔루 본인 및 그 팀과 무관합니다. 그의 목소리나 초상을 사용하지 않으며, 산출물에 그의 이름을 서명하거나 본인을 사칭해서는 안 됩니다.

## 코퍼스와 방법론

빌리빌리 왕쯔루AI 채널의 71개 영상, 약 50시간 분량 864,937자가 어휘 빈도의 기반이 됩니다. 여기에 2026년 4월부터 10월까지의 공식 장편 7편과 서드파티 클립 25편 등 32개 전문 전사가 `corpus/`에 타임스탬프와 함께 공개되어 있어 누구나 이 저장소의 숫자를 재현할 수 있습니다. 연구 방법은 질적 부호화가 중심이고 어휘 빈도는 검증에만 씁니다. 샘플링과 채집, 전사 명령, 재현 가이드는 [`METHODOLOGY.md`](METHODOLOGY.md)에, 연구 과정의 원본 기록은 `research/`에 공개되어 있습니다.

## 커뮤니티

- **기여**: 결론의 재현과 반박, 새 코퍼스 부호화, 즉흥 레이어의 표본 편향 검증이 현재 가장 중요한 열린 문제입니다. 번역도 환영합니다. [기여 가이드](CONTRIBUTING.md)와 [행동 강령](CODE_OF_CONDUCT.md)을 참고하세요
- **자매 저장소**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1), 제1판, 오리지널 레시피, 청사진 워크플로

## 라이선스

[CC BY-NC 4.0](LICENSE). 출처를 밝히면 자유롭게 쓰고 고치고 다시 배포할 수 있고 상업적 사용은 금지됩니다. 원문 인용은 이 라이선스 범위 밖입니다. 상세한 연구 문서는 [README.md](README.md)와 [README.en.md](README.en.md)를 참고하세요.
