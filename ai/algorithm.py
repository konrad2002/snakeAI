# simple hardcoded algorithm to find direction

class AlgorithmDirection (object):
    def __init__ (self):
        print("[game] created " + str(self.__class__))

        self.autoReady = True

    def direction(self):
        newDirection = 2
        return newDirection