import io

from Utils.logger import logger
from Utils.matrix_utils import step

"""
Start each config with an [(0,0), 0] (position, cost)
Iterate 100 times (max)
Each iteration, explode the list into two, one for button A and one for button B
Filter out positions which have exceeded the score
if a position meets the score, track it's score (if it's lower than the current one)


Possible optimisation:
- keep a map of positions to scores, and at each position check if the score in the map is lower. If it is, filter out.
-- intuition here is that if we've gotten to the current position for less tokens, we can scrap this route

Ahhh this is a red herring. There is only one solution for each, it's just linear equations
"""


def parse_file_to_claw_config(file, error = True):
    output = []
    l1 = file.readline()
    l2 = file.readline()
    l3 = file.readline()
    while l1:
        config = {}
        l1 = l1.split(" ")
        config["A"] = (int(l1[2][2:-1]), int(l1[3][2:]))
        l2 = l2.split(" ")
        config["B"] = (int(l2[2][2:-1]), int(l2[3][2:]))
        l3 = l3.split(" ")
        if error:
            config["Target"] = (int(l3[1][2:-1]) + 10000000000000, int(l3[2][2:]) + 10000000000000)
        else:
            config["Target"] = (int(l3[1][2:-1]), int(l3[2][2:]))
        output.append(config)
        file.readline()

        l1 = file.readline()
        l2 = file.readline()
        l3 = file.readline()
    return output

def minimum_tokens(configs):
    tokens = 0
    for config in configs:
        target = config["Target"]
        a_button = config["A"]
        b_button = config["B"]

        xa = a_button[0]
        xb = b_button[0]

        ya = a_button[1]
        yb = b_button[1]
        xt = target[0]
        yt = target[1]

        m = (ya*xt - xa*yt)/(xb*ya-xa*yb)
        n = (xt-xb*m)/xa
        logger.debug(config)
        logger.debug(f"m: {m}, n: {n}")

        if int(n) == n and int(m) == m:
            tokens += int(m) + int(n)*3

    return tokens


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""")

    try:
        file = open(filepath)
    except:
        pass

    configs = parse_file_to_claw_config(file, False)
    logger.print(f"Configurations: {configs}")
    logger.print(minimum_tokens(configs))

    logger.enable()
    file.seek(0)
    configs = parse_file_to_claw_config(file, True)
    logger.print(f"Configurations w/ errors: {configs}")
    logger.print(minimum_tokens(configs))

