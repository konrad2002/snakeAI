# example code for a neural network

import numpy as np

class AiAnnExample (object):
    def __init__ (self, nNeurons = [1, 1, 1], weights = None, activationF = "heaviside", outputF = "id"):
        print("[ai  ] created " + str(self.__class__))

        self.nNeurons = nNeurons

        self.activationF = activationF
        self.outputF = outputF


        self.network = []

        for layer,neurons in enumerate(self.nNeurons):

            # init neurons of layer with 0
            self.network.append(
                np.zeros((neurons, 5))
            )


            if weights:
                self.network.append(weights[layer])
            else:
                # init weights between layer and next layer with 0
                if layer < ( len(self.nNeurons) - 1 ):
                    self.network.append(
                        np.zeros((self.nNeurons[layer + 1], neurons))
                    )

    def function(self, fType, x):

        # used for activation functions and output functions

        y = 0

        if not fType:
            fType = "heaviside"

        if fType == "heaviside":
            if x > 0:
                y = 1
            else:
                y = 0

        elif fType == "sigmoid":
            y = 1 / ( 1 + np.exp(-x) )

        elif fType == "relu":
            y = np.maximum(0, x)

        elif fType == "id":
            y = x


        return y


    def predict(self, x):

        output = [0, 0, 1, 0]

        return output


    def direction(self):

        x = [0]

        output = self.predict(x)
        newDirection = output.index(max(output))

        return newDirection


    def printNetwork(self):
        print(self.network)



ai = AiAnnExample([2, 2, 1])
ai.printNetwork()