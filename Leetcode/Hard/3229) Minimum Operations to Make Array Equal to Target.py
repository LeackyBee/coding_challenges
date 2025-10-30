from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        counter = 0
        prev = 0
        for i in range(len(target)):
            val = target[i] - nums[i]
            if val > prev:
                counter += val - prev

            prev = val

        if prev < 0:
            counter -= prev

        return counter


if __name__ == "__main__":
    assert Solution().minimumOperations([3,5,1,2],[4,6,2,4]) == 2
    assert Solution().minimumOperations([1,3,2], [2,1,4]) == 5
    assert Solution().minimumOperations([1,1,3,4], [4,1,3,2]) == 5