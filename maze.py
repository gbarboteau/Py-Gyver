import string
import item
import random

class Maze:
    def __init__(self, path):
        self.level = self.createLevel(path)
        self.itemList = [item.Item("needle"), item.Item("toothpaste"), item.Item("ether")]
        for i in self.itemList:
            i.position = self.setItemPosition(i.char)

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

    def setItemPosition(self, char):
        new_position = (random.randrange(15), random.randrange(15))
        if self.isThereWalls(new_position, (0, 0)):
            return self.setItemPosition(char)
        else:
            self.level[new_position[1]][new_position[0]] = char
            return new_position

    def updateLevel(self, previousMGPosition, currentMGPosition):
        px, py, cx, cy = previousMGPosition[0], previousMGPosition[1], currentMGPosition[0], currentMGPosition[1]
        self.level[py][px] = " "
        self.level[cy][cx] = "m"

    def pickItem(self, itemPosition):
        for i in self.itemList:
            if i.position == itemPosition:
                name_to_return = i.name
                self.itemList.remove(i)
                return name_to_return

    def meetTheGuardian(self):
        pass

    def findSomething(self, char):
        for x in range(len(self.level) -1):
            if(char in self.level[x]):
                return(self.level[x].index(char), x)

    def checkSomething(self, position, char):
        if(self.level[position[1]][position[0]] == char):
            return True
        else:
            return False

    def isThereWalls(self, currentPosition, direction):
        targetPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
        return self.checkSomething(targetPosition, "x")
        