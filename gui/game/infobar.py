# info bar at top of each game

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line


class InfoBar (RelativeLayout):
    def __init__ (self, **kwargs):
        super(InfoBar, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        with self.canvas:
            self.canvas.clear()

            Color(.1, .2, .7, .5)
            self.bg = Rectangle(pos=(0, 0), size=(self.size[0], self.size[1]))

            self.margin = self.size[0] / 7

            Color(1,1,1,1)

            self.lbl1 = Label(
                text = "Typ: ",
                center = (1 * self.margin, self.size[1] / 2),
                bold = True
            )

            self.lbl2 = Label(
                text = "Hs. (immer): ",
                center = (2 * self.margin, self.size[1] / 2),
                bold = True
            )

            self.lbl3 = Label(
                text = "Highscore: ",
                center = (3 * self.margin, self.size[1] / 2),
                bold = True
            )

            self.lbl4 = Label(
                text = "Länge: ",
                center = (4 * self.margin, self.size[1] / 2),
                bold = True
            )

            self.lbl5 = Label(
                text = "Runde/Generation: ",
                center = (5 * self.margin, self.size[1] / 2),
                bold = True
            )

            self.lbl6 = Label(
                text = "Alive: ",
                center = (6 * self.margin, self.size[1] / 2),
                bold = True
            )