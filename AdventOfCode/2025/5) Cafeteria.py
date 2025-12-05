import io

from Utils.logger import logger
from Utils.parse_utils import parse_file_to_lines


def findFresh(lines: list[str]):
    total_fresh_ingredients = 0
    total_fresh_options = 0
    ranges = []
    range = lines.pop(0)
    while range != "":
        start, end = range.split("-")
        start = int(start)
        end = int(end)
        ranges.append([start, end])
        range = lines.pop(0)

    ranges.sort(key=lambda x: x[0])
    i = 1
    logger.debug(f"Ranges to combine: {ranges}")
    merged_ranges = [ranges[0]]
    while i < len(ranges):
        prev_range = merged_ranges[-1]
        curr_range = ranges[i]

        if curr_range[0] - 1 <= prev_range[1]:
            logger.debug(f"Combining {prev_range} and {curr_range}")
            # if this is the case, the previous ranges end overlaps our start, so merge the two
            prev_range[1] = max(curr_range[1], prev_range[1])
        else:
            merged_ranges.append(curr_range)
        i += 1
    ranges = merged_ranges
    logger.debug(f"Combined ranges: {ranges}")

    for start, end in ranges:
        total_fresh_options += end - start + 1

    ids = []
    for id in lines:
        ids.append(int(id))

    curr_range_i = 0
    curr_id_i = 0
    while curr_id_i < len(ids) and curr_range_i < len(ranges):
        curr_id = ids[curr_id_i]
        curr_range = ranges[curr_range_i]

        if curr_id > curr_range[1]:
            curr_range_i += 1
        elif curr_range[0] <= curr_id <= curr_range[1]:
            total_fresh_ingredients += 1
            curr_id_i += 1
        else:
            curr_id_i += 1

    return total_fresh_ingredients, total_fresh_options

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")

    try:
        file = open(filepath)
    except:
        pass

    lines = ["".join(x) for x in parse_file_to_lines(file)]

    logger.enable()
    fresh_inventory, fresh_ids = findFresh(lines)

    logger.print(f"There are {fresh_inventory} fresh ingredients")
    logger.print(f"There are {fresh_ids} total fresh ids")