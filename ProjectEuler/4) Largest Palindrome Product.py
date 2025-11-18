import math


def getVal(x: int, pos: int) -> int:
    # 1234, 1 -> 1234 % 100 -> 34 // 10 -> 3
    return (x % (10 ** (pos + 1))) // (10 ** pos)

def findLength(x: int) -> int:
    # 100 -> 2 (0-indexed length)
    return math.floor(math.log(x, 10))

# grabbed from a leetcode submission
def isPalindromeNoStringCast(x: int) -> bool:
    if x < 0:
        # negative numbers are not palindromic
        return False
    if x < 10:
        # single digit numbers are palindromic
        return True
    left = findLength(x)
    right = 0

    while left > right:
        if getVal(x, left) != getVal(x, right):
            return False
        else:
            left -= 1
            right += 1
    return True


def main():
    max_val = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            val = i*j
            if isPalindromeNoStringCast(val):
                max_val = max(max_val, val)
    print(max_val)

main()