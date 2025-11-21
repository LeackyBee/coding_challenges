class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        seen = set()
        output = 0
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                continue
            seen.add(char)
            for j in range(len(s)-1, i, -1):
                if s[j] == char:
                    unique_mids = set(s[i+1:j])
                    output += len(unique_mids)
                    break

        return output