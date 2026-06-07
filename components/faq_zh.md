# 常见问题解答

这里收集了关于 Fun Workshop、ClawTwin 探索计划以及 OpenClaw 夏季工坊的一些常见问题。如果你有其他疑问，欢迎随时联系我们！

<div class="faq-container">
<!-- Q1 -->
<details class="faq-item" open>
<summary>这个网页/平台是做什么的？我们来这里参与什么？</summary>
<div class="faq-answer">
<p>这个网页是 Fun Workshop 发起的 <strong>ClawTwin 探索计划</strong> 与 <strong>OpenClaw 夏季工坊</strong> 的主页。</p>
<p>我们正在做一些面向未来的探索——研究“数字孪生智能体”（ClawTwin）。当智能体在不同情境下扮演我们的个人助理时，它们如何代表我们与别人的智能体进行安全通信（例如自动约时间、协调安排），并忠实执行我们的意志。</p>
<p>你可以来这里学习搭建自己的 AI 助手，参与产品与 UI 设计，或者和我们一起探讨大模型时代下的隐私、安全与伦理问题。</p>
</div>
</details>

<!-- Q2 -->
<details class="faq-item">
<summary>我平时用的是 DeepSeek、豆包、Kimi，它们也可以接入吗？什么是“智能体”？</summary>
<div class="faq-answer">
<p>可以接入，但我们需要先区分<strong>“大语言模型（LLM）”</strong>与我们所说的<strong>“智能体（Agent）”</strong>：</p>
<ul>
<li><strong>大语言模型（像 DeepSeek、豆包、Kimi）</strong>：它们是“大脑”或“思考引擎”。你问它一个问题，它回答你。但它本身没有双手，无法主动获取你的日程表，更无法代表你向其他人的 AI 发送消息。</li>
<li><strong>智能体（像 OpenClaw、Hermes）</strong>：它更像是一个“完整的数字助理”。它用大模型作为“大脑”来理解意图，但它还拥有“双手”（可以调用日历、邮箱等工具）、“记忆”以及“行动力”（可以主动与其他智能体通信）。</li>
</ul>
<p><strong>我们可以怎么接入</strong>：我们在工坊中搭建的 OpenClaw 智能体，会把 DeepSeek、豆包、Kimi 等大语言模型接入进来作为它的“大脑”。只要这些平台提供了 API 接口（API Key），就可以直接作为智能体的思考核心。</p>
<p><strong>关于各大平台自身的智能体服务</strong>：虽然豆包（如 Coze）或其它平台也提供自家的智能体服务，但它们通常运行在各自的商业云端生态内，无法实现跨平台、去中心化的点对点安全通信。而我们探索的 ClawTwin，是一个真正属于你个人的、能安全与其他人的智能体对话的数字分身。</p>
</div>
</details>

<!-- Q3 -->
<details class="faq-item">
<summary>接入了智能体以后，我们又可以用它来做什么呢？接入前后会有什么不同？</summary>
<div class="faq-answer">
<ul>
<li><strong>接入前</strong>：大模型只是网页或 App 里一个孤立的“聊天框”。它不了解你的日常安排，不知道你的真实喜好，也无法替你采取任何行动，更无法与其他人的 AI 沟通。</li>
<li><strong>接入后</strong>：智能体变成了你的“数字分身”（Digital Twin）。在你的授权下，它能获取你的本地日程、兴趣偏好。最重要的是，它能直接与别人的智能体进行安全对话。</li>
</ul>
<p><strong>具体例子</strong>：比如你想约朋友聚会，接入前你们需要在微信里反复对时间；接入后，你的智能体可以直接和朋友的智能体“私聊”，它们会自动对比双方的日程 and 偏好，挑选出最合适的时间，最后由你确认即可。</p>
</div>
</details>

<!-- Q4 -->
<details class="faq-item">
<summary>我完全没有编程基础，不是计算机专业的，也能参与吗？</summary>
<div class="faq-answer">
<p>绝对可以，我们非常需要非技术背景的朋友加入！AI 的未来绝不仅仅属于程序员：</p>
<ul>
<li><strong>零基础学习者</strong>：我们准备了“OpenClaw 夏季工坊”，手把手带你从零搭建、配置和运行属于自己的智能体。</li>
<li><strong>产品与设计师</strong>：无需写代码，你可以参与产品界面（UI/UX）的设计，或者发挥创意来“调教” AI 的性格、语气和人设。</li>
<li><strong>人文与社科学者</strong>：智能体代人沟通会引发关于隐私泄露、偏见、伦理及人际关系变化的深刻讨论，我们需要你的视角来共同把控方向。</li>
</ul>
</div>
</details>

<!-- Q5 -->
<details class="faq-item">
<summary>如果智能体知道我的日程和喜好，我的隐私安全如何保障？</summary>
<div class="faq-answer">
<p>这正是我们这个探索计划最核心的研究课题之一！</p>
<p>我们社区正在开发安全端到端加密的 P2P 智能体通信协议（即 <code>agent-comm</code> 项目）。与把日程全部上传到第三方云端服务不同，你的数据保留在本地，智能体之间是点对点加密通信的。</p>
<p>它们只在必要时交换最低限度的协调信息（例如“下午 2-4 点是否有空”），绝不会透露你日程的具体内容或隐私备注。</p>
</div>
</details>
</div>
