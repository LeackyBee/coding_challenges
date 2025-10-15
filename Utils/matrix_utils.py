def step(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def within_bounds(grid, pos):
    return pos[0] >=0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

def get_valid_neighbours(grid, i, j, diagonals=False):
    neighbours = get_all_neighbours(i, j, diagonals)
    neighbours = [x for x in neighbours if within_bounds(grid, x)]
    return neighbours

def get_all_neighbours(i, j, diagonals=False):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] + ([(i+1,j+1),(i-1,j+1),(i+1,j-1),(i-1,j-1)] if diagonals else [])

def turn_right(direction, count=1):
    output = direction
    for i in range(count):
        output = (output[1], -output[0])
    return output

def turn_left(direction, count=1):
    output = direction
    for i in range(count):
        output = (-output[1], output[0])
    return output


def init_matrix(i,j, init_value=None):
    return [[init_value for _ in range(j)] for _ in range(i)]