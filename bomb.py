from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

class Bomb(Widget):
    bomb_texture = ObjectProperty(None)
    pos_x = 1
    pos_y = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bomb_texture = Image(source="Images/bomb.png")