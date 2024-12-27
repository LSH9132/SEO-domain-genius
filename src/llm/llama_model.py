from .base import BaseLLM
from langchain_community.llms import LlamaCpp
from config.settings import (
    LLAMA_MODEL_PATH,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_CONTEXT_LENGTH,
    DEFAULT_THREADS
)

class LlamaModel(BaseLLM):
    def __init__(self):
        self.model = None

    def initialize(self) -> None:
        if not LLAMA_MODEL_PATH.exists():
            raise FileNotFoundError(f"모델 파일이 없습니다: {LLAMA_MODEL_PATH}")
        
        self.model = LlamaCpp(
            model_path=str(LLAMA_MODEL_PATH),
            temperature=DEFAULT_TEMPERATURE,
            max_tokens=DEFAULT_MAX_TOKENS,
            n_ctx=DEFAULT_CONTEXT_LENGTH,
            n_threads=DEFAULT_THREADS
        )

    def generate(self, prompt: str) -> str:
        if not self.model:
            self.initialize()
        return self.model.predict(prompt) 