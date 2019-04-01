from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import (
    StringProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.uix.scrollview import ScrollView
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class TrackColumn(GridLayout):
    infoLP = ListProperty(["a","b","c","d"])
    def __init__(self,**kwargs):
        super(TrackColumn,self).__init__(**kwargs)
        #self.playerLists = [[1,2,3,4]]
        #self.playerLists = ["asd"]

class Log(ScrollView):
    textLogSP = StringProperty("bla\nbla2\nbla3\nbla4\nbla5\nbla6\nbla7\nbla8\n")

class PlayerView(Widget):
    logOP = ObjectProperty(None)
    logOP2 = ObjectProperty(None)
    trackOP1 = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(PlayerView,self).__init__(**kwargs)
        self.i = 0
    
    def update(self,dt):
        #call ball.move and other stuff
        self.logOP.textLogSP = self.logOP.textLogSP + "\nble"
        self.i += 1
        if (self.i > 3):
            self.logOP2.textLogSP = "Hi"
            self.trackOP1.infoLP[0] = "ffff"
        if(self.i > 5):
            self.logOP2.textLogSP = "Hi2"
            

class SoeApp(App):
    def build(self):
        game = PlayerView()
        Clock.schedule_interval(game.update, 1.0/1.0)
        return game

if __name__ == '__main__':
    SoeApp().run()