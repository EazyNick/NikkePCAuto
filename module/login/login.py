import os
import sys

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("assets_login"))
sys.path.append(path_manager.get_path("module"))

try:
    from logs import log_manager
    from module import screenhandler
except Exception as e:
    log_manager.logger.info(f"임포트 실패: {e}")

def run():
    """
    로그인 동작
    """
    log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "a_icon.png")
    # log_manager.logger.debug(f"템플릿 경로: {login_template_path}")

    # 1단계: 로그인 아이콘 클릭
    log_manager.logger.info("1단계: 로그인 아이콘 클릭 시작")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("1단계 실패: 로그인 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("1단계 완료: 로그인 아이콘 클릭 성공")



if __name__ == "__main__":
    run()