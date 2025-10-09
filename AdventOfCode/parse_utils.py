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

def parse_file_to_int_matrix(file, sep=" "):
    output = []
    for line in file:
        output.append([int(x.strip()) for x in line.strip().split(sep)])
    return output

def parse_file_to_int_array(file, sep=" "):
    # assert only one line
    for line in file:
        return [int(x.strip()) for x in line.split(sep)]


def parse_char_array_to_string(char_array):
    return "\n".join(["".join(line) for line in char_array])

def parse_int_array_to_string(array):
    array = [[str(cell) for cell in line] for line in array]
    return "\n".join(["".join(line) for line in array])
