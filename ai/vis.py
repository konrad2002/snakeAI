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

            self.add_widget(self.closeBtn)

            Color(1,1,1,1)

            self.layers = []

            for i,layer in enumerate(self.ann.layers):

                neurons = []
                for j,neuron in enumerate(layer):
                    if j == 0:
                        Color(1,0,0,1)
                    else:
                        Color(1,1,1,1)

                    neurons.append(Ellipse(pos=(i * 400 + 50, j * 50 + 50), size=(30, 30)))

                self.layers.append(neurons)

                Color(1,1,1,1)
                self.weights = []
                for i,layer in enumerate(self.ann.weights):
                    
                    weight = []
                    for j,pre in enumerate(layer):

                        neuron = []
                        for k,last in enumerate(pre):
                            
                            Line(points=[i * 400 + 50 + 30, j * 50 + 50 + 15, i * 400 + 50 + 400, k * 50 + 50 + 15])
                        
                        weight.append(neuron)

                    self.weights.append(weight)


    # update colors and strength
    def update(self):
        print("update ai vis")


    def onClose(self, a):
        self.parent.remove_widget(self.parent.aiVis)