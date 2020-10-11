# class with all stored values of one snake game

class Data (object):
    def __init__(self):
        self.speed = 1
        self.ready = False
        self.pause = False
        self.running = False

        self.turn = 0
        
        self.keyboardType = 0

        self.state = 0

        self.highscore = 0
        self.best = 0

        # KNN (Perceptron) settings
        self.epochs = 1
        self.batch = 1
        self.iterations = 1
        self.eta = 0.1

        # Evolutional Algorithm settings
        self.doEvolution = False

        self.generation = 0
        self.population = 1

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

        self.startSize = 3

        self.aiSensor = []
        self.sensorType = 0