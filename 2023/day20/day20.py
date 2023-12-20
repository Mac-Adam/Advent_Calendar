import math

file = 'in20'


def part_one():
    with open(file) as f:
        modules = {}
        states = {}
        for l in f:
            l = l.rstrip()
            l = l.replace(' ', '')
            module, to_pass = l.split('->')
            if module == 'broadcaster':

                modules[module] = ('-', to_pass.split(','))
            else:

                t, name = module[0], module[1:]
                if t == "%":
                    states[name] = 'low'

                modules[name] = (t, to_pass.split(','))

        for name, data in modules.items():
            for conn in data[1]:
                if conn not in modules:
                    continue
                if modules[conn][0] == "&":
                    if conn in states:

                        states[conn][name] = 'low'
                    else:
                        states[conn] = {name: 'low'}

        low = 0
        high = 0

        for _ in range(1000):
            signal_q = [('broadcaster', ('button', 'low'))]
            low += 1
            while signal_q:
                next_node, signal = signal_q.pop()
                if next_node not in modules:
                    continue
                signal_sender, signal_val = signal
                if modules[next_node][0] == '-':
                    for node in modules[next_node][1]:
                        if signal_val == 'low':
                            low += 1
                        else:
                            high += 1
                        signal_q.append((node, (next_node, signal_val)))
                elif modules[next_node][0] == '%':
                    if signal_val == 'low':
                        states[next_node] = 'low' if states[next_node] == 'high' else 'high'
                        for node in modules[next_node][1]:
                            if states[next_node] == 'low':
                                low += 1
                            else:
                                high += 1
                            signal_q.append((node, (next_node, states[next_node])))
                else:
                    states[next_node][signal_sender] = signal_val
                    to_send = 'low'
                    for v in states[next_node].values():
                        if v == 'low':
                            to_send = "high"
                            break
                    for node in modules[next_node][1]:
                        if to_send == 'low':
                            low += 1
                        else:
                            high += 1
                        signal_q.append((node, (next_node, to_send)))
        print(low * high)


### BADLY WRIITEN AND DOESN't eaven work properly idk why. Maybe will fix it in the future (probably not xD)
def part_two():
    watch_list = {'jq': [], 'cc': [], 'sp': [], 'nx': []}
    with open(file) as f:
        modules = {}
        states = {}
        for l in f:
            l = l.rstrip()
            l = l.replace(' ', '')
            module, to_pass = l.split('->')
            if module == 'broadcaster':

                modules[module] = ('-', to_pass.split(','))
            else:

                t, name = module[0], module[1:]
                if t == "%":
                    states[name] = 'low'

                modules[name] = (t, to_pass.split(','))

        for name, data in modules.items():
            for conn in data[1]:
                if conn not in modules:
                    continue
                if modules[conn][0] == "&":
                    if conn in states:

                        states[conn][name] = 'low'
                    else:
                        states[conn] = {name: 'low'}

        for i in range(1000000):
            signal_q = [('broadcaster', ('button', 'low'))]
            while signal_q:

                next_node, signal = signal_q.pop()
                signal_sender, signal_val = signal
                if next_node in watch_list and signal_val == 'low':
                    if len(watch_list[next_node]) == 0 or i != watch_list[next_node][-1]:
                        watch_list[next_node].append(i)
                    p = True
                    for l in watch_list.values():
                        if len(l) < 4:
                            p = False
                    if p:
                        to_lcm = []
                        for id, l in watch_list.items():
                            print(id, l)
                            to_lcm.append(l[-1] - l[-2])
                        print(math.lcm(*to_lcm))
                        return

                if next_node not in modules:
                    continue

                if modules[next_node][0] == '-':
                    for node in modules[next_node][1]:
                        signal_q.append((node, (next_node, signal_val)))
                elif modules[next_node][0] == '%':
                    if signal_val == 'low':
                        states[next_node] = 'low' if states[next_node] == 'high' else 'high'
                        for node in modules[next_node][1]:
                            signal_q.append((node, (next_node, states[next_node])))
                else:
                    states[next_node][signal_sender] = signal_val
                    to_send = 'low'
                    for v in states[next_node].values():
                        if v == 'low':
                            to_send = "high"
                            break
                    for node in modules[next_node][1]:
                        signal_q.append((node, (next_node, to_send)))


if __name__ == '__main__':
    part_one()
    part_two()
