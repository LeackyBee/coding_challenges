class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0  # represents start of substring
        right = 0  # represents next character, not in substring
        length = 0  # longest right-left value
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                # only need to recheck length when right is updated
                length = max(right - left, length)
            else:
                left += 1

        return length

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3