class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace("0", ""))

if __name__ == "__main__":
    assert Solution().removeZeros(1020030) == 123
    assert Solution().removeZeros(1) == 1