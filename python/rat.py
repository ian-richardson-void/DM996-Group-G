import maze

class Rat:
	# the rat to be controlled
	def __init__(self, maze):
		self.ratPos = maze.getStart()

	def getPos(self):
		return self.ratPos

	def getMoves(self):
		return 0
	
	def move(self):
		return 0

if __name__ == "__main__":
	print("rat run")