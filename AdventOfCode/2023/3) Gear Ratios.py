import io
from curses.ascii import isdigit

from Utils.parse_utils import parse_file_to_char_matrix
from Utils.logger import logger
from Utils.matrix_utils import within_bounds, get_valid_neighbours

"""
Parse to grid of characters
scan over grid, on first digit start adding to neighbours list
on non-digits, 
"""


def find_part_numbers(grid):
    output = []
    for i in range(len(grid)):
        neighbours = set()
        num = 0
        for j in range(len(grid[i])):
            char = grid[i][j]
            logger.debug(char)
            if isdigit(char):
                # building up neighbour locations
                num = num*10 + int(char)
                neighbours = neighbours.union(get_valid_neighbours(grid, i, j, True))
                logger.debug(f"Number now {num}, neighbours {neighbours}")
            elif neighbours:
                # stopped building neighbour locations, time to check
                logger.debug(f"Checking neighbours for {num} at pos {i} and {j}")
                for n in neighbours:
                    logger.debug(f"Checking neighbour {n}")
                    if within_bounds(grid, n):
                        if (not (isdigit(grid[n[0]][n[1]]) or grid[n[0]][n[1]] == ".")):
                            # symbol found
                            logger.debug(f"Number found! {num}")
                            output.append(num)
                            logger.debug(f"Output now {output}")
                            break
                num = 0
                neighbours.clear()

    return sum(output)

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)
    logger.enable()
    logger.print(find_part_numbers(grid))