import pyautogui
import os
from datetime import datetime

def capture_screen_to_temp():
    """
    현재 화면을 캡처하여 지정된 폴더에 저장합니다.
    파일 이름은 현재 시간(년월일_시분초)으로 저장됩니다.
    반환값으로 저장된 파일 경로를 반환합니다.
    """
    # 현재 화면 캡처
    screenshot = pyautogui.screenshot()

    # 저장할 디렉토리 경로 설정
    base_dir = r"C:\Users\User\Desktop\python\auto\python\NikkePCAuto"
    temp_dir = os.path.join(base_dir, "assets", "temp")
    os.makedirs(temp_dir, exist_ok=True)  # 디렉토리가 없으면 생성

    # 현재 시간으로 파일 이름 설정
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(temp_dir, f"screenshot_{timestamp}.png")

    # 캡처한 이미지를 저장
    screenshot.save(file_path)
    print(f"화면 캡처가 저장되었습니다: {file_path}")

    # 저장된 파일이 30장 이상일 경우 삭제
    clean_up_temp_files(temp_dir)
    
    return file_path

def clean_up_temp_files(directory, max_files=30):
    """
    지정된 디렉토리 내 파일 개수가 max_files를 초과하면 모든 파일을 삭제합니다.

    Args:
        directory (str): 디렉토리 경로.
        max_files (int): 최대 허용 파일 개수. 초과 시 모든 파일 삭제.
    """
    try:
        # 디렉토리 내 파일 목록 가져오기
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # 파일 개수가 max_files를 초과하면 삭제
        if len(files) > max_files:
            for file in files:
                os.remove(file)
            print(f"{len(files)}개의 파일이 삭제되었습니다. 디렉토리: {directory}")
        else:
            print(f"현재 파일 개수: {len(files)}. 삭제 작업은 수행되지 않았습니다.")
    except Exception as e:
        print(f"파일 정리 중 오류 발생: {e}")

# 테스트 실행
if __name__ == "__main__":
    capture_screen_to_temp()