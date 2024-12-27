import whois
from typing import Optional

class DomainValidator:
    def __init__(self):
        pass

    def is_valid(self, domain: str) -> bool:
        """도메인 이름이 유효한지 검사합니다."""
        # 기본적인 도메인 규칙 검사
        if not domain or len(domain) > 253:
            return False
        
        # 영문 소문자, 숫자, 하이픈만 허용
        valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-.')
        if not all(c in valid_chars for c in domain):
            return False
        
        # 하이픈으로 시작하거나 끝나면 안됨
        if domain.startswith('-') or domain.endswith('-'):
            return False
        
        return True

    def is_available(self, domain: str) -> bool:
        """도메인이 등록 가능한지 확인합니다."""
        try:
            w = whois.whois(domain)
            return w.domain_name is None
        except Exception:
            # whois 조회 실패 시 기본적으로 사용 불가능으로 처리
            return False 