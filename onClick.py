from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
# import speach as sp


def test():
    pass


class TestApp(App):
    def init(self, kwargs):
        super(TestApp, self).init(kwargs)
        self.engine = None

    def build(self):
        button = Button(text = "hello")
        button.bind(on_press = self.pressed)
        return button

    def pressed(self, instance):
        # sp.get_audio()
        # print("pressed")
        self.engine.recognize()

    def add_engine(self, engine):
        self.engine = engine




# if __name__ == '__main__':
    # TestApp().run()
