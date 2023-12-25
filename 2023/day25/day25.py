import random

file = "in25"


def part_one():
    conn = {}
    edges_basic = []
    nodes = set()
    with open(file) as f:
        for l in f:
            l = l.rstrip()
            conn_from, conn_to = l.split(':')
            conn_to = conn_to.strip().split(' ')
            nodes.add(conn_from)
            for c in conn_to:
                nodes.add(c)
                if conn_from in conn:
                    conn[conn_from].add(c)
                else:
                    conn[conn_from] = {c}
                if c in conn:
                    conn[c].add(conn_from)
                else:
                    conn[c] = {conn_from}
                edges_basic.append((conn_from, c))
    iter = 0
    while True:
        iter += 1
        node_weight = {n: 1 for n in nodes}
        edges = edges_basic[:]
        while len(node_weight) > 2:
            rand_edge = random.choice(edges)
            while rand_edge in edges:
                edges.remove(rand_edge)
            edge_rev = rand_edge[1], rand_edge[0]
            while edge_rev in edges:
                edges.remove(edge_rev)
            if rand_edge[0] == rand_edge[1]:
                continue
            v1, v2 = rand_edge
            node_weight[v1] += node_weight[v2]
            del node_weight[v2]
            to_remove = []
            for i in range(len(edges)):
                if edges[i][0] == v2:
                    edges[i] = v1, edges[i][1]
                elif edges[i][1] == v2:
                    edges[i] = edges[i][0], v1
            for rm in to_remove:
                edges.remove(rm)
            # print(edges)

        if len(edges) == 3:
            print(node_weight, iter)
            res = 1
            for k, v in node_weight.items():
                res *= v
            print(res)
            break
        print(iter)


if __name__ == "__main__":
    part_one()
