import sys
import os


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))
sys.path.append(path_manager.get_path("module"))
sys.path.append(path_manager.get_path("commands"))

try:
    from logs import log_manager
    from commands import Command
    from module import favorite_run
except Exception as e:
    print(f"임포트 실패: {e}")

class Favoritecommand(Command):
    """
    호감도 커맨드
    """
    def execute(self):
        log_manager.logger.info("호감도 실행 시작")
        try:
            favorite_run()
            log_manager.logger.info("호감도 실행 완료")
        except Exception as e:
            log_manager.logger.error(f"호감도 실행 중 오류 발생: {e}")

if __name__ == "__main__":
    log_manager.logger.info("Favoritecommand 테스트 시작")

    # LoginCommand 인스턴스 생성
    command = Favoritecommand()

    # 성공 테스트
    try:
        log_manager.logger.info("성공 테스트 실행")
        command.execute()
        log_manager.logger.info("성공 테스트 완료")
    except Exception as e:
        log_manager.logger.error(f"성공 테스트 실패: {e}")

    # 실패 테스트
    try:
        log_manager.logger.info("실패 테스트 실행")

        # freind_run.run 함수에 강제로 예외 발생
        from module import freind_run
        freind_run.run = lambda: (_ for _ in ()).throw(Exception("로그인 오류"))

        command.execute()
    except Exception as e:
        log_manager.logger.error(f"실패 테스트에서 발생한 예외: {e}")

    log_manager.logger.info("Favoritecommand 테스트 종료")

