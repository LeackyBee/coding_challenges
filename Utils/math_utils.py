def generate_n_primes(n):
    output = []
    i = 0

    while len(output) < n:
        i += 1
        divisible = False
        for div in output:
            if i % div == 0:
                divisible = True
                break
        if not divisible:
            output.append(i)

def generate_primes():
    output = []
    i = 0

    while True:
        i += 1
        divisible = False
        for div in output:
            if i % div == 0:
                divisible = True
                break
        if not divisible:
            output.append(i)