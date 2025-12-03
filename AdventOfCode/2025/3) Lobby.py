import io
from curses.ascii import isdigit
from typing import List

from Utils.parse_utils import parse_file_to_lines
from Utils.logger import logger



def findMaxJoltage(banks:List[str], batteries:int):
    output = 0
    for bank in banks:
        prevI = -1
        joltage = ""
        for i in range(batteries-1, -1, -1):
            maxBattery = "0"
            for i in range(prevI+1, len(bank) - i):
                if bank[i] > maxBattery:
                    maxBattery = bank[i]
                    prevI = i
                    if maxBattery == "9":
                        break
            joltage += maxBattery
        logger.debug(f"Max for {"".join(bank)} is {joltage}")
        output += int(joltage)

    return output



if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""987654321111111
811111111111119
234234234234278
818181911112111""")

    try:
        file = open(filepath)
    except:
        pass

    logger.enable()
    lines = parse_file_to_lines(file)

    logger.print(findMaxJoltage(lines, 12))