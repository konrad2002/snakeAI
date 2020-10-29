# check if object given to a function of a other object is a copy or a reference

import numpy as np

test = ["test1", "test2", "test3"]

print(test)

test.append("test4")

print(test)

test.pop(1)

print(test)

test.insert(0, "test0")

print(test)

class Main (object):
    def __init__ (self):
        self.test = "Johann"
        print(self.test)
        self.data = np.ones((10, 5))

        self.data[1,1] = 5
        self.data[1,3] = 5
        self.data[2,0] = 5
        self.data[4,2] = 5
        self.data[8,3] = 5

    def output (self):
        print(self.test)

    def doMutation(self):

        print(self.data)
        newData = self.data
        for i,row in enumerate(newData):
            for j,tile in enumerate(row):
                if (i == 1 and j == 1):
                    print(self.data)
                self.data[i][j] = tile * 2
        print(self.data)

        print("done")


class Test (object):
    def __init__ (self):
        self.test2 = "Weiß"
        print(self.test2)

    def output (self, main):
        print(self.test2)
        print(main.test)

    def change (self, main):
        main.test += self.test2
        print("after change")
        print(main.test)


main = Main()
main.output()

test = Test()
test.change(main)
test.output(main)

main.output()

main.doMutation()
