class Expression:
    def evaluate(self) -> int:
        pass


class IntegerExpr(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self) -> int:
        return self.value

    def __str__(self):
        return str(self.value)


class AdditionExpr(Expression):
    def __init__(self, a: Expression, b: Expression):
        self.a = a
        self.b = b

    def evaluate(self) -> int:
        return self.a.evaluate() + self.b.evaluate()

    def __str__(self):
        return f"({self.a}+{self.b})"


class SubtractionExpr(Expression):
    def __init__(self, a: Expression, b: Expression):
        self.a = a
        self.b = b

    def evaluate(self) -> int:
        return self.a.evaluate() - self.b.evaluate()

    def __str__(self):
        return f"({self.a}-{self.b})"


class Solution:
    def parse_int(self, chars: list, i: int) -> None:
        # given the starting index of an integer
        # pop all the digits off and replace the index with the full integer
        val = 0
        while chars and chars[i].isnumeric():
            val = val * 10 + int(chars.pop(i))
        chars.insert(i, IntegerExpr(val))

    def parse_subexpression(self, chars: list, index: int):
        chars.pop(index)  # will be a "("
        # There will be no two consecutive operators in the input.
        # because of this, only the first character in s can be the unary negation
        if chars[index] == "-":
            # first char is unary negation
            # -x == 0-x
            # therefore add a 0 at pos i
            chars.insert(index, "0")


        i = index
        while chars[i] != ")":
            if type(chars[i]) is str and chars[i].isnumeric():
                # [..., "1","2","3",...] -> [..., 123, ...]
                self.parse_int(chars, i)
            elif chars[i] == "(":
                self.parse_subexpression(chars, i)
            i += 1

        end = i

        i = index
        while i < end:
            char = chars[i]
            if char == "+":
                b = chars.pop(i+1)
                chars.pop(i)
                a = chars.pop(i-1)

                chars.insert(i-1, AdditionExpr(a,b))
                i -= 1
                end -= 2
            elif char == "-":
                b = chars.pop(i + 1)
                chars.pop(i)
                a = chars.pop(i - 1)

                chars.insert(i-1, SubtractionExpr(a, b))
                i -= 1
                end -= 2
            else:
                i += 1
        # remove bracket
        chars.pop(i)

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # remove all spaces
        chars = ["("] + list(s) + [")"]  # add terminator

        # assert that we only see ) if we've seen a ( beforehand
        # So if we see a ), we should return the list and the current index
        # can then parse the string in-place, recursing into the substring when we encounter a (
        # if we see an operator, the left
        self.parse_subexpression(chars, 0)

        return chars[0].evaluate()


if __name__ == "__main__":
    solution = Solution()

    assert solution.calculate("10+1+(100-53)") == 58
    assert solution.calculate("1 + 1") == 2
    assert solution.calculate(" 2-1 + 2 ") == 3
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate("-10") == -10


