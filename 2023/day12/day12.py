file = "in12"


def solve_line(seen, data, rows, i, curr_row, curr_len):
    key = (i, curr_row, curr_len)
    if key in seen:
        return seen[key]
    if i >= len(data):
        if curr_row >= len(rows) and curr_len == 0:
            return 1
        if curr_row == len(rows) - 1 and curr_len == rows[curr_row]:
            return 1
        return 0
    ans = 0
    for possible_char in ["#", "."]:
        if data[i] == possible_char or data[i] == "?":
            if possible_char == "." and curr_len == 0:
                ans += solve_line(seen, data, rows, i + 1, curr_row, curr_len)
            elif possible_char == "." and curr_row < len(rows) and curr_len == rows[curr_row]:
                ans += solve_line(seen, data, rows, i + 1, curr_row + 1, 0)
            elif possible_char == "#":
                ans += solve_line(seen, data, rows, i + 1, curr_row, curr_len + 1)
    seen[key] = ans
    return ans


def solution():
    with open(file) as f:
        res1 = 0
        res2 = 0
        for line in f:
            line = line.rstrip().split(" ")
            data1 = list(line[0])
            data2 = "?".join(5 * [line[0]])
            rows = line[1].split(",")
            rows1 = list(map(int, rows))
            rows2 = rows1 * 5
            seen = {}
            res1 += solve_line(seen, data1, rows1, 0, 0, 0)
            seen = {}
            res2 += solve_line(seen, data2, rows2, 0, 0, 0)
        print(res1, res2)


if __name__ == "__main__":
    solution()
