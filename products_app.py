from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty


class ShoppingApp(App):
    cart_total = NumericProperty()

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "CP1404 Meetup"
        self.root = Builder.load_file("products_app.kv")
        return self.root

    def press_entry(self, instance):
        """Handle pressing product buttons."""
        # Each button was given its own .product object reference, so we can get it directly
        product = instance.product
        self.cart_total += product.cost

    def press_reset(self):
        """Handle pressing reset button."""
        self.cart_total = 0


ShoppingApp().run()
