from llama_cpp import Llama
from pathlib import Path

MODEL_PATH = Path("app/models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf")

def load_llm():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found. Expected at models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf"
        )

    return Llama(
        model_path=str(MODEL_PATH),
        n_ctx=2048,
        n_threads=8,     # adjust automatically later if you want
        verbose=False
    )
