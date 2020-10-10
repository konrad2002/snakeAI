# vis ann

import numpy as np

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

class AiVisualisation (Widget):
    def __init__ (self, screenX, screenY, ann, **kwargs):
        super(AiVisualisation, self).__init__(**kwargs)
        print("[ai  ] created " + str(self.__class__))

        self.screenX = screenX
        self.screenY = screenY

        self.ann = ann

        self.draw()


    # create neurons and weights
    def draw(self):

        with self.canvas:
            self.canvas.clear()
            Color(0,0,0,1)

            self.bg = Rectangle(pos=(0, 0), size=(self.screenX, self.screenY))

            self.closeBtn = Button(
                text = "Schließen",
                pos = (self.screenX - 100, self.screenY - 50),
                size = (100, 50),
                on_release = self.onClose
            )

            self.updateBtn = Button(
                text = "Update",
                pos = (self.screenX - 210, self.screenY - 50),
                size = (100, 50),
                on_release = self.update
            )

            self.add_widget(self.closeBtn)
            self.add_widget(self.updateBtn)

            Color(1,1,1,1)

            self.layers = []
            self.labels = []

            for i,layer in enumerate(self.ann.layers):

                neurons = []
                neuronValues = []
                for j,neuron in enumerate(layer):

                    brightness = 0.9
                    neurons.append(brightness)

                    neuronValues.append(
                        Label(
                            pos=(
                                i * 400 + 30,
                                j * 50 + 40
                            ),
                            text=str(neuron[0])
                        )
                    )


                self.layers.append(neurons)
                self.labels.append(neuronValues)



            for i,layer in enumerate(self.ann.layers):
                for j,neuron in enumerate(layer):

                    if j == 0:
                        Color(1,0,0,1)
                    else:
                        Color(1,1,1,self.layers[i][j])

                    Ellipse(
                        pos=(i * 400 + 50, j * 50 + 50),
                        size=(30, 30)
                    )


            Color(1,1,1,1)
            self.weights = []
            for i,layer in enumerate(self.ann.weights):

                weight = []
                for j,pre in enumerate(layer):

                    neuron = []
                    for k,_ in enumerate(pre):

                        neuron.append(
                            Line(
                                points=[
                                    i * 400 + 50 + 30,
                                    j * 50 + 50 + 15,
                                    i * 400 + 50 + 400,
                                    k * 50 + 50 + 15
                                ],
                                width = 5
                            )
                        )

                    weight.append(neuron)

                self.weights.append(weight)


    # update colors and strength
    def update(self, a = None):
        print("update ai vis")

        for i,layer in enumerate(self.ann.layers):
            for j,neuron in enumerate(layer):
                value = round(neuron[2], 3)
                self.labels[i][j].text = str(value)

                self.layers[i][j] = (round(neuron[2], 3)) / 32

        for i,layer in enumerate(self.ann.weights):
            for j,pre in enumerate(layer):
                for k,last in enumerate(pre):
                    self.weights[i][j][k].width = last * 3


    def onClose(self, a):
        self.parent.aiVisActive = False
        self.parent.remove_widget(self.parent.aiVis)