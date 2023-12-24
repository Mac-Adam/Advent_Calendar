file = "in24"


def check_intersection(p1, p2, v1, v2, x_range, y_range):
    if v1[1] * v2[0] == v1[0] * v2[1]:
        return False
    a1 = v1[1] / v1[0]
    a2 = v2[1] / v2[0]
    b1 = p1[1] - a1 * p1[0]
    b2 = p2[1] - a2 * p2[0]

    inter_x = (b2 - b1) / (a1 - a2)

    if (inter_x - p1[0]) * v1[0] < 0 or (inter_x - p2[0]) * v2[0] < 0:
        return False

    inter_y = a1 * inter_x + b1

    if x_range[0] <= inter_x <= x_range[1] and y_range[0] <= inter_y <= y_range[1]:
        return True
    return False


def part_one():
    hailstones = []
    with open(file) as f:
        for l in f:
            l = l.strip().replace(' ', '')
            p, v = l.split("@")
            p = [int(x) for x in p.split(',')]
            v = [int(x) for x in v.split(',')]
            hailstones.append((p, v))
    res = 0
    for i in range(len(hailstones)):
        for j in range(i):
            p1, v1 = hailstones[i]
            p2, v2 = hailstones[j]
            p1, v1 = (p1[0], p1[1]), (v1[0], v1[1])
            p2, v2 = (p2[0], p2[1]), (v2[0], v2[1])
            # inter_range = (7, 27)
            inter_range = (200000000000000, 400000000000000)
            if check_intersection(p1, p2, v1, v2, inter_range, inter_range):
                res += 1
    print(res)
    possible = [{x for x in range(-1000, 1001)}, {x for x in range(-1000, 1001)}, {x for x in range(-1000, 1001)}]
    for i in range(len(hailstones)):
        for j in range(i):
            p1, v1 = hailstones[i]
            p2, v2 = hailstones[j]
            for xyz in range(3):
                if v1[xyz] == v2[xyz]:
                    dist_diff = p2[xyz] - p1[xyz]
                    for sample_v in range(-1000, 1001):
                        if sample_v == v1[xyz]:
                            continue
                        if dist_diff % (sample_v - v1[xyz]) != 0:
                            if sample_v in possible[xyz]:
                                possible[xyz].remove(sample_v)
    vx, vy, vz = possible[0].pop(), possible[1].pop(), possible[2].pop()

    x1, y1, z1 = hailstones[1][0]
    vx1, vy1, vz1 = hailstones[1][1]
    x2, y2, z2 = hailstones[5][0]
    vx2, vy2, vz2 = hailstones[5][1]

    a1 = (vy1 - vy) / (vx1 - vx)
    a2 = (vy2 - vy) / (vx2 - vx)
    b1 = y1 - (a1 * x1)
    b2 = y2 - (a2 * x2)
    xp = int((b2 - b1) / (a1 - a2))
    yp = int(a1 * xp + b1)
    t = (xp - x1) // (vx1 - vx)
    zp = z1 + (vz1 - vz) * t

    res2 = xp + yp + zp
    print(res2)


if __name__ == "__main__":
    part_one()
