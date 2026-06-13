---
language:
- zh
license: mit
task_categories:
- text-retrieval
- text-generation
- question-answering
tags:
- islam
- rag
- chinese-muslim
- knowledge-base
- instruction-tuning
pretty_name: Chinese Muslim Knowledge Base
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: corpus
    path: data/corpus.parquet
  - split: rag_chunks
    path: data/rag_chunks.parquet
---

# Chinese Muslim Knowledge Base & RAG Dataset

This dataset contains 247 high-quality, human-curated articles about Chinese Muslim culture, mosques, halal food, and travel guidelines, meticulously extracted from [Salaamalykum.com](https://salaamalykum.com).

## Dataset Structure

The dataset is strictly partitioned into two splits for optimized AI training and RAG (Retrieval-Augmented Generation) pipelines:

1. **`corpus`**: The full-length articles containing raw, clean Markdown text. Best for continuous pre-training (CPT) or bulk knowledge extraction.
2. **`rag_chunks`**: The articles deterministically chunked into paragraph-level segments. Best for embedding generation, vector database ingestion, and instruction-tuning retrieval tasks.

### Data Dictionary

Both splits feature strongly typed Parquet columns optimized for SQL Data Studio filtering:

| Field | Type | Description |
|-------|------|-------------|
| `url` | `string` | The canonical source URL. In `rag_chunks`, this includes the `#chunk-id` anchor. |
| `title` | `string` | The original title of the article. |
| `text` | `string` | The sanitized Markdown content. |
| `timestamp` | `string` | ISO 8601 publication or scraping timestamp. |
| `language` | `string` | `zh-CN` (Simplified Chinese). |
| `tags` | `string` | Serialized JSON array of author-defined categorization tags. |
| `content_hash` | `string` | (Corpus only) SHA-256 hash of the `text` field for deduplication. |
| `chunk_index` | `int` | (RAG only) The zero-indexed position of the chunk in the original article. |

## Data Provenance & Cleaning Rules

All contents are strictly mirrored from the original author `yusuf908` on Salaamalykum. 

**Cleaning Rules:**
- Extracted natively from WeCenter `message` fields via Regex DOM-bypass.
- `<br>` tags normalized to `\n`.
- Embedded `<img>` attributes strictly converted to valid Markdown syntax `![image](src)`.
- Triplicate or more `\n` suppressed to `\n\n`.

**Failure Edges & Anomalies:**
- Articles containing highly complex nested tables or external iframe embeds (e.g., YouTube/Bilibili videos) will have those specific elements stripped, preserving only the textual context.
- Short form comments and discussions are excluded; this dataset focuses strictly on long-form articles.

## Embedding Atlas Architecture (Pre-computation Ready)

This dataset is fully compatible with the Hugging Face **Embedding Atlas**. The `rag_chunks` split is designed specifically for Nomic Atlas or UMAP visualization. Future iterations will include pre-computed multi-lingual embeddings (e.g., `bge-m3`) mapped directly to the `text` column to visualize the thematic clusters of Chinese Muslim geography and Halal culinary distributions.

## Human-Readable View

For the human-readable GitHub Pages deployment with a highly-indexed glassmorphism UI, visit: [https://salaamalykum.github.io/Halal-Food-In-China](https://salaamalykum.github.io/Halal-Food-In-China)
