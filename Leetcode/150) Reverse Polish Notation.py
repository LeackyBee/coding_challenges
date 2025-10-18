import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) != 1:
            match tokens[i]:
                case "+":
                    i = i-2 # set i to the position of the first argument
                    a = int(tokens.pop(i))
                    b = int(tokens.pop(i))
                    tokens[i] = a + b
                case "-":
                    i = i-2
                    a = int(tokens.pop(i))
                    b = int(tokens.pop(i))
                    tokens[i] = a - b
                case "*":
                    i = i-2
                    a = int(tokens.pop(i))
                    b = int(tokens.pop(i))
                    tokens[i] = a * b
                case "/":
                    i = i-2
                    a = int(tokens.pop(i))
                    b = int(tokens.pop(i))

                    val = a / b
                    if val < 0:
                        val = math.ceil(val)
                    else:
                        val = math.floor(val)
                    tokens[i] = val
            i += 1

        return int(tokens[0])

if __name__ == '__main__':
    solution = Solution()
    assert solution.evalRPN(["2","1","+","3","*"]) == 9
    assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22