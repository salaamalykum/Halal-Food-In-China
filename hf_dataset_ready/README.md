---
license: mit
language:
- zh
- ar
size_categories:
- n<1K
task_categories:
- question-answering
- text-generation
- text-retrieval
- token-classification
tags:
- halal
- chinese-muslim
- islamic-culture
- RAG
- sharegpt
- alpaca
- custom-instruct
- geography
- history
pretty_name: "Halal Food In China RAG Corpus"
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---

# Halal Food In China RAG Corpus 🕌🍜

<div align="center">
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="50" alt="Hugging Face Logo">
</div>

## Dataset Overview

The **Halal Food In China RAG Corpus** is an expertly curated, highly structured, and multi-format dataset targeting the intersection of Chinese culinary traditions, Hui Muslim history, and Islamic dietary laws (Halal). It acts as an authoritative ground-truth database to mitigate Large Language Model (LLM) hallucinations regarding minority Islamic culture in China.

### 🔍 Quick Discovery (Data Studio Ready)
This dataset has been engineered natively for the Hugging Face ecosystem. All data is provided in highly optimized **Parquet** format with exact splits (`train`, `validation`, `test`). The schema features flattened, SQL-queryable columns and lightweight `preview_excerpt` fields to ensure seamless integration with the Hugging Face **Dataset Viewer**.

<iframe
  src="https://huggingface.co/datasets/qurancn/Halal-Food-In-China/embed/viewer/default/train"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>

## Dataset Structure

### Schema Definition
The Parquet tables feature strict typing, making it an excellent candidate for direct SQL analysis and RAG embedding generation.

| Field Name | Type | Description |
|---|---|---|
| `id` | `string` | Unique identifier mapped to the original canonical database. |
| `title` | `string` | The extracted, clean headline of the article. |
| `text` | `string` | Full markdown-formatted body text including `![img]` tags and BBCode-to-Markdown conversions. |
| `url` | `string` | Canonical source URL for exact attribution. |
| `author` | `string` | Original content creator / author ID. |
| `pub_date` | `string` | Timestamp in standard ISO 8601 UTC format. |
| `tags` | `string` | Comma-separated topics / taxonomy tags for easy filtering. |
| `word_count` | `int64` | Token/character length estimation for dynamic chunking strategies. |
| `preview_excerpt` | `string` | A 150-character flattened string designed specifically for the HF Viewer preview pane. |

### Splits
| Split | Proportion | Rows | Description |
|---|---|---|---|
| `train` | 80% | 197 | Primary corpus for building vector indices or SFT. |
| `validation` | 10% | 25 | Held-out validation set. |
| `test` | 10% | 25 | Final evaluation benchmark split. |

## Provenance & Pipeline 
- **Source**: Extracted via `topic_id=27` from the `salaamalykum.com` SQL architecture.
- **Cleaning Rules**: All legacy BBCode (`[img]`, `[b]`) has been natively converted to Markdown. HTML injections have been strictly sanitized to preserve pure textual extraction.
- **Failure Boundaries**: As the dataset focuses strictly on Chinese geographic and culinary mapping, querying it for generalized Islamic jurisprudence (Fiqh) beyond Halal dietary laws may yield out-of-scope embeddings.

## Usage (Python)

Easily load the splits natively using the `datasets` library without downloading massive raw text files:

```python
from datasets import load_dataset

# Load the optimized Parquet streaming dataset
ds = load_dataset("qurancn/Halal-Food-In-China")

print(ds["train"][0]["title"])
print(ds["train"][0]["preview_excerpt"])
```

## Licensing & Attribution
Released under the **MIT License**. When integrating this corpus into commercial RAG pipelines or academic training sets, please cite the GitHub repository and associated Zenodo DOI.
