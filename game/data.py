# class with all stored values of one snake game

import random

class Data (object):
    def __init__(self, snakeId):

        self.snakeId = snakeId

        if self.snakeId == None:
            self.snakeId = random.randint(100000, 999999)

        self.speed = 1
        self.ready = False
        self.pause = False
        self.running = False

        self.turn = 0
        
        self.keyboardType = 0

        self.state = 0

        # highscore of currently best snake
        self.highscore = 0
        # highscore of all snakes with these type
        self.best = 0

        self.showCovers = False

        # KNN (Perceptron) settings
        self.epochs = 1
        self.batch = 16
        self.iterations = 100
        self.eta = 1

        self.weights = []

        self.isTrained = False

        # Evolutional Algorithm settings
        self.doEvolution = False

        self.generation = 1
        self.population = 1

        self.mutationRate = 1
        self.reproductionRate = 2


        self.tempPopulation = 1

        self.dead = 0

        self.fitness = [
            [1000,0], # lenght 3
            [1000,0], # lenght 4
            [1000,0], # lenght 5
            [1000,0], # lenght 6
            [1000,0], # lenght 7
            [1000,0], # lenght 8
            [1000,0]  # lenght 9
        ]

        # snakes and settings
        self.snakes = []
        self.foods = []

        self.displayedSnake = None

        self.bestSnake = None
        self.worstSnake = None

        self.bestFitness = 0
        self.worstFitness = 100

        self.startSize = 3

        self.aiSensor = []
        self.sensorType = 0

        self.fitnesses = []
        self.scores = []

        self.fitnessMax = []
        self.fitnessMin = []
        self.fitnessAvarage = []

        self.scoreMax = []
        self.scoreMin = []
        self.scoreAvarage = []

    def setSettings (self, highscore, epochs, batch, iterations, eta, generation, population, startSize, fitnesses, scores):

        self.highscore = highscore
        self.epochs = epochs
        self.batch = batch
        self.iterations = iterations
        self.eta = eta
        self.generation = generation
        self.population = population
        self.startSize = startSize
        self.fitnesses = fitnesses
        self.scores = scores