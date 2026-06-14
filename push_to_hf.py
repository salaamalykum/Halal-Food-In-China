import os
import sys
from huggingface_hub import HfApi

# Ensure the user provided their HF_TOKEN
hf_token = os.environ.get("HF_TOKEN")
if not hf_token:
    print("ERROR: Please set your HF_TOKEN environment variable.")
    print("Example: HF_TOKEN=your_hf_token python3 push_to_hf.py")
    sys.exit(1)

# Initialize the API
api = HfApi(token=hf_token)
repo_id = "qurancn/Halal-Food-In-China"
folder_to_push = os.path.join(os.path.dirname(__file__), "hf_dataset_ready")

print(f"Pushing dataset to {repo_id}...")

try:
    # 1. Create the repo if it doesn't exist
    api.create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)
    
    # 2. Upload the perfectly structured folder
    api.upload_folder(
        folder_path=folder_to_push,
        repo_id=repo_id,
        repo_type="dataset",
        commit_message="Release v1.0.0: Native Parquet splits with structured preview fields and ultimate YAML metadata"
    )
    print("✅ Successfully pushed high-quality structured dataset to Hugging Face!")
    print(f"Check it out at: https://huggingface.co/datasets/{repo_id}")
    
except Exception as e:
    print(f"❌ Failed to push dataset: {e}")
