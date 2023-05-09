# https://www.codewars.com/kata/58663693b359c4a6560001d6/python
# Introduction
# Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!
# Task
# You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.
# The Maze array will look like

# maze = [[1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,3],
#         [1,0,1,0,1,0,1],
#         [0,0,1,0,0,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,2,1,0,1,0,1]]
# ..with the following key

#       0 = Safe place to walk
#       1 = Wall
#       2 = Start Point
#       3 = Finish Point
#   direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
# Rules
# 1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.

# 2. The start and finish positions will change for the final tests.

# 3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.

# 4. If you reach the end point before all your moves have gone, you should return Finish.

# 5. If you hit any walls or go outside the maze border, you should return Dead.

# 6. If you find yourself still in the maze after using all the moves, you should return Lost.

def maze_runner(maze, directions):
    def find_start(_maze):
        for x, item in enumerate(_maze):
            for y, thing in enumerate(item):
                if thing == 2:
                    location = [x,y]
        return location

    start = find_start(maze)
    
    for direction in directions:
        if direction == "N":
            start[0] -= 1
        elif direction == "S":
            start[0] += 1
        elif direction == "W":
            start[1] -= 1
        elif direction == "E":
            start[1] += 1
        
        if start[0] < 0 or start[0] >= len(maze) or start[1] < 0 or start[1] >= len(maze):
            return 'Dead'
        elif maze[start[0]][start[1]] == 1:
            return 'Dead'
        elif maze[start[0]][start[1]] == 3:
            return 'Finish'
   
    return 'Lost'