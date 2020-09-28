# class that stores the input data of the ai

class AiSensor (object):
    def __init__(self, snake, sensorType):
        print("[game] created " + str(self.__class__))

        self.data = []

        self.snake = snake
        self.sensorType = sensorType

        if self.sensorType == 1:
            self.data.append([1, 1, 1, 1]) # wall (top, right, bottom, left)
            self.data.append([1, 1, 1, 1]) # food (top, right, bottom, left)
            self.data.append([1, 1, 1, 1]) # body (top, right, bottom, left)


        elif self.sensorType == 2:
            self.data.append([1, 1]) # head (x, y)
            self.data.append([1, 1]) # food (x, y)
            self.data.append([])     # history
            
            for _ in range(768):
                self.data[2].append([1, 1]) # for each step koords of head
                

    def update(self):
        if self.sensorType == 1:

            self.data[0][0] = 24 - self.snake.body[0].y
            self.data[0][1] = 32 - self.snake.body[0].x
            self.data[0][2] = self.snake.body[0].y
            self.data[0][3] = self.snake.body[0].x

            print(self.data[0])