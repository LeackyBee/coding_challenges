import io

from Utils.parse_utils import parse_file_to_int_matrix_with_sep, parse_matrix_to_string

def maxPath(grid):

    prev_row = [0 for _ in range(len(grid[-1]))]
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        for j in range(len(row)-1):
            row[j] = max(row[j] + prev_row[j], row[j+1]+prev_row[j+1])

        prev_row = row

    print(parse_matrix_to_string(grid, sep=" "))
    print(grid[0][0] + max(grid[1]))




if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = open(filepath)

    grid = parse_file_to_int_matrix_with_sep(file, sep=" ")
    maxPath(grid)