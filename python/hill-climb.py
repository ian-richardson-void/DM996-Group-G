import maze
import rat
# Hill-climb will have a fitness function (end - ratPos) 
# and will move the rat a step towards the end each turn

def fitness():
	return 0

if __name__ == "__main__":
	print("RUNNING HILL-CLIMB OPTIMISATION")
	maze1 = maze.Maze(15, 15)
	barry = rat.Rat(maze1)
	maze1.printBoard(barry.getPos())
	
	d = barry.getMoves()
	barry.move(d[0])
	maze1.printBoard(barry.getPos())