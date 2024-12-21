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
    로그인 동작
    """
    assets_login_path = path_manager.get_path("assets_login")
    process_step = ProcessStep(base_path=assets_login_path)

    log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

    # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
    steps = [
        {"step": "1단계: 니케 아이콘 클릭", "image_name_or_coords": "a_icon.png", "double_click": True, "wait": 5},
        {"step": "2단계: 구글 로그인", "image_name_or_coords": "b_google.png", "window_name": "로그인 - Google 계정 - Chrome", "wait": 2},
        {"step": "3단계: 아이디 로그인", "image_name_or_coords": "c_google_login.png", "wait": 2},
        {"step": "4단계: 계속", "image_name_or_coords": "d_keep_going.png", "wait": 4},
        # {"step": "5단계: 페이지 닫기", "image_name_or_coords": "e_closepage.png", "wait": 3},
        {"step": "6단계: 웹페이지 종료", "window_name": "NIKKE", "image_name_or_coords": "f_exit.png", "wait": 1},
        {"step": "7단계: 게임 시작", "image_name_or_coords": "g_gamestart.png", "window_name": "NIKKE", "wait": 130},
        {"step": "8단계: 게임 접속", "image_name_or_coords": "h_ingame.png", "wait": 25},
        {"step": "9단계: 공지사항 닫기", "image_name_or_coords": "i_btn_X.png", "wait": 1},
        {"step": "9단계: 추가 공지사항 닫기", "image_name_or_coords": "i_btn_X.png", "retry": 3, "wait": 1},
    ]

    # 각 단계 실행
    for step in steps:
        if not process_step.execute(
            step["step"], 
            step["image_name_or_coords"], 
            step.get("double_click", False), 
            step.get("drag"),
            step.get("window_name"),
            step.get("retry", 10),
            step["wait"]
        ):
            log_manager.logger.error(f"{step.get('step', '단계 이름 없음')} 실패로 자동화 종료")
            return  # 단계 실패 시 함수 종료

    # 추가 동작: 게임 창 포커스 및 크기 조정
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

if __name__ == "__main__":
    # 추가 동작: 게임 창 포커스 및 크기 조정
    # screenhandler.resize_game_window('NIKKE', 2200, 1300)
    # time.sleep(0.1)
    # screenhandler.focus_game_window('NIKKE')
    # time.sleep(1)
    run()