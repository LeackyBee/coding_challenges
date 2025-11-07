from typing import List


class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # initialise grid
        grid = [[1 for _ in range(n)] for _ in range(m)]
        total = m * n - len(guards) - len(walls)
        if total == 0:
            return total
        for cell in walls + guards:  # can treat guards and walls the same way
            grid[cell[0]][cell[1]] = None

        for guard in guards:

            # -> right
            for i in range(guard[0] + 1, m):
                cell = [i, guard[1]]
                if grid[cell[0]][cell[1]] is None:
                    # hit a wall or another guard
                    break
                # mark as observed
                if grid[cell[0]][cell[1]] != 0:
                    grid[cell[0]][cell[1]] = 0
                    total -= 1

            # left <-
            for i in range(guard[0] - 1, -1, -1):
                cell = [i, guard[1]]
                if grid[cell[0]][cell[1]] is None:
                    # hit a wall or another guard
                    break
                # mark as observed
                if grid[cell[0]][cell[1]] != 0:
                    grid[cell[0]][cell[1]] = 0
                    total -= 1

            # up ^
            for i in range(guard[1] + 1, n):
                cell = [guard[0], i]
                if grid[cell[0]][cell[1]] is None:
                    # hit a wall or another guard
                    break
                # mark as observed
                if grid[cell[0]][cell[1]] != 0:
                    grid[cell[0]][cell[1]] = 0
                    total -= 1

            # down V
            for i in range(guard[1] - 1, -1, -1):
                cell = [guard[0], i]
                if grid[cell[0]][cell[1]] is None:
                    # hit a wall or another guard
                    break
                # mark as observed
                if grid[cell[0]][cell[1]] != 0:
                    grid[cell[0]][cell[1]] = 0
                    total -= 1

        return total


