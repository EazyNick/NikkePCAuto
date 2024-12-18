import os
import sys
import time

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_login"))
sys.path.append(path_manager.get_path("module"))
sys.path.append(path_manager.get_path("display"))

try:
    from logs import log_manager
    from module import screenhandler
    from display import resize_game_window, focus_game_window
except Exception as e:
    print(f"임포트 실패: {e}")

def process_step(step_name, image_name, double_click=False, wait_time=3, window_name=None):
    """
    각 단계를 수행하는 공통 함수

    Args:
        step_name (str): 단계 이름 (로그 출력용)
        image_name (str): 템플릿 이미지 파일명
        double_click (bool): 더블 클릭 여부
        wait_time (int): 다음 단계로 넘어가기 전 대기 시간 (초)
        window_name (str): 포커스할 창 이름 (기본값: None)
    """
    login_template_path = os.path.join(path_manager.get_path("assets_login"), image_name)
    log_manager.logger.info(f"{step_name} 시작")

    if not screenhandler.process(login_template_path, double_click):
        log_manager.logger.error(f"{step_name} 실패: '{image_name}' 아이콘을 찾을 수 없습니다.")
        return False

    log_manager.logger.info(f"{step_name} 완료: '{image_name}' 아이콘 클릭 성공")
    
    # 창 포커스
    if window_name:
        focus_game_window(window_name)
        log_manager.logger.info(f"창 포커스: {window_name}")
        time.sleep(1)
    time.sleep(wait_time)
    
    return True

if __name__ == "__main__":

    def run():
        """
        로그인 동작
        """
        log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

        # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
        steps = [
            {"step": "1단계: 로그인 아이콘 클릭", "image": "a_icon.png", "double_click": True, "wait": 8},
            {"step": "2단계: 구글 로그인", "image": "b_google.png", "wait": 3},
            {"step": "3단계: 아이디 로그인", "image": "c_google_login.png", "wait": 3},
            {"step": "4단계: 계속", "image": "d_keep_going.png", "wait": 5},
            {"step": "5단계: 페이지 닫기", "image": "e_closepage.png", "wait": 3},
            {"step": "6단계: 웹페이지 종료", "image": "f_exit.png", "wait": 10},
            {"step": "7단계: 게임 시작", "image": "g_gamestart.png", "wait": 3}
        ]

        # 각 단계 실행
        for step in steps:
            if not process_step(step["step"], step["image"], step.get("double_click", False), step["wait"]):
                return  # 단계 실패 시 종료

        # 추가 동작: 게임 창 포커스 및 크기 조정
        focus_game_window('NIKKE')
        time.sleep(1)
        resize_game_window('NIKKE', 2200, 1300)
        time.sleep(0.1)
        focus_game_window('NIKKE')
        time.sleep(1)

    run()
