from .templetmatching import TemplateMatcher, ExactMatchStrategy

matcher = TemplateMatcher()
matcher.set_strategy(ExactMatchStrategy())

__all__ = ["matcher"]
