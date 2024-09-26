"""
CP1404 Practical 08 Hunter Kruger-Ilingworth
Greet the user based on name input
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """Handle clear button press"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        """Handle greet button press"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
