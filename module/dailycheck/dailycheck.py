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
    일일 출석체크
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_dailycheck")
    process_step = ProcessStep(base_path=assets_login_path)

    # 단계별 실행
    process_step.execute_click("1단계: 알람 아이콘 클릭", "a_alert.png", wait_time=1)
    process_step.execute_drag("2단계: 이벤트 드래그", drag={"start": (1250, 910), "end": (1250, 400), "duration": 0.5}, wait_time=3)

    if process_step.execute_click("2단계: 이벤트 이동", "b_move.png",retry = 3, wait_time=1):
        process_step.execute_click("3단계: 이벤트 이동2", "c_move2.png", wait_time=1)
        process_step.execute_click("4단계: 확인", "d_ok.png", wait_time=1)
        process_step.execute_click("5단계: 출석체크", "e_dailycheckgo.png", wait_time=1)
        process_step.execute_click("6단계: 확인", "f_ok.png", wait_time=1)
        process_step.execute_press_key("8단계: 나가기1", ("alt", "f4"), wait_time=3)
        process_step.execute_click("9단계: 나가기2", (500, 300), wait_time=2)
        process_step.execute_click("10단계: 나가기3", "i_exit.png", wait_time=2)
    else:
        process_step.execute_drag("2단계: 이벤트 드래그", drag={"start": (1250, 910), "end": (1250, 420), "duration": 0.5}, wait_time=3)
        process_step.execute_click("2단계: 이벤트 이동", "b_move.png",retry = 3, wait_time=1)
        process_step.execute_click("3단계: 이벤트 이동2", "c_move2.png", wait_time=1)
        process_step.execute_click("4단계: 확인", "d_ok.png", wait_time=1)
        process_step.execute_click("5단계: 출석체크", "e_dailycheckgo.png", wait_time=1)
        process_step.execute_click("6단계: 확인", "f_ok.png", wait_time=1)
        process_step.execute_press_key("8단계: 나가기1", ("alt", "f4"), wait_time=3)
        process_step.execute_click("9단계: 나가기2", (500, 300), wait_time=2)
        process_step.execute_click("10단계: 나가기3", "i_exit.png", wait_time=2)

if __name__ == "__main__":
    run()