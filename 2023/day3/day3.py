file = './in3'


def part_one():
    with open(file) as f:
        res = 0
        around = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]
        char_mat = []
        for line in f:
            char_mat.append(line.replace("\n", ""))

        h = len(char_mat)
        w = len(char_mat[0])
        mask = [[False for _ in range(w)] for _ in range(h)]
        nums = [str(i) for i in range(10)]
        for row in range(h):
            for col in range(w):

                for idx in around:
                    newr, newc = row + idx[0], col + idx[1]
                    if newr < 0 or newc < 0 or newr >= h or newc >= w:
                        continue
                    if char_mat[newr][newc] not in [*nums, '.']:
                        mask[row][col] = True
        for row in range(h):
            curr_num = ''
            flag = False
            for col in range(w):
                if char_mat[row][col] in nums:
                    curr_num += char_mat[row][col]
                    flag = flag or mask[row][col]
                else:
                    if curr_num != '':
                        if flag:
                            res += int(curr_num)
                        curr_num = ''
                        flag = False
            if flag and curr_num != '':
                res += int(curr_num)

        print(res)


def part_two():
    with open(file) as f:
        res = 0
        around = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]
        char_mat = []
        for line in f:
            char_mat.append(line.replace("\n", ""))

        h = len(char_mat)
        w = len(char_mat[0])
        mask = [[(-1, -1) for _ in range(w)] for _ in range(h)]
        nums = [str(i) for i in range(10)]
        for row in range(h):
            for col in range(w):
                for idx in around:
                    newr, newc = row + idx[0], col + idx[1]
                    if newr < 0 or newc < 0 or newr >= h or newc >= w:
                        continue
                    if char_mat[newr][newc] == '*':
                        mask[row][col] = (newr, newc)
        gears = {}
        for row in range(h):
            curr_num = ''
            flag = (-1, -1)
            for col in range(w):
                if char_mat[row][col] in nums:
                    curr_num += char_mat[row][col]
                    if mask[row][col] != (-1, -1):
                        flag = mask[row][col]

                else:
                    if curr_num != '':
                        if flag != (-1, -1):
                            if flag in gears:
                                gears[flag].append(int(curr_num))
                            else:
                                gears[flag] = [int(curr_num)]
                        curr_num = ''
                        flag = (-1, -1)
            if flag != (-1, -1) and curr_num != '':
                if flag in gears:
                    gears[flag].append(int(curr_num))
                else:
                    gears[flag] = [int(curr_num)]

        for _, vals in gears.items():
            if len(vals) == 2:
                res += vals[0] * vals[1]
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
