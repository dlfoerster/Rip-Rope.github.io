from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from specialbuttons import ImageButton, LabelButton
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, Line
import kivy.utils
from functools import partial

class LeaderBoardBanner(FloatLayout):

    def __init__(self, **kwargs):
        self.player = kwargs.pop('player', '')
        self.place = kwargs.pop('place', '')
        self.score = kwargs.pop('score', '')
        self.character = kwargs.pop('character', '')
        super(LeaderBoardBanner, self).__init__()
        float_layout = FloatLayout()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#ADD8E6")))
            self.rect = Rectangle(size=(.5,.5), pos=self.pos)
        with self.canvas.before:
            Color(rgb=(0,0,0,1))
            self.line1 = Line(width=4, rectangle=(self.x,self.y,self.width,self.height))
        with self.canvas.before:
            Color(rgb=(0,0,0,1))
            self.line2 = Line(width=4, rectangle=(self.x,self.y,self.width/5,self.height))
        with self.canvas.before:
            Color(rgb=(0,0,0,1))
            self.line3 = Line(width=4, rectangle=(self.width - (self.width/5),self.y,self.width/4.69,self.height))
        with self.canvas.before:
            Color(rgb=(0,0,0,1))
            self.line4 = Line(width=4, rectangle=(self.x + self.width/5,self.y,self.width/5,self.height))
        self.bind(size=self.update_rect, pos=self.update_rect)

        placement = Label(text=self.place,
                                    size_hint=(.2,.2),
                                    pos_hint={"top": .55, "right": .2},
                                    color=(1,1,1,1),
                                    outline_color=(0, 0, 0, 1),
                                    outline_width=4
                                    )
        
        player = Label(text=self.player,
                                    size_hint=(.6,.2),
                                    pos_hint={"top": .55, "right": .89},
                                    color=(1,1,1,1),
                                    outline_color=(0, 0, 0, 1),
                                    outline_width=4
                                    )
        
        character = Image(source="Images/characters/" + self.character + ".png", size_hint=(1,1), pos_hint={"top": .9, "right": .8})
        
        score = Label(text=self.score,
                                    size_hint=(.2,.2),
                                    pos_hint={"top": .55, "right": .99},
                                    color=(1,1,1,1),
                                    outline_color=(0, 0, 0, 1),
                                    outline_width=4
                                    )

        self.add_widget(player)
        self.add_widget(placement)
        self.add_widget(score)
        self.add_widget(character)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.line1.rectangle = (self.x,self.y,self.width,self.height)
        self.line2.rectangle = (self.x,self.y,self.width/5,self.height)
        self.line3.rectangle = (self.width - self.width/5,self.y,self.width/4.69,self.height)
        self.line4.rectangle = (self.x + self.width/5,self.y,self.width/5,self.height)