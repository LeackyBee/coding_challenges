def main():
    list = []
    i = 1
    while len(list) < 10001:
        i += 1
        divs = [x for x in list if i % x == 0]
        if not divs:
            list.append(i)
    print(list[-1])

main()


