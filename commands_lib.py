import os
import time
from pynput.keyboard import Key, Controller
from commands import Command, Commands_container as Commands
from recognition_engine import Recognition_engine
from speaking import read_text

from math import sqrt

from calculator import calculator
from open_apps import open_app
from my_speedtest import speed_test
from notes import add_note
from my_calendar import add_event, list_events

from crypto_prices import get_crypto_info
from weather import weather
from web_searching import search_youtube, search_google


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


def list_commands(args):
    commands = Commands()
    commands.read_from_file()
    print(commands.commands.keys())


