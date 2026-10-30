# MySkills

通用 Skills 集合，支持多种 Agent 框架。

## 目录结构

```
MySkills/
├── README.md
├── convert.py
├── claude/          # Claude Desktop JSON 格式
├── gpt/             # OpenAI GPTs 格式
├── academic/        # Alma 源文件
├── knowledge/
└── tools/
```

## 平台适配

| 平台 | 格式 | 导入方式 |
|------|------|----------|
| **Alma** | YAML+Markdown | `alma skill use <name>` |
| **Claude Desktop** | JSON | 复制 `claude/*.json` 到 Custom Skills |
| **OpenAI GPTs** | Markdown | 复制 `gpt/*.md` 到 Instructions |

## Skills 列表

| Skill | 描述 |
|-------|------|
| `paper-deep-read` | 论文精读 - 逐段精读，包含原文、翻译、讲解和笔记总结 |
| `paper-quick-read` | 论文粗读 - 快速提取核心信息 |
| `paper-critique` | 论文批判性分析 |
| `paper-popularize` | 学术科普 - 转译成通俗易懂的文章 |
| [`clear-writing`](academic/clear-writing/SKILL.md) | 清晰写作 - 改善中英文稿件的可读性，保留事实、限定条件与作者声音 |
| `literature-survey` | 文献调研 |
| `lecture-notes` | 课件讲解 - 逐页讲解并生成笔记 |
| `knowledge-linking` | 碎片化知识整合 |
| `latex-homework` | LaTeX作业助手 |

## 清晰写作

`clear-writing` 可单独编辑已有稿件，也可作为文章初稿完成后的审校步骤。

示例：`请用 $clear-writing 修改这篇文章，读者是产品经理。保留术语和事实，只给修改稿。`

源文件与补充案例位于 [`academic/clear-writing/`](academic/clear-writing/)。Claude JSON 和 GPT Markdown 由现有转换脚本生成；核心编辑流程在单文件导出中完整保留。Codex 可将整个 `clear-writing` 文件夹放入自己的 skills 目录使用。

方法受 [arXiv:2610.29162v1](https://arxiv.org/abs/2610.29162v1) 启发；中文规则与编辑流程是实践设计，效果需结合目标读者检验。

## 格式转换

修改源文件后运行：

```bash
python3 convert.py
```

## 添加新 Skill

1. 在 `academic/` 下创建目录，添加 `SKILL.md`（YAML frontmatter 格式）
2. 运行 `python3 convert.py`

## License

MIT
