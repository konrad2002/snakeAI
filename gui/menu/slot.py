# menu which shows list of game modes and ai modes to select for a slot

from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SlotMenu (GridLayout):
    def __init__ (self, parentMenu, slot, **kwargs):
        super(SlotMenu, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.parentMenu = parentMenu
        self.slot = slot

        self.cols = 3

        self.height = 220
        self.width = 400
        self.row_default_height = 110

        self.typeBtns = []

        self.type1Btn = Button(text="Spieler normal", size=(120, 100), on_release=lambda *args: self.onSelectType(1))
        self.type4Btn = Button(text="Spieler Snake", size=(120, 100), on_release=lambda *args: self.onSelectType(2))
        self.type2Btn = Button(text="KNN normal", size=(120, 100), on_release=lambda *args: self.onSelectType(3))
        self.type5Btn = Button(text="KNN Snake", size=(120, 100), on_release=lambda *args: self.onSelectType(4))
        self.type3Btn = Button(text="Zufall", size=(120, 100), on_release=lambda *args: self.onSelectType(5))
        self.type6Btn = Button(text="Algorithmus", size=(120, 100), on_release=lambda *args: self.onSelectType(6))

        self.add_widget(self.type1Btn)
        self.add_widget(self.type2Btn)
        self.add_widget(self.type3Btn)
        self.add_widget(self.type4Btn)
        self.add_widget(self.type5Btn)
        self.add_widget(self.type6Btn)

        self.typeBtns.append(self.type1Btn)
        self.typeBtns.append(self.type2Btn)
        self.typeBtns.append(self.type3Btn)
        self.typeBtns.append(self.type4Btn)
        self.typeBtns.append(self.type5Btn)
        self.typeBtns.append(self.type6Btn)

    def onSelectType(self, playerType):
        print(str(playerType) + " was selected for slot " + str(self.slot))
        self.parentMenu.selectPlayerType(playerType, self.slot)