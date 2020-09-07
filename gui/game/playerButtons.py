# buttons for game with player slot

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

class PlayerButtons (RelativeLayout):
    def __init__ (self, game, **kwargs):
        super(PlayerButtons, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.game = game

    def drawBackground(self):
        with self.canvas:
            self.canvas.clear()

            Color(.1, .2, .7, .5)
            self.bg = Rectangle(pos=(0, 0), size=(self.size[0], self.size[1]))

            self.buttonLayer = BoxLayout(padding = 20, orientation = "vertical", size = (self.size[0], self.size[1] - 40), pos = (0, 0))

            self.readyBtn = Button(
                text = "Bereit",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.onReady
            )

            self.buttonLayer.add_widget(self.readyBtn)


            self.key1Btn = Button(
                text = "W-A-S-D",
                id = "1",
                # pos = (100 , 0),
                # size_hint = (.1, .1),
                on_release = self.onSetKeyboard
            )
            self.key2Btn = Button(
                text = "Pfeiltasten",
                id = "2",
                # pos = (200 , 0),
                # size_hint = (.1, .1),
                on_release = self.onSetKeyboard
            )

            self.buttonLayer.add_widget(self.key1Btn)
            self.buttonLayer.add_widget(self.key2Btn)


    def onReady(self, a):
        self.game.ready()

    def onSetKeyboard(self, a):
        print("set keyboard for " + str(self.game.instance) + " to " + str(a.id))
        a.color = (0,1,0,1)
        self.game.setKeyboard(int(a.id))