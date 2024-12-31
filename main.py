from logs import log_manager
from commands import *

from git.git_manager import *

class NikkeAutomation:
    """
    승리의 여신: 니케 자동화 프로그램
    """
    def __init__(self):
        """
        초기화 메서드
        """
        log_manager.logger.info("Nikke Automation 프로그램 초기화")
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
    import subprocess

    # git_manager = GitManager()
    # pull_strategy = PullStrategy()

    # try:
    #     pull_strategy.sync(git_manager)
    #     print("레포지토리 동기화 성공!")
    # except Exception as e:
    #     log_manager.logger.error(f"레포지토리 동기화 실패: {e}")

    # NikkeAutomation 클래스 인스턴스 생성
    automation = NikkeAutomation()

    # 커맨드 등록
    # automation.register_command("login", LoginCommand())
    # automation.register_command("dailycheck", DailycheckCommand())
    # automation.register_command("freinds", FreindCommand())
    # automation.register_command("mail", MailCommand())
    # automation.register_command("shop", ShopCommand())
    # automation.register_command("stagingarea", StagingAreaCommand())
    # automation.register_command("outpost", OutpostCommand())    
    # automation.register_command("ark", ArkCommand())
    automation.register_command("favorite", Favoritecommand())
    

    # 자동화 시작
    automation.start()

        