from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# import bibliotek koniecznych do danych operacji po kliknięciu guzika 

from recognition_engine import Recognition_engine
from typing import Optional
import traceback




class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)


        # Create pannels

        self.controlPanel = GridLayout()
        self.txtPanel = GridLayout()

        # Pannels size
        self.cols = 2
        self.controlPanel.rows = 4
        self.txtPanel.rows = 2

        # Add Pannels to Grid
        self.add_widget(self.txtPanel)
        self.add_widget(self.controlPanel)

        # Create Buttons
        self.ButtonSpeak = Button(text="Click and speak!!!")
        self.ButtonSpeak.bind(on_press=self.pressedSpeak)

        self.ButtonExecute = Button(text="Click and Execute!!!")
        self.ButtonExecute.bind(on_press=self.pressedExecute)

        self.ButtonCommandList = Button(text="Show Command List")
        self.ButtonCommandList.bind(on_press=self.pressedCommandList)

        self.ButtonEnd = Button(text="End")
        self.ButtonEnd.bind(on_press=self.pressedEnd)

        # Add buttons to control Panel
        self.controlPanel.add_widget(self.ButtonSpeak)
        self.controlPanel.add_widget(self.ButtonExecute)
        self.controlPanel.add_widget(self.ButtonCommandList)
        self.controlPanel.add_widget(self.ButtonEnd)

        # Create txt pannels
        self.inputPanel = TextInput(multiline=False)
        self.txtPanel.add_widget(self.inputPanel)

        # add txt pannels to txtPanel
        self.outputPanel = Label(text="Output")
        self.txtPanel.add_widget(self.outputPanel)

        # recognition engine, chyba to musi tu byc
        self.engine = None  # type: Optional[Recognition_engine]


    def print_result(self, result):
        print("res", result)

        if result == None:
            self.outputPanel.text = ""
        else:

            self.outputPanel.text = result



    # WSZYSTKIE PRESSY DO PRZEGLĄDNIĘCIA
    def pressedSpeak(self, instance):
        # klikasz i mówisz
        # dodać rozpoznawanie komendy
        self.outputPanel.text = "speak"  # słowo speak można zastąpić jakimś outputem z komend jeżeli chce nam się w to bawić chcoiaż nie wiem czy to zadziała

        self.print_result(self.engine.listen_and_execute())



    def pressedExecute(self, instance):
        # znajduje daną komende wpisaną i ją wykonuje np  wpisujesz 'turn off computer' klikasz guzik i sie dzieją rzeczy
        # można wywalić te przycisk jak uważasz jak chcemyt go implementować to jutro ogarne żeby to łądnie zczytwyało stry

        try:
            command = self.inputPanel.text
            # self.outputPanel.text = command

            # wywołanie komendy command

            command_to_run, text = self.engine.recognize_command(command)

            print(command_to_run, text)

            self.print_result(command_to_run.execute(text))

        except Exception as ex:
            print("".join(traceback.TracebackException.from_exception(ex).format()))


        self.inputPanel.text = ""

    def pressedCommandList(self, instance):
        # pobiera z pliku tekstowego commands listy komend i wypisanie ich
        f = open('commands')
        lines = f.read()  # -> jest szansa że tu trzeba to będzie zmienic na innego read-a
        # lines = "ten plik z komendami" # to wywalić jak zadziała plik
        lines = lines.replace(',', '\n')
        print(lines)
        self.outputPanel.text = lines

    def pressedEnd(self, instance):
        App.get_running_app().stop()

    def add_engine(self, engine):
        print("ADDING ENGINE")
        self.engine = engine


class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__()
        self.engine = None

    def add_engine(self, engine):
        print("ADDING ENGINE")
        self.engine = engine

    def build(self):
        my_grid = MyGrid()
        self.title = "Assistant"
        my_grid.add_engine(self.engine)
        return my_grid

    def on_stop(self):
        print("Closing")


from commands import Commands_container

if __name__ == '__main__':
    engine = Recognition_engine(Commands_container())
    app = MyApp()
    app.add_engine(engine)
    app.run()
