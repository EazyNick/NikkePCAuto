import os

class PathManager:
    """
    프로젝트 내 모든 주요 폴더 경로를 관리하는 클래스.
    """
    def __init__(self):
        # 프로젝트 최상위 디렉토리 경로 계산
        self.project_root = os.path.abspath(os.path.join(__file__, "..", ".."))

        # 주요 폴더 경로 설정
        self.folders = {
            "assets_ark": os.path.join(self.project_root, "assets", "ark"),
            "assets_dailycheck": os.path.join(self.project_root, "assets", "dailycheck"),
            "assets_favorite": os.path.join(self.project_root, "assets", "favorite"),
            "assets_freind": os.path.join(self.project_root, "assets", "freind"),
            "assets_login": os.path.join(self.project_root, "assets", "login"),
            "assets_mail": os.path.join(self.project_root, "assets", "mail"),
            "assets_outpost": os.path.join(self.project_root, "assets", "outpost"),
            "assets_shop": os.path.join(self.project_root, "assets", "shop"),
            "assets_stagingarea": os.path.join(self.project_root, "assets", "stagingarea"),
            "assets_temp": os.path.join(self.project_root, "assets", "temp"),
            "assets_test": os.path.join(self.project_root, "assets", "test"),
            "commands": os.path.join(self.project_root, "commands"),
            "common": os.path.join(self.project_root, "common"),
            "display": os.path.join(self.project_root, "display"),  
            "git": os.path.join(self.project_root, "git"),
            "logs": os.path.join(self.project_root, "logs"),  # 로그 폴더가 필요한 경우
            "manage": os.path.join(self.project_root, "manage"),
            "module": os.path.join(self.project_root, "module"),
            "utils": os.path.join(self.project_root, "utils"),
        }

    def get_path(self, folder_name):
        """
        지정된 폴더 이름의 경로를 반환합니다.
        
        :param folder_name: 폴더 이름 (예: "utils", "assets_temp")
        :return: 해당 폴더의 절대 경로
        """
        if folder_name not in self.folders:
            raise ValueError(f"'{folder_name}'은(는) 관리되지 않는 폴더입니다.")
        return self.folders[folder_name]

    def list_all_paths(self):
        """
        관리 중인 모든 폴더의 경로를 반환합니다.
        :return: dict
        """
        return self.folders

if __name__ == "__main__":
    # PathManager 객체 생성
    path_manager = PathManager()

    # 모든 경로 출력
    print("=== 관리 중인 디렉토리 경로 목록 ===")
    all_paths = path_manager.list_all_paths()
    for folder_name, path in all_paths.items():
        print(f"{folder_name}: {path}")