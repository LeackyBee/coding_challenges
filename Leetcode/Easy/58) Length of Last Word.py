class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [x for x in s.split(" ") if x]
        return len(words[-1])


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6