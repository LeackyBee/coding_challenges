class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1

        return -1

if __name__ == "__main__":
    solution = Solution()

    assert solution.strStr("a", "a") == 0
    assert solution.strStr("adsasdbutsad", "sad") == 9
    assert solution.strStr("sadbutsad", "sad") == 0