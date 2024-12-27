from abc import ABC, abstractmethod
from typing import List, Dict

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def initialize(self) -> None:
        pass 