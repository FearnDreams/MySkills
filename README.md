# MySkills

通用技能（Skills）集合，支持各类 Agent 框架（如 Alma、Claude Desktop、OpenAI GPTs 等）。

## 目录结构

```
MySkills/
├── academic/          # 学术研究
│   ├── lecture-notes/      # 课件讲解与笔记总结
│   ├── literature-survey/  # 文献调研
│   ├── paper-deep-read/    # 论文精读
│   ├── paper-quick-read/   # 论文粗读
│   ├── paper-critique/    # 论文深度解析与批判性思考
│   └── paper-popularize/  # 学术论文科普
├── knowledge/          # 知识整理
│   └── knowledge-linking/  # 碎片化知识串联整理
├── tools/              # 工具类
│   └── latex-homework/     # LaTeX作业模板助手
└── README.md
```

## 什么是 Skill？

Skill（技能）是一种可复用的 prompt 模板，可以在不同 Agent 框架中使用。每个 skill 包含：

- **SKILL.md**: 技能的核心 prompt 定义
- **描述**: 技能的用途和使用场景

## 支持的框架

这个仓库的 skill 格式设计为通用格式，已适配或可轻松适配以下框架：

| 框架 | 适配状态 | 说明 |
|------|----------|------|
| Alma | ✅ 已适配 | 使用 `alma skill use <skill>` 调用 |
| Claude Desktop | 🔄 需转换 | 转换为 JSON 格式 |
| OpenAI GPTs | 🔄 需转换 | 转换为 instruction 格式 |
| 自定义 Agent | ✅ 即插即用 | 只需读取 SKILL.md |

## 使用方法

### Alma

```bash
# 列出所有 skills
alma skill list

# 使用某个 skill
alma skill use <skill-name>

# 例如
alma skill use academic/lecture-notes
alma skill use academic/paper-deep-read
```

### 通用方式

直接读取 `SKILL.md` 文件内容作为 system prompt：

```python
# 示例：Python 中读取 skill
with open("academic/paper-deep-read/SKILL.md", "r") as f:
    system_prompt = f.read()
```

## 添加新 Skill

1. 在对应分类目录下创建新文件夹
2. 添加 `SKILL.md` 文件
3. 更新 README.md

### SKILL.md 模板

```markdown
# 技能名称

一句话描述这个技能的功能。

## 使用方法

什么时候使用这个技能？如何调用？

## Prompt

你的完整 prompt 内容...
```

## 贡献

欢迎提交 PR 添加新的 skill！

1. Fork 本仓库
2. 创建新分支
3. 添加你的 skill
4. 提交 PR

## License

MIT
