#!/usr/bin/env python 
from kivy.lang import Builder

class MyApp(App):
    def build(self):
        
        self.window = FloatLayout()
        self.lbl = Label(text="Hello world")
        self.window.add_widget(self.lbl)
        return self.window

if __name__ == '__main__': #Documentation suggests that each program file should be called main.py but I think that only matters if you're creating the final App to go onto a phone or tablet we're a long way off from that yet

    MyApp().run() #This must match the name of your App
