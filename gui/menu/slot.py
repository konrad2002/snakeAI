# menu which shows list of game modes and ai modes to select for a slot

from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SlotMenu (GridLayout):
    def __init__ (self, parentMenu, slotBtn, **kwargs):
        super(SlotMenu, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.parentMenu = parentMenu
        self.slotBtn = slotBtn

        self.cols = 3

        self.height = 220
        self.width = 400
        self.row_default_height = 110

        self.type1Btn = Button(text="Spieler normal", id="1", size=(120, 100), on_release=self.onSelectType)
        self.type4Btn = Button(text="Spieler Snake", id="2", size=(120, 100), on_release=self.onSelectType)
        self.type2Btn = Button(text="KNN normal", id="3", size=(120, 100), on_release=self.onSelectType)
        self.type5Btn = Button(text="KNN Snake", id="4", size=(120, 100), on_release=self.onSelectType)
        self.type3Btn = Button(text="Zufall", id="5", size=(120, 100), on_release=self.onSelectType)
        self.type6Btn = Button(text="Algorithmus", id="6", size=(120, 100), on_release=self.onSelectType)

        self.add_widget(self.type1Btn)
        self.add_widget(self.type2Btn)
        self.add_widget(self.type3Btn)
        self.add_widget(self.type4Btn)
        self.add_widget(self.type5Btn)
        self.add_widget(self.type6Btn)

    def onSelectType(self, a):
        print(str(a.id) + " was selected")
        self.parentMenu.selectPlayerType(a, self.slotBtn)