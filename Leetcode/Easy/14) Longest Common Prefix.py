class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        guide_string = strs[0]

        output = ""
        for i in range(len(guide_string)):
            char = guide_string[i]
            valid = True
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return output
            output += char
        return output

if __name__ == "__main__":
    solution = Solution()

    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert solution.longestCommonPrefix(["ab", "a"]) == "a"