import win32gui
import win32con
import win32api
import os
import sys


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))

try:
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")

class ScreenHandler:
    """
    화면 조작과 관련된 동작을 관리하는 클래스
    """
    def resize_game_window(self, window_title, width, height, x=150, y=50):
        """
        지정된 제목의 창을 찾아 크기와 위치를 설정합니다.
        
        Args:
            window_title (str): 창의 제목
            width (int): 창의 너비
            height (int): 창의 높이
            x (int): 창의 X 위치
            y (int): 창의 Y 위치
        """
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, win32con.SWP_SHOWWINDOW)
            log_manager.logger.info(f"'{window_title}' 창의 크기를 {width}x{height}, 위치를 ({x}, {y})로 설정했습니다.")
        else:
            log_manager.logger.info(f"'{window_title}' 창을 찾을 수 없습니다.")

    def focus_game_window(self, window_title):
        """
        지정된 제목의 창에 포커스를 맞춥니다.
        
        Args:
            window_title (str): 창의 제목
        """
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
            log_manager.logger.info(f"'{window_title}' 창에 포커스를 맞췄습니다.")
        else:
            log_manager.logger.info(f"'{window_title}' 창을 찾을 수 없습니다.")

def list_windows():
    def callback(hwnd, extra):
        title = win32gui.GetWindowText(hwnd)
        if title:
            log_manager.logger.info(f"HWND: {hwnd}, Title: {title}")
    win32gui.EnumWindows(callback, None)


# 예제 실행
if __name__ == "__main__":
    list_windows()
    screenhandler = ScreenHandler
    game_title = "NIKKE"  # 게임 창의 제목을 정확히 입력
    screenhandler.resize_game_window(game_title, 2200, 1300)  # 원하는 크기와 위치 설정
    # test_title = '로그인 - Google 계정 - Chrome'
    # screenhandler.focus_game_window(test_title)  # 원하는 크기와 위치 설정
