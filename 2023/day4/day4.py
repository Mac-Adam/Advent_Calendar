file = 'in4.txt'


def get_winings(line):
    line = line.replace("\n", "")
    data = line.split(":")[1]
    nums = data.split("|")
    win = set(map(int, nums[0][1:-1].split()))
    have = set(map(int, nums[1][1:].split()))
    have_win = win.intersection(have)
    return len(have_win)


def part_one():
    res = 0
    with open(file) as f:
        for line in f:
            win = get_winings(line)
            if win != 0:
                res += 2 ** (win - 1)

    print(res)


def part_two():
    with open(file) as f:
        lines = f.readlines()
        scratchcards = [1 for _ in range(len(lines))]
        i = 0
        for line in lines:
            win = get_winings(line)
            for j in range(i + 1, i + win + 1):
                scratchcards[j] += scratchcards[i]
            i += 1

    print(sum(scratchcards))


if __name__ == "__main__":
    part_one()
    part_two()
