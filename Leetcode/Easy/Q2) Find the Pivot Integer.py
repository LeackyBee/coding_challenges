class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        end = n * (n + 1) / 2

        for i in range(1, n):
            if i * (i + 1) / 2 == end - (i - 1) * i / 2:
                return i
        return -1
