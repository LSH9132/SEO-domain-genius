from typing import List, Dict
from src.llm.base import BaseLLM
from src.domain.validator import DomainValidator
from src.domain.analyzer import DomainAnalyzer
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

class DomainGenerator:
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.validator = DomainValidator()
        self.analyzer = DomainAnalyzer()
        self._setup_prompt_template()

    def _setup_prompt_template(self):
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
        # 새로운 방식으로 체인 생성
        self.chain = self.prompt_template | self.llm

    def generate_domains(self, platform_name: str) -> List[Dict]:
        suggestions = self.chain.invoke({"platform_name": platform_name})
        domains = self._parse_suggestions(suggestions)
        
        return [
            {
                "domain": domain,
                "available": self.validator.is_available(domain),
                "seo_benefits": self.analyzer.analyze_seo(domain),
                "brand_meaning": self.analyzer.analyze_brand(domain)
            }
            for domain in domains
            if self.validator.is_valid(domain)
        ]

    def _parse_suggestions(self, suggestions: str) -> List[str]:
        domains = []
        lines = suggestions.split('\n')
        for line in lines:
            if '도메인:' in line:
                domain = line.split('도메인:')[1].strip()
                if domain.endswith('.com'):
                    domains.append(domain)
        return domains 