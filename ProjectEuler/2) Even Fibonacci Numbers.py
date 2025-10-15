from Utils.logger import logger


def even_fibonacci_numbers(max_val):
    fib = {-2: 0, -1: 1}
    i = 0
    output = 0
    while fib[i-1] <= max_val:
        fib[i] = fib[i-1] + fib[i-2]
        if fib[i] % 2 == 0:
            logger.debug(f"Adding {fib[i]}, count now {output}")
            output += fib[i]
        i += 1
    logger.debug(fib)
    return output


if __name__ == '__main__':
    logger.enable()
    logger.print(even_fibonacci_numbers(4000000))