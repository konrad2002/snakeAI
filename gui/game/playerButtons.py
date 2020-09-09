# buttons for game with player slot

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
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

            self.buttons = []

            self.readyBtn = Button(
                text = "Bereit",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.onReady
            )

            self.buttons.append(self.readyBtn)



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

            self.buttons.append(self.key1Btn)
            self.buttons.append(self.key2Btn)


            for i,button in enumerate(self.buttons):
                button.size = (
                    self.size[0] / 3,
                    self.size[1] / 3
                )

                button.pos = (
                    
                )



    def onReady(self, a):
        self.game.ready()

    def onSetKeyboard(self, a):
        print("[KEYS] set keyboard for " + str(self.game.instance) + " to " + str(a.id))
        a.color = (0,1,0,1)
        self.game.setKeyboard(int(a.id))