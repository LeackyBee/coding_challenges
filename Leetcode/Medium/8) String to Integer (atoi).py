class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        negative = s[0] == "-"

        if s[0] in ["+", "-"]:
            s = s[1:]

        if not s:
            return 0
        output = 0

        i = 0

        # find first digit
        while i < len(s) and s[i] == "0":
            i += 1

        # read in digits
        while i < len(s) and s[i].isdigit():
            output = output * 10 + int(s[i])
            i += 1

        if negative:
            output = -output

        # round
        output = min(2 ** 31 - 1, output)
        output = max(-2 ** 31, output)

        return output


if __name__ == "__main__":
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("   -042") == -42
    assert Solution().myAtoi("1337c0d3") == 1337
    assert Solution().myAtoi("    0000000000000   ") == 0
    assert Solution().myAtoi("words and 987") == 0
    assert Solution().myAtoi("") == 0
    assert Solution().myAtoi("-") == 0
    assert Solution().myAtoi("+1") == 1
