from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Iterate over list
        Every time the value increases, add the difference to the counter
        """
        counter = 0
        prev = 0
        for val in target:
            if val > prev:
                counter += val - prev

            prev = val

        return counter


if __name__ == "__main__":
    assert Solution().minNumberOperations([1,2,3,2,1]) == 3
    assert Solution().minNumberOperations([3,1,5,4,2]) == 7
    assert Solution().minNumberOperations([3,1,1,2]) == 4