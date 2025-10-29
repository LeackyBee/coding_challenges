from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            num = digits[i] + 1
            carry = num // 10
            digits[i] = num % 10
            i -= 1

        if carry:
            digits.insert(0, 1)

        return digits

if __name__ == "__main__":
    solution = Solution()

    assert solution.plusOne([9]) == [1,0]
    assert solution.plusOne([4,3,2,1]) == [4,3,2,2]