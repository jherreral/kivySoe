#!/usr/bin/env python 
from kivy.app import App #We need to import the bits of kivy we need as we need them as importing everything would slow the app down unnecessarily
from kivy.uix.widget import Widget #this is a thing that you want the App to display
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from Soe_Log import Log

# class userLayout(FloatLayout):
#     def __init__(self,**kwargs):
#         super(userLayout, self).__init__(**kwargs)
#         #self.cols = 2
#         self.map = Label(text="map")
#         self.topBar = Label(text="topBar")
#         self.hand = Label(text="hand")
#         self.log = Log()
#         self.decks = Label(text="decks")
#         self.track = Track()
#         #self.add_widget(self.map)
#         #self.add_widget(self.topBar)
#         #self.add_widget(self.hand)
#         self.add_widget(self.log)
#         #self.add_widget(self.decks)
#         #self.add_widget(self.track)

# class Track(BoxLayout):
#     def __init__(self, **kwargs):
#         super(Track,self).__init__(orientation='vertical',**kwargs)
#         players = 4
#         for player in range(players):
#             self.add_widget(Label(
#                 text="Player"+str(player+1),
#                 size_hint=(.25,1)
#             ))

class myMainApp(App):
    def build(self):
        return userLayout()

if __name__ == '__main__': #Documentation suggests that each program file should be called main.py but I think that only matters if you're creating the final App to go onto a phone or tablet we're a long way off from that yet

    myMainApp().run() #This must match the name of your App
