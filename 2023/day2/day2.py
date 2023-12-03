def part_one():
    res = 0
    with open('./in2') as f:
        for line in f:
            data = line.split(':')[1]
            idx = int(line.split(':')[0].split(" ")[1])
            runds = data.split(";")
            flag = True
            for rund in runds:
                for col_num in rund.split(','):
                    temp = col_num.split(" ")
                    n = int(temp[1])
                    col = temp[2]
                    if col == "red" and n > 12 or col == "green" and n > 13 or col == "blue" and n > 14:
                        flag = False
            if flag:
                res += idx
    print(res)


def part_two():
    res = 0
    with open('./in2') as f:
        for line in f:
            line = line.replace("\n", "")
            data = line.split(':')[1]
            idx = int(line.split(':')[0].split(" ")[1])
            runds = data.split(";")
            r = 0
            g = 0
            b = 0
            for rund in runds:
                for col_num in rund.split(','):
                    temp = col_num.split(" ")
                    n = int(temp[1])
                    col = temp[2]
                    if col == "red":
                        r = max(r, n)
                    elif col == "green":
                        g = max(g, n)
                    else:
                        b = max(b, n)

            res += r * g * b
    print(res)


if __name__ == "__main__":
    part_one()
    part_two()
