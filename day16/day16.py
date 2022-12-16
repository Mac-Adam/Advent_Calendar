
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

def getRouteValue(route):
    sum = 0
    alreadyOpened = set()
    for idx,t in enumerate(route):
        if type(t) != str:
            if not route[idx-1] in alreadyOpened:
                sum += (29-idx)*t[1]
                
                alreadyOpened.add(route[idx-1])
    return sum



def getRoute(tunel,route=[],opened =[],minutesLeft = 30):
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
            getRoute(tunel,route+[("open",tunel.rate)],opened+[route[-1]],minutesLeft-1)
    
    for t in tunel.tunels:
        getRoute(t,route+[t.name],opened,minutesLeft-1)
   




def getTunels(data):
    with open("day16/test.txt","r") as file:
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
    
    for t in tunels:
        if t.name == "AA":
            getRoute(t)
    

if __name__ == "__main__":
    task1()
    
