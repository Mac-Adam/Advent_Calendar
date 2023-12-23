import numpy as np

file = 'in22'


def solution():
    # seems the inputs fit this
    tiles = np.zeros((10, 10, 400), int)
    resting_on = {}
    bricks = []
    with open(file) as f:
        for l in f:
            l = l.rstrip()
            start, end = l.split('~')
            start = tuple([int(x) for x in start.split(',')])
            end = tuple([int(x) for x in end.split(',')])
            bricks.append((start, end))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    for i, brick in enumerate(bricks):
        brick_id = i + 1
        start, end = brick
        lowest_z = min(start[2], end[2])
        highest_z = max(start[2], end[2])
        stop = False

        for z in range(lowest_z - 1, -1, -1):
            temp_rest = set()
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    if tiles[x, y, z] != 0:
                        stop = True
                        temp_rest.add(tiles[x, y, z])
            resting_on[brick_id] = temp_rest
            if stop:
                break
        if stop:
            z += 1
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(z, z + end[2] - start[2] + 1):
                    tiles[x, y, z] = brick_id
    solo_supports = {}
    for brick, supports in resting_on.items():
        if len(supports) == 1:
            solo_supports[next(iter(supports))] = brick
    res1 = 0
    for i in range(1, brick_id + 1):
        if i not in solo_supports:
            res1 += 1
    print(res1)
    res2 = 0
    for s in solo_supports:
        curr_falling = {s}
        added = True
        while added:
            added = False
            for brick, supports in resting_on.items():
                if not supports:
                    continue
                if brick in curr_falling:
                    continue
                for sup in supports:
                    if sup not in curr_falling:
                        break
                else:
                    added = True
                    curr_falling.add(brick)
        res2 += len(curr_falling) - 1
    print(res2)


if __name__ == "__main__":
    solution()
