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
    방주
    """
    screenhandler.resize_game_window('NIKKE', 2200, 1300)
    time.sleep(0.1)
    screenhandler.focus_game_window('NIKKE')
    time.sleep(1)

    assets_login_path = path_manager.get_path("assets_ark")
    process_step = ProcessStep(base_path=assets_login_path)
    log_manager.logger.info("방주 프로세스를 시작합니다.")

    # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
    steps = [
        {"step": "1단계: 방주 이동", "image_name_or_coords": "a_ark.png", "wait": 3},
        {"step": "2단계: 트라이브 타워", "image_name_or_coords": "b_trivetower.png", "wait": 3},
        {"step": "3단계: 열린 타워로 이동", "image_name_or_coords": "c_dailyclear.png", "wait": 6},
        {"step": "4단계: 시작", "image_name_or_coords": (1246, 620), "wait": 2},
        {"step": "5단계: 전투진입", "image_name_or_coords": "e_ingame.png","retry": 60, "wait": 50},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 60, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 60, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 60, "wait": 60},
        {"step": "7단계: 나가기1", "image_name_or_coords": "g_exit.png", "wait": 3},
        {"step": "3단계: 열린 타워로 이동", "image_name_or_coords": "c_dailyclear.png","retry": 0, "wait": 6},
        {"step": "4단계: 시작", "image_name_or_coords": (1246, 620),"retry": 1, "wait": 2},
        {"step": "5단계: 전투진입", "image_name_or_coords": "e_ingame.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "7단계: 나가기1", "image_name_or_coords": "g_exit.png","retry": 1, "wait": 3},
        {"step": "3단계: 열린 타워로 이동", "image_name_or_coords": "c_dailyclear.png","retry": 0, "wait": 6},
        {"step": "4단계: 시작", "image_name_or_coords": (1246, 620),"retry": 1, "wait": 2},
        {"step": "5단계: 전투진입", "image_name_or_coords": "e_ingame.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "7단계: 나가기1", "image_name_or_coords": "g_exit.png","retry": 1, "wait": 3},
        {"step": "3단계: 열린 타워로 이동", "image_name_or_coords": "c_dailyclear.png","retry": 0, "wait": 6},
        {"step": "4단계: 시작", "image_name_or_coords": (1246, 620),"retry": 1, "wait": 2},
        {"step": "5단계: 전투진입", "image_name_or_coords": "e_ingame.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "6단계: 다음 스테이지", "image_name_or_coords": "f_nextstage.png","retry": 1, "wait": 60},
        {"step": "7단계: 나가기1", "image_name_or_coords": "g_exit.png", "wait": 3},
        {"step": "8단계: 나가기2", "image_name_or_coords": "h_back", "wait": 3},
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

if __name__ == "__main__":
    run()