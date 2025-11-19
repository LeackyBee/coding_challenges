

def main():
    num = 1000000
    collatz = {1:1}
    collatz[1] = 0
    max_length = 1
    max_i = 1
    for i in range(2,num):
        print(i)
        chain = [i]
        while collatz.get(i, None) is None:
            if i % 2 == 0:
                i = i//2
            else:
                i = 3*i + 1
            chain.insert(0, i)
        seq_length = collatz[i] + 1
        for i in chain[1:]:
            collatz[i] = seq_length
            seq_length += 1
        if seq_length > max_length:
            max_i = i
            max_length = seq_length
    print(max_i)


main()