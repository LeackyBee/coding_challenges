def step(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def within_bounds(grid, pos):
    return pos[0] >=0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

def get_valid_neighbours(grid, i, j):
    neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    neighbours = [x for x in neighbours if within_bounds(grid, x)]
    return neighbours