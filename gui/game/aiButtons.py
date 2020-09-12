# buttons for game with player slot

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

import random

import math

class AiButtons (RelativeLayout):
    def __init__ (self, game, **kwargs):
        super(AiButtons, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.game = game

    def drawBackground(self):
        with self.canvas:
            self.canvas.clear()

            self.sizeX = self.size[0]
            self.sizeY = self.size[1]

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

            self.add_widget(self.readyBtn)


            self.populationInput = TextInput(
                text = "Population",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_text_validate = self.onChangePopulation,
                multiline = False
            )
            self.create100 = Button(
                text = "100 Snakes",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.on100snakes
            )
            self.randomSnake = Button(
                text = "showRandom",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.onShowRandomSnake
            )

            self.buttons.append(self.populationInput)
            self.buttons.append(self.create100)
            self.buttons.append(self.randomSnake)

            self.add_widget(self.populationInput)
            self.add_widget(self.create100)
            self.add_widget(self.randomSnake)

            
            # calculation of button positions and size (depending on number of buttons)
            self.sqrt = math.sqrt(len(self.buttons))
            self.cols = round(self.sqrt + 0.4999)

            for i,button in enumerate(self.buttons):
                if self.game.main.settings.playerMode != 2:
                    button.size_hint = (
                        0.1,
                        ( 1 / self.cols - ( 0.15 / self.cols ) )
                    )
                else:
                    button.size_hint = (
                        1 / self.cols,
                        0.06
                    )

                row = round( ( i / self.cols ) + 0.500001 ) - 1
                col = i % self.cols

                button.pos = (
                    col * self.sizeX / self.cols,
                    row * self.sizeY / self.cols,
                )

                print("Button " + str(i) + ": " + str(col) + " | " + str(row))

    
    def onReady(self, a):
        self.game.ready()

    def on100snakes(self, a):
        self.game.data.tempPopulation = 100

    def onShowRandomSnake(self, a):
        self.game.showSnake(mode = "random")

    def onChangePopulation(self, instance):
        self.game.data.tempPopulation = int(instance.text)
