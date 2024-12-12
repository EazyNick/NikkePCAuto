import pyautogui
import os
from datetime import datetime


def capture_screen_to_temp():
    """
    현재 화면을 캡처하여 assets/temp 폴더에 저장합니다.
    파일 이름은 현재 시간(년월일_시분초)으로 저장됩니다.
    반환값으로 저장된 파일 경로를 반환합니다.
    """
    # 현재 화면 캡처
    screenshot = pyautogui.screenshot()

    # 저장할 디렉토리 경로 설정
    temp_dir = os.path.abspath(os.path.join("assets", "temp"))
    os.makedirs(temp_dir, exist_ok=True)  # 디렉토리가 없으면 생성

    # 현재 시간으로 파일 이름 설정
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(temp_dir, f"screenshot_{timestamp}.png")

    # 캡처한 이미지를 저장
    screenshot.save(file_path)
    print(f"화면 캡처가 저장되었습니다: {os.path.abspath(file_path)}")
    
    return os.path.abspath(file_path)
