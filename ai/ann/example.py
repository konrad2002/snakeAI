# example code for a neural network

import numpy as np

class AiAnnExample (object):
    def __init__ (self, nInputNeurons = 1, nHiddenNeurons = (1, 1), nOutputNeurons = 1, activationF = "heaviside", outputF = "id"):
        print("[ai  ] created " + str(self.__class__))

        self.nInputNeurons = nInputNeurons
        self.nHiddenNeurons = nHiddenNeurons
        self.nOutputNeurons = nOutputNeurons

        self.activationF = activationF
        self.outputF = outputF


        self.network = []

        self.inputNeurons = np.zeros(self.nInputNeurons)
        self.hiddenNeurons = np.zeros(self.nHiddenNeurons)
        self.outputNeurons = np.zeros(self.nOutputNeurons)


        self.network.append(self.inputNeurons)
        self.network.append(self.hiddenNeurons)
        self.network.append(self.outputNeurons)



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
