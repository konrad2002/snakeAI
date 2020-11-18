# main menu for selection of one of the two modes -> single player and 1 vs 1

from kivy.uix.widget import Widget
from kivy.uix.button import Button

class MainMenu (Widget):
    def __init__ (self, menuApp, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.menuApp = menuApp

        self.pBtn = Button(text="Einzelspieler", pos=(50, 190), size=(300, 50), on_press=self.onSelectSingle)
        self.ppBtn = Button(text="2 Spieler", pos=(50, 120), size=(300, 50), on_press=self.onSelectTwo)
        self.ppppBtn = Button(text="4 Spieler", pos=(50, 50), size=(300, 50), on_press=self.onSelectFour)


        self.add_widget(self.pBtn)
        self.add_widget(self.ppBtn)
        self.add_widget(self.ppppBtn)

    def onSelectSingle(self, btn):
        self.menuApp.showSubMenu(1)

    def onSelectTwo(self, btn):
        self.menuApp.showSubMenu(2)

    def onSelectFour(self, btn):
        self.menuApp.showSubMenu(4)