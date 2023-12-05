file = 'in5.txt'


def part_one():
    with open(file) as f:
        lines = f.readlines()
        seeds = lines.pop(0).split(":")[1].split()
        seeds = [int(x) for x in seeds]
        lines = [line for line in lines if line != '\n']
        lines.pop(0)
        temp = []
        for line in lines:
            if not any(char.isdigit() for char in line):
                for s in seeds:
                    temp.append(s)
                seeds = temp
                temp = []
                continue
            t = line.split()
            start_dest = int(t[0])
            start_org = int(t[1])
            width = int(t[2])
            to_del = []
            for s in seeds:
                if start_org <= s < start_org + width:
                    temp.append(start_dest + s - start_org)
                    to_del.append(s)
            for d in to_del:
                seeds.remove(d)
        for s in seeds:
            temp.append(s)
        print(min(temp))


def part_two():
    with open(file) as f:
        lines = f.readlines()
        seeds = lines.pop(0).split(":")[1].split()
        ranges = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1) for i in range(0, len(seeds), 2)]
        lines = [line for line in lines if line != '\n']
        lines.pop(0)
        temp = []
        for line in lines:
            if not any(char.isdigit() for char in line):
                for r in ranges:
                    temp.append(r)
                ranges = temp
                temp = []
                # print(len(ranges))
                # print("new Ranges: ", ranges)
                continue
            t = line.split()
            start_dest = int(t[0])
            start_org = int(t[1])
            width = int(t[2])
            to_del = []
            to_update = []
            for r in ranges:
                # print("looking into <{},{}>".format(r[0], r[1]),
                #       "the conv is <{},{}> -> <{},{}>".format(start_org, start_org + width - 1, start_dest,
                #                                               start_dest + width - 1))
                if start_org <= r[0] and r[1] < start_org + width:
                    temp.append((start_dest + r[0] - start_org, start_dest + r[1] - start_org))
                    # print("1split into: <{},{}>".format(start_dest + r[0] - start_org, start_dest + r[1] - start_org))
                    to_del.append(r)
                elif r[0] < start_org <= r[1] < start_org + width:
                    temp.append((start_dest, start_dest + r[1] - start_org))
                    to_update.append((r[0], start_org - 1))
                    # print("2split into: <{},{}> and <{},{}>".format(start_dest, start_dest + r[1] - start_org, r[0],
                    #                                                 start_org - 1))
                    to_del.append(r)
                elif start_org <= r[0] < start_org + width <= r[1]:
                    temp.append((start_dest + r[0] - start_org, start_dest + width - 1))
                    to_update.append((start_org + width, r[1]))
                    # print(
                    #     "3split into: <{},{}> and <{},{}>".format(start_dest + r[0] - start_org, start_dest + width - 1,
                    #                                               start_org + width, r[1]))

                    to_del.append(r)
                elif r[0] < start_org and start_org + width <= r[1]:
                    temp.append((start_dest, start_dest + width - 1))
                    to_update.append((r[0], start_org - 1))
                    to_update.append((start_org + width, r[1]))
                    # print("4split into: <{},{}>, <{},{}> and <{},{}>".format(start_org, start_org + width - 1, r[0],
                    #                                                          start_org - 1, start_org + width, r[1]))
                    to_del.append(r)

            for d in to_del:
                ranges.remove(d)
            for u in to_update:
                ranges.append(u)
        for r in ranges:
            temp.append(r)
        print(min(temp, key=lambda x: x[0])[0])


if __name__ == "__main__":
    part_one()
    part_two()
