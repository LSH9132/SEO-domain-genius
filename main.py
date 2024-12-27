from src.llm.openai_model import OpenAIModel
from src.llm.llama_model import LlamaModel
from src.domain.generator import DomainGenerator
from src.utils.helpers import load_env_file
from config.settings import DEFAULT_MODEL_TYPE
from pathlib import Path
import argparse

def main():
    # 환경 변수 로드 및 검증
    env_path = Path(__file__).parent / ".env"
    env_vars = load_env_file(env_path)

    parser = argparse.ArgumentParser(description='도메인 이름 생성기')
    parser.add_argument('platform_name', help='플랫폼 이름')
    parser.add_argument('--model-type', default=DEFAULT_MODEL_TYPE, 
                       choices=['openai', 'llama'], help='사용할 모델 타입')
    args = parser.parse_args()

    # 모델 초기화
    if args.model_type == 'openai':
        llm = OpenAIModel()
    else:
        llm = LlamaModel()

    # 도메인 생성기 초기화 및 실행
    generator = DomainGenerator(llm)
    domains = generator.generate_domains(args.platform_name)
    
    # 결과 출력
    for domain in domains:
        print(f"\n도메인: {domain['domain']}")
        print(f"사용 가능 여부: {domain['available']}")
        print(f"SEO 장점: {domain['seo_benefits']}")
        print(f"브랜드 의미: {domain['brand_meaning']}")

if __name__ == "__main__":
    main()
