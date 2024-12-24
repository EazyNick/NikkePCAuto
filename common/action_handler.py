import pyautogui
import os
import sys


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("common"))

try:
    from utils import capture_screen
    from common import matcher
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")

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

    def double_click(self, x, y, button="left"):
        """
        지정된 좌표를 더블클릭합니다.

        Args:
            x (int): 클릭할 X 좌표.
            y (int): 클릭할 Y 좌표.
            button (str): 클릭할 버튼 ("left", "right", "middle").
        """
        pyautogui.click(x=x, y=y, clicks=2, button=button, interval=0.1)
        log_manager.logger.info(f"Double-clicked at ({x}, {y}) with button {button}")

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

    def drag(self, start_x, start_y, end_x, end_y, duration=0.5):
        """
        지정된 시작 좌표에서 끝 좌표로 마우스를 드래그합니다.

        Args:
            start_x (int): 드래그 시작 X 좌표.
            start_y (int): 드래그 시작 Y 좌표.
            end_x (int): 드래그 종료 X 좌표.
            end_y (int): 드래그 종료 Y 좌표.
            duration (float): 드래그 시간 (초 단위).
        """
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, duration=duration)
        log_manager.logger.info(f"Dragged from ({start_x}, {start_y}) to ({end_x}, {end_y}) in {duration} seconds")

    def press_key(self, key):
        """
        지정된 키 또는 키 조합을 입력합니다.

        Args:
            key (str or tuple): 입력할 키(예: 'a') 또는 키 조합 튜플(예: ('alt', 'f4')).
        """
        try:
            import pyautogui
            if isinstance(key, tuple):
                pyautogui.hotkey(*key)
                log_manager.logger.info(f"Hotkey pressed: {' + '.join(key)}")
            else:
                pyautogui.press(key)
                log_manager.logger.info(f"Key pressed: {key}")
        except Exception as e:
            log_manager.logger.error(f"키 입력 중 오류 발생: {e}")

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
        action_handler.drag(x=location[0] + 200, y=location[1] + 200)

        # 키 입력 예시 (단일 키)
        action_handler.press_key('enter')

        # 키 입력 예시 (조합 키)
        action_handler.press_key(('alt', 'f4'))
    else:
        log_manager.logger.info("Template did not match.")

