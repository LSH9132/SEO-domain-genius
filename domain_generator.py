from langchain_community.llms import LlamaCpp
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import whois
import requests
import os
from typing import Literal

class DomainGenerator:
    def __init__(self, model_type: Literal["llama", "openai"] = "openai", openai_api_key: str = None):
        """
        Args:
            model_type: "llama" 또는 "openai" 선택
            openai_api_key: OpenAI API 키 (model_type이 "openai"일 때 필요)
        """
        self.model_type = model_type
        
        if model_type == "llama":
            model_path = os.path.join(os.path.dirname(__file__), "models", "llama-3.2.bin")
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"모델 파일이 없습니다: {model_path}")
                
            self.llm = LlamaCpp(
                model_path=model_path,
                temperature=0.7,
                max_tokens=2000,
                n_ctx=2048,
                n_threads=4
            )
        else:  # openai
            if not openai_api_key:
                openai_api_key = os.getenv("OPENAI_API_KEY")
                if not openai_api_key:
                    raise ValueError("OpenAI API 키가 필요합니다.")
            
            self.llm = ChatOpenAI(
                api_key=openai_api_key,
                model_name="gpt-4",  # 또는 "gpt-3.5-turbo"
                temperature=0.7
            )
        
        self.prompt_template = PromptTemplate(
            input_variables=["platform_name"],
            template="""
            다음 플랫폼을 위한 SEO 친화적인 도메인 이름을 5개 생성해주세요:
            플랫폼: {platform_name}
            
            각 도메인에 대해 다음 형식으로 응답해주세요:
            1. 도메인: [도메인명]
               SEO 장점: [장점 설명]
               브랜드 의미: [의미 설명]
            
            주의사항:
            - 짧고 기억하기 쉬운 도메인
            - 영문 소문자만 사용
            - 하이픈(-) 최소화
            - .com 도메인 위주
            """
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def is_domain_available(self, domain):
        try:
            w = whois.whois(domain)
            return w.domain_name is None
        except:
            return True
            
    def generate_domains(self, platform_name):
        suggestions = self.chain.run(platform_name=platform_name)
        available_domains = []
        
        # LLM 응답 파싱
        domains = self._parse_suggestions(suggestions)
        
        for domain in domains:
            if self.is_domain_available(domain):
                available_domains.append({
                    "domain": domain,
                    "available": True,
                    "seo_benefits": self._analyze_seo_benefits(domain),
                    "brand_meaning": self._get_brand_meaning(domain)
                })
                
        return available_domains
    
    def _parse_suggestions(self, suggestions):
        # 여기에 실제 파싱 로직 구현
        # 예시 구현:
        domains = []
        for line in suggestions.split('\n'):
            if line.strip().startswith('도메인:'):
                domain = line.split(':')[1].strip()
                if domain.endswith('.com'):
                    domains.append(domain)
        return domains
        
    def _analyze_seo_benefits(self, domain):
        # SEO 분석 로직 구현
        pass
        
    def _get_brand_meaning(self, domain):
        # 브랜드 의미 분석 로직 구현
        pass

# OpenAI API 사용
generator_openai = DomainGenerator(
    model_type="openai",
    openai_api_key="your-api-key-here"
)

# 또는 환경 변수에서 API 키 가져오기
import os
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
generator_openai = DomainGenerator(model_type="openai")

# Llama 모델 사용
generator_llama = DomainGenerator(model_type="llama")

# 도메인 생성
domains = generator_openai.generate_domains("온라인 쇼핑몰")
for domain in domains:
    print(f"도메인: {domain['domain']}")
    print(f"사용 가능 여부: {domain['available']}")
    print(f"SEO 장점: {domain['seo_benefits']}")
    print(f"브랜드 의미: {domain['brand_meaning']}")
    print("---")