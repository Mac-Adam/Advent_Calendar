import numpy as np

file = 'in21'


def get_next_steps(curr, garden):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = []
    for d in dirs:
        next_c = curr[0] + d[0], curr[1] + d[1]
        w = len(garden[0])
        h = len(garden)
        if 0 <= next_c[0] < h and 0 <= next_c[1] < w and garden[next_c] != '#':
            res.append(next_c)
    return res


def solution():
    with open(file) as f:
        garden_map = []
        for l in f:
            l = l.rstrip()
            garden_map.append(list(l))
        for row in range(len(garden_map)):
            for col in range(len(garden_map[0])):
                if garden_map[row][col] == 'S':
                    rute = {(row, col)}
        garden_map = np.array(garden_map)
        next_rute = set()
        reach_map = {}
        last = -1
        i = 0
        while 1:
            if len(reach_map) == last:
                break
            last = len(reach_map)
            for t in rute:
                if t not in reach_map:
                    reach_map[t] = i
                next_steps = get_next_steps(t, garden_map)
                for s in next_steps:
                    if s in reach_map:
                        continue
                    next_rute.add(s)
            rute = next_rute
            next_rute = set()
            i += 1
        res1 = 0
        for k, v in reach_map.items():
            if v <= 64 and v % 2 == 0:
                res1 += 1
        print(res1)

        tiled_map = []
        n = 7
        for _ in range(n):
            for i in range(len(garden_map)):
                rest = garden_map[i]
                for j in range(len(rest)):
                    if rest[j] == "S":
                        rest[j] = '.'
                tiled_map.append(list(rest) * n)
        garden_map = np.array(tiled_map)
        next_rute = set()
        reach_map2 = {}
        last = -1
        i = 0
        rute = {(len(tiled_map) // 2, len(tiled_map) // 2)}
        while 1:
            if len(reach_map2) == last:
                break
            last = len(reach_map2)
            for t in rute:
                if t not in reach_map2:
                    reach_map2[t] = i
                next_steps = get_next_steps(t, garden_map)
                for s in next_steps:
                    if s in reach_map2:
                        continue
                    next_rute.add(s)
            rute = next_rute
            next_rute = set()
            i += 1

        siz = len(tiled_map) // n
        max_dist = 26501365
        res = 0

        for k, v in reach_map.items():
            this_tile = 0
            tiles = [(i, j) for i in range(n) for j in range(n)]
            for t in tiles:
                if reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])] % 2 == max_dist % 2:
                    this_tile += 1
            # top
            for t in [(0, j) for j in range(1, n - 1)]:
                last_calc_tile = reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])]
                moves_left = (max_dist - last_calc_tile) // siz
                this_tile += moves_left // 2
                if moves_left % 2 == 1 and (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                    this_tile += 1
            # bot
            for t in [(n - 1, j) for j in range(1, n - 1)]:
                last_calc_tile = reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])]
                moves_left = (max_dist - last_calc_tile) // siz
                this_tile += moves_left // 2
                if moves_left % 2 == 1 and (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                    this_tile += 1
            # left
            for t in [(j, 0) for j in range(1, n - 1)]:
                last_calc_tile = reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])]
                moves_left = (max_dist - last_calc_tile) // siz
                this_tile += moves_left // 2
                if moves_left % 2 == 1 and (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                    this_tile += 1
            # right
            for t in [(j, n - 1) for j in range(1, n - 1)]:
                last_calc_tile = reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])]
                moves_left = (max_dist - last_calc_tile) // siz
                this_tile += moves_left // 2
                if moves_left % 2 == 1 and (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                    this_tile += 1
            # corners
            for t in [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]:
                temp = 0
                last_calc_tile = reach_map2[(k[0] + siz * t[0], k[1] + siz * t[1])]
                moves_left = (max_dist - last_calc_tile) // siz
                temp += moves_left // 2
                if moves_left % 2 == 1:
                    if (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                        this_tile += (2 + 2 * (temp + 1)) / 2 * (temp + 1)
                    else:
                        this_tile += (3 + (2 * temp) + 1) / 2 * temp
                else:
                    if (max_dist - siz * moves_left - last_calc_tile) % 2 == 0:
                        this_tile += (3 + 2 * temp + 1) / 2 * temp
                    else:
                        this_tile += (2 + 2 * temp) / 2 * temp
            res += this_tile

            # input()
        print(int(res))


if __name__ == "__main__":
    solution()
