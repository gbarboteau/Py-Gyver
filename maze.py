import string

class Maze:
    def __init__(self, path):
        #self.level = [ch for ch in open(path).read() if ch != '\n']
        self.level = self.createLevel(path)

    def createLevel(self, path):
        with open(path, 'r') as p:
            lines = p.readlines()
            level = []
            for x in range(len(lines) -1):
                thisline = [ch for ch in lines[x] if ch != '\n']
                level.append(thisline)
            return level

    def printLevel(self):
        for l in self.level:
            print("".join(l))

    def findSomething(self, char):
        for x, line in enumerate(self.level):
            try:
                y = line.index(char)
                return x, y
            except ValueError:
                continue