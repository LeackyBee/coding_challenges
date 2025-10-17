from typing import List

from Utils.logger import logger


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Start with offset = 0
        For each zero passed, increase offset by 1
        For each non-zero, shift position back by offset
        At the end, set last <offset> positions to 0
        """
        offset = 0
        for i in range(len(nums)):
            if nums[i] != 0 and offset: # no need to swap if no offset
                nums[i - offset] = nums[i]
            if nums[i] == 0:
                offset += 1
        for i in range(offset):
            nums[-1-i] = 0


if __name__ == '__main__':
    solution = Solution()
    a = [1,0,2,3,0,4,0]
    solution.moveZeroes(a)
    assert a == [1,2,3,4,0,0,0]

    a = [0,1,0,3,12]
    solution.moveZeroes(a)
    assert a == [1,3,12,0,0]