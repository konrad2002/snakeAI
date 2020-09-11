# small nav bar at top of screen

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class GuiNav (Widget):
    def __init__ (self, gameApp, **kwargs):
        super(GuiNav, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.gameApp = gameApp

        # setup keyboard controlle
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.menuBtn = Button(text="Menu", size=(100,40), pos=(10, self.gameApp.mainController.settings.screenY - 50), on_release=self.onShowMenu)

        self.higherSpeedBtn = Button(text="+", id="up", size=(40,40), pos=(120, self.gameApp.mainController.settings.screenY - 50), on_release=self.onChangeSpeed)
        self.speedLbl = Label(text=str(self.gameApp.mainController.settings.speed), size=(40,40), pos=(170, self.gameApp.mainController.settings.screenY - 50))
        self.lowerSpeedBtn = Button(text="-", id="down", size=(40,40), pos=(220, self.gameApp.mainController.settings.screenY - 50), on_release=self.onChangeSpeed)

        self.closeBtn = Button(text="Beenden", size=(100,40), pos=(self.gameApp.mainController.settings.screenX - 110, self.gameApp.mainController.settings.screenY - 50), on_release=self.onClose)

        self.add_widget(self.menuBtn)
        self.add_widget(self.higherSpeedBtn)
        self.add_widget(self.speedLbl)
        self.add_widget(self.lowerSpeedBtn)
        self.add_widget(self.closeBtn)

    def onShowMenu(self, a):
        self.gameApp.mainController.settings.configurated = False
        self.gameApp.mainController.stopGame()

    def onClose (self, a):
        self.gameApp.mainController.stop()

    def onChangeSpeed(self, a):
        if a.id == "up":
            self.gameApp.mainController.settings.speed *= 2
        elif a.id == "down":
            self.gameApp.mainController.settings.speed /= 2

        self.gameApp.modifyClock()

    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        direction = None
        if keycode[1] == 'up':
            self.changeDirection(0, 2)
        elif keycode[1] == 'right':
            self.changeDirection(1, 2)
        elif keycode[1] == 'down':
            self.changeDirection(2, 2)
        elif keycode[1] == 'left':
            self.changeDirection(3, 2)

        elif keycode[1] == 'w':
            self.changeDirection(0, 1)
        elif keycode[1] == 'd':
            self.changeDirection(1, 1)
        elif keycode[1] == 's':
            self.changeDirection(2, 1)
        elif keycode[1] == 'a':
            self.changeDirection(3, 1)

        elif keycode[1] == 'q':
            self.setReady(1)
        elif keycode[1] == 'numpad0':
            self.setReady(2)

        elif keycode[1] == 'spacebar':
            for game in self.gameApp.games:
                if game.data.running:
                    game.data.running = False
                else:
                    game.data.running = True

        return True

    def changeDirection(self, direction, keyboardType):
        if keyboardType:
            for game in self.gameApp.games:
                if game.data.keyboardType == keyboardType:
                    for snake in game.data.snakes:
                        snake.newDirection = direction
        else:
            for game in self.gameApp.games:
                for snake in game.data.snakes:
                    snake.newDirection = direction

    def setReady(self, keyboardType):
        if keyboardType:
            for game in self.gameApp.games:
                if game.data.keyboardType == keyboardType:
                    game.ready()