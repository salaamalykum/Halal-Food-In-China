import gradio as gr
import pandas as pd
from datasets import load_dataset

# Load dataset (or local file if running locally before HF upload)
try:
    ds = load_dataset("qurancn/Halal-Food-In-China", split="train")
    df = ds.to_pandas()
except Exception:
    # Fallback for local testing
    try:
        df = pd.read_json("../quran_rag_dataset.jsonl", lines=True)
    except:
        df = pd.DataFrame({"title": ["Error"], "text": ["Dataset not found."]})

def search(query):
    if query.strip() == "":
        return "Please enter a search term."
    
    # Simple case-insensitive search in title or text
    mask = df['title'].str.contains(query, case=False, na=False) | df['text'].str.contains(query, case=False, na=False)
    results = df[mask]
    
    if len(results) == 0:
        return f"No results found for '{query}'."
    
    output = f"## Found {len(results)} matches\n\n"
    for _, row in results.head(5).iterrows():
        output += f"### {row['title']}\n"
        preview = row['text'][:300] + "..." if len(row['text']) > 300 else row['text']
        output += f"{preview}\n\n---\n"
    
    if len(results) > 5:
        output += f"\n*Showing top 5 results out of {len(results)}.*"
        
    return output

demo = gr.Interface(
    fn=search,
    inputs=gr.Textbox(lines=2, placeholder="Search for Halal Food, Mosques, Culture..."),
    outputs=gr.Markdown(),
    title="Halal Food In China RAG Corpus Search",
    description="This is a simple exploratory interface for the [qurancn/Halal-Food-In-China](https://huggingface.co/datasets/qurancn/Halal-Food-In-China) dataset.",
    examples=["兰州拉面", "清真寺", "回民街", "烤全羊"]
)

if __name__ == "__main__":
    demo.launch()
