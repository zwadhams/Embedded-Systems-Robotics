import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        self.window = GridLayout()
        self.icon = 'hello.jpg'
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y" : 0.5}
        self.window.add_widget(Image(source='hello.jpg',
                                     size_hint = (3,3)))
        self.question = Label(text="What is your robot's name?",
                              font_size = 36,
                              color = '#00abFF')
        self.window.add_widget(self.question)
        self.answer = TextInput(multiline = False,
                                padding_y = (20 ,20),
                                padding_x = (10,10),
                                size_hint = (1, 0.9))
        self.window.add_widget(self.answer)
        self.button = Button(text="Talk")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        
        return self.window

    def callback(self, instance):
        print(instance)
        self.question.text = "Hello " + self.answer.text + "!"


def main():
    MyApp().run()
main()
