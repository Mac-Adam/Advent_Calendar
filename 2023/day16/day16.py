file = "in16"


def move_beam(b, w, h):
    new_pos = (b[0][0] + b[1][0], b[0][1] + b[1][1])
    if 0 <= new_pos[0] < h and 0 <= new_pos[1] < w:
        return (b[0][0] + b[1][0], b[0][1] + b[1][1]), b[1]
    return None


def interact(b, mirrors):
    n = mirrors[b[0][0]][b[0][1]]
    interactions = {
        '/': lambda x: (x[0], (-x[1][1], -x[1][0])),
        '\\': lambda x: (x[0], (x[1][1], x[1][0])),
        '|': lambda x: x if x[1][1] == 0 else [(x[0], (1, 0)), (x[0], (-1, 0))],
        '-': lambda x: x if x[1][0] == 0 else [(x[0], (0, 1)), (x[0], (0, -1))],
    }
    if n in interactions:
        return interactions[n](b)
    return b


def find_num(s, mirrors):
    beams = [s]
    new_beams = []
    h = len(mirrors)
    w = len(mirrors[0])
    been_to = {}
    while beams:
        temp = []
        for b in beams:
            temp.append(move_beam(b, w, h))
        temp = list(filter(lambda x: x, temp))
        for b in temp:
            n = interact(b, mirrors)
            if isinstance(n, list):
                new_beams.extend(n)
            else:
                new_beams.append(n)
        new_beams = list(filter(lambda x: x not in been_to, new_beams))
        for n in new_beams:
            been_to[n] = 1
        beams = new_beams
        new_beams = []
    s = set()
    for k in been_to:
        s.add(k[0])
    return len(s)


def part_one():
    with open(file) as f:
        mirrors = []
        for l in f:
            l = l.rstrip()
            mirrors.append(l)
        print(find_num(((0, -1), (0, 1)), mirrors))


def part_two():
    with open(file) as f:
        curr_max = 0
        mirrors = []
        for l in f:
            l = l.rstrip()
            mirrors.append(l)
        h = len(mirrors)
        w = len(mirrors[0])
        for i in range(h):
            curr_max = max(curr_max, find_num(((i, -1), (0, 1)), mirrors))
            curr_max = max(curr_max, find_num(((i, w), (0, -1)), mirrors))
        for i in range(w):
            curr_max = max(curr_max, find_num(((-1, i), (1, 0)), mirrors))
            curr_max = max(curr_max, find_num(((h, i), (-1, 0)), mirrors))
        print(curr_max)


if __name__ == "__main__":
    part_one()
    part_two()
