import maze
import rat

maze = maze.Maze(15, 15)
barry = rat.Rat(maze)

maze.printBoard(barry.getPos())