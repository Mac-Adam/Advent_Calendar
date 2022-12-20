class blueprint:
    def __init__(self,costs):
        self.costs = costs


def getBlueprints(blueprints):
    with open("day19/data.txt","r") as file:
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




def getBuildPossibilities(possibilities,resources,blue):
    for robot in blue.costs:



def evaluateBluePrint(blue,robots=[1,0,0,0],resources=[0,0,0,0],timeLeft = 24):
    newResources = []
    for idx in range(4):
        newResources.append(resources[idx] + robots[idx])
    possibleRobotsBuilds = [0,0,0,0]





def task1():
    blueprints = []
    getBlueprints(blueprints)




if __name__ == "__main__":
    task1()
