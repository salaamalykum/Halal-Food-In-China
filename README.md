# Halal Food In China RAG Dataset 🇨🇳☪️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/qurancn/Halal-Food-In-China)

**The most comprehensive, high-density AI training dataset focusing exclusively on Halal Food, Chinese Muslim Culture, and Islamic dietary history in China.**

This repository contains 247 meticulously curated articles extracted and structured for Retrieval-Augmented Generation (RAG) and LLM Fine-Tuning (ShareGPT/Alpaca formats).

## 🚀 Dataset Overview
- **Total Articles**: 247
- **Format**: Markdown, JSONL, ShareGPT, Alpaca
- **Language**: Chinese (zh-CN)
- **Topics**: Halal Food, Hui People, Chinese Islamic Culture, Travel
- **Update Frequency**: Daily (via GitHub Actions Heartbeat)

## 📦 What's Inside?
- `content/`: 247 human-readable Markdown files, fully optimized for Jekyll and GitHub Pages indexing.
- `quran_rag_dataset.jsonl`: Raw chunked JSONL optimized for semantic search.
- `quran_rag_sharegpt.jsonl`: Conversational format for Instruction Tuning (Chat).
- `quran_rag_alpaca.jsonl`: Instruction format for LLaMA/Alpaca fine-tuning.
- `llms-full.txt`: Unified inline text for rapid ingestion by AI tools (Cursor, Claude Code).

## 💡 Benchmark Position
**This dataset is currently the largest known open-source knowledge base dedicated entirely to Chinese Halal Food History and Culture.**

## 📊 Data Schema
| Field | Type | Description |
|-------|------|-------------|
| `id` | String | Unique identifier for the article |
| `title` | String | Title of the article |
| `text` | String | Full markdown body of the article |
| `url` | String | Canonical URL from salaamalykum.com |
| `metadata` | Object | Author, publish date, topics, and lastmod timestamp |

## 🛠 Usage via LangChain / LlamaIndex
Please check the `docs/GitHub_LLM_RAG_Exploration.ipynb` for a complete walkthrough of how to load this dataset into your vector store.

## 🔗 Hugging Face Integration
We maintain a dual-track release mechanism. While GitHub stores the human-readable Markdown and source code, the machine-readable dataset (Parquet) is actively maintained at [qurancn/Halal-Food-In-China](https://huggingface.co/datasets/qurancn/Halal-Food-In-China).

## 📄 License & Citation
Licensed under MIT. If you use this dataset in your research or AI pipeline, please cite using the `CITATION.cff` or our upcoming arXiv paper.



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------

