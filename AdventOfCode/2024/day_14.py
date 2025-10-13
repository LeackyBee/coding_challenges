import io
from math import floor

from AdventOfCode.parse_utils import parse_matrix_to_string
from Utils.logger import logger
from Utils.matrix_utils import step

"""

"""

def parse_robots(file):
    output = []
    logger.debug(f"Parsing robots file: {file}")
    for line in file:
        p, v = line.split(" ")
        pos = [int(x) for x in p[2:].split(",")]
        velocity = [int(x) for x in v[2:].split(",")]
        output.append([pos,velocity])
    return output

def wrap_edges(pos, max_x, max_y):
    return [pos[0] % max_x, pos[1] % max_y]

def get_display(robots, max_x, max_y):
    grid = [[" " for _ in range(max_x)] for _ in range(max_y)]
    for robot in robots:
        grid[robot[0][1]][robot[0][0]] = "#"
    logger.debug(parse_matrix_to_string(grid))

def iterate_robots(robots, max_x, max_y, seconds=100):
    logger.debug(f"Iterating robots: {robots}")
    for i in range(seconds):
        logger.debug(f"Seconds: {i}")
        for robot in robots:
            logger.debug(f"Iterating robot: {robot}")
            pos = robot[0]
            vel = robot[1]
            npos = step(pos, vel)
            robot[0] = wrap_edges(npos, max_x, max_y)
        get_display(robots, max_x, max_y)

    quadrants = {(True, True): [], (True, False): [], (False, True): [], (False, False): []}

    logger.debug(f"Iteration done, checking positions!")
    for robot in robots:
        logger.debug(f"Checking robot: {robot}")
        middle = (robot[0][0] == (max_x-1)/2) or (robot[0][1] == (max_y-1)/2)
        if middle:
            logger.debug(f"Middle position: {robot}")
            continue
        left = robot[0][0] <( max_x-1) / 2
        top = robot[0][1] < (max_y-1) / 2
        quadrants[(left, top)].append(robot)

    factor = 1
    for quadrant in quadrants:
        factor *= len(quadrants[quadrant])

    return factor




if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""")

    try:
        file = open(filepath)
    except:
        pass
    logger.enable()
    robots = parse_robots(file)
    logger.print(f"Parsed robots: {robots}")
    logger.print(f"Safety Factor robots: {iterate_robots(robots, 101, 103, 100)}")