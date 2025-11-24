class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        output = []
        curr = 0
        for i in range(len(nums)):
            curr = (curr * 2 + nums[i]) % 5
            output.append(curr == 0)

        return output