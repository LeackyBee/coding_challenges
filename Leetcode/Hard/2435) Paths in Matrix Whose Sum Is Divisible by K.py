from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[[0 for _ in range(k)] for _ in grid[0]] for __ in grid]
        dp[0][0][grid[0][0] % k] = 1

        empty = [0 for _ in range(k)]

        # It's fine to go negative, the cell on the other side of the dp matrix will be all 0s
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                mod = grid[i][j] % k

                curr = dp[i][j]

                if i == 0:
                    up = empty
                else:
                    up = dp[i - 1][j]

                if j == 0:
                    left = empty
                else:
                    left = dp[i][j - 1]

                for pos in range(len(curr)):
                    curr[pos] = up[pos - mod] + left[pos - mod]

        return dp[-1][-1][0] % (10 ** 9 + 7)

if __name__ == "__main__":
    assert Solution().numberOfPaths([[1,5,3,7,3,2,3,5]], 29) == 1
    assert Solution().numberOfPaths([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1) == 10
    assert Solution().numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3) == 2