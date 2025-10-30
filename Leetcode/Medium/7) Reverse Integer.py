class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = list(str(x))
        if negative:
            x = x[1:]

        output = 0
        for i, digit in enumerate(x):
            output += int(digit) * 10 ** i

        if negative:
            output = -output

        # problem asserts only 32 bit integers allowed, returning 0 if outside this range
        if output > 2 ** 31 - 1 or output < -2 ** 31:
            return 0
        return output

if __name__ == "__main__":
    assert Solution().reverse(-321) == -123
    assert Solution().reverse(321) == 123
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(120) == 21
