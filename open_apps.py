
from commands import Command, Commands_container as Commands
from recognition_engine import Recognition_engine
from speaking import read_text
from threading import Thread
import os
import subprocess



def open_app(args): #todo rozbudowac liste aplikacji (potrzebna sciezka do exe)
    def open_path(path):
        return subprocess.Popen(path)

    apps = {
        "microsoft word": '"C:/Program Files (x86)/Microsoft Office/root/Office16/winword"',
        "microsoft edge": '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"',
    }

    commands = Commands()

    for name, path in apps.items():
        c = Command(name, open_path, path)
        commands.add_command(c)

    args = args.lower()
    text = args.replace("open ", "")
    print(text)

    engine = Recognition_engine(commands)
    command, transcript = engine.recognize_command(text=text)

    if command is None:
        read_text("Tell me what app you wanna open")
        transcript = engine.get_transcript()

        if transcript is not None:
            command, transcript = engine.recognize_command(text=transcript)
            if command is None:
                return

    print("opening", transcript)

    command.execute()

if __name__ == '__main__':
    open_app("open microsoft word")


