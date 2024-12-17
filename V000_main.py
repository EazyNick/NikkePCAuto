from common.V000 import TemplateMatcher, ExactMatchStrategy
from utils import capture_screen
from logs import log_manager

def main():
    






if __name__ == "__main__":
    import cv2
    import os
    # TemplateMatcher 인스턴스 생성
    matcher = TemplateMatcher()

    # 매칭 전략 설정
    matcher.set_strategy(ExactMatchStrategy())

    # 현재 화면 캡처
    captured_screen_path = capture_screen()

    # 템플릿 매칭 수행 (정확한 경로 사용)
    # 루트 디렉토리 설정 (NikkePCAuto)
    base_dir = os.path.abspath(__file__)  # 현재 파일 절대 경로
    # 템플릿 이미지 경로 설정
    template_path = os.path.join(base_dir, "assets", "test", "test.png")

    img = cv2.imread(captured_screen_path)

    if captured_screen_path is None:
        raise ValueError("Screen image could not be loaded.")
    if template_path is None:
        raise ValueError("Template image could not be loaded.")

    is_match, location = matcher.match_template(captured_screen_path, template_path)

    if is_match:
        log_manager.logger.info(f"Template matched at location: {location}")
    else:
        log_manager.logger.info("Template did not match.")