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

class Track(GridLayout):
    boxOP = ObjectProperty(None)
    #playersInfoLP = ListProperty([])

    def createPlayerColumns(self, playerInfo):
        """ playerInfo must be a list with lists"""        
        for pc in playerInfo:
            newPlayer = TrackColumn()
            newPlayer.infoLP.set(pc)
            self.boxOP.add_widget(newPlayer)

    def updateColumns(self,playerInfo):
        #Change enumerate to zip playerInfo-boxOP.children
        for idx,child in enumerate(self.boxOP.children):
            child.infoLP.set(playerInfo[idx])

class TrackColumn(GridLayout):
    infoLP = ListProperty([0,0,0,0])
    def __init__(self,**kwargs):
        super(TrackColumn,self).__init__(**kwargs)
        #self.playerLists = [[1,2,3,4]]
        #self.playerLists = ["asd"]

class Log(ScrollView):
    textLogSP = StringProperty("bla\nbla2\nbla3\nbla4\nbla5\nbla6\nbla7\nbla8\n")

class PlayerView(Widget):
    logOP = ObjectProperty(None)
    logOP2 = ObjectProperty(None)
    trackOP0 = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(PlayerView,self).__init__(**kwargs)
        self.i = 0
        self.trackSet = False
        self.playerTrackData = [
        [1,1,1,0],
        [2,2,2,0],
        [3,3,3,0]]
    
    def update(self,dt):
        #call ball.move and other stuff
        self.logOP.textLogSP = self.logOP.textLogSP + "\nble"
        self.i += 1
        if (self.i > 3):
            self.logOP2.textLogSP = "Hi"
            if not self.trackSet:
                self.trackOP0.createPlayerColumns(self.playerTrackData)
                self.trackSet = True
        if(self.i > 5):
            self.logOP2.textLogSP = "Hi2"
            self.playerTrackData[0][0] = 7
            self.trackOP0.updateColumns(self.playerTrackData)


    

class SoeApp(App):
    def build(self):
        game = PlayerView()
        Clock.schedule_interval(game.update, 1.0/1.0)
        return game

if __name__ == '__main__':
    SoeApp().run()