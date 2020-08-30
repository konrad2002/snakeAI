# app to show up menus

from gui.menu.main import MainMenu
from gui.menu.sub import SubMenu

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window

class MenuApp (App):
    def build (self):
        print("[game] created " + str(self.__class__))

        self.playerMode = 0

        Window.size = (400, 290)
        root = Widget()

        self.mainMenu = MainMenu(self)

        root.add_widget(self.mainMenu)

        return root

    def setMainController(self, mainController):
        self.mainController = mainController

    def showSubMenu(self, menuType):
        self.backBtn = Button(text="Zurück", pos=(15, 270), size=(50, 20), on_press=self.showMainMenu)
        self.root.add_widget(self.backBtn)

        self.playerMode = menuType
        self.subMenu = SubMenu(self)
        
        self.root.add_widget(self.subMenu)
        self.root.remove_widget(self.mainMenu)

    def showMainMenu(self, a):
        self.root.clear_widgets()
        self.root.add_widget(self.mainMenu)

    def updatePlayerTypes(self):
        self.playerTypes = self.subMenu.playerTypes
        print("[menu] updated playerTypes: " + str(self.playerTypes))

        setAll = True

        for x in self.playerTypes:
            if (x == 0):
                setAll = False

        if setAll:
            self.startBtn = Button(text="Starten", size=(70, 30), pos=(320, 10), on_release=self.onStart)
            self.subMenu.add_widget(self.startBtn)
    
    def onStart(self, a):
        self.mainController.setConfiguration()