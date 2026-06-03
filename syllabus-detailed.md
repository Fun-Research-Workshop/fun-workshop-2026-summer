# Workshop Syllabus — Detailed Plan

> Per-session detail for the Fun Workshop Summer 2026 series. Pairs with the
> rendered page at `components/syllabus.html`.

## Overall Rhythm

```
1. 跑起来  → 2. 用得顺手  → 3-4. 写得出 agent
5. 落到场景 → 6-7. 撑得起复杂场景 → 8-10. 拓展视野
```

每节课 90 分钟，60% 实操 + 30% 讲 + 10% Q&A。

## Pace

| 周次 | 课 | 类型 | 前后依赖 |
|---|---|---|---|
| 1 | S1 | Setup | 无 |
| 2 | S2 | 调教 | S1 |
| 3 | S3 | 模式 | S2 |
| 4 | S4 | 理论 | S3 |
| 5 | S5 | 应用 | S3–4 |
| 6 | S6 | KG 记忆 | S2 + S5 |
| 7 | S7 | 生态架构 | S6 |
| 8–10 | T8–10 | 拓展 | S7 之后任选 |

---

## ✅ Session 1 — OpenClaw / Hermes 搭建与基本使用
**已确定：6/18 14:30–15:30（60 分钟起步版）**

**核心问题**：从零到跑通一个本地 agent，需要装什么、跑什么命令、怎么验证？

**讲**：
- 什么是 agent、什么是 LLM 调用、什么是工具（10 min）
- 三种部署形态：纯本地 / API 网关 / 混合（5 min）
- 目录结构、配置位置、env 文件、首次启动（5 min）

**实操（每人一组）**：
- 装 Python 3.12 / uv、克隆 repo、装依赖
- 配 `.env`、跑 `hermes setup` 验证
- 跑通第一个对话，调用一个工具（文件读写 / shell）
- 注册一个 cron job 验证调度

**验收**：
- ✅ `hermes chat` 能对话
- ✅ 至少 1 个工具调用成功
- ✅ 1 个 cron job 触发并执行

**衔接 Session 2**：默认配置千篇一律 → 下一课把它调成"你想要的形状"。

---

## 🧭 Session 2 — 调教你的 Agent
**核心问题**：如何让 agent 从"通用助手"变成"你的助手"？

**讲**：
- 四层配置：系统 prompt / 记忆 / 工具白名单 / 回复风格
- Persona 设计的反模式（"你是一个有用的助手"是垃圾 prompt）
- 记忆的分类：user profile / preferences / past decisions / transient state

**实操**：
- 写一个 system prompt：身份、语气、回答长度、禁止行为
- 配 memory：观察 agent 在多轮对话里"记住"了什么、丢掉了什么
- 工具开关：禁用不需要的工具，看行为变化
- 用 `skill_view` 加载一个 skill，验证 persona 生效

**验收**：
- ✅ 同样的问题，agent 回答风格符合你的 persona
- ✅ 跨 session 记忆持久化（kill 重启后仍记得）
- ✅ 禁用工具后 agent 知道改用别的方式

**衔接 Session 3**：单 agent 已经顺手 → 下一课让 agent 学会"思考"。

---

## 🧭 Session 3 — Agent 常见设计模式
**核心问题**：面对复杂任务，agent 怎么拆解、调用、纠错？

**讲**：
- **Planner-Executor**：先列计划、再逐步执行（ReAct、Plan-and-Execute）
- **Tool Calling**：JSON schema、参数校验、错误处理
- **Reflection**：执行后自评，失败重试
- **Human-in-the-Loop**：哪些动作必须人工确认（写文件、发消息、付钱）
- 何时该用哪个模式（决策树）

**实操（选 1）**：
- 用 `delegate_task` 写一个 research subagent，能并行调研 3 个问题
- 写一个带 reflection 的翻译/总结 pipeline：生成 → 评估 → 重写
- 写一个 HITL 工具调用：发邮件前必须确认

**验收**：
- ✅ 写出的 agent 能拆解 ≥3 步的复杂任务
- ✅ 工具失败时能重试或 fallback
- ✅ 危险操作有人工拦截

