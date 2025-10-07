from Utils.logger import logger


def parse_file_to_list(file):
    output = []
    for line in file:
        output.append([int(x) for x in line.split(" ")])
    return output

def check_levels(levels):
    logger.print(f"Checking {levels} levels")
    if len(levels) < 2:
        # technically nothing wrong
        return True

    prev = levels[0]
    inc = (levels[1] - levels[0]) > 0
    for level in levels[1:]:
        diff = level - prev
        prev = level
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        elif (diff > 0) != inc:
            return False
    return True

def check_levels_with_dampener(levels):
    if len(levels) < 2:
        # technically nothing wrong
        return True
    logger.print(f"Checking {levels} with dampening")
    prev = levels[0]
    inc = (levels[1] - levels[0]) > 0
    logger.print(f"{"Increasing" if inc else "Decreasing"}")
    used_dampener = False
    for i in range(1, len(levels[1:])+1):
        level = levels[i]
        diff = level - prev
        logger.print(prev)
        logger.print(level)
        error = abs(diff) < 1 or abs(diff) > 3 or ((diff > 0) != inc)
        if error and not used_dampener:
            logger.print("Error Dampened")
            # check if removing the previous one fixes the error or if removing the one before that does
            # Does sadly mean this is checking each input 1 (no dampener needed) or 3 times.
            if check_levels(levels[:i-1] + levels[i:]) or check_levels(levels[:i-2] + levels[i-1:]):
                return True
            used_dampener = True
        elif error:
            return False
        else:
            prev = level
    return True

def boring(levels):
    for i in range(len(levels)):
        if check_levels(levels[:i] + levels[i+1:]):
            return True
    return False

def count_valid_levels(levels_list, dampening):
    count = 0
    function = check_levels
    if dampening:
        function = check_levels_with_dampener
    for levels in levels_list:
        valid = function(levels)
        print(f"{levels} is {"valid" if valid else "not valid"}")
        count += 1 if valid else 0
    return count

if __name__  == "__main__":
    logger.enable()
    filepath = input("Input File Path")

    list = [
        [7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9],
        [71, 69, 70, 71, 72, 75],
        [69, 70, 71, 72, 75, 790],
        [19, 21, 24, 27, 24],
        [3, 1, 2, 3, 4, 5],
        [93, 92, 91, 90, 88],
        [87, 90, 93, 94, 98],
        [51, 53, 54, 55, 57, 60, 63, 63],
        [27, 29, 30, 33, 34, 35, 37, 35],
        [8, 6, 4, 4, 1],
        [71, 69, 70, 69, 66],
        [1, 2, 3, 4, 3, 4],
        [1, 3, 5, 10, 1],
        [10, 4, 3, 2, 1],
        [1, 7, 4, 0, 5],
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    list = [
        [12, 10, 11, 13, 15, 18, 20],
        [56, 59, 58, 55, 53, 51, 49, 48],
        [42, 40, 41, 44, 45, 47],
        [83, 86, 85, 84, 81, 79, 78],
        [88, 85, 88, 89, 92, 95],
    ]
    try:
        with open(filepath) as file:
            list = parse_file_to_list(file)
    except:
        pass

    #print(f"There are {count_valid_levels(list, False)} valid levels")
    print(f"There are {count_valid_levels(list, True)} valid levels with Dampening")
