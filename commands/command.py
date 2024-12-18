class Command:
    """
    커맨드 인터페이스

    모든 커맨드는 이 클래스를 상속하여 구현해야 합니다.
    """
    def execute(self):
        """
        커맨드 실행 메서드
        모든 하위 클래스에서 반드시 구현해야 합니다.
        """
        raise NotImplementedError("execute 메서드를 구현해야 합니다.")
