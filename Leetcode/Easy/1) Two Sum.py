from typing import List

from Utils.logger import logger


class Solution:

    # method is O(nlogn) - the sorting is the bottleneck
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # maintain a sorted copy of the list
        nums_sorted = nums.copy()
        nums_sorted.sort()
        # O(nlogn) n = len(list)

        # define pointers to the start and end of the sorted list
        # we then shuffle these pointers inwards until we find the value
        # moving left pointer inwards will increase the sum
        # moving the right pointer inwards will decrease the sum
        # when we eventually find the target, we find the indices of the elements in the original list
        # this is O(n)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums_sorted[left] + nums_sorted[right] > target:
                # we are too high, so we need a smaller number
                right -= 1
            elif nums_sorted[left] + nums_sorted[right] < target:
                # we are too low, we need a larger number
                left += 1
            else:
                if nums_sorted[left] == nums_sorted[right]:
                    # if the numbers are the same, we have to find the indices differently
                    # we find the first instance of the element
                    # we then use this index to add a window to the index method
                    # this returns the index in the list, not in the window - so no offsetting needed
                    left_i = nums.index(nums_sorted[left])
                    right_i = nums.index(nums_sorted[right], left_i + 1)
                    return [left_i, right_i]
                else:
                    return [nums.index(nums_sorted[left]), nums.index(nums_sorted[right])]
        raise Exception("No solution exists!")

if __name__ == '__main__':
    solution = Solution()
    logger.print(solution.twoSum([3,2,4], 6))