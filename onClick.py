from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
import speach as sp

class TestApp(App):
    def build(self):
        button = Button(text = "hello")
        button.bind(on_press = self.pressed)
        return button
    def pressed(self,instance):
        sp.get_audio()

TestApp().run()