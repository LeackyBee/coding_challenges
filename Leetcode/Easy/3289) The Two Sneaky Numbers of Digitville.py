from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        output = []
        for num in nums:
            if num in seen:
                output.append(num)
            else:
                seen.add(num)

        return output

if __name__ == "__main__":
    assert Solution().getSneakyNumbers([0,1,1,0]) == [1,0]
    assert Solution().getSneakyNumbers([0,3,2,1,3,2]) == [3,2]