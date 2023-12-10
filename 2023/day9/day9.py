file = "in9"


def propagate_forward(data):
    new_data = []
    for i in range(len(data) - 1):
        new_data.append(data[i + 1] - data[i])
    return new_data


def part_one():
    with open(file) as f:
        res = 0
        for line in f:
            data = line.split()
            data = list(map(int, data))
            old = []
            while any(data):
                old.append(data)
                data = propagate_forward(data)
            old.append(data)
            for i in reversed(range(len(old) - 1)):
                old[i].append(old[i][-1] + old[i + 1][-1])
            res += old[0][-1]

        print(res)


def part_two():
    with open(file) as f:
        res = 0
        for line in f:
            data = line.split()
            data = list(map(int, data))
            old = []
            while any(data):
                old.append(data)
                data = propagate_forward(data)
            old.append(data)
            for i in reversed(range(len(old) - 1)):
                old[i] = [(old[i][0] - old[i + 1][0])] + old[i]
            res += old[0][0]
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
