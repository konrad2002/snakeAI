# map where snake is shown

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

class GameMap (RelativeLayout):
    def __init__ (self, game, sizeX, sizeY, **kwargs):
        super(GameMap, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.game = game

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.pixel = self.sizeX / 32

        self.drawBackground()

    def drawBackground(self):
        with self.canvas:
            self.canvas.clear()
            
            Color(1,1,1,1)
            self.box = Rectangle(source='images/bg1.png', pos=(0, 0), size=(self.sizeX, self.sizeY))

    def prepare(self):
        with self.canvas:
            self.drawBackground()
            self.food = Ellipse(source='images/food4.png', pos=(0, 0), size=(self.pixel, self.pixel))

            self.body = []
            for tile in self.game.data.displayedSnake.body:
                bodyTile = Rectangle(source='images/body.png',pos=(self.pixel * tile.x, self.pixel * tile.y), size=(self.pixel, self.pixel))
                self.body.append(bodyTile)

            if self.game.type == 2 or self.game.type == 4:
                Color(0,0,0,1)
                self.hideBox1 = Rectangle(pos=(9 * self.pixel, 9 * self.pixel), size=(23 * self.pixel, 15 * self.pixel))
                self.hideBox2 = Rectangle(pos=(0, 9 * self.pixel), size=(8 * self.pixel, 15 * self.pixel))
                self.hideBox3 = Rectangle(pos=(0, 0), size=(8 * self.pixel, 8 * self.pixel))
                self.hideBox4 = Rectangle(pos=(9 * self.pixel, 0), size=(23 * self.pixel, 8 * self.pixel))
                Color(1,1,1,1)



    def update(self):
        with self.canvas:

            l = len(self.game.data.displayedSnake.body)

            for i,tile in enumerate(self.game.data.displayedSnake.body):
                if i > ( len(self.body) - 1 ):
                    bodyTile = Rectangle(source='images/body.png',pos=(self.pixel * tile.x, self.pixel * tile.y), size=(self.pixel, self.pixel))
                    self.body.append(bodyTile)

                self.body[i].pos = (
                    tile.x * self.pixel,
                    tile.y * self.pixel
                )

                if i > 0 and i < l-1:
                    # conditions for edges
                    coming = 0
                    if self.game.data.displayedSnake.body[i-1].x < self.game.data.displayedSnake.body[i].x:
                        coming = 3
                    if self.game.data.displayedSnake.body[i-1].x > self.game.data.displayedSnake.body[i].x:
                        coming = 1
                    if self.game.data.displayedSnake.body[i-1].y < self.game.data.displayedSnake.body[i].y:
                        coming = 2
                    if self.game.data.displayedSnake.body[i-1].y > self.game.data.displayedSnake.body[i].y:
                        coming = 0
                        
                    going = 2
                    if self.game.data.displayedSnake.body[i+1].x < self.game.data.displayedSnake.body[i].x:
                        going = 3
                    if self.game.data.displayedSnake.body[i+1].x > self.game.data.displayedSnake.body[i].x:
                        going = 1
                    if self.game.data.displayedSnake.body[i+1].y < self.game.data.displayedSnake.body[i].y:
                        going = 2
                    if self.game.data.displayedSnake.body[i+1].y > self.game.data.displayedSnake.body[i].y:
                        going = 0

                    self.body[i].source = "images/body" + str(coming) + "-" + str(going) + ".png"



            # source of head
            self.body[0].source = "images/head" + str(self.game.data.displayedSnake.direction) + ".png"

            # set tail image source
            if l > 2:
                if self.game.data.displayedSnake.hasEaten:
                    j = 1
                    self.body[l-2].source = "images/invisible.png"
                    self.game.data.displayedSnake.hasEaten = False
                else:
                    j = 0

                tail = 0
                if self.game.data.displayedSnake.body[l-2-j].x < self.game.data.displayedSnake.body[l-1].x:
                    tail = 1
                if self.game.data.displayedSnake.body[l-2-j].x > self.game.data.displayedSnake.body[l-1].x:
                    tail = 3
                if self.game.data.displayedSnake.body[l-2-j].y < self.game.data.displayedSnake.body[l-1].y:
                    tail = 0
                if self.game.data.displayedSnake.body[l-2-j].y > self.game.data.displayedSnake.body[l-1].y:
                    tail = 2
                self.body[l-1].source = "images/tail" + str(tail) + ".png"


            self.food.pos = (
                self.pixel * self.game.data.foods[len(self.game.data.displayedSnake.body)].x,
                self.pixel * self.game.data.foods[len(self.game.data.displayedSnake.body)].y
            )

            if self.game.type == 2 or self.game.type == 4:
                self.hideBox1.pos = (
                    ( self.game.data.displayedSnake.body[0].x + 1 ) * self.pixel,
                    ( self.game.data.displayedSnake.body[0].y + 1 ) * self.pixel
                )
                self.hideBox1.size = (
                    ( 31 - self.game.data.displayedSnake.body[0].x ) * self.pixel,
                    ( 23 - self.game.data.displayedSnake.body[0].y ) * self.pixel
                )
                
                self.hideBox2.pos = (
                    0,
                    ( self.game.data.displayedSnake.body[0].y + 1 ) * self.pixel
                )
                self.hideBox2.size = (
                    self.game.data.displayedSnake.body[0].x * self.pixel,
                    ( 23 - self.game.data.displayedSnake.body[0].y ) * self.pixel
                )

                self.hideBox3.pos = (
                    0,
                    0
                )
                self.hideBox3.size = (
                    self.game.data.displayedSnake.body[0].x * self.pixel,
                    self.game.data.displayedSnake.body[0].y * self.pixel
                )

                self.hideBox4.pos = (
                    ( self.game.data.displayedSnake.body[0].x + 1 ) * self.pixel,
                    0
                )
                self.hideBox4.size = (
                    ( 31 - self.game.data.displayedSnake.body[0].x ) * self.pixel,
                    self.game.data.displayedSnake.body[0].y * self.pixel
                )



            if self.game.data.displayedSnake.death:
                Color(0.5,0,0,0.3)
                self.deadRed = Rectangle(pos=(0, 0), size=(self.sizeX, self.sizeY))
                self.deathLbl = Label(
                    text = "Game Over",
                    pos = (0, 0),
                    size = (self.sizeX, self.sizeY),
                    font_size = str(self.sizeX / 10) + "sp"
                )