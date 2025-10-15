from math import *

from Utils.logger import logger


def multiples_of_3_and_5(n):
    n = n-1
    vals = [(3, floor(n/3)), (5, floor(n/5)), (15, floor(n/15))]
    print(vals)
    output = []
    for val in vals:
        if val[1] % 2 != 0:
            output.append(val[0]*val[1]*ceil(val[1]/2))
        else:
            output.append(val[0]*(val[1]+1)*(val[1]/2))
    print(output)
    return output[0] + output[1] - output[2]


if __name__ == '__main__':
    logger.print(multiples_of_3_and_5(1000))