import pyautogui
import time

print("Move your mouse to the target menus.")
print("Press Ctrl+C to stop.")
print("-" * 30)

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x} | Y: {y}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone!")
