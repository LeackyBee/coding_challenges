from Utils.logger import logger


def even_fibonacci_numbers(length):
    fib = {1: 1, 2:1}
    i = 2
    while len(str(fib[i])) < length:
        fib[i+1] = fib[i] + fib[i-1]
        i += 1
    logger.debug(fib)
    return i


if __name__ == '__main__':
    logger.enable()
    logger.print(even_fibonacci_numbers(1000))