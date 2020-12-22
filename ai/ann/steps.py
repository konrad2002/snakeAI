# steps for special situations

class Steps (object):
    def __init__(self):
        self.X = []
        self.Y = []

        for i in range(4):
            
            for a in range(32):
                for b in range(24):
                    for c in range(32):
                        for d in range(24):

                            x1 = [a, b, c, d]

                            if i == 0:
                                x2 = [1, 0, 0, 0]
                                y = 0

                            if i == 1:
                                x2 = [0, 1, 0, 0]
                                y = 1

                            if i == 2:
                                x2 = [0, 0, 1, 0]
                                y = 2

                            if i == 3:
                                x2 = [0, 0, 0, 1]
                                y = 3

                            self.X.append([x1, x2, [0, 0, 0, 0]])
                            self.Y.append(y)


    def printSteps(self):
        print("X:")
        print(self.X)
        print("")
        print("Y:")
        print(self.Y)


steps = Steps()
steps.printSteps()