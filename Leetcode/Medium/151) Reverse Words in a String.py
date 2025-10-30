class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words_no_spaces = [word for word in words if word]
        words_no_spaces.reverse()
        return " ".join(words_no_spaces)

    def reverseWordsInPlace(self, s:str) -> str:
        # TODO O(1) memory
        raise NotImplementedError


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseWords("hello world") == "world hello"
    assert solution.reverseWords(" hello  world  ") == "world hello"