from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.properties import (
    StringProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.uix.behaviors import DragBehavior
from kivy.uix.scrollview import ScrollView
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Decks(FloatLayout):
    btnDiscardOP = ObjectProperty(None)
    
    def on_press(self):
        self.showDiscardDeck()
        print("Button pressed")

    def showDiscardDeck(self):
        pass

class ListChoice(DragBehavior,GridLayout):
    stackOP=ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(ListChoice,self).__init__(**kwargs)


    def fillWithLabels(self,n):
        for x in range(n):
            l = Label(text="placeholder")
            l.size = l.texture_size
            l.size_hint=(1,None)
            self.stackOP.add_widget(l)

class Track(GridLayout):
    boxOP = ObjectProperty(None)
    #playersInfoLP = ListProperty([])

    def createPlayerColumns(self, playerInfo):
        """ playerInfo must be a list with lists"""
        nOfPlayers = len(playerInfo)        
        for pc in playerInfo:
            newPlayer = TrackColumn()
            for x in range(nOfPlayers):
                newPlayer.infoLP[x]=pc[x]
            self.boxOP.add_widget(newPlayer,0)

    def updateColumns(self,playerInfo):
        #Change enumerate to zip playerInfo-boxOP.children
        adjustedInfo = playerInfo[::-1]
        for idx,child in enumerate(self.boxOP.children):
            for x in range(4):
                child.infoLP[x]=adjustedInfo[idx][x]

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
    
    def __init__(self,boardData,**kwargs):
        super(PlayerView,self).__init__(**kwargs)
        self.i = 0
        self.trackSet = False
        self.boardData = boardData
    
    def update(self,dt):
        #call ball.move and other stuff
        self.logOP.textLogSP = self.logOP.textLogSP + "\nble"
        self.i += 1
        if (self.i > 2):
            self.logOP2.textLogSP = "Hi"
            self.listOP1.fillWithLabels(3)
            if not self.trackSet:
                self.trackOP0.createPlayerColumns(self.boardData.track)
                self.trackSet = True
        if(self.i > 4):
            self.logOP2.textLogSP = "Hi2"
            self.boardData.track[0][0] = 7
            self.trackOP0.updateColumns(self.boardData.track)

class Card:
    def __init__(self,name):
        self.name = name

class BoardData:
    def __init__(self):
        self.log = ("You spin me \n"
                    "You spin me right round, baby\n"
                    "Right round like a record, baby\n"
                    "Right round round round\n"
                    "You spin me right round, baby\n"
                    "Right round like a record, baby\n"
                    "Right round round round")
        self.track = [[1,1,1,1],
                    [2,2,2,2],
                    [3,3,3,3],
                    [4,4,4,4]]
        self.turnDeck = [Card("Copter"),
                        Card("Sniper")]
        self.discardDeck = [Card("Diplomacy"),
                            Card("Revolution")]
        self.map = None

class SoeApp(App):
    def build(self):
        boardData = self.getBoardData()
        game = PlayerView(boardData)
        Clock.schedule_interval(game.update, 1.0/1.0)
        return game

    def getBoardData(self):
        return BoardData()

if __name__ == '__main__':
    SoeApp().run()