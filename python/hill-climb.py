import maze
import rat
# Hill-climb will have a fitness function (end - ratPos) 
# and will move the rat a step towards the end each turn

def move(rat):
	coordiff = fitness(rat)
	if(coordiff[0] > coordiff[1]):
		return rat.move(rat.down_char)
	elif(coordiff[0] <= coordiff[1]):
		if(coordiff[1] > 0):
			return rat.move(rat.right_char)
		elif(coordiff[1] <= 0):
			return rat.move(rat.left_char)

def fitness(rat):
	ratPos = rat.getPos()
	exit = rat.maze.getExit()
	coordiff = [exit[0] - ratPos[0], exit[1] - ratPos[1]]
	return coordiff

if __name__ == "__main__":
	print("RUNNING HILL-CLIMB OPTIMISATION")
	barry = rat.Rat(maze.Maze(15, 15))
	barry.maze.printBoard(barry.getPos())
	while(True):
		result = move(barry)
		if(result == False):
			break
	barry.maze.printBoard(barry.getPos())