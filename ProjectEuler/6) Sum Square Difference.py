"""
sum of i^2 for 0...n = n(n+1)(2n+1)/6

"""


def sum_squares(n):
    return n*(n+1)*(2*n+1)/6

def sum(n):
    return n*(n+1)/2

def main():
    print(abs(int(sum_squares(100) - sum(100)**2)))

main()