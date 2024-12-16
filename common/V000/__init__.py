from .templetmatching_simple import TemplateMatcher, ExactMatchStrategy
from .action_handler import ActionHandler

# 전역 TemplateMatcher 인스턴스 생성
matcher = TemplateMatcher()
matcher.set_strategy(ExactMatchStrategy())  # 기본 매칭 전략 설정

# __init__.py에서 matcher를 노출
__all__ = ["matcher"]