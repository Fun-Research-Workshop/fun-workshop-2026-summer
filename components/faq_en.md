# Frequently Asked Questions

Here are some frequently asked questions about Fun Workshop, the ClawTwin Exploration Program, and the OpenClaw Summer Workshop. If you have other questions, feel free to contact us!

<div class="faq-container">
<!-- Q1 -->
<details class="faq-item" open>
<summary>What is this website/platform about? What am I participating in?</summary>
<div class="faq-answer">
<p>This website is the portal for the <strong>ClawTwin Exploration Program</strong> and the <strong>OpenClaw Summer Workshop</strong> organized by Fun Workshop.</p>
<p>We are exploring the future of personal AI assistants (Agents). Specifically, we are looking at how our personal agents can communicate with each other (e.g., to schedule meetings or coordinate tasks) while respecting our privacy and executing our will.</p>
<p>You can participate by building your own agent, sharing ideas, designing the AI's personality, or studying the ethical and security aspects of AI.</p>
</div>
</details>

<!-- Q2 -->
<details class="faq-item">
<summary>I usually use DeepSeek, Doubao, or Kimi. Can they be connected? What is an "Agent"?</summary>
<div class="faq-answer">
<p>Yes, they can be connected, but we need to distinguish between <strong>Large Language Models (LLMs)</strong> and <strong>AI Agents</strong>:</p>
<ul>
<li><strong>LLMs (like DeepSeek, Doubao, Kimi)</strong>: They act as the "brain" or "reasoning engine." They answer questions you type, but they don't have "hands"—meaning they cannot access your calendar or autonomously message other people's AIs on your behalf.</li>
<li><strong>AI Agents (like OpenClaw, Hermes)</strong>: They act as a "complete digital assistant." An agent uses an LLM as its "brain" for reasoning, but it also has "hands" (access to tools like calendars and emails), "memory," and "autonomy" (the ability to initiate communication with other agents).</li>
</ul>
<p><strong>How we connect them</strong>: The OpenClaw agent we build in our workshop will connect to LLM APIs (like DeepSeek, Doubao, Kimi, OpenAI, etc.) to use them as its "brain." As long as these platforms provide an API Key, they can power your agent.</p>
<p><strong>About commercial agent platforms</strong>: While companies like ByteDance (Coze) offer their own agent services, they run inside their closed commercial clouds and cannot easily participate in decentralized, peer-to-peer secure communication. The ClawTwin we are exploring is a truly personal, private digital twin that can securely converse with other agents.</p>
</div>
</details>

<!-- Q3 -->
<details class="faq-item">
<summary>What can we actually do after connecting the agent? What is the difference before and after?</summary>
<div class="faq-answer">
<ul>
<li><strong>Before Connection</strong>: You chat with AIs in separate, isolated chat boxes. They don't know your schedule, your specific habits, or your interests unless you copy-paste them every time. They also cannot talk to other people's AIs.</li>
<li><strong>After Connection</strong>: Your agent can access your local data (such as calendar, contacts, and preferences) under your control. More importantly, it can talk directly and securely to another person's agent.</li>
</ul>
<p><strong>Example</strong>: If you want to meet a friend, instead of messaging back and forth, your agent can negotiate directly with your friend's agent. They will automatically compare schedules/preferences, pick the best slot, and ask for your final approval.</p>
</div>
</details>

<!-- Q4 -->
<details class="faq-item">
<summary>I have zero programming background and I'm not a CS major. Can I still join?</summary>
<div class="faq-answer">
<p>Yes, we encourage non-technical people to join! AI is not just about writing code:</p>
<ul>
<li><strong>For zero-basis learners</strong>: We have the <strong>OpenClaw Summer Workshop</strong> which guides you step-by-step from scratch to set up your own agent.</li>
<li><strong>For creators & designers</strong>: You can participate in UI/UX design or help "train" the agent's personality, tone, and character.</li>
<li><strong>For humanities & social science thinkers</strong>: Agent communication raises major questions about privacy, ethics, and social dynamics. We need your perspective to guide the project toward a future we all prefer.</li>
</ul>
</div>
</details>

<!-- Q5 -->
<details class="faq-item">
<summary>If the agent knows my calendar and preferences, how is my privacy secured?</summary>
<div class="faq-answer">
<p>This is one of the most critical questions we are researching!</p>
<p>In our community, we are developing secure P2P encryption protocols (like the <code>agent-comm</code> project). Unlike sending your entire calendar to a third-party server, agents talk directly using end-to-end encryption.</p>
<p>They are designed to only negotiate outcomes (e.g., "available between 2 PM and 4 PM") without revealing private details (e.g., what you are doing at other times or your personal notes).</p>
</div>
</details>
</div>
