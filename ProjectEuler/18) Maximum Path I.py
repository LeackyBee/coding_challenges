import io

from Utils.parse_utils import parse_file_to_int_matrix_with_sep, parse_matrix_to_string

grid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

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
    grid = io.StringIO(grid)
    grid = parse_file_to_int_matrix_with_sep(grid, sep=" ")
    maxPath(grid)