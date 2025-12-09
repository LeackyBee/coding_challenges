import heapq
import io

from Utils.logger import logger
from Utils.parse_utils import parse_file_to_char_matrix

def parse_file_to_coords(file):
    output = []
    for line in file:
        X, Y = line.split(",")
        output.append((int(X),int(Y)))
    return output

def find_area(A, B):
    return (abs(A[0] - B[0]) + 1) * (abs(A[1] - B[1]) + 1)

def find_rectangles(coords):
    max_area = 0
    for A in coords:
        for B in coords:
            curr = find_area(A,B)
            max_area = max(curr, max_area)
    return max_area

def between(A, B, X):
    max_i = max(A[0], B[0])
    max_j = max(A[1], B[1])
    min_i = min(A[0], B[0])
    min_j = min(A[1], B[1])

    return (min_i < X[0] < max_i) and (min_j < X[1] < max_j)

def find_rectangles_2(coords):
    """
    General approach here is to compute all the edge tiles in a hashset
    Then, we iterate over all rectangles and filter this set for nodes inside the rectangle
    If none are found, we compute the size
    """
    # TODO - can maybe be replaced by a DIET
    edge_tiles = set()

    for i in range(len(coords)):
        prev = coords[i-1]
        curr = coords[i]
        if prev[0] == curr[0]:
            min_j = min(prev[1], curr[1])
            max_j = max(prev[1], curr[1])
            points = [(prev[0], x) for x in range(min_j, max_j+1)]
        else:
            min_i = min(prev[0], curr[0])
            max_i = max(prev[0], curr[0])
            points = [(x, prev[1]) for x in range(min_i, max_i + 1)]

        logger.debug(f"Points between {prev} and {curr}")
        logger.debug(points)
        logger.debug()
        edge_tiles.update(points)

    logger.debug(f"Final set of edge_tiles {edge_tiles}")

    sizes = []

    for A in coords:
        for B in coords:
            if A == B:
                continue
            sizes.append((-find_area(A,B), A, B))

    heapq.heapify(sizes)

    while sizes:
        logger.debug()
        size, A, B = heapq.heappop(sizes)
        size *= -1 # heapq is a minheap, so sizes were negative
        logger.debug(f"Inspecting {A}, {B} with size {size}")
        internal_vertices = [x for x in coords if between(A, B, x)]
        logger.debug(f"{internal_vertices} lie between {A} and {B}")
        if internal_vertices:
            continue

        mid_j = int((A[1] + B[1])/2)
        td_path = set([(x, mid_j) for x in range(min(A[0], B[0])+1, max(A[0], B[0]))])
        logger.debug(f"Edge tiles: {edge_tiles}")
        logger.debug(f"Vertical path is {td_path}")
        error = False
        for node in td_path:
            if node in edge_tiles:
                logger.debug(f"{node} was an edge")
                error = True
                break
        if error: continue

        mid_i = int((A[0] + B[0]) / 2)
        lr_path = set([(mid_i, x) for x in range(min(A[1], B[1])+1, max(A[1], B[1]))])
        logger.debug(f"Horizontal path is {lr_path}")

        for node in lr_path:
            if node in edge_tiles:
                logger.debug(f"{node} was an edge")
                error = True
                break
        if error: continue

        return size


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""1,7
    1,11
    7,11
    7,9
    5,9
    5,2
    3,2
    3,7""")

    try:
        file = open(filepath)

    except:
        pass

    coords = parse_file_to_coords(file)

    logger.disable()
    logger.print(f"1) The largest rectangle has an area of {find_rectangles(coords)}")
    logger.print(f"2) The largest rectangle has an area of {find_rectangles_2(coords)}")