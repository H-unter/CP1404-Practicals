"""
CP1404 Practical 08 Hunter Kruger-Ilingworth
Miles to kilometers conversion app
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for distance unit conversions """
    kilometers = StringProperty()

    def build(self):
        """ build the Kivy app"""
        Window.size = (1000, 500)
        self.title = "Distance Unit Conversions"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion_press(self, value):
        """Convert the miles input into kilometers using conversion factor"""
        try:
            self.kilometers = str(float(value) * 1.609)
        except ValueError:
            self.kilometers = str("undefined")

    def increment_input(self, delta):
        """Increment or decrement the miles input"""
        current_value = float(self.root.ids.input_number.text)
        new_value = current_value + float(delta)
        self.root.ids.input_number.text = str(new_value)


ConvertMilesKmApp().run()
