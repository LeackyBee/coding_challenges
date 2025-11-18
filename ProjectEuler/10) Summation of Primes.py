def main():
    list = []
    i = 1
    while i < 2000000:
        i += 1
        divisible = False
        for div in list:
            if i % div == 0:
                divisible = True
                break

        if not divisible:
            list.append(i)
    print(sum(list))

main()