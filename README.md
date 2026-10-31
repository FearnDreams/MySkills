# MySkills

研究、阅读与写作的可复用方法。

每个 skill 只维护一份 `SKILL.md`，供 Codex、Claude Code 及其他 agent 读取使用。支持 skills 的 agent 可安装加载，其他 agent 也可直接读取文件执行；具体读文件、检索等操作使用各自已有的工具。

## 开始使用

**发消息给 Codex / Claude Code：**

```text
请从 https://github.com/FearnDreams/MySkills 安装 clear-writing 和 paper-quick-read。
先阅读仓库 README，再将这两个 skill 的完整目录安装到你当前环境支持的 skills 位置，
保留附带文件。完成后确认能读取各自的 SKILL.md，并告诉我如何调用。
```

想全部安装，把名称换成「全部 skills」即可。

也可以先不安装，在 agent 能读取仓库文件时直接发：

```text
请读取 https://github.com/FearnDreams/MySkills 中的 clear-writing/SKILL.md，
按其中的方法编辑下面这篇文章。
```

## 使用示例

安装后，直接告诉 agent 要用哪个 skill，并附上材料。

**快速读论文**

> 用 paper-quick-read 阅读这篇论文，帮我判断它解决了什么问题、证据是否充分，以及值不值得精读。

默认按 **Insight & Motivation → Method → Experiments → Limitations → 研究启发** 讲解，方法部分先给流程图，再解释执行步骤与核心公式。完整回答通常为 3,000–5,000 个中文正文汉字，Method 约占 45%–55%；也可以直接要求简短版、只讲方法或深入解释某条公式。细则和已认可的 STAR 示例随 skill 目录一起安装。

**把文章写清楚**

> 用 clear-writing 修改下面的文章。读者是产品经理，保留事实和必要术语，只给修改稿。

**组合使用**

> 先用 paper-popularize 把这篇论文写成科普文章，再用 clear-writing 检查可读性。保留研究的限定条件，不夸大结论。

## Skills

| Skill | 用途 |
| --- | --- |
| [clear-writing](clear-writing/SKILL.md) | 改善中英文稿件的可读性，保留事实与作者声音 |
| [paper-quick-read](paper-quick-read/SKILL.md) | 用方法流程图、分步公式与实验取证完成五部分论文讲解 |
| [paper-deep-read](paper-deep-read/SKILL.md) | 逐段精读，翻译、讲解公式并整理笔记 |
| [paper-critique](paper-critique/SKILL.md) | 评估研究设计、证据和贡献，寻找不足与启发 |
| [paper-popularize](paper-popularize/SKILL.md) | 将学术论文写成通俗易懂的科普文章 |
| [literature-survey](literature-survey/SKILL.md) | 围绕研究主题检索、筛选与整理文献 |
| [lecture-notes](lecture-notes/SKILL.md) | 逐页讲解课件，形成结构化学习笔记 |
| [knowledge-linking](knowledge-linking/SKILL.md) | 补全知识缺口，连接零散概念 |
| [latex-homework](latex-homework/SKILL.md) | 按已有 LaTeX 模板组织作业内容 |

## 添加 Skill

在仓库根目录创建 `<skill-name>/SKILL.md`，包含 `name`、`description` 的 YAML frontmatter 和执行说明。示例、参考资料与脚本放在该 skill 内，使用相对路径引用。保持同一份内容可被不同 agent 使用，不绑定平台工具名。

---

MIT
