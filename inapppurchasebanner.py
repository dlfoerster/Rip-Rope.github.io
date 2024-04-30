from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from specialbuttons import ImageButton, LabelButton
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import kivy.utils
from functools import partial

class InAppPurchaseBanner(FloatLayout):

    def __init__(self, **kwargs):
        self.image_id = kwargs.pop('image_id', '')
        self.purchase_name = kwargs.pop('purchase_name', '')
        self.price = kwargs.pop('price', '')
        super(InAppPurchaseBanner, self).__init__()
        float_layout = FloatLayout()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#029640")))
            self.rect = Rectangle(size=(1,.5), pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)
        unlock_label = Label(
                                    text=self.purchase_name,
                                    size_hint=(.5,.2),
                                    pos_hint={"top": .3, "left": .9},
                                    color=(1,1,1,1),
                                    outline_color=(0, 0, 0, 1),
                                    outline_width=4
                                    )
        image = "Images/" + self.image_id + ".png"
        image_widget = Image(source=image, size_hint=(.5,.8), pos_hint={"top": .9, "left": .9})
        coin_image = Image(source="Images/coin.png", size_hint=(.5,.5), pos_hint={"top": .9, "right": 1})
        price_label = Label(text="$" + self.price + " CAD", 
                            color=(1,1,1,1),
                            outline_color=(0, 0, 0, 1),
                            outline_width=4, 
                            size_hint=(.5,.2), 
                            pos_hint={"top": .5, "right": 1})
        buy_button = ImageButton(source="Images/buy_image.png", size_hint=(.5,.2), pos_hint={"top": .3, "right": 1}, on_release=partial(App.get_running_app().make_purchase))
        
        self.add_widget(image_widget)
        self.add_widget(unlock_label)
        self.add_widget(coin_image)
        self.add_widget(price_label)
        self.add_widget(buy_button)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos