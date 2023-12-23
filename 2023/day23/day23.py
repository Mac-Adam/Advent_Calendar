import numpy as np
from copy import deepcopy

file = 'in23'


def part_one():
    maze = []
    with open(file) as f:
        for l in f:
            l = l.rstrip()
            maze.append(list(l))
        maze = np.array(maze)

    paths = [((1, 1), set())]
    w = len(maze[0])
    h = len(maze)
    results = [0]
    while paths:
        new_paths = []
        for path in paths:
            curr_pos, been_to = path
            been_to.add(curr_pos)

            if curr_pos[0] >= h - 1 or curr_pos[1] >= w - 1:
                results.append(len(been_to))
                continue
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if maze[curr_pos] == '<':
                dirs = [(0, -1)]
            elif maze[curr_pos] == '>':
                dirs = [(0, 1)]
            elif maze[curr_pos] == '^':
                dirs = [(-1, 0)]
            elif maze[curr_pos] == 'v':
                dirs = [(1, 0)]
            split = False
            for d in dirs:
                next_pos = curr_pos[0] + d[0], curr_pos[1] + d[1]
                if maze[next_pos] == '#' or next_pos in been_to:
                    continue
                if split:
                    new_paths.append((next_pos, deepcopy(been_to)))
                else:
                    new_paths.append((next_pos, been_to))
                    split = True
        paths = new_paths
    print(max(results))


def part_two():
    maze = []
    with open(file) as f:
        for l in f:
            l = l.rstrip()
            maze.append(list(l))
        maze = np.array(maze)
    w = len(maze[0])
    h = len(maze)
    nodes = {}
    trails = [((1, 1), (1, 1), set())]
    global_been_to = set()
    while trails:
        new_trails = []
        for trail in trails:
            curr_pos, pos_from, been_to = trail
            been_to.add(curr_pos)
            global_been_to.add(curr_pos)
            if curr_pos[0] >= h - 1 or curr_pos[1] >= w - 1:
                if pos_from in nodes:
                    nodes[pos_from].append(((h, w), len(been_to)))
                else:
                    nodes[pos_from] = [((h, w), len(been_to))]
                continue
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            possible_paths = []
            for d in dirs:
                next_pos = curr_pos[0] + d[0], curr_pos[1] + d[1]
                if maze[next_pos] == '#' or next_pos in been_to:
                    continue
                possible_paths.append(next_pos)
            if len(possible_paths) == 1:
                new_trails.append((possible_paths[0], pos_from, been_to))
            else:
                if pos_from in nodes:
                    nodes[pos_from].append((curr_pos, len(been_to)))
                else:
                    nodes[pos_from] = [(curr_pos, len(been_to))]
                for new_trail in possible_paths:
                    if new_trail in global_been_to:
                        continue
                    new_trails.append((new_trail, curr_pos, {curr_pos}))
        trails = new_trails
    print(nodes)

    for node, conn in nodes.items():
        for other in conn:
            cords, dist = other
            if cords not in nodes:
                continue
            if (node, dist) not in nodes[cords]:
                nodes[cords].append((node, dist))
    print(nodes)

    paths = [((1, 1), [], 0)]

    results = [0]
    while paths:
        new_paths = []
        for path in paths:
            curr_pos, been_to, curr_len = path
            been_to.append(curr_pos)
            if curr_pos == (h, w):
                print(curr_len + 2 - len(been_to))
                results.append(curr_len + 2 - len(been_to))
                continue
            for next_node in nodes[curr_pos]:
                cords, dist = next_node
                if cords in been_to:
                    continue
                new_paths.append((cords, deepcopy(been_to), curr_len + dist))
        paths = new_paths
    print(max(results))


if __name__ == "__main__":
    part_one()
    part_two()
