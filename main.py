from recognition_engine import Recognition_engine
from commands import Command, Commands_container as Commands
from commands_lib import *

from GUI import MyApp
from threading import Thread
import subprocess
# language = "pl-PL"
language = "en-US"

# def run_GUI(engine):
#     app = MyApp()
#     app.add_engine(engine)
#
#     app.run()
#
#
# def run_app(commands):
#     engine = Recognition_engine(commands)
#
#     t = Thread(name="opened app", target=run_GUI, args=[engine])
#     t.start()  # TODO zmienić na proces

def main():
    commands = Commands(language=language)

    commands.add_command(Command("turn off computer", shutdown))
    commands.add_command(Command("restart computer", restart))
    commands.add_command(Command("turn volume down", decrease_volume))
    commands.add_command(Command("turn volume up", increase_volume))
    commands.add_command(Command("calculator", calculator))
    commands.add_command(Command("open", open_app))
    commands.add_command(Command("what is my internet speed", speed_test))
    commands.add_command(Command("create new note", add_note))
    commands.add_command(Command("add new event to calendar", add_event))
    commands.add_command(Command("list events in my calendar", list_events))
    commands.add_command(Command("tell me the price", get_crypto_info))
    commands.add_command(Command("what is the weather like", weather))
    commands.add_command(Command("search in google", search_google))
    commands.add_command(Command("search in youtube", search_youtube))
    commands.add_command(Command("tell me what can you do", list_commands))

    commands.save_to_file()
    commands.read_from_file()

    commands["tell me what can you do"].execute(None)


    run_app(commands)





if __name__ == '__main__':
    main()
