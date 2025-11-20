from math import prod


def generate_primes_until(n):
    if n < 2:
        return []
    output = [2]
    i = 1

    while i < n:
        i += 2
        divisible = False
        for div in output:
            if i % div == 0:
                divisible = True
                break
        if not divisible:
            output.append(i)
    return output

primes = generate_primes_until(100)

def triangularNumbers():
    i = 1
    number = 0
    while True:
        number += i
        i += 1
        yield number


def find_num_divisors(number):
    exponents = []
    for i in primes:
        exponents.append(0)
        while number % i == 0:
            exponents[-1] += 1
            number = number // i
        if i == 1:
            break
    return prod([x+1 for x in exponents])

if __name__ == "__main__":
    for number in triangularNumbers():
        divisors = find_num_divisors(number)
        if divisors >= 500:
            print(number)
            break