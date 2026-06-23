# qiaomu-xinzhiyuan-title

> 把 AI/科技文章或原标题改成“新智元版”标题：高密度实体、数字钩子、强转折、强后果感，同时保留事实边界。<br>
> Rewrite AI and tech source material into Xinzhiyuan-style Chinese headline options with dense entities, true hooks, and explicit fact boundaries.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-qiaomu-purple?style=flat-square)](SKILL.md)
[![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg?style=flat-square)](manifest.json)

**中文** | [English](#english)

---

## 中文

`qiaomu-xinzhiyuan-title` 是一个标题改写 skill。你给它一篇 AI 新闻、科技文章、素材摘要或普通标题，它会按“新智元式”标题规律生成多个候选：实体密度高，数字钩子明显，常用 `！`、`，`、`：`、`「」` 做信息压缩，并且会提示哪些说法需要事实支撑。

这个 skill 基于维护者提供的 2688 篇新智元微信公众号标题做聚合分析。仓库不包含原始文章或工作簿，只保留统计结果、标题公式、触发评估和本地体检脚本。

## 适合做什么

| 场景 | 你会得到什么 |
|---|---|
| AI 新闻起标题 | 5-7 个新智元风格候选，推荐标题排第一 |
| 原标题改写 | 更强的实体、数字、动作、后果结构 |
| 公众号发布前筛标题 | 数字版、冲突版、权威版、疑问版、克制版 |
| 事实边界检查 | 标出不能凭空添加的“刚刚”“全球第一”“Nature”等 claim |

## 快速安装

```bash
npx skills add joeseesun/qiaomu-xinzhiyuan-title
```

本地验证：

```bash
ls ~/.agents/skills/qiaomu-xinzhiyuan-title
```

也可以手动 clone：

```bash
git clone https://github.com/joeseesun/qiaomu-xinzhiyuan-title.git ~/.agents/skills/qiaomu-xinzhiyuan-title
```

## 你可以直接这样说

- `把这篇文章改成新智元版标题`
- `这个标题不够新智元，帮我起 5 个更抓人的版本`
- `用 qiaomu-xinzhiyuan-title 给这条 AI 新闻起公众号标题`
- `给我一个新智元味更重的标题，但不要编造事实`

## 输出格式

```markdown
推荐标题：...

备选：
1. ...
2. ...
3. ...

风格依据：...
事实边界：...
```

## 样例

输入：

```text
豆包大模型 2.1 发布，主打生产级 Coding 和 Agent，Pro 每百万 Tokens 综合成本 1.96 元。
```

输出示例：

```text
1.96元跑生产级Agent！豆包2.1 Pro上线，开发者工作流变天
```

输入：

```text
我饿了，想吃烧烤
```

输出示例：

```text
饥饿感全面上线，烧烤成唯一解！碳水与肉串集体狂飙
```

日常梗题会被当成“风格戏仿”，不会伪造成真实科技新闻。

## 风格边界

默认强度是“新智元味明显，但不过度炸裂”。如果来源只是普通产品更新或信息不足，skill 会优先给克制版，不会硬加来源里没有的事实。

不能凭空添加：

- `刚刚`
- `全球第一` / `国内首个` / `最强`
- `Nature` / `Science` / 顶会 / 榜单
- 融资金额、用户数、benchmark、排名
- 未在原文出现的人名、公司名、模型名

## 本地体检

候选标题可用内置脚本快速看风格密度：

```bash
python3 scripts/score_title.py "ChatGPT「学习模式」上线，AI老师杀进课堂！24小时导师免费用"
```

维护者验证：

```bash
python3 ../qiaomu-meta-skill/scripts/validate_skill.py .
python3 ../qiaomu-meta-skill/scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 -m json.tool manifest.json >/dev/null
python3 -m json.tool evals/trigger_cases.json >/dev/null
python3 -m json.tool reports/skill-ir.json >/dev/null
python3 -m json.tool reports/trigger-eval.json >/dev/null
python3 -m py_compile scripts/score_title.py
python3 scripts/score_title.py "ChatGPT「学习模式」上线，AI老师杀进课堂！24小时导师免费用"
```

已验证的包级 gate：

- `trigger_eval`: 12/12 passed
- `validate_skill`: passed in the maintainer environment
- `npx skills add ... --list`: passed in the maintainer environment

## 隐私与版权边界

- 不联网，不读用户文件，不需要账号或 API key。
- 正常使用时只读取本 skill 内的规则文件。
- 原始新智元文章和维护者本地工作簿不随仓库发布。
- 标题风格来自聚合统计与人工归纳，不复制原文正文，不保证商业传播效果。

## Troubleshooting

- 标题太像标题党：降低到 Level 1 或使用输出里的克制版。
- 事实边界不够稳：删掉未在来源中出现的时间、榜单、机构背书、精确数字。
- 标题太平：补一个真实硬钩子，优先顺序是实体、数字、冲突、权威、后果。
- 触发不到 skill：提示里明确说“新智元版标题”或 `$qiaomu-xinzhiyuan-title`。

## 关于向阳乔木

- 官网：<https://qiaomu.ai>
- 博客：<https://blog.qiaomu.ai>
- 推荐：<https://tuijian.qiaomu.ai>
- X：<https://x.com/vista8>
- GitHub：<https://github.com/joeseesun>
- 微信公众号：向阳乔木推荐看

---

<a name="english"></a>

## English

`qiaomu-xinzhiyuan-title` rewrites Chinese AI and tech source material into Xinzhiyuan-style headline options. It favors dense entities, real numbers, strong action verbs, consequence-driven framing, and explicit fact boundaries.

The skill is based on aggregate analysis of 2,688 Xinzhiyuan WeChat article titles provided by the maintainer. The raw workbook and article corpus are not included.

### Install

```bash
npx skills add joeseesun/qiaomu-xinzhiyuan-title
```

Manual clone:

```bash
git clone https://github.com/joeseesun/qiaomu-xinzhiyuan-title.git ~/.agents/skills/qiaomu-xinzhiyuan-title
```

### Example Prompts

- `Rewrite this AI article as a Xinzhiyuan-style Chinese headline.`
- `Use qiaomu-xinzhiyuan-title to generate 5 headline candidates.`
- `Make this title more Xinzhiyuan-like, but do not invent facts.`

### Output

The default output includes a recommended headline, alternatives, style rationale, and a fact-boundary note. It should not invent freshness, rankings, journal/conference names, money, user counts, benchmark results, or named people that are not present in the source.

### Verification

```bash
python3 -m json.tool manifest.json >/dev/null
python3 -m json.tool evals/trigger_cases.json >/dev/null
python3 -m py_compile scripts/score_title.py
python3 scripts/score_title.py "ChatGPT「学习模式」上线，AI老师杀进课堂！24小时导师免费用"
```

### License

MIT. See [LICENSE](LICENSE).

### Credit

Skill packaging follows the Qiaomu Meta Skill workflow, inspired by `yaojingang/yao-meta-skill`.
