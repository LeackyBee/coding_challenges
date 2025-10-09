import io
from copy import deepcopy
from heapq import heapify, heappop, heappush

from AdventOfCode.parse_utils import parse_file_to_int_array, parse_file_to_int_matrix, parse_char_array_to_string, \
    parse_int_array_to_string
from Utils.logger import logger
from Utils.matrix_utils import step, get_valid_neighbours, init_matrix

def iterate(grid, positions, count):
    for i in range(count):
        pos = positions[i]
        grid[pos[1]][pos[0]] = "#"
    return grid

def enumerate(grid, positions):
    output = [(0, deepcopy(grid))]
    for i in range(len(positions)):
        pos = positions[i]
        grid[pos[1]][pos[0]] = "#"
        output.append(deepcopy(grid))
    return output

def astar(grid):
    pos = (0,0)
    target = (len(grid)-1,len(grid[0])-1)
    grid[pos[0]][pos[1]] = 0

    frontier = [(0, pos)]
    heapify(frontier)

    logger.debug(frontier)
    while frontier:
        min_node = heappop(frontier)
        score = min_node[0]
        pos = min_node[1]

        if pos == target:
            return score

        neighbours = get_valid_neighbours(grid, pos[0], pos[1])

        for neighbour in neighbours:
            neighbour_score = grid[neighbour[0]][neighbour[1]]
            if neighbour_score == "#":
                # wall
                continue
            elif type(neighbour_score) != int:
                neighbour_score = 0

            nscore = score + 1

            if (not neighbour_score) or (neighbour_score > nscore):
                # if we're updating the score
                grid[neighbour[0]][neighbour[1]] = nscore
                heappush(frontier, (nscore, neighbour))
        logger.debug(frontier)
        #logger.debug(parse_int_array_to_string(grid))

    return None

def bisect_search(grids, start, end):
    while start < end:
        mid = (start+end)//2
        res = astar(grids[mid])
        logger.debug(f"Grid {mid} has result {res}")
        if res is None:
            end = mid
        else:
            start = mid
        logger.debug(f"Start = {start}. End = {end}")
    return start

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""")

    try:
        file = open(filepath)
    except:
        pass

    positions = parse_file_to_int_matrix(file, sep=",")

    grid = init_matrix(71,71,".")

    grids = enumerate(grid, positions)
    logger.print(grids)

    #iterate(grid, positions, 1024)
    #logger.print(parse_int_array_to_string(grid))
    #logger.print(astar(grid))

    logger.print(positions[bisect_search(grids, 12, len(grids))])


