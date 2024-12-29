import os
import sys
import time


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("assets_ark"))
sys.path.append(path_manager.get_path("module"))
sys.path.append(path_manager.get_path("display"))
sys.path.append(path_manager.get_path("common"))

try:
    from logs import log_manager
    from module import templateprocessor
    from common import ActionHandler
    from display import screenhandler
    from utils import capture_screen, click_and_save_with_highlight
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

    def execute_click(self, step_name, image_name_or_coords, double_click=False, retry=10, window_name=None, wait_time=3):
        """
        클릭 동작을 수행하는 메서드

        Args:
            step_name (str): 단계 이름 (로그 출력용)
            image_name_or_coords (str or tuple): 템플릿 이미지 파일명 또는 클릭 좌표 (예: (x, y))
            double_click (bool): 더블 클릭 여부 (기본값: False)
            retry (int): 이미지 매칭 실패 시 재시도 횟수 (기본값: 10)
            window_name (str): 포커스할 창 이름 (기본값: None)
            wait_time (int): 다음 단계로 넘어가기 전 대기 시간 (초, 기본값: 3)

        Returns:
            bool: 단계 수행 성공 여부
        """
        log_manager.logger.info(f"{step_name} 시작")
        if self.run_exception_scenario():
            time.sleep(0.1)
        try:
            if isinstance(image_name_or_coords, tuple):
                # 좌표 클릭 처리
                x, y = image_name_or_coords
                if double_click:
                    self.action_handler.double_click(x, y)
                else:
                    self.action_handler.click(x, y)
            else:
                # 이미지 기반 클릭 처리
                for attempt in range(retry):
                    template_paths = [
                        os.path.join(self.base_path, image_name_or_coords)
                    ]
                    for i in range(1, 4):
                        template_paths.append(
                            os.path.join(
                                self.base_path, f"{os.path.splitext(image_name_or_coords)[0]}{i}.png"
                            )
                        )
                    base_name, ext = os.path.splitext(image_name_or_coords)
                    for i, template_path in enumerate(template_paths):
                        if os.path.exists(template_path):
                            if double_click:
                                if templateprocessor.process_double_click(template_path):
                                    if window_name:
                                        time.sleep(5)
                                        screenhandler.focus_game_window(window_name)
                                    time.sleep(wait_time)
                                    return True
                            else:
                                if templateprocessor.process_click(template_path):
                                    if window_name:
                                        time.sleep(5)
                                        screenhandler.focus_game_window(window_name)
                                    time.sleep(wait_time)
                                    return True
                            log_manager.logger.warning(
                            f"{step_name}: '{base_name}{'' if i == 0 else str(i)}{ext}' 아이콘을 찾을 수 없습니다. 재시도 중... ({attempt + 1}/{retry})"
                        )
                        else:
                            pass
                    log_manager.logger.error(
                        f"{step_name} 실패: '{base_name}{'' if i == 0 else str(i)}{ext}' 아이콘을 찾지 못했습니다."
                    )
                    time.sleep(1)
                return False
            time.sleep(wait_time)
        except Exception as e:
            log_manager.logger.warn(f"{step_name} 실패: {e}")
            return False
        return True

    def execute_drag(self, step_name, drag, repeat=1, window_name=None, wait_time=3):
        """
        드래그 동작을 수행하는 메서드

        Args:
            step_name (str): 단계 이름 (로그 출력용)
            drag (dict): 드래그 동작 설정 {"start": (x1, y1), "end": (x2, y2), "duration": float}
            repeat (int): 드래그 반복 횟수 (기본값: 1)
            window_name (str): 포커스할 창 이름 (기본값: None)
            wait_time (int): 다음 단계로 넘어가기 전 대기 시간 (초, 기본값: 3)

        Returns:
            bool: 단계 수행 성공 여부
        """
        log_manager.logger.info(f"{step_name} 시작")

        capture_screen()

        if isinstance(drag, dict):
            start = drag.get("start")
            end = drag.get("end")
            duration = drag.get("duration", 0.5)
            if start and end:
                for attempt in range(repeat):
                    try:
                        self.action_handler.drag(start[0], start[1], end[0], end[1], duration)
                        time.sleep(2)
                    except Exception as e:
                        log_manager.logger.error(f"{step_name} 실패: 드래그 동작 중 오류 발생 - {e}")
                        return False
            else:
                log_manager.logger.warning(f"{step_name}: 잘못된 drag 설정으로 무시됨: {drag}")
                return False

        if window_name:
            time.sleep(5)
            screenhandler.focus_game_window(window_name)

        time.sleep(wait_time)
        capture_screen()
        return True

    def execute_press_key(self, step_name, key, wait_time=1):
        """
        키 입력 동작을 수행하는 메서드

        Args:
            step_name (str): 단계 이름 (로그 출력용)
            key (str or tuple): 입력할 키(예: 'a') 또는 키 조합 튜플(예: ('alt', 'f4')).
            wait_time (int): 다음 단계로 넘어가기 전 대기 시간 (초, 기본값: 1)

        Returns:
            bool: 단계 수행 성공 여부
        """
        log_manager.logger.info(f"{step_name} 시작")
        
        capture_screen()

        try:
            self.action_handler.press_key(key)
        except Exception as e:
            log_manager.logger.error(f"{step_name} 실패: 키 입력 중 오류 발생: {e}")
            return False

        time.sleep(wait_time)
        capture_screen()
        return True

    def run_exception_scenario(self):
        """
        캐시 구매 팝업 발견 시 실행할 예외 처리 로직
        """
        log_manager.logger.info("run_exception_scenario 실행")
        # 여기에서 원하는 동작 수행
        # 예: 특정 좌표 클릭, 다른 템플릿 탐색, 대기 등
        _template_path = os.path.join(self.except_path, "zz_event_exit.png")
        templateprocessor.process_click(_template_path)
        time.sleep(2)
        _template_path = os.path.join(self.except_path, "zz_event_exit2.png")
        templateprocessor.process_click(_template_path)
        log_manager.logger.info("예외 처리 로직 완료")

if __name__ == "__main__":

    sys.path.append(path_manager.get_path("assets_login"))

    def run():
        """
        로그인 동작
        """
        log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

        assets_login_path = path_manager.get_path("assets_login")
        process_step = ProcessStep(base_path=assets_login_path)

        # 단계별 실행
        process_step.execute_drag("0단계: 드래그 테스트", drag={"start": (1250, 910), "end": (1250, 465), "duration": 1.5}, wait_time=1)
        process_step.execute_click("1단계: 니케 아이콘 클릭", "a_icon.png", double_click=True, wait_time=1)
        process_step.execute_click("2단계: 구글 로그인", "b_google.png", window_name="로그인 - Google 계정 - Chrome", wait_time=1)
        process_step.execute_click("3단계: 아이디 로그인", "c_google_login.png", wait_time=2)
        process_step.execute_click("4단계: 계속", "d_keep_going.png", wait_time=2)
        process_step.execute_click("6단계: 웹페이지 종료", "f_exit.png", window_name="NIKKE", wait_time=1)
        process_step.execute_click("7단계: 게임 시작", "g_gamestart.png", retry=100, window_name="NIKKE", wait_time=100)
        process_step.execute_click("7.1단계: 페이지 닫기", "h_btn_X.png", wait_time=3)
        process_step.execute_click("8단계: 게임 접속", "h_ingame.png", retry=100, wait_time=20)
        process_step.execute_click("9단계: 공지사항 닫기", "i_btn_X.png", wait_time=1)
        process_step.execute_click("10단계: 추가 공지사항 닫기", "i_btn_X.png", retry=3, wait_time=1)
        process_step.execute_press_key("1.5단계: Alt + Tab 전환", ("alt", "tab"), wait_time=1)
        
    run()
