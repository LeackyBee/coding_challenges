import io

from Utils import parse_utils
from Utils.logger import logger


def min_potions_needed(enemies: str):
    potions_needed = {
        "A": 0,
        "B": 1,
        "C": 3
    }

    output = 0

    for enemy in enemies:
        output += potions_needed[enemy]

    return output

def min_potions_needed_paired_enemies(enemies: str):
    potions_needed = {
        "A": 1,
        "B": 2,
        "C": 4,
        "D": 6,
        "x": -1
    }

    output = 0

    for i in range(0, len(enemies), 2):
        enemy1 = enemies[i]
        enemy2 = enemies[i+1]
        if enemy1 + enemy2 == "xx":
            continue

        output += potions_needed[enemy1]
        output += potions_needed[enemy2]

    return output

def min_potions_needed_trio_enemies(enemies: str):
    potions_needed = {
        "A": 2,
        "B": 3,
        "C": 5,
        "D": 7,
        "x": 0
    }

    output = 0

    for i in range(0, len(enemies), 3):
        enemy1 = enemies[i]
        enemy2 = enemies[i+1]
        enemy3 = enemies[i+2]
        group = enemy1 + enemy2 + enemy3
        if group == "xxx":
            continue

        output += potions_needed[enemy1]
        output += potions_needed[enemy2]
        output += potions_needed[enemy3]

        if "x" in group:
            # if we have xCC - need to subtract 1 from both C's => -2
            # if we have xxC - need to subtract 2 from the C => -2
            # xxx filtered out above
            output -= 2

    return output


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("ABBAC")
    file = io.StringIO("AxBCDDCAxD")
    file = io.StringIO("xBxAAABCDxCC")

    try:
        file = open(filepath)
    except:
        pass

    enemies = parse_utils.parse_file_to_line(file)

    logger.enable()
    logger.print(enemies)
    min_potions = min_potions_needed_trio_enemies(enemies)
    logger.print(min_potions)