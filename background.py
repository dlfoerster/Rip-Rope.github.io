from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

class Background(Widget):
    rope_texture = ObjectProperty(None)
    full_background_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create textures
        self.background_image = "full_background.png"
        self.scroll_background = True
        self.rope_texture = Image(source="Images/rope.png").texture
        self.full_background_texture = Image(source="Images/backgrounds/" + self.background_image).texture

    def change_texture_image(self, image):
        self.background_image = image
        if self.background_image != "full_background.png":
            self.scroll_background = False
            self.full_background_texture = Image(source="Images/backgrounds/" + self.background_image).texture
        else:
            self.scroll_background = True
            self.full_background_texture = Image(source="Images/backgrounds/" + self.background_image).texture

    def scroll_textures(self, time_passed):
        # Get the current uvpos of the texture
        uv_x, uv_y = self.rope_texture.uvpos

        # Calculate the new uvpos for scrolling effect
        if App.get_running_app().score < 250:
             uv_y = (uv_y + (time_passed*(1/14.5))) % 1
        elif App.get_running_app().score < 1000 and App.get_running_app().score >= 250:
            uv_y = (uv_y + (time_passed*(1/14.5* App.get_running_app().score/250.0))) % 1
        else:
            uv_y = (uv_y + (time_passed*(1/15.0 * 4))) % 1

        if uv_y < 0.4:
            uv_y = 0.5


        self.rope_texture.uvpos = (uv_x, uv_y)

        # Redraw the texture
        ropeTexture = self.property('rope_texture')
        ropeTexture.dispatch(self)

        if self.scroll_background:
            bg_uv_x, bg_uv_y = self.full_background_texture.uvpos
            if App.get_running_app().score <= 0:
                bg_uv_y = 1
            else:    
                bg_uv_y += time_passed*1/1000

            if bg_uv_y >= 2:
                bg_uv_y = 2
            self.full_background_texture.uvpos = (bg_uv_x, bg_uv_y)
            fullBackgroundTexture = self.property('full_background_texture')
            fullBackgroundTexture.dispatch(self)