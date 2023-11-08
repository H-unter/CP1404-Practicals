from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

"""TODO: error check!!!!!"""


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for distance unit conversions """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 500)
        self.title = "Distance Unit Conversions"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = str(float(value) * 1.609)
            self.root.ids.output_label.text = str(result)
        except:
            pass

    def increment_input(self, value):
        try:
            current_value = float(self.root.ids.input_number.text)
            new_value = current_value + float(value)
            self.root.ids.input_number.text = str(new_value)
        except ValueError:
            self.root.ids.input_number.text = "Enter a number"


ConvertMilesKmApp().run()
