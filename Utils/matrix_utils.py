def step(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def within_bounds(grid, pos):
    return pos[0] >=0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])
