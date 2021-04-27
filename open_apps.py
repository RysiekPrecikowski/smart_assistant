from commands import Command, Commands_container as Commands
from recognition_engine import Recognition_engine
from speaking import read_text
from threading import Thread
import os

def open_app(args): #todo rozbudowac liste aplikacji (potrzebna sciezka do exe)
    def word():
        os.system('"C:/Program Files (x86)/Microsoft Office/root/Office16/winword"')
    def edge():
        os.system('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
        #todo docelowo komendy w pliku txt!!

    def open_path(path):
        os.system(path)

    commands = Commands()
    commands.add_command(Command("microsoft word", word))
    commands.add_command(Command("microsoft edge", edge))


    c = Command("test edge", open_path, '"C:/Program Files (x86)/Microsoft Office/root/Office16/winword"') #TODO mozna dodawac komendy przez sama sciezke, bez tworzenia dodatkowej funkcji
    commands.add_command(c)



    args = args.lower()
    text = args.replace("open ", "")
    print(text)

    engine = Recognition_engine(commands)
    command, transcript = engine.recognize_command(text=text)

    if command is not None:
        print("opening", transcript)
        t = Thread(name="opened app", target=command.execute)
        t.start()  # TODO jak to zrobic zeby odpalac niezalezny program?
    else:
        # print("Tell what app you wanna open")
        read_text("Tell me what app you wanna open")
        transcript = engine.get_transcript()

        if transcript is not None:
            command, transcript = engine.recognize_command(text=transcript)
            if command is not None:
                print("opening", transcript)
                # p = Process(target= command.execute)
                # p.start()
                # command.execute()

                t = Thread(name="opened app", target=command.execute)
                t.start() #TODO jak to zrobic zeby odpalac niezalezny program?

if __name__ == '__main__':
    # open_app("open microsoft word")
    open_app("open test edge")
    # open_app("open edge")