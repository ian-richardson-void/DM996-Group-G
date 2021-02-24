import random
from colorama import init
from colorama import Fore, Back, Style

class Maze:
	# GLOBALS
	path_char = 'P'
	wall_char = 'W'
	unvisited = 'U'
	start_char = 'S'
	exit_char = 'E'
	rat_char = 'R'
	
	def __init__(self, w, h):
		print(w, h)
		self.board = self.genBoard(w, h)
	
	##################
	# USABLE METHODS #
	##################
	
	def genBoard(self, w, h):
		# INIT
		self.board = [self.unvisited]*h
		for i in range(h):
			self.board[i] = [self.unvisited]*w

		# POPULATE
		starting_h = random.randrange(1,h-1)
		starting_w = random.randrange(1,w-1)
		self.board[starting_h][starting_w] = self.path_char
		
		walls = [] # list of coords of the walls positions
		for i in range(starting_h-1, starting_h+2, 2):
			walls.append([i,starting_w])
			self.board[i][starting_w] = self.wall_char
		for i in range(starting_w-1, starting_w+2, 2):
			walls.append([starting_h,i])
			self.board[starting_h][i] = self.wall_char
			
		self.board = self.wallLoop(w, h, walls)
		return self.board
	
	def printBoard(self, ratPos):
		init()
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if(ratPos[0] == i and ratPos[1] == j):
					print(Fore.BLUE + str(self.rat_char), end=" ")
				elif(self.board[i][j] == self.unvisited):
					print(Fore.WHITE + str(self.board[i][j]), end=" ")
				elif(self.board[i][j] == self.path_char):
					print(Fore.GREEN + str(self.board[i][j]), end=" ")
				elif(self.board[i][j] == self.start_char or self.board[i][j] == self.exit_char):
					print(Fore.YELLOW + str(self.board[i][j]), end=" ")
				elif(self.board[i][j] == self.wall_char):
					print(Fore.RED + str(self.board[i][j]), end=" ")
			print('\n', end="")
		print("")
		
	def getStart(self):
		for i in range(len(self.board[0])):
			if (self.board[0][i] == self.start_char):
				return [0, i]
		return -1
		
	def getExit(self):
		h = len(self.board)-1
		for i in range(len(self.board[h])):
			if (self.board[h][i] == self.exit_char):
				return [h, i]
		return -1
		
	###################
	# PRIVATE METHODS #
	###################
	
	def wallLoop(self, w, h, walls):
		while walls:
			# pick random wall from list
			rand_wall = walls[random.randrange(0,len(walls))]
			
			# check if it is NOT a left wall
			if (rand_wall[1] != 0):
				if (self.board[rand_wall[0]][rand_wall[1]-1] == self.unvisited) and (self.board[rand_wall[0]][rand_wall[1]+1] == self.path_char):
					s_paths = self.surroundingPaths(rand_wall,w,h)
					# if wall has too few path surrounding, break rand_wall and replace with a path
					if (s_paths < 2):
						self.board[rand_wall[0]][rand_wall[1]] = self.path_char
						walls = self.addUpperWall(walls,rand_wall,w,h)
						walls = self.addBottomWall(walls,rand_wall,w,h)
						walls = self.addLeftWall(walls,rand_wall,w,h)
					# Delete wall
					for wall in walls:
						if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
							walls.remove(wall)
					continue
			
			# NOT Upper wall
			if rand_wall[0] != 0:
				if (self.board[rand_wall[0]-1][rand_wall[1]] == self.unvisited) and (self.board[rand_wall[0]+1][rand_wall[1]] == self.path_char):
					s_paths = self.surroundingPaths(rand_wall,w,h)
					# if wall has too few path surrounding, break rand_wall and replace with a path
					if (s_paths < 2):
						self.board[rand_wall[0]][rand_wall[1]] = self.path_char
						walls = self.addUpperWall(walls,rand_wall,w,h)
						walls = self.addLeftWall(walls,rand_wall,w,h)
						walls = self.addRightWall(walls,rand_wall,w,h)
					# Delete wall
					for wall in walls:
						if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
							walls.remove(wall)
					continue
				
			# NOT Bottom wall
			if (rand_wall[0] != h-1):
				if (self.board[rand_wall[0]+1][rand_wall[1]] == self.unvisited) and (self.board[rand_wall[0]-1][rand_wall[1]] == self.path_char):
					s_paths = self.surroundingPaths(rand_wall,w,h)
					# if wall has too few path surrounding, break rand_wall and replace with a path
					if (s_paths < 2):
						self.board[rand_wall[0]][rand_wall[1]] = self.path_char
						walls = self.addBottomWall(walls,rand_wall,w,h)
						walls = self.addLeftWall(walls,rand_wall,w,h)
						walls = self.addRightWall(walls,rand_wall,w,h)
					# Delete wall
					for wall in walls:
						if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
							walls.remove(wall)
					continue
					
			# NOT Right wall
			if rand_wall[1] != w-1:
				if self.board[rand_wall[0]][rand_wall[1]+1] == self.unvisited and self.board[rand_wall[0]][rand_wall[1]-1] == self.path_char:
					s_paths = self.surroundingPaths(rand_wall,w,h)
					# if wall has too few path surrounding, break rand_wall and replace with a path
					if (s_paths < 2):
						self.board[rand_wall[0]][rand_wall[1]] = self.path_char
						walls = self.addBottomWall(walls,rand_wall,w,h)
						walls = self.addUpperWall(walls,rand_wall,w,h)
						walls = self.addRightWall(walls,rand_wall,w,h)
					# Delete wall
					for wall in walls:
						if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
							walls.remove(wall)
					continue
			
			# Delete the wall from the list anyway
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
		
		# Mark the remaining unvisited cells as walls
		for i in range(h):
			for j in range(w):
				if (self.board[i][j] == self.unvisited):
					self.board[i][j] = self.wall_char

		# Set entrance and exit
		for i in range(w):
			if (self.board[1][i] == self.path_char):
				self.board[0][i] = self.start_char
				break

		for i in range(w-1, 0, -1):
			if (self.board[h-2][i] == self.path_char):
				self.board[h-1][i] = self.exit_char
				break
		
		return self.board
		
	def surroundingPaths(self, rand_wall,w,h):
		s_paths = 0
		if (rand_wall[0] != 0) and (self.board[rand_wall[0]-1][rand_wall[1]] == self.path_char):
			s_paths += 1
		if (rand_wall[0] != h-1) and (self.board[rand_wall[0]+1][rand_wall[1]] == self.path_char):
			s_paths += 1
		if (rand_wall[1] != 0) and (self.board[rand_wall[0]][rand_wall[1]-1] == self.path_char):
			s_paths += 1
		if (rand_wall[1] != w-1) and (self.board[rand_wall[0]][rand_wall[1]+1] == self.path_char):
			s_paths += 1
		return s_paths
		
	def addUpperWall(self, walls,rand_wall,w,h):
		# Upper cell
		if (rand_wall[0] != 0):
			if (self.board[rand_wall[0]-1][rand_wall[1]] != self.path_char):
				self.board[rand_wall[0]-1][rand_wall[1]] = self.wall_char
			if ([rand_wall[0]-1, rand_wall[1]] not in walls):
				walls.append([rand_wall[0]-1, rand_wall[1]])
		return walls
		
	def addBottomWall(self, walls,rand_wall,w,h):
		# Bottom cell
		if (rand_wall[0] != h-1):
			if (self.board[rand_wall[0]+1][rand_wall[1]] != self.path_char):
				self.board[rand_wall[0]+1][rand_wall[1]] = self.wall_char
			if ([rand_wall[0]+1, rand_wall[1]] not in walls):
				walls.append([rand_wall[0]+1, rand_wall[1]])
		return walls

	def addLeftWall(self, walls,rand_wall,w,h):
		# Left cell
		if (rand_wall[1] != 0):	
			if (self.board[rand_wall[0]][rand_wall[1]-1] != self.path_char):
				self.board[rand_wall[0]][rand_wall[1]-1] = self.wall_char
			if ([rand_wall[0], rand_wall[1]-1] not in walls):
				walls.append([rand_wall[0], rand_wall[1]-1])
		return walls
	
	def addRightWall(self, walls,rand_wall,w,h):
		# Right cell
		if (rand_wall[1] != 0):	
			if (self.board[rand_wall[0]][rand_wall[1]+1] != self.path_char):
				self.board[rand_wall[0]][rand_wall[1]+1] = self.wall_char
			if ([rand_wall[0], rand_wall[1]+1] not in walls):
				walls.append([rand_wall[0], rand_wall[1]-1])
		return walls

if(__name__ == "__main__"):
	board = Maze(10, 10)
	board.printBoard(board.getStart())