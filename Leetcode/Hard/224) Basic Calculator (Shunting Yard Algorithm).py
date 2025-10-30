class Solution:
    def __init__(self):
        self.output = []
        self.operators = []
        self.precedence = {
            "-": 2,
            "+": 2,
            "/": 3,
            "*": 3,
            "^": 4
        }
        self.associativity = {
            "-": "Left",
            "+": "Left",
            "*": "Left",
            "/": "Left",
            "^": "Right",
        }

    def parse_int(self, chars: list, i: int) -> None:
        # given the starting index of an integer
        # pop all the digits off and replace the index with the full integer
        val = 0
        while chars and i < len(chars) and chars[i].isnumeric():
            val = val * 10 + int(chars.pop(i))
        chars.insert(i, val)

    def evaluateRpn(self, rpn:list[str]):
        stack = []
        for char in rpn:
            print(f"Char = {char}, stack = {stack}")
            if type(char) is int:
                stack.append(char)
            else:
                match char:
                    case "+":
                        b = stack.pop(-1)
                        a = stack.pop(-1)
                        stack.append(a+b)
                    case "-":
                        b = stack.pop(-1)
                        a = stack.pop(-1)
                        stack.append(a-b)
                    case "*":
                        b = stack.pop(-1)
                        a = stack.pop(-1)
                        stack.append(a*b)
                    case "/":
                        b = stack.pop(-1)
                        a = stack.pop(-1)
                        stack.append(a/b)
        return stack[0]


    def calculate(self, s: str) -> int:
        self.output = []
        self.operators = []
        print(s)
        chars = list(s.replace(" ", ""))

        # preparse so that all integers are fully formed
        print(chars)
        i = 0
        prev = None
        while i < len(chars):
            if chars[i].isnumeric():
                self.parse_int(chars, i)
            elif chars[i] == "-" and ((prev == None) or prev == "("):
                # turn unary -x into binary 0-x
                chars.insert(i, 0)
                i += 1
            prev = chars[i]
            i += 1

        print(f"Input = {chars}")
        for char in chars:
            print(f"Token = {char} and output = {self.output} and operators = {self.operators}")
            if type(char) is int:
                self.output.append(char)
            elif char in self.precedence.keys():
                while (self.operators and self.operators[-1] != "("
                       and (self.precedence[self.operators[-1]] > self.precedence[char]
                            or (self.precedence[self.operators[-1]] == self.precedence[char]
                                and self.associativity[char] == "Left"))):
                    self.output.append(self.operators.pop(-1))
                self.operators.append(char)
            elif char == "(":
                self.operators.append(char)
            elif char == ")":
                while self.operators and self.operators[-1] != "(":
                    self.output.append(self.operators.pop(-1))
                assert self.operators[-1] == "("
                self.operators.pop(-1)

        while self.operators:
            self.output.append(self.operators.pop(-1))

        return self.evaluateRpn(self.output)

"""
while (
    there is an operator o2 at the top of the operator stack
    and o2 != "(", 
    and (o2 has greater precedence than o1 or (o1 and o2 have the same precedence and o1 is left-associative))
):"""

if __name__ == "__main__":
    solution = Solution()

    assert solution.calculate("0-2147483647") != 0
    assert False
    assert solution.calculate("10+1+(100-53)") == 58
    assert solution.calculate("1 + 1") == 2
    assert solution.calculate(" 2-1 + 2 ") == 3
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate("-10") == -10


