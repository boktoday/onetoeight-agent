# OneToEight Agent: 개요와 설정 흐름

**OneToEight Agent**는 **여덟 가지 핵심**을 매일의 삶에
들여놓는 법을 배우는 젊은 세대를 위해
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) 위에
만든 맞춤형 AI 어시스턴트예요. 오디오 계획과 돌아보기 체크인,
작은 실천으로 하루의 리듬을 다정하게 이끌어 주는 멘토이고,
repo에 함께 들어 있는 여덟 가지 핵심 가이드에서 가르쳐요.

이 README는 개요이자, agent가 처음부터 끝까지 돌아가게 만드는
설정 흐름이에요. 한 번 읽고, 단계를 따라가 봐요.

> **두 가지 길.** **build path**를 따라 agent를 하나씩
> 만들어 볼 수 있어요: 매주 능력 하나, 성과 하나, 따라 들을
> 오디오까지요. 아니면 아래 설정 흐름으로 설치해도 돼요.
>
> **build path 시작하기: <https://gladtobe.here.now/build-path/>**

> 다른 언어로 보기: **한국어** · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Filipino](README.tl.md) · [Español](README.es.md) · [中文](README.zh.md) · [日本語](README.ja.md)

---

## 이 제품은 무엇인가요

여덟 가지 핵심은 책을 읽는 것보다 **하루에 작은 일 하나를 해
보는 것**으로, 몇 주 몇 달에 걸쳐 가장 잘 몸에 붙어요.
그 하루의 리듬이 계속 이어지게 돕는 게 OneToEight Agent예요:

- **아침의 1분**(Morning Minute)이 정한 시간에 채팅
  (Telegram 또는 WhatsApp)으로 도착해요. 그날을 위한 짧은
  오디오 계획과 텍스트예요.
- **오후 체크인**(Afternoon Check-In)이 오후에 도착해요. 짧은
  문자 메시지예요: 하루가 어땠는지, 다음은 무엇인지, 밤새
  곱씹어 볼 질문 하나.
- **계획 세션**(Planning Session)이 잠들기 전에 도착해요.
  내일을 그려 줘요: 학교 과제, 숙제 마감, 이번 주에 다루는
  핵심, 직접 해 보고 싶은 실제의 일 하나. agent가 계획을 쓰면
  직접 고치고, 로컬에 저장돼요. 앱도, 계정도, 클라우드
  동기화도 없어요.
- agent는 repo에 담긴 **여덟 가지 핵심 가이드**
  (`essentials/01..08/lessons/*.md`)에서 가르치고, 고른 전통에
  따라 내용을 나눠요.
- 가이드는 **열 개 언어**로도 발행돼요. 온라인으로 읽거나,
  인터넷 없이 쓸 수 있는 offline pack으로 내려받을 수 있어요.
  `essentials/guide-editions.md`를 봐요.

agent는 설교하지 않아요. 질문으로 지혜를 끌어내고, 리듬을
다정하게 붙들어 주고, 넘어졌을 때 꾸중 없이 다시 시작하게
도와줘요.

### 두 가지 전통, 아니면 나만의 전통

온보딩에서 하나를 골라요. 아니면 원하는 전통을 agent에게 알려
주면 그걸로 맞춰 줘요. agent는 고른 전통 안에 머물고, 전통을
섞는 일은 없어요:

- **크리스천**: 성경에 뿌리를 둬요. 아침의 1분에 매일 성경
  구절이 자연스럽게 들어가고, 체크인은 하루를 살아 있는 믿음
  안에서 바라봐요.
- **유니버설(세속)**: 교리 없이 지혜의 전통을 존중해요. 아침의
  1분에 사상가의 짧은 성찰이나 질문이 들어가고, 체크인은
  돌아보기와 감사, 의도 안에서 하루를 바라봐요.

나중에 전통을 바꿀 수는 있지만, 그 순간부터 레슨이 새 전통을
따라가요.

### 두 가지 전달 순서

여덟 가지 핵심을 어떤 순서로 전할지도 골라요:

- **순차**(기본): 핵심 1부터 8까지 차례대로 지나가요. 가장
  일관성 있고, 가이드가 쓰인 순서예요. 이제 막 시작한다면
  추천해요.
- **무작위**: 어느 날이든 그날 필요해 보이는 핵심을 뽑아요
  (가장 오래 안 다룬 것, 최근에 어려워한 것, 그날의 에너지).
  아침의 1분마다 고른 핵심의 지식 요약과 작은 활동 하나로
  시작해요. 이미 무엇이 필요한지 아는 사람에게 잘 맞아요.

두 방식 모두 **언젠가는 여덟 가지 핵심을 다 다뤄요.** 나중에
`essentials_order` memory key를 바꾸면 전환할 수 있고, 온보딩을
다시 할 필요는 없어요.

### 여덟 가지 핵심 (가이드가 가르치는 순서대로)

1. **침묵에 앉아 있는 능력**: 가만히 앉아서 자기 생각과 단둘이 있어요
2. **몸은 집이다**: 잠, 음식, 물, 움직임, 햇빛
3. **실생활에 쓸모 있는 기술**: 요리하고, 고치고, 만들고, 예산을 세우는 힘
4. **디지털 자기방어**: 사생활, 주의, 신원 문해력
5. **진짜 공동체**: 내 이름을 아는 사람들
6. **Wi-Fi 없이도 되는 지식**: 빌리지 않고 내 것으로
7. **자연을 처방하다**: 처방된 바깥 시간, 양보는 없어요
8. **시험을 거친 신념**: 내 것이고, 압박 속에서도 버텨요

---

## 어떻게 작동하나요

### 하루의 흐름

