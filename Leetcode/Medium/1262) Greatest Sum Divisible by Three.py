from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        output = sum(nums)
        one = sorted([x for x in nums if x % 3 == 1])
        two = sorted([x for x in nums if x % 3 == 2])

        if output % 3 == 1:
            ones_option = None
            if one:
                ones_option = one[0]
            twos_option = None
            if len(two) >= 2:
                twos_option = two[0] + two[1]
            if ones_option and twos_option:
                output -= min(ones_option, twos_option)
            else:
                output -= ones_option or twos_option
        elif output % 3 == 2:
            ones_option = None
            if len(one) >= 2:
                ones_option = one[0] + one[1]
            twos_option = None
            if two:
                twos_option = two[0]
            if ones_option and twos_option:
                output -= min(ones_option, twos_option)
            else:
                output -= ones_option or twos_option

        return output

