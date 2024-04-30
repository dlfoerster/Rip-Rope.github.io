from kivy.uix.widget import Widget
from kivy.uix.image import Image
from random import choice

class ExtraLife(Widget):
    velocity_x = choice([-200,200])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
