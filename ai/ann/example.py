# example code for a neural network

import numpy as np
from sklearn.utils.validation import check_random_state

class AiAnnExample (object):
    def __init__ (self, nNeurons = [1, 1, 1], weights = None, activationF = "heaviside", outputF = "id"):
        print("[ai  ] created " + str(self.__class__))

        self.nNeurons = nNeurons

        self.activationF = activationF
        self.outputF = outputF


        self.random_state_ = check_random_state(41)


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
                        self.random_state_.random_sample((neurons, self.nNeurons[layer + 1]))
                    )

    def function(self, fType, x):

        # used for activation functions and output functions

        y = []

        if not fType:
            fType = "heaviside"

        if fType == "heaviside":
            for X in x:
                if X > 0:
                    y.append(1)
                else:
                    y.append(0)

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
                print(i)
                layer[:,0] = np.dot(self.layers[i - 1][:,2], self.weights[i - 1])

                layer[:,1] = self.function(self.activationF, layer[:,0])

                layer[:,2] = self.function(self.outputF, layer[:,1])
            
        output = self.layers[len(self.nNeurons) - 1][:,2]

        return output


    def direction(self, sensorData):

        x = []

        for data in sensorData:
            for subdata in data:
                x.append(subdata)

        print(x)

        output = self.predict(x)
        newDirection = output.index(max(output))

        return newDirection


    def printNetwork(self):

        for i,layer in enumerate(self.layers):
            print("[Layer  " + str(i) + "]: ")
            print(layer)

            if i < ( len(self.weights) ):
                print("[Weight " + str(i) + "]: ")
                print(self.weights[i])


        for i,layer in enumerate(self.layers):

            row = ""
            ro2 = ""
            for _ in range(self.nNeurons[i]):
                row += " O "
                ro2 += " | "

            print("")
            if i > 0:
                print(ro2)
            print(row)
            if i < ( len(self.weights) ):
                print(ro2)
            print("")

            if i < ( len(self.weights) ):
                print(" " + str(self.nNeurons[i]) + "x" + str(self.nNeurons[i + 1]) + " weights")



ai = AiAnnExample([12, 8, 4], None, "sigmoid")
ai.printNetwork()

x = [3,12,1,4,7,3,6,3,6,5,4,18]
output = ai.predict(x)

print("")
print("")
print("output:")
print(output)
print("")
print("")

ai.printNetwork()