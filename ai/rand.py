# algorithm for random choosen direction

import random

class RandomDirection (object):
    def __init__ (self):
        print("[game] created " + str(self.__class__))

        self.autoReady = True

    def direction(self):
        newDirection = random.randint(0, 3)
        return newDirection