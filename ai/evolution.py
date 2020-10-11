# evolutional behaviors (called from game contollers)

class Evolution (object):
    def __init__ (self, **kwargs):
        super(Evolution, self).__init__(**kwargs)
        print("[evol] created " + str(self.__class__))



    def getFitness(self):
        print("getFitness")


    def getWeights(self):
        print("getWeights")


    def generatePopulation(self):
        print("generatePopulation")


    def doMutation(self):
        print("doMutation")

