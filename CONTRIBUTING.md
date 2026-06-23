# Contributing

## 中文

欢迎提交小而清晰的改进，尤其是：

- 更好的触发样例或反例
- 更稳的事实边界规则
- 更准确的标题风格体检逻辑
- README、安装和排障文档修正

提交前请运行：

```bash
python3 -m json.tool manifest.json >/dev/null
python3 -m json.tool evals/trigger_cases.json >/dev/null
python3 -m json.tool reports/skill-ir.json >/dev/null
python3 -m json.tool reports/trigger-eval.json >/dev/null
python3 -m py_compile scripts/score_title.py
python3 scripts/score_title.py "ChatGPT「学习模式」上线，AI老师杀进课堂！24小时导师免费用"
```

不要提交原始公众号语料、私有工作簿、账号凭据或未经授权的全文内容。

## English

Small, focused improvements are welcome: trigger examples, fact-boundary rules, headline scoring logic, and documentation fixes.

Before opening a pull request, run the validation commands above and avoid submitting private corpora, credentials, or copyrighted full-text content.
