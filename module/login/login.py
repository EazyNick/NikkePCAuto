import os
import sys

# 프로젝트 루트 경로 추가
current_file = os.path.abspath(__file__)  # 현재 파일의 절대 경로
project_root = os.path.abspath(os.path.join(current_file, "..", "..", ".."))
sys.path.append(project_root)

from manage import PathManager 

from common.V000 import matcher 
from utils import capture_screen_to_temp

def main():
    # 현재 화면 캡처
    captured_screen_path = capture_screen_to_temp()

    # 템플릿 매칭 수행 (정확한 경로 사용)
    template_path = r"C:\Users\User\Desktop\python\auto\python\NikkePCAuto\assets\test\test.png" # 절대 경로 생성

    try:
        # 템플릿 매칭 수행
        is_match, location = matcher.match_template(captured_screen_path, template_path)

        if is_match:
            print(f"Template matched at location: {location}")
        else:
            print("Template did not match.")
    except ValueError as e:
        print(f"Error during matching: {e}")



if __name__ == "__main__":
    main()