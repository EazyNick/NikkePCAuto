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
    방주 시뮬레이션 룸
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_ark")
    process_step = ProcessStep(base_path=assets_login_path)

    process_step.execute_click("1단계: 방주 이동", "a_ark.png", wait_time=3)
    process_step.execute_click("2단계: 시뮬레이션 룸", "b_simulationroom.png", wait_time=3)
    process_step.execute_click("3단계: 시뮬레이션 시작", "c_simulationstart.png", wait_time=3)
    process_step.execute_click("4단계: 5단계", 'd_5th', wait_time=2)
    process_step.execute_click("5단계: 난이도 c", "e_C.png", retry=3, wait_time=3)
    process_step.execute_click("6단계: 시뮬레이션 시작", "f_startsimulation.png", wait_time=5)
    process_step.execute_click("7단계: 하드 단계", "g_hard.png", wait_time=5)
    process_step.execute_click("8단계: 전투진입", "h_enter_combat.png", wait_time=50)
    process_step.execute_click("9단계: 뒤로가기", "i_next.png", retry=60, wait_time=8)
    process_step.execute_click("10단계: 업그레이드 선택", "j_sword", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    
    process_step.execute_click("11단계: 확인", "k_ok", retry=3, wait_time=3)
    process_step.execute_click("12단계: 취소", "l_cancle", retry=3, wait_time=3)
    process_step.execute_click("13단계: 선택하지 않음", "m_nochoice", retry=3, wait_time=3)
    process_step.execute_click("10단계: 확인", "n_ok", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)

    process_step.execute_click("7단계: 하드 단계", "g_hard.png", wait_time=5)
    process_step.execute_click("8단계: 전투진입", "h_enter_combat.png", wait_time=50)
    process_step.execute_click("9단계: 뒤로가기", "i_next.png", retry=60, wait_time=8)
    process_step.execute_click("10단계: 업그레이드 선택", "j_sword", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    
    process_step.execute_click("11단계: 확인", "k_ok", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)

    process_step.execute_click("7단계: 하드 단계", "g_hard.png", wait_time=5)
    process_step.execute_click("8단계: 전투진입", "h_enter_combat.png", wait_time=50)
    process_step.execute_click("9단계: 뒤로가기", "i_next.png", retry=60, wait_time=8)
    process_step.execute_click("10단계: 업그레이드 선택", "j_sword", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    
    process_step.execute_click("11단계: 확인", "k_ok", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)
    process_step.execute_click("10단계: 업그레이드 선택", "j_criticalpersentage", retry=3, wait_time=3)

if __name__ == "__main__":
    run()