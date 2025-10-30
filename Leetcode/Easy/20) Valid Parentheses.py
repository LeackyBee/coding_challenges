class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairings = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop(-1)
                if pairings[char] != prev:
                    return False
        return not stack

if __name__ == "__main__":
    solution = Solution()

    assert solution.isValid("[") == False
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([])") == True
    assert solution.isValid("([)]") == False
