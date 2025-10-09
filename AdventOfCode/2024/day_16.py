from heapq import *

import io

from AdventOfCode.parse_utils import parse_file_to_char_matrix, parse_char_array_to_string, parse_int_array_to_string
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
    min_target_score = None

    path_nodes = {pos: {pos}}

    logger.debug(frontier)
    while frontier:
        logger.debug()
        logger.debug(path_nodes)
        #logger.debug(parse_int_array_to_string(grid))
        min_node = heappop(frontier)
        score = min_node[0]
        pos = min_node[1]

        if min_target_score is not None and score > min_target_score:
            # lowest score is higher than the minimum score to the target, no more best paths can be found
            break

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

            if neighbour_score == nscore:
                # if the score is the same, we just need to add our nodes to the list
                # no need to worry about forward propagation, if we get here we must have a lower score
                # therefore its not been popped and so has no forward nodes#
                logger.debug("updating neighbour")
                logger.debug(f"neighbour has {path_nodes[neighbour]}")
                logger.debug(f"current has {path_nodes[pos]}")

                ppath_nodes = path_nodes[pos].copy()
                npath_nodes = path_nodes[neighbour].copy()
                npath_nodes.add(neighbour)

                npath_nodes = npath_nodes.union(ppath_nodes)
                path_nodes[neighbour] = npath_nodes
                logger.debug(f"neighbour now has {path_nodes[neighbour]}")

            if (not neighbour_score) or (neighbour_score > nscore):
                # if we're updating the score we just replace the nodes in path_nodes
                ppath_nodes = path_nodes[pos].copy()
                ppath_nodes.add(neighbour)
                path_nodes[neighbour] = ppath_nodes
                grid[neighbour[0]][neighbour[1]] = nscore
                heappush(frontier, (nscore, neighbour, ndirection))
        logger.debug(frontier)
        #logger.debug(parse_int_array_to_string(grid))

    return grid[target[0]][target[1]], len(path_nodes[target])

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)
    logger.enable()
    score, sitting = astar(grid)
    logger.print(f"Shortest path has score {score} and best path tiles {sitting}")