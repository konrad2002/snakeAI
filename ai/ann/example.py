# example code for a neural network

import numpy as np

class AiAnnExample (object):
    def __init__ (self, nNeurons = [1, 1, 1], weights = None, activationF = "heaviside", outputF = "id"):
        print("[ai  ] created " + str(self.__class__))

        self.nNeurons = nNeurons

        self.activationF = activationF
        self.outputF = outputF


        self.network = []
        self.layers = []
        self.weights = []

        for layer,neurons in enumerate(self.nNeurons):

            # init neurons of layer with 0
            self.layers.append(
                np.zeros((neurons, 5))
            )


            if weights:
                self.weights.append(weights[layer])
            else:
                # init weights between layer and next layer with 0
                if layer < ( len(self.nNeurons) - 1 ):
                    self.weights.append(
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

        self.layers[0][:,2] = x

        for i,layer in enumerate(self.layers):
            if i > 0:
                layer[i][:,0] = np.dot(self.layers[i - 1][:,2], self.weights[i - 1])

                layer[i][:,1] = self.function(self.activationF, layer[i][:,0])

                layer[i][:,2] = self.function(self.outputF, layer[i][:,1])
            
        output = layer[len(self.nNeurons) - 1][:,2]

        return output


    def direction(self):

        x = [0, 1]

        output = self.predict(x)
        newDirection = output.index(max(output))

        return newDirection


    def printNetwork(self):


        print(self.layers)
        print(self.weights)



ai = AiAnnExample([2, 2, 4])
ai.printNetwork()

x = [0, 1]
ai.predict(x)