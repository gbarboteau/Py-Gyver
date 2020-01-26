import string


class Maze:
    def __init__(self, path):
        self.level = self.createLevel(path)

    def createLevel(self, path):
        with open(path, 'r') as p:
            lines = p.readlines()
            level = []
            for x in range(len(lines)):
                thisline = [char for char in lines[x] if char != '\n']
                level.append(thisline)
            return level

    def printLevel(self):
        for l in self.level:
            print("".join(l))

    def updateLevel(self, previousMGPosition, currentMGPosition):
        px, py, cx, cy = previousMGPosition[0], previousMGPosition[1], currentMGPosition[0], currentMGPosition[1]
        self.level[py][px] = " "
        self.level[cy][cx] = "m"

    def findSomething(self, char):
        for x in range(len(self.level) -1):
            if(char in self.level[x]):
                return(self.level[x].index(char), x)

    def checkSomething(self, position, char):
        print("the tile is: " + str(self.level[position[0]][position[1]]))
        if(self.level[position[1]][position[0]] == char):
            return True
        else:
            return False

    def isThereWalls(self, currentPosition, direction):
        targetPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
        print(targetPosition)
        return self.checkSomething(targetPosition, "x")
        