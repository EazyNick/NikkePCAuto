import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_ark"))
sys.path.append(path_manager.get_path("module"))
sys.path.append(path_manager.get_path("display"))
sys.path.append(path_manager.get_path("common"))

try:
    from logs import log_manager
    from module import templateprocessor
    from common import ActionHandler
    from display import screenhandler
except Exception as e:
    print(f"임포트 실패: {e}")

class ProcessStep:
    """
    각 단계를 수행하는 클래스
    """
    def __init__(self, base_path):
        """
        Args:
            base_path (str): 템플릿 이미지의 기본 경로
        """
        self.base_path = base_path
        self.except_path = path_manager.get_path("assets_ark")
        self.action_handler = ActionHandler()

    def execute(self, step_name, image_name_or_coords, double_click=False, drag=None, window_name=None,retry=10, wait_time=3):
        """
        단계를 수행하는 메서드

        Args:
            step_name (str): 단계 이름 (로그 출력용)
            image_name_or_coords (str | tuple): 템플릿 이미지 파일명 또는 클릭할 좌표 (x, y)
            double_click (bool): 더블 클릭 여부 (기본값: False)
            drag (dict): 드래그 동작 설정 {"start": (x1, y1), "end": (x2, y2), "duration": float}
            window_name (str): 포커스할 창 이름 (기본값: None)
            retry (int): 이미지 매칭 실패 시 재시도 횟수 (기본값: 10)
            wait_time (int): 다음 단계로 넘어가기 전 대기 시간 (초, 기본값: 3)

        Returns:
            bool: 단계 수행 성공 여부
        """
        log_manager.logger.info(f"{step_name} 시작")

        # ALT+F4 동작 처리
        if image_name_or_coords == "ALT+F4":
            log_manager.logger.info(f"{step_name}: ALT+F4 키 입력 실행")
            self.action_handler.press_alt_f4()
            return True

        # 예외 현질 알림
        try:
            temp_path = os.path.join(self.except_path, "zz_event_exit.png")
            if templateprocessor.process(temp_path, double_click):
                log_manager.logger.info("zz_event_exit 템플릿 발견, 예외 처리 로직 실행")
                self.run_exception_scenario()
                log_manager.logger.info(f"{step_name} 완료: '{temp_path}' 아이콘 클릭 성공")
        except Exception as e:
            log_manager.logger.error(f"예외 처리 중 오류 발생: {e}")

        # 드래그 동작 수행
        if isinstance(drag, dict):  # drag가 dict인지 확인
            start = drag.get("start")
            end = drag.get("end")
            duration = drag.get("duration", 0.5)
            if start and end:
                log_manager.logger.info(f"{step_name}: 드래그 수행 {start} -> {end} (duration: {duration}s)")
                self.action_handler.drag(start[0], start[1], end[0], end[1], duration)
                time.sleep(2)
        elif drag is not None:  # drag가 dict가 아닌 다른 값일 경우 경고
            log_manager.logger.warning(f"{step_name}: 잘못된 drag 설정으로, 무시됨: {drag}")

        for attempt in range(retry):
            if isinstance(image_name_or_coords, tuple):
                # 좌표를 클릭하는 경우
                x, y = image_name_or_coords
                if double_click:
                    self.action_handler.double_click(x, y)
                    log_manager.logger.info(f"{step_name}: 좌표 ({x}, {y}) 더블 클릭 완료")
                else:
                    self.action_handler.click(x, y)
                    log_manager.logger.info(f"{step_name}: 좌표 ({x}, {y}) 클릭 완료")
                break  # 좌표 클릭은 반복하지 않음
            else:
                # 템플릿 매칭을 사용하는 경우
                template_path = os.path.join(self.base_path, image_name_or_coords)
                if templateprocessor.process(template_path, double_click):
                    log_manager.logger.info(f"{step_name} 완료: '{image_name_or_coords}' 아이콘 클릭 성공")
                    break
                else:
                    log_manager.logger.warning(f"{step_name}: '{image_name_or_coords}' 아이콘을 찾을 수 없습니다. 재시도 중... ({attempt + 1}/{retry})")
                    time.sleep(1)
        else:
            log_manager.logger.error(f"{step_name} 실패: '{image_name_or_coords}' 아이콘을 찾지 못했습니다.")
            return False
        
        # 창 포커스
        if window_name:
            time.sleep(5)
            screenhandler.focus_game_window(window_name)
            log_manager.logger.info(f"창 포커스: {window_name}")

        time.sleep(wait_time)
        return True
    
    def run_exception_scenario(self):
        """
        캐시 구매 팝업 발견 시 실행할 예외 처리 로직
        """
        log_manager.logger.info("run_exception_scenario 실행")
        # 여기에서 원하는 동작 수행
        # 예: 특정 좌표 클릭, 다른 템플릿 탐색, 대기 등
        _template_path = os.path.join(self.except_path, "zz_event_exit.png")
        templateprocessor.process(_template_path)
        time.sleep(2)
        _template_path = os.path.join(self.except_path, "zz_event_exit2.png")
        templateprocessor.process(_template_path)
        log_manager.logger.info("예외 처리 로직 완료")

if __name__ == "__main__":

    sys.path.append(path_manager.get_path("assets_login"))

    def run():
        """
        로그인 동작
        """
        log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

        # 단계별 설정 (단계 이름, 이미지 파일명 또는 좌표, 더블클릭 여부, 대기 시간, 드래그 설정)
        steps = [
            # {"step": "1단계: 로그인 아이콘 클릭", "image": "a_icon.png", "double_click": True, "wait": 8},
            # {"step": "2단계: 구글 로그인", "image": "b_google.png", "wait": 3},
            {"step": "3단계: 아이디 클릭", "image_name_or_coords": (500, 300), "wait": 3},
            # {"step": "4단계: 계속", "image": "d_keep_going.png", "wait": 5},
            # {"step": "5단계: 페이지 닫기", "image": "e_closepage.png", "wait": 3},
            # {"step": "6단계: 웹페이지 종료", "image": "f_exit.png", "wait": 10},
            # {"step": "7단계: 게임 시작", "image": "g_gamestart.png", "wait": 3}
        ]

        process_step = ProcessStep(base_path=path_manager.get_path("assets_login"))

        # 각 단계 실행
        for step in steps:
            if not process_step.execute(
                step["step"], 
                step["image_name_or_coords"], 
                step.get("double_click", False), 
                step.get("drag"),
                step.get("window_name"),
                step.get("wait", 3)
            ):
                return  # 단계 실패 시 종료

        # # 추가 동작: 게임 창 포커스 및 크기 조정
        # screenhandler.focus_game_window('NIKKE')
        # time.sleep(1)
        # screenhandler.resize_game_window('NIKKE', 2200, 1300)
        # time.sleep(0.1)
        # screenhandler.focus_game_window('NIKKE')
        # time.sleep(1)

    run()