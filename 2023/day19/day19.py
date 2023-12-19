from copy import deepcopy

file = 'in19'


def shorten_ranges(r):
    sorted_r = sorted(r)
    res = []
    curr = sorted_r[0]
    for ran in sorted_r:
        if ran[0] < curr[1]:
            curr = curr[0], max(curr[1], ran[1])
        else:
            res.append(curr)
            curr = ran
    res.append(curr)
    return res


def combine_ranges(r1, r2):
    res = {'x': [], 'm': [], 'a': [], 's': []}
    for key in 'xmas':
        res[key] = []
        for t in r1[key]:
            res[key].append(t)
        for t in r2[key]:
            res[key].append(t)
        res[key] = shorten_ranges(res[key])
    return res


def ranges_if_less(new_ranges, op, off=1):
    temp = []
    for r in new_ranges[op[1]]:
        if r[1] < op[3]:
            temp.append(r)
        elif r[0] < op[3] < r[1]:
            temp.append((r[0], op[3] - off))
    return temp


def ranges_if_more(new_ranges, op, off=1):
    temp = []
    for r in new_ranges[op[1]]:
        if r[0] > op[3]:
            temp.append(r)
        elif r[0] < op[3] < r[1]:
            temp.append((op[3] + off, r[1]))
    return temp


class Workflow:
    def __init__(self, workflow_str):
        workflow_str = workflow_str.replace('}', '')
        id_, rest = workflow_str.split('{')
        self.id = id_
        self.operations = []
        for operation in rest.split(","):
            if ':' not in operation:
                self.operations.append(operation)
            else:
                rest, next_id = operation.split(":")
                if rest[1] == '<':
                    t, val = rest.split('<')
                    val = int(val)
                    self.operations.append((next_id[:], t, rest[1], val))
                else:
                    t, val = rest.split('>')
                    val = int(val)
                    self.operations.append((next_id[:], t, rest[1], val))

    def update_ranges(self, ranges):
        new_ranges = deepcopy(ranges)
        res = []
        for op in self.operations:
            if isinstance(op, str):
                res.append((op, deepcopy(new_ranges)))
                return res
            if op[2] == '>':
                if_in = deepcopy(new_ranges)
                if_in[op[1]] = ranges_if_more(new_ranges, op)
                new_ranges[op[1]] = ranges_if_less(new_ranges, op, 0)
                res.append((op[0], deepcopy(if_in)))
            if op[2] == '<':
                if_in = deepcopy(new_ranges)
                if_in[op[1]] = ranges_if_less(new_ranges, op)
                new_ranges[op[1]] = ranges_if_more(new_ranges, op, 0)
                res.append((op[0], deepcopy(if_in)))

    def go_through(self, data):
        for op in self.operations:
            if isinstance(op, str):
                return op
            if op[2] == '>' and data[op[1]] > op[3]:
                return op[0]
            if op[2] == '<' and data[op[1]] < op[3]:
                return op[0]


def part_one():
    with open(file) as f:
        workflows = {}
        all_workflows = False
        res = 0
        for line in f:
            line = line.rstrip()
            if all_workflows:

                line = line[1:-1]
                xmas = {s[0]: int(s[2:]) for s in line.split(',')}
                wf_id = 'in'
                while wf_id not in 'AR':
                    wf_id = workflows[wf_id].go_through(xmas)
                if wf_id == 'A':
                    res += sum(xmas.values())
            else:
                if line == '':
                    all_workflows = True
                else:
                    wf = Workflow(line)
                    workflows[wf.id] = wf
        print(res)


def part_two():
    with open(file) as f:
        workflows = {}
        res = 0
        for line in f:
            line = line.rstrip()

            if line == '':
                break
            else:
                wf = Workflow(line)
                workflows[wf.id] = wf

        ranges = {'in': [{'x': [(1, 4000)], 'm': [(1, 4000)], 'a': [(1, 4000)], 's': [(1, 4000)]}]}
        to_visit = {'in'}
        while to_visit:
            curr_node = to_visit.pop()
            # print("Visiting: ", curr_node)
            for parent_range in ranges[curr_node]:
                next_ranges = workflows[curr_node].update_ranges(parent_range)
                # print("next ranges")
                # for x in next_ranges:
                #     print(x)

                for idx, rs in next_ranges:
                    if idx not in "AR":
                        to_visit.add(idx)
                    if idx in ranges:
                        ranges[idx].append(rs)
                    else:
                        ranges[idx] = [rs]
                # print("curr ranges")
                # for x in ranges.items():
                #     print(x)

        # print(workflows['in'].update_ranges({'x': [(0, 4000)], 'm': [(0, 4000)], 'a': [(0, 4000)], 's': [(0, 4000)]}))
        res = 0
        a_ranges = ranges["A"]
        for r in a_ranges:
            t = 1
            for x in r.values():
                t *= x[0][1] - x[0][0] + 1
            res += t
        # print(ranges["A"])
        print(res)


if __name__ == "__main__":
    part_one()
    part_two()
    # print(shorten_ranges([(0, 4), (2, 3), (8, 10), (6, 9)]))
