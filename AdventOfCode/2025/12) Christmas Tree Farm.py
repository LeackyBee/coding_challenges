import io

from Utils.logger import logger
from Utils.parse_utils import parse_file_to_lines

def parse_lines(lines):
    shapes = {}
    i = 0
    for _ in range(6):
        num = lines[i][0]
        t = lines[i+1]
        m = lines[i+2]
        b = lines[i+3]

        shapes[int(num)] = [t,m,b]
        i += 5

    trees = []
    while i < len(lines):
        dimensions, presents = "".join(lines[i]).split(": ")
        x, y = [int(x) for x in dimensions.split("x")]
        presents = [int(x) for x in presents.split(" ")]
        trees.append(((x,y),presents))
        i += 1

    return shapes, trees

def fit_presents(shapes, trees):
    output = 0
    for tree in trees:
        (x,y), presents = tree
        total_presents = sum(presents)
        slots = (x//3) * (y//3)
        
        if total_presents <= slots:
            # trivially possible
            output += 1
            continue

        total_space_needed = total_presents * 7
        total_space_available = x * y

        if total_space_needed > total_space_available:
            # trivially impossible
            continue

        output += 1
    return output



if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""")

    try:
        file = open(filepath)
    except:
        pass

    lines = parse_file_to_lines(file)

    shapes, trees = parse_lines(lines)

    logger.print(fit_presents(shapes, trees))