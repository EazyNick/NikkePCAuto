import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_ark"))
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
    방주 트라이브 타워
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_ark")
    process_step = ProcessStep(base_path=assets_login_path)

    process_step.execute_click("1단계: 방주 이동", "a_ark.png", wait_time=3)
    process_step.execute_click("2단계: 트라이브 타워", "b_trivetower.png", wait_time=3)
    process_step.execute_click("3단계: 열린 타워로 이동", "c_dailyclear.png", wait_time=3)
    process_step.execute_click("4단계: 시작", (1246, 620), wait_time=2)
    process_step.execute_click("5단계: 전투진입", "e_ingame.png", retry=60, wait_time=50)
    # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
    process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
    # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
    process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
    process_step.execute_click("7단계: 나가기1", "g_exit.png", retry=120, wait_time=8)
    process_step.execute_click("8단계: 뒤로가기", "h_back.png", wait_time=3)

    if process_step.execute_click("3단계: 열린 타워로 이동", "c_dailyclear.png", retry=6, wait_time=6):
        process_step.execute_click("4단계: 시작", (1246, 620), retry=1, wait_time=2)
        if process_step.execute_click("5단계: 일일 전투진입 끝", "e_outgame.png", retry=1, wait_time=3):
            pass
        else:
            process_step.execute_click("5단계: 전투진입", "e_ingame.png", retry=1, wait_time=50)
            # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
            process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
            # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
            process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
            process_step.execute_click("7단계: 나가기1", "g_exit.png", retry=60, wait_time=3)
            process_step.execute_click("8단계: 뒤로가기", "h_back.png", wait_time=3)

            if process_step.execute_click("3단계: 열린 타워로 이동", "c_dailyclear.png", retry=6, wait_time=6):
                process_step.execute_click("4단계: 시작", (1246, 620), retry=1, wait_time=2)
            if process_step.execute_click("5단계: 일일 전투진입 끝", "e_outgame.png", retry=1, wait_time=3):
                pass
            else:
                process_step.execute_click("5단계: 전투진입", "e_ingame.png", retry=1, wait_time=3)
                # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
                process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
                # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
                process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
                process_step.execute_click("7단계: 나가기1", "g_exit.png", retry=60, wait_time=3)
                process_step.execute_click("8단계: 뒤로가기", "h_back.png", wait_time=3)
            
                if process_step.execute_click("3단계: 열린 타워로 이동", "c_dailyclear.png", retry=6, wait_time=6):
                    process_step.execute_click("4단계: 시작", (1246, 620), retry=1, wait_time=2)
                if process_step.execute_click("5단계: 일일 전투진입 끝", "e_outgame.png", retry=1, wait_time=3):
                    pass
                else:
                    process_step.execute_click("5단계: 전투진입", "e_ingame.png", retry=1, wait_time=50)
                    # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
                    process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
                    # process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=3, wait_time=3)
                    process_step.execute_click("6단계: 다음 스테이지", "f_nextstage.png", retry=60, wait_time=50)
                    process_step.execute_click("7단계: 나가기1", "g_exit.png", retry=60, wait_time=3)
                    process_step.execute_click("8단계: 뒤로가기", "h_back.png", wait_time=3)
                    process_step.execute_click("8단계: 뒤로가기", "h_back", wait_time=3)
    process_step.execute_click("8단계: 홈", "i_home.png", wait_time=3)

if __name__ == "__main__":
    run()