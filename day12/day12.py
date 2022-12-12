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

def getQueueObjectByPos(queue,pos):
    for node in queue:
        if node.possition == pos:
            return node
    

def wasVisited(beenTo,pos):
    for node in beenTo:
        if node.possition == pos:
            return True
    return False

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
    queue = []
    for idxY, row in enumerate(data):
        for idxX, _ in enumerate(row):
            queue.append(Node((idxX,idxY),end,data[idxY][idxX]))

    for e in queue:
        if e.possition == start:
            e.distanceFromStart = 0
            e.cameFrom == start
    sortQueue(queue)
    beenTo = []
    while queue[0].possition != end:
        currNode = queue[0]
        possibleRutes = [(0,1),(0,-1),(1,0),(-1,0)]

        for rute in possibleRutes:
            #loop Over possible routes
            destination = (currNode.possition[0] + rute[0],currNode.possition[1] + rute[1])
            if isValidRoute(destination,width,height):
                if data[destination[1]][destination[0]] <= currNode.height + 1:
                    if not wasVisited(beenTo,destination):
                        #route is Valid
                        nodeToUpdate = getQueueObjectByPos(queue,destination)
                        newDistance = currNode.distanceFromStart + 1
                        if newDistance < nodeToUpdate.distanceFromStart:
                            nodeToUpdate.distanceFromStart = newDistance
                            nodeToUpdate.cameFrom = currNode.possition

        #after all the routes have been checked delete the node
        beenTo.append(queue.pop(0))   
        sortQueue(queue)  
    
    return getQueueObjectByPos(queue,end).distanceFromStart

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