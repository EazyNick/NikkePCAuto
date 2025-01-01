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
    로그인 동작을 단계별로 실행
    """
    assets_login_path = path_manager.get_path("assets_login")
    process_step = ProcessStep(base_path=assets_login_path)

    # 단계별 실행
    process_step.execute_click("1단계: 니케 아이콘 클릭", "a_icon.png", double_click=True, wait_time=1)
    process_step.execute_click("2단계: 구글 로그인", "b_google.png", window_name="로그인 - Google 계정 - Chrome", wait_time=1)
    process_step.execute_click("3단계: 아이디 로그인", "c_google_login.png", wait_time=2)
    process_step.execute_click("4단계: 계속", "d_keep_going.png", wait_time=2)
    process_step.execute_click("6단계: 웹페이지 종료", "f_exit.png", window_name="NIKKE", wait_time=1)
    process_step.execute_click("7단계: 게임 시작", "g_gamestart.png", window_name="NIKKE", wait_time=10)
    # 추가 동작: 게임 창 포커스 및 크기 조정
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)
    process_step.execute_click("7.1단계: 페이지 닫기", "h_btn_X.png", retry=50, wait_time=40)
    process_step.execute_click("8단계: 게임 접속", "h_ingame.png", retry=100, wait_time=15)
    process_step.execute_click("9단계: 공지사항 닫기", "i_btn_X.png", wait_time=1)

    process_step.execute_click("10단계: 이벤트 모두 받기", "i_event_getall.png", retry=3, wait_time=1)
    process_step.execute_click("10단계: 이벤트 모두 받기", "j_event_exit.png", retry=3, wait_time=1)
    process_step.execute_click("10단계: 이벤트 모두 받기", "k_event_back.png", retry=3, wait_time=1)

    for i in range(3):
        process_step.execute_click("11단계: 이벤트 뽑기", "l_event.png", wait_time=5)
        process_step.execute_click("11단계: 리워드 흭득", "m_event.png", wait_time=2)
    process_step.execute_click("11단계: 터치하여 닫기", "n_event_exit.png", retry=3, wait_time=1)

    process_step.execute_click("12단계: 추가 공지사항 닫기", "i_btn_X.png", retry=3, wait_time=1)

    # 추가 동작: 게임 창 포커스 및 크기 조정
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

if __name__ == "__main__":
    run()
