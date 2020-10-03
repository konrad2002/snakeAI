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
            self.data.append(self.snake.startSize) # length = init
            self.data.append([])     # history
                

    def update(self):

        # snake head view
        if self.sensorType == 1:

            # set wall distance
            self.data[0][0] = 24 - self.snake.body[0].y
            self.data[0][1] = 32 - self.snake.body[0].x
            self.data[0][2] = self.snake.body[0].y
            self.data[0][3] = self.snake.body[0].x


            # set food distance (if no food in row/col = 0), (only saved, if head in same row/col like food)
            self.data[1][0] = 0
            self.data[1][1] = 0
            self.data[1][2] = 0
            self.data[1][3] = 0

            diffX = self.snake.foods[len(self.snake.body)].y - self.snake.body[0].y
            diffY = self.snake.foods[len(self.snake.body)].x - self.snake.body[0].x

            if diffX == 0:
                if diffY > 0:
                    self.data[1][0] = diffY
                elif diffY < 0:
                    self.data[1][2] = diffY * ( -1 )

            elif diffY == 0:
                if diffX > 0:
                    self.data[1][1] = diffX
                elif diffX < 0:
                    self.data[1][3] = diffX * ( -1 )
                

            # set distance to own body (closest, nothing = 0)
            self.data[2][0] = 100
            self.data[2][1] = 100
            self.data[2][2] = 100
            self.data[2][3] = 100

            for i,tile in enumerate(self.snake.body):
                diffX = 0
                diffY = 0
                if i > 0:

                    if tile.x == self.snake.body[0].x:
                        diffY = tile.y - self.snake.body[0].y

                        if self.data[2][0] > diffY and diffY > 0:
                            self.data[2][0] = diffY
                        if self.data[2][2] > diffY * ( -1 ) and diffY < 0:
                            self.data[2][2] = diffY * ( -1 )

                    if tile.y == self.snake.body[0].y:
                        diffX = tile.x - self.snake.body[0].x

                        if self.data[2][1] > diffX and diffX > 0:
                            self.data[2][1] = diffX
                        if self.data[2][3] > diffX * ( -1 ) and diffX < 0:
                            self.data[2][3] = diffX * ( -1 )

            for i,value in enumerate(self.data[2]):
                if value == 100:
                    self.data[2][i] = 0


        elif self.sensorType == 2:

            # coords head
            self.data[0][0] = self.snake.body[0].x
            self.data[0][1] = self.snake.body[0].y

            # coords food
            self.data[1][0] = self.snake.foods[len(self.snake.body)].x
            self.data[1][1] = self.snake.foods[len(self.snake.body)].y

            # snake length
            self.data[2] = len(self.snake.body)

            # body history (step one forward => set new head)
            self.data[3].insert(0, [
                self.snake.body[0].x,
                self.snake.body[0].y
            ])