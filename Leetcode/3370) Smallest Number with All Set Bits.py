from math import log, pow

class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(pow(2,(int(log(n,2)+1))))-1


if __name__ == "__main__":
    assert Solution().smallestNumber(5) == 7
    assert Solution().smallestNumber(1) == 1
    assert Solution().smallestNumber(10) == 15