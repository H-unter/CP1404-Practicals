from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for distance unit conversions """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 500)
        self.title = "Distance Unit Conversions"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKmApp().run()
