import os
import time
from pynput.keyboard import Key, Controller
from commands import Command, Commands_container as Commands
from recognition_engine import Recognition_engine
from speaking import read_text

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


def open_app(args): #todo rozbudowac liste aplikacji (potrzebna sciezka do exe)
    def word():
        os.system('"C:/Program Files (x86)/Microsoft Office/root/Office16/winword"')
    def edge():
        os.system('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
        #todo docelowo komendy w pliku txt!!

    commands = Commands()
    commands.add_command(Command("microsoft word", word))
    commands.add_command(Command("microsoft edge", edge))

    args = args.lower()
    text = args.replace("open ", "")
    print(text)

    engine = Recognition_engine(commands)
    command, transcript = engine.recognize_command(text=text)

    if command is not None:
        print("opening", transcript)
        command.execute()
    else:
        print("Tell what app you wanna open")
        transcript = engine.get_transcript()

        if transcript is not None:
            command, transcript = engine.recognize_command(text=transcript)
            if command is not None:
                print("opening", transcript)
                command.execute()



def calculator(args): #TODO napisac to od nowa xd
    def add(numbers):
        if len(numbers) == 0:
            return None
        res = 0
        print(numbers)
        for a in numbers:
            res += a
        return res

    def subtract(numbers):
        if len(numbers) != 2:
            return None
        return numbers[1] - numbers[0]

    def multiply(numbers):
        if len(numbers) == 0:
            return None
        res = 1
        print(numbers)
        for a in numbers:
            res *= a
        return res

    def divide(numbers):
        if len(numbers) != 2:
            return None
        return numbers[0] / numbers[1]

    def square_root(number):
        print(number[0])
        return sqrt(number[0])

    def prepare(text, command):
        if command is not None and text is not None:
            text = text.replace(command.normalized, "")
            print(text)
            if command.action == add or command.action == multiply:
                text = text.replace("+", "and")

                numbers = text.split("and")

            if command.action == subtract:
                numbers = text.split("from")

            if command.action == divide:
                numbers = text.split("by")

            if command.action == square_root:
                numbers = [text.split("of")[1]]

            print(numbers)
            numbers = [w2n.word_to_num(number) for number in numbers]
            print(numbers)
            return numbers
        else:
            return None

    print("calculator")

    commands = Commands()
    commands.add_command(Command("add", add))
    commands.add_command(Command("subtract", subtract))
    commands.add_command(Command("multiply", multiply))
    commands.add_command(Command("divide", divide))
    commands.add_command(Command("root", square_root))

    test_cases = ["add twenty three and one",
                  "subtract two from twenty one",
                  "multiply two and three and twenty one",
                  "divide six by two",
                  "root of thirty six"]

    engine = Recognition_engine(commands)

    transcript, options = engine.get_transcript(all=True)
    #
    # transcript = "add one and two"

    print("TRANSCRIPT", transcript)
    print("OPTIONS", options)

    def xd(transcript):
        transcript = transcript.replace("+", "and +")
        return transcript

    if transcript is not None:
        transcript = xd(transcript)
        command, transcript = engine.recognize_command(text=transcript, options=options)

        print("KURWA", transcript, command)
        if command is not None:
            transcript = xd(transcript)
            print(transcript)
            normalized = Command.normalize(transcript)
            print("COMMAND", command)

            res = command.execute(prepare(normalized, command))
            read_text("result of " + transcript + " is " + str(res), language="en-US")  # TODO language :c
