import os
import time
from pynput.keyboard import Key, Controller
from commands import Command, Commands_container as Commands
from recognition_engine import Recognition_engine
from speaking import read_text

from multiprocessing import Process

from math import sqrt

import wolframalpha as wolfram
from word2number import w2n


def shutdown(args):
    print("shutdown")
    # os.system("shutdown /s /t 5") #windows
    # os.system("shutdown now -h") #linux


def restart(args):
    print("restart")
    # os.system("shutdown -t 5 -r -f") #Windows


def increase_volume(args):
    keyboard = Controller()
    # zwieksza o 10
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.15)


def decrease_volume(args):
    keyboard = Controller()
    # zmniejsza o 10
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.15)




