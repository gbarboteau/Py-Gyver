import maze
import character

class GameManager:
	def __init__(self, path):
		self.maze = maze.Maze(path)
		self.mcgyver = character.McGyver(self.maze.findSomething("m"))
		self.guardian = character.Guardian(self.maze.findSomething("g"))

	def play(self):
		self.maze.printLevel()