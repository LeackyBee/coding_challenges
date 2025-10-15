import io

from Utils.logger import logger


def parse_file(file):
    # x | y == x before y (y is dependent on x)
    ordering = {}
    updates = []
    orderingDone = False
    logger.print(file)
    for line in file:
        logger.print(f"current line = {line}")
        if not orderingDone:
            if line == "\n":
                orderingDone = True
            else:
                logger.print(line)
                a,b = line.split("|")
                a = int(a)
                b = int(b)

                dependents = ordering.get(b, set())
                dependents.add(a)

                ordering[b] = dependents # b is dependent on a being seen
        else:
            updates.append([int(i) for i in line.split(",")])

    return ordering, updates

def check_orderings(ordering, updates):
    valid = []
    invalid = []
    for update in updates:
        logger.print()
        logger.print(f"Looking at {update}")
        seen = set()
        present = set(update)
        good = True
        for page in update:
            # get dependents
            dependents = ordering.get(page, set())
            # filter for only present dependents
            dependents = dependents.intersection(present)
            logger.print(f"{page}|{dependents}")
            if not dependents.issubset(seen):
                invalid.append(update)
                good = False
                break
            seen.add(page)
        if good:
            valid.append(update)
    return valid, invalid

def reorder(ordering, invalid_updates):
    output = []
    for update in invalid_updates:
        seen = set()
        present = set(update)
        i = 0
        while i < len(update):
            page = update[i]
            # get dependents
            dependents = ordering.get(page, set())
            # filter for only present dependents
            dependents = dependents.intersection(present)
            logger.print(f"{page}|{dependents}")
            if not dependents.issubset(seen):
                # swap with the dependent
                missing = dependents.difference(seen)
                pos = update.index(missing.pop())
                # swap
                logger.print(f"swapping {update[i]} with {update[pos]}")
                logger.print(update)
                update[i] = update[pos]
                logger.print(update)
                update[pos] = page
                logger.print(update)
            else:
                seen.add(page)
                i += 1
        output.append(update)
    return output


if __name__  == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""")

    try:
        file =  open(filepath)
    except:
        pass

    ordering, pages = parse_file(file)

    logger.enable()
    logger.print(ordering)
    logger.print(pages)
    logger.disable()

    valid, invalid = check_orderings(ordering, pages)

    logger.print(f"valid orders: {valid}")
    logger.print(f"invalid orders: {invalid}")

    count = 0
    for update in valid:
        count += update[len(update)//2]

    logger.print(f"Count of valid orders: {count}")

    reordered = reorder(ordering, invalid)
    count = 0
    for update in reordered:
        count += update[len(update)//2]

    logger.print(f"Count of reordered: {count}")

    #print(find_multiples_with_do_and_dont(text))