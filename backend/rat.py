import backend.maze

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
			nextChar = self.maze.board[self.ratPos[0]-1][self.ratPos[1]]
			if(nextChar == self.maze.path_char or nextChar == self.maze.exit_char):
				moves.append(self.up_char)
		if(self.ratPos[0] != len(self.maze.board)-1):
			nextChar = self.maze.board[self.ratPos[0]+1][self.ratPos[1]]
			if(nextChar == self.maze.path_char or nextChar == self.maze.exit_char):
				moves.append(self.down_char)
		if(self.ratPos[1] != 0):
			nextChar = self.maze.board[self.ratPos[0]][self.ratPos[1]-1]
			if(nextChar == self.maze.path_char or nextChar == self.maze.exit_char):
				moves.append(self.left_char)
		if(self.ratPos[1] != len(self.maze.board[0])-1):
			nextChar = self.maze.board[self.ratPos[0]][self.ratPos[1]+1]
			if(nextChar == self.maze.path_char or nextChar == self.maze.exit_char):
				moves.append(self.right_char)
		return moves
	
	def move(self, d):
		if(d == self.up_char):
			newpos = [self.ratPos[0]-1, self.ratPos[1]]
			if(self.maze.board[newpos[0]][newpos[1]] == self.maze.path_char):
				self.ratPos = newpos
				return True
			elif(self.maze.board[newpos[0]][newpos[1]] == self.maze.exit_char):
				self.ratPos = newpos
				return False
		if(d == self.down_char):
			newpos = [self.ratPos[0]+1, self.ratPos[1]]
			if(self.maze.board[newpos[0]][newpos[1]] == self.maze.path_char):
				self.ratPos = newpos
				return True
			elif(self.maze.board[newpos[0]][newpos[1]] == self.maze.exit_char):
				self.ratPos = newpos
				return False
		if(d == self.left_char):
			newpos = [self.ratPos[0], self.ratPos[1]-1]
			if(self.maze.board[newpos[0]][newpos[1]] == self.maze.path_char):
				self.ratPos = newpos
				return True
			elif(self.maze.board[newpos[0]][newpos[1]] == self.maze.exit_char):
				self.ratPos = newpos
				return False
		if(d == self.right_char):
			newpos = [self.ratPos[0], self.ratPos[1]+1]
			if(self.maze.board[newpos[0]][newpos[1]] == self.maze.path_char):
				self.ratPos = newpos
				return True
			elif(self.maze.board[newpos[0]][newpos[1]] == self.maze.exit_char):
				self.ratPos = newpos
				return False
		return False
		
	def reset(self):
		self.ratPos = self.maze.getStart()
		return True
		
	def tempMove(self, m):
		old = self.getPos()
		self.move(m)
		new = self.getPos()
		self.ratPos = old
		return new