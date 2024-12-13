from common.V000 import TemplateMatcher, ExactMatchStrategy
from utils import capture_screen_to_temp

def main():
    






if __name__ == "__main__":
    import cv2
    # TemplateMatcher 인스턴스 생성
    matcher = TemplateMatcher()

    # 매칭 전략 설정
    matcher.set_strategy(ExactMatchStrategy())

    # 현재 화면 캡처
    captured_screen_path = capture_screen_to_temp()

    # 템플릿 매칭 수행 (정확한 경로 사용)
    template_path = r"C:\Users\User\Desktop\python\auto\python\NikkePCAuto\assets\test\test.png" # 절대 경로 생성

    img = cv2.imread(captured_screen_path)

    if captured_screen_path is None:
        raise ValueError("Screen image could not be loaded.")
    if template_path is None:
        raise ValueError("Template image could not be loaded.")

    is_match, location = matcher.match_template(captured_screen_path, template_path)

    if is_match:
        print(f"Template matched at location: {location}")
    else:
        print("Template did not match.")