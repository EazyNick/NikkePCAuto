import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_login"))
sys.path.append(path_manager.get_path("module"))
sys.path.append(path_manager.get_path("display"))

try:
    from logs import log_manager
    from module import ProcessStep
    from display import screenhandler
except Exception as e:
    print(f"임포트 실패: {e}")

def run():
    """
    우편 받기
    """

    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_mail")
    process_step = ProcessStep(base_path=assets_login_path)

    # 단계별 실행
    process_step.execute_click("1단계: 우편", "a_mail.png", wait_time=3)
    process_step.execute_click("2단계: 모두 받기", "b_getall.png", wait_time=3)
    process_step.execute_click("3단계: 보상 받기", "c_getreward.png", wait_time=3)
    process_step.execute_click("4단계: 나가기", "d_exit.png", wait_time=2)

if __name__ == "__main__":
    run()
