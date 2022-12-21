import time


class blueprint:
    def __init__(self,costs):
        self.costs = costs
        max = []
        for x in range(len(costs[0])):
            high = 0
            for i in range(len(costs)):
                if costs[i][x]>high:
                    high = costs[i][x]
            max.append(high)
        max.append(1000000)
        self.max = max


def getBlueprints(blueprints):
    with open("day19/data.txt","r") as file:
        for line in file:
            line = line.strip("\n")
            robotCostsLines = line.split(".")
            robotCosts = []
            robotCosts.append((int(robotCostsLines[0].split("Each ore robot costs")[-1].strip("ore")),0,0))
            robotCosts.append((int(robotCostsLines[1].split("Each clay robot costs")[-1].strip("ore")),0,0))
            robotCosts.append((int(robotCostsLines[2].split("Each obsidian robot costs")[-1].split("ore and")[0]),int(robotCostsLines[2].split("Each obsidian robot costs")[-1].split("ore and")[1].strip("clay")),0))
            robotCosts.append((int(robotCostsLines[3].split("Each geode robot costs")[-1].split("ore and")[0]),0,int(robotCostsLines[3].split("Each geode robot costs")[-1].split("ore and")[1].strip("obsidian"))))
            blueprints.append(blueprint(robotCosts))
def canBuild(resources,cost):
    can = True
    for i,c in enumerate(cost):
        if c>resources[i]:
            can = False
    return can


def canBuildInMin(resources,robots,cost):
    for i,c in enumerate(cost):
        if c > 0 and robots[i]==0:
            return -1
    tempResources = resources[:]
    minutes = 0
    while not canBuild(tempResources,cost):
        addResources(tempResources,robots)
        minutes+=1
    return minutes

def build(resources,cost):
    for i,c in enumerate(cost):
        resources[i]-=c

def addResources(resources,robots,min = 1):
    for i,r in enumerate(robots):
        resources[i]+=r*min


def evaluateBluePrint(blue,robots=[1,0,0,0],resources=[0,0,0,0],timeLeft = 24):
    
    canBuild = False
    possibilities = []
   
    for id,robot in enumerate(blue.costs):
        if robots[id] >= blue.max[id]:
            continue 
        minutes = canBuildInMin(resources,robots,robot)
        if minutes<0:
            continue
        if timeLeft-minutes-1 <=0:
            continue
       
       
        canBuild = True
        newResources = resources[:]
       
        addResources(newResources,robots,minutes+1)
   
        build(newResources,robot)
         
        newRobots = robots[:]
        newRobots[id] +=1
       

        possibilities.append(evaluateBluePrint(blue,newRobots,newResources,timeLeft-minutes-1))
    if canBuild:
        return max(possibilities)

    res = resources[3]+robots[3]*timeLeft

    return res

   


def task1():
    start = time.time()
    blueprints = []
    getBlueprints(blueprints)
    sum = 0
    for id,blue in enumerate(blueprints):

        sum+= (id+1)*evaluateBluePrint(blue)
        now = time.time()
        print(f"evaluated {id} time elapsed: {now-start}")
    print(sum)


if __name__ == "__main__":
    task1()
