from recognition_engine import Recognition_engine
from commands import Command, Commands_container as Commands
from commands_lib import *
from GUI import MyApp


# language = "pl-PL"
language = "en-US"

def main():
    commands = Commands(language=language)

    commands.add_command(Command("turn off computer", shutdown))
    commands.add_command(Command("restart computer", restart))
    commands.add_command(Command("turn volume down", decrease_volume))
    commands.add_command(Command("turn volume up", increase_volume))
    # commands.add_command(Command("calculator", calculator))
    # commands.add_command(Command("open", open_app))

    engine = Recognition_engine(commands)


    app = MyApp()
    app.add_engine(engine)

    app.run()



if __name__ == '__main__':
    main()
