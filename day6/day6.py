
def allDiferent(q, messLen):
    if len(q) == messLen:
        dif = True
        for i in range(messLen):
            temp = q[:]
            el = temp[i]
            temp.pop(i)
            if el in temp:
                dif = False
        return dif
    return False

with open("day6/data.txt") as file:
    queue = []
    idx = 0
    for char in file.readline():
        idx+=1
        queue.append(char)
        if len(queue)>14:
            queue.pop(0)
        if allDiferent(queue,14):
            break
    print(idx)
        