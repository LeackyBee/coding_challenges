import io

from Utils.logger import logger

def parse_ranges(file):
    output = []

    for line in file:
        output = line.split(",")

    return output

def check_if_silly1(num):
    length = len(str(num))

    if length % 2 != 0:
        return False

    test = str(num)[:length//2] * 2
    logger.debug(f"Testing {test} against {num}")
    if test == str(num):
        logger.debug(f"{num} is silly!")
        return True
    return False

def check_if_silly2(num):
    length = len(str(num))

    for i in range(1,length//2+1):
        if length % i == 0:
            test = str(num)[:i] * (length // i)
            logger.debug(f"Testing {test} against {num}")
            if test == str(num):
                logger.debug(f"{num} is silly!")
                return True
    return False


def find_invalid(ranges):
    output = 0

    for srange in ranges:
        start, end = srange.split("-")
        start = int(start)
        end = int(end)

        for num in range(start, end+1):
            logger.debug(f"Testing {num}")
            if check_if_silly2(num):
                output += num

    return output

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""")

    try:
        file = open(filepath)
    except:
        pass

    logger.disable()
    lines = parse_ranges(file)

    logger.print(find_invalid(lines))