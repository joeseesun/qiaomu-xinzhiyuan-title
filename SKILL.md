---
name: qiaomu-xinzhiyuan-title
description: |
  Rewrite Chinese AI or tech 文章、新闻素材、article titles, article drafts, and source material into 新智元-style headline options for Qiaomu workflows. Use this skill when the user asks for 新智元版标题, 新智元风格起标题, 微信公众号爆款标题改写, or to convert an article/title into a high-density AI media headline while preserving facts.
metadata:
  author: 向阳乔木
  copyright: Copyright (c) 向阳乔木
  x: https://x.com/vista8
  github: https://github.com/joeseesun/
  source_dataset: "maintainer-provided local workbook; aggregate analysis only; raw corpus not bundled"
  upstream_inspiration: qiaomu-meta-skill; yaojingang/yao-meta-skill
---

# Qiaomu Xinzhiyuan Title

把用户给出的文章、新闻素材或原始标题改写成“新智元版”中文标题：高密度实体、数字钩子、强转折、AI 圈语感，但不捏造事实。

## Trigger

Use this skill when the user asks to:

- 把文章、新闻、草稿或标题改成新智元风格。
- 给 AI/科技内容起“新智元版标题”或微信公众号爆款标题。
- 让标题更像新智元、更抓人、更有 AI 媒体冲击力。
- 在 Qiaomu workflow 中批量生成或筛选新智元味候选标题。

## Do Not Trigger

- 用户要学术论文标题、报告标题、乔木博客标题、36 氪/量子位/机器之心等其他媒体风格。
- 用户明确要求克制、官方、SEO、产品公告、招聘 JD 或法律合规文案。
- 用户只是总结、翻译、校对新智元文章，并明确“不改标题”。

## Required Reference

Before rewriting, read [Xinzhiyuan Title Style](references/xinzhiyuan-title-style.md). It contains the data-backed style rules extracted from the local 2688-article workbook.

## Workflow

1. Parse the input into a fact card:
   - core entity: model, company, lab, person, paper, product, event
   - action: 发布、开源、泄露、登顶、融资、跳槽、翻车、突破、被裁、下架
   - hard hooks: numbers, rankings, speed, cost, benchmark, time, money, headcount
   - authority: OpenAI, Anthropic, Google, Meta, DeepMind, Nature, Science, top conference, top university, known researcher
   - stakes: who benefits, who is threatened, what changes, why now
2. Choose one primary angle. Priority order:
   - major AI entity or famous person
   - hard number or benchmark
   - conflict, reversal, surprise, leak, ban, job movement
   - global/China/ranking/first-time framing
   - practical consequence for users, developers, researchers, companies
3. Generate 5-7 headline candidates:
   - one recommended standard 新智元 version
   - one number-heavy version when numbers exist
   - one conflict/reversal version when the material supports it
   - one authority/ranking version when the material supports it
   - one question-hook version when uncertainty or suspense is real
   - one restrained version for lower-risk publishing
4. Score candidates with the checklist in the reference. If many candidates are close, optionally run:

```bash
python3 scripts/score_title.py "候选标题1" "候选标题2"
```

5. Return the recommended title first, then alternatives and a short fact boundary.

## Hard Rules

- Do not invent facts. Do not add “刚刚”, “全球第一”, “首个”, “Nature”, exact money, user count, benchmark, ranking, or named people unless present in the source or explicitly provided by the user.
- Keep the default title between 24 and 42 Chinese characters. A longer title is acceptable only when it carries multiple true hooks.
- Use `！`, `，`, `：`, `？`, and `「」` deliberately. Do not stack punctuation until the title becomes noisy.
- Preserve real English model/company names such as GPT-5, Claude, Gemini, DeepSeek, OpenAI, Anthropic, Meta, xAI, Nvidia.
- If the source is dry or low-stakes, make it “有新智元味但不过度炸裂”; use the restrained candidate as default.
- Never transform sensitive medical, financial, legal, safety, or personal-risk claims into exaggerated certainty.

## Output Format

Default output:

```markdown
推荐标题：...

备选：
1. ...
2. ...
3. ...

风格依据：...
事实边界：...
```

When the user asks for only one title, output only `推荐标题` plus one brief `事实边界` note if any claim may need source support.
