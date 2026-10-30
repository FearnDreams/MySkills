# 编辑判断示例

所有例子均为本 skill 自拟，不是论文样本。修改方式不唯一；重点是判断何时改、改到哪里、何时停。

## 1. 展开名词之间的关系

场景：产品文档，上文已明确讨论检索系统。

原文：长尾查询覆盖不足导致的召回质量波动增加了人工复核负担。

修改：系统对少见的查询覆盖不足，因此有时会漏掉相关结果，有时又能找到。这种不稳定增加了人工复核的负担。

判断：仅当上下文说明“召回质量波动”指上述表现时，才采用这版解释。如果指标定义未知，保留“召回质量不稳定”，不要自行具体化成漏检频率或准确率变化。

## 2. 把主干与附加说明分开

原文：这项在三个数据集上进行、排除了训练集重叠样本、但尚未覆盖真实业务流量的评测发现了性能差异。

修改：这项评测发现了性能差异。评测使用三个数据集，并排除了与训练集重叠的样本，但尚未覆盖真实业务流量。

判断：条件和局限仍紧邻结果。不能只留下第一句，也不能把“性能差异”擅自写成“显著提升”。

## 3. 条件比短句更重要

原文：仅当请求不含个人信息、用户已同意且缓存未过期时，系统才复用缓存结果；管理员撤回授权后，即使缓存未过期，也不得继续复用。

可保留原文，也可在格式允许时把三个必要条件列出来，随后完整保留撤回授权的例外。

错误改法：用户同意后，系统会复用未过期的缓存。

判断：错误版本丢了个人信息限制和撤回授权例外，还把必要条件写成了足以触发复用的条件。

## 4. 不替作者决定模糊的指代

原文：作者把审稿人的意见发给编辑后，他撤回了修改建议。

处理：这里的“他”可能指作者、审稿人或编辑；上下文不足时无法安全消歧。只改能确定的部分，在说明中询问“撤回建议的是谁？”

判断：更流畅的错误归属比保留歧义更糟。若用户只要正文，不能为消歧偷偷补一个身份。

## 5. 保留专业术语和统计边界

原文：在该样本中，A 组错误率从 10% 降至 8%，即下降 2 个百分点；这不等于已证明 A 导致了下降。[1]

处理：这句话已经清楚，可以保留。除非任务需要，不添加相对降幅，不把百分比和百分点互换，也不删掉因果限制或引用。

判断：清晰度编辑不要求每句留下修改痕迹。

## 6. 保留有作用的文学表达

原文：我把那封信读了三遍。窗外的雨还没停，屋里却已经安静下来。

处理：保留。

判断：停顿和含蓄是表达的一部分。不要补上作者没有说出的情绪、事件或解释；不要把它改成概括式报告。

## 7. English: unpack a noun stack with context

Context: The report compares how often different teams make mistakes when reviewing deployment exceptions.

Before: Cross-team deployment exception review error rates remain unmeasured.

After: We have not measured how often different teams make mistakes when reviewing deployment exceptions.

Decision: The context fixes which relationships the noun stack encodes. Without it, ask whether the rates are compared across teams or concern a review conducted jointly by several teams. Do not introduce “we” if the document does not establish that perspective; “No measurement is available…” is another option when supported.

## 8. English: preserve modality and causality

Before: In this sample, lower latency was associated with higher completion rates; the observational design cannot establish causality.

After: In this sample, completion rates were higher when latency was lower. Because the study was observational, it cannot establish that lower latency caused the higher completion rates.

Decision: Sample scope and the causal limitation remain. Do not promise that reducing latency will improve completion rates.

## 9. English: sometimes a familiar construction is fine

Original: The server rejected the request. The results suggest that the effect may depend on sample size.

Decision: Both sentences are clear in ordinary technical writing. “The server rejected” does not require replacing an inanimate subject; “suggest” and “may” preserve uncertainty. Do not expand every conventional metaphor or remove every optional “that.”

## 10. 连贯性不能靠添加因果来补

原文：团队缩短了培训。次月，投诉增加了。

可改为：团队缩短了培训。到了次月，投诉增加了。

判断：时间关系可表达得更顺，但原文没有证实因果，不能改成“缩短培训导致投诉增加”。如果用户要解释原因，应另行查证。