**衔接 Session 4**：模式都会了，但为什么同一个模式用 GPT-4 和 Llama-3 效果差很多？下一课解释底层原因。

---

## 🧭 Session 4 — LLM 特性对 Agent 的影响
**核心问题**：模型边界（context、幻觉、延迟、成本）如何决定 agent 设计？

**讲**：
- **Context window**：长对话如何截断、摘要、检索
- **Hallucination**：哪些任务高发、怎么抑制（chain-of-thought、工具验证、RAG）
- **Instruction following**：复杂 prompt 的失败模式
- **Latency / Cost**：streaming、batch、模型选型（小模型做路由、大模型做精修）
- **Function calling 的可靠性**：不同模型差异巨大

**实操**：
- 跑同一个 agent，切换 3 个不同模型（Haiku / Sonnet / 本地 Qwen）
- 记录：成功率、平均 token、平均延迟、成本
- 写一份"模型选型决策表"（什么场景用什么模型）

**验收**：
- ✅ 能解释为什么某任务 GPT-4o 强、Llama-3 弱
- ✅ 给一个真实需求推荐模型 + 估算成本
- ✅ 写出一个能"降级到便宜模型"的 fallback 逻辑

**衔接 Session 5**：理论够了，下一课去真实场景里解决问题。

---

## 🧭 Session 5 — 落地场景的 Agent 开发
**核心问题**：如何把通用能力封装成"开箱即用"的场景化 agent？

**讲**（30 min）：
- 场景拆解：日程同步 / 笔记整理 / 待办 / 学习聚合
- 每个场景的关键问题：
  - 数据从哪来？（API、文件、邮件、IM）
  - 触发点是什么？（cron / webhook / 手动）
  - 输出给谁看？（dashboard / 推送 / 静默）
- 复用 vs 重写的边界

**实操（4 选 1，60 min）**：
- **A. 日程同步 agent**：跨 Google Calendar / Outlook / 飞书日历，统一视图
- **B. 笔记整理 agent**：Obsidian / Notion 入库、自动打 tag、生成周报
- **C. 待办跟踪 agent**：从邮件/微信提取 todo，加到 Todoist/微软待办
- **D. 学习聚合 agent**：把论文/视频/书摘汇总成结构化笔记

**验收**：
- ✅ 至少 1 个真实数据源接通
- ✅ 端到端跑通 1 次
- ✅ 错误有合理降级（数据源挂了不崩）

**衔接 Session 6**：单场景够用，但 agent 记不住 3 个月前的事 → 下一课用 KG 升级记忆。

---

## 🧭 Session 6 — 用知识图谱替代 Agent 记忆
**核心问题**：context window 装不下"agent 的全部人生"，怎么办？

**讲**：
- 为什么聊天历史记忆不够用（线性、扁平、检索差）
- 本体（Ontology）建模：人 / 事件 / 偏好 / 决策 / 地点
- 三种存储：纯文本（markdown）、图数据库（Neo4j）、混合
- KG Memory 的查询模式：按人、按时间、按关系

**实操**：
- 设计一个 minimal ontology（你的 agent 用得到 5–8 类实体）
- 用 `kg_write` / `kg_search` / `kg_query_events` 写一批样例数据
- 写一个 query：跨 session 召回"过去 3 个月我跟谁聊过 X 主题"
- 对比：纯 context 检索 vs KG 检索的效果差异

**验收**：
- ✅ 能解释为什么 KG 比 context 更适合长期记忆
- ✅ 至少 5 类实体、10 条 relation 写入成功
- ✅ 一次跨 session 召回能拿到 3 个月前的信息

**衔接 Session 7**：单 agent 有了 KG 记忆，但 agent 之间还互相孤立 → 下一课看怎么打通。

---

## 🧭 Session 7 — Ecosystem 架构解析
**核心问题**：社区自研的基础设施是怎么解决"agent 之间怎么聊天"这个问题的？

**讲**：
- **问题域**：中心化 IM（微信、Slack）不能信任、需要 P2P
- **agent-comm 架构**：
  - libp2p bootstrap / DHT 发现
  - QUIC 传输
  - Double Ratchet 加密（每条消息独立密钥，前向安全）
  - relay 模式（NAT 穿透失败时）
