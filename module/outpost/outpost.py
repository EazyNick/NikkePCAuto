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
except Exception as e:
    print(f"임포트 실패: {e}")

def run():
    """
    친구 하트 주고받기
    """

    assets_login_path = path_manager.get_path("assets_outpost")
    process_step = ProcessStep(base_path=assets_login_path)
    log_manager.logger.info("친구 자동화 프로세스를 시작합니다.")

    # 단계별 설정 (단계 이름, 이미지 파일명, 더블클릭 여부, 대기 시간)
    steps = [
        {"step": "1단계: 일일 보상 클릭", "image": "a_outpostdefense_reward.png", "wait": 3},
        {"step": "2단계: 보상 받기", "image": "b_getreward.png", "wait": 5},
        {"step": "3단계: 확인", "image": "c_exit.png", "wait": 3},
        {"step": "4단계: 나가기", "image": "d_exit.png", "wait": 3},
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

if __name__ == "__main__":
    run()