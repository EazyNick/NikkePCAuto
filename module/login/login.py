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
    from module import screenhandler
    from display import resize_game_window, focus_game_window
except Exception as e:
    print(f"임포트 실패: {e}")

def run():
    """
    로그인 동작
    """
    log_manager.logger.info("로그인 자동화 프로세스를 시작합니다.")

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "a_icon.png")
    log_manager.logger.info("1단계: 로그인 아이콘 클릭 시작")
    if not screenhandler.process(login_template_path, True):
        log_manager.logger.error("1단계 실패: 로그인 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("1단계 완료: 로그인 아이콘 클릭 성공")
    time.sleep(8)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "b_google.png")
    log_manager.logger.info("2단계: 구글 로그인 시작")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("2단계 실패: 구글 로그인 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("2단계 완료: 구글 로그인 아이콘 클릭 성공")
    time.sleep(3)

    focus_game_window('로그인 - Google 계정 - Chrome')
    time.sleep(1)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "c_google_login.png")
    log_manager.logger.info("3단계: 아이디 로그인")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("3단계 실패: 아이디 로그인 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("3단계 완료: 아이디 로그인 아이콘 클릭 성공")
    time.sleep(3)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "d_keep_going.png")
    log_manager.logger.info("4단계: 계속")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("4단계 실패: '계속' 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("4단계 완료: '계속' 아이콘 클릭 성공")
    time.sleep(5)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "e_closepage.png")
    log_manager.logger.info("5단계: 페이지 닫기")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("5단계 실패: 'closepage' 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("5단계 완료: 'closepage' 아이콘 클릭 성공")
    time.sleep(3)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "f_exit.png")
    log_manager.logger.info("6단계: 웹페이지 종료")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("6단계 실패: 'exit' 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("6단계 완료: 'exit' 아이콘 클릭 성공")
    time.sleep(10)

    focus_game_window('NIKKE')
    time.sleep(1)

    # 'login' 폴더의 템플릿 이미지 경로
    login_template_path = os.path.join(path_manager.get_path("assets_login"), "g_gamestart.png")
    log_manager.logger.info("7단계: 게임 시작")
    if not screenhandler.process(login_template_path):
        log_manager.logger.error("7단계 실패: '게임시작' 아이콘을 찾을 수 없습니다.")
        return
    log_manager.logger.info("7단계 완료: '게임시작' 아이콘 클릭 성공")
    time.sleep(3)
    # log_manager.logger.debug(f"템플릿 경로: {login_template_path}")

    resize_game_window('NIKKE', 2200, 1300)  # 원하는 크기와 위치 설정
    time.sleep(0.1)
    focus_game_window('NIKKE')
    time.sleep(1)

if __name__ == "__main__":
    run()