class InputOutputString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Give a new string")

    def printString(self):
        print(self.s.upper())


