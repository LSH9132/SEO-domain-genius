from pathlib import Path
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 기본 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
LLAMA_MODEL_PATH = MODEL_DIR / os.getenv("LLAMA_MODEL_PATH", "llama-3.2.bin")

# API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 모델 설정
DEFAULT_MODEL_TYPE = os.getenv("DEFAULT_MODEL_TYPE", "openai")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "2000"))
DEFAULT_CONTEXT_LENGTH = int(os.getenv("DEFAULT_CONTEXT_LENGTH", "2048"))
DEFAULT_THREADS = int(os.getenv("DEFAULT_THREADS", "4"))

# GPT 모델 설정
GPT_MODEL_NAME = os.getenv("GPT_MODEL_NAME", "gpt-3.5-turbo")