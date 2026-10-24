<div align="center">

<img src="assets/banner.svg" width="860" alt="wangziru-analysis"/>

# 왕쯔루(王自如) 표현 분석 제2판 · wangziru-analysis · V2

**구조를 배우고 억양을 흉내내지 않습니다. 그의 사고가 어떻게 굴러가는지를 연구합니다.**

[![Version](https://img.shields.io/badge/version-v1.10-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/chrislitality-svg/wangziru-analysis-skill-v2/ci.yml?branch=main&label=CI)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](tools/)
[![Corpus](https://img.shields.io/badge/corpus-103%20videos%20%C2%B70.96M%20chars-8b5cf6)](corpus/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[![Last Commit](https://img.shields.io/github/last-commit/chrislitality-svg/wangziru-analysis-skill-v2)](https://github.com/chrislitality-svg/wangziru-analysis-skill-v2/commits/main)

[简体中文](README.md) · [English](README.en.md) · **한국어** · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

</div>

> **제2판, 데이터 강화판입니다.** 제1판 위에 더 많은 영상 데이터를 얹어 발전시켰습니다. 본인에 더 가까워진 대신 원본 표본에 과적합되었을 수 있습니다. 더 범용적인 오리지널 레시피, 즉 주제를 먼저 해체하고 품질 게이트를 통과시킨 뒤 집필하는 청사진 워크플로가 필요하면 [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1)을 사용하세요. 두 버전 모두 써보시길 권합니다.

---

## 이 저장소는 무엇인가

**이 저장소는 먼저 연구 프로젝트입니다. 왕쯔루의 사고가 실제로 어떻게 작동하는지, 표현 습관은 무엇인지를 연구합니다.** AI 코딩 어시스턴트용 Agent Skill은 그 연구 결론을 실행 가능하게 요약한 제품 레이어입니다. 두 층을 나눠 읽으세요. 연구 입구는 [`references/thinking-思维运转.md`](references/thinking-思维运转.md)이고, 모든 결론이 코퍼스 파일과 타임스탬프로 소급 가능합니다. 제품 입구는 `SKILL.md`입니다. 어떤 결론이 측정된 사실이고 어떤 것이 번역된 작성 규칙인지는 [`METHODOLOGY.md`](METHODOLOGY.md) §9의 증거 등급표에 정리되어 있습니다.

### 핵심 발견: 그의 사고는 어떻게 굴러가는가

전체 문서는 [thinking-思维运转.md](references/thinking-思维运转.md)에 있습니다. 요약은 다섯 줄입니다.

1. **즉흥에서는 판단이 이유보다 먼저 나오는 경우가 많다.** 클립 25개의 응답 단위 72개 중 첫 문장이 판정인 것은 72%(예/아니오 질문 90%, 열린 질문 65%)이고, 89%는 메커니즘 설명이 뒤따릅니다. "휴대폰 업계에 미래가 있나? 없어." 뒤따르는 것은 주로 메커니즘이지 형용사가 아닙니다. 예전에는 "대본 영상은 증거가 먼저, 즉흥은 반대이니 판단은 미리 만들어진 것"이라고 추론했지만 v1.9에서 철회했습니다. 대본 영상도 판정을 먼저 내놓는 경우가 많고(iPhone18 [00:58]), 클립의 시작점은 편집자가 정하며, 클립 속 질문은 대부분 예/아니오 질문입니다. "미리 만들어진 판단"은 검증 전의 가설입니다.
2. **자는 재고다.** 판단은 영상을 가로질러 호출되는 장기 기준 라이브러리에서 나옵니다. 화웨이 영상은 아이폰18 영상의 3격자 자를 직접 재사용합니다. 기준은 수사의문문 형태로 나타나기도 합니다.
3. **양보는 명시적이다.** 망설임의 분기를 소리 내어 말하고, 하나를 고르고, 자기 판단임을 표시합니다. "我觉得"는 만자당 6.5회이고 헤지 단어가 확신 단어의 약 2.7배입니다. 확신은 정의와 번호 매기기에서 나오지 "분명히"나 "절대적으로"에서 나오지 않습니다.
4. **마무리 문장은 저장 형식이다.** 모든 추론 사슬의 끝에서 판단을 인용 가능한 한 문장으로 주조합니다. 예를 들어 "침에 빠져 죽은 회사는 없다"가 그렇습니다.
5. **입버릇은 영상마다 편차가 크다.** 2026년 단독 장편 6개에서 "对吧"는 만자당 2.4회에서 20.0회까지 오가며, 9월 두 편은 71영상 기반 장편 평균(약 15회)보다 높습니다. 이전의 "입버릇이 사라지고 있다, 20.8 → 3.7"은 양쪽 분모가 모두 틀렸고 표본도 겹쳐 v1.9에서 철회했습니다. 확실한 것은 입버릇으로는 그를 잡을 수 없다는 점입니다. 같은 사람이 같은 해에 8배까지 차이 납니다.

<div align="center">
<img src="assets/mindflow.svg" width="820" alt="검증 중인 가설: 대본 영상은 증거→판단, 즉흥 대답은 판단→메커니즘. 앞부분에는 반례가 있고, 뒷부분은 편집·질문 형식·주제 때문일 수 있습니다."/>
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

Claude Code, Codex, Cursor 같은 AI 코딩 어시스턴트에 스킬을 설치하면 작성, 수정, 코칭을 바로 쓸 수 있습니다. 설치는 `git clone https://github.com/chrislitality-svg/wangziru-analysis-skill-v2.git ~/.claude/skills/wangziru-analysis` 한 줄입니다.

> **비공식** · 본 저장소는 표현 방법 연구로 왕쯔루 본인 및 그 팀과 무관합니다. 그의 목소리나 초상을 사용하지 않으며, 산출물에 그의 이름을 서명하거나 본인을 사칭해서는 안 됩니다.

## 코퍼스와 방법론

빌리빌리 왕쯔루AI 채널의 71개 영상, 약 50시간 분량 864,937자가 어휘 빈도의 기반이 됩니다. 여기에 2026년 4월부터 10월까지의 공식 장편 7편과 서드파티 클립 25편 등 32개 전문 전사가 `corpus/`에 타임스탬프와 함께 공개되어 있어 누구나 이 저장소의 숫자를 재현할 수 있습니다. 연구 방법은 질적 부호화가 중심이고 어휘 빈도는 검증에만 씁니다. 샘플링과 채집, 전사 명령, 재현 가이드는 [`METHODOLOGY.md`](METHODOLOGY.md)에, 연구 과정의 원본 기록은 `research/`에 공개되어 있습니다.

## 커뮤니티

- **기여**: 결론의 재현과 반박, 새 코퍼스 부호화, 즉흥 레이어의 표본 편향 검증이 현재 가장 중요한 열린 문제입니다. 번역도 환영합니다. [기여 가이드](CONTRIBUTING.md)와 [행동 강령](CODE_OF_CONDUCT.md)을 참고하세요
- **자매 저장소**: [wangziru-analysis-skill-v1](https://github.com/chrislitality-svg/wangziru-analysis-skill-v1), 제1판, 오리지널 레시피, 청사진 워크플로

## 라이선스

[CC BY-NC 4.0](LICENSE). 출처를 밝히면 자유롭게 쓰고 고치고 다시 배포할 수 있고 상업적 사용은 금지됩니다. 원문 인용은 이 라이선스 범위 밖입니다. 상세한 연구 문서는 [README.md](README.md)와 [README.en.md](README.en.md)를 참고하세요.
