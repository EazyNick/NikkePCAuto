import cv2
import sys
import os
import numpy as np

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))

try:
    from utils import capture_screen_to_temp
    print("임포트 성공")
except Exception as e:
    print(f"임포트 실패: {e}")


class TemplateMatcher:
    """
    Singleton

    TemplateMatcher Singleton Class: Matches a template image against the current screen.
    """
    _instance = None

    #
    def __new__(cls, *args, **kwargs):
        """
        __new__는 클래스 인스턴스가 생성될 때 호출되는 메서드
        """
        if not cls._instance:
            cls._instance = super(TemplateMatcher, cls).__new__(cls) # __new__ 메서드를 통해 클래스의 단일 인스턴스를 보장.
        return cls._instance

    def __init__(self):
        """
        매칭 전략을 저장하는 변수
        """
        self.matching_strategy = None

    def set_strategy(self, strategy):
        """
        템플릿 매칭에 사용할 전략을 설정합니다.

        V000에서는 opencv grayscale 전략만 있음
        """
        self.matching_strategy = strategy

    def match_template(self, screen_image, template_image):
        """
        화면 이미지와 템플릿 이미지를 매칭하여 결과를 반환합니다.
        
        :param screen_image: 화면 이미지 파일 경로나 numpy 배열
        :param template_image: 템플릿 이미지 파일 경로나 numpy 배열
        :return: Tuple (is_match: bool, top_left: tuple or None)
        """
        if self.matching_strategy is None:
            raise ValueError("Matching strategy is not set.")

        return self.matching_strategy.match(screen_image, template_image)

class ExactMatchStrategy:
    """
    정확한(단순) 템플릿 매칭을 수행하는 전략 클래스.
    """
    def match(self, screen_image, template_image):
        """
        템플릿 매칭을 수행합니다.

        Args:
            screen_image (str or numpy.ndarray): 화면 이미지 경로 또는 numpy 배열.
            template_image (str or numpy.ndarray): 템플릿 이미지 경로 또는 numpy 배열.

        Returns:
            tuple: (is_match: bool, top_left: tuple or None) 매칭 여부와 매칭 좌표.
        """
        if screen_image is None:
            raise ValueError(f"Screen image could not be loaded from {screen_image}")
        if template_image is None:
            raise ValueError(f"Template image could not be loaded from {template_image}")

        # 이미지 경로가 제공된 경우 파일을 로드
        if isinstance(screen_image, str):
            screen_image = cv2.imread(screen_image, cv2.IMREAD_GRAYSCALE)
        if isinstance(template_image, str):
            template_image = cv2.imread(template_image, cv2.IMREAD_GRAYSCALE)

        if screen_image is None:
            raise ValueError(f"GRAYSCALE Screen image could not be loaded from {screen_image}")
        if template_image is None:
            raise ValueError(f"GRAYSCALE Template image could not be loaded from {template_image}")

        # 유효한 이미지인지 확인
        if screen_image is None or template_image is None:
            raise ValueError("Invalid image provided.")

        # 템플릿 매칭 수행
        result = cv2.matchTemplate(screen_image, template_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 임계값 설정
        threshold = 0.8
        if max_val >= threshold:
            return True, max_loc
        else:
            return False, None

if __name__ == "__main__":
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
