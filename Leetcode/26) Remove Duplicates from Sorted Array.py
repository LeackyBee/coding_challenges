from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        offset = 0
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                offset += 1
            else:
                nums[i - offset] = nums[i]

            prev = nums[i]

        return len(nums) - offset


if __name__ == "__main__":
    solution = Solution()

    nums = [1,1,2]
    assert solution.removeDuplicates(nums) == 2
    assert nums[:2] == [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums) == 5
    assert nums[:5] == [0,1,2,3,4]