import maze
import rat
import random

# make lots of random moves when in high temp
# when half way to the exit OR a certain time is up, switch to low temp
# move slowly towards exit in low temp

def highTemp(rat):
	legalMoves = rat.getMoves()
	m = 0
	if(len(legalMoves) == 1):
		m = legalMoves[0]
	else:
		m = legalMoves[random.randrange(0,len(legalMoves),1)]
	result = rat.move(m)
	return m, result
	
def lowTemp(rat):
	bm = fitness(rat, rat.getPos())
	for p in rat.getMoves():
		am = fitness(rat, rat.tempMove(p))
		if(bm[0] >= am[0] and bm[1] >= am[1]):
			result = rat.move(p)
			return result, True
	print("STUCK")
	return False, False
	
def fitness(rat, newpos):
	exit = rat.maze.getExit()
	coordiff = [abs(exit[0] - newpos[0]), abs(exit[1] - newpos[1])]
	return coordiff
	
def run(maze):
	print("RUNNING SIMULATED ANNEALING")
	barry = rat.Rat(maze)
	barry.maze.printBoard(barry.getPos())
	t = 0
	while(True):
		# high temp loop
		if(t >= 35):
			print("TIME EXPIRED, MOVING TO LOW TEMP")
			break
		coordiff = fitness(barry, barry.getPos())
		if(coordiff[0] <= barry.maze.hight/2 and coordiff[1] <= barry.maze.width/2):
			print("HALF-WAY, CHANGING TO LOW TEMP")
			break
		highTemp(barry)
		t += 1
	barry.maze.printBoard(barry.getPos())
	while(True):
		# low temp loop
		result, notStuck = lowTemp(barry)
		if((result == False) and (notStuck == True)):
			# we have reached the exit (or made an illegal move, shouldnt be possible)
			print("REACHED EXIT")
			break
		if(notStuck == False):
			break
	barry.maze.printBoard(barry.getPos())

if __name__ == "__main__":
	run(maze.Maze(15, 15))