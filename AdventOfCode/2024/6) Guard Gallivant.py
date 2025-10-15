import io
from copy import deepcopy

from AdventOfCode.parse_utils import parse_file_to_char_matrix, parse_matrix_to_string
from Utils.logger import logger
from Utils.matrix_utils import step, within_bounds

"""
Part 2 here (find_loops) took me way longer than normal, the key insight was that you can't place a block on the path.
Since if you did, you couldn't be where you currently are.

Another hurdle was that my code was attempting to put an obstacle outside the map - which isn't possible
This took a LONG time to figure out, but finally looked at my code and went "hang on"
"""

def find_start(grid):
    logger.debug("Finding start...")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "^":
                return (y, x)
    raise ValueError("No start found")

def turn_right(direction):
    logger.debug("Turning right!")
    return (direction[1], -direction[0])


def get_dir_char(direction):
    dir_map = {
        (0,1): "R",
        (0,-1): "L",
        (1,0): "D",
        (-1,0): "U",
    }
    return dir_map[direction[0]][direction[1]]

def map_patrol(grid):
    # find at guard pos
    # set pos = guard pos
    # loop:
    # if pos is not marked as X, mark it as X and add 1 to count
    # get next pos by pos + dir
    # check if next pos is free, if so set pos = next pos
    # if not, change direction and don't touch pos
    pos = find_start(grid)
    direction = (-1,0)
    count = 0
    logger.debug(parse_matrix_to_string(grid))
    while within_bounds(grid, pos):
        if grid[pos[0]][pos[1]] != "X":
            grid[pos[0]][pos[1]] = "X"
            count += 1
        next_pos = step(pos, direction)
        logger.debug(f"Current position: {pos}")
        logger.debug(f"Current direction: {direction}")
        logger.debug(f"Next position: {next_pos}")
        if within_bounds(grid, next_pos) and grid[next_pos[0]][next_pos[1]] == "#":
            direction = turn_right(direction)
            logger.debug(parse_matrix_to_string(grid))
        else:
            pos = next_pos
    logger.debug(parse_matrix_to_string(grid))
    return count

def check_direction(grid, pos, direction):
    # start at pos
    # while pos is within bounds
    # if current pos has current direction marker, return true (we've found a path we've already been on in this direction)
    # set current pos to have current direction marker
    # get next pos
    # if next pos is a wall, turn right and change direction marker
    # else set pos = next pos
    # if the loop escapes, return false
    char = get_dir_char(direction)
    logger.debug("Checking direction...")
    logger.debug(f"Current grid")
    logger.debug(parse_matrix_to_string(grid))
    logger.debug(f"Current position: {pos}")
    logger.debug(f"Current direction: {direction}")
    logger.debug("Entering loop")
    while within_bounds(grid, pos):
        logger.debug(f"Current position: {pos}")
        if char in grid[pos[0]][pos[1]]:
            return True
        if grid[pos[0]][pos[1]] == ".":
            grid[pos[0]][pos[1]] = char
        else:
            grid[pos[0]][pos[1]] += char
        next_pos = step(pos, direction)
        if within_bounds(grid, next_pos) and grid[next_pos[0]][next_pos[1]] == "#":
            direction = turn_right(direction)
            char = get_dir_char(direction)
        else:
            pos = next_pos
    return False

def find_loops(grid):
    # find guard pos
    # set pos = guard pos
    # mark current pos with direction
    # get next pos
    # if next pos is a wall, turn right and continue
    # otherwise if the next tile is unvisited, deepcopy the grid and send a ray out to the right
    #   if it lands on a square with the same direction, it returns true and we add 1 to our count
    #   otherwise, it must eventually escape the grid, so once that happens return false
    # set pos = next_pos
    pos = find_start(grid)
    direction = (-1, 0)
    count = 0

    # while we're still in the grid
    while within_bounds(grid, pos):
        # append current direction to the position
        char = get_dir_char(direction)
        if grid[pos[0]][pos[1]] == ".":
            grid[pos[0]][pos[1]] = char
        else:
            grid[pos[0]][pos[1]] += char

        # get next step
        next_pos = step(pos, direction)

        if within_bounds(grid, next_pos) and grid[next_pos[0]][next_pos[1]] == "#":
            # if wall, can continue without checking to the right (since we're now going that way)
            direction = turn_right(direction)
        else:
            if within_bounds(grid, next_pos) and grid[next_pos[0]][next_pos[1]] == ".":
                # can only place a block if we've not been to the tile

                # make new grid with obstacle in front
                ngrid = deepcopy(grid)
                ngrid[next_pos[0]][next_pos[1]] = "#"
                if check_direction(ngrid, pos, turn_right(direction)):
                    count += 1
            pos = next_pos

    return count

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)
    logger.print(f"The guard visits {map_patrol(deepcopy(grid))} distinct positions")
    logger.print(f"There are {find_loops(grid)} positions that a block can be placed to create a loop")