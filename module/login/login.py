import os
import sys
import time

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
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
    from display import resize_game_window, focus_game_window
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
        {"step": "1단계: 로그인 아이콘 클릭", "image": "a_icon.png", "double_click": True, "wait": 8},
        {"step": "2단계: 구글 로그인", "image": "b_google.png", "window_name": "로그인 - Google 계정 - Chrome", "wait": 3},
        {"step": "3단계: 아이디 로그인", "image": "c_google_login.png", "wait": 3},
        {"step": "4단계: 계속", "image": "d_keep_going.png", "wait": 5},
        # {"step": "5단계: 페이지 닫기", "image": "e_closepage.png", "wait": 3},
        {"step": "6단계: 웹페이지 종료", "window_name": "NIKKE", "image": "f_exit.png", "wait": 3},
        {"step": "7단계: 게임 시작", "image": "g_gamestart.png", "wait": 120},
        {"step": "8단계: 게임 접속", "image": "h_ingame.png", "wait": 20},
        {"step": "9단계: 공지사항 닫기", "image": "i_btn_X.png", "wait": 20},
    ]

    # 각 단계 실행
    for step in steps:
        if not process_step.execute(
            step["step"], 
            step["image"], 
            step.get("double_click", False), 
            step.get("drag"),
            step.get("window_name"),
            step["wait"]
        ):
            log_manager.logger.error(f"{step.get('step', '단계 이름 없음')} 실패로 자동화 종료")
            return  # 단계 실패 시 함수 종료

    # 추가 동작: 게임 창 포커스 및 크기 조정
    resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    focus_game_window('NIKKE')
    time.sleep(1)

if __name__ == "__main__":
    run()