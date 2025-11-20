import io

from Utils.parse_utils import parse_file_to_int_array
from Utils.logger import logger

"""
This one is fairly easy too, just maintain a list of
"""

def iterate_stones(stones, blinks):

    for i in range(blinks):
        ninput = []
        logger.print(f"Blink {i}, stones: {stones}")
        for stone in stones:
            string = str(stone)
            if stone == 0:
                ninput.append(1)
            elif len(string) % 2 == 0:
                left = int(string[:len(string)//2])
                right = int(string[len(string)//2:])
                ninput.append(left)
                ninput.append(right)
            else:
                ninput.append(stone * 2024)
        stones = ninput
    return len(stones)

def iterate_stones(stones, blinks):
    seen = set()
    for i in range(blinks):
        ninput = []
        logger.print(f"Blink {i}, stones: {stones}")
        seenAll = True
        for stone in stones:
            if stone not in seen:
                seenAll = False
                seen.add(stone)
            string = str(stone)
            if stone == 0:
                ninput.append(1)
            elif len(string) % 2 == 0:
                left = int(string[:len(string)//2])
                right = int(string[len(string)//2:])
                ninput.append(left)
                ninput.append(right)
            else:
                ninput.append(stone * 2024)
        stones = ninput
        if seenAll:
            break
    return len(stones)


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""125 17""")
    file = io.StringIO("""0""")

    try:
        file = open(filepath)
    except:
        pass

    stones = parse_file_to_int_array(file)

    logger.enable()
    logger.print(f"Stones: {stones}")
    logger.print(f"After 25 blinks, you have {iterate_stones(stones, 25)}")
