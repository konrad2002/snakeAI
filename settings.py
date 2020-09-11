# main settings and states

class Settings (object):
    def __init__ (self):
        print("[game] created " + str(self.__class__))

        self.configurated = False

        self.screenX = 1440
        self.screenY = 800

        self.typeNames = ["Spieler normal", "Spieler Snake", "KNN normal", "KNN Snake", "Zufall", "Algorithmus"]

        self.playerMode = 0
        self.playerTypes = [0, 0]

        self.cols = 1
        self.rows = 1

        self.gameStarted = False

        self.close = False

        self.speed = 0.1