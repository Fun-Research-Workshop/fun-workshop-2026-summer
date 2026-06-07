#!/usr/bin/env python3
import os
import re

# Configurations
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
COMPONENTS_DIR = os.path.join(WORKSPACE_DIR, "components")
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "llms.txt")

# Project static metadata (can be updated here)
TITLE = "Fun Workshop 2026 Summer & ClawTwin Initiative"
SUBTITLE = "Repository manifest optimized for LLMs and AI agents."
OVERVIEW = (
    "This repository contains the source code and content for the Fun Workshop 2026 Summer website. "
    "The website is structured as a single-page app that dynamically renders markdown files. "
    "All core information is located in the Markdown source files under the `components/` directory."
)

METADATA = """- **Venue**: Cozy Coffee, 1st Floor, E Building, XJTLU Taicang Campus, Suzhou, China.
- **Timeline**: June - August, 2026.
- **First Session**: June 18, 2026.
- **Prerequisites**: Laptop (Windows/macOS/Linux with admin privileges) and a budget of 50-200 RMB for model APIs.
- **Fees**: Initiative is free (with Cozy Coffee purchase); Workshop is 50 RMB per session (40 RMB if attending the Initiative).
- **Coordinator**: Shiyao Zhang (shiyao.zhang14@student.xjtlu.edu.cn)."""


def extract_markdown_info(filepath):
    """
    Extracts the main heading (# Title) and the first paragraph of a markdown file
    to use as the link text and description in llms.txt.
    """
    title = None
    description = ""

    if not os.path.exists(filepath):
        return None, ""

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        # Parse lines
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped:
                continue

            # Extract title if not found yet
            if title is None:
                match = re.match(r"^#\s+(.+)$", stripped)
                if match:
                    title = match.group(1).strip()
                else:
                    # Fallback title if first non-empty line isn't a heading
                    title = os.path.basename(filepath)
                continue

            # Extract first paragraph as description (skip style/html tags or other headers)
            if not description:
                if stripped.startswith("<") or stripped.startswith("<!--") or stripped.startswith("#"):
                    continue
                # Clean up markdown styling from description
                clean_desc = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", stripped)  # remove links
                clean_desc = re.sub(r"[\*_`]", "", clean_desc)  # remove bold/italic/code ticks
                description = clean_desc[:150] + ("..." if len(clean_desc) > 150 else "")

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    # Fallback title if none was found
    if not title:
        title = os.path.basename(filepath)

    return title, description


def generate_llms_txt():
    # 1. Collect all markdown files in components/
    files = []
    if os.path.exists(COMPONENTS_DIR):
        for f in sorted(os.listdir(COMPONENTS_DIR)):
            if f.endswith(".md"):
                files.append(os.path.join(COMPONENTS_DIR, f))

    # 2. Extract info for each file
    content_links = []
    for filepath in files:
        rel_path = os.path.relpath(filepath, WORKSPACE_DIR)
        title, desc = extract_markdown_info(filepath)
        lang_suffix = " (Chinese)" if rel_path.endswith("_zh.md") else ""
        
        # Add descriptive link line
        link_line = f"- [{title}{lang_suffix}]({rel_path})"
        if desc:
            link_line += f" - {desc}"
        content_links.append(link_line)

    # 3. Add other top-level markdown files (like syllabus-detailed.md)
    detailed_syllabus = os.path.join(WORKSPACE_DIR, "syllabus-detailed.md")
    if os.path.exists(detailed_syllabus):
        rel_path = os.path.relpath(detailed_syllabus, WORKSPACE_DIR)
        title, desc = extract_markdown_info(detailed_syllabus)
        link_line = f"- [{title}]({rel_path})"
        if desc:
            link_line += f" - {desc}"
        content_links.append(link_line)

    # 4. Build output string
    output_lines = [
        f"# {TITLE}",
        "",
        f"> {SUBTITLE}",
        "",
        OVERVIEW,
        "",
        "## Core Information Index",
        "",
    ]
    
    output_lines.extend(content_links)
    output_lines.extend([
        "",
        "## Key Metadata",
        METADATA,
        ""
    ])

    # 5. Write to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"Successfully generated llms.txt with {len(content_links)} indexes.")


if __name__ == "__main__":
    generate_llms_txt()
