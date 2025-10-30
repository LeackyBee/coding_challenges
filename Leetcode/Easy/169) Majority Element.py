from typing import List, Optional


class Solution:
    # Boyer-Moore Majority Algorithm
    def majorityElement(self, nums: List[int]) -> Optional[int]:
        curr = nums[0]
        counter = 0

        # first pass
        for val in nums:
            if counter == 0:
                curr = val
                counter = 1
                continue

            if val == curr:
                counter += 1
            else:
                counter -= 1

        # second pass
        counter = 0
        for val in nums:
            if val == curr:
                counter += 1

        if counter > len(nums)/2:
            return curr
        else:
            return None


if __name__ == "__main__":
    assert Solution().majorityElement([3,2,3]) == 3
    assert Solution().majorityElement([3, 2]) is None