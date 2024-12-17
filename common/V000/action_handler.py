import pyautogui
import os
import sys

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("common"))

try:
    from utils import capture_screen
    from common.V000 import matcher
    from logs import log_manager
except Exception as e:
    log_manager.logger.info(f"임포트 실패: {e}")

class ActionHandler:
    """
    ActionHandler Singleton Class: 화면 조작(클릭, 이동 등)을 관리하는 클래스.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ActionHandler, cls).__new__(cls)
        return cls._instance

    def click(self, x, y, button="left"):
        """
        지정된 좌표를 클릭합니다.

        Args:
            x (int): 클릭할 X 좌표.
            y (int): 클릭할 Y 좌표.
            button (str): 클릭할 버튼 ("left", "right", "middle").
        """
        pyautogui.click(x=x, y=y, button=button)
        log_manager.logger.info(f"Clicked at ({x}, {y}) with button {button}")

    def move_to(self, x, y, duration=0.5):
        """
        지정된 좌표로 마우스를 이동합니다.

        Args:
            x (int): 이동할 X 좌표.
            y (int): 이동할 Y 좌표.
            duration (float): 이동 시간 (초 단위).
        """
        pyautogui.moveTo(x, y, duration=duration)
        log_manager.logger.info(f"Moved to ({x}, {y}) in {duration} seconds")

    def drag_to(self, x, y, duration=0.5, button="left"):
        """
        마우스를 드래그합니다.

        Args:
            x (int): 드래그 종료 X 좌표.
            y (int): 드래그 종료 Y 좌표.
            duration (float): 드래그 시간 (초 단위).
            button (str): 드래그할 버튼 ("left", "right", "middle").
        """
        pyautogui.dragTo(x, y, duration=duration, button=button)
        log_manager.logger.info(f"Dragged to ({x}, {y}) in {duration} seconds with button {button}")

if __name__ == "__main__":
    # TemplateMatcher 인스턴스 생성
    # 현재 화면 캡처 및 템플릿 경로 설정
    captured_screen_path = capture_screen()
    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))  # 루트 디렉토리 경로

    # 템플릿 이미지 경로 설정
    template_path = os.path.join(project_root, "assets", "test", "test.png")

    # 템플릿 매칭 수행
    is_match, location = matcher.match_template(captured_screen_path, template_path)

    if is_match:
        log_manager.logger.info(f"Template matched at location: {location}")

        # ActionHandler 인스턴스 생성
        action_handler = ActionHandler()

        # 좌표 클릭
        action_handler.click(x=location[0], y=location[1])

        # 마우스 이동
        action_handler.move_to(x=location[0] + 100, y=location[1] + 100)

        # 드래그 예시
        action_handler.drag_to(x=location[0] + 200, y=location[1] + 200)
    else:
        log_manager.logger.info("Template did not match.")

