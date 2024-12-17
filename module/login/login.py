import os
import sys

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("utils"))
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("common"))
sys.path.append(path_manager.get_path("module"))

try:
    from common.V000 import matcher 
    from utils import capture_screen
    from logs import log_manager
    from click_image import ScreenHandler
except Exception as e:
    log_manager.logger.info(f"임포트 실패: {e}")

def main():
    # 현재 화면 캡처
    captured_screen_path = capture_screen()

    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    base_dir = os.path.abspath(os.path.join(current_file, "..", "..", ".."))  # 루트 디렉토리 경로
    # 템플릿 이미지 경로 설정
    template_path = os.path.join(base_dir, "assets", "test", "test.png")

    try:
        # 템플릿 매칭 수행
        is_match, location = matcher.match_template(captured_screen_path, template_path)

        if is_match:
            log_manager.logger.info(f"Template matched at location: {location}")
        else:
            log_manager.logger.info("Template did not match.")
    except ValueError as e:
        log_manager.logger.info(f"Error during matching: {e}")



if __name__ == "__main__":
    main()