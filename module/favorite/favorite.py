import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_favorite"))
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
    호감도
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_favorite")
    process_step = ProcessStep(base_path=assets_login_path)

    # 단계별 실행
    process_step.execute_click("1단계: 니케 목록으로 이동", "a_nikkecharactor.png", wait_time=3)
    process_step.execute_click("2단계: 상담", "b_dialogue.png", wait_time=3)
    process_step.execute_click("3단계: 시작", "c_picknikke.png", retry=3, wait_time=2)
    for i in range(10):
        if process_step.execute_click(f"4단계: 간편상담 ({i+1})", "d_simpledialogue.png", retry=3, wait_time=3):
            process_step.execute_click(f"5단계: 확인 ({i+1})", "e_ok.png", retry=3, wait_time=2)
            process_step.execute_click(f"6단계: 터치하여 나가기 ({i+1})", "f_next.png", retry=1, wait_time=2)
            process_step.execute_click(f"6단계: 터치하여 나가기 ({i+1})", "f_next.png", retry=3, wait_time=2)
            process_step.execute_click(f"7단계: 다음 니케 ({i+1})", "g_next.png", retry=3, wait_time=2)
        else:
            process_step.execute_click(f"4단계: 상담하기 ({i+1})", "d_dialogue.png", retry=3, wait_time=3)
            process_step.execute_click(f"5단계: 확인 ({i+1})", "e_ok.png", retry=3, wait_time=2)
            process_step.execute_click(f"6단계: 자동 대화 ({i+1})", "f_auto.png", wait_time=2)
            while process_step.execute_click(f"6단계: 1번 선택지", "g_1st.png", retry=1, wait_time=20) or process_step.execute_click(f"6단계: 2번 선택지", "g_2st.png", retry=1, wait_time=20):
                time.sleep(1)
    process_step.execute_click("8단계: 뒤로가기", "h_back.png", retry=3, wait_time=2)
    process_step.execute_click("9단계: 홈", "i_home.png", retry=3, wait_time=2)

if __name__ == "__main__":
    run()
