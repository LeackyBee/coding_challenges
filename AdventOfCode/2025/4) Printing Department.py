import io
from copy import deepcopy

from Utils.logger import logger
from Utils.matrix_utils import get_all_neighbours, within_bounds
from Utils.parse_utils import parse_file_to_char_matrix, parse_matrix_to_string


def get_accessible_rolls(grid: list[list[str]]):
    output = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                neighbours = get_all_neighbours(i, j, diagonals=True)
                neighbouring_rolls = 0
                for neighbour in neighbours:
                    if within_bounds(grid, neighbour):
                        neighbouring_rolls += 1 if grid[neighbour[0]][neighbour[1]] == "@" else 0

                if neighbouring_rolls < 4:
                    output += 1

    return output



def simulate(grid: list[list[str]]):
    output = 0

    # get a new grid with the same dimensions, so we can replace each cell with an integer
    ngrid = deepcopy(grid)

    frontier = []
    # Mark each cell with how many neighbouring rolls it has
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                neighbours = get_all_neighbours(i, j, diagonals=True)
                neighbouring_rolls = 0
                for neighbour in neighbours:
                    if within_bounds(grid, neighbour):
                        neighbouring_rolls += 1 if grid[neighbour[0]][neighbour[1]] == "@" else 0

                ngrid[i][j] = neighbouring_rolls
                if neighbouring_rolls < 4:
                    frontier.append((i,j))
            else:
                ngrid[i][j] = 0

    grid = ngrid

    logger.debug(parse_matrix_to_string(grid))
    logger.debug()
    while frontier:
        nfrontier = []
        if logger.is_enabled():
            for cell in frontier:
                grid[cell[0]][cell[1]] = "@"  # mark it as "being processed", for the debug output
            logger.debug(parse_matrix_to_string(grid))
            for cell in frontier:
                grid[cell[0]][cell[1]] = 0

        for cell in frontier:
            logger.debug(f"Removing {cell}")
            output += 1
            grid[cell[0]][cell[1]] = 0

            neighbours = get_all_neighbours(cell[0], cell[1], diagonals=True)
            for neighbour in neighbours:
                if within_bounds(grid, neighbour):
                    if grid[neighbour[0]][neighbour[1]] > 0:
                        grid[neighbour[0]][neighbour[1]] -= 1

                        if grid[neighbour[0]][neighbour[1]] < 4 and neighbour not in frontier:
                            nfrontier.append(neighbour)
        frontier = set(nfrontier)

    return output


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)

    logger.disable()

    #logger.print(get_accessible_rolls(grid))
    logger.print(simulate(grid))