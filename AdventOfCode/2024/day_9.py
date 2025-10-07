import io

from Utils.logger import logger

"""
First impression is that we first need to parse to the file system representation, since we need that to see what's happening
Then, we maintain a left and right pointer
Each iteration, we swap the values at left and right
Then, we move left to the next ".", and right to the next "not ."

Realised also that this needs to be a list, not a string since we'll likely have multi-digit numbers

For part 2:
Once parsed, iterate over the disk map and make a list of the empty positions [(start, end), (start, end), ...]
additionally, make a map of {id:(start, end), ...}
and keep track of the largest id
Now, from max_id -> 0
size = end-start
for i in empty_positions:
if the position is big enough and is to the left of the files position, move file over and update the start and end for the empty position
No need to update the empty positions list, we can't move a new file to the newly opened position so no point updating it
No need to update the file locations map either, we won't re-reference it
"""

def checksum(disk_map):
    checksum = 0
    for i in range(len(disk_map)):
        checksum += i * int(disk_map[i] if disk_map[i] else 0)
    return checksum

def parse_disk_map(disk_map):
    output = []
    vals = list(disk_map)
    num = 0
    file = True
    for val in vals:
        if file:
            arr = [num]
            num += 1
            file = False
        else:
            arr = [None]
            file = True
        arr = arr * int(val)
        output.extend(arr)
    return output

def parse_file_to_string(file):
    return file.read().strip()

def move_pointers(disk_map, left, right):
    while disk_map[left] is not None:
        left += 1
    while disk_map[right] is None:
        right -= 1
    return left, right

def defragment(disk_map):
    disk_map = parse_disk_map(disk_map)

    left, right = move_pointers(disk_map, 0, len(disk_map) - 1)

    while left < right:
        # swap values
        disk_map[left], disk_map[right] = disk_map[right], disk_map[left]
        left, right = move_pointers(disk_map, left, right)
    return checksum(disk_map)

def defragment_whole_file(disk_map):
    disk_map = parse_disk_map(disk_map)
    empty_positions = []
    file_locations = {}
    pos = [0, 0]
    id = 0
    prev = 0
    logger.debug(disk_map)
    for i in range(len(disk_map)):
        curr = disk_map[i]
        logger.debug(f"Currently looking at {curr} at position {i}. Previously looked at {prev}")
        if curr != prev:
            pos[1] = i
            if prev is None:
                logger.debug(f"Adding {pos} to empty positions")
                empty_positions.append(pos)
            else:
                logger.debug(f"Assigning {prev} position {pos}")
                file_locations[id] = pos
                id += 1
            pos = [i, 0]
        prev = curr

    pos[1] = i+1
    if prev is None:
        logger.debug(f"Adding {pos} to empty positions")
        empty_positions.append(pos)
    else:
        logger.debug(f"Assigning {prev} position {pos}")
        file_locations[id] = pos

    logger.debug(f"empty_positions: {empty_positions}")
    logger.debug(f"file_locations: {file_locations}")

    logger.debug(id)
    for i in range(id, 0, -1):
        logger.debug(f"Looking at file {i}")
        pos = file_locations[i]
        size = pos[1] - pos[0]

        for j in range(len(empty_positions)):
            epos = empty_positions[j]
            esize = epos[1] - epos[0]
            if epos[0] < pos[0] and esize >= size:
                logger.debug(f"Moving file {i} at position {pos} to position {epos}")
                for position in range(epos[0], epos[0] + size):
                    disk_map[position] = i
                empty_positions[j] = [position+1, epos[1]]
                for position in range(pos[0], pos[1]):
                    disk_map[position] = None

                logger.debug(disk_map)
                break
            if epos[0] > pos[0]:
                break
    return checksum(disk_map)



if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""2333133121414131402""")

    try:
        file = open(filepath)
    except:
        pass

    disk_map = parse_file_to_string(file)

    #logger.print(defragment(disk_map))
    logger.print(defragment_whole_file(disk_map))