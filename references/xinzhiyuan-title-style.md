# Xinzhiyuan Title Style

Source: maintainer-provided local workbook with 2688 Xinzhiyuan WeChat article rows. The raw workbook and article corpus are not bundled in this public skill package.

Analysis date: 2026-06-23. The workbook has 2688 rows, with `标题` and `文章内容` columns. This reference stores extracted title rules and aggregate evidence, not the raw article corpus.

## Data Signals

- Title count: 2688 raw titles, 2530 unique titles. Repeated event/promo titles were treated as weak signals.
- Length: average 31.1 characters, median 32. Quartiles: 27 / 32 / 36. Most usable titles sit between 24 and 42 characters.
- Punctuation:
  - `！`: 77.8% of titles
  - `，`: 78.8% of titles
  - `「」`: 24.9% of titles
  - `？`: 12.2% of titles
  - `：`: 21.5% of titles
- Lexical signals:
  - English/model/company names appear in 90.8% of titles.
  - Digits appear in 56.7% of titles.
  - Common entities: AI, OpenAI, Claude, Anthropic, GPT, Gemini, DeepSeek, Meta, Google, Nvidia, 马斯克, 奥特曼, 小扎, 清华, 北大, MIT, Stanford.
  - Common power words: 刚刚、爆、开源、全球、首个、首次、最强、第一、封神、杀疯、狂飙、登顶、霸榜、翻车、破防、血洗.

## Core DNA

新智元标题通常不是一句完整新闻标题，而是三段信息压缩：

1. attention hook: entity, number, breaking-news cue, conflict, or surprise
2. event/action: 发布、开源、泄露、登顶、封杀、跳槽、抢人、裁员、突破
3. consequence: who is shocked, who loses, what changes, why this matters

Default shape:

```text
[核心实体/时间钩子]，[动作或冲突]！[数字/权威/结果/后果]
```

Examples of the observed rhythm:

- `刚刚，北大DeepSeek斩获ACL 2025最佳论文！全网首发一作演讲，稀疏注意力是终局`
- `GPT-5发布倒计时？全网泄露来了：微软Copilot憋大招，GPT-5上线最后冲刺！`
- `小扎一夜反水，背刺开源！亲手葬送「Llama神话」，股价大涨12%`
- `地球版ChatGPT爆诞！谷歌AI 64维压缩人类星球，10米级「上帝视角」秒开`

## High-Value Formulas

### 1. Breaking News

Use when the source is truly fresh or the user says it just happened.

```text
刚刚，[机构/模型/人物][动作]！[硬结果/榜单/后果]
突发！[人物/公司][动作]，[行业后果]
```

Do not add `刚刚` if the source does not support freshness.

### 2. Entity Plus Hard Number

Use when the source has metrics, money, speed, user count, parameter count, paper count, benchmark, or ranking.

```text
[数字][单位][对象]，[实体][动作]！[对手/行业/用户后果]
[实体][指标]狂飙[数字]！[场景结果]
```

Numbers should stay specific: `2.5亿`, `400 tokens/秒`, `25%录用`, `10分钟`, `98%`.

### 3. Conflict Or Reversal

Use only when the story has real opposition, reversal, controversy, job movement, ban, leak, or competitive tension.

```text
[人物/公司][冲突动作]，[对手/旧路线]！[真实后果]
[实体]护城河被攻破！[新王/对手][结果]
```

Useful verbs: 炮轰、决裂、封杀、反水、背刺、挖空、抢人、逼宫、翻车、下架、被端、怒批.

### 4. Authority Or Ranking

Use when the source has a top conference, prestigious journal, leaderboard, famous scientist, or elite university.

```text
[顶会/榜单]放榜：[中国/某机构][成绩]！[附加价值]
[权威人物/机构]亲测/转赞/背书，[模型/方法][结果]
```

Never fake authority. `Nature`, `Science`, `MIT`, `Stanford`, `清华`, `北大`, `ICLR`, `NeurIPS`, `CVPR`, `ACL`, `ISCA` must come from source material.

### 5. Quoted Concept

Use `「」` to package one sticky concept, not random emphasis.

```text
[实体]「新概念」上线/曝光！[类比式后果]
[人物]押注的「世界模型」，[新进展]已实现？
```

Good quoted concepts are short: `学习模式`, `世界模型`, `上帝视角`, `AI科学家`, `永久记忆`, `曼哈顿计划`.

### 6. Question Hook

Use when the source has suspense, uncertainty, or a counterintuitive finding.

```text
[现象/判断]？[真相/转折]：[实体][动作]，[后果]
[旧认知]错了？[新证据][结论]
```

Do not make every title a question. In the dataset, questions are a minority signal, about 12%.

### 7. China / Global / First-Time Frame

Use when China, global rank, domestic first, worldwide benchmark, or cross-border comparison is central.

```text
[国产/中国][模型/公司]登顶全球第一！[对手/行业后果]
[全球首个/国内首个][对象]来了，[标准/生态/应用]变天
```

`全球第一`, `首个`, `首次`, and `最强` require evidence.

### 8. Human Consequence

Use when the story affects researchers, developers, students, creators, employees, or companies.

```text
[AI/模型][动作]，[人群]变天！[具体场景]
[工具/模型]一夜刷屏，[人群]直呼[情绪/结果]
```

Useful consequence words: 变天、破防、汗颜、抢破头、输在起跑线、饭碗、打工人、科研狗、开发者、创业者.

## Candidate Checklist

Aim for at least 4 of the following 7:

- has a recognizable AI/tech entity
- has one true number or hard metric
- has a clear action verb
- has one consequence or affected group
- has one punctuation pivot, usually `！` or `：`
- has a ranking/authority/conflict/novelty hook
- packages one concept with `「」` when useful

Avoid:

- two or more unsupported superlatives in one title
- vague hype without entity: `震撼发布！AI彻底改变世界`
- borrowed facts from similar stories
- too many quoted terms
- `刚刚` on old or evergreen material
- violence-like words when the source is only a normal product update

## Intensity Levels

Level 1, restrained:

```text
[实体][动作]，[数字/权威]揭示[变化]
```

Level 2, default 新智元:

```text
[实体][动作]，[对手/行业]变天！[数字/后果]
```

Level 3, explosive:

```text
刚刚，[实体][强动作]！[冲突/数字/后果]，全网[情绪]
```

Default to Level 2. Use Level 3 only when the source really has breaking news, fierce competition, viral reaction, or strong benchmark evidence.

## Rewrite Examples

Input fact: OpenAI releases a study mode for ChatGPT; it targets education and tutors users step by step.

Output:

```text
ChatGPT「学习模式」上线，AI老师杀进课堂！24小时导师免费用
```

Input fact: a domestic model wins a coding benchmark with lower cost than Claude.

Output:

```text
国产编程模型登顶新榜！成本打到Claude零头，开发者集体破防
```

Input fact: a paper from Tsinghua improves a long-standing graph algorithm.

Output:

```text
清华团队突破40年算法瓶颈！教科书级难题被改写，顶会最佳论文到手
```

Input title only: `AI agents can now browse websites`

Output:

```text
AI Agent终于会自己上网了！网页操作全自动，打工人工作流变天
```

Fact boundary: title-only input lacks exact source proof, so do not add specific model, benchmark, company, or timing unless provided.
