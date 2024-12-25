import pyautogui
import os
from datetime import datetime
import cv2
import numpy as np
import sys


current_file = os.path.abspath(__file__) 
project_root = os.path.abspath(os.path.join(current_file, "..", ".."))
sys.path.append(project_root)

from manage import PathManager

path_manager = PathManager()
sys.path.append(path_manager.get_path("logs"))

try:
    from logs import log_manager
except Exception as e:
    print(f"임포트 실패: {e}")

def capture_screen():
    """
    현재 화면을 캡처하여 지정된 폴더에 저장합니다.
    파일 이름은 현재 시간(년월일_시분초)으로 저장됩니다.
    반환값으로 저장된 파일 경로를 반환합니다.
    """
    # 현재 화면 캡처
    screenshot = pyautogui.screenshot()

    # 저장할 디렉토리 경로 설정
    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    base_dir = os.path.abspath(os.path.join(current_file, "..", ".."))  # 루트 디렉토리 경로
    temp_dir = os.path.join(base_dir, "assets", "temp")
    os.makedirs(temp_dir, exist_ok=True)  # 디렉토리가 없으면 생성

    # 현재 시간으로 파일 이름 설정
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"screenshot_{timestamp}.png"
    file_path = os.path.join(temp_dir, file_name)

    # 캡처한 이미지를 저장
    screenshot.save(file_path)
    log_manager.logger.debug(f"화면 캡처가 저장되었습니다: {file_name}")

    # 저장된 파일이 30장 이상일 경우 삭제
    clean_up_temp_files(temp_dir)
    
    return file_path

def click_and_save_with_highlight(coords):
    """
    temp 폴더의 가장 최근에 생성된 이미지를 불러와 좌표를 클릭한 위치를 강조 표시하고, 저장합니다.

    Args:
        coords (tuple): (x, y) 클릭 좌표.

    Returns:
        str: 강조 표시된 새 스크린샷의 파일 경로.
    """
    # 루트 디렉토리 설정 (NikkePCAuto)
    current_file = os.path.abspath(__file__)  # 현재 파일 절대 경로
    base_dir = os.path.abspath(os.path.join(current_file, "..", ".."))  # 루트 디렉토리 경로
    temp_dir = os.path.join(base_dir, "assets", "temp")
    os.makedirs(temp_dir, exist_ok=True)  # 디렉토리가 없으면 생성

    # temp 폴더에서 가장 최근에 생성된 PNG 파일 찾기
    try:
        png_files = [
            os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith(".png")
        ]
        if not png_files:
            raise FileNotFoundError("temp 폴더에 PNG 파일이 존재하지 않습니다.")
        latest_file = max(png_files, key=os.path.getctime)
    except Exception as e:
        log_manager.logger.error(f"최근 파일 검색 중 오류 발생: {e}")
        return None

    # 이미지를 OpenCV 형식으로 불러오기
    image = cv2.imread(latest_file)
    if image is None:
        log_manager.logger.error(f"이미지를 불러올 수 없습니다: {latest_file}")
        return None

    # 클릭 좌표 강조 표시 (십자 표시)
    x, y = coords
    height, width, _ = image.shape
    # 가로 선 그리기
    cv2.line(image, (0, y), (width, y), color=(0, 0, 255), thickness=2)
    # 세로 선 그리기
    cv2.line(image, (x, 0), (x, height), color=(0, 0, 255), thickness=2)

    # 새 파일 이름 설정
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"highlighted_{timestamp}.png"
    new_file_path = os.path.join(temp_dir, file_name)

    # 강조된 이미지를 저장
    cv2.imwrite(new_file_path, image)
    log_manager.logger.debug(f"좌표가 지정된 스크린샷이 저장되었습니다: {file_name}")

    return new_file_path

def clean_up_temp_files(directory, max_files=100):
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
            log_manager.logger.info(f"{len(files)}개의 파일이 삭제되었습니다. 디렉토리: {directory}")
        else:
            log_manager.logger.info(f"현재 파일 개수: {len(files)}. 삭제 작업은 수행되지 않았습니다.")
    except Exception as e:
        log_manager.logger.info(f"파일 정리 중 오류 발생: {e}")


# 테스트 실행
if __name__ == "__main__":
    capture_screen()
    coords = (100, 200)  # 테스트용 좌표
    click_and_save_with_highlight(coords)