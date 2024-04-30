from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

class Eagle(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.eagle_texture = Image(source="Images/eagle2.png")
