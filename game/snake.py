# snake class (1 to 1000+)

from game.tile import GameTile

class Snake (object):
    def __init__ (self, startSize, foods):

        self.body = []
        self.foods = foods

        self.startSize = startSize

        for i in range(self.startSize):
            tile = GameTile(
                8 - i,
                8
            )
            self.body.append(tile)

        self.direction = 1
        self.newDirection = 1
        
        self.death = False

        self.hasEaten = False

        self.ai = None
        self.aiSensor = None

    def eat(self):
        newTile = GameTile(
            self.body[len(self.body) - 1].x,
            self.body[len(self.body) - 1].y
        )
        self.body.append(newTile)
        self.hasEaten = True

    def die(self):
        self.death = True