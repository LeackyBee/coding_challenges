import io

from Utils.parse_utils import parse_matrix_to_string
from Utils.logger import logger
from Utils.matrix_utils import step


def parse_file(file):
    grid = []
    for line in file:
        line = line.strip()
        if not line:
            break
        grid.append(list(line))
    instructions = []
    for line in file:
        line = line.strip()
        instructions.extend(list(line))
    return grid, instructions

def parse_file_double_wide(file):
    grid = []
    for line in file:
        line = line.strip()
        if not line:
            break
        chars = list(line)
        print(chars)
        dchars = []
        for char in chars:
            if char == ".":
                dchars.extend([".", "."])
            if char == "O":
                dchars.extend(["[", "]"])
            if char == "@":
                dchars.extend(["@", "."])
            if char == "#":
                dchars.extend(["#", "#"])
        grid.append(dchars)
    instructions = []
    for line in file:
        line = line.strip()
        instructions.extend(list(line))
    return grid, instructions

def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                return i, j
    return None

def map_direction(char):
    return {"^": (-1,0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[char]

def is_move_possible(grid, npos, direction):
    # returns whether the move is possible, and where the next free space is
    if grid[npos[0]][npos[1]] == "#":
        # if the next tile is a wall, can't move
        return False, None
    elif grid[npos[0]][npos[1]] == ".":
        return True, npos
    elif grid[npos[0]][npos[1]] == "O":
        npos = step(npos, direction)
        logger.debug(f"Wall, attempting to move to {npos}")
        return is_move_possible(grid, npos, direction)
    return None, None


def simulate_robot(grid, instructions):
    pos = find_robot(grid)

    for instruction in instructions:
        logger.debug(f"Move = {instruction}")
        direction = map_direction(instruction)
        npos = step(pos, direction)
        logger.debug(f"Attempting to move to {npos}")
        possible, free = is_move_possible(grid, npos, direction)
        logger.debug(free)
        if possible:
            grid[npos[0]][npos[1]] = "@"
            grid[pos[0]][pos[1]] = "."
            if npos != free:
                # if this has happened, the free space is behind a box, so we're pushing a box into it
                grid[free[0]][free[1]] = "O"
            pos = npos
        logger.debug(parse_matrix_to_string(grid))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                count += 100*i + j
    return count

def is_move_possible_doublewide(grid, npos, direction):
    # returns whether the move is possible, and where the next free space is
    if grid[npos[0]][npos[1]] == "#":
        # if the next tile is a wall, can't move
        return False, None
    elif grid[npos[0]][npos[1]] == ".":
        return True, npos
    elif grid[npos[0]][npos[1]] == "[":
        nposl = npos
        nposr = step(npos, (0,1))

        nposl = step(nposl, direction)
        nposr = step(nposr, direction)

        logger.debug(f"Wall, attempting to move to {npos}")
        return is_move_possible(grid, npos, direction)
    return None, None

def simulate_robot_doublewide(grid, instructions):
    pos = find_robot(grid)

    for instruction in instructions:
        logger.debug(f"Move = {instruction}")
        direction = map_direction(instruction)
        npos = step(pos, direction)
        logger.debug(f"Attempting to move to {npos}")
        possible, free = is_move_possible_doublewide(grid, npos, direction)
        logger.debug(free)
        if possible:
            grid[npos[0]][npos[1]] = "@"
            grid[pos[0]][pos[1]] = "."
            if npos != free:
                # if this has happened, the free space is behind a box, so we're pushing a box into it
                grid[free[0]][free[1]] = "O"
            pos = npos
        logger.debug(parse_matrix_to_string(grid))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                count += 100*i + j
    return count


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""")

    file = io.StringIO("""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""")

    try:
        file = open(filepath)
    except:
        pass

    grid, instructions = parse_file(file)
    logger.print(parse_matrix_to_string(grid))
    logger.print(instructions)
    logger.print(f"Sum of box coordinates = {simulate_robot(grid, instructions)}")

    file.seek(0)
    grid, instructions = parse_file_double_wide(file)
    logger.print(parse_matrix_to_string(grid))
    logger.print(instructions)