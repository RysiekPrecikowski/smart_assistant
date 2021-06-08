import threading

import keyboard
import time
from recognition_engine import Recognition_engine
from commands import Command, Commands_container as Commands
from commands_lib import *

from GUI import MyApp
from threading import Thread
import subprocess
from multiprocessing import Process

# language = "pl-PL"
language = "en-US"




def main():
    commands = Commands(language=language)

    commands.add_command(Command("turn off computer", shutdown))
    commands.add_command(Command("restart computer", restart))
    commands.add_command(Command("turn volume down by", decrease_volume))
    commands.add_command(Command("turn volume up by", increase_volume))
    commands.add_command(Command("calculate", calculator))
    commands.add_command(Command("open", open_app))
    commands.add_command(Command("what is my internet speed", speed_test))
    commands.add_command(Command("add note", add_note))
    commands.add_command(Command("get notes", get_notes))
    commands.add_command(Command("add event on", add_event)) # add event on 09.06.2021 from 10:00 to 15:00 name spanko
    commands.add_command(Command("list events in my calendar", list_events))
    commands.add_command(Command("tell me the price of", get_crypto_info))
    commands.add_command(Command("what is the weather like in", weather))
    commands.add_command(Command("search in google", search_google))
    commands.add_command(Command("search in youtube", search_youtube))
    commands.add_command(Command("tell me what can you do", list_commands))

    commands.save_to_file()
    commands.read_from_file()

    engine = Recognition_engine(commands)


    app = MyApp()
    app.add_engine(engine)
    app.run()


if __name__ == '__main__':
    main()