```
06:00  아침의 1분        Piper TTS 오디오 + 텍스트 → Telegram 또는 WhatsApp
        ↓
낮     작은 실천 하나를 해요
        ↓
17:00  오후 체크인       텍스트만 → Telegram 또는 WhatsApp
        ↓
21:00  계획 세션         텍스트만 → Telegram 또는 WhatsApp
       agent가 내일 계획 초안 → 직접 고치기 → 로컬에 저장
        ↓
        잠
        ↓
        반복
```

agent는 잔소리 없이 이 흐름을 북돋아요. 놓친 날은 다정하게
다시 시작해요. 꾸중도, 훈계도 없어요.

**일정에 대해:** 위에 나온 시간은 사는 곳의 로컬 timezone
기준이에요. cron daemon은 일정을 **UTC**로 저장해요. 한국 시간
오전 6시(UTC+9)를 고르면 cron에는 `0 21 * * *`(21:00 UTC)로
저장돼요. 일정은 언제나 "내 timezone의 시간"이고, UTC 변환은
자동이에요.

### 각 순간마다 agent가 하는 일

| 언제 | agent가 하는 일 |
|---|---|
| 새 profile에서의 첫 채팅 | 짧게, 자기 목소리로 오리엔테이션을 제안해요 |
| "설정해 줘"라고 말할 때 | `agent-onboarding`을 실행해요(동의 기반, 단계별) |
| 질문할 때 | 관련 `essentials/<NN-name>/lessons/*.md`를 읽고, 정리해서 가르쳐요 |
| 아침의 1분 cron이 돌 때 | 그날의 계획을 만들고, Piper를 돌리고, 업로드해서 바로 전달해요 |
| 체크인 cron이 돌 때 | 가장 최근의 아침의 1분을 읽고, 짧은 돌아보기를 써서 텍스트로 보내요 |
| 계획 세션 cron이 돌 때 | 내일 계획 초안(학교 과제, 마감, 이번 주 핵심, 실제로 해 볼 일 하나)을 쓰면, 직접 고치고, 로컬에 저장돼요 |
| 더 깊이 배우고 싶다고 할 때 | `eight-essentials-curriculum` skill로 가이드를 읽고, 그대로 가르쳐요 |

### 백그라운드에서 돌아가는 것들

cron job 세 개가 있어요. 모두 온보딩에서 명확히 승인하기
전까지는 꺼져 있어요:

1. **아침의 1분**: 사는 곳의 timezone 기준으로 정한 시간에,
   매일(또는 원하면 평일에만) 돌아요. 오디오와 텍스트를 만들어
   Telegram 또는 WhatsApp으로 보내요.
2. **오후 체크인**: 정한 오후 시간에 돌아요. 아침의 1분과 같은
   요일 규칙이에요. 짧은 문자 메시지를 보내요.
3. **계획 세션**: 잠들기 전(기본 오후 9시)에 돌아요. 같은 요일
   규칙이에요. 내일 계획 초안을 써서 직접 고칠 수 있게 하고,
   로컬에 저장해요.

세 가지 모두 **opt-in**이에요. 명확히 승인한 뒤에만
오리엔테이션이 만들어요.

### 스무 개의 일상 질문

언제든 OneToEight Agent에게 던질 수 있는, 자주 쓰는 질문
모음이에요. agent는 관련 장을 읽고, 이미 알고 있는 것을
바탕으로, 그 사람의 목소리와 전통으로 답해요.

핵심은 스무 개를 매일 다 답하는 게 **아니에요.** 여덟 가지
핵심을 꺼내고, 돌아보기를 이끌고, 호기심을 매일의 연습으로
바꾸는 질문 몇 개를 곁에 두는 거예요. 하나나 둘을 골라요.
나머지는 건너뛰어요. 한 주 동안 돌아가며 써요.

질문은 젊은 세대의 목소리로 쓰여 있어요. agent는 설교하듯
되받지 않아요. 질문을 던지고, 답할 공간을 열어 두고, 작은
실천 하나로 이어 줘요.

전체 질문 파일은
`essentials/00-introduction/lessons/prompts.md`에 있어요.
"생각할 거리"나 곱씹어 볼 질문, 막힌 곳을 뚫을 도움이
필요하다고 할 때 agent가 읽어요.

#### 방식별

| 방식 | 질문 |
|---|---|
| 자기 성찰 | #1, #3, #6, #7, #12, #15, #16, #20 |
| 활동 | #2, #9, #13, #14, #17, #19 |
| 비판적 사고 | #5, #8, #10, #18 |
| 일상 리추얼 | #11, #16, #20 |

#### 에너지별

| 에너지 | 추천 질문 |
|---|---|
| 피곤, 무기력 | #1, #20, #11 |
| 들떠 있음, 호기심 | #5, #10, #14 |
| 막막함, 무기력 | #3, #9, #15 |
| 생각하고 싶음 | #4, #6, #16, #18 |
| 움직이고 싶음 | #2, #9, #13, #17, #19 |

#### 핵심별 (모든 핵심이 최소 두 번씩 나와요)

| 핵심 | 이쪽으로 기우는 질문 |
|---|---|
| 침묵에 앉아 있는 능력 | #1, #7, #9, #12, #16 |
| 몸은 집이다 | #2, #9, #14, #19 |
| 실생활에 쓸모 있는 기술 | #8, #13, #14 |
| 디지털 자기방어 | #4, #8, #18 |
| 진짜 공동체 | #6, #15, #17 |
| Wi-Fi 없이도 되는 지식 | #3, #6, #8, #10, #11 |
| 자연을 처방하다 | #9, #19 |
| 시험을 거친 신념 | #1, #5, #7, #10, #16, #18 |

#### 무거운 질문 (드물게 써요)

**#1**, **#5**, **#10**, **#18**은 무거운 질문이에요. agent는
이 질문들을 먼저 꺼내지 않아요. 이름을 대고 직접 요청해야
해요. 무거운 질문을 요청했는데 그날은 아닌 것 같다고
판단되면, agent는 더 가벼운 대안을 다정하게 제안하고 이유를
설명할 수 있어요.

#### 스무 개

| # | 질문 | 방식 | 에너지 | 핵심 |
|---|----------|------|--------|------------|
| 1 | 내가 듣기 싫어하지만 꼭 답해야 할 질문 하나를 해 줘요. | 자기 성찰 | 피곤 / 무기력 | 여덟 가지 전부(특히 시험을 거친 신념, 침묵) |
| 2 | 쓸모 있게 불편하게 만들어 줄 10분짜리 과제를 줘요. | 활동 | 움직이고 싶음 | 몸, 침묵, 시험을 거친 신념 |
| 3 | 3일 전에 했는데 그 뒤로 안 하고 있는 일은 뭐예요? 왜 안 하고 있을까요? | 자기 성찰 | 막막함 / 무기력 | 자기 이해, Wi-Fi 없이도 되는 지식 |
| 4 | 내가 가장 약한 핵심 하나를 골라 줘요. 오늘 할 수 있는 가장 작은 연습은 뭐예요? | 비판적 사고 | 생각하고 싶음 | 여덟 가지 전부(진단용) |
| 5 | 내 마지막 결정에 반대해 봐요. 현명한 비판자라면 뭐라고 할까요? | 비판적 사고 | 들떠 있음 / 호기심 | Wi-Fi 없이도 되는 지식, 시험을 거친 신념 |
| 6 | 올해 배운 것 중 하나를 중학교 1학년에게 가르쳐야 한다면, 뭘 가르쳐야 할까요? | 자기 성찰 | 생각하고 싶음 | Wi-Fi 없이도 되는 지식, 진짜 공동체 |
| 7 | 내 삶에서 진짜로 하는 대신 연기하고 있는 곳은 어디예요? 연기 대신 진짜로 하고 있는 곳은 또 어디고요? | 자기 성찰 | 피곤 / 무기력 | 시험을 거친 신념, 침묵 |
| 8 | 지금 남에게 맡기고 있지만 내가 직접 길러야 할 것은 뭐예요? | 비판적 사고 | 생각하고 싶음 | 실생활에 쓸모 있는 기술, 디지털 자기방어, Wi-Fi 없이도 되는 지식 |
| 9 | 휴대폰도, 다른 사람도 필요 없는 30분짜리 활동을 줘요. | 활동 | 막막함 / 무기력 | 몸, 침묵, 자연을 처방하다 |
| 10 | 꼬치꼬치 캐물으면 변호하지 못할 믿음 하나는 뭐예요? 그래도 계속 믿어야 할까요? | 비판적 사고 | 들떠 있음 / 호기심 | 시험을 거친 신념, Wi-Fi 없이도 되는 지식 |
| 11 | 내가 예전에 알았는데 잊고 있었던 걸로 퀴즈를 내 줘요. | 일상 리추얼 | 피곤 / 무기력 | Wi-Fi 없이도 되는 지식 |
| 12 | 마지막으로 진짜 심심했던 게 언제였는지, 그 고요함 속에서 뭘 알아차렸는지 물어봐 줘요. | 자기 성찰 | 막막함 / 무기력 | 침묵, 몸 |
| 13 | 일주일 전에 시작해서 오늘 끝낼 수 있는 일 하나를 제안해 줘요. | 활동 | 움직이고 싶음 | 실생활에 쓸모 있는 기술, 시험을 거친 신념 |
| 14 | 아직 못 하는 실제 일 하나를 알려 줘요. 밥 차려 먹기, 펑크 고치기, 이력서 쓰기, 타이어 교체하기 같은 거요. | 활동 | 들떠 있음 / 호기심 | 실생활에 쓸모 있는 기술, 몸 |
| 15 | 내 삶에서 새벽 2시에 달려와 줄 사람은 누구예요? 안 올 사람은? 왜일까요? | 자기 성찰 | 막막함 / 무기력 | 진짜 공동체 |
| 16 | 오늘 시간을 어떻게 썼는지와 어떻게 쓰고 싶다고 했는지를 비교해 줘요. 틈은 어디예요? | 일상 리추얼 | 생각하고 싶음 | 시험을 거친 신념, 침묵 |
| 17 | 한동안 제대로 이야기하지 못한 사람에게 쓸 대화 시작 문장 하나를 줘요. | 활동 | 움직이고 싶음 | 진짜 공동체 |
| 18 | 휴대폰에서 세 개만 남기고 앱을 다 지운다면, 어떤 세 개를 남겨야 하고 왜예요? | 비판적 사고 | 생각하고 싶음 | 디지털 자기방어, 시험을 거친 신념 |
| 19 | 15분 동안 바깥으로 나가요. 뭘 봐야 하고, 뭘 들어야 하고, 뭘 알아차려야 할까요? | 활동 | 움직이고 싶음 | 자연을 처방하다, 몸, 침묵 |
| 20 | 같이 하루를 마무리해요. 있었던 일 세 가지, 알아차린 것 세 가지, 고마운 것 한 가지. | 일상 리추얼 | 피곤 / 무기력 | 여덟 가지 전부(하루 마무리) |

#### agent가 이 질문들을 쓰는 방식

agent는 질문을 요청할 때마다
`essentials/00-introduction/lessons/prompts.md`를 읽어요.
질문을 그대로 **붙여 넣지** 않아요. 하나를 가리키고, 함께
읽자고 하고, 답할 공간을 열어 둬요. 세 개를 연달아 묻는 일은
없어요.

**순차** 전달에서는 지금 다루는 핵심 주변으로 질문이
자연스럽게 모여요. **무작위**에서는 그 순간에 맞는 질문을
골라요. 두 방식 모두에서 여덟 가지 핵심을 다 쓸 수 있어요.

---

## 일상 리추얼

agent가 돌리는 모든 리추얼을 한눈에 보여 주는 지도예요.
무엇인지, 언제 도는지, 어디로 도착하는지, 자세한 설명이 어디
있는지요.

| 리추얼 | 언제 | 채널 | 무슨 일이 일어나요 |
|---|---|---|---|
| **아침의 1분** | 매일, 정해 둔 시간(기본 오전 6시) | Telegram 또는 WhatsApp, **음성 메시지 + 텍스트** | 그날의 오디오 계획이에요. 지금 다루는 핵심에서 작은 실천 하나에 집중해요. |
| **오후 체크인** | 매일, 정해 둔 시간(기본 오후 5시) | Telegram 또는 WhatsApp, **텍스트만** | 하루가 어땠는지 돌아보기, 내일 계획, 밤새 곱씹어 볼 질문 하나. |
| **계획 세션** | 매일 잠들기 전, 정해 둔 시간(기본 오후 9시) | Telegram 또는 WhatsApp, **텍스트만** | agent가 내일 계획(학교 과제, 숙제 마감, 이번 주 핵심, 실제로 해 볼 일 하나) 초안을 써요. 직접 고치고, 로컬에 저장돼요. |
| **핵심 요약** | 요청할 때마다, 언제든 | Telegram 또는 WhatsApp, **음성 메시지** | 한 핵심을 3~5분 분량으로 소리 내어 요약 + 짧은 핵심 포인트 목록. |
| **핵심 레슨** | 요청할 때마다, 언제든 | here.now, **채팅에 HTML 페이지 링크** | 한 핵심을 다룬 세 페이지 레슨이에요. 출처를 밝힌 자료, 핵심 인용문, 짧은 퀴즈가 있어요. |
| **핵심 시** | 요청할 때마다, 언제든 | Telegram 또는 WhatsApp, **음성 메시지 + 텍스트** | 핵심을 다룬 라임 있는 낭독 시를 소리 내어 읽고, 아래에 텍스트를 붙여 줘요. |
| **핵심 노래** | 요청할 때마다, 언제든 | Telegram 또는 WhatsApp, **MP3 음성 메시지 + 텍스트** | agent가 핵심에 대한 시를 쓰고, OpenRouter의 Google Lyria 3로 진짜 노래로 만들어요. 곡당 약 $0.08이에요. 실행 전에 확인해요. |
| **핵심 뮤직비디오** | 요청할 때마다, 언제든 | here.now, **채팅에 MP4 영상 링크** | 위의 노래에 스토리보드 이미지를 오디오와 이어 붙이고, 원하면 시 텍스트를 얹어요. 모두 합쳐 약 $0.35예요. 실행 전에 확인해요. |

**하루.** 아침의 1분이 하루를 열고, 체크인이 하루를 닫고,
계획 세션이 잠들기 전에 내일을 그려요. 요청형 포맷 세 가지
(요약 / 레슨 / 시)는 아침의 1분이 1분 안에 담지 못하는 만큼
더 깊이 배우고 싶을 때 언제든 있어요.

**코드는 여기에.** 각 줄은 repo의 skill로 이어져요:

| 리추얼 | skill 경로 |
|---|---|
| 아침의 1분 | `skills/hermes/morning-minute/` |
| 오후 체크인 | `skills/profile/afternoon-checkin/` |
| 계획 세션 | `skills/profile/planning-session/` |
| 요약, 레슨, 시, 노래, 뮤직비디오 | `skills/profile/essential-deep-dives/` (노래와 뮤직비디오는 `skills/creative/openrouter-lyria-music/`와 `skills/creative/poem-song-video-studio/`를 써요) |

**동의.** cron 기반 리추얼 세 가지(아침의 1분, 체크인, 계획
세션)는 온보딩에서 본인이나 부모님이 승인하기 전까지 꺼져
있어요. 요청형 포맷 다섯 가지(요약, 레슨, 시, 노래,
뮤직비디오)는 바로 쓸 수 있어요. 말하기만 하면 되거든요. 유료 포맷 두
가지(노래와 뮤직비디오, Lyria 3 + 스토리보드 이미지)는 요청할
때마다 비용을 확인해야 해요. 정확한 opt-in 흐름은 [설정 흐름 →
백그라운드에서 돌아가는 것들](#백그라운드에서-돌아가는-것들)을
봐요.

**노래와 뮤직비디오 skill.** 유료 포맷 두 가지는 이미 있는
skill 두 개를 다시 써요:

| 포맷 | 바탕 skill | `essential-deep-dives` 위에 더하는 것 |
|---|---|---|
| **핵심 노래** | `skills/creative/openrouter-lyria-music/` | 시 가사 → Google Lyria 3로 MP3 오디오(곡당 약 $0.08). |
| **핵심 뮤직비디오** | `skills/creative/poem-song-video-studio/` | 노래 + 스토리보드 이미지 약 8장 + ffmpeg → MP4(총 약 $0.35). |

두 skill 모두 Lyria 3 모델 노트와 스크립트, cost guard까지
갖춰 repo에 이미 있어요. 요청하면 agent가 바탕 skill을
불러와요.

**바꾸는 방법.** 오리엔테이션에서 각 cron 리추얼의 시간과
timezone, 요일 규칙을 정해요. 세 가지 모두 나중에
`cronjob(action="...")`로 멈추거나 다시 시작하거나 지울 수
있어요. 요청형 포맷은 고른 전통을 알아서 따르고, 목소리와
길이는 이미 정한 아침의 1분 Piper 보이스를 물려받아요.

---

## 돌리는 데 드는 비용

OneToEight Agent는 **사용한 만큼 내는 방식**이에요. 구독이
없어요. OpenRouter 계정에 크레딧을 채워 두면, agent가 거기서
꺼내 써요.

| 비용 | 금액 | 메모 |
|---|---|---|
| **첫 달** | **약 $20** | 설정에 더해, 적응하는 동안의 첫 달 실제 사용량까지 |
| **이후** | **월 $5~$10** | 저렴한 모델로 가볍게 매일 쓰는 기준 |

이 profile은 일상적인 작업에 저렴한 모델을 써요:

- **DeepSeek V4 Flash**: 매일의 채팅과 레슨에 쓰는 기본 모델이에요.
- **Google Gemini 3.7 Flash**: 짧은 작업에 쓰는 빠른 fallback이에요.
- **오픈소스 모델**(무료 또는 거의 무료 tier): frontier 모델까지 필요 없는 기본적이고 양이 많은 작업에 써요.

무료 tier는 달마다 돌아가기 때문에 목록이 바뀌어요. 최신 무료
모델 목록은 <https://openrouter.ai/openrouter/free>에서 봐요.
이 profile은 저렴한 선택을 기본으로 하고, 정말 필요할 때만
더 큰 모델을 불러요.

---

## 튜토리얼

단계별 안내가 더 좋다면? 튜토리얼 허브에 모든 설정 페이지가
모여 있어요:

- **build path**: 직접 만들어 보면서 배우는 일곱 페이지예요. agent를 하나씩 완성해 가고, 따라 들을 오디오도 있어요. <https://gladtobe.here.now/build-path/>에서 시작해요.
- **온보딩 커리큘럼**: 일곱 페이지예요. 처음 설치부터 채팅에 연결된 agent까지, 설치 과정을 다뤄요.
- **워크스루 시트**: 설정을 한 장에 담았어요. 세 가지 언어로 제공돼요.

<https://gladtobe.here.now/hub-tutorials.html>에서 허브를 열어요.
아래 설정 흐름은 같은 내용을 텍스트로, 한 단계씩 다뤄요.

---

## 설정 흐름

### 1: 사전 준비 (한 번만, 컴퓨터에서)

필요한 것:

- **Hermes Agent** 설치. 빠른 확인: `hermes --version`. [설치 가이드](https://hermes-agent.nousresearch.com/docs)를 봐요.
- **Python 3.10~3.13**(Windows Store의 가짜 버전이 아니라 실제 설치본). `python --version`.
- **Piper TTS.** 제대로 작동하는 설치본이 필요해요. 아래 2단계를 봐요.
- **ffmpeg**(WAV → OGG 변환용). `ffmpeg -version`.
- **모델 provider key.** 이 profile의 기본값은 `openrouter + deepseek-v4-flash`예요. key 하나면 무료 tier와 멀티모달(이미지, 오디오) 모델까지, 넓은 모델 목록을 열 수 있어요. <https://openrouter.ai/>에서 무료로 가입하고, `hermes setup`으로 key를 넣어요. fallback은 OpenCode Go예요.
- **Jina AI 무료 API key**(웹 검색용). <https://jina.ai/>에서 무료로 가입해요. 신용카드가 필요 없어요. 무료 tier로도 매일 쓰기에 충분해요.
- **Telegram bot**(추천) 또는 WhatsApp bridge. Telegram이 훨씬 쉬워요. 4단계를 봐요.

### 2: 프로필 압축 풀기 (한 번만)

profile은 `onetoeight-agent-ko.zip` zip 파일로 받아요.
`~/.hermes/profiles/` 안에서 풀면
`~/.hermes/profiles/onetoeight-agent/`가 돼요. 그다음:

```bash
mkdir -p ~/.hermes/profiles
# onetoeight-agent-ko.zip을 이 폴더에 압축 풀기
hermes profile use onetoeight-agent
hermes chat
```

> **참고:** profile 디렉터리 이름은 `onetoeight`가 아니라
> `onetoeight-agent`예요. profile 경로를 쓰는 명령은 그에 맞게
> 고쳐 써요.

나중에 업데이트하려면: 새 zip을 내려받아 임시 폴더에 압축을
풀어요. 새 파일을 복사해 넣되, `memories/` 폴더와 기록된
세션은 **지우면 안 돼요.** 폴더 루트의 `LOCALE.md`가 어느
버전에서 온 것인지 기록해요.

### 3: 첫 채팅 → 오리엔테이션

첫 채팅에서 agent가 이렇게 시작해요:

> "시작하기 전에, 설정을 하나씩 안내해 줄까요? 몇 분이면
> tool과 memory, 아침의 1분까지 원하는 대로 맞출 수 있어요.
> 아니면 건너뛰고 바로 시작해도 돼요."

좋다고 말하면 돼요(또는 언제든 *"profile 설정을 도와줘"*라고
물어봐도 돼요). 그러면 `agent-onboarding` skill이 실행돼요.

### 4: 오리엔테이션 (동의 기반)

오리엔테이션은 대화 방식으로 진행돼요. 관련된 질문을 한
묶음씩 묻고, **인증 정보가 필요한 단계마다 멈춰요.** 채팅에서
key나 token을 절대 묻지 않아요.

무엇을 다루는지, 순서대로 보여 줄게요:

| 단계 | 무슨 일이 일어나요 | 어디에 넣어요 |
|---|---|---|
| 1. 정체성 | 이름(본인, 배우는 사람, agent), 답변 스타일, 가이드와 레슨, 메시지에 쓸 언어 | profile memory에 저장 |
| 2. 프로필과 생활 | 나이, 사는 곳, 함께 사는 사람, 한 주의 흐름, 관심사 3가지, 집중 목표, 친구 관계, 걸림돌, 다루지 않을 주제 | profile memory에 저장 |
| 3. 전통 | 크리스천, 유니버설, 또는 나만의 전통 | profile memory에 저장 |
| 4. Piper 설치 + 목소리 | Piper가 작동하는지 확인하고, 목소리를 고르고, voice model을 내려받아요 | voice model은 `piper-voices/`에 |
| 5. Jina API key | 무료로 가입하고 `.env`에 추가하면, agent가 실제 검색으로 확인해요 | `.env`의 `JINA_API_KEY=` |
| 6. 전달 채널 | Telegram 또는 WhatsApp bot 인증 정보 | `.env`의 `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` |
| 7. 여덟 가지 핵심 가이드 | 레슨 MD 파일이 `essentials/01..08/lessons/`에 있는지 확인하고, 고른 언어의 가이드 에디션을 안내해요(`essentials/guide-editions.md`) | repo 안의 파일 |
| 8. Memory | Mnemosyne 추천(로컬 우선, 외부 계정 없음) | `hermes memory setup` |
| 9. 아침의 1분 일정 | 몇 시, 어느 timezone, 무슨 요일 | cron job으로 만들어져요 |
| 10. 오후 체크인 일정 | 몇 시, 어느 timezone, 무슨 요일 | cron job으로 만들어져요 |
| 11. 계획 세션 일정 | 몇 시(기본 오후 9시), 어느 timezone, 무슨 요일 | cron job으로 만들어져요 |
| 12. Token Router (선택) | agent에게 보이는 도구 범위를 좁히는 플러그인 | `config.yaml`의 `plugins.enabled` |

끝나면 agent가 **Proposed setup** 요약을 보여 주고, 명확하게
승인하기 전까지는 아무것도 적용하지 않아요.

### 5: 각 부분 확인하기

첫 예약 아침의 1분이 돌기 전에, 구성 요소마다 확인해요:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer jina_x...xxxx" \
  "https://s.jina.ai/https://hermes-agent.nousresearch.com/docs"
# → clean snippet of the docs page means it works

# Telegram bot works (sends a test message)
# Use the test script in Step 3 of the Telegram setup below.
# If you get "chat not found", you must first send any message to your bot in Telegram.

# Guide MD files are present
for d in essentials/*/lessons/; do echo "--- $d ---"; ls "$d"; done

# Mnemosyne is configured
hermes memory status

# Cron jobs are queued
cronjob(action="list")
```

**플랫폼별 Piper binary 위치:**

| 플랫폼 | 일반적인 경로 |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (직접 설치) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, 그다음 PATH에서 `piper` 실행 |

오리엔테이션이 Piper를 찾아봐요. PATH에 있으면 바로 찾아내고,
특이한 곳에 설치돼 있으면 경로를 물어봐요.

**voice model 저장 위치**(한 번 받아 두면 계속 써요):

| 목소리 | 로케일 | Hugging Face path |
|---|---|---|
| `en_US-joe-medium` | 미국 남성 | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | 미국 여성 | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | 영국 남성 | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | 영국 여성 | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | 호주 여성 | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

내려받는 방법(예: Linux에서 Joe):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: 첫 예약 실행

아침의 1분은 사는 곳의 timezone 기준으로 다음 예약 시간에 돌아요.
오디오를 만들고(Piper), 공개 URL을 받으려고 here.now에
올린 다음, 그 오디오를 multipart upload로 Telegram에 바로
보내요. `MEDIA:<url>` 링크로는 **보내지 않아요**(here.now의
Cloudflare 설정이 Telegram의 파일 가져오기 bot을 막아요).
체크인은 다음 예약된 오후 시간에 돌아요.

### 7: 일상 운영

매일 터미널로 agent와 만나지는 않아요. Telegram이나 WhatsApp
채팅이 **바로** 매일의 접점이에요:

- **아침의 1분**이 음성 메시지 + 텍스트 계획으로 도착해요.
- **오후 체크인**이 텍스트로 도착해요.
- **계획 세션**이 잠들기 전에 텍스트로 도착해요. agent가 내일
  계획(학교 과제, 숙제 마감, 이번 주 핵심, 실제로 해 볼 일
  하나) 초안을 쓰면 직접 고치고, 로컬에 저장돼요.
  `skills/profile/planning-session/`을 봐요.
- **체크인에 답장해요.** 하루가 어땠는지 한 줄이면 충분해요.
  agent가 요약해서 저장해 두고, 내일 아침의 1분에서 다시
  꺼내 써요.
- **언제든 질문해요.** "시험을 거친 신념은 실제로 어떤
  모습이에요?" "진짜 공동체는 어떻게 찾아요?" agent가 가이드를
  읽고 가르쳐 줘요.

#### 핵심을 더 깊이 배우는 방법 (요청할 때)

매일의 리듬 밖에서도, 어떤 핵심이든 더 깊이 배우는 포맷을
요청할 수 있어요. 모두 `essential-deep-dives` skill이
맡아요(`skills/profile/essential-deep-dives/` 참고). 말하기만
하면 돼요:

- **핵심 요약**: 한 핵심의 핵심 포인트를 쉬운 말로 정리하고,
  agent가 만든 3~5분 **음성 메시지**(Piper)를 채팅에 넣어
  줘요. 산책하거나 집안일을 하면서 들을 수 있어요.
- **핵심 레슨**: HTML 페이지로 만든 아름다운 **세 페이지
  레슨**을 집에서 쓰는 **here.now** 계정에 발행해요. **출처를
  밝힌 자료**(가이드에 없는 내용이 필요하면 Jina API로
  찾아요), **핵심 인용문**, 페이지에서 직접 푸는 짧은
  **퀴즈**로 가르쳐요. agent가 채팅으로 링크를 보내 줘요.
- **핵심 시**: 핵심을 다룬 라임 있는 **낭독 시**를 음성
  메시지로 읽어 주고, 아래에 텍스트를 붙여 줘서 따라 읽을 수
  있어요.
- **핵심 노래**: agent가 핵심에 대한 오리지널 시를 쓰고,
  OpenRouter의 `google/lyria-3-pro-preview`로 진짜 노래(MP3)로
  만들어요(곡당 약 $0.08). 음성 메시지가 채팅에서 재생되고,
  시 텍스트가 이어져요. 실행 전에 비용을 확인해요.
- **핵심 뮤직비디오**: 위의 노래에 스토리보드 이미지 프레임을
  오디오와 이어 붙이고, 원하면 시 텍스트를 얹어요(노래 +
  스토리보드 이미지 + ffmpeg 조립까지 모두 약 $0.35). MP4로
  here.now에 발행하고, 링크를 채팅에 보내 줘요. 실행 전에
  비용을 확인해요.

무엇을 만들든 agent는 먼저 가이드를 읽고, 고른 전통에 따라
나누고, 프로필에 맞춰 줘요. curriculum skill과 같은 규칙이에요.

### 8: 유지 관리

가끔씩:

- `hermes update`: 표준 Hermes skill library를 profile로
  가져와요(curated skill은 절대 덮어쓰지 않아요).
- `git -C ~/.hermes/profiles/onetoeight-agent pull`: 가이드와
  skill의 upstream 개선 사항을 받아요.
- `cronjob(action="list")`: 두 job이 아직 예약돼 있는지 확인해요.

---

## `.env`에 설정하는 것들

이 profile에는 모든 변수를 보여 주는 `.env.example`이 들어
있어요. 실제로 채우는 것은 이거예요.

### 필수 (모든 설정)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Telegram 전달에 필수

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Telegram 설정 참고:** @BotFather로 bot을 만든 뒤에는, agent가
> 메시지를 보내기 전에 **bot에게 먼저 메시지를 하나 보내야
> 해요**(예: `/start`). 한 번도 메시지를 받은 적 없는 bot은
> 전송에 조용히 실패해요.

chat ID를 찾으려면: Telegram에서 `@userinfobot`에게 메시지를
보내면 숫자 ID를 답해 줘요.

### 오디오(아침의 1분)에 필수

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **here.now 참고:** 오디오는 here.now의 publish API로 올려서
> 공개 URL을 받아요. 이 URL은 multipart upload로 Telegram에
> 보내기 때문에 DRIVE_ID가 **필요 없어요**. 예전 문서나 예시에서
> `HERENOW_DRIVE_ID`를 봤다면, 그건 legacy이고 지금 오디오 전달
> 흐름에서는 쓰지 않아요.

### 선택 integration

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### env 변수가 **아닌** 것들

- **voice model 경로**: profile memory에 저장돼요. env가
  아니에요. 경로는 컴퓨터마다 달라요.
- **cron 일정**: `cronjob(action="create", ...)`로 만들고,
  cron registry에 저장돼요. env가 아니에요.
- **Piper binary 경로**: profile memory에 저장돼요.
- **Mnemosyne**: 로컬 우선이라 key가 필요 없어요.

---

## repo에 들어 있는 것

```
onetoeight-agent/
├── README.md                              ← 이 파일
├── SOUL.md                                ← persona와 운영 목소리
├── AGENTS.md                              ← 운영 원칙
├── profile.yaml                           ← profile descriptor
├── config.yaml                            ← Hermes runtime config
├── .env.example                           ← 모든 변수와 설명
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← 여덟 가지 핵심 원본 콘텐츠
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← 서론 (크리스천 에디션)
│   │   └── universal.md                   ← 서론 (유니버설 에디션)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← 이 핵심에 대한 agent의 가르침 노트
│   │   ├── lessons/
│   │   │   ├── README.md                 ← 파일 스키마
│   │   │   ├── christian.md               ← 1장 (크리스천 에디션)
│   │   │   └── universal.md               ← 1장 (유니버설 에디션)
│   │   └── activities/README.md
│   ├── 02-body/        (같은 구조)
│   ├── 03-skills/      (같은 구조)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← 시험을 거친 신념 + 크리스천 맞춤
│   │   │   └── universal.md               ← 시험을 거친 신념 + 세속 맞춤
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← 열 개 언어로 나온 온라인 가이드
│
├── skills/
│   ├── hermes/                            ← Hermes가 고른 curated skill
│   │   ├── agent-onboarding/  ← 오리엔테이션
│   │   ├── morning-minute/                ← 매일의 계획 + 오디오
│   │   ├── hermes-mnemosyne/              ← memory provider
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← 이 profile 자체의 skill
│       ├── afternoon-checkin/           ← 오후 돌아보기
│       ├── eight-essentials-curriculum/   ← 가이드에서 가르치기
│       ├── essential-deep-dives/          ← 요약, 레슨, 시 포맷
│       └── setup-walkthrough/            ← Piper, Jina, 채널 설정
│
├── plugins/hermes-token-router/           ← 선택형 도구 범위 축소 플러그인
├── memories/                              ← 일반 운영 관행 씨앗
└── skins/onetoeight.yaml                 ← 색 테마
```

> **표준 Hermes skill**(web, terminal, github, creative 등)은
> `hermes update`가 가져와요. 이 repo의 일부가 아니고, 여기가
> 아니라 표준 library에 있어요.

---

## 설정 레퍼런스

### 모델 provider (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

`provider`와 `default`를 바꾸면 모델을 바꿀 수 있어요.
OpenRouter가 기본인 이유는 key 하나로 가장 넓은 목록을 열 수
있어서예요: 무료 모델과 멀티모달(이미지, 오디오) 모델까지,
provider를 갈아타지 않고요. fallback chain은 기본 provider를
쓸 수 없을 때만 돌아가요.

### Toolset (`config.yaml`)

모든 CLI toolset은 **기본으로 켜져 있어요**. 오리엔테이션에서
하나씩 검토해요. 직접 꺼두려면:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

`tts` toolset은 아침의 1분을 위해 켜 둬야 해요.

### Cron job

오리엔테이션에서 만들어요. 직접 관리하려면:

```python
# List
cronjob(action="list")

# Create Morning Minute (UTC schedule — 6am AEST = 20:00 UTC)
cronjob(
    action="create",
    schedule="0 20 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute.
    Use the morning-minute skill. The student's tradition is
    <christian/universal>. Generate the day's plan, run Piper TTS,
    upload to here.now, deliver via multipart upload to Telegram.
    Do not write memories. Deliver only the final voice + text.""",
    skills=["morning-minute"],
    deliver="telegram",
)

# Weekdays only Morning Minute (6am, Mon–Fri)
cronjob(
    action="create",
    schedule="0 20 * * 1-5",
    name="Morning Minute",
    ...
)

# Pause without deleting
cronjob(action="pause", job_id="<id>")

# Resume
cronjob(action="resume", job_id="<id>")

# Remove (requires approval — deletes the schedule permanently)
cronjob(action="remove", job_id="<id>")
```

아침의 1분 cron 계약 전체는
`skills/hermes/morning-minute/SKILL.md`에 있어요.

> **cron 전달:** TUI/CLI 세션에는 실시간 전달 채널이 없어요.
> cron이 돌 때 알림을 받고 싶다면 만들 때
> `deliver="telegram"`(또는 `deliver="all"`)을 설정해요.
> 그러지 않으면 출력이 로컬에 저장되고
> `cronjob(action="list")`로 볼 수 있어요.

---

## 자주 겪는 문제

| 증상 | 흔한 원인 | 해결 |
|---|---|---|
| Piper가 로드되지 않아요 | voice model 경로가 틀렸거나, 내려받지 않았어요 | 오리엔테이션의 Piper 단계를 다시 실행해요 |
| 아침의 1분 오디오가 무음이거나 잘려요 | TTS 입력 텍스트가 잘렸어요 | 합성 전에 텍스트 파일이 완전한지 확인해요 |
| Telegram 전송이 "chat not found"로 실패해요 | bot이 메시지를 한 번도 받은 적 없어요 | Telegram을 열어 bot을 찾고 `/start`를 보내요 |
| Telegram 오디오가 재생되지 않아요 | here.now URL과 `MEDIA:<url>`을 함께 썼어요 | `sendVoice`로 multipart upload를 써요(skill이 처리해요) |
| cron이 엉뚱한 시간에 돌아요 | UTC 혼동 | cron은 UTC로 저장돼요. 한국 시간 오전 6시 = `0 21 * * *`. 시드니 오전 6시 = `0 20 * * *` |
| 매일이라고 했는데 평일에만 돌아요 | cron 형식이 틀렸어요 | `0 6 * * *` = 매일. `0 6 * * 1-5` = 월~금 |
| Jina 검색이 아무것도 못 찾아요 | `.env`에 key가 없거나 틀렸어요 | `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"`로 테스트해요 |
| agent가 다른 전통의 내용을 줘요 | memory에 전통이 없어요 | 오리엔테이션의 전통 단계를 다시 실행해요 |
| 레슨 파일을 읽지 않아요 | `.christian.md` 또는 `.universal.md` 접미사가 없어요 | `ls essentials/<NN>/lessons/`로 확인해요. 파일 이름 접미사가 맞아야 해요 |

---

## Token Router 플러그인 (선택)

Token Router는 선택형 Hermes 플러그인으로, agent에게 보이는
**도구 범위**를 좁혀요. 배우는 사람이 보는 게 아니라 agent가
보는 범위예요. 켜면 agent가 기본으로 볼 수 있는 tool 수가
줄어서, 토큰 사용량을 아끼고 agent가 여덟 가지 핵심 작업에
집중하게 도와줘요.

배우는 사람에게서 기능을 숨기지는 **않아요.** 무엇이든 물어볼
수 있고, router는 agent가 자동으로 고르는 선택지만 줄여 줘요.

이럴 때 켜요:
- agent가 코드나 데이터 분석보다 가르치는 일에 집중하길 원해요.
- 토큰 사용량이 신경 쓰여요.

이럴 때는 꺼 둬요:
- 배우는 사람(또는 부모님)이 모든 도구를 쓰길 원해요.

켜려면: `hermes plugins enable hermes-token-router`
(`hermes profile use onetoeight-agent` 실행 후에 해요).

---

## 라이선스

MIT, `LICENSE`를 봐요.

OneToEight Agent persona는 이 프로젝트를 위해 새로 쓴 오리지널
어시스턴트 원형이에요. 여덟 가지 핵심 가이드 콘텐츠는 onetoeight
*Eight Essentials* Universal Edition V.3.0.0에서 왔고, 이 profile
안에서 쓰도록 허락을 받아 포함했어요.
