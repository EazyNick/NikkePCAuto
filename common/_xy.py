import pyautogui
import keyboard
import time

def track_mouse_coordinates():
    """
    실시간으로 마우스 좌표를 추적하여 출력합니다.
    'q' 키를 누르면 프로그램 종료.
    """
    print("마우스 좌표 추적을 시작합니다. 'q'를 누르면 종료됩니다.")
    try:
        while True:
            # 현재 마우스 좌표 가져오기
            x, y = pyautogui.position()
            print(f"마우스 좌표: X={x}, Y={y}", end="\r")  # 실시간 출력
            time.sleep(0.1)  # 0.1초마다 업데이트
            
            # 'q' 키가 눌리면 종료
            if keyboard.is_pressed('q'):
                print("\n좌표 추적 종료.")
                break
    except KeyboardInterrupt:
        print("\n사용자가 종료했습니다.")

if __name__ == "__main__":
    track_mouse_coordinates()
