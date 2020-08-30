# check if object given to a function of a other object is a copy or a reference

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

    def output (self):
        print(self.test)


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