from curses.ascii import isdigit


def main():
    a = input("Input both numbers separated by a space").split(" ")
    n = int(a[0])
    m = int(a[1])

    for i in range(n, m + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        out = out or str(i)
        print(out)


if __name__ == "__main__":
    main()
    isdigit