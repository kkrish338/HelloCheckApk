from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window

class HelloWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=20, **kwargs)
        Window.clearcolor = (0.2, 0.6, 0.8, 1)  # Light blue background
        self.icon = Image(source='icon.png', size_hint=(None, None), size=(96, 96), allow_stretch=True)
        self.add_widget(self.icon)
        self.input = TextInput(hint_text='Enter your name', size_hint_y=None, height=40, multiline=False)
        self.add_widget(self.input)
        self.button = Button(text='Submit', size_hint_y=None, height=40, background_color=(0.1, 0.5, 0.2, 1))
        self.button.bind(on_press=self.say_hello)
        self.add_widget(self.button)
        self.label = Label(text='', font_size=24, color=(1,1,1,1))
        self.add_widget(self.label)

    def say_hello(self, instance):
        name = self.input.text.strip()
        if name:
            self.label.text = f"Hello {name}!"
        else:
            self.label.text = "Hello!"

class HelloApp(App):
    def build(self):
        self.title = 'Hello Kivy App'
        return HelloWidget()

if __name__ == '__main__':
    HelloApp().run()
