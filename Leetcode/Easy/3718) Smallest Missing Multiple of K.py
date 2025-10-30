from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mults = [k * (i + 1) for i in range(len(nums) + 1)]
        for num in nums:
            if num % k == 0:
                index = num // k - 1
                if index >= len(mults):
                    # number outside of this range can be ignored, it isn't going to be the smallest
                    continue

                mults[num // k - 1] = None

        for num in mults:
            if num:
                return num

        raise RuntimeError("Impossible State")

