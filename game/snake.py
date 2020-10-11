# snake class (1 to 1000+)

from game.tile import GameTile

from ai.ann.example import AiAnnExample
from ai.rand import RandomDirection
from ai.algorithm import AlgorithmDirection

class Snake (object):
    def __init__ (self, startSize, foods, gameType):

        self.body = []
        self.foods = foods
        self.gameType = gameType

        self.startSize = startSize

        for i in range(self.startSize):
            tile = GameTile(
                8 - i,
                8
            )
            self.body.append(tile)

        self.direction = 1
        self.newDirection = 1

        self.steps = 0
        
        self.death = False

        self.hasEaten = False

        self.ai = None
        self.aiSensor = None

        # set ann
        if self.gameType == 3 or self.gameType == 4:
            self.ai = AiAnnExample([12, 8, 4], None, ["sigmoid", "sigmoid"], ["id", "id"])

        if self.gameType == 5:
            self.ai = RandomDirection()
        elif self.gameType == 6:
            self.ai = AlgorithmDirection()

    def eat(self):
        newTile = GameTile(
            self.body[len(self.body) - 1].x,
            self.body[len(self.body) - 1].y
        )
        self.body.append(newTile)
        self.hasEaten = True

    def die(self):
        self.death = True