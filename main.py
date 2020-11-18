#  +–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––+
#  |                                    SnakeAI                                  |
#  |       Snake game with artificial neural network and genetic algorithm       |
#  +–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––+
#  |                                                                             |
#  |  creator:       Konrad Weiß       email:   info@logilutions.de              |
#  |  start of dev:  4.8.2020          url:     logilutions.de/snakeAI           |
#  |  version:       see about.md      github:  github.com/konrad2002/snakeAI    |
#  |                                                                             |
#  |                (C) 2020 - Konrad Weiß and logilutions.de                    |
#  |                                                                             |
#  +–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––+


# import local classes
from settings import Settings

from gui.app.menu import MenuApp
from gui.app.game import GameApp

# import used kivy parts
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

# random, numpy, time, sys, json, socket and sqlite3
from random import randrange
import numpy as np
import time
import sys
import json
import socket

class MainController (object):
    def __init__ (self):
        self.settings = Settings()

    def run (self):
        if self.settings.configurated:
            #sth
            print("configuration set")
            self.showGame()
        else:
            self.showMenu()

    def showMenu (self):
        self.menuApp = MenuApp()
        self.menuApp.setMainController(self)
        self.menuApp.run()

    def showGame(self):
        self.gameApp = GameApp()
        self.gameApp.setMainController(self)
        self.gameApp.run()

    # if conf is done write data into settings
    def setConfiguration(self):
        print("[menu] set configuration")
        self.settings.playerMode = self.menuApp.playerMode
        self.settings.playerTypes = self.menuApp.playerTypes
        self.settings.configurated = True

        self.menuApp.stop()

        self.run()

    def stopGame(self):
        self.gameApp.stop()
        self.run()

    def stop(self):
        if self.settings.gameStarted:
            self.gameApp.stop()
        else:
            self.menuApp.stop()



main = MainController()
main.run()