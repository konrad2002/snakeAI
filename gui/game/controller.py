# main game controller, used 1 - 2 times

from ai.rand import RandomDirection
from ai.algorithm import AlgorithmDirection
from ai.ann.example import AiAnnExample

from ai.vis import AiVisualisation
from ai.evolution import Evolution

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
    def __init__ (self, mainController, instance = 1, snakeId = None, **kwargs):
        super(GameController, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.main = mainController

        self.instance = instance

        self.data = Data(snakeId)

        self.type = self.main.settings.playerTypes[self.instance - 1]

        # get best from database
        self.bestQuery = "SELECT highscore FROM highscores WHERE player_type = " + str(self.type)


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

        # init evolutional behavior object
        self.evolution = None
        if self.type == 3 or self.type == 4:
            self.evolution = Evolution()


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


        if self.data.turn > 1 and self.evolution:
            self.evolution.generatePopulation(self.data.population)
            self.data.generation += 1
            self.evolution.doMutation()


        # create snake(s)
        self.data.population = self.data.tempPopulation

        self.data.snakes.clear()
        for i in range(self.data.population):

            newWeights = None
            if self.data.turn > 1 and self.evolution:
                newWeights = self.evolution.newGeneration.weights[i]

            snake = Snake(self.data.startSize, self.data.foods, self.type, newWeights)

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
        self.data.turn += 1
        self.buttons.readyBtn.color = (1,1,1,1)

        if self.aiVisActive:
            self.aiVis.onClose()
            self.showAiVis()

    def update(self):

        self.infoBar.lbl1.text = str(self.main.settings.typeNames[self.type - 1])
        self.infoBar.lbl2.text = "Beste: " + str(self.data.best)
        self.infoBar.lbl3.text = "Highscore: " + str(self.data.highscore)
        if (self.data.state >= 1):
            self.infoBar.lbl4.text = "Länge: " + str(len(self.data.displayedSnake.body))
            # self.infoBar.lbl4.text = "Fitness: " + str(round(self.data.fitness, 3))
            self.infoBar.lbl6.text = "Alive: " + str(self.data.population - self.data.dead) + " / " + str(self.data.population)
        
        if self.type <= 2 or self.type >= 5:
            self.infoBar.lbl5.text = "Runde: " + str(self.data.turn)
        else:
            self.infoBar.lbl5.text = "Generation: " + str(self.data.generation) + "/" + str(self.data.turn)

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

                snake.aiSensor.update()

                snake.steps += 1

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

                # if to long without eating (to prevent infinity)

                if ( snake.steps / ( len(snake.body) - self.data.startSize + 1 ) ) > 500:
                    snake.die()

                for i,tile in enumerate(snake.body):
                    if i > 0:
                        if snake.body[0].x == tile.x and snake.body[0].y == tile.y:
                            snake.die()


            else:
                dead += 1
        self.alive = alive
        self.data.dead = dead


        if not self.alive:
            self.allDeath()


    def allDeath(self):
        
            self.data.running = False
            self.data.state = 4
            self.buttons.readyBtn.color = (1,0.4,0.4,1)

            self.fitness = 0
            self.fitnesses = []
            self.weights = []
            self.scores = []

            self.data.bestSnake = None
            self.data.worstSnake = None

            self.data.bestFitness = 0
            self.data.worstFitness = 100

            highscore = 0
            lowscore = 100

            fitnessSum = 0
            scoreSum = 0


            # count highscore, collect weights and store fitnesses
            for snake in self.data.snakes:
                if len(snake.body) > highscore:
                    highscore = len(snake.body)

                if len(snake.body) < lowscore:
                    lowscore = len(snake.body)

                scoreAdd = (len(snake.body) - self.data.startSize)
                snake.fitness = (scoreAdd * 10000000 ) / ( snake.steps ) / 100000


                #sum up for avarage
                fitnessSum += snake.fitness
                scoreSum += len(snake.body)


                if snake.fitness > self.data.bestFitness:
                    self.data.bestSnake = snake
                    self.data.bestFitness = snake.fitness

                if snake.fitness < self.data.worstFitness:
                    self.data.worstSnake = snake
                    self.data.worstFitness = snake.fitness

                # snake.fitness = snake.steps

                # store for evolution
                if self.evolution:
                    self.fitnesses.append(snake.fitness)
                    self.scores.append(len(snake.body))
                    self.weights.append(snake.ai.weights)
                	
                # if snake.fitness < self.data.fitness[scoreAdd][0]:
                #     self.data.fitness[scoreAdd][0] = snake.fitness
                # if snake.fitness > self.data.fitness[scoreAdd][1]:
                #     self.data.fitness[scoreAdd][1] = snake.fitness

                if snake.fitness > self.fitness:
                    self.fitness = snake.fitness

            self.data.fitnessAvarage.append(fitnessSum / len(self.data.snakes))
            self.data.scoreAvarage.append(scoreSum / len(self.data.snakes))

            self.data.fitnessMax.append(self.data.bestFitness)
            self.data.fitnessMin.append(self.data.worstFitness)

            self.data.scoreMax.append(highscore)
            self.data.scoreMin.append(lowscore)
                

            if self.data.highscore < highscore:
                self.data.highscore = highscore

            if self.data.best < highscore:
                self.data.best = highscore
                query = "UPDATE highscores SET highscore = " + str(highscore) + " WHERE player_type = " + str(self.type)
                self.main.gameApp.cursor.execute(query)
                self.main.gameApp.db.commit()

            self.data.fitnesses.append(self.fitnesses)
            self.data.scores.append(self.scores)


            if self.data.turn > 2 and self.evolution:
                self.saveToDb()


            print("[" + str(self.instance) + "] highscore:  " + str(highscore))
            print("[" + str(self.instance) + "] lowscore:   " + str(lowscore))
            print("[" + str(self.instance) + "] fitness:    " + str(self.fitness))



            if self.evolution:
                self.evolution.getFitness(self.fitnesses)
                self.evolution.getWeights(self.weights)


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

        self.aiVis = AiVisualisation(self.main.settings.screenX, self.main.settings.screenY, self.data.displayedSnake.ai)

        self.aiVisActive = True

        self.add_widget(self.aiVis)

    def saveToDb(self):

        # check if snake is already in database
        query = "SELECT id FROM snakes WHERE snake_id = '" + str(self.data.snakeId) + "';"
        self.main.gameApp.cursor.execute(query)
        rows = self.main.gameApp.cursor.fetchall()


        db_id = 0
        for row in rows:
            db_id = row[0]


        if db_id == 0:

            query = "INSERT INTO `snakes` (snake_id, player_type, highscore, best_weights, best_fitness, worst_weights, worst_fitness, fitness_max, fitness_min, fitness_avarage, score_max, score_min, score_avarage, generations, population, iterations, eta, epochs, batch, start_size, fitness_function_id, activation_functions, output_functions) VALUES (" + str(self.data.snakeId) + ", " + str(self.type) + ", " + str(self.data.highscore) + ", \"" + str(self.data.bestSnake.weights) + "\", " + str(self.data.bestSnake.fitness) + ", \"" + str(self.data.worstSnake.weights) + "\", " + str(self.data.worstSnake.fitness) + ", \"" + str(self.data.fitnessMax) + "\", \"" + str(self.data.fitnessMin) + "\", \"" + str(self.data.fitnessAvarage) + "\", \"" + str(self.data.scoreMax) + "\", \"" + str(self.data.scoreMin) + "\", \"" + str(self.data.scoreAvarage) + "\", " + str(self.data.generation) + ", " + str(self.data.population) + ", " + str(self.data.iterations) + ", " + str(self.data.eta) + ", " + str(self.data.epochs) + ", " + str(self.data.batch) + ", " + str(self.data.startSize) + ", " + str(1) + ", \"" + str(self.data.snakes[0].ai.activationF) + "\", \"" + str(self.data.snakes[0].ai.outputF) + "\");"

        else:
            query = "UPDATE `snakes` SET player_type = " + str(self.type) + ", highscore = " + str(self.data.highscore) + ", best_weights = \"" + str(self.data.snakes[0].weights) + "\", best_fitness = " + str(self.data.snakes[0].fitness) + ", worst_weights = \"" + str(self.data.snakes[0].weights) + "\", worst_fitness = " + str(self.data.snakes[0].fitness) + ", fitness_max = \"" + str(self.data.fitnessMax) + "\", fitness_min = \"" + str(self.data.fitnessMin) + "\", fitness_avarage = \"" + str(self.data.fitnessAvarage) + "\", score_max = \"" + str(self.data.scoreMax) + "\", score_min = \"" + str(self.data.scoreMin) + "\", score_avarage = \"" + str(self.data.scoreAvarage) + "\", generations = " + str(self.data.generation) + ", population = " + str(self.data.population) + ", iterations = " + str(self.data.iterations) + ", eta = " + str(self.data.eta) + ", epochs = " + str(self.data.epochs) + ", batch = " + str(self.data.batch) + ", start_size = " + str(self.data.startSize) + ", fitness_function_id = " + str(1) + ", activation_functions = \"" + str(self.data.snakes[0].ai.activationF) + "\", output_functions = \"" + str(self.data.snakes[0].ai.outputF) + "\" WHERE snake_id = \"" + str(self.data.snakeId) + "\";"

        self.main.gameApp.cursor.execute(query)
        self.main.gameApp.db.commit()
