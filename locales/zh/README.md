# OneToEight Agent：总览与设置流程

**OneToEight Agent** 是一款个性化 AI 助理，基于
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) 搭建，
面向正在学习把**八大要素**融入日常生活的年轻人。
它是一位温和的导师，每天运行一套由音频计划、
反思问候和小行动组成的日常节奏，内容都来自随仓库
一起提供的八大要素指南。

这份 README 是总览，也是让 Agent 从头到尾运转起来的
设置流程。先读一遍，然后照着步骤走。

> **两种进入方式。**走 **build path**，一块一块地把 Agent
> 搭起来：每周一个能力、一份收获，配有音频可以跟学。
> 或者，用下面的设置流程直接安装。
>
> **开始 build path：<https://gladtobe.here.now/build-path/>**

> 阅读语言: **中文** · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Filipino](README.tl.md) · [Español](README.es.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## 这是什么产品

年轻人学会八大要素的最好方式，是**每天做一件小事**，
坚持数周乃至数月，而不是读一本书。OneToEight
Agent 的存在，就是让这个日常节奏持续下去：

- 一个 **晨间一分钟**（Morning Minute）会在学生选定的
  时间出现在聊天里（Telegram 或 WhatsApp）。它是当天
  简短的音频计划，外加文字。
- 一个 **午后问候**（Afternoon Check-In）会在下午到达。
  它是一条简短的文字消息：今天过得怎么样、接下来做
  什么、一个留到夜里慢慢想的问题。
- 一个 **睡前规划**（Planning Session）会在睡前到达。
  它把明天安排出来：学校任务、作业截止日期、这周在学
  的要素、一件想做的现实中的事。Agent 起草计划，学生
  修改，保存在本地。没有 App，没有账号，没有云端同步。
- Agent 从存在仓库里的**八大要素指南**教学
  （`essentials/01..08/lessons/*.md`），按学生选择的
  传统分支讲授。
- 这份指南还以**十种语言**发布，可以在线阅读，也可以
  下载离线包，在没有网络时使用。见
  `essentials/guide-editions.md`。

Agent 不会说教。它用提问把学生心里的智慧引出来，
温柔地托住节奏，在学生掉队时帮他们重新开始，
不责备。

### 两种传统，或者你自己的

每位学生在入门引导时会选择一种。或者告诉 Agent
你的传统，它会把那种传统构建进来。Agent 始终停留在
选定的传统里，从不混合传统：

- **基督教**：以圣经为根基。晨间一分钟每天早上包含
  一节圣经经文，自然地读出来。问候把一天放进活的
  信仰之中。
- **通用（世俗）**：尊重各种智慧传统，不带教义。
  晨间一分钟包含一位思想家的短反思或问题。问候把
  一天放进反思、感恩与意向之中。

学生之后可以更换传统，但从那一刻起，课程按新传统
分支。

### 两种推送顺序

每位学生还要选择八大要素的推送方式：

- **顺序**（默认）：按要素一到八的顺序依次进行。
  这是最连贯的方式，也是这本指南写作时预设的顺序。
  推荐给新学生。
- **随机**：任何一天抽取任何一个要素，贴合学生当天
  看起来最需要的（间隔最久、最近卡住的地方、当天
  的精力）。每个晨间一分钟都以所选要素的知识小结
  开场，再加一个小活动。最适合已经知道自己需要
  什么的学生。

两种模式下，**八大要素最终都会被覆盖**。学生之后
可以通过更新 `essentials_order` 记忆键来切换，不需要
重新做入门引导。

### 八大要素（按指南的教学顺序）

1. **静默**：安静地坐着，独自与自己的想法待在一起
2. **身体**：睡眠、食物、水、运动、阳光
3. **技能**：实用的现实能力（做饭、修理、动手做、做预算）
4. **数字自卫**：隐私、注意力、身份素养
5. **真实的群体**：知道你的名字的人
6. **没有Wi-Fi的知识**：拥有它，而不是租用它
7. **自然**：像处方一样的户外时间，不容商量
8. **经过考验的信念**：属于你自己的，压力之下依然站得住

---

## 如何运作

### 每日循环

```
06:00  晨间一分钟   Piper TTS 音频 + 文本 → Telegram 或 WhatsApp
        ↓
白天   学生完成一个小行动
        ↓
17:00  午后问候     纯文本 → Telegram 或 WhatsApp
        ↓
21:00  睡前规划     纯文本 → Telegram 或 WhatsApp
       Agent 起草明天的计划 → 学生修改 → 保存在本地
        ↓
        睡觉
        ↓
        重复
```

Agent 会强化这个循环，但不唠叨。错过的日子会温和地
重新开始。不责备。不说教。

**关于时间表：**上面列出的时间都在学生所在的本地时区。
cron 守护进程以 **UTC** 存储时间表。如果你选择北京时间
（UTC+8）早上 6 点，cron 会存成 `0 22 * * *`（22:00
UTC）。时间表始终是“你所在时区的时间”，转换成 UTC
是自动的。

### Agent 在每个时刻的工作

| 时机 | Agent 做什么 |
|---|---|
| 新 profile 上的第一次聊天 | 用自己的声音，简短地提供入门引导 |
| 学生说“帮我设置好” | 运行 `agent-onboarding`（需经同意、分阶段进行） |
| 学生提问 | 读取相关的 `essentials/<NN-name>/lessons/*.md`，综合后讲解 |
| 晨间一分钟 cron 触发 | 生成当天的计划，运行 Piper，上传，直接推送 |
| 问候 cron 触发 | 读取最近一次晨间一分钟，起草简短的反思，以文本推送 |
| 睡前规划 cron 触发 | 起草明天的计划（学校任务、作业截止日期、本周要素、一件现实中的事），学生修改，保存在本地 |
| 学生要求更深入的学习 | 使用 `eight-essentials-curriculum` 技能：读取指南，从中教学 |

### 后台运行的内容

三个 cron 任务，在学生在入门引导中批准之前全部关闭：

1. **晨间一分钟**：在学生时区的选定时间触发，每天
   （或者只在工作日）。生成音频和文本，推送到
   Telegram 或 WhatsApp。
2. **午后问候**：在选定的下午时间触发，运行日规则与
   晨间一分钟相同。发送一条简短的文字消息。
3. **睡前规划**：在睡前触发（默认晚上 9 点），同样的
   运行日规则。起草明天的计划供学生修改，然后保存在
   本地。

三个都**需要主动开启**，只有得到明确批准后，入门引导
才会创建它们。

### 二十个每日提问

一个小问题库，装着年轻人随时可以向 OneToEight
Agent 提出的常用提问。Agent 会阅读相关的指南章节，
参考它已经了解的学生情况，用学生自己的语气、在学生
的传统里回答。

重点**不是**每天把二十个都问一遍。重点是有一小套
常用提问，能让要素浮现出来、引出反思，把好奇心变成
每天的习惯。挑一两个，跳过其余的，一周里轮换着来。

这些提问是用年轻人的语气写的。Agent 不会反过来讲
大道理。它提出问题，为回答留出空间，再跟进一步
小行动。

完整的提问文件在
`essentials/00-introduction/lessons/prompts.md`。当学生
想要“一个可以想一想的东西”、一个可以慢慢琢磨的
问题，或者卡住时想找点帮助，Agent 就会读取它。

#### 按方式

| 方式 | 提问 |
|---|---|
| 自我反思 | #1, #3, #6, #7, #12, #15, #16, #20 |
| 活动 | #2, #9, #13, #14, #17, #19 |
| 批判性思考 | #5, #8, #10, #18 |
| 每日仪式 | #11, #16, #20 |

#### 按状态

| 状态 | 建议的提问 |
|---|---|
| 疲惫、低落 | #1, #20, #11 |
| 亢奋、好奇 | #5, #10, #14 |
| 卡住或无感 | #3, #9, #15 |
| 想思考 | #4, #6, #16, #18 |
| 想行动 | #2, #9, #13, #17, #19 |

#### 按要素（每个要素至少出现两次）

| 要素 | 偏向它的提问 |
|---|---|
| 静默 | #1, #7, #9, #12, #16 |
| 身体 | #2, #9, #14, #19 |
| 技能 | #8, #13, #14 |
| 数字自卫 | #4, #8, #18 |
| 真实的群体 | #6, #15, #17 |
| 没有Wi-Fi的知识 | #3, #6, #8, #10, #11 |
| 自然 | #9, #19 |
| 经过考验的信念 | #1, #5, #7, #10, #16, #18 |

#### 沉重的提问（少用）

提问 **#1**、**#5**、**#10** 和 **#18** 比较沉重。
Agent 从不主动推这些。必须由学生自己点名提出。如果
学生提出一个沉重的问题，而 Agent 判断今天不合适，
它可以温和地提供一个更轻的替代，并解释原因。

#### 二十个提问

| # | 问题 | 方式 | 状态 | 要素 |
|---|----------|------|--------|------------|
| 1 | 问我一个我大概不想回答、但应该回答的问题。 | 自我反思 | 疲惫／低落 | 全部八项（尤其经过考验的信念、静默） |
| 2 | 给我一个 10 分钟的任务，让我以有用的方式感到不自在。 | 活动 | 想行动 | 身体、静默、经过考验的信念 |
| 3 | 三天前我做了什么，之后就再没做过？为什么？ | 自我反思 | 卡住／无感 | 自我认识、没有Wi-Fi的知识 |
| 4 | 挑一个我最弱的要素。今天我能做的最小练习是什么？ | 批判性思考 | 想思考 | 全部八项（诊断） |
| 5 | 反对我最近的一个决定。一位明智的批评者会怎么说？ | 批判性思考 | 亢奋／好奇 | 没有Wi-Fi的知识、经过考验的信念 |
| 6 | 如果我要把一个今年学到的东西教给一名初一学生，应该是什么？ | 自我反思 | 想思考 | 没有Wi-Fi的知识、真实的群体 |
| 7 | 我的生活里，哪里我在表演，而不是真的在做？哪里我真的在做，而不是表演？ | 自我反思 | 疲惫／低落 | 经过考验的信念、静默 |
| 8 | 我现在把什么外包了出去，而它本该由我自己建立？ | 批判性思考 | 想思考 | 技能、数字自卫、没有Wi-Fi的知识 |
| 9 | 给我一个 30 分钟的活动，不需要手机，也不需要别人。 | 活动 | 卡住／无感 | 身体、静默、自然 |
| 10 | 我持有一个被追问时说不清楚的信念吗？我该保留它吗？ | 批判性思考 | 亢奋／好奇 | 经过考验的信念、没有Wi-Fi的知识 |
| 11 | 考我一个我忘了自己曾经会的东西。 | 每日仪式 | 疲惫／低落 | 没有Wi-Fi的知识 |
| 12 | 问我上一次真正感到无聊是什么时候，以及我在那份安静里注意到了什么。 | 自我反思 | 卡住／无感 | 静默、身体 |
| 13 | 建议一件我一周多前开始、今天就能完成的事。 | 活动 | 想行动 | 技能、经过考验的信念 |
| 14 | 带我一步步做一件我还不会做的实用的事：喂饱自己、补好车胎、写一份简历、换一个轮胎。 | 活动 | 亢奋／好奇 | 技能、身体 |
| 15 | 我的生活里，谁会在凌晨两点赶来？谁不会？为什么？ | 自我反思 | 卡住／无感 | 真实的群体 |
| 16 | 比较我今天实际怎么用的时间和我说想怎么用。差距在哪里？ | 每日仪式 | 想思考 | 经过考验的信念、静默 |
| 17 | 给我一个开场话题，让我能和一位很久没好好聊过的人聊起来。 | 活动 | 想行动 | 真实的群体 |
| 18 | 如果我只留下手机里的三个 App，其他都删掉，哪三个该留下？为什么？ | 批判性思考 | 想思考 | 数字自卫、经过考验的信念 |
| 19 | 带我出门走 15 分钟：我该真正看什么、听什么、注意到什么？ | 活动 | 想行动 | 自然、身体、静默 |
| 20 | 陪我给这一天收尾。三件发生的事，三件我注意到的事，一件我感恩的事。 | 每日仪式 | 疲惫／低落 | 全部八项（为一天收尾） |

#### Agent 如何使用它们

学生每次要一个提问时，Agent 都会读取
`essentials/00-introduction/lessons/prompts.md`。它**不会**
把提问一条条贴在学生面前。它会引出一个，邀请学生
去读，并为回答留出空间。它从不会连着问三个提问。

在**顺序**推送模式下，提问会自然地围绕学生当前在学
的那个要素聚拢。在**随机**模式下，Agent 会挑选贴合
当下情境的提问。两种模式下，八大要素都仍然可用。

---

## 每日仪式

这是一张一览表，列出 Agent 运行的所有仪式：它是什么、
什么时候触发、发到哪里，以及在哪里有详细文档。

| 仪式 | 时间 | 渠道 | 会发生什么 |
|---|---|---|---|
| **晨间一分钟** | 每天在学生选定的时间（默认早上 6 点） | Telegram 或 WhatsApp，**语音气泡 + 文本** | 当天的音频计划，聚焦当前要素里的一个小行动。 |
| **午后问候** | 每天在学生选定的时间（默认下午 5 点） | Telegram 或 WhatsApp，**纯文本** | 回顾这一天过得怎么样，为明天做计划，一个留到夜里慢慢想的问题。 |
| **睡前规划** | 每天睡前，学生选定的时间（默认晚上 9 点） | Telegram 或 WhatsApp，**纯文本** | Agent 起草明天的计划（学校任务、作业截止日期、本周要素、一件现实中的事）。学生修改它。保存在本地。 |
| **要素摘要** | 按需，学生随时提出 | Telegram 或 WhatsApp，**语音消息** | 三到五分钟的口头摘要，讲一个要素，附一份简短的要点清单。 |
| **要素课程** | 按需，学生随时提出 | here.now，**聊天里的 HTML 页面链接** | 三页课程，讲一个要素，带引用来源、关键引语和一个小测验。 |
| **要素诗** | 按需，学生随时提出 | Telegram 或 WhatsApp，**语音消息 + 文本** | 一首押韵的口头诗，讲这个要素，朗读出来，下面配着文字。 |
| **要素歌曲** | 按需，学生随时提出 | Telegram 或 WhatsApp，**MP3 语音消息 + 文本** | Agent 先写一首关于这个要素的诗，再通过 OpenRouter 上的 Google Lyria 3 把它变成真正的歌曲。每首约 $0.08，运行前请确认。 |
| **要素音乐视频** | 按需，学生随时提出 | here.now，**聊天里的 MP4 视频链接** | 上面的歌曲，加上一组静态画面的分镜，与音频拼接起来，可选叠加诗的文字。总共约 $0.35，运行前请确认。 |

**一天的样子。**晨间一分钟开启一天，问候为一天收尾，
睡前规划在入睡前把明天安排好。三个按需格式
（摘要／课程／诗）随时都在，让年轻人能比一分钟的
晨间一分钟更深入地学习一个要素。

**代码在哪里。**每一行都指向仓库里的一个技能：

| 仪式 | 技能路径 |
|---|---|
| 晨间一分钟 | `skills/hermes/morning-minute/` |
| 午后问候 | `skills/profile/afternoon-checkin/` |
| 睡前规划 | `skills/profile/planning-session/` |
| 摘要、课程、诗、歌曲、音乐视频 | `skills/profile/essential-deep-dives/`（歌曲和音乐视频会用到 `skills/creative/openrouter-lyria-music/` 和 `skills/creative/poem-song-video-studio/`） |

**同意。**三个基于 cron 的仪式（晨间一分钟、问候、
睡前规划）默认关闭，直到学生或家长在入门引导时批准
它们。五个按需格式（摘要、课程、诗、歌曲、音乐视频）
立即可用：学生开口就有。两个付费格式（歌曲和音乐
视频：Lyria 3 + 分镜图片）每次被请求时，都需要学生
确认花费。确切的开启流程见
[设置流程 → 后台运行的内容](#后台运行的内容)。

**歌曲和音乐视频技能。**两个付费格式复用两个已有的
技能，而不是重新发明它们：

| 格式 | 底层技能 | 在 `essential-deep-dives` 之上增加了什么 |
|---|---|---|
| **要素歌曲** | `skills/creative/openrouter-lyria-music/` | 诗 → 歌词 → 通过 Google Lyria 3 生成 MP3 音频（每首约 $0.08）。 |
| **要素音乐视频** | `skills/creative/poem-song-video-studio/` | 歌曲 + 约 8 张分镜图片 + ffmpeg → MP4（总共约 $0.35）。 |

这两个技能已经在仓库里，包含完整的 Lyria 3 模型
说明、脚本和 cost guard。学生请求某个格式时，Agent
会加载对应的底层技能。

**如何自定义。**设置时，Agent 会带学生为每个 cron
仪式选择时间、时区和运行日规则。三个之后都可以用
`cronjob(action="...")` 暂停、恢复或移除。按需格式会
自动采用学生的传统；它们的声音和时长继承自晨间
一分钟已经选好的 Piper 声音。

---

## 运行花费

OneToEight Agent 采用**按用量付费**，不需要订阅。
你往 OpenRouter 账户里充值，Agent 从这笔余额里
取用。

| 花费 | 金额 | 说明 |
|---|---|---|
| **第一个月** | **约 $20** | 覆盖设置，以及学生适应期的第一个月实际使用 |
| **之后** | **每月 $5–$10** | 在低成本模型上的轻量日常使用 |

这份 profile 在日常工作上偏向低成本模型：

- **DeepSeek V4 Flash**：日常聊天和课程的默认模型。
- **Google Gemini 3.7 Flash**：短任务的快速后备。
- **开源模型**（免费或近乎免费的档位）：用于不需要
  前沿模型的基础、高频工作。

免费档位每月轮换，所以确切名单会变。免费模型的最新
列表见 <https://openrouter.ai/openrouter/free>。这份
profile 默认选便宜方案，只有任务真正需要时才会动用
更大的模型。
---

## 教程

更喜欢有人带着走一遍？教程中心把所有设置页面集中在
一处：

- **build path**：七页内容，边搭边学：agent 一块一块
  被搭起来，配有音频可以跟学。从
  <https://gladtobe.here.now/build-path/> 开始。
- **onboarding curriculum**：七页；这门安装课程带你从
  第一次安装走到一个接通了聊天的 agent。
- **walkthrough sheets**：把设置浓缩在一页上，有三种
  语言。

打开教程中心：<https://gladtobe.here.now/hub-tutorials.html>。
下面的流程用文字、一步一步覆盖同样的内容。

---

## 设置流程

### 1：准备工作（一次性，在这台机器上）

你需要：

- **Hermes Agent**，已安装。快速检查：`hermes --version`。
  见[安装指南](https://hermes-agent.nousresearch.com/docs)。
- **Python 3.10 到 3.13**（不是 Windows 商店的那个
  shim，要真正的安装）。`python --version`。
- **Piper TTS。**一个能正常工作的安装。见下面的第 2 步。
- **ffmpeg**，用于 WAV → OGG 转换。`ffmpeg -version`。
- **一个模型服务商密钥。**这份 profile 默认使用
  `openrouter + deepseek-v4-flash`。一把密钥就能打开
  大量模型，包括免费档位和多模态（图像、音频）模型。
  在 <https://openrouter.ai/> 免费注册，然后用
  `hermes setup` 添加密钥。OpenCode Go 是后备。
- **一把 Jina AI 免费 API 密钥**，用于网页搜索。
  在 <https://jina.ai/> 免费注册，不需要信用卡。免费
  档位足够一个年轻人日常使用。
- **一个 Telegram 机器人**（推荐）或一个 WhatsApp 桥接。
  Telegram 简单得多，见第 4 步。

### 2：解压 profile（一次性）

你会以压缩包的形式收到这份 profile：
`onetoeight-agent-zh.zip`。把它解压到
`~/.hermes/profiles/` 里面，让它成为
`~/.hermes/profiles/onetoeight-agent/`，然后：

```bash
mkdir -p ~/.hermes/profiles
# 把 onetoeight-agent-zh.zip 解压到这个文件夹里
hermes profile use onetoeight-agent
hermes chat
```

> **注意：**profile 目录的名字是 `onetoeight-agent`，
> 不是 `onetoeight`。请相应更新引用 profile 路径的
> 命令。

以后要更新：下载新的压缩包，解压到一个临时文件夹，
把新文件复制进来，但**千万不要删除**你的 `memories/`
文件夹和已记录的会话。文件夹根目录的 `LOCALE.md`
记录了这份副本来自哪次构建。

### 3：第一次聊天 → 入门引导

第一次聊天时，Agent 会这样开场：

> “在正式开始之前，要不要我带你走一遍设置？只需要
> 几分钟，就能让你的工具、记忆和晨间一分钟按你希望
> 的方式运转起来。或者，我们跳过它，直接开始。”

回答“好”（或者随时直接说*“帮我设置好我的 profile”*）。
`agent-onboarding` 技能就会运行。

### 4：入门引导（需经同意）

入门引导是对话式的。Agent 每次只问一小串相关的
问题，并**在每个凭据环节暂停**：它从不在聊天里
索要密钥或令牌。

以下是它按顺序涵盖的内容：

| 步骤 | 会发生什么 | 在哪里添加 |
|---|---|---|
| 1. 身份 | 名字（你的、学生的、Agent 的）、回复风格，以及指南、课程和消息使用的语言 | 保存在 profile 记忆里 |
| 2. Profile 与生活 | 年龄、所在地、居住情况、一周的节奏、3 个兴趣、专注目标、朋友圈、卡点、禁谈话题：Agent 用来定制晨间一分钟和课程的字段 | 保存在 profile 记忆里 |
| 3. 传统 | 基督教、通用，或者你自己的传统 | 保存在 profile 记忆里 |
| 4. Piper 安装 + 声音 | 验证 Piper 能正常工作，挑选一个声音，下载声音模型 | 声音模型在 `piper-voices/` |
| 5. Jina API 密钥 | 免费注册，加到 `.env`，Agent 用一次真实的搜索来验证 | `JINA_API_KEY=` 在 `.env` |
| 6. 推送渠道 | Telegram 或 WhatsApp 机器人凭据 | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` 在 `.env` |
| 7. 八大要素指南 | 确认课程 MD 文件在 `essentials/01..08/lessons/`，并分享学生语言版本的指南（`essentials/guide-editions.md`） | 仓库里的文件 |
| 8. 记忆 | 推荐 Mnemosyne（本地优先，没有外部账号） | `hermes memory setup` |
| 9. 晨间一分钟时间表 | 几点、哪个时区、哪些天 | 创建为 cron 任务 |
| 10. 午后问候时间表 | 几点、哪个时区、哪些天 | 创建为 cron 任务 |
| 11. 睡前规划时间表 | 几点（默认晚上 9 点）、哪个时区、哪些天 | 创建为 cron 任务 |
| 12. Token Router（可选） | 收窄工具面的插件 | `config.yaml` 里的 `plugins.enabled` |

最后，Agent 会展示一份 **Proposed setup** 摘要，
在你明确批准之前，不会应用任何东西。

### 5：逐项验证

在第一次定时晨间一分钟运行之前，逐项验证每个组件：

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer ***" \
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

**各平台的 Piper 可执行文件位置：**

| 平台 | 常见路径 |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS（Homebrew） | `/opt/homebrew/bin/piper` |
| macOS（手动安装） | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows（pip） | `pip install piper-tts`，然后让 `piper` 出现在 PATH 上 |

入门引导会探测 Piper，只要它在你的 PATH 上就能找到。
如果它装在非常规的位置，入门引导会询问路径。

**声音模型存放**（下载一次，永久复用）：

| 声音 | 地区 | Hugging Face 路径 |
|---|---|---|
| `en_US-joe-medium` | 美国男声 | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | 美国女声 | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | 英国男声 | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | 英国女声 | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | 澳大利亚女声 | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

下载示例（以 Linux 上的 Joe 为例）：

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6：第一次定时运行

晨间一分钟会在学生时区的下一个计划时间触发。它会
生成音频（Piper），上传到 here.now 得到一个公开 URL，
再通过 multipart 上传把音频直接送到 Telegram，
**不是**通过 `MEDIA:<url>` 链接（here.now 的 Cloudflare
配置会拦截 Telegram 的文件抓取机器人）。问候会在
下一个计划的下午时间触发。

### 7：日常使用

学生不需要每天通过终端和 Agent 互动。Telegram 或
WhatsApp 聊天**就是**日常界面：

- **晨间一分钟**以语音气泡 + 文字计划的形式到达。
- **午后问候**以文本形式到达。
- **睡前规划**在睡前以文本形式到达：Agent 起草明天的
  计划（学校任务、作业截止日期、本周要素、一件现实
  中的事），学生修改，然后保存在本地。见
  `skills/profile/planning-session/`。
- **回复问候**，用一句话写下今天过得怎么样。Agent
  会存下一句摘要，并在明天的晨间一分钟里呼应它。
- **随时提问。**“经过考验的信念到底是什么样的？”
  “我怎样才能找到真实的群体？”Agent 会读指南并
  讲解。

#### 更深入地学习一个要素（按需）

在每天的节奏之外，学生还可以围绕任何一个要素，
点播更深入的格式。这些都由 `essential-deep-dives`
技能处理（见 `skills/profile/essential-deep-dives/`），
而且全部只需要开口要：

- **要素摘要**：用平实的语言讲一个要素的要点，
  再加上一段 3 到 5 分钟的**语音消息**，由 Agent
  （Piper）生成并送进聊天，学生可以在走路或做家务
  时听。
- **要素课程**：一堂漂亮的**三页课程**，做成 HTML
  页面，发布到这个家庭的 **here.now** 账号上。它用
  **引用来源**（每当课程需要指南里没有的材料时，
  就通过 Jina API 去检索）、**关键引语**和一个小
  **测验**来教这个要素，测验由学生在页面上作答。
  Agent 会把链接发进聊天。
- **要素诗**：一首押韵的**口头诗**，讲这个要素，
  作为语音消息朗读出来，下面配着文字，学生可以
  边听边读。
- **要素歌曲**：Agent 先写一首关于这个要素的原创
  诗，然后通过 OpenRouter 上的
  `google/lyria-3-pro-preview` 把它变成真正的歌曲
  （MP3）（每首约 $0.08）。语音消息在聊天里播放，
  诗的文本随后跟上。运行前确认花费。
- **要素音乐视频**：上面的歌曲，加上一组静态画面
  的分镜，与音频拼接，可选叠加诗的文字（歌曲 +
  分镜图片 + ffmpeg 合成，总共约 $0.35）。以 MP4
  发布到 here.now，链接发进聊天。运行前确认花费。

在起草这些内容之前，Agent 都会先读指南，按学生的
传统分支，并贴合学生的 profile，规则和课程技能
相同。

### 8：维护

偶尔需要：

- `hermes update`：把标准 Hermes 技能库拉进 profile
  （精选技能永远不会被覆盖）。
- `git -C ~/.hermes/profiles/onetoeight-agent pull`：
  获取指南或技能的上游改进。
- `cronjob(action="list")`：确认各个任务仍然在计划中。
---

## 你将在 `.env` 里配置什么

这份 profile 自带 `.env.example`，列出了每个变量。
下面是你实际要设置的内容。

### 必需（任何安装方式）

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 使用 Telegram 推送时必需

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Telegram 设置提示：**通过 @BotFather 创建机器人之后，
> 在 Agent 能给你发消息之前，你**必须先给它发至少
> 一条消息**（比如 `/start`）。从未收到过消息的机器人
> 发送时会静默失败。

要找到你的 chat ID：在 Telegram 里给 `@userinfobot`
发消息，它会回复你的数字 ID。

### 音频必需（晨间一分钟）

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **关于 here.now 的说明：**音频通过 here.now 的发布
> API 上传，得到一个公开 URL。这个 URL 通过 multipart
> 上传发送给 Telegram，**不需要** DRIVE_ID。如果你在
> 旧文档或示例里看到 `HERENOW_DRIVE_ID`，那是遗留
> 字段，当前的音频推送流程不使用它。

### 可选集成

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### 不是环境变量的东西

- **声音模型路径**：存在 profile 记忆里，不是环境
  变量。路径因机器而异。
- **Cron 时间表**：通过
  `cronjob(action="create", ...)` 设置，存在 cron
  注册表里，不是环境变量。
- **Piper 可执行文件路径**：存在 profile 记忆里。
- **Mnemosyne**：本地优先，不需要密钥。

---

## 仓库里有什么

```
onetoeight-agent/
├── README.md                              ← 这份文件
├── SOUL.md                                ← 人格与运行语气
├── AGENTS.md                              ← 运行原则
├── profile.yaml                           ← profile 描述文件
├── config.yaml                            ← Hermes 运行时配置
├── .env.example                           ← 每个变量，带注释
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← 八大要素的源内容
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← 导言（基督教版）
│   │   └── universal.md                   ← 导言（通用版）
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← Agent 对这个要素的教学笔记
│   │   ├── lessons/
│   │   │   ├── README.md                 ← 文件结构说明
│   │   │   ├── christian.md               ← 第一章（基督教版）
│   │   │   └── universal.md               ← 第一章（通用版）
│   │   └── activities/README.md
│   ├── 02-body/        （结构相同）
│   ├── 03-skills/      （结构相同）
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← 经过考验的信念 + 基督教定制
│   │   │   └── universal.md               ← 经过考验的信念 + 世俗定制
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← 十种语言的在线指南
│
├── skills/
│   ├── hermes/                            ← Hermes 精选技能
│   │   ├── agent-onboarding/  ← 入门引导
│   │   ├── morning-minute/                ← 每日计划 + 音频
│   │   ├── hermes-mnemosyne/              ← 记忆提供方
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← 这个 profile 自己的技能
│       ├── afternoon-checkin/           ← 下午的反思
│       ├── eight-essentials-curriculum/   ← 从指南教学
│       ├── essential-deep-dives/          ← 摘要、课程、诗等格式
│       └── setup-walkthrough/            ← Piper、Jina、渠道设置
│
├── plugins/hermes-token-router/           ← 可选的工具收窄插件
├── memories/                              ← 通用运行实践种子
└── skins/onetoeight.yaml                 ← 配色主题
```

> **标准 Hermes 技能**（web、terminal、github、creative
> 等）由 `hermes update` 拉取，不属于这个仓库。它们
> 在标准技能库里，不在这里。

---

## 配置参考

### 模型服务商（`config.yaml`）

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

改动 `provider` 和 `default` 即可切换。默认是
OpenRouter，因为一把密钥就能打开最广的模型目录：
免费模型，加上多模态（图像、音频）模型，不用更换
服务商。只有在主服务商不可用时，后备链才会运行。

### 工具集（`config.yaml`）

每个 CLI 工具集都**默认启用**。入门引导会带学生
逐一检查。要手动关闭：

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

`tts` 工具集必须保持开启，晨间一分钟才能工作。

### Cron 任务

通过入门引导创建。要手动管理：

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

完整的晨间一分钟 cron 约定见
`skills/hermes/morning-minute/SKILL.md`。

> **Cron 推送：**TUI/CLI 会话没有实时推送渠道。如果
> 你希望在 cron 触发时收到通知，请在创建时设置
> `deliver="telegram"`（或 `deliver="all"`）。否则
> 输出会保存在本地，可以通过 `cronjob(action="list")`
> 查看。

---

## 常见问题

| 症状 | 可能原因 | 解决办法 |
|---|---|---|
| Piper 加载失败 | 声音模型路径不对，或者还没下载 | 重新运行入门引导里的 Piper 步骤 |
| 晨间一分钟的音频无声或被截断 | TTS 输入的文本被截断了 | 合成之前确认文本文件是完整的 |
| Telegram 发送失败，提示“chat not found” | 机器人从未收到过消息 | 打开 Telegram，找到你的机器人，给它发 `/start` |
| Telegram 里音频播放不出来 | 用 `MEDIA:<url>` 传 here.now 的 URL | 用 `sendVoice` 做 multipart 上传（技能会处理这个） |
| cron 在错误的时间触发 | UTC 搞混了 | cron 存的是 UTC。北京时间早上 6 点 = `0 22 * * *`。悉尼早上 6 点 = `0 20 * * *` |
| 时间表写的是每天，却只在工作日触发 | cron 格式错误 | `0 6 * * *` = 每天。`0 6 * * 1-5` = 周一到周五 |
| Jina 搜索没有结果 | 密钥不在 `.env` 里，或者不对 | 用 `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` 测试 |
| Agent 给出错误传统的内容 | 记忆里没有传统 | 重新运行入门引导里的传统步骤 |
| 课程文件没有被读取 | 缺少 `.christian.md` 或 `.universal.md` 后缀 | 检查 `ls essentials/<NN>/lessons/`，文件名后缀必须正确 |

---

## Token Router 插件（可选）

Token Router 是一个可选的 Hermes 插件，它**收窄展示
给 Agent 的工具面**，而不是学生看到的。启用后，Agent
默认看到的工具更少，这能减少 token 消耗，让 Agent
专注于八大要素的工作。

它**不会**对学生隐藏任何功能。学生仍然可以问任何
问题；router 只影响 Agent 自动挑选的范围。

在以下情况启用：
- 你希望 Agent 专注于教学，而不是代码或数据分析。
- 你关心 token 消耗。

在以下情况保持关闭：
- 学生（或家长）希望完整的工具面可用。

启用方式：`hermes plugins enable hermes-token-router`
（在 `hermes profile use onetoeight-agent` 之后）。

---

## 许可证

MIT，见 `LICENSE`。

OneToEight Agent 的人格是专为本项目撰写的原创助理
原型。八大要素指南的内容来自 onetoeight *Eight
Essentials* 通用版 V.3.0.0，经许可收录，供本 profile
内使用。
