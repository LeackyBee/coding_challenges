import io

from AdventOfCode.parse_utils import parse_file_to_int_matrix
from Utils.logger import logger
from Utils.matrix_utils import within_bounds, get_valid_neighbours

"""
This is essentially breadth first search again, but we only consider links where the value increases by 1
For part 1, we only care about the distinct destinations, so we keep the frontier as a set
For part 2, we care about the distinct paths, so we keep the frontier as a list
"""

def find_trailheads(grid):
    output = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                output.append((i, j))
    return output



def count_trailhead_scores(grid):
    trailheads = find_trailheads(grid)
    count = 0
    for head in trailheads:
        logger.debug(f"Trailhead: {head}")
        positions = {head}
        for i in range(1, 10):
            logger.debug(f"Current positions: {positions}")
            npositions = set()
            for position in positions:
                logger.debug(f"Current position: {position}")
                neighbours = get_valid_neighbours(grid, position[0], position[1])
                logger.debug(f"Current neighbours: {positions}")
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] == i:
                        npositions.add(neighbour)
            positions = npositions
        logger.debug(positions)
        count += len(positions)
    return count

def get_trailhead_rating(grid):
    trailheads = find_trailheads(grid)
    count = 0
    for head in trailheads:
        logger.debug(f"Trailhead: {head}")
        positions = [head]
        for i in range(1, 10):
            logger.debug(f"Current positions: {positions}")
            npositions = []
            for position in positions:
                logger.debug(f"Current position: {position}")
                neighbours = get_valid_neighbours(grid, position[0], position[1])
                logger.debug(f"Current neighbours: {positions}")
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] == i:
                        npositions.append(neighbour)
            positions = npositions
        logger.debug(positions)
        count += len(positions)
    return count



if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_int_matrix(file)

    logger.print(f"Trailhead score = {count_trailhead_scores(grid)}")
    logger.print(f"Trailhead rating = {get_trailhead_rating(grid)}")
