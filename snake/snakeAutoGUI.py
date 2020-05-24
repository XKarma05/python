import pyautogui
import time


def action(key, duree):
    pyautogui.keyDown(key)
    time.sleep(duree)
    pyautogui.keyUp(key)
    time.sleep(1)


pyautogui.FAILSAFE = True

print("Starting")

for i in range(5):
    print(".")
    time.sleep(1)

print("Go")

while 1:
    action("up", 0.1)
    action("right", 0.1)
    action("down", 0.1)
    action("left", 0.1)
