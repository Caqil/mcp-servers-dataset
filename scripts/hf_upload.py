"""Uploads the Hugging Face copy of the dataset (export.py --hf DIR) to huggingface.co/datasets/hostedmcp/mcp-servers-dataset.
The token comes from HF_TOKEN (the dataset repo's GitHub secret) or ~/.config/hostedmcp/hf_token (fine-grained, write
access to the hostedmcp org) and is never printed."""
import os
import sys

from huggingface_hub import HfApi

REPO = "hostedmcp/mcp-servers-dataset"
folder = sys.argv[1]
token = os.environ.get("HF_TOKEN") or open(os.path.expanduser("~/.config/hostedmcp/hf_token")).read().strip()
api = HfApi(token=token)
api.create_repo(REPO, repo_type="dataset", exist_ok=True, private=False)
info = api.upload_folder(repo_id=REPO, repo_type="dataset", folder_path=folder, commit_message="Weekly export from hostedmcp.org")
print(f"uploaded: {info.commit_url}")
