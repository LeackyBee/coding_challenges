
def primes():
    list = []
    i = 1
    while True:
        i += 1
        divs = [x for x in list if i % x == 0]
        if not divs:
            list.append(i)
            yield i

def main():
    x = 600851475143
    for i in primes():
        if x == i:
            print(i)
            return
        elif x % i == 0:
            print(i)
            x = x // i

main()