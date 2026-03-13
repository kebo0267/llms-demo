'''Download the Qwen3.5-35B-A3B mxfp4 GGUF model from HuggingFace.

Downloads into models/hugging_face (respects $HF_HOME if set).
Only downloads the BF16 GGUF file.

Usage:
    python utils/download_qwen35_35b.py
'''

import os

from dotenv import load_dotenv
from huggingface_hub import snapshot_download

load_dotenv()

snapshot_download(
    repo_id='noctrex/Qwen3.5-35B-A3B-MXFP4_MOE-GGUF',
    allow_patterns=['*BF16.gguf'],
    token=os.environ.get('HF_TOKEN'),
)
