# Fun Workshop 2026 Summer & ClawTwin Initiative Website

Welcome! This repository hosts the source code for the **Fun Workshop 2026 Summer** and **ClawTwin Initiative** website, a single-page application (SPA) designed to be highly readable and accessible for both human users and AI agents.

## Repository Overview

To keep the codebase easy to maintain and prevent duplication, all core content is stored exactly once per language inside clean Markdown files under the `components/` directory. The main website dynamically fetches, parses, and renders these Markdown files client-side using [marked.js](https://marked.js.org/).

## Agent Guidance (llms.txt)

If you are an AI agent reading this repository to answer questions about the workshop, you can find the single source of truth for all content mapped below.

### Content Directory Map

| Section | English Source | Chinese Source | Description |
| :--- | :--- | :--- | :--- |
| **Letter** | [`components/letter_en.md`](components/letter_en.md) | [`components/letter_zh.md`](components/letter_zh.md) | Introduction, background, and rationale for the ClawTwin Initiative and Summer Workshop. |
| **Program** | [`components/program_en.md`](components/program_en.md) | [`components/program_zh.md`](components/program_zh.md) | Activities, logistics (time, location, tickets), risk warnings, and list of co-organizers. |
| **Syllabus** | [`components/syllabus_en.md`](components/syllabus_en.md) | [`components/syllabus_zh.md`](components/syllabus_zh.md) | Zero-to-One workshop lesson path, schedule of sessions, topics, and prerequisites. |
| **Detailed Syllabus** | [`syllabus-detailed.md`](syllabus-detailed.md) | - | Exhaustive per-session plan with course rhythm, topics, hands-on tasks, and acceptance criteria. |
| **FAQ** | [`components/faq_en.md`](components/faq_en.md) | [`components/faq_zh.md`](components/faq_zh.md) | Frequently asked questions about agents, LLMs, privacy security, and prerequisites. |
| **Join Us** | [`components/join_en.md`](components/join_en.md) | [`components/join_zh.md`](components/join_zh.md) | Role descriptions and signup application form details. |

---

## Technical Architecture & Development

The website is a lightweight Single-Page Application (SPA):
1. **Core**: `index.html` implements client-side hash routing (`#letter`, `#program`, `#syllabus`, `#faq`, `#join`) and loads the appropriate language Markdown file.
2. **Markdown Parser**: Uses `marked.js` loaded via CDN to translate Markdown into HTML at runtime.
3. **Styling**: `assets/main.css` contains the design tokens, fonts, and specific layouts for all components (letters, syllabus cards, FAQ accordions, and join forms) including full light/dark mode support.

### Running Locally

You can run the website locally by starting any static file server from the root directory:

```bash
# Using Python
python3 -m http.server 8000

# Using Node (npm)
npx http-server -p 8000
```

Then open `http://localhost:8000` in your browser.
