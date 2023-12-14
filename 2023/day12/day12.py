import math
import itertools

file = "test"


def check(data, rows):
    streak = 0
    try:

        for c in data:
            if c == "#":
                streak += 1
            elif c == "." or c == "?":
                if streak != 0:
                    if streak != rows.pop(0):
                        return False
                    streak = 0
    except IndexError:
        return False
    if rows:
        if len(rows) == 1 and rows[0] == streak:
            return True
        return False

    return True


def islands_after(data):
    island = False
    curr = 0
    res = [0] * len(data)
    for i in reversed(range(len(data))):
        if data[i] == "#":
            island = True
        else:
            if island:
                curr += 1
            island = False
        res[i] = curr
    return res


def find_possible_places(data, l, start=0):
    idx = []
    streak = 0
    last_possible = len(data)
    for i in range(start, len(data)):
        if data[i] == "#" or data[i] == "?":
            if data[i] == "#" and last_possible == len(data):
                last_possible = i
            streak += 1
        else:
            streak = 0
        if streak >= l:

            index = i - l + 1
            idx.append(index)
            if index >= last_possible:
                return idx
    return idx


def solution():
    with open(file) as f:
        res = 0
        for line in f:
            line = line.rstrip().split(" ")
            data = list(line[0])
            rows = line[1].split(",")
            rows = list(map(int, rows))
            last = [0] * len(data)
            curr = [0] * len(data)
            curr_start = 0
            next_start = 0
            islands = islands_after(data)
            for j in range(len(rows)):
                max_end = len(data)
                streak = 0
                s = 1 if j == 0 else 0
                print(last)
                for i in range(curr_start, len(data)):

                    if i > rows[j]:
                        s += last[i - rows[j] - 1]
                    if i > max_end:
                        break
                    if len(rows) - 1 == j and islands[i] > 0:
                        # print(i)
                        continue
                    if data[i] == "#" or data[i] == "?":
                        if data[i] == "#" and max_end == len(data):
                            max_end = i + rows[j] - 1
                        streak += 1
                    if data[i] == ".":
                        streak = 0
                    # print(i, streak)
                    if streak >= rows[j]:
                        if i != len(data) - 1:
                            if data[i + 1] != "#":
                                if next_start == curr_start:
                                    next_start = i + 2
                                curr[i] = s
                        else:
                            if next_start == curr_start:
                                next_start = i + 2
                            curr[i] = s
                # print(curr, next_start)
                curr_start = next_start
                last = curr
                curr = [0] * len(data)
            print(data, last, sum(last))
            res += sum(last)

            # t1 = sum(last)
            # q_idx = []
            # q_num = 0
            # t2 = 0
            # for i, c in enumerate(data):
            #     if c == "?":
            #         q_idx.append(i)
            #         q_num += 1
            # n_to_place = sum(rows) - data.count("#")
            #
            # for c in itertools.combinations(q_idx, n_to_place):
            #
            #     d = data[:]
            #     for i in c:
            #         d[i] = "#"
            #     if check(d, rows[:]):
            #         res += 1
            #         t2 += 1
            # print(t1, t2)
        print(res)


def part_one():
    with open(file) as f:
        res = 0
        for line in f:
            line = line.rstrip().split(" ")
            data = list(line[0])
            rows = line[1].split(",")
            rows = list(map(int, rows))
            q_idx = []
            q_num = 0
            for i, c in enumerate(data):
                if c == "?":
                    q_idx.append(i)
                    q_num += 1
            n_to_place = sum(rows) - data.count("#")

            for c in itertools.combinations(q_idx, n_to_place):

                d = data[:]
                for i in c:
                    d[i] = "#"
                if check(d, rows[:]):
                    res += 1

        print(res)


if __name__ == "__main__":
    part_one()
    solution()
