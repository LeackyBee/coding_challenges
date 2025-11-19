from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        vals = set(nums)

        while True:
            if original in vals:
                original *= 2
            else:
                return original

