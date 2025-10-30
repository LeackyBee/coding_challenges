import math
from typing import Optional, List

from Utils.logger import logger
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        # single digit number is palindromic, and so is empty char and both of these edge cases pass this loop
        while left < right:
            if x[left] != x[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def getVal(self, x:int, pos:int) -> int:
        # 1234, 1 -> 1234 % 100 -> 34 // 10 -> 3
        return (x % (10 ** (pos+1))) // (10**pos)

    def findLength(self, x:int) -> int:
        # 100 -> 2 (0-indexed length)
        return math.floor(math.log(x, 10))

    def isPalindromeNoStringCast(self, x: int) -> bool:
        if x < 0:
            # negative numbers are not palindromic
            return False
        if x < 10:
            # single digit numbers are palindromic
            return True
        left = self.findLength(x)
        right = 0

        while left > right:
            if self.getVal(x, left) != self.getVal(x, right):
                return False
            else:
                left -= 1
                right += 1
        return True





if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindromeNoStringCast(101)
    assert solution.isPalindromeNoStringCast(9)
    assert solution.isPalindromeNoStringCast(0)
    assert not solution.isPalindromeNoStringCast(48)
    assert not solution.isPalindromeNoStringCast(-121)