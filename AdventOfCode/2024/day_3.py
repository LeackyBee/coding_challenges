from curses.ascii import isdigit

from Utils.logger import logger



def find_multiples(text):
    states = {
        "": {"m": "m"},
        "m": {"u": "mu"},
        "mu": {"l": "mul"},
        "mul": {"(": "mul("},
        "mul(": {",": "mul(,"},
        "mul(,": {")": "match"}
    }
    output = 0
    match = ""
    left = 0
    right = 0
    for i in text:
        state = states[match]
        nextstate = state.get(i, "")

        logger.print("")
        logger.print(f"current character is {i}")
        logger.print(f"match is {match}")
        logger.print(f"current state map is {state}")
        logger.print(f"next state is {nextstate}")

        if isdigit(i):
            if match == "mul(":
                left = left * 10 + int(i)
                continue
            elif match == "mul(,":
                right = right*10 + int(i)
                continue
        else:
            if nextstate == "match":
                output += left * right
                nextstate = ""
        if nextstate == "":
            left = 0
            right = 0
        match = nextstate
    return output

def find_multiples_with_do_and_dont(text):
    states = {
        True: {
            "": {
                "m": "m",
                "d": "d"
            },
            "m": {
                "u": "mu",
                "d": "d"
            },
            "mu": {
                "l": "mul",
                "d": "d"
            },
            "mul": {
                "(": "mul(",
                "d": "d"
            },
            "mul(": {
                ",": "mul(,",
                "d": "d"
            },
            "mul(,": {
                ")": "match",
                "d": "d"
            },
            "d": {
                "o": "do",
                "m": "m"
            },
            "do": {
                "n": "don",
                "m": "m"
            },
            "don": {
                "'": "don'",
                "m": "m"
            },
            "don'": {
                "t": "don't",
                "m": "m"
            },
            "don't": {
                "(": "don't(",
                "m": "m"
            },
            "don't(": {
                ")": "don't()",
                "m": "m"
            }
               },
        False: {
            "": {"d": "d"},
            "d": {"o": "do"},
            "do": {"(": "do("},
            "do(": {")": "do()"}
        }
    }
    output = 0
    match = ""
    left = 0
    right = 0
    enabled = True
    for i in text:
        logger.print("")
        logger.print(f"current character is {i}")
        logger.print(f"match is {match}")
        logger.print(f"matches are currently {"enabled" if enabled else "disabled"}")

        state = states[enabled][match]

        logger.print(f"current state map is {state}")

        nextstate = state.get(i, "")
        logger.print(f"next state is {nextstate}")


        if isdigit(i):
            if match == "mul(":
                left = left * 10 + int(i)
                continue
            elif match == "mul(,":
                right = right * 10 + int(i)
                continue
        else:
            if nextstate == "match":
                output += left * right
                nextstate = ""
            elif nextstate == "don't()":
                enabled = False
                nextstate = ""
            elif nextstate == "do()":
                enabled = True
                nextstate = ""
        if nextstate == "":
            left = 0
            right = 0
        match = nextstate
    return output



def parse_file_to_string(file):
    output = ""
    for line in file:
        output += line
    return output


if __name__  == "__main__":
    filepath = input("Input File Path: ")
    logger.enable()

    # example for part 1
    text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    #example for part 2
    text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    try:
        with open(filepath) as file:
            text = parse_file_to_string(file)
    except:
        pass

    print(find_multiples(text))
    print(find_multiples_with_do_and_dont(text))