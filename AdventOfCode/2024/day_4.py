from AdventOfCode.parse_utils import parse_file_to_char_array
from Utils.logger import logger

def filter_options(options, x, y):
    valid_options = []
    for option in options:
        valid = True
        for pos in option:
            if pos[0] < 0 or pos[0] >= x or pos[1] < 0 or pos[1] >= y:
                valid = False
                break
        if valid:
            valid_options.append(option)
    logger.print(f"Options are {valid_options}")
    return valid_options

def check_options(options, grid):
    count = 0
    for option in options:
        string = ""
        for pos in option:
            string += grid[pos[0]][pos[1]]
        logger.print(f"String is {string}")
        if string == "MAS":
            count += 1
    return count


def search_for_xmas(grid):
    output = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            char = grid[x][y]
            logger.print(char)
            if char == "X":
                options = [
                    [(x, y-1), (x, y-2), (x, y-3)], # up
                    [(x, y+1), (x, y+2), (x, y+3)], # down
                    [(x+1, y), (x+2, y), (x+3, y)], # right
                    [(x-1, y), (x-2, y), (x-3, y)], # left
                    [(x-1, y-1), (x-2, y-2), (x-3, y-3)],
                    [(x+1, y-1), (x + 2, y - 2), (x + 3, y - 3)],
                    [(x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)],
                    [(x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)],
                ]
                options = filter_options(options, len(grid), len(grid[x]))
                output += check_options(options, grid)
    return output

def search_for_x_mas(grid):
    output = 0
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[x])-1):
            char = grid[x][y]
            logger.print(char)
            if char == "A":
                logger.print("A Found!")
                tl, tr, bl, br = grid[x-1][y-1], grid[x+1][y-1], grid[x-1][y+1], grid[x+1][y+1]
                logger.print(tl + " " + tr)
                logger.print(" " + char + " ")
                logger.print(bl + " " + br)

                if tl + br in ["MS", "SM"] and tr + bl in ["MS", "SM"]:
                    logger.print("X-MAS found!")
                    output += 1
                else:
                    logger.print("X-MAS not found!")
    return output

if __name__  == "__main__":
    logger.enable()
    filepath = input("Input File Path")

    grid = [["M","M","M","S","X","X","M","A","S","M"],
            ["M","S","A","M","X","M","S","M","S","A"],
            ["A","M","X","S","X","M","A","A","M","M"],
            ["M","S","A","M","A","S","M","S","M","X"],
            ["X","M","A","S","A","M","X","A","M","M"],
            ["X","X","A","M","M","X","X","A","M","A"],
            ["S","M","S","M","S","A","S","X","S","S"],
            ["S","A","X","A","M","A","S","A","A","A"],
            ["M","A","M","M","M","X","M","M","M","M"],
            ["M","X","M","X","A","X","M","A","S","X"],
            ]
    try:
        with open(filepath) as file:
            grid = parse_file_to_char_array(file)
    except Exception as e:
        logger.print(e)
        pass

    print(search_for_xmas(grid))
    print(search_for_x_mas(grid))