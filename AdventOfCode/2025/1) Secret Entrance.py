import io

from Utils.parse_utils import parse_file_to_lines
from Utils.logger import logger

def find_zeroes(rotations: list[str]):
    combination = []
    curr = 50
    for rotation in rotations:
        value = int("".join(rotation[1:]))
        if rotation[0] == "L":
            value *= -1
        curr = (curr + value) % 100
        combination.append(curr)

    return combination.count(0)

def find_zeroes2(rotations: list[str]):
    curr = 50
    output = 0
    crotation = 0
    direction = rotations[0][0]

    def perform_rotation(direction, value):
        nonlocal output, curr
        wasZero = curr == 0
        logger.debug(f"Performing {direction} rotation of value {value}!")
        if value >= 100:
            logger.debug(f"Ping! Value {value} was >= 100, truncating")
            output += value // 100
            value = value % 100
        if value == 0:
            return
        if direction == "L":
            value *= -1
        curr = (curr + value)
        if curr <= 0 or curr >= 100:
            logger.debug(f"Ping! Curr wrapped around {abs(curr // 100)} times, value is {curr}")
            output += 1 if not wasZero else 0
        curr %= 100
        logger.debug(curr)

    for rotation in rotations:
        logger.debug()
        value = int("".join(rotation[1:]))
        ndirection = rotation[0]
        logger.debug(f"Output is {output}")

        if direction == ndirection:
            crotation += value
        else:
            perform_rotation(direction, crotation)

            direction = ndirection
            crotation = value

    perform_rotation(direction, crotation)

    return output

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""")

    try:
        file = open(filepath)
    except:
        pass

    logger.disable()
    lines = parse_file_to_lines(file)

    logger.print(find_zeroes2(lines))