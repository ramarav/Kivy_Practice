from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class Box1App(App):
    pass
class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        b1 = Button(text="Hello")
        b2 = Button(text="Happy")
        b3 = Button(text="Learning")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

Box1App().run()
