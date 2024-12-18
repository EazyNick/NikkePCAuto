from common.V000 import matcher
from utils import capture_screen
from logs import log_manager
from commands import Command, LoginCommand

class NikkeAutomation:
    """
    승리의 여신: 니케 자동화 프로그램
    """
    def __init__(self):
        """
        초기화 메서드
        """
        log_manager.logger.info("Nikke Automation 프로그램 초기화")
        # self.matcher = matcher
        self.capture_screen = capture_screen
        self.commands = {}  # 커맨드 등록용 딕셔너리

    def register_command(self, command_name, command):
        """
        커맨드 등록
        Args:
            command_name (str): 커맨드 이름
            command (Command): 커맨드 객체
        """
        if not isinstance(command, Command):
            raise TypeError("command는 Command 클래스의 인스턴스여야 합니다.")
        self.commands[command_name] = command
        log_manager.logger.info(f"커맨드 등록: {command_name}")

    def run_command(self, command_name):
        """
        커맨드 실행
        Args:
            command_name (str): 실행할 커맨드 이름
        """
        if command_name not in self.commands:
            log_manager.logger.error(f"커맨드 '{command_name}'가 등록되지 않았습니다.")
            return
        try:
            log_manager.logger.info(f"커맨드 '{command_name}' 실행 시작")
            self.commands[command_name].execute()
            log_manager.logger.info(f"커맨드 '{command_name}' 실행 완료")
        except Exception as e:
            log_manager.logger.error(f"커맨드 '{command_name}' 실행 중 오류 발생: {e}")

    def start(self):
        """
        자동화 시작 메서드
        """
        log_manager.logger.info("Nikke Automation 프로그램 시작")
        try:
            # 등록된 모든 커맨드 순차 실행
            for command_name, command in self.commands.items():
                log_manager.logger.info(f"등록된 커맨드 실행: {command_name}")
                command.execute()
        except Exception as e:
            log_manager.logger.error(f"자동화 도중 오류 발생: {e}")
            self.terminate()

    def terminate(self):
        """
        프로그램 종료 메서드
        """
        log_manager.logger.info("Nikke Automation 프로그램 종료")
        exit(1)


if __name__ == "__main__":
    # NikkeAutomation 클래스 인스턴스 생성
    automation = NikkeAutomation()

    # 커맨드 등록
    automation.register_command("login", LoginCommand())
    # automation.register_command("shop", ShopCommand())

    # 자동화 시작
    automation.start()

    # import cv2
    # import os
    # # 현재 화면 캡처
    # captured_screen_path = capture_screen()

    # # 템플릿 매칭 수행 (정확한 경로 사용)
    # # 루트 디렉토리 설정 (NikkePCAuto)
    # base_dir = os.path.abspath(__file__)  # 현재 파일 절대 경로
    # # 템플릿 이미지 경로 설정
    # project_root = os.path.abspath(os.path.join(base_dir, ".."))
    # template_path = os.path.join(project_root, "assets", "test", "test.png")

    # img = cv2.imread(captured_screen_path)

    # if captured_screen_path is None:
    #     raise ValueError("Screen image could not be loaded.")
    # if template_path is None:
    #     raise ValueError("Template image could not be loaded.")

    # is_match, location = matcher.match_template(captured_screen_path, template_path)

    # if is_match:
    #     log_manager.logger.info(f"Template matched at location: {location}")
    # else:
    #     log_manager.logger.info("Template did not match.")
        