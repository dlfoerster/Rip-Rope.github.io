from kivy.uix.image import Image
from kivy.app import App

class Character(Image):
    velocity = 0
    pos_x = 3
    moving = False
    def on_touch_move(self, touch):
        if self.moving == False:
            if touch.dx > 0:
                self.velocity = 1000
            elif touch.dx < 0:
                self.velocity = -1000
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.velocity > 0:
            self.source = "Images/jump_images/" + App.get_running_app().current_character + "_jump_right.png"
        elif self.velocity < 0:
            self.source = "Images/jump_images/" + App.get_running_app().current_character + "_jump_left.png"
        return super().on_touch_up(touch)