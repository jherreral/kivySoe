from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class Log(ScrollView):
    def __init__(self,**kwargs):
        super(Log,self).__init__(**kwargs)
        self.pos_hint={'center_x':1,'center_y':1}
        self.size_hint=(.5,.5)
        with self.canvas:
            Color(.5,.5,.5,.5)
            self.rect = Rectangle(
                pos=self.center,
                size=(self.width/2.,
                      self.height/2.))
        self.lbl=Label(
            text="Loglog\nlogloglog"
        )
        with self.lbl.canvas:
            Color(.5,.5,.5,.5)
        self.add_widget(self.lbl)
