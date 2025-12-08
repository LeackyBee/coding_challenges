import heapq
import io
import math

from Utils.logger import logger

def parse_file_to_coords(file):
    output = []
    for line in file:
        X, Y, Z = line.split(",")
        output.append((int(X),int(Y),int(Z)))
    return output

def get_distance(A, B):
    return math.sqrt((B[0]-A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)

def get_1000_shortest(coords, connections):
    heap = []

    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            A = coords[i]
            B = coords[j]
            distance = get_distance(A,B)

            heapq.heappush(heap, (-distance, (A,B)))
            if len(heap) > connections:
                heapq.heappop(heap)

    groups = {i:[node] for i, node in enumerate(coords)}
    node_to_group = {node:i for i, node in enumerate(coords)}
    # at this point, ordering isn't relevant, so can ditch the heap principle
    for _, (A,B) in heap:
        logger.debug()
        logger.debug(groups)
        logger.debug(node_to_group)
        group_id_A = node_to_group[A]
        group_id_B = node_to_group[B]
        if group_id_A == group_id_B:
            continue
        group_B = groups[group_id_B]

        for node in group_B:
            logger.debug(f"Adding {node} to {group_id_A}")
            node_to_group[node] = group_id_A
            groups[group_id_A].append(node)

        groups.pop(group_id_B)

    largest = [len(x) for x in groups.values()]
    largest = sorted(largest)

    return largest[-1] * largest[-2] * largest[-3]

def get_fully_connected(coords):
    heap = []

    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            A = coords[i]
            B = coords[j]
            distance = get_distance(A,B)

            heapq.heappush(heap, (distance, (A,B)))

    groups = {i:[node] for i, node in enumerate(coords)}
    node_to_group = {node:i for i, node in enumerate(coords)}
    output = 0
    while len(groups) > 1:
        _, (A, B) = heapq.heappop(heap)
        logger.debug()
        logger.debug(groups)
        logger.debug(node_to_group)
        group_id_A = node_to_group[A]
        group_id_B = node_to_group[B]
        if group_id_A == group_id_B:
            continue
        output = A[0] * B[0]
        group_B = groups[group_id_B]

        for node in group_B:
            logger.debug(f"Adding {node} to {group_id_A}")
            node_to_group[node] = group_id_A
            groups[group_id_A].append(node)

        groups.pop(group_id_B)

    return output

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""")

    try:
        file = open(filepath)
        connections = 1000
    except:
        connections = 10

    coords = parse_file_to_coords(file)

    logger.disable()
    logger.print(f"After {connections} connections, largest 3 group sizes multiply to get {get_1000_shortest(coords, connections)}")
    logger.print(f"The X-coords of the last 2 boxes needed for the MST multiply to {get_fully_connected(coords)}")