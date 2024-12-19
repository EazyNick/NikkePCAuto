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
    일일 전투 보상
    """

    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_outpost")
    process_step = ProcessStep(base_path=assets_login_path)
    log_manager.logger.info("일일 전투 보상 프로세스를 시작합니다.")

    # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
    steps = [
        {"step": "1단계: 일일 보상 클릭", "image_name_or_coords": "a_outpostdefense_reward.png", "wait": 3},
        {"step": "2단계: 보상 받기", "image_name_or_coords": "b_getreward.png", "wait": 5},
        {"step": "3단계: 확인", "image_name_or_coords": "c_exit.png", "wait": 3},
        {"step": "4단계: 나가기", "image_name_or_coords": "d_exit.png", "wait": 3},
        {"step": "5단계: 일일 보상 클릭", "image_name_or_coords": "e_outpostdefense_reward.png", "wait": 3},
        {"step": "6단계: 단기 섬멸", "image_name_or_coords": "f_Instantclear.png", "wait": 3},
        {"step": "7단계: 섬멸 진행", "image_name_or_coords": "g_progressclear.png", "wait": 3},
        {"step": "8단계: 나가기", "image_name_or_coords": "h_exit.png", "wait": 2},
        {"step": "9단계: 나가기", "image_name_or_coords": "i_exit.png", "wait": 2},
        {"step": "10단계: 나가기", "image_name_or_coords": "j_exit.png", "wait": 2},
    ]

    # 각 단계 실행
    for step in steps:
        if not process_step.execute(
            step["step"], 
            step["image_name_or_coords"], 
            step.get("double_click", False), 
            step.get("drag"),
            step.get("window_name"),
            step["wait"]
        ):
            log_manager.logger.error(f"{step.get('step', '단계 이름 없음')} 실패로 자동화 종료")
            return  # 단계 실패 시 함수 종료

if __name__ == "__main__":
    run()