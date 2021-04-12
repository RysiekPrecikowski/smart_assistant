from recognition_engine import Recognition_engine
from commands import Command, Commands_container as Commands
from commands_lib import *
from onClick import TestApp
from kivy.app import App

language = "pl-PL"

def main():
    commands = Commands()

    commands.add_command(Command("Wyłącz komputer", shutdown))
    commands.add_command(Command("Zrestartuj komputer", restart))
    commands.add_command(Command("Ścisz", decrease_volume))
    commands.add_command(Command("Podgłośnij", increase_volume))

    engine = Recognition_engine(commands)


    app = TestApp()
    app.add_engine(engine)

    app.run()


if __name__ == '__main__':
    main()
