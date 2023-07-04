import mouse
import pyautogui
import time as t
while 1:
    x, y = mouse.get_position()
    mouse.drag(x, y, x, y + 5, duration=0.1)
    t.sleep(0.1)