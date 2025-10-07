import io

from AdventOfCode.parse_utils import parse_file_to_char_array
from Utils.logger import logger
from Utils.matrix_utils import within_bounds

"""
Get a map with the frequency as the key, and a list of positions of antennae with that frequency
Match each antenna with each other of the same frequency
Find the difference D (A-B) between their positions
Antinode at A + D and at B - D
Add to seen if they are within bounds
Return len(seen)

For part 2:
Get a map with the frequency as the key, and a list of positions of antennae with that frequency
Match each antenna with each other of the same frequency
Find the difference D (A-B) between their positions
Antinode at A
Keep adding D until it's out of bounds, each iteration adding to seen
Antinode at B
Keep adding D until it's out of bounds, each iteration adding to seen
Return len(seen)
"""

def find_antennae_positions(grid):
    output = {}
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            cell = row[j]
            if cell != ".":
                curr = output.get(cell, [])
                curr.append((i, j))
                output[cell] = curr
    return output

def find_antinodes(grid):
    antennae = find_antennae_positions(grid)
    seen = set()
    for frequency, positions in antennae.items():
        logger.print(f"Frequency: {frequency}")
        for i in range(len(positions)-1):
            for j in range(i+1,len(positions)):
                A = positions[i]
                B = positions[j]
                logger.print(f"A: {A}, B: {B}")
                D = (A[0] - B[0], A[1] - B[1])

                antinode1 = (A[0] + D[0], A[1] + D[1])
                antinode2 = (B[0] - D[0], B[1] - D[1])
                logger.print(f"Antinode1: {antinode1}, Antinode2: {antinode2}")
                if within_bounds(grid, antinode1):
                    seen.add(antinode1)
                if within_bounds(grid, antinode2):
                    seen.add(antinode2)
    return len(seen)

def find_antinodes_with_resonance(grid):
    antennae = find_antennae_positions(grid)
    seen = set()
    for frequency, positions in antennae.items():
        logger.print(f"Frequency: {frequency}")
        for i in range(len(positions)-1):
            for j in range(i+1,len(positions)):
                A = positions[i]
                B = positions[j]
                logger.print(f"A: {A}, B: {B}")
                D = (A[0] - B[0], A[1] - B[1])

                antinode = A
                while within_bounds(grid, antinode):
                    seen.add(antinode)
                    antinode = (antinode[0] + D[0], antinode[1] + D[1])

                antinode = B
                while within_bounds(grid, antinode):
                    seen.add(antinode)
                    antinode = (antinode[0] - D[0], antinode[1] - D[1])
    return len(seen)

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO(
        """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""")


    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_array(file)
    logger.enable()
    logger.print(find_antinodes(grid))
    logger.print(find_antinodes_with_resonance(grid))

