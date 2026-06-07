# A Word on the ClawTwin Initiative & Workshop

Finally, I have some time to write down some thoughts for you all—about what this exploration initiative and workshop are actually for, what to expect, and some details that are already on the website but might have been overlooked.

## ClawTwin Initiative

As I briefly touched upon before, I feel that the interaction between AI agents belonging to different individuals or organizations will mark a crucial turning point. Before this point, much of the work could still be left to humans; after it, there might not be room for humans to do much of it. The reason is simple: human intelligence might no longer be a premium commodity.

When we experiment with buying things using AI agents today, only a single agent is typically involved—the one we interact with. It takes our commands, searches the web for relevant info, and awaits our next instruction. This process requires a continuous stream of commands from us, meaning it still demands significant cognitive overhead from the user.

Yet, we have already begun delegating massive amounts of human cognition to agents. For instance, how many people still write code completely by hand? Working with a programming agent for just one hour can easily match the output of two or three days of traditional coding. And we all know this is not the endgame of cognitive delegation. Take the e-commerce scenario above: currently, merchants are not intelligent. They list products in structured forms on delivery platforms, and once a human, an agent, or whatever orders, they prepare the items. But merchants will also use agents (instead of static delivery systems) to interact with consumers' agents. This creates agent-to-agent interaction.

This kind of interaction can be incredibly helpful. Naturally, I interact a lot with my own agent, so it knows my preferences—like preferring Pepsi over Coke (a bit weird?), being sensitive to heat, liking quiet places, and so on. When it interacts with other agents, it can query them based on my preferences to see if they can meet my needs. Meanwhile, the merchant's agent, which has a deep understanding of their products, can answer any questions to the best of its ability.

Of course, this might mean that our agent could negotiate a better price simply by proving we are a high-quality consumer; or, it could mean our agent ends up paying a premium for highly customized service.

We are all too familiar with user data exploitation, dynamic pricing traps (algorithmic price discrimination), and short-video addiction. Naturally, I sometimes worry that AI agents could usher in an even more dystopian era. I'm surely not the only one thinking this way; when OpenAI suggested inserting ads into ChatGPT responses, many users immediately abandoned it.

I believe we all look forward to a better life driven by technological progress, rather than a more exploitative and oppressive environment. Yet, in a way, I can't even know what the future looks like because the technology is still in its infancy, and the future has not yet arrived.

That is why I launched this Initiative. Since we don't know, let's explore it together—after all, this is my field of research. Of course, I don't want this to be just a gathering for tech geeks. The future concerns everyone and will be shaped by all of us. Bringing in diverse perspectives is vital, so no matter what your background is or how you wish to participate, you are warmly welcome!

The goal of this Initiative is to explore possibilities without limitations. Everyone is welcome to share any directions or topics they find interesting, identify like-minded friends, and explore together. During the preparation phase, I chatted with many friends and identified several topics we need to explore: how agents interact, how authorization works, how to protect privacy, how to leverage existing infrastructure, what role humans should assign to them, whether they should have complete autonomy, and more.

To kick off the discussion and prepare some basic infrastructure, I have developed the following projects over the past few days:

- **[agent-comm](https://github.com/BillShiyaoZhang/agent-comm/)**: An agent skill that maintains peer-to-peer (P2P) communication between agents.
- **[agent-comm-platform](https://github.com/BillShiyaoZhang/agent-comm-platform)**: Provides identity authentication, NAT traversal, and message queue services for agent-comm. It supports message routing between platforms and compliant message decryption (e.g., to meet platform message archiving requirements in mainland China).
- **[agent-collaboration-web](https://github.com/BillShiyaoZhang/agent-collaboration-web)**: User-facing platform that provides agent connectivity anytime, anywhere based on agent-comm and platform. It plans to support human-in-the-loop (HITL) decision-making, transaction confirmation between agents, and agent contacts management. An iOS app is also under development.

## The Workshop

I decided to host the workshop because during the initial prep, many friends expressed great interest but were worried they wouldn't be able to keep up since they hadn't used agents like OpenClaw or Hermes before.

Although the original goal was just a hands-on class starting from scratch, every chat with our speakers brought up fascinating new ideas that made me want to hear their professional, in-depth insights.

Coupled with the preferences indicated in the signup forms, the workshop syllabus has evolved into the following:

### Basic Level
1. OpenClaw or Hermes setup and basic usage
2. How to customize (tune) your agent
3. Practical common Agent design patterns

### Intermediate Level
4. LLM characteristics to consider when using agents
5. Agent development tailored for specific deployment scenarios

### Advanced Level
6. Replacing agent memory using knowledge graphs and ontologies
7. Architectural design analysis of projects like agent-comm, agent-comm-platform, and agent-collaboration-web

### Pending Speaker Confirmation
8. Training, fine-tuning, and iterating customized models for agents
9. Cryptographic applications in agents
10. Analyzing human-agent interactions

---

The above is the tentative course sequence. Feedback is highly welcome, and we can adjust as we go. A single session might cover multiple topics, or a single topic might take several sessions.

For those attending the workshop, please bring a computer running Windows, macOS, or Linux, and ensure you have administrator privileges. If you don't have an API key for your agent (or have no idea what that is), don't worry! Just prepare a budget of around 50 to 200 RMB, and we will guide you on how to set one up during the workshop :D

## Schedule, Location, and Cost

| Aspect | Details |
| :--- | :--- |
| **Time** | • Once a week: 1-hour Workshop first, followed by a 2-hour Initiative session.<br>• **First session: June 18, 14:30 - 17:30**. We will agree on a fixed weekly slot during this first session. |
| **Venue** | Cozy Coffee, 1st Floor, E Building, XJTLU Taicang Campus |
| **Capacity** | • **Initiative:** Unlimited (suggested around 30 to avoid overcrowding).<br>• **Workshop:** Capped at 30 people (to guarantee hands-on guidance). |
| **Cost** | • **Initiative:** Entry with any purchase at Cozy Coffee.<br>• **Workshop:** ¥50 per session, or ¥40 if you also attend the Initiative session on the same day. |
| **Online** | • **Initiative:** No fixed online participation since it's hard to bridge online and offline discussions. However, online keynote speeches are very welcome! :D<br>• **Workshop:** Online streaming/access can be provided, but it is not recommended as speakers can rarely support online attendees effectively in hands-on workshops. |

<div class="letter-footer">
Check out the navigation links above to see the full Schedule, FAQ, and how to Join Us!
</div>
