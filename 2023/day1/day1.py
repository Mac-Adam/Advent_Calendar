def part_one():
    res = 0
    with open("./in1.txt") as file:
        for line in file:
            for c in line:
                try:
                    res += 10 * int(c)
                    break
                except ValueError:
                    continue

            for c in reversed(line):
                try:
                    res += int(c)
                    break
                except ValueError:
                    continue

    print(res)


def part_two():
    res = 0
    digits = [
        (1, '1', 'one'),
        (2, '2', 'two'),
        (3, '3', 'three'),
        (4, '4', 'four'),
        (5, '5', 'five'),
        (6, '6', 'six'),
        (7, '7', 'seven'),
        (8, '8', 'eight'),
        (9, '9', 'nine')
    ]
    with open("./in1.txt") as file:

        for line in file:
            found = []
            for d in digits:

                for i in range(1, 3):
                    idx = line.find(d[i])
                    if idx >= 0:
                        found.append((idx, d[0]))

            res += 10 * min(found, key=lambda x: x[0])[1]
            found = []
            for d in digits:
                for i in range(1, 3):
                    idx = line.rfind(d[i])
                    if idx >= 0:
                        found.append((idx, d[0]))
            res += max(found, key=lambda x: x[0])[1]
    print(res)


if __name__ == "__main__":
    part_one()
    part_two()
