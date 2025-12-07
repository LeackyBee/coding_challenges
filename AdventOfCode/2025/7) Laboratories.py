import io

from Utils.logger import logger
from Utils.matrix_utils import step, within_bounds
from Utils.parse_utils import parse_file_to_char_matrix

def simulate(grid):
    frontier = set()
    timelines = [[0 for _ in grid[0]] for _ in grid]

    done = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                frontier.add((i, j))
                timelines[i][j] = 1
                done = True
                break
        if done:
            break

    splits = 0
    while frontier:
        logger.debug()
        logger.debug(frontier)
        nfrontier = set()
        for node in frontier:
            next = step(node, (1, 0))
            if within_bounds(grid, next):
                if grid[next[0]][next[1]] == "^":
                    splits += 1
                    nfrontier.add((next[0], next[1]+1))
                    timelines[next[0]][next[1]+1] += timelines[node[0]][node[1]]

                    nfrontier.add((next[0], next[1]-1))
                    timelines[next[0]][next[1]-1] += timelines[node[0]][node[1]]
                else:
                    nfrontier.add(next)
                    timelines[next[0]][next[1]] += timelines[node[0]][node[1]]
        logger.debug(nfrontier)
        frontier = nfrontier

    timeline_count = sum(timelines[-1])

    return splits, timeline_count


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO(""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""")

    try:
        file = open(filepath)
    except:
        pass

    grid = parse_file_to_char_matrix(file)

    logger.enable()

    splits, timelines = simulate(grid)

    logger.print(f"Tachyon beam splits {splits} times")
    logger.print(f"There are {timelines} timelines")