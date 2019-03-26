from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    StringProperty, ReferenceListProperty, ObjectProperty
)
from kivy.uix.scrollview import ScrollView
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Log(ScrollView):
    textLogSP = StringProperty("bla\nbla2\nbla3\nbla4\nbla5\nbla6\nbla7\nbla8\n")

class PlayerView(Widget):
    logOP = ObjectProperty(None)
    def update(self,dt):
        #call ball.move and other stuff
        self.logOP.textLogSP = self.logOP.textLogSP + "\nble"

class SoeApp(App):
    def build(self):
        game = PlayerView()
        Clock.schedule_interval(game.update, 1.0/1.0)
        return game

if __name__ == '__main__':
    SoeApp().run()