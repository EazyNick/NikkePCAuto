import os
import sys
from datetime import datetime

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
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
    from common.V000 import TemplateMatcher, ExactMatchStrategy, ActionHandler
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")
    sys.exit(1)

class ScreenHandler:
    """
    화면 캡처, 템플릿 매칭, 클릭 및 클릭 후 강조된 이미지 저장을 관리하는 클래스.
    """
    def __init__(self):
        # 템플릿 매칭 및 액션 핸들러 초기화
        self.matcher = TemplateMatcher()
        self.matcher.set_strategy(ExactMatchStrategy())
        self.action_handler = ActionHandler()

    def process(self, template_path):
        """
        화면 캡처 → 템플릿 매칭 → 클릭 → 강조된 이미지 저장의 단일 프로세스 실행.

        Args:
            template_path (str): 매칭할 템플릿 이미지의 경로.

        Returns:
            str: 강조된 이미지 파일 경로 또는 에러 메시지.
        """
        try:
            # 1. 화면 캡처
            captured_screen_path = capture_screen()
            log_manager.logger.info(f"화면 캡처 완료: {captured_screen_path}")

            # 2. 템플릿 매칭
            is_match, location = self.matcher.match_template(captured_screen_path, template_path)

            if not is_match:
                log_manager.logger.info("템플릿이 화면에서 발견되지 않았습니다.")
                return "템플릿 매칭 실패"

            log_manager.logger.info(f"템플릿이 매칭된 좌표: {location}")

            # 3. 클릭
            self.action_handler.click(x=location[0], y=location[1])

            # 4. 강조된 스크린샷 저장
            highlighted_path = click_and_save_with_highlight(location)
            log_manager.logger.info(f"강조된 스크린샷 저장 완료: {highlighted_path}")

            return highlighted_path

        except Exception as e:
            log_manager.logger.error(f"프로세스 중 오류 발생: {e}")
            return f"오류 발생: {e}"

if __name__ == "__main__":
    import os

    # ScreenHandler 인스턴스 생성
    screen_handler = ScreenHandler()

    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    project_root = os.path.abspath(os.path.join(current_file, "..", ".."))  # 루트 디렉토리 경로

    # 템플릿 이미지 경로 설정
    template_path = os.path.join(project_root, "assets", "test", "test.png")

    # 프로세스 실행
    result = screen_handler.process(template_path)

    if "오류 발생" not in result:
        print(f"프로세스 완료! 강조된 이미지 저장 경로: {result}")
    else:
        print(result)
