from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label


class Test(App):
    def build(self):
        screen = Screen()
        return screen
if __name__ == '__main__':
    app = Test()
    app.run()
