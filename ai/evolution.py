# evolutional behaviors (called from game contollers)

from ai.generation import Generation

import numpy as np
import random

class Evolution (object):
    '''
    adds evolutional behaviors (called from game contollers) and stores last and new generation
        functions:
            - getFitness(self)
            - getWeights(self)
            - generatePopulation(self)
            - doMutation(self)
    '''

    def __init__ (self, **kwargs):
        super(Evolution, self).__init__(**kwargs)
        print("[evol] created " + str(self.__class__))


        self.lastGeneration = Generation()
        self.newGeneration = Generation()


    def getFitness(self, fitnesses):
        print("stored fitness for " + str(len(fitnesses)) + " snakes")

        self.lastGeneration.fitnesses = fitnesses


    def getWeights(self, weights):
        print("stored weights for " + str(len(weights)) + " snakes")

        self.lastGeneration.weights = weights


    def generatePopulation(self, size):

        # calculate probability of each snake
        self.probability = np.divide(self.lastGeneration.fitnesses, sum(self.lastGeneration.fitnesses) + 0.000000001)
        self.probability = np.multiply(self.probability, 100)
        # for i,p in enumerate(self.probability):
        #     print(str(self.lastGeneration.fitnesses[i]) + " => " + str(p))


        # generate weights of new generation

        self.newGeneration.weights = []
        for i in range(size):

            if i % 100 == 0:
                print(
                    "reproduction progress: " +
                    str(
                        round(
                            i / size,
                            3
                        ) * 100
                    )
                    + "%"
                )

            s = self.randomByValue(self.probability)

            self.newGeneration.weights.append(
                self.lastGeneration.weights[s]
            )



    def doMutation(self):
        print("mutating...")

        reproduction = [True, False, False, False]

        weightLayers = len(self.newGeneration.weights)

        for i,snake in enumerate(self.newGeneration.weights):
            
            if i % 100 == 0:
                print(
                    "mutation progress: " + 
                    str(
                        round( #  (  current layer  )   (all layers) 
                            ( i / weightLayers ) * 100,
                            3
                        )
                    ) 
                    + "%"
                )

            for j,layer in enumerate(snake):

                for k,pre in enumerate(layer):
                    for l,value in enumerate(pre):

                        changeWeight = random.choice(reproduction)
                        if changeWeight:
                            r = random.randint(-2, 2)
                            r = r / 10
                            self.newGeneration.weights[i][j][k][l] = value + r




    def randomByValue(self, array):
        self.minimum = 0
        self.maximum = sum(array)

        self.randomIndex = 0

        if self.maximum > 0:
            self.r = random.randint(self.minimum, round(self.maximum))

            b = 0
            for i,a in enumerate(array):
                if self.r > b and self.r <= ( a + b ):
                    self.randomIndex = i
                    b += a
                else:
                    b += a
        else:
            self.randomIndex = random.randint(0, len(array) - 1)

        return self.randomIndex