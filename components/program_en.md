# About this Workshop

This summer, [Fun Workshop](https://fun-research-workshop.github.io/fun-workshop/) presents two parallel tracks designed to spark your curiosity and expand your horizons.

## 🤖 ClawTwin Exploration Program

Similar to OpenClaw, AI agents are already helping us handle daily chores. But imagine this scenario: "Help me add this event to my calendar, and ask Li Hua if they'd like to come along." — then your AI reaches out to Li Hua (or their agent!) using your unique tone and habits!

If you think this "digital twin" prospect is cool, please join us!

We have launched the **ClawTwin Exploration Program**, planning to develop a prototype over the coming months. We hope to build an open, fun community where people can make friends, share resources, and turn wild ideas into reality.

**🔑 Early Exploration Cases — Agent Collaboration Ecosystem:**

We have developed a comprehensive suite of tools to enable secure, human-in-the-loop multi-agent collaboration across networks. The ecosystem consists of the following project and its submodules:

- **[agent-collaboration-deploy](https://github.com/BillShiyaoZhang/agent-collaboration-deploy)** — The parent repository containing a unified Docker Compose and Nginx configuration to orchestrate and deploy the entire multi-agent collaboration system in one click.
  - **[agent-collaboration-web](https://github.com/BillShiyaoZhang/agent-collaboration-web)** (Submodule) — A responsive Next.js web application for Human-in-the-Loop (HITL) management. It allows users to register agents, view real-time chat histories, search for peer agents on the network, call remote agent services, and review/approve sensitive actions requiring human authorization. Plans to support human-in-the-loop decisions, transaction confirmation, and agent contact management; an iOS app is also under development.
  - **[agent-comm-platform](https://github.com/BillShiyaoZhang/agent-comm-platform)** (Submodule) — The Go-based backend infrastructure. It serves as the network's address book (Registry), dynamic message broker (MQ/Mailbox for offline buffering), and NAT traversal assistant (libp2p Circuit Relay v2), ensuring reliable communication even behind firewalls. Supports message routing between platforms and compliant message decryption (e.g., to meet platform message archiving requirements).
    - **[agent-comm](https://github.com/BillShiyaoZhang/agent-comm)** (Nested Submodule) — The core SDK and P2P communication library in Go. It can be integrated directly as a skill for agents to use. It enables agents to maintain local cryptographic identities (Ed25519/URN), establish direct end-to-end encrypted tunnels (using X25519 and a Double Ratchet crypto protocol for forward secrecy), and fall back to P2P relaying when necessary.

Whether you're a developer, designer, academic, or just a curious student, there's a place for you here:

- **💻 Geeks & Developers:** Core logic development and API integration. Regular meetings + open GitHub. Every line of code you write becomes a highlight on your resume.
- **🎨 Product & Designers:** No coding required! You can participate in UI/UX design or get creative "training" AI's personality and tone.
- **⚖️ Humanities & Social Science Explorers:** LLM use comes with privacy leaks, bias, and other inherent risks. We especially need students interested in AI ethics and data security.
- **🌱 New to Claw?** No experience needed! We provide introductory guidance in the OpenClaw Summer Workshop to get you up to speed.

### 🎉 Activities: Geek & Coffee Summer Party

| Aspect | Details |
| :--- | :--- |
| **Venue** | Cozy Coffee, 1st Floor, E Building, XJTLU Taicang Campus |
| **Time** | Once a week, first is 1h Workshop then 2h Initiative (First session: June 18th 14:30-17:30, fixed time to TBD at first session) |
| **Format** | Team exploration with topic suggestions; voluntary pairing; no pressure |
| **Capacity** | Unlimited (approx. 30 people estimated to avoid overcrowding) |
| **Ticket** | Any purchase at Cozy Coffee |

> [!WARNING]
> **Notes & Risk Warnings (Please Read Carefully)**
> - Due to the open and experimental nature of the project, we cannot guarantee absolute information security. Please stay vigilant when using models, authorizing agent behaviors, and sharing information.
> - Activity organizers provide voluntary ethics consulting but cannot be held responsible for any individual or team behavior. We encourage everyone to maintain an open and inclusive mindset, respecting each other's privacy and boundaries.
> - But that's exactly why we need everyone together — to face and solve these real challenges. We believe that in this process, we can not only create interesting technology and products, but also nurture a group of responsible and creative AI explorers.

---

## 🛠️ OpenClaw Summer Workshop

OpenClaw is on fire, but we haven't started exploring it yet! Don't worry — this summer, let's build our own Claw from scratch!

- **Goal:** From zero to hero — set up a simple OpenClaw and customize it to your habits. Detailed tutorials and guidance help you understand the underlying principles and get it running on your own device.
- **Instructors:**
  - Shiyao Zhang — PhD candidate, XJTLU, researching multi-agent systems, LLM applications, and knowledge engineering.
  - Zhilu Zhang — PhD candidate, XJTLU, researching financial market prediction and LLM.
  - Yuxin Xia — PhD candidate, XJTLU, researching cryptography.
  - Peng Zitian — PhD candidate, XJTLU, researching human-computer interaction and related areas.
  - More instructors welcome!

### Logistics

| Aspect | Details |
| :--- | :--- |
| **Format** | Online + Offline at Cozy Coffee, Taicang (Online is not recommended) |
| **Time** | Once a week, first is 1h Workshop then 2h Initiative (First session: June 18th 14:30-15:30) |
| **Capacity** | Capped at 30 people (to guarantee proper hands-on guidance) |
| **Fee** | ¥50 per person per session. If you also join the ClawTwin Exploration Program on the same day, you can enjoy a 20% discount (¥40). |
| **Requirement** | Bring a laptop (Windows/macOS/Linux with admin privileges) + prepare 50-200 RMB budget for model APIs (we'll guide you if you don't have a key) |

### 📚 Topics (Tentative)

#### -- Basic Level --
1. OpenClaw or Hermes setup and basic usage.
2. How to customize (tune) your agent.
3. Practical common Agent design patterns.

#### -- Intermediate Level --
4. LLM characteristics to consider when using agents.
5. Agent development tailored for specific deployment scenarios.

#### -- Advanced Level --
6. Replacing agent memory using knowledge graphs and ontologies.
7. Architectural design analysis of projects like agent-comm, agent-comm-platform, and agent-collaboration-web.

#### -- Pending Speaker Confirmation --
8. Training, fine-tuning, and iterating customized models for agents.
9. Cryptographic applications in agents.
10. Analyzing human-agent interactions.

---

## Co-organizers

**Confirmed:**
- [Fun Workshop](https://fun-research-workshop.github.io/fun-workshop/)
- Cozy Coffee
- IoTClub
- Unofficial Guide for XJTLU PGRS

**Reaching out:**
- ... (more to come)

期待在这个夏天，遇见充满好奇心的你！

For any questions, please contact the coordinator Shiyao Zhang at [shiyao.zhang14@student.xjtlu.edu.cn](mailto:shiyao.zhang14@student.xjtlu.edu.cn).
