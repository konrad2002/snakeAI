# app to show game

from gui.nav import GuiNav
from gui.game.controller import GameController

from kivy.uix.floatlayout import FloatLayout

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

import sqlite3

class GameApp (App):
    def build(self):
        print("[game] created " + str(self.__class__))

        root = Widget(size=(self.mainController.settings.screenX, self.mainController.settings.screenY))

        self.nav = GuiNav(self)

        root.add_widget(self.nav)

        self.games = []

        self.db = sqlite3.connect("file:snake.db?mode=rwc", uri=True)
        self.cursor = self.db.cursor()

        if self.mainController.settings.playerMode == 2:
            self.layoutType = 2
            self.mainController.settings.cols = 2
        else:
            self.layoutType = 1

        if self.mainController.settings.playerMode == 4:
            self.mainController.settings.cols = 2
            self.mainController.settings.rows = 2

        for i in range(self.mainController.settings.playerMode):
            game = GameController(self.mainController,
                instance = ( i + 1 )
            )

            root.add_widget(game)
            self.games.append(game)

        self.clock = Clock.schedule_interval(self.mainLoop, self.mainController.settings.speed)


        return root


    def setMainController(self, mainController):
        self.mainController = mainController
        print("[game] set window size to: " + str((self.mainController.settings.screenX, self.mainController.settings.screenY)))
        Window.size = (self.mainController.settings.screenX, self.mainController.settings.screenY)

    def checkReady(self):
        ready = True

        for game in self.games:
            if game.data.ready == False:
                ready = False

        if ready:
            for game in self.games:
                game.start()

    def mainLoop(self, a):
        for game in self.games:
            if game.data.state > 2:
                game.update()

    def modifyClock(self):
        Clock.unschedule(self.clock)
        self.clock = Clock.schedule_interval(self.mainLoop, self.mainController.settings.speed)
        self.nav.speedLbl.text = str(self.mainController.settings.speed)