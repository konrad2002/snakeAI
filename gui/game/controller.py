# main game controller, used 1 - 2 times

from ai.rand import RandomDirection
from ai.algorithm import AlgorithmDirection
from ai.ann.example import AiAnnExample
from ai.vis import AiVisualisation

from game.data import Data
from game.tile import GameTile
from game.snake import Snake
from game.aiSensor import AiSensor

from gui.game.map import GameMap
from gui.game.infobar import InfoBar

from gui.game.playerButtons import PlayerButtons
from gui.game.aiButtons import AiButtons

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout

import random


class GameController (RelativeLayout):
    def __init__ (self, mainController, instance = 1, **kwargs):
        super(GameController, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.main = mainController

        self.instance = instance

        self.data = Data()

        self.type = self.main.settings.playerTypes[self.instance - 1]

        # get best from database
        self.bestQuery = "SELECT highscore FROM highscores WHERE playerType = " + str(self.type)


        self.x = 0 # smallest coord of game on window
        if self.instance % 2 == 0:
            self.x = ( self.main.settings.screenX / 2 )

        self.y = 0 # smallest coord of game on window
        if self.main.settings.playerMode == 4:
            if self.instance <= 2:
                self.y = ( self.main.settings.screenY - 60 ) / 2

        self.sizeX = self.main.settings.screenX
        if self.main.settings.playerMode != 1:
            self.sizeX = self.main.settings.screenX / 2

        self.sizeY = self.main.settings.screenY - 60
        if self.main.settings.playerMode == 4:
            self.sizeY = ( self.main.settings.screenY - 60 ) / 2

        print()
        print("=== GameController - " + str(self.instance) + " ===")
        print("--- Pos --")
        print("x: " + str(self.x))
        print("y: " + str(self.y))
        print()
        print("--- Size --")
        print("x: " + str(self.sizeX))
        print("y: " + str(self.sizeY))

        self.pos = (self.x, self.y)
        self.size = (self.sizeX, self.sizeY)

        self.aiVisActive = False


        self.drawBorder()
        self.showMap()
        self.showInfoBar()

        self.showButtons()

        self.prepare()

    def drawBorder(self):
        with self.canvas:
            self.canvas.clear()
            # border and box
            Color(.1,.2,.7,1)
            self.border = Rectangle(pos=(0,0), size=(self.sizeX, self.sizeY))
            Color(0,0,0,1)
            self.box = Rectangle(pos=(2, 2), size=(self.sizeX - 4, self.sizeY - 4))

    def showMap(self):
        if self.main.gameApp.layoutType == 1:
            self.mapX = self.sizeX / 3 * 2
        else:
            self.mapX = self.sizeX

        self.mapY = self.mapX / 32 * 24 - 4
        self.mapX = self.mapX - 4

        self.map = GameMap(self, self.mapX, self.mapY)
        self.map.pos = (
            2,
            self.sizeY - self.mapY - 2 - ( self.sizeY / 15 )
        )
        self.add_widget(self.map)

    def showInfoBar(self):
        self.infoBar = InfoBar(
            size = (
                self.sizeX,
                self.sizeY / 15
            ),
            pos = (
                0,
                self.sizeY - ( self.sizeY / 15 )
            )
        )

        self.add_widget(self.infoBar)

    def showButtons(self):

        if self.main.settings.playerMode == 2:
            btnX = 0
            btnY = self.sizeY / 15
            
            btnSizeX = self.sizeX
            btnSizeY = self.sizeY - self.sizeY / 15 * 2 - self.mapY - 4

        else:
            btnX = self.sizeX / 3 * 2
            btnY = self.sizeY - self.mapY - 2 - ( self.sizeY / 15 )


            btnSizeX = self.sizeX / 3
            btnSizeY = self.mapY
            
        
        if self.type <= 2:
            self.buttons = PlayerButtons(self)
        else:
            self.buttons = AiButtons(self)

        self.buttons.pos = (btnX, btnY)
        self.buttons.size = (btnSizeX, btnSizeY)

        self.buttons.drawBackground()

        self.add_widget(self.buttons)

    def setKeyboard(self, keyboardType):
        self.data.keyboardType = keyboardType


    # called every time the game restarts
    def prepare(self):
        # get best score
        self.main.gameApp.cursor.execute(self.bestQuery)
        rows = self.main.gameApp.cursor.fetchall()

        for row in rows:
            self.data.best = row[0]

        # create foods
        self.data.foods.clear()
        for _ in range(768):
            x = random.randint(0, 31)
            y = random.randint(0, 23)

            newFood = GameTile(x, y)

            self.data.foods.append(newFood)

        # create snake(s)
        self.data.population = self.data.tempPopulation

        self.data.snakes.clear()
        for _ in range(self.data.population):
            snake = Snake(self.data.startSize, self.data.foods, self.type)

            if self.type % 2 == 0:
                snake.aiSensor = AiSensor(snake, 1)
            else:
                snake.aiSensor = AiSensor(snake, 2)


            self.data.snakes.append(snake)

        self.data.displayedSnake = self.data.snakes[0]

        self.data.state = 1
        self.data.dead = 0

        self.map.prepare()

        self.update()

    def ready(self):
        print("[" + str(self.instance) + "] ready")
        self.prepare()
        self.data.ready = True
        self.data.state = 2
        self.buttons.readyBtn.color = (0,1,0,1)
        self.alive = True
        self.main.gameApp.checkReady()

    def start(self):
        self.data.running = True
        self.data.ready = False
        self.data.state = 3
        self.data.generation += 1
        self.buttons.readyBtn.color = (1,1,1,1)

    def update(self):

        self.infoBar.lbl1.text = str(self.main.settings.typeNames[self.type - 1])
        self.infoBar.lbl2.text = "Beste: " + str(self.data.best)
        self.infoBar.lbl3.text = "Highscore: " + str(self.data.highscore)
        if (self.data.state >= 1):
            self.infoBar.lbl4.text = "Länge: " + str(len(self.data.displayedSnake.body))
            self.infoBar.lbl6.text = "Alive: " + str(self.data.population - self.data.dead) + " / " + str(self.data.population)
        
        if self.type <= 2 or self.type >= 5:
            txt = "Runde"
        else:
            txt = "Generation"
        self.infoBar.lbl5.text = txt + ": " + str(self.data.generation)

        if self.data.running and self.data.state < 4 and self.data.state > 2:
            self.move()
            self.map.update()
            if self.aiVisActive:
                self.aiVis.update()

    def move(self):

        alive = False
        dead = 0
        for snake in self.data.snakes:
            if snake.death == False:

                if snake.ai:
                    snake.newDirection = snake.ai.direction(snake.aiSensor.data)

                alive = True
                lastTile = snake.body[len(snake.body) - 1]
                snake.body.insert(0, lastTile)
                snake.body.pop(len(snake.body) - 1)

                snake.body[0].x = snake.body[1].x
                snake.body[0].y = snake.body[1].y
            
                if not ( (snake.direction + 1 ) % 2 == ( snake.newDirection + 1 ) % 2 ):
                    snake.direction = snake.newDirection

                if snake.direction == 0:
                    snake.body[0].y += 1
                if snake.direction == 1:
                    snake.body[0].x += 1
                if snake.direction == 2:
                    snake.body[0].y += -1
                if snake.direction == 3:
                    snake.body[0].x += -1

                
                # if in food
                if snake.body[0].x == self.data.foods[len(snake.body)].x and snake.body[0].y == self.data.foods[len(snake.body)].y:
                    snake.eat()

                # if in wall
                if (
                    snake.body[0].x < 0 or
                    snake.body[0].x > 31 or
                    snake.body[0].y < 0 or
                    snake.body[0].y > 23
                ):
                    snake.body[0].x = snake.body[1].x
                    snake.body[0].y = snake.body[1].y
                    snake.die()

                for i,tile in enumerate(snake.body):
                    if i > 0:
                        if snake.body[0].x == tile.x and snake.body[0].y == tile.y:
                            snake.die()


                if snake.death == False:

                    snake.aiSensor.update()

            else:
                dead += 1
        self.alive = alive
        self.data.dead = dead


        if not self.alive:
            self.data.running = False
            self.data.state = 4
            self.buttons.readyBtn.color = (1,0.4,0.4,1)
            
            highscore = 0
            for snake in self.data.snakes:
                if len(snake.body) > highscore:
                    highscore = len(snake.body)

            if self.data.highscore < highscore:
                self.data.highscore = highscore

            if self.data.best < highscore:
                self.data.best = highscore
                query = "UPDATE highscores SET highscore = " + str(highscore) + " WHERE playerType = " + str(self.type)
                self.main.gameApp.cursor.execute(query)
                self.main.gameApp.db.commit()

            print("[" + str(self.instance) + "] died with score of " + str(highscore))

            if self.type > 2:
                self.ready()

    def showSnake(self, mode = ""):
        newSnake = 0

        if mode == "":
            for i,snake in enumerate(self.data.snakes):
                if not snake.death:
                    newSnake = i
                    break

        elif mode == "random":
            alive = []
            for i,snake in enumerate(self.data.snakes):
                if not snake.death:
                    alive.append(i)

            newSnake = random.choice(alive)

        self.data.displayedSnake = self.data.snakes[newSnake]


    def showAiVis(self):

        self.aiVis = AiVisualisation(self.main.settings.screenX, self.main.settings.screenY, self.ai)

        self.aiVisActive = True

        self.add_widget(self.aiVis)