
class monkey:
    def __init__(self,startingItems,operationType,operationNum,testNum,testSucces,testFailed):
        self.inspectedItems = 0
        self.startingItems = startingItems
        self.operationType = operationType
        self.operationNum = operationNum
        self.testNum = testNum
        self.testSucces = testSucces
        self.testFailed = testFailed
    def print(self):
        print(f"Inspected Items: {self.inspectedItems}")
        print(f"starting Items: {self.startingItems}")
        print(f"operation: old {self.operationType} {self.operationNum}")
        print(f"tes: divisible by  {self.testNum} succes {self.testSucces} failed {self.testFailed}")

    def operation(self,old):
        if self.operationType == "+":
            return old + self.operationNum
        if self.operationType == "*":
            return old * self.operationNum
        if self.operationType == "**":
            return old ** self.operationNum
    def test(self,i):
        return i % self.testNum == 0
    
    def distributeItems(self,monkeys,devisor):
        for i in self.startingItems:
         
            self.inspectedItems +=1
            i = self.operation(i) 
            if devisor:
                i = i%devisor
               
            else:
                i = i//3
            if self.test(i):
             
                monkeys[self.testSucces].startingItems.append(i)
            else:
              
                monkeys[self.testFailed].startingItems.append(i)
        self.startingItems = []
def getMonkeys(monkeys):
    with open("day11/data.txt") as file:
        for line in file:
            
            if line.startswith("Monkey"):
                monkeys.append(monkey([],"",0,0,0,0))
            if line.startswith("  Starting items"):
                items = line.split(":")[1].split(",")
                items = [int(i) for i in items]
                monkeys[-1].startingItems = items
            if line.startswith("  Operation"):
                op = line.split("old ")[1].split(" ")
                if op[1].startswith("old"):
                    monkeys[-1].operationType = "**"
                    monkeys[-1].operationNum = 2
                else:
                    monkeys[-1].operationType = op[0]
                    monkeys[-1].operationNum = int(op[1])
            if line.startswith("  Test:"):
                monkeys[-1].testNum = int(line.split("by")[1])
            if line.startswith("    If true:"):
                monkeys[-1].testSucces =  int(line.split("monkey")[1])
            if line.startswith("    If false:"):
                monkeys[-1].testFailed =  int(line.split("monkey")[1])
def task1():
        monkeys  = []
        getMonkeys(monkeys)
        for _ in range(20):
            for m in monkeys:
                m.distributeItems(monkeys,False)

        inspections = []
        for m in monkeys:
            inspections.append(m.inspectedItems)
        inspections.sort()
        print(inspections[-1]*inspections[-2])
def task2():
    monkeys  = []
    getMonkeys(monkeys)
    devisor =  1
    for m in monkeys:
        devisor*=m.testNum
    
    for _ in range(10000):
        for m in monkeys:
            m.distributeItems(monkeys,devisor)

    inspections = []
    for m in monkeys:
        inspections.append(m.inspectedItems)
  
    inspections.sort()
    print(inspections[-1]*inspections[-2])

def main():
    task1()
    task2()
if __name__ == "__main__":
    main()
        