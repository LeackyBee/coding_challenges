class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [x.lower() for x in list(s) if x.isalnum()]

        left = 0
        right = len(chars) - 1

        while left < right:
            if chars[left] != chars[right]:
                return False
            else:
                left += 1
                right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama")
    assert not solution.isPalindrome("race a car")