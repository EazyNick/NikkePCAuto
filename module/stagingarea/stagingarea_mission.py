import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_stagingarea"))
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
    전초기지 파견
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_stagingarea")
    process_step = ProcessStep(base_path=assets_login_path)

    process_step.execute_click("1단계: 전초기지", "a_stagingarea.png", wait_time=3)
    process_step.execute_click("2단계: 파견 게시판", "b_mission.png", wait_time=3)
    process_step.execute_click("3단계: 전체 수령", "c_collectall.png", wait_time=3)
    process_step.execute_click("4단계: 터치하여 보상받기", "d_getreward", wait_time=3)
    process_step.execute_click("5단계: 일괄 파견", "e_batchall.png", wait_time=3)
    process_step.execute_click("6단계: 파견하기", "f_batch.png", wait_time=3)
    process_step.execute_click("6단계: 나가기", "g_exit.png", wait_time=3)
    process_step.execute_click("7단계: 홈", "h_home.png", wait_time=3)

if __name__ == "__main__":
    run()