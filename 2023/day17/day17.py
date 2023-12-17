import numpy as np

file = "in17"


def in_been_to(node, been_to):
    if (node[0], node[1]) in been_to and node[2] in been_to[(node[0], node[1])]:
        return True
    return False


def update_been_to(node, been_to):
    if (node[0], node[1]) in been_to:
        been_to[(node[0], node[1])].add(node[2])
    else:
        been_to[(node[0], node[1])] = {node[2]}


def next_positions(p, w, h, nodes):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    next_pos = []
    for d in dirs:
        if p[2] == d:
            next_len = p[1] + 1
        else:
            next_len = 1
        if p[1] >= 3 and p[2] == d:
            continue
        new_id = p[0][0] + d[0], p[0][1] + d[1]
        if 0 <= new_id[0] < h and 0 <= new_id[1] < w:
            next_pos.append((new_id, next_len, d, p[3] + nodes[new_id], p[0]))
    return next_pos


def update_q(new_node, q):
    for i in range(len(q)):
        n = q[i]
        if n[0] == new_node[0] and n[1] == new_node[1]:
            q[i] = q[i][0], q[i][1], min(new_node[2], q[i][2])
            return
    q.append(new_node)


def min_heat_loss(s, e, nodes, min_d, max_d):
    # 0 - pos
    # 1 - dir
    # 2 - heat
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(s, (0, 0), 0)]  # nodes[s])]
    been_to = {(s, (0, 0))}
    w = len(nodes[0])
    h = len(nodes)
    while q[0][0] != e:
        curr_node = q.pop(0)
        for d in dirs:
            if d == curr_node[1]:
                # print("skipped: ", d)
                continue
            for i in range(min_d, max_d + 1):
                new_id = curr_node[0][0] + d[0] * i, curr_node[0][1] + d[1] * i
                if 0 <= new_id[0] < h and 0 <= new_id[1] < w:
                    if (new_id, d) in been_to:
                        # print("was in: ", new_id, d)
                        continue
                    # print(curr_node[0], new_id)
                    ids_for_heat = [(curr_node[0][0] + d[0] * j, curr_node[0][1] + d[1] * j) for j in range(1, i + 1)]
                    # print(ids_for_heat)
                    additional_heat = sum([nodes[idx] for idx in ids_for_heat])
                    # print([nodes[idx] for idx in ids_for_heat], additional_heat, curr_node, i)
                    update_q((new_id, d, curr_node[2] + additional_heat), q)
                    # print("adding:", (new_id, d, curr_node[2] + additional_heat))
        been_to.add((curr_node[0], curr_node[1]))
        q.sort(key=lambda x: x[2])
        # print(q)
        # input()

    return q[0][2]


def part_one():
    with open(file) as f:
        nodes = []
        for line in f:
            nodes.append([int(x) for x in line.rstrip()])
        nodes = np.array(nodes)
        end = (len(nodes) - 1, len(nodes[0]) - 1)
        print(min_heat_loss((0, 0), end, nodes, 1, 3))
        print(min_heat_loss((0, 0), end, nodes, 4, 10))


if __name__ == "__main__":
    part_one()
