file = "in8"
import math


def prepare_nodes():
    with  open(file) as f:
        lines = f.readlines()
        move = lines.pop(0).rstrip()
        lines.pop(0)
        nodes = {}
        for l in lines:
            l = l.replace("(", '').replace(')', '').replace(',', '').replace('=', '')
            l = l.split()
            nodes[l[0]] = (l[1], l[2])
        return nodes, move


def part_two():
    nodes, move = prepare_nodes()
    start_nodes = list(filter(lambda x: x[2] == "A", nodes.keys()))
    cycles = []
    for n in start_nodes:
        res = 0
        while True:
            flag = False
            for c in move:
                if c == "L":
                    n = nodes[n][0]
                else:
                    n = nodes[n][1]
                res += 1
                if n[2] == "Z":
                    cycles.append(res)
                    flag = True
                    break
            if flag:
                break
    print(math.lcm(*cycles))


def part_one():
    nodes, move = prepare_nodes()
    curr_node = "AAA"
    res = 0
    while True:
        for c in move:
            if c == "L":
                curr_node = nodes[curr_node][0]
            else:
                curr_node = nodes[curr_node][1]
            res += 1
            if curr_node == "ZZZ":
                print(res)
                return


if __name__ == "__main__":
    part_one()
    part_two()
