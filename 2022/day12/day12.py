import time

class Node:
    def __init__(self,possition,end,height):
        self.height = height
        self.possition = possition
        self.cameFrom = None
        self.distanceFromStart = 100000000 #big num deffinietly to big for this task to cause problems
        self.minDistanceToEnd = distance(possition,end)
    def print(self):
        print(self.possition,self.cameFrom,self.distanceFromStart,self.minDistanceToEnd,self.height)

def getheight(char):
    return ord(char) - ord("a")
def isValidRoute(pos,w,h):
    if pos[0]<0:
        return False
    if pos[1]<0:
        return False
    if pos[0]>w-1:
        return False
    if pos[1]>h-1:
        return False
    return True

def printData(data):
    for row in data:
        for char in row:
            print(f"{char:3}",end="")
        print()
def distance(curr,end):
    return abs(curr[0]-end[0]) + abs(curr[1]-end[1])

def sortQueue(queue):
    queue.sort(key=lambda x: x.distanceFromStart + x.minDistanceToEnd)

def getQueueObjectByPos(qMap,pos):
    return qMap[pos[1]][pos[0]]
    

def wasVisited(beenTo,pos):
    return beenTo[pos[1]][pos[0]]

def loadData(data):
    with open("day12/data.txt","r") as file:
        for idxRow, line in enumerate(file):
            line = line.strip("\n")
            row = []
            for idxCol, char in enumerate(line):
                if char == "S":
                    start = (idxCol,idxRow)
                    row.append(getheight("a"))
                elif char == 'E':
                    end = (idxCol,idxRow)
                    row.append(getheight("z"))
                else:
                    row.append(getheight(char))
            data.append(row)
        return start,end
                
def findShortestRoute(data,start,end):
    
    width,height = len(data[0]),len(data)
    nodeMap = []
    activeNodes = []
    for idxY, row in enumerate(data):
        nodeRow = []
        for idxX, _ in enumerate(row):
            qObj = Node((idxX,idxY),end,data[idxY][idxX])
            nodeRow.append(qObj)
        nodeMap.append(nodeRow)
    startNode = getQueueObjectByPos(nodeMap,start)
    activeNodes.append(startNode)
    startNode.distanceFromStart = 0
    startNode.cameFrom == start
    sortQueue(activeNodes)
    beenTo = [[False for _ in range(width)]for _ in range(height)]
    while activeNodes[0].possition != end:
        currNode = activeNodes[0]
        possibleRutes = [(0,1),(0,-1),(1,0),(-1,0)]

        for rute in possibleRutes:
            #loop Over possible routes
 
            destination = (currNode.possition[0] + rute[0],currNode.possition[1] + rute[1])
            if isValidRoute(destination,width,height):
              
                if data[destination[1]][destination[0]] <= currNode.height + 1:
                  
                    if not wasVisited(beenTo,destination):
                      
                        #route is Valid
            
                        nodeToUpdate = getQueueObjectByPos(nodeMap,destination)
                        if not nodeToUpdate in activeNodes:
                            activeNodes.append(nodeToUpdate)

                        newDistance = currNode.distanceFromStart + 1
                        if newDistance < nodeToUpdate.distanceFromStart:
                            nodeToUpdate.distanceFromStart = newDistance
                            nodeToUpdate.cameFrom = currNode.possition
         
        #after all the routes have been checked delete the node
        readyElement = activeNodes.pop(0)
        beenTo[readyElement.possition[1]][readyElement.possition[0]] = True
        sortQueue(activeNodes)  

        if len(activeNodes)==0:
            break

    return getQueueObjectByPos(nodeMap,end).distanceFromStart

def task1():
    data = []
    start,end = loadData(data)
    print(findShortestRoute(data,start,end))

def task2():
    data = []
    possibleStartingPoints = []
    start,end = loadData(data)
    for idxY,row in enumerate(data):
        for idxX,e in enumerate(row):
            if e == 0:
                possibleStartingPoints.append((idxX,idxY,distance((idxX,idxY),end)))
    possibleStartingPoints.sort(key=lambda x: x[2])
    currLowest = 1000000
    checked = 0
    for startingPoint in possibleStartingPoints:
        checked +=1
        pathLen = findShortestRoute(data,(startingPoint[0],startingPoint[1]),end)
        if pathLen<currLowest:
            currLowest = pathLen
        print(f"\rcurrLowest: {currLowest} checked {checked} out of {len(possibleStartingPoints)}",end="")    
    print() 
    print(currLowest)

if __name__ == "__main__":
    task1()
    task2()