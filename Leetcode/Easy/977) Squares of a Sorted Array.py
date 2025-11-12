from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0 for _ in nums]
        left = -1
        right = 0
        while right < len(nums) and nums[right] < 0:
            left += 1
            right += 1

        i = 0
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < nums[right]:
                output[i] = nums[left] ** 2
                left -= 1
            else:
                output[i] = nums[right] ** 2
                right += 1
            i += 1

        while left >= 0:
            output[i] = nums[left] ** 2
            left -= 1
            i += 1

        while right < len(nums):
            output[i] = nums[right] ** 2
            right += 1
            i += 1

        return output
