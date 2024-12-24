import os
import sys


current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("common"))

try:
    # 필요한 모듈 임포트
    from utils import capture_screen, click_and_save_with_highlight
    # from common import TemplateMatcher, ExactMatchStrategy, ActionHandler
    from common import matcher, ActionHandler
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")
    sys.exit(1)

class TemplateProcessor:
    """
    화면 캡처, 템플릿 매칭, 클릭 및 클릭 후 강조된 이미지 저장을 관리하는 클래스.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TemplateProcessor, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # 인스턴스 중복 초기화 방지
            # 템플릿 매칭 및 액션 핸들러 초기화
            self.matcher = matcher
            self.action_handler = ActionHandler()
            self.initialized = True  # 초기화 완료 상태
            log_manager.logger.debug("TemplateProcessor initialized")

    def capture_and_match(self, template_path):
        """
        화면 캡처 후 템플릿 매칭을 수행합니다.

        Args:
            template_path (str): 매칭할 템플릿 이미지의 경로.

        Returns:
            tuple: (bool, tuple) 매칭 성공 여부 및 매칭된 좌표
        """
        captured_screen_path = capture_screen()
        is_match, location = self.matcher.match_template(captured_screen_path, template_path)
        return is_match, location

    def process_click(self, template_path):
        """
        화면 캡처 → 템플릿 매칭 → 클릭 → 강조된 이미지 저장의 단일 프로세스 실행.

        Args:
            template_path (str): 매칭할 템플릿 이미지의 경로.

        Returns:
            bool: 성공(True) 또는 실패(False)
        """
        try:
            # 1. 화면 캡처 및 템플릿 매칭
            is_match, location = self.capture_and_match(template_path)

            if not is_match:
                log_manager.logger.info("템플릿이 화면에서 발견되지 않았습니다.")
                return False

            log_manager.logger.info(f"템플릿이 매칭된 좌표: {location}")

            # 2. 클릭 수행
            self.action_handler.click(x=location[0], y=location[1])
            log_manager.logger.info("클릭 수행 완료")

            # 3. 클릭 좌표 스크린샷 저장
            click_and_save_with_highlight(location)
            return True

        except Exception as e:
            log_manager.logger.error(f"프로세스 중 오류 발생: {e}")
            return False

    def process_double_click(self, template_path):
        """
        화면 캡처 → 템플릿 매칭 → 더블클릭 → 강조된 이미지 저장의 단일 프로세스 실행.

        Args:
            template_path (str): 매칭할 템플릿 이미지의 경로.

        Returns:
            bool: 성공(True) 또는 실패(False)
        """
        try:
            # 1. 화면 캡처 및 템플릿 매칭
            is_match, location = self.capture_and_match(template_path)

            if not is_match:
                log_manager.logger.info("템플릿이 화면에서 발견되지 않았습니다.")
                return False

            log_manager.logger.info(f"템플릿이 매칭된 좌표: {location}")

            # 2. 더블클릭 수행
            self.action_handler.double_click(x=location[0], y=location[1])
            log_manager.logger.info("더블클릭 수행 완료")

            # 3. 클릭 좌표 스크린샷 저장
            click_and_save_with_highlight(location)
            return True

        except Exception as e:
            log_manager.logger.error(f"프로세스 중 오류 발생: {e}")
            return False

if __name__ == "__main__":
    # TemplateProcessor 인스턴스 생성
    screen_handler = TemplateProcessor()

    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    project_root = os.path.abspath(os.path.join(current_file, "..", ".."))  # 루트 디렉토리 경로
    template_base_path = os.path.join(project_root, "assets", "login")

    # 템플릿 이미지 경로 설정
    template_path = os.path.join(template_base_path, "a_icon.png")

    # 단일 클릭 프로세스 실행
    success_click = screen_handler.process_click(template_path)

    if success_click:
        print("단일 클릭 프로세스 완료! 템플릿 매칭 및 클릭이 성공적으로 수행되었습니다.")
    else:
        print("단일 클릭 프로세스 실패! 템플릿을 찾을 수 없거나 오류가 발생했습니다.")

    # 더블클릭 프로세스 실행
    success_double_click = screen_handler.process_double_click(template_path)

    if success_double_click:
        print("더블클릭 프로세스 완료! 템플릿 매칭 및 더블클릭이 성공적으로 수행되었습니다.")
    else:
        print("더블클릭 프로세스 실패! 템플릿을 찾을 수 없거나 오류가 발생했습니다.")

