import maze
import rat
import random

# Evolutionary Optimisation would run multiple agents from start to end, 
# at first making random moves but each building on the last agents successes

def moveRand(rat):
	legalMoves = rat.getMoves()
	m = 0
	if(len(legalMoves) == 1):
		m = legalMoves[0]
	else:
		m = legalMoves[random.randrange(0,len(legalMoves),1)]
	result = rat.move(m)
	return m, result
	
def moveMemory(rat, moves):
	for m in moves:
		rat.move(m)
	# check if all other moves reduce fitness
	bm = fitness(rat, rat.getPos())
	for p in rat.getMoves():
		am = fitness(rat, rat.tempMove(p))
		if(bm[0] >= am[0] and bm[1] >= am[1]):
			return True
	print("STUCK")
	return False
	
def fitness(rat, newpos):
	exit = rat.maze.getExit()
	coordiff = [abs(exit[0] - newpos[0]), abs(exit[1] - newpos[1])]
	return coordiff
	
def run(maze):
	print("RUNNING EVOLUTIONARY OPTIMISATION")
	barry = rat.Rat(maze)
	barry.maze.printBoard(barry.getPos())
	moveList = []
	while(True):
		bm = fitness(barry, barry.getPos())
		move, result = moveRand(barry)
		am = fitness(barry, barry.getPos())
		if(result == False):
			# we have reached the exit (or made an illegal move, shouldnt be possible)
			print("REACHED EXIT")
			break
		elif(bm[0] >= am[0] and bm[1] >= am[1]):
			# improvment on last pos
			moveList.append(move)
		else:
			# we have gone backwards, new child
			barry.reset()
			notStuck = moveMemory(barry, moveList)
			if(notStuck == False):
				break
	barry.maze.printBoard(barry.getPos())

if __name__ == "__main__":
	run(maze.Maze(15, 15))