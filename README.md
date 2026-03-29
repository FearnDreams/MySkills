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
| `literature-survey` | 文献调研 |
| `lecture-notes` | 课件讲解 - 逐页讲解并生成笔记 |
| `knowledge-linking` | 碎片化知识整合 |
| `latex-homework` | LaTeX作业助手 |

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
