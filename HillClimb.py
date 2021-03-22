import backend.maze as maze
import backend.rat as rat

# Hill-climb will have a fitness function (end - ratPos) 
# and will move the rat a step towards the end each turn

def move(rat):
	stuck, move = checkStuck(rat)
	if(stuck == False):
		result = rat.move(move)
		return result, True
	else:
		return False, False
	
def checkStuck(rat):
	bm = fitness(rat, rat.getPos())
	for p in rat.getMoves():
		am = fitness(rat, rat.tempMove(p))
		if(bm[0] >= am[0] and bm[1] >= am[1]):
			return False, p
	print("STUCK")
	return True, 0

def fitness(rat, newpos):
	exit = rat.maze.getExit()
	coordiff = [abs(exit[0] - newpos[0]), abs(exit[1] - newpos[1])]
	return coordiff
	
def run(maze):
	print("RUNNING HILL-CLIMB OPTIMISATION")
	barry = rat.Rat(maze)
	barry.maze.printBoard(barry.getPos())
	while(True):
		result, notStuck = move(barry)
		if((result == False) and (notStuck == True)):
			# we have reached the exit (or made an illegal move, shouldnt be possible)
			print("REACHED EXIT")
			break
		if(notStuck == False):
			break
	barry.maze.printBoard(barry.getPos())

if __name__ == "__main__":
	run(maze.Maze(15, 15))