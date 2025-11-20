from math import sqrt

def triangularNumbers():
    i = 1
    number = 0
    while True:
        number += i
        i += 1
        yield number


def find_divisors(number):
    output = []
    for i in range(1,int(sqrt(number)+1)):
        if number % i == 0:
            output.append(i)
            if i != number // i:
                output.append(number//i)
    return output

if __name__ == "__main__":
    for number in triangularNumbers():
        divisors = find_divisors(number)
        if len(divisors) >= 500:
            print(number)
            break
        else:
            pass
            #print(f"Checked {number}, only {len(divisors)} divisors, and they are {sorted(divisors)}")