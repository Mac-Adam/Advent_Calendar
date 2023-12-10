file = "in10"
#       right 0  left 1  up 2   down 3
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
ways = {
    "|": (dirs[2], dirs[3]),
    "-": (dirs[0], dirs[1]),
    "L": (dirs[0], dirs[2]),
    "F": (dirs[0], dirs[3]),
    "7": (dirs[1], dirs[3]),
    "J": (dirs[1], dirs[2]),
    ".": ((0, 0), (0, 0)),
}


def add_coordinates(a, b):
    return a[0] + b[0], a[1] + b[1]


def check_coordinates(a, w, h):
    return 0 <= a[0] < h and 0 <= a[1] < w


def possible_coordinates(a, t):
    return add_coordinates(a, ways[t][0]), add_coordinates(a, ways[t][1])


def next_coordinates(p, a, t):
    if p == add_coordinates(a, ways[t][0]):
        return add_coordinates(a, ways[t][1])
    return add_coordinates(a, ways[t][0])


def pick_dir(a, w, h):
    dist = [w - a[1], a[1] + 1, a[0] + 1, h - a[0]]
    low_dist = min(dist)
    return dirs[dist.index(low_dist)]


def solution():
    with (open(file) as f):
        pipes = []

        for line in f:
            pipes.append(line.rstrip())
        width = len(pipes[0])
        height = len(pipes)

        for row in range(height):
            for col in range(width):
                if pipes[row][col] == "S":
                    way = [(row, col), (row, col)]
                    start = (row, col)

        for d in dirs:
            new = add_coordinates(start, d)
            if check_coordinates(new, width, height):
                first, sec = possible_coordinates(new, pipes[new[0]][new[1]])
                if first == start or sec == start:
                    way = new
        dist = 1
        loop = [start, way]
        prev = start
        while way != start:
            pipe = pipes[way[0]][way[1]]
            next_pipe = next_coordinates(prev, way, pipe)
            prev = way
            way = next_pipe
            loop.append(next_pipe)
            dist += 1

        print((len(loop) - 1) // 2)
        new_pipes = [["." for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]
        for i in range(len(loop) - 1):
            new_cords = loop[i][0] * 2 + 1, loop[i][1] * 2 + 1
            new_pipes[new_cords[0]][new_cords[1]] = pipes[loop[i][0]][loop[i][1]]
            diff = loop[i + 1][0] - loop[i][0], loop[i + 1][1] - loop[i][1]
            if diff[0] == 0:
                new_pipes[new_cords[0]][new_cords[1] + diff[1]] = "-"
            else:
                new_pipes[new_cords[0] + diff[0]][new_cords[1]] = "|"
        res = 0
        for row in range(1, height * 2 + 1, 2):
            for col in range(1, width * 2 + 1, 2):
                if new_pipes[row][col] == ".":
                    new_cords = row - 1, col - 1

                    cnt = 0
                    while new_cords[0] >= 0:
                        if new_pipes[new_cords[0]][new_cords[1]] == "-":
                            cnt += 1
                        new_cords = new_cords[0] - 1, new_cords[1]
                    if cnt % 2 == 1:
                        res += 1
        print(res)


if __name__ == "__main__":
    solution()
