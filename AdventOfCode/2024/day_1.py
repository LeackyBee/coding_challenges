

def parse_file_to_lists(file):
    list1 = []
    list2 = []
    for line in file:
        inputs = line.split()
        if line:
            list1.append(int(inputs[0]))
            list2.append(int(inputs[1]))

    return list1, list2

def find_difference(list1, list2):
    sum = 0

    list1.sort()
    list2.sort()

    for (a, b) in zip(list1, list2):
        sum += abs(a - b)

    return sum

def find_similarity(list1, list2):
    appearances = {}
    sum = 0
    for i in list2:
        appearances[i] = appearances.get(i, 0) + 1

    for i in list1:
        sum += appearances.get(i, 0) * i

    return sum

if __name__  == "__main__":
    filepath = input("Input File Path")

    with open(filepath) as file:
        list1, list2 = parse_file_to_lists(file)

        print(find_difference(list1, list2))
        print(find_similarity(list1, list2))

