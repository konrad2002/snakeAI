# buttons for game with player slot

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

class AiButtons (RelativeLayout):
    def __init__ (self, game, **kwargs):
        super(AiButtons, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.game = game

    def drawBackground(self):
        with self.canvas:
            self.canvas.clear()

            Color(.1, .2, .7, .5)
            self.bg = Rectangle(pos=(0, 0), size=(self.size[0], self.size[1]))

            self.readyBtn = Button(
                text = "Bereit",
                pos = (0 , 0),
                size_hint = (.1, .1),
                on_release = self.onReady
            )

            self.add_widget(self.readyBtn)

    
    def onReady(self, a):
        self.game.ready()