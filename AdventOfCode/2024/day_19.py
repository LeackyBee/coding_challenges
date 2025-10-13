import io

from Utils.logger import logger

def parse_file(file):
    alphabet = set()
    configs = []
    for line in file:
        if line.strip():
            alphabet = alphabet.union(set(line.strip().split(", ")))
        else:
            break
    for line in file:
        if line.strip():
            configs.append(line.strip())

    return alphabet, configs

def construct_trie(alphabet):
    trie = [None, {}]
    for token in alphabet:
        position = trie
        chars = list(token)
        for char in chars:
            if char not in position[1].keys():
                position[1][char] = [None, {}]
            position = position[1][char]
        position[0] = token
    return trie

def lr_parser(trie, configs):
    valid = []
    for config in configs:
        logger.debug(f"config: {config}")
        chars = list(config)
        position = trie
        i = 0
        tokens = []
        curr_token = None
        offset = 0
        checkpoints = []
        while i < len(chars):
            logger.debug()
            char = chars[i]
            logger.debug(char)
            if char not in position[1].keys():
                if curr_token is not None:
                    tokens.append(curr_token)
                    i -= offset
                    logger.debug(f"Token: {curr_token} appended, i reset back by {offset}")
                    offset = 0
                    curr_token = None
                    position = trie
                    continue
                else:
                    if checkpoints:
                        checkpoint = checkpoints.pop()
                        i = checkpoint[0]
                        tokens = checkpoint[1]
                        position = trie
                        curr_token = None
                        offset = 0
                    else:
                        # config is invalid
                        logger.debug(f"{config} is invalid")
                        break
            else:
                if i != 0 and offset == 0 and (char in trie[1].keys()):
                    # previous char completed a token, but this one has two options
                    # either extend the current token, or accept it and go back to the start of the trie
                    # so we save the other option as a checkpoint, and if we get to an invalid state later we pop back to here
                    logger.debug(f"Checkpoints was {checkpoints}")
                    checkpoints.append([i, tokens])
                    logger.debug(f"Checkpoints is now {checkpoints}")
                logger.debug(f"Position was {position}")
                position = position[1][char]
                logger.debug(f"Position is now {position}")
                if position[0]:
                    logger.debug(f"Token was {curr_token}")
                    curr_token = position[0]
                    logger.debug(f"Token is now {curr_token}")
                    offset = 0
                else:
                    offset += 1
            i += 1
# bgrwwwbuugwrruurrwgbgrbwrrruurgbuwbgbwuuruubwuubruwgubw
        if curr_token:
            tokens.append(curr_token)
        logger.debug(f"Tokens: {tokens}")
        if "".join(tokens) == config:
            valid.append(config)
    return valid


if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""")

    try:
        file = open(filepath)
    except:
        pass

    alphabet, configs = parse_file(file)
    logger.enable()
    logger.print(alphabet)
    logger.print(configs)
    trie = construct_trie(alphabet)

    valid = lr_parser(trie, configs)
    logger.print(len(valid))
