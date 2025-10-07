def parse_file_to_char_matrix(file):
    output = []
    for line in file:
        output.append(list(line.strip()))
    return output

def parse_file_to_int_matrix(file):
    output = []
    for line in file:
        output.append([int(x) for x in list(line.strip())])
    return output


def parse_char_array_to_string(char_array):
    return "\n".join(["".join(line) for line in char_array])
