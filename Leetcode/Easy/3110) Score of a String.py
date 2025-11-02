class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:
            return 0

        prev = ord(s[0])
        total = 0
        for c in list(s)[1:]:
            total += abs(ord(c) - prev)
            prev = ord(c)
        return total

if __name__ == "__main__":
    assert Solution().scoreOfString("hello") == 13
    assert Solution().scoreOfString("") == 0
    assert Solution().scoreOfString("zaz") == 50