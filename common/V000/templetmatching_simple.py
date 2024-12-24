import cv2
import sys
import os
import numpy as np


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("logs"))

try:
    from utils import capture_screen
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")

class TemplateMatcher:
    """
    Singleton

    TemplateMatcher Singleton Class: Matches a template image against the current screen.
    """
    _instance = None
    
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
                template_image (str): 템플릿 이미지 파일명 (기본 이미지 경로).

            Returns:
                tuple: (is_match: bool, top_left: tuple or None) 매칭 여부와 매칭 좌표.
            """
            if isinstance(screen_image, str):
                screen_image_data = cv2.imread(screen_image, cv2.IMREAD_GRAYSCALE)
            else:
                screen_image_data = screen_image

            if screen_image_data is None:
                raise ValueError(f"Screen image could not be loaded from {screen_image}")

            # 템플릿 이미지 파일 이름 변형 리스트 생성
            template_variations = [
                template_image,
                *[f"{template_image.split('.')[0]}{i}.png" for i in range(1, 3)]
            ]

            for template_path in template_variations:
                template_image_data = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
                print(template_path)
                if template_image_data is None:
                    log_manager.logger.warning(f"Template image could not be loaded from {template_path}, skipping...")
                    continue

                # 템플릿 매칭 수행
                result = cv2.matchTemplate(screen_image_data, template_image_data, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                # 임계값 설정
                threshold = 0.91
                if max_val >= threshold:
                    # 매칭된 영역의 중앙 좌표 계산
                    template_height, template_width = template_image_data.shape[:2]
                    center_x = max_loc[0] + template_width // 2
                    center_y = max_loc[1] + template_height // 2
                    log_manager.logger.info(f"Template matched: {template_path} with confidence {max_val}")
                    return True, (center_x, center_y)
                else:
                    log_manager.logger.info(f"템플릿 매칭 실패 - 매칭값: {max_val}, 쓰레시홀드: {threshold}")
                
            return False, None

            # 모든 템플릿 이미지에서 매칭 실패
            log_manager.logger.info("No matching template found.")
            return False, None

if __name__ == "__main__":
    # TemplateMatcher 인스턴스 생성
    matcher = TemplateMatcher()

    # 매칭 전략 설정
    matcher.set_strategy(ExactMatchStrategy())

    # 현재 화면 캡처
    captured_screen_path = capture_screen()

    # 템플릿 매칭 수행 (정확한 경로 사용)
    template_path = os.path.join(os.getcwd(), "assets", "test", "test.png")  # 현재 폴더 기준 절대 경로 생성

    try:
        # 템플릿 매칭 수행
        is_match, location = matcher.match_template(captured_screen_path, template_path)

        if is_match:
            log_manager.logger.info(f"Template matched at location: {location}")
        else:
            log_manager.logger.info("Template did not match.")
    except ValueError as e:
        log_manager.logger.info(f"Error during matching: {e}")

    def run():
        """
        방주
        """

        assets_login_path = path_manager.get_path("assets_ark")
        process_step = matcher.match_template(base_path=assets_login_path)
        log_manager.logger.info("방주 프로세스를 시작합니다.")

        # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
        steps = [
            {"step": "1단계: 방주 이동", "image_name_or_coords": "d_start.png", "wait": 3},
        ]

        # 각 단계 실행
        for step in steps:
            if not process_step.execute(
                step["step"], 
                step["image_name_or_coords"], 
                step.get("double_click", False), 
                step.get("drag"),
                step.get("window_name"),
                step.get("retry", 10),
                step["wait"]
            ):
                log_manager.logger.error(f"{step.get('step', '단계 이름 없음')} 실패로 자동화 종료")
                return  # 단계 실패 시 함수 종료
    run()
