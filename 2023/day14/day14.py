file = "in14"


def calculate_weight(rocks):
    res = 0
    for c in range(len(rocks[0])):
        for row in range(len(rocks)):
            if rocks[row][c] == "O":
                res += len(rocks) - row
    return res


def iterate(rocks, d):
    rocks = list(rocks)
    rocks = list(map(list, rocks))
    if d == "north":
        for c in range(len(rocks[0])):
            for row in range(len(rocks)):
                if rocks[row][c] == "O":
                    rocks[row][c] = "."
                    while row > 0:
                        if rocks[row - 1][c] == "#" or rocks[row - 1][c] == "O":
                            rocks[row][c] = "O"
                            break
                        row -= 1
                    else:
                        rocks[0][c] = "O"
    elif d == "south":
        for c in range(len(rocks[0])):
            for row in reversed(range(len(rocks))):
                if rocks[row][c] == "O":
                    rocks[row][c] = "."
                    while row < len(rocks) - 1:
                        if rocks[row + 1][c] == "#" or rocks[row + 1][c] == "O":
                            rocks[row][c] = "O"
                            break
                        row += 1
                    else:
                        rocks[-1][c] = "O"
    elif d == "west":
        for row in range(len(rocks)):
            for c in range(len(rocks[0])):
                if rocks[row][c] == "O":
                    rocks[row][c] = "."
                    while c > 0:
                        if rocks[row][c - 1] == "#" or rocks[row][c - 1] == "O":
                            rocks[row][c] = "O"
                            break
                        c -= 1
                    else:
                        rocks[row][0] = "O"
    elif d == "east":
        for row in range(len(rocks)):
            for c in reversed(range(len(rocks[0]))):
                if rocks[row][c] == "O":
                    rocks[row][c] = "."
                    while c < len(rocks[0]) - 1:
                        if rocks[row][c + 1] == "#" or rocks[row][c + 1] == "O":
                            rocks[row][c] = "O"
                            break
                        c += 1
                    else:
                        rocks[row][-1] = "O"
    rocks = tuple(map(tuple, rocks))
    return tuple(rocks)


def part_one():
    with open(file) as f:
        rocks = []
        for l in f:
            rocks.append([*l.rstrip()])
        print(calculate_weight(iterate(rocks, "north")))


def part_two():
    with open(file) as f:
        rocks = []
        for l in f:
            rocks.append(tuple([*l.rstrip()]))
        rocks = tuple(rocks)
        dirs = ["north", "west", "south", "east"]
        i = 0
        configs = {}
        vals = []
        while i < 1000:
            for d in dirs:
                rocks = iterate(rocks, d)
            vals.append(calculate_weight(rocks))
            if rocks in configs:
                org_idx = configs[rocks]
                period = i - org_idx
                print(vals[org_idx + (1000000000 - org_idx - 1) % period])
                break
            configs[rocks] = i
            i += 1


if __name__ == "__main__":
    part_one()
    part_two()
