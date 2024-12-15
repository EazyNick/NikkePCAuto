import win32gui
import win32con
import os
import sys

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))

try:
    from logs import log_manager
except Exception as e:
    log_manager.logger.info(f"임포트 실패: {e}")

def resize_game_window(window_title, width, height, x=150, y=50):
    """
    지정된 제목의 창을 찾아 크기와 위치를 설정합니다.
    
    :param window_title: 게임 창의 제목
    :param width: 창의 너비
    :param height: 창의 높이
    :param x: 창의 X 위치 (기본값 0)
    :param y: 창의 Y 위치 (기본값 0)
    """
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        # 창의 위치와 크기 설정
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, win32con.SWP_SHOWWINDOW)
        log_manager.logger.info(f"'{window_title}' 창의 크기를 {width}x{height}, 위치를 ({x}, {y})로 설정했습니다.")
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
    # list_windows()
    game_title = "NIKKE"  # 게임 창의 제목을 정확히 입력
    resize_game_window(game_title, 2200, 1300)  # 원하는 크기와 위치 설정
