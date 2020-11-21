# evolutional behaviors (called from game contollers)

from ai.generation import Generation

import numpy as np
import random
import copy

class Evolution (object):
    '''
    adds evolutional behaviors (called from game contollers) and stores last and new generation
        functions:
            - getFitness(self)
            - getWeights(self)
            - generatePopulation(self)
            - doMutation(self)
    '''

    def __init__ (self, mutationRate, **kwargs):
        super(Evolution, self).__init__(**kwargs)
        print("[evol] created " + str(self.__class__))

        self.mutationList = [True]
        for _ in range(mutationRate):
            self.mutationList.append(False)

        self.lastGeneration = Generation()
        self.newGeneration = Generation()


    def getFitness(self, fitnesses):
        print("stored fitness for " + str(len(fitnesses)) + " snakes")

        self.lastGeneration.fitnesses.clear()
        self.lastGeneration.fitnesses = fitnesses


    def getWeights(self, weights):
        print("stored weights for " + str(len(weights)) + " snakes")

        self.lastGeneration.weights.clear()
        self.lastGeneration.weights = weights


    def generatePopulation(self, size):

        # calculate probability of each snake
        self.probability = np.divide(self.lastGeneration.fitnesses, sum(self.lastGeneration.fitnesses) + 0.000000001)
        self.probability = np.multiply(self.probability, 100)
        # for i,p in enumerate(self.probability):
        #     print(str(self.lastGeneration.fitnesses[i]) + " => " + str(p))


        # generate weights of new generation

        self.newGeneration.weights.clear()
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
                copy.deepcopy(self.lastGeneration.weights[s])
            )



    def doMutation(self):
        print("mutating...")

        weightLayers = len(self.newGeneration.weights)

        self.tempNewWeights = []

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

                        changeWeight = random.choice(self.mutationList)
                        # changeWeight = True
                        if changeWeight:
                            r = random.randint(-100, 100)
                            r = r / 100
                            newValue = value + r


                            # if k < 2:
                            #     print("-----")
                            #     print(self.newGeneration.weights[i][j][k,l])
                            self.newGeneration.weights[i][j][k,l] = newValue
                                # print(self.newGeneration.weights[i][j][k,l])

                            # print(str(i) + "|" + str(j) + "|" + str(k) + "|" + str(l) + ": " + str(value) + " -> " + str(r) + " => " + str(newValue))

            # print(str(i))
            # print(str(self.newGeneration.weights[i][0][0,0]))

            self.tempNewWeights.append(self.newGeneration.weights[i])

        # for i,snake in enumerate(self.tempNewWeights):
        #     for j,layer in enumerate(snake):
        #         for k,pre in enumerate(layer):
        #             for l,value in enumerate(pre):
        #                 if k < 2:
        #                     print(str(i) + "|" + str(j) + "|" + str(k) + "|" + str(l) + " => " + str(snake[j][k,l]))
        print("mutation done")



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

    def doRecombination():
        pass




    # -15.125783906293101 -> -0.77 => -15.8957839062931
    # -8.153571347657783 -> 0.84 => -7.313571347657783
    # -8.023571347657782 -> -0.13 => -8.153571347657783