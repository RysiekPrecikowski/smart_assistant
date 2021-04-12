import os
import time
from pynput.keyboard import Key,Controller



def shutdown():
    print("shutdown")
    # os.system("shutdown /s /t 5") #windows
    # os.system("shutdown now -h") #linux

def restart():
    print("restart")
    os.system("shutdown -t 5 -r -f") #Windows

def increase_volume():
    keyboard = Controller()
    #zwieksza o 10
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.15)

def decrease_volume():
    keyboard = Controller()
    #zmniejsza o 10
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.15)