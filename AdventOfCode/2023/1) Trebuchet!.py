import io
from curses.ascii import isdigit

from Utils.parse_utils import parse_file_to_lines
from Utils.logger import logger

"""
Part 1 super easy

For part 2 need to preprocess the line to convert words into numbers and then run through the same code
"""

def find_calibration(lines):
    output = []
    for line in lines:
        ints = [int(x) for x in list(line) if isdigit(x)]
        output.append(ints[0]*10 + ints[-1])

    return sum(output)

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")

    try:
        file = open(filepath)
    except:
        pass

    lines = parse_file_to_lines(file)

    logger.print(find_calibration(lines))