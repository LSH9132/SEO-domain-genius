from langchain_core.runnables import RunnableConfig
from langchain_core.runnables.base import Runnable
from typing import Any, Optional, Dict
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, GPT_MODEL_NAME, DEFAULT_TEMPERATURE

class OpenAIModel(Runnable):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or OPENAI_API_KEY
        self.model = None

    def initialize(self) -> None:
        if not self.api_key:
            raise ValueError("OpenAI API 키가 필요합니다.")
        
        self.model = ChatOpenAI(
            api_key=self.api_key,
            model_name=GPT_MODEL_NAME,
            temperature=DEFAULT_TEMPERATURE
        )

    def invoke(self, input: Any, config: Optional[RunnableConfig] = None) -> str:
        """Runnable 인터페이스 구현"""
        if not self.model:
            self.initialize()
        return self.model.invoke(input)

    def batch(self, inputs: list, config: Optional[RunnableConfig] = None) -> list:
        """배치 처리를 위한 메서드"""
        if not self.model:
            self.initialize()
        return [self.invoke(input, config) for input in inputs] 