#!/usr/bin/env python3
"""Score candidate headlines against the qiaomu-xinzhiyuan-title style checklist."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict


ENTITY_RE = re.compile(
    r"(AI|AGI|ASI|GPT|ChatGPT|Claude|Gemini|DeepSeek|OpenAI|Anthropic|Meta|Google|"
    r"谷歌|微软|英伟达|Nvidia|xAI|马斯克|奥特曼|小扎|清华|北大|MIT|斯坦福|"
    r"Nature|Science|ICLR|NeurIPS|CVPR|ACL|ISCA)",
    re.I,
)
NUMBER_RE = re.compile(r"\d+(?:\.\d+)?\s*(?:万|亿|%|倍|秒|分钟|小时|天|年|人|tokens?/秒|token|参数|美元|刀)?", re.I)
ACTION_RE = re.compile(r"(发布|上线|开源|官宣|曝光|泄露|登顶|霸榜|放榜|突破|斩获|吊打|碾压|狂飙|杀疯|翻车|封杀|裁员|抢人|跳槽|融资|下架|被端)")
CONSEQUENCE_RE = re.compile(r"(变天|破防|汗颜|抢破头|输在起跑线|饭碗|打工人|开发者|科研|行业|市场|全网|用户|企业|公司|课堂|工作流)")
SOURCE_REQUIRED_RE = re.compile(r"(刚刚|突发|全球第一|国内首个|全球首个|首次|最强|Nature|Science|诺奖|图灵奖|最佳论文|金牌|首发)")


@dataclass
class Score:
    title: str
    score: float
    max_score: float
    verdict: str
    hits: list[str]
    warnings: list[str]


def title_len(title: str) -> int:
    return len(title.strip())


def score_one(title: str) -> Score:
    hits: list[str] = []
    warnings: list[str] = []
    score = 0.0
    length = title_len(title)

    if 24 <= length <= 42:
        score += 2.0
        hits.append("length-24-42")
    elif 20 <= length <= 48:
        score += 1.0
        hits.append("length-near-range")
    else:
        warnings.append(f"length={length}; target 24-42")

    if ENTITY_RE.search(title):
        score += 1.5
        hits.append("ai-tech-entity")
    else:
        warnings.append("missing recognizable AI/tech entity")

    if NUMBER_RE.search(title):
        score += 1.2
        hits.append("hard-number")

    if ACTION_RE.search(title):
        score += 1.5
        hits.append("strong-action")
    else:
        warnings.append("missing strong action verb")

    if CONSEQUENCE_RE.search(title):
        score += 1.2
        hits.append("consequence")

    if any(p in title for p in ("！", "？", "：")):
        score += 1.0
        hits.append("punctuation-pivot")
    else:
        warnings.append("missing punctuation pivot")

    if "，" in title or "," in title:
        score += 0.6
        hits.append("comma-compression")

    if "「" in title and "」" in title:
        score += 0.8
        hits.append("quoted-concept")

    if SOURCE_REQUIRED_RE.search(title):
        warnings.append("contains source-required claim; verify it appears in the input")

    if score >= 7.0:
        verdict = "strong"
    elif score >= 5.0:
        verdict = "usable"
    else:
        verdict = "weak"

    return Score(title=title, score=round(score, 1), max_score=9.8, verdict=verdict, hits=hits, warnings=warnings)


def read_titles(args: argparse.Namespace) -> list[str]:
    titles = [t.strip() for t in args.titles if t.strip()]
    if titles:
        return titles
    return [line.strip() for line in sys.stdin if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Score candidate titles for qiaomu-xinzhiyuan-title style fit.")
    parser.add_argument("titles", nargs="*", help="Candidate title strings. If omitted, read one title per stdin line.")
    parser.add_argument("--json", action="store_true", help="Render JSON instead of a compact text report.")
    args = parser.parse_args()

    scores = [score_one(title) for title in read_titles(args)]
    if args.json:
        print(json.dumps([asdict(score) for score in scores], ensure_ascii=False, indent=2))
        return

    for item in scores:
        print(f"{item.score:>4}/{item.max_score:g} {item.verdict:>6} | {item.title}")
        print(f"     hits: {', '.join(item.hits) if item.hits else '-'}")
        if item.warnings:
            print(f" warnings: {'; '.join(item.warnings)}")


if __name__ == "__main__":
    main()
