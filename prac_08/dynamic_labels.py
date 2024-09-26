"""
CP1404 Practical 08 Hunter Kruger-Ilingworth
Dynamic labels app
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Kivy app to dynamically create labels"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Ben", "Liam", "Joel", "David", "John", "Darcy", "Hunter"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI"""
        for name in self.names:
            new_label = Label(text=name)
            self.root.ids.main.add_widget(new_label)


DynamicLabelsApp().run()
