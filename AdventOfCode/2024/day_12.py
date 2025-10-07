import io
from copy import deepcopy

from AdventOfCode.parse_utils import parse_file_to_char_matrix, parse_char_array_to_string, parse_int_array_to_string
from Utils.logger import logger
from Utils.matrix_utils import get_all_neighbours, within_bounds

"""
Idea:
Iterate over the grid
Assign regions a increasing numerical id
Regions are stores as <id, [area nodes, perimeter nodes]>
Every time a new letter is found, initialise the map with the lists and the first node
Then enter a new method where a bfs is performed on the region. Only allowed to traverse to nodes with the same letter
Traversed nodes go to the area nodes, neighbour nodes that we don't allow traversal to go to the perimeter nodes
Assign each traversed node the id in the grid, this marks it as explored

For part 2:
Each grid cell is a list
Iterate over the perimeters for each region, add the region id to the list
Traverse in one direction until you hit something that isn't the id, then turn in the direction of the next tile with the id
Each iteration, pop from the list to mark as visited
Each turn you start a new line

Assertions
Always at most one neighbour has the id NOPE
Corners don't exist
If we find a non-empty list, it must have only 1 id in it. 
- Intuition here is that we've explored all higher regions, and all nodes to the left. 
- Only direction possible is down and to the right, and we can't have two regions going that way

hours later...

Instead, lets find
"""

def explore_region(grid, i, j, id):
    letter = grid[i][j]
    perimeter = []
    area = {(i, j)}
    frontier = [(i,j)]
    logger.debug(parse_int_array_to_string(grid))
    while frontier:
        logger.debug()

        nfrontier = []
        for node in frontier:
            # mark as explored
            grid[node[0]][node[1]] = id
            neighbours = get_all_neighbours(node[0], node[1])
            for neighbour in neighbours:
                # edge or different region
                if (not within_bounds(grid, neighbour)) or grid[neighbour[0]][neighbour[1]] not in [letter, id]:
                    perimeter.append(neighbour)
                elif neighbour not in area:
                    area.add(neighbour)
                    nfrontier.append(neighbour)
        frontier = nfrontier
        logger.debug(parse_int_array_to_string(grid))
    logger.debug()
    return perimeter, area

def find_regions(grid):
    regions = {}
    next_id = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if value is not None, the tile has not been explored
            if type(grid[i][j]) is not int:
                regions[next_id] = explore_region(grid, i, j, next_id)
                logger.debug(parse_int_array_to_string(grid))
                logger.debug()
                next_id += 1
    return regions

def find_fence_costs(grid):
    regions = find_regions(grid)
    logger.debug(f"regions: {regions}")
    cost = 0
    for region in regions:
        logger.debug(f"region: {region} has perimeter {len(regions[region][0])} and area {len(regions[region][1])}")
        cost += len(regions[region][0]) * len(regions[region][1])
    return cost

def mark_perimeters(grid, regions):
    # make new grid that includes outer edges
    grid = [[[]]*(len(grid[0])+2)] * (len(grid)+2)

    for region in regions:
        perimeter = regions[region][0]
        for node in perimeter:
            # offset to allow for the edge
            nnode = (node[0]+1, node[1]+1)
            if region not in grid[nnode[0]][nnode[1]]:
                grid[nnode[0]][nnode[1]].append(region)
        logger.debug(f"Marked {region}")
        logger.debug(parse_int_array_to_string(grid))
    return grid



def find_lines(grid):
    regions = find_regions(grid)
    grid = mark_perimeters(grid, regions)

    logger.debug("Marked Perimeters")
    logger.debug(parse_int_array_to_string(grid))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                # non-empty list means there's a region perimeter here
                pass


def traverse_perimeter(grid, i, j, id):
    lines = []
    pos = (i, j)
    line = []

    while True:
        line.append(pos)
        grid[pos[0]][pos[1]].remove(id)

        neighbours = get_all_neighbours(pos[0], pos[1])
        for neighbour in neighbours:
            pass # todo





if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)
    #logger.print(find_fence_costs(grid))
    logger.enable()
    logger.print(find_lines(grid))