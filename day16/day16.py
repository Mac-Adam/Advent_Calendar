
currMax = 0

class Tunel:

    def __init__(self,name,tunels,rate):
        self.tunelNames = tunels
        self.name = name
        self.rate = rate

    def link(self,tunels):
        self.tunels = []
        for t in tunels:
            
            if t.name in self.tunelNames:
                self.tunels.append(t)
        self.tunels.sort(key = lambda x: -x.rate)

    def __str__(self):
        return f"Valve {self.name} with rate {self.rate} leads to {self.tunelNames}"


class Route:
    def __init__(self,lenght,leadsTo):
        self.lenght = lenght
        self.leadsTo = leadsTo

    def __str__(self):
        return f"Route to {self.leadsTo.name} is {self.lenght} minutes long"

        

class Valve: #basicly a tunel but it It surely contains a valid Valve + links to all other valves
    
    def __init__(self,name,rate,tunel):
        self.name = name
        self.rate = rate
        self.tunel = tunel

        self.routes = []


def getRouteValue(route):
    sum = 0
    alreadyOpened = set()
    for idx,t in enumerate(route):
        if type(t) != str:
            if not route[idx-1] in alreadyOpened:
                sum += (29-idx)*t[1]
                
                alreadyOpened.add(route[idx-1])
    return sum
def getRoute(tunel,route=[],opened = [],beenTo = [],minutesLeft = 30):
    if minutesLeft == 0:   
        global currMax
        routeVal = getRouteValue(route)
        if routeVal> currMax:
            currMax = routeVal
            print(f"New max: {currMax}")
            print(route)
        return
    if tunel.rate !=0:
        if type (route[-1] ) == str and not route[-1] in opened:
            getRoute(tunel,route+[("open",tunel.rate)],opened+[route[-1]],beenTo,minutesLeft-1)
    
    for t in tunel.tunels:
        if not t.name in beenTo:

            getRoute(t,route+[t.name],opened,beenTo+[tunel.name],minutesLeft-1)
    for t in tunel.tunels:
        if t.name in beenTo:
            getRoute(t,route+[t.name],opened,beenTo+[tunel.name],minutesLeft-1)

def sortQueue(queue):
    queue.sort(key=lambda x: x[1])



def wasVisited(beenTo,tunel):
    for t in beenTo:
        if t == tunel:
            return True
    return False


def isInQ(q,tunel):
    for qObj in q:
        if qObj[0] == tunel:
            return True
    return False


def getQidxByName(q,name):
    for i , t in enumerate(q):
        if t[0].name == name:
            return i
    return False 



def calcPath(start,path):
    sum = 0


def maximmizePressure(start,path=[],pressure = 0,minutesLeft = 30):
    # test = [
    #     [],
    #     ['DD'],
    #     ['DD','BB'],
    #     ['DD','BB','JJ'],
    #     ['DD','BB','JJ','HH'],
    #     ['DD','BB','JJ','HH','EE'],
    #     ['DD','BB','JJ','HH','EE','CC'],
    # ]

    hasOptions = False

    for route in start.routes:
        if route.leadsTo.name in path:
            continue
        minutesLeftAfterOpening = minutesLeft-1-route.lenght
        if minutesLeftAfterOpening<0:
            continue
        hasOptions = True
        # if path + [route.leadsTo.name] in test:
        #     print("-"*40)
        #     print(f"currently at: {start.name}")
        #     print(route)
        #     print(f"Time Left: {minutesLeft} time after openning: {minutesLeftAfterOpening} Opening {route.leadsTo.name} ")

        maximmizePressure(
            route.leadsTo,
            path+[route.leadsTo.name],
            pressure + route.leadsTo.rate*(minutesLeftAfterOpening),
            minutesLeftAfterOpening
            )
    if not hasOptions:
        global currMax
        if pressure >= currMax:
            print(pressure)
            print(path)
            currMax = pressure


def shortestLen(start,endName):

    queue = []
    queue.append([start,0])
    sortQueue(queue)

    beenTo = []
    while queue[0][0].name != endName:
        currNode = queue[0]
 
        for tunel in currNode[0].tunels:
            #loop Over possible route
    
            if not wasVisited(beenTo,tunel):
                
                #route is Valid

                if not isInQ(queue,tunel):
                    queue.append([tunel,1000000])

                nodeIdxToUpdate = getQidxByName(queue,tunel.name)
             
                newDistance = currNode[1] + 1
                if newDistance < queue[nodeIdxToUpdate][1]:
                    queue[nodeIdxToUpdate][1] = newDistance
            
    
        #after all the routes have been checked delete the node
        readyElement = queue.pop(0)
        beenTo.append(readyElement[0])
        sortQueue(queue)  

        if len(queue)==0:
            break
    return queue[0][1]




def getTunels(data):
    with open("day16/data.txt","r") as file:
        for line in file:
            line = line.strip("\n")
            tunels = line.split("; tunnels lead to valves ")[-1].replace(" ","").split(",")
            if len(tunels[0]) >10: #dirty way to handle single tunel
                tunels = [line.split("tunnel leads to valve")[-1].replace(" ","")] 
            valeIdx = line[6:8]
            rate = int(line.split(";")[0].split("=")[1])
            data.append(Tunel(valeIdx,tunels,rate))

def task1():
    tunels = []
    getTunels(tunels)
    for t in tunels:
        t.link(tunels)
        print(t)


    valves = []
    for t in tunels:
        if t.rate != 0:
            valves.append(Valve(t.name,t.rate,t))

    for v in valves:
        routes = []
        for otherV in valves:
            if otherV != v:
                dist = shortestLen(v.tunel,otherV.name)
                routes.append(Route(dist,otherV))
        v.routes = routes



    for potenitialStartTunel in tunels:
        if potenitialStartTunel.name == "AA":  
            startValve = Valve("AA",0,potenitialStartTunel)
            routes = []
            for v in valves:
                dist = shortestLen(potenitialStartTunel,v.name)
                routes.append(Route(dist,v))
            startValve.routes = routes

    maximmizePressure(startValve )



    
    

    



if __name__ == "__main__":
    task1()
    
