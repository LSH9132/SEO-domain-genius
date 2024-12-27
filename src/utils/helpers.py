import os
from typing import Dict, Any
from pathlib import Path

def load_env_file(env_path: Path) -> Dict[str, Any]:
    """환경 변수 파일을 로드하고 검증합니다."""
    if not env_path.exists():
        raise FileNotFoundError(f".env 파일이 없습니다: {env_path}")
    
    required_vars = [
        "OPENAI_API_KEY",
        "DEFAULT_MODEL_TYPE",
        "GPT_MODEL_NAME"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"필수 환경 변수가 없습니다: {', '.join(missing_vars)}")

    return {var: os.getenv(var) for var in required_vars}

def validate_model_path() -> bool:
    """Llama 모델 파일의 존재 여부를 확인합니다."""
    from config.settings import LLAMA_MODEL_PATH
    return LLAMA_MODEL_PATH.exists() 