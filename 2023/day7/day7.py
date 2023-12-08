file = "in7"


def get_rank(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    items = d.items()
    items = sorted(items, key=lambda x: x[1], reverse=True)
    if items[0][1] == 5:
        return 6
    if items[0][1] == 4:
        return 5
    if items[0][1] == 3 and items[1][1] == 2:
        return 4
    if items[0][1] == 3 and items[1][1] != 2:
        return 3
    if items[0][1] == 2 and items[1][1] == 2:
        return 2
    if items[0][1] == 2 and items[1][1] != 2:
        return 1
    return 0


def get_rank2(s):
    d = {}
    s2 = s.replace("J", '')
    j_count = len(s) - len(s2)
    for c in s2:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    items = d.items()
    items = sorted(items, key=lambda x: x[1], reverse=True)
    if items:
        items[0] = (items[0][0], items[0][1] + j_count)
    else:
        return 6
    if items[0][1] == 5:
        return 6
    if items[0][1] == 4:
        return 5
    if items[0][1] == 3 and items[1][1] == 2:
        return 4
    if items[0][1] == 3 and items[1][1] != 2:
        return 3
    if items[0][1] == 2 and items[1][1] == 2:
        return 2
    if items[0][1] == 2 and items[1][1] != 2:
        return 1
    return 0


def part_one():
    with open(file) as f:
        data = []
        for line in f:
            line = line.split()
            d = (line[0], int(line[1]))
            data.append(d)
        lut = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14

        }
        data = sorted(data, key=lambda x: [get_rank(x[0]), *map(lambda y: lut[y], x[0])])
        res = 0
        for i, x in enumerate(data):
            res += (i + 1) * x[1]
        print(res)


def part_two():
    with open(file) as f:
        data = []
        for line in f:
            line = line.split()
            d = (line[0], int(line[1]))
            data.append(d)
        lut = {
            "J": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "Q": 11,
            "K": 12,
            "A": 13

        }
        data = sorted(data, key=lambda x: [get_rank2(x[0]), *map(lambda y: lut[y], x[0])])
        res = 0
        for i, x in enumerate(data):
            res += (i + 1) * x[1]
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
