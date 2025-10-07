import io

from Utils.Logger import logger

"""
This one was pretty easy, you just treat it like a breadth first search and each operation as an edge
"""

def parse(file):
    output = []
    for line in file:
        target, vals = line.split(": ")
        vals = vals.split(" ")
        output.append([int(target), [int(x) for x in vals]])
    return output

def check_equations(equations):
    output = 0

    for equation in equations:
        target = equation[0]
        vals = equation[1]
        curr = [vals[0]]
        for val in vals[1:]:
            logger.debug(curr)
            ncurr = []
            for prev in curr:
                ncurr.append(prev + val)
                ncurr.append(prev * val)
            curr = ncurr
        if target in curr:
            output += target
    return output

def check_equations_2(equations):
    output = 0

    for equation in equations:
        target = equation[0]
        vals = equation[1]
        curr = [vals[0]]
        for val in vals[1:]:
            logger.debug(curr)
            ncurr = []
            for prev in curr:
                ncurr.append(prev + val)
                ncurr.append(prev * val)
                ncurr.append(int(str(prev) + str(val)))
            curr = ncurr
        if target in curr:
            output += target
    return output


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO(
"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""")

    try:
        file = open(filepath)
    except:
        pass

    equations = parse(file)
    logger.enable()

    logger.print(equations)
    logger.print(check_equations(equations))
    logger.print(check_equations_2(equations))