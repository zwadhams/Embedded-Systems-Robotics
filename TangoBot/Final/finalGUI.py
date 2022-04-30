from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random
from TextToSpeech import *



#Builder.load_file('images.kv')

class MyLayout(GridLayout):
    img = Image(source='images/maps/One.png')
    key = Button(color =(1, 0, .65, 1),
                 background_normal = 'images/items/nokey.png',
                 size_hint_y = None,
                 height=50,
                   )

    health = Button(color =(1, 0, .65, 1),
                    text= "Health 60/60",
                    size_hint_y = None,
                    height=50,
                    )

    map = 1
    enemyID = 1
    
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1

        self.bottom = GridLayout(size_hint_y = None,
                    height=50)
        self.bottom.cols = 2
        
        self.img.keep_ratio= False
        self.img.allow_stretch = True 
        self.add_widget(self.img)
        self.location
        self.enemy
        self.add_widget(self.bottom)


        self.key.bind(on_press=self.location)
        self.bottom.add_widget(self.key)
        

        
        self.health.bind(on_press=self.enemy)
        self.bottom.add_widget(self.health)
        

    def location(self, instance):
        map = random.randint(1,10)
        self.key.background_normal = 'images/items/key.png'
        self.health.text = "Health 50/60"


        if map == 1:
            self.img.source = 'images/maps/One.png'
        elif map == 2:
            self.img.source = 'images/maps/two.png'
        elif map == 3:
            self.img.source = 'images/maps/three.png'
        elif map == 4:
            self.img.source = 'images/maps/six.png'
        elif map == 5:
            self.img.source = 'images/maps/seven.png'
        elif map == 6:
            self.img.source = 'images/maps/eight.png'
        elif map == 7:
            self.img.source = 'images/maps/eleven.png'
        elif map == 8:
            self.img.source = 'images/maps/twelve.png'
        elif map == 9:
            self.img.source = 'images/maps/thirteen.png'
        elif map == 10:
            self.img.source = 'images/enemy/monster.gif'

    def enemy(self, instance):
        enemyID = random.randint(1,2)
        if enemyID == 1:
            self.img.source = 'images/enemy/slime.gif'
            talkBack("Splash")
        elif enemyID == 2:
            self.img.source = 'images/enemy/boss.gif'
            talkBack("Screeeeeeetch")


class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (800,480)
        Window.top = 10
        Window.left = 50
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
