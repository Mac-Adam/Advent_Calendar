file = "in13"


def reverse(pattern):
    temp = list(zip(*pattern))
    temp = list(map(lambda x: ''.join(x), temp))
    return temp


def diff(a, b):
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    return res


def part_one():
    with open(file) as f:
        patters = []
        p = []
        for l in f:
            if l == "\n":
                patters.append(p)
                p = []
            else:
                p.append(l.rstrip())
        patters.append(p)
        res = 0
        for p in patters:
            rp = reverse(p)
            for i in range(len(rp) - 1):
                if rp[i] == rp[i + 1]:
                    j = 0
                    while i - j >= 0 and j + i + 1 < len(rp):
                        if rp[i - j] != rp[i + j + 1]:
                            break
                        j += 1
                    else:
                        res += (i + 1)
            for i in range(len(p) - 1):
                if p[i] == p[i + 1]:
                    j = 0
                    while i - j >= 0 and j + i + 1 < len(p):
                        if p[i - j] != p[i + j + 1]:
                            break
                        j += 1
                    else:
                        res += 100 * (i + 1)
        print(res)


def part_two():
    with open(file) as f:
        patters = []
        p = []
        for l in f:
            if l == "\n":
                patters.append(p)
                p = []
            else:
                p.append(l.rstrip())
        patters.append(p)
        res = 0
        for p in patters:
            rp = reverse(p)
            for i in range(len(rp) - 1):
                if diff(rp[i], rp[i + 1]) <= 1:
                    d = diff(rp[i], rp[i + 1])
                    j = 1
                    while i - j >= 0 and j + i + 1 < len(rp):
                        d += diff(rp[i - j], rp[i + j + 1])
                        if d > 1:
                            break
                        j += 1
                    else:
                        if d == 1:
                            res += (i + 1)
            for i in range(len(p) - 1):
                if diff(p[i], p[i + 1]) <= 1:
                    d = diff(p[i], p[i + 1])
                    j = 1
                    while i - j >= 0 and j + i + 1 < len(p):
                        d += diff(p[i - j], p[i + j + 1])
                        if d > 1:
                            break
                        j += 1
                    else:
                        if d == 1:
                            res += 100 * (i + 1)
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
