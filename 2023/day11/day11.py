file = "in11"


def empty_between(a, b, l):
    res = 0
    if a > b:
        a, b = b, a
    for x in l:
        if x < a:
            continue
        if a < x < b:
            res += 1
        if b < x:
            break
    return res


def solution():
    with open(file) as f:
        galaxies = []
        empty_rows = []
        empty_cols = []
        for i, line in enumerate(f):
            line = line.rstrip()
            if '#' not in line:
                empty_rows.append(i)
            galaxies.append(line)
        for i in range(len(galaxies[0])):
            flag = True
            for j in range(len(galaxies)):
                if galaxies[j][i] == "#":
                    flag = False
            if flag:
                empty_cols.append(i)
        cords = []
        for i in range(len(galaxies[0])):
            for j in range(len(galaxies)):
                if galaxies[j][i] == "#":
                    cords.append((j, i))
        exp = [2, 10, 100, 1000000]
        for e in exp:
            res = 0
            for first in range(len(cords)):
                for second in range(first):
                    res += abs(cords[second][0] - cords[first][0]) + abs(cords[second][1] - cords[first][1]) + (
                            e - 1) * (
                                   empty_between(cords[second][0], cords[first][0], empty_rows) + empty_between(
                               cords[second][1], cords[first][1], empty_cols))
            print("expansion: ", e, ", result: ", res)


if __name__ == "__main__":
    solution()
