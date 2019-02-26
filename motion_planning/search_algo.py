# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


GRID = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
INIT = [0, 0]
GOAL = [len(grid)-1, len(grid[0])-1]
COST = 1

DELTA = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]  # go right
         ]

DELTA_NAME = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = []
    # possibilities = []
    # g_value = 0
    # success = False
    # while not success:
    #     if init == goal:
    #         # starting point and the goal is the same
    #         path.append(g_value)
    #         path.extend(init)
    #         success = True
    #     else:
    #         for d in delta:
    #             pass

    closed_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    closed_grid[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open_grid = [[g, x, y]]

    found = resign = False

    while not found and not resign:
        if len(open_grid) == 0:
            resign = True
            path = 'fail'
            print('fail')
        else:
            open_grid.sort()
            open_grid.reverse()
            next_item = open_grid.pop()
            g = next_item[0]
            x = next_item[1]
            y = next_item[2]

            if goal == [x, y]:
                found = True
                path = next_item
                print(next_item)
            else:
                for i in range(len(DELTA)):
                    x_prime, y_prime = x + DELTA[i][0], y + DELTA[i][1]
                    # if (x2 >= 0 and x2 < len(grid)) and (y2 >= 0 and y2 < len(grid[0])):
                    if 0 <= x_prime < len(grid) and 0 <= y_prime < len(grid[0]):
                        if closed_grid[x_prime][y_prime] == 0 and grid[x_prime][y_prime] == 0:
                            g_prime = g + cost
                            open_grid.append([g_prime, x_prime, y_prime])
                            closed_grid[x_prime][y_prime] = 1
    return path


search(GRID, INIT, GOAL, COST)
