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

def hasHuman(monkey,monkeyDict):
    if monkey.name == 'humn':
        return True
    if monkey.num:
        return False
    return hasHuman(monkeyDict[monkey.a],monkeyDict) or hasHuman(monkeyDict[monkey.b],monkeyDict)

def colapse(monkey,monkeyDict):
    if monkey.num:
        return
    if not hasHuman(monkey,monkeyDict):
        monkey.num = getVal(monkey,monkeyDict)
    colapse(monkeyDict[monkey.a],monkeyDict)
    colapse(monkeyDict[monkey.b],monkeyDict)



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

def fitNum(monkey,value,monkeyDict):
    if monkey.name == 'humn':
        return value
    if hasHuman(monkeyDict[monkey.a],monkeyDict):
        if monkey.op == '+':
            return fitNum(monkeyDict[monkey.a],value-monkeyDict[monkey.b].num,monkeyDict)
        if monkey.op == '-':
            return fitNum(monkeyDict[monkey.a],value+monkeyDict[monkey.b].num,monkeyDict)
        if monkey.op == '*':
            return fitNum(monkeyDict[monkey.a],value/monkeyDict[monkey.b].num,monkeyDict)
        if monkey.op == '/':
            return fitNum(monkeyDict[monkey.a],value*monkeyDict[monkey.b].num,monkeyDict)
    if hasHuman(monkeyDict[monkey.b],monkeyDict):
        if monkey.op == '+':
            return fitNum(monkeyDict[monkey.b],value-monkeyDict[monkey.a].num,monkeyDict)
        if monkey.op == '-':
            return fitNum(monkeyDict[monkey.b],monkeyDict[monkey.a].num-value,monkeyDict)
        if monkey.op == '*':
            return fitNum(monkeyDict[monkey.b],value/monkeyDict[monkey.a].num,monkeyDict)
        if monkey.op == '/':
            return fitNum(monkeyDict[monkey.b],monkeyDict[monkey.a].num/value,monkeyDict)



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
    
    colapse(monkeyDict[root.a],monkeyDict)
    colapse(monkeyDict[root.b],monkeyDict)
    if hasHuman(monkeyDict[root.a],monkeyDict):
        print(f"\ntask 2 in {end-start}")
        print(fitNum(monkeyDict[root.a],monkeyDict[root.b].num,monkeyDict))
    if hasHuman(monkeyDict[root.b],monkeyDict):
        print(f"\ntask 2 in {end-start}")
        print(fitNum(monkeyDict[root.b],monkeyDict[root.a].num,monkeyDict))

    

if __name__ == "__main__":
    task1()
    task2()