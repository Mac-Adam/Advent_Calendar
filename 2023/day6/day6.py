import math

file = "in6.txt"


def part_two():
    with open(file) as f:
        lines = f.readlines()
        times = lines[0].split(":")[1].split()
        time = int("".join(times))
        dist = lines[1].split(":")[1].split()
        dist = int("".join(dist))

        h1 = math.ceil((time - math.sqrt(time ** 2 - 4 * dist)) / 2)
        h2 = math.floor((time + math.sqrt(time ** 2 - 4 * dist)) / 2)

        num = h2 - h1 + 1
        if h1 * (time - h1) == dist:
            num -= 1
        if h2 * (time - h2) == dist:
            num -= 1

        print(num)


def part_one():
    with open(file) as f:
        lines = f.readlines()
        times = lines[0].split(":")[1].split()
        times = [int(t) for t in times]
        dist = lines[1].split(":")[1].split()
        dist = [int(d) for d in dist]
        res = 1
        for t, d in zip(times, dist):
            h1 = math.ceil((t - math.sqrt(t ** 2 - 4 * d)) / 2)
            h2 = math.floor((t + math.sqrt(t ** 2 - 4 * d)) / 2)

            num = h2 - h1 + 1
            if h1 * (t - h1) == d:
                num -= 1
            if h2 * (t - h2) == d:
                num -= 1
            res *= num

        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
