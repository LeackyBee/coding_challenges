import io
from functools import cache
from time import sleep

from Utils.logger import logger
from Utils.parse_utils import parse_file_to_lines

def getDag(lines):
    outputs_dag = {}
    inputs_dag = {}

    for line in lines:
        device, outputs = "".join(line).split(": ")
        outputs = outputs.split(" ")

        outputs_dag[device] = outputs
        for output in outputs:
            inputs = inputs_dag.get(output, [])
            inputs.append(device)
            inputs_dag[output] = inputs

    return inputs_dag, outputs_dag

def bfs(dag, start, end, terminate=None):
    frontier = set(dag.get(start, []))
    out_count = 0

    while frontier:
        nfrontier = []
        for node in frontier:
            if node == terminate or node == start:
                continue
            elif node == end:
                out_count += 1
            else:
                nfrontier.extend(dag.get(node, []))
        frontier = nfrontier

    return out_count

def dfs(dag, start, end):
    seen = set()

    @cache
    def dfs_internal(node, seen_dac, seen_fft):
        if node not in seen:
            if node == end:
                return 1 if seen_dac and seen_fft else 0
            else:
                if node == "dac":
                    seen_dac = True
                elif node == "fft":
                    seen_fft = True
                return sum([dfs_internal(node, seen_dac, seen_fft) for node in dag[node]])

    return dfs_internal(start, False, False)

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""")

    try:
        file = open(filepath)
    except:
        pass

    lines = parse_file_to_lines(file)

    input_dag, output_dag = getDag(lines)

    logger.enable()
    logger.print(f"There are {bfs(output_dag, "you", "out")} paths from you to out")

    logger.print(dfs(output_dag, "svr", "out"))

    """
    bfs(output_dag, "svr", "out")

    svr_to_fft = bfs(output_dag, "svr", "fft", "dac")
    print(svr_to_fft)
    fft_to_dac = bfs(output_dag, "fft", "dac")
    print(fft_to_dac)
    dac_to_out = bfs(output_dag, "dac", "out")
    print(dac_to_out)
    valid = svr_to_fft * fft_to_dac * dac_to_out

    logger.print(f"There are {valid} paths from svr to out that pass fft and dac")
    """