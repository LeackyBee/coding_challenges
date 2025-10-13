from heapq import *

import io

from AdventOfCode.parse_utils import parse_file_to_char_matrix, parse_matrix_to_string, parse_matrix_to_string
from Utils.logger import logger
from Utils.matrix_utils import get_all_neighbours, step, turn_right, turn_left

"""
This is just a pathfinding problem
An easy approach would be to do a BFS/DFS
"""

def find(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                return (i, j)

def heuristic(pos, target):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])

def astar(grid):
    pos = find(grid, "S")
    target = find(grid, "E")
    direction = (0, 1)
    grid[pos[0]][pos[1]] = 0

    frontier = [(0, pos, direction)]
    heapify(frontier)

    logger.debug(frontier)
    while frontier:
        min_node = heappop(frontier)
        score = min_node[0]
        pos = min_node[1]

        if pos == target:
            return score
        direction = min_node[2]

        neighbours = get_all_neighbours(pos[0], pos[1])

        backwards = turn_right(direction, 2)
        left = turn_left(direction, 1)
        right = turn_right(direction, 1)

        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] == "#" or step(pos, backwards) == neighbour:
                # wall or behind us
                continue
            neighbour_score = grid[neighbour[0]][neighbour[1]]
            if type(neighbour_score) != int:
                neighbour_score = None
            if step(pos, direction) == neighbour:
                # forward costs 1
                nscore = score + 1
                ndirection = direction
            elif step(pos, left) == neighbour:
                # turn costs 1000, and moving forward costs 1
                nscore = score + 1001
                ndirection = left
            elif step(pos, right) == neighbour:
                nscore = score + 1001
                ndirection = right
            else:
                logger.print(f"Invalid Neighbour {neighbour}, Direction {direction} for position {pos}!")
                assert False

            if (not neighbour_score) or (neighbour_score > nscore):
                # if we're updating the score
                grid[neighbour[0]][neighbour[1]] = nscore
                heappush(frontier, (nscore, neighbour, ndirection))
        logger.debug(frontier)
        #logger.debug(parse_int_array_to_string(grid))

    return grid[target[0]][target[1]]

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)
    logger.enable()
    logger.print(astar(grid))