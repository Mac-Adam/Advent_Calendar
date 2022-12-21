import time

class monkey:
    def __init__(self,name,num,aMonkey,bMonkey,op):
        self.name = name
        self.num = num
        self.a = aMonkey
        self.b = bMonkey
        self.op = op

def getMonkeys(monkeys):
    with open("day21/data.txt","r") as file:
        for line in file:
            name = line[:4]
            if len(line)>=12: #complex monkey
                op = line[11]
                a =  line[6:10]
                b =  line[13:17]
                monkeys.append(monkey(name,None,a,b,op))
            else:
                num = int(line.split(':')[1]) 
                monkeys.append(monkey(name,num,None,None,None))

def getVal(monkey,monkeyDict):
    if monkey.num:
        return monkey.num
    if monkey.op == "+":
        return getVal(monkeyDict[monkey.a],monkeyDict) + getVal(monkeyDict[monkey.b],monkeyDict)
    if monkey.op == "-":
        return getVal(monkeyDict[monkey.a],monkeyDict) - getVal(monkeyDict[monkey.b],monkeyDict)

    if monkey.op == "*":
        return getVal(monkeyDict[monkey.a],monkeyDict) * getVal(monkeyDict[monkey.b],monkeyDict)

    if monkey.op == "/":
        return getVal(monkeyDict[monkey.a],monkeyDict) / getVal(monkeyDict[monkey.b],monkeyDict)




def task1():
    start = time.time()
    monkeys = []
    monkeyDict = dict()
    getMonkeys(monkeys)
    for m in monkeys:
        monkeyDict[m.name] = m
    end = time.time()
    print(getVal(monkeyDict['root'],monkeyDict))
    print(f"task 1 in {end-start}")

def  task2():
    start = time.time()
    monkeys = []
    monkeyDict = dict()
    getMonkeys(monkeys)
    for m in monkeys:
        monkeyDict[m.name] = m
    end = time.time()
    i = 1
    root = monkeyDict['root']
    while True:
        monkeyDict['humn'].num = i
        if getVal(monkeyDict[root.a],monkeyDict) == getVal(monkeyDict[root.b],monkeyDict):
            break
        i+=1
        print(f"\r{i}",end="")
    print(f"\ntask 2 in {end-start}")

if __name__ == "__main__":
    task1()
    task2()