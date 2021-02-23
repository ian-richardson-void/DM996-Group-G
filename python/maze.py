import random
from colorama import init
from colorama import Fore, Back, Style

# GLOBALS
path_char = 'P'
wall_char = 'W'
unvisited = 'U'
start_char = 'S'
exit_char = 'E'
rat_char = 'R'

##################
# USABLE METHODS #
##################

def genBoard(w, h):
	# INIT
	board = [unvisited]*h
	for i in range(h):
		board[i] = [unvisited]*w
	
	# POPULATE
	starting_h = random.randrange(1,h-1)
	starting_w = random.randrange(1,w-1)
	board[starting_h][starting_w] = path_char
	
	walls = [] # list of coords of the walls positions
	for i in range(starting_h-1, starting_h+2, 2):
		walls.append([i,starting_w])
		board[i][starting_w] = wall_char
	for i in range(starting_w-1, starting_w+2, 2):
		walls.append([starting_h,i])
		board[starting_h][i] = wall_char
		
	board = wallLoop(board, w, h, walls)
	return board

def printBoard(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if(board[i][j] == unvisited):
				print(Fore.WHITE + str(board[i][j]), end=" ")
			elif(board[i][j] == path_char):
				print(Fore.GREEN + str(board[i][j]), end=" ")
			elif(board[i][j] == start_char or board[i][j] == exit_char):
				print(Fore.YELLOW + str(board[i][j]), end=" ")
			elif(board[i][j] == wall_char):
				print(Fore.RED + str(board[i][j]), end=" ")
			elif(board[i][j] == rat_char):
				print(Fore.BLUE + str(board[i][j]), end=" ")
		print('\n', end="")
	print("")

def getStart(board):
	for i in range(len(board[0])):
		if (board[0][i] == start_char):
			return [0, i]
	return -1
	
def getExit(board):
	h = len(board)-1
	for i in range(len(board[h])):
		if (board[h][i] == exit_char):
			return [h, i]
	return -1

###################
# PRIVATE METHODS #
###################

def wallLoop(board, w, h, walls):
	while walls:
		# pick random wall from list
		rand_wall = walls[random.randrange(0,len(walls))]
		
		# check if it is NOT a left wall
		if (rand_wall[1] != 0):
			if (board[rand_wall[0]][rand_wall[1]-1] == unvisited) and (board[rand_wall[0]][rand_wall[1]+1] == path_char):
				s_paths = surroundingPaths(rand_wall,board,w,h)
				# if wall has too few path surrounding, break rand_wall and replace with a path
				if (s_paths < 2):
					board[rand_wall[0]][rand_wall[1]] = path_char
					board, walls = addUpperWall(board,walls,rand_wall,w,h)
					board, walls = addBottomWall(board,walls,rand_wall,w,h)
					board, walls = addLeftWall(board,walls,rand_wall,w,h)
				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)
				continue
		
		# NOT Upper wall
		if rand_wall[0] != 0:
			if (board[rand_wall[0]-1][rand_wall[1]] == unvisited) and (board[rand_wall[0]+1][rand_wall[1]] == path_char):
				s_paths = surroundingPaths(rand_wall,board,w,h)
				# if wall has too few path surrounding, break rand_wall and replace with a path
				if (s_paths < 2):
					board[rand_wall[0]][rand_wall[1]] = path_char
					board, walls = addUpperWall(board,walls,rand_wall,w,h)
					board, walls = addLeftWall(board,walls,rand_wall,w,h)
					board, walls = addRightWall(board,walls,rand_wall,w,h)
				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)
				continue
			
		# NOT Bottom wall
		if (rand_wall[0] != h-1):
			if (board[rand_wall[0]+1][rand_wall[1]] == unvisited) and (board[rand_wall[0]-1][rand_wall[1]] == path_char):
				s_paths = surroundingPaths(rand_wall,board,w,h)
				# if wall has too few path surrounding, break rand_wall and replace with a path
				if (s_paths < 2):
					board[rand_wall[0]][rand_wall[1]] = path_char
					board, walls = addBottomWall(board,walls,rand_wall,w,h)
					board, walls = addLeftWall(board,walls,rand_wall,w,h)
					board, walls = addRightWall(board,walls,rand_wall,w,h)
				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)
				continue
				
		# NOT Right wall
		if rand_wall[1] != w-1:
			if board[rand_wall[0]][rand_wall[1]+1] == unvisited and board[rand_wall[0]][rand_wall[1]-1] == path_char:
				s_paths = surroundingPaths(rand_wall,board,w,h)
				# if wall has too few path surrounding, break rand_wall and replace with a path
				if (s_paths < 2):
					board[rand_wall[0]][rand_wall[1]] = path_char
					board, walls = addBottomWall(board,walls,rand_wall,w,h)
					board, walls = addUpperWall(board,walls,rand_wall,w,h)
					board, walls = addRightWall(board,walls,rand_wall,w,h)
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
			if (board[i][j] == unvisited):
				board[i][j] = wall_char

	# Set entrance and exit
	for i in range(w):
		if (board[1][i] == path_char):
			board[0][i] = rat_char
			break

	for i in range(w-1, 0, -1):
		if (board[h-2][i] == path_char):
			board[h-1][i] = exit_char
			break
	
	return board
	
def surroundingPaths(rand_wall,board,w,h):
	s_paths = 0
	if (rand_wall[0] != 0) and (board[rand_wall[0]-1][rand_wall[1]] == path_char):
		s_paths += 1
	if (rand_wall[0] != h-1) and (board[rand_wall[0]+1][rand_wall[1]] == path_char):
		s_paths += 1
	if (rand_wall[1] != 0) and (board[rand_wall[0]][rand_wall[1]-1] == path_char):
		s_paths += 1
	if (rand_wall[1] != w-1) and (board[rand_wall[0]][rand_wall[1]+1] == path_char):
		s_paths += 1
	return s_paths
	
def addUpperWall(board,walls,rand_wall,w,h):
	# Upper cell
	if (rand_wall[0] != 0):
		if (board[rand_wall[0]-1][rand_wall[1]] != path_char):
			board[rand_wall[0]-1][rand_wall[1]] = wall_char
		if ([rand_wall[0]-1, rand_wall[1]] not in walls):
			walls.append([rand_wall[0]-1, rand_wall[1]])
	return (board, walls)
	
def addBottomWall(board,walls,rand_wall,w,h):
	# Bottom cell
	if (rand_wall[0] != h-1):
		if (board[rand_wall[0]+1][rand_wall[1]] != path_char):
			board[rand_wall[0]+1][rand_wall[1]] = wall_char
		if ([rand_wall[0]+1, rand_wall[1]] not in walls):
			walls.append([rand_wall[0]+1, rand_wall[1]])
	return (board, walls)

def addLeftWall(board,walls,rand_wall,w,h):
	# Left cell
	if (rand_wall[1] != 0):	
		if (board[rand_wall[0]][rand_wall[1]-1] != path_char):
			board[rand_wall[0]][rand_wall[1]-1] = wall_char
		if ([rand_wall[0], rand_wall[1]-1] not in walls):
			walls.append([rand_wall[0], rand_wall[1]-1])
	return (board, walls)
	
def addRightWall(board,walls,rand_wall,w,h):
	# Right cell
	if (rand_wall[1] != 0):	
		if (board[rand_wall[0]][rand_wall[1]+1] != path_char):
			board[rand_wall[0]][rand_wall[1]+1] = wall_char
		if ([rand_wall[0], rand_wall[1]+1] not in walls):
			walls.append([rand_wall[0], rand_wall[1]-1])
	return (board, walls)

if(__name__ == "__main__"):
	init()
	board = genBoard(10, 10)
	printBoard(board)