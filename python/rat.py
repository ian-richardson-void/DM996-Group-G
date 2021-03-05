import maze

class Rat:
	# GLOBALS
	up_char = 'U'
	down_char = 'D'
	left_char = 'L'
	right_char = 'R'

	# the rat to be controlled
	def __init__(self, maze):
		self.ratPos = maze.getStart()
		self.maze = maze

	def getPos(self):
		return self.ratPos

	def getMoves(self):
		# CHECK CELLS SURROUNDING
		# returns a list of L, R, U or D
		moves = []
		if(self.ratPos[0] != 0):
			if(self.maze.board[self.ratPos[0]-1][self.ratPos[1]] == self.maze.path_char):
				moves.append(self.up_char)
		if(self.ratPos[0] != len(self.maze.board)-1):
			if(self.maze.board[self.ratPos[0]+1][self.ratPos[1]] == self.maze.path_char):
				moves.append(self.down_char)
		if(self.ratPos[1] != 0):
			if(self.maze.board[self.ratPos[0]][self.ratPos[1]-1] == self.maze.path_char):
				moves.append(self.left_char)
		if(self.ratPos[1] != len(self.maze.board[0])-1):
			if(self.maze.board[self.ratPos[0]][self.ratPos[1]+1] == self.maze.path_char):
				moves.append(self.right_char)
		return moves
	
	def move(self, d):
		if(d == self.up_char and self.maze.board[self.ratPos[0]-1][self.ratPos[1]] == self.maze.path_char):
			self.ratPos = [self.ratPos[0]-1, self.ratPos[1]]
		if(d == self.down_char and self.maze.board[self.ratPos[0]+1][self.ratPos[1]] == self.maze.path_char):
			self.ratPos = [self.ratPos[0]+1, self.ratPos[1]]
		if(d == self.left_char and self.maze.board[self.ratPos[0]][self.ratPos[1]-1] == self.maze.path_char):
			self.ratPos = [self.ratPos[0], self.ratPos[1]-1]
		if(d == self.right_char and self.maze.board[self.ratPos[0]][self.ratPos[1]+1] == self.maze.path_char):
			self.ratPos = [self.ratPos[0], self.ratPos[1]+1]