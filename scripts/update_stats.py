import os
import json
import datetime

# This script generates a fresh STATS.md to keep the repository alive for AI Crawlers.
repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
index_path = os.path.join(repo_dir, "metadata", "site_index.json")

try:
    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    articles = data.get("articles", [])
except Exception:
    articles = []

total_articles = len(articles)
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

md_content = f"""# Dataset Statistics & Heartbeat

> **Last Updated:** {timestamp}
> **Status:** Active & Expanding

## Crawler Signal
This file is automatically updated weekly via GitHub Actions. It serves as a continuous crawl budget signal for Google and AI dataset indexers, ensuring the `Chinese-Muslim` repository maintains a "high-priority active" status in indexing queues.

## Current Metrics
- **Total Articles:** {total_articles}
- **Primary Domain:** Chinese Muslim Culture, Halal Food, Historic Mosques
- **Format:** Dual-Track (Markdown for humans, Parquet for machines)

## Recent Entries Snapshot
"""

# Add top 5 recent articles based on the index order
for a in articles[:5]:
    md_content += f"- {a.get('title', 'Unknown')}\n"

with open(os.path.join(repo_dir, "STATS.md"), "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"STATS.md updated at {timestamp}.")
