import io
from math import prod

from Utils.logger import logger
from Utils.parse_utils import parse_file_to_str_matrix_with_sep, parse_file_to_char_matrix


def solve_problems(lines):
    output = []
    for question in zip(*lines[:-1], lines[-1]):
        op = question[-1]
        operands = question[:-1]
        operands = [int(x) for x in operands]
        logger.debug()
        logger.debug(operands)
        logger.debug(op)
        match op:
            case "*":
                output.append(prod(operands))
            case "+":
                output.append(sum(operands))

    return sum(output)


def parse_columnar_problems(lines: list[list[str]]):
    output = []
    operands = []
    op = " "
    for line in lines:
        # add a sentinel
        line.insert(0, " ")

    for i in range(len(lines[-1])-1, -1, -1):
        vals = [line[i] for line in lines]
        if "".join(vals[:-1]).strip() == "":
            # no values in any column, so we're between problems
            logger.debug()
            logger.debug(operands)
            logger.debug(op)
            match op:
                case "*":
                    val = prod(operands)
                case "+":
                    val = sum(operands)
            logger.debug(val)
            output.append(val)
            operands = []
            op = " "
        else:
            if op == " ":
                op = vals[-1]
            num = 0
            for digit in vals[:-1]:
                if digit.isdigit():
                    num = num*10 + int(digit)
            operands.append(num)
    return sum(output)


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    example = io.StringIO("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """)

    try:
        file = open(filepath)
    except:
        file = example

    problem1_lines = parse_file_to_str_matrix_with_sep(file, " ")

    logger.disable()
    logger.print(f"Part 1 answer = {solve_problems(problem1_lines)}")

    file.seek(0)

    logger.print(f"Part 2 answer = {parse_columnar_problems(parse_file_to_char_matrix(file, strip=False))}")