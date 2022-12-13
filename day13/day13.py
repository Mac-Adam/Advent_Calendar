import functools
def compare(f,s):
    if  type(f) == int:
        first = f
    else:
        first = f[:]
    if  type(s) == int:
        second = s
    else:
        second = s[:]
    if type(first) == int and type (second) == int:
        if first > second:
            return -1
        if first < second:
            return 1
        return 0
    if type(first) == int:
        first = [first]
    if type(second) == int:
        second = [second]
    while True:
        if first == [] and second != []:
            return 1
        if second == [] and first != []:
            return -1
        if first == [] and second == []:
            return 0
        e1 = first.pop(0)
        e2 = second.pop(0)
        res = compare(e1,e2)
        if res == 0:
            continue
        return res

        
     

def getData(data):
    with open("day13/data.txt") as file:
        for line in file:
            if line == "\n":
                continue
            line = line.strip("\n")
            line = line.replace("10","a")
            lineData = []
            arrayStack = [lineData]
            currArr = lineData
            for c in line:
               
                if c == "[":
                    currArr.append([])
                    currArr = currArr[-1]
                    arrayStack.append(currArr)
                elif c == "]":
                    arrayStack.pop()
                    currArr = arrayStack[-1]
                elif c != ",":
                    if c == "a":
                        currArr.append(10)
                    else:
                        currArr.append(int(c))
            data.append(lineData[0])

def task1():
    data =[]
    getData(data)
    sum = 0
    for rowIdx in range(0,len(data),2):
        if(compare(data[rowIdx],data[rowIdx + 1]) == 1):
            sum +=rowIdx/2 + 1
    print(sum)
def task2():
    data =[]
    getData(data)
    data.append([[6]])
    data.append([[2]])
    data = sorted(data, key=functools.cmp_to_key(compare))
    data = reversed(data)
    start = 0
    for i,d in enumerate(data):
        if d == [[2]]:
            start = i+1
        if d == [[6]]:
            print(start*(i+1))
if __name__ == "__main__":
    task1()
    task2()