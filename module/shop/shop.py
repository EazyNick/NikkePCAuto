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
    캐시 상점
    """

    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_shop")
    process_step = ProcessStep(base_path=assets_login_path)

    # 단계별 실행
    process_step.execute_click("1단계: 캐시 상점", "a_cashshop.png", wait_time=3)
    process_step.execute_click("2단계: 선물", "b_present.png", wait_time=2)
    process_step.execute_click("3단계: 일일", "c_daily.png", wait_time=2)
    process_step.execute_click("4단계: 무료", "d_dailyfree.png", wait_time=2)
    process_step.execute_click("5단계: 터치하여 보상 수령", "e_exit.png", wait_time=2)
    process_step.execute_click("6단계: 주간", "f_weekly.png", retry=1, wait_time=2)
    process_step.execute_click("7단계: 무료", "g_weeklyfree.png", retry=1, wait_time=2)
    process_step.execute_click("8단계: 터치하여 보상 수령", "h_exit.png", retry=1, wait_time=2)
    process_step.execute_click("9단계: 나가기", "i_back.png", wait_time=3)

if __name__ == "__main__":
    run()