- **agent-comm-platform**：中继节点、身份认证、URN 解析
- **agent-collaboration-web**：Web 端桥接

**实操**：
- clone agent-comm、看 `bootstrap.go`、理解 peer 发现
- 启动两个节点，跑通一次加密消息
- 修改 URN，看 relay 行为
- （可选）抓包看 QUIC handshake

**验收**：
- ✅ 能画出 3 个项目的组件图
- ✅ 能解释为什么需要 Double Ratchet（不是简单 TLS）
- ✅ 至少跑通一次 P2P + 一次 relay 通信

**衔接 Topic 8–10**：理论 + 工程都过了，剩下的是研究 / 安全 / 训练方向的拓展。

---

## 💡 Topic 8 — 训练、微调定制 Agent 模型
**讲师待定**

**核心问题**：当 prompt 工程到极限仍然不够，怎么办？

**讲**：
- 何时值得微调 vs 继续调 prompt
- 数据集构造：从你自己的对话日志里蒸馏
- 工具调用 SFT：怎么让小模型学会 function calling
- 平台对比：Unsloth / LLaMA-Factory / axolotl / Hugging Face TRL
- 评估：怎么测"agent 能力"而不只是"对话能力"

**实操**：
- 准备 50–200 条自己的 agent 对话数据
- 用 LoRA 微调一个 7B 模型，训练 function calling
- 跑同一个 eval，对比 base vs fine-tuned

**验收**：
- ✅ 知道微调的代价（数据、时间、GPU、效果上限）
- ✅ 训练至少 1 个小模型，完成 1 个 eval 任务
- ✅ 能判断"这个场景该微调还是该换模型"

---

## 💡 Topic 9 — 密码学在 Agent 中的应用
**讲师待定**

**核心问题**：多 agent 协同网络里，身份、消息、隐私怎么保护？

**讲**：
- **身份层**：DID（去中心化身份）、公私钥对、URN 编码
- **传输层**：TLS / QUIC / Noise protocol
- **消息层**：Double Ratchet（Signal Protocol）—— 跟 Session 7 接上
- **隐私层**：零知识证明（"我知道密钥但不告诉你密钥"）、环签名
- **密钥管理**：agent 的密钥怎么存、怎么轮换、怎么恢复

**实操**：
- 解析 agent-comm 用的加密栈（每一层对应什么攻击）
- 设计一个威胁模型：你的 agent 面对哪些对手、哪些攻击面
- 写一个最小的 Zero-Knowledge 验证 demo（年龄 ≥18 但不暴露生日）

**验收**：
- ✅ 能解释 DID、Double Ratchet、ZKP 各自解决什么问题
- ✅ 能给一个 agent 协同场景画威胁模型
- ✅ 至少实现 1 个 ZK / 加密 demo

---

## 💡 Topic 10 — 人机交互分析方法
**讲师待定**

**核心问题**：怎么知道用户和 agent 协作得"好不好"？

**讲**：
- 定量方法：行为日志、任务完成率、修正次数、停留时间、认知负荷测量（NASA-TLX）
- 定性方法：think-aloud、访谈、信任度量表
- agent 特有的研究问题：
  - 用户如何建立对 agent 的信任？
  - 何时用户会"过度信任"或"不信任"？
  - 错误如何归因（agent 的错 vs 模型的错 vs 自己的错）？
  - 长期使用中习惯如何演化？

**实操**：
- 设计一个 5 人小规模研究：让 5 个用户用 Session 5 做的 agent，记录 3 天
- 写一份研究方案：研究问题 / 招募 / 任务 / 度量 / 分析
- 跑一轮 pilot，整理发现

**验收**：
- ✅ 有一份可执行的研究方案
- ✅ 至少 3 个用户的数据
- ✅ 至少 1 条 actionable insight 反哺 agent 设计

---

## 整体建议

- **S4 留 1 份"失败案例集"** —— 让学员从别人的失败里学，比自己试错快 5 倍。
- **T8–10 的顺序可调** —— 看邀请讲师的档期，谁先来谁先讲。
