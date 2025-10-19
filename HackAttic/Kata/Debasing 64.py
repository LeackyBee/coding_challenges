import re


B64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
B64_INDEX = {ch: i for i, ch in enumerate(B64_ALPHABET)}

def main():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        lines.append(line)
    for string in lines:
        bits = [format(B64_ALPHABET.index(char), "06b") for char in list(string) if char != "="]
        bits_str = "".join(bits)
        eight_bits = re.findall("........", bits_str)
        chars = [chr(int(x,2)) for x in eight_bits]
        print("".join(chars))

if __name__ == "__main__":
    main()