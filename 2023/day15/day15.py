file = "in15"


def hash_code(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def part_one():
    with open(file) as f:
        res = 0
        for l in f:
            codes = l.rstrip().split(",")
            for c in codes:
                res += hash_code(c)
        print(res)


def part_two():
    with open(file) as f:

        lenses = [{} for _ in range(256)]
        for l in f:
            codes = l.rstrip().split(",")
            for c in codes:
                if "-" in c:
                    c = c.replace("-", '')
                    h = hash_code(c)
                    if c in lenses[h]:
                        lenses[h].pop(c)
                elif "=" in c:
                    c = c.split("=")
                    h = hash_code(c[0])
                    strength = int(c[1])
                    lenses[h][c[0]] = strength
        res = 0
        for i, b in enumerate(lenses):
            for j, k in enumerate(b):
                res += (i + 1) * (j + 1) * b[k]
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
