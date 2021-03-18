import maze
import rat
import HillClimb
import EvolOpt
import SimAnneal

# will create a board of set size and run all opt algs one after another and compair results

if __name__ == "__main__":
	print("RUNING ALL ALGORITHMS")
	maze = maze.Maze(15, 15)
	HillClimb.run(maze)
	SimAnneal.run(maze)
	EvolOpt.run(maze)