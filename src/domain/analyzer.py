from typing import Dict, Optional

class DomainAnalyzer:
    def __init__(self):
        pass

    def analyze_seo(self, domain: str) -> Dict[str, str]:
        """도메인의 SEO 관점에서의 장점을 분석합니다."""
        seo_score = self._calculate_seo_score(domain)
        return {
            "length": self._analyze_length(domain),
            "memorability": self._analyze_memorability(domain),
            "keyword_relevance": self._analyze_keywords(domain),
            "overall_score": str(seo_score)
        }

    def analyze_brand(self, domain: str) -> Dict[str, str]:
        """도메인의 브랜드 관점에서의 의미를 분석합니다."""
        return {
            "brand_potential": self._analyze_brand_potential(domain),
            "uniqueness": self._analyze_uniqueness(domain)
        }

    def _calculate_seo_score(self, domain: str) -> float:
        # 기본적인 SEO 점수 계산 로직
        base_score = 100
        
        # 도메인 길이에 따른 감점
        if len(domain) > 15:
            base_score -= (len(domain) - 15) * 2
        
        # 하이픈 사용에 따른 감점
        base_score -= domain.count('-') * 5
        
        return max(0, min(100, base_score))

    def _analyze_length(self, domain: str) -> str:
        length = len(domain)
        if length <= 10:
            return "최적의 길이"
        elif length <= 15:
            return "적절한 길이"
        else:
            return "다소 긴 길이"

    def _analyze_memorability(self, domain: str) -> str:
        # 기억하기 쉬운 정도 분석
        if len(domain) <= 8:
            return "매우 기억하기 쉬움"
        elif len(domain) <= 12:
            return "기억하기 쉬움"
        else:
            return "다소 기억하기 어려움"

    def _analyze_keywords(self, domain: str) -> str:
        # 키워드 관련성 분석
        return "키워드 분석 결과"

    def _analyze_brand_potential(self, domain: str) -> str:
        # 브랜드 잠재력 분석
        return "브랜드 잠재력 분석 결과"

    def _analyze_uniqueness(self, domain: str) -> str:
        # 고유성 분석
        return "고유성 분석 결과" 