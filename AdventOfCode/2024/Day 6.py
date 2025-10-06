import io
from copy import deepcopy

from AdventOfCode.parse_utils import parse_file_to_char_array, parse_char_array_to_string
from Utils.Logger import logger

# map direction to letter
dir_map = {0: {1: "R", -1: "L"},
           1: {0: "D"},
           -1: {0: "U"}}

# when heading (0,1), check (1,0) for "D"
check_dir_map = {0: {1: (1, 0, "D"), -1: (-1, 0, "U")},
                 1: {0: (0, -1, "L")},
                 -1: {0: (0, 1, "R")}}

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "^":
                return (y, x)
    raise ValueError("No start found")


def map_patrol(grid):
    grid = grid.copy()
    pos = find_start(grid)
    direction = (-1,0)



    grid[pos[0]][pos[1]] = "X"
    count = 1
    next_pos = (pos[0]+direction[0],pos[1]+direction[1])
    logger.debug(parse_char_array_to_string(grid))
    while next_pos[0] >= 0 and next_pos[0] < len(grid) and next_pos[1] >= 0 and next_pos[1] < len(grid[0]):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        logger.debug(f"Current position: {pos}")
        logger.debug(f"Current direction: {direction}")
        logger.debug(f"Next position: {next_pos}")
        if grid[next_pos[0]][next_pos[1]] == "#":
            logger.debug("Wall! Turning right")
            direction = (direction[1], -direction[0])
            logger.debug(parse_char_array_to_string(grid))
            continue
        elif grid[next_pos[0]][next_pos[1]] != "X":
            grid[next_pos[0]][next_pos[1]] = "X"
            count += 1
        pos = (pos[0]+direction[0],pos[1]+direction[1])

        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

    logger.debug(parse_char_array_to_string(grid))
    return count, grid

def check_direction(grid, direction, pos, value):
    while grid[pos[0]][pos[1]] != value:
        grid[pos[0]][pos[1]] = value
        npos = (pos[0] + direction[0], pos[1] + direction[1])
        logger.debug(f"Currently checking: {npos}")
        if npos[0] < 0 or npos[0] >= len(grid) or npos[1] < 0 or npos[1] >= len(grid[0]):
            return False
        if grid[npos[0]][npos[1]] == "#":
            direction = (direction[1], -direction[0])
            value = dir_map[direction[0]][direction[1]]
            npos = (pos[0] + direction[0], pos[1] + direction[1])
        pos = npos
    return True

def find_loops(grid):
    # find points where a right turn would put you back on the path
    # instead of Xs, put either U, D, L, or R (Up, Down, Left, Right)
    # if moving left, check for U's above, if right, D's below, etc

    pos = find_start(grid)
    direction = (-1, 0)
    count = 0

    grid[pos[0]][pos[1]] = "U"
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    logger.debug(parse_char_array_to_string(grid))
    while next_pos[0] >= 0 and next_pos[0] < len(grid) and next_pos[1] >= 0 and next_pos[1] < len(grid[0]):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        logger.debug(f"Current position: {pos}")
        logger.debug(f"Current direction: {direction}")
        logger.debug(f"Next position: {next_pos}")
        if grid[next_pos[0]][next_pos[1]] == "#":
            logger.debug("Wall! Turning right")
            direction = (direction[1], -direction[0])
            logger.debug(parse_char_array_to_string(grid))
            continue

        check_dir = check_dir_map[direction[0]][direction[1]]
        check_pos = (pos[0]+check_dir[0], pos[1]+check_dir[1])
        logger.debug(f"Checking position: {check_pos} for {check_dir[2]}. Has {grid[check_pos[0]][check_pos[1]]}")
        if check_direction(deepcopy(grid), (check_dir[0], check_dir[1]), deepcopy(pos), check_dir[2]):
            logger.debug(f"Found loop pos at {check_pos[0]}, {check_pos[1]}")
            grid[next_pos[0]][next_pos[1]] = "!"
            logger.debug(parse_char_array_to_string(grid))
            count += 1
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        grid[next_pos[0]][next_pos[1]] = dir_map[direction[0]][direction[1]]
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

    logger.debug(parse_char_array_to_string(grid))
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

    grid = parse_file_to_char_array(file)
    logger.print(grid)
    logger.print(map_patrol(deepcopy(grid)))

    logger.enable()
    logger.print(find_loops(grid))