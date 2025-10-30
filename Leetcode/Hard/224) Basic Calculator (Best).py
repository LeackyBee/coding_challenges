class Solution:
    def calculate(self, s: str) -> int:
        # carries the sign applied to the result of the parenthesis
        parenthesis_stack = []
        # carries the current value before we entered the parenthesis
        curr_stack = []

        s = s.replace(" ", "") + "$" # terminator
        sign = 1
        running = 0
        curr = 0
        for char in s:
            if char.isnumeric():
                running = running*10 + int(char)
            else:
                curr += sign * running
                running = 0
                if char == "(":
                    parenthesis_stack.append(sign)
                    curr_stack.append(curr)
                    sign = 1
                    curr = 0
                elif char == ")":
                    val = parenthesis_stack.pop() * curr
                    curr = curr_stack.pop() + val
                else:
                    sign = 1 if char == "+" else -1

        return curr

if __name__ == "__main__":
    solution = Solution()

    assert solution.calculate("0-2147483647") != 0
    assert solution.calculate("10+1+(100-53)") == 58
    assert solution.calculate("1 + 1") == 2
    assert solution.calculate(" 2-1 + 2 ") == 3
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate("-10") == -10
    assert solution.calculate("1-(     -2)") == 3