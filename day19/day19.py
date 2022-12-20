currMax = 0

class blueprint:
    def __init__(self,costs):
        self.costs = costs


def getBlueprints(blueprints):
    with open("day19/test.txt","r") as file:
        for line in file:
            line = line.strip("\n")
            robotCostsLines = line.split(".")
            robotCosts = []
            robotCosts.append((int(robotCostsLines[0].split("Each ore robot costs")[-1].strip("ore")),0,0))
            robotCosts.append((int(robotCostsLines[1].split("Each clay robot costs")[-1].strip("ore")),0,0))
            robotCosts.append((int(robotCostsLines[2].split("Each obsidian robot costs")[-1].split("ore and")[0]),int(robotCostsLines[2].split("Each obsidian robot costs")[-1].split("ore and")[1].strip("clay")),0))
            robotCosts.append((0,int(robotCostsLines[3].split("Each geode robot costs")[-1].split("ore and")[0]),int(robotCostsLines[3].split("Each geode robot costs")[-1].split("ore and")[1].strip("obsidian"))))
            blueprints.append(blueprint(robotCosts))

def canBuild(resources,cost):
    can = True
    for i,c in enumerate(cost):
        if c>resources[i]:
            can = False
    return can

def build(resources,cost):
    for i,c in enumerate(cost):
        resources[i]-=c


def buildMany(resources,blue,whatTobuild):
    for robotId,amunt in enumerate(whatTobuild):
        for resourceId,c in enumerate(blue.costs[robotId]):
            resources[resourceId]-=c*amunt

def getBuildPossibilities(possibilities,resources,blue,workingOn=(0,0,0,0)):
    addedSomething = False
    for id,robot in enumerate(blue.costs):
        if canBuild(resources,robot):
            newResources = resources[:]
            build(newResources,robot)
            newWorkingOn= list(workingOn[:])
            newWorkingOn[id]+=1
            newWorkingOn = tuple(newWorkingOn)
            possibilities.add(newWorkingOn)
            getBuildPossibilities(possibilities,newResources,blue,newWorkingOn)
    possibilities.add(workingOn)
    if not addedSomething:
        return

def subArr(a,b):
    res =[]
    for i in range(len(a)):
        res.append(a[i]-b[i])
    return res

def allNegative(arr):
    res = True
    for a in arr:
        if a>0:
            res = False
    return res

def evaluateBluePrint(blue,robots=[1,0,0,0],resources=[0,0,0,0],timeLeft = 24):
  dif = subArr(blue.costs[3],robots)
  for id,amount in enumerate(reversed(dif)):
    if amount >=0:
        dif = subArr(dif,blue.costs[2-id])
        dif[2-id] = 0
  print(dif)
 



def task1():
    blueprints = []
    getBlueprints(blueprints)
    print(evaluateBluePrint(blueprints[0]))


if __name__ == "__main__":
    task1()
