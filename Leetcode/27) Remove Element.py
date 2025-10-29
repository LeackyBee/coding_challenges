from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        for i in range(len(nums)):
            if nums[i] == val:
                offset += 1
            else:
                nums[i - offset] = nums[i]

            prev = nums[i]

        return len(nums) - offset


if __name__ == "__main__":
    solution = Solution()

    nums = [1,1,2]
    assert solution.removeElement(nums, 1) == 1
    assert nums[:1] == [2]

    nums = [0,1,2,2,3,0,4,2]
    assert solution.removeElement(nums, 2) == 5
    assert set(nums[:5]) == {0, 1, 4, 0, 3}