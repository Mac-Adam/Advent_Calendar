file = 'in18'

dirs = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


def part_one():
    with open(file) as f:
        curr = (0, 0)
        curr_a = 0
        curr_ob = 1
        for l in f:
            l = l.rstrip().split()
            d = dirs[l[0]]
            dist = int(l[1])
            next_point = curr[0] + d[0] * dist, curr[1] + d[1] * dist
            curr_ob += dist
            if l[0] == "R":
                curr_a += dist * curr[1]
            if l[0] == "L":
                curr_a -= (dist * curr[1])
            curr = next_point
        print(curr_a + curr_ob // 2 + 1)


def decode(c):
    d = "RDLU"[int(c[-1])]
    c = c[:-1]
    conv = {"0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15,
            }
    res = 0
    mul = 0
    for char in reversed(c):
        res += conv[char] * (16 ** mul)
        mul += 1
    return res, d


def part_two():
    with open(file) as f:
        curr = (0, 0)
        curr_a = 0
        curr_ob = 1
        for l in f:
            l = l.rstrip().split()
            c = l[2][2:-1]
            dist, d_s = decode(c)
            d = dirs[d_s]
            next_point = curr[0] + d[0] * dist, curr[1] + d[1] * dist
            curr_ob += dist
            if d_s == "R":
                curr_a += dist * curr[1]
            if d_s == "L":
                curr_a -= (dist * curr[1])
            curr = next_point
        print(curr_a + curr_ob // 2 + 1)


if __name__ == "__main__":
    part_one()
    part_two()
