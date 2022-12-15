class sensor:
    def __init__(self,pos,dist):
        self.pos = pos
        self.dist = dist
    
    def print(self):
        print(f"SENSOR IS AT {self.pos} with distance to beacon: {self.dist}")

def deleteInclusion(inList,outList):
    
    for checkingPos in inList:
        isRedudntand = False
    
        tempForRedundance = inList[:]
        tempForRedundance.remove(checkingPos)
        for otherPos in tempForRedundance:     
            if otherPos[0] <= checkingPos[0] and otherPos[1]>= checkingPos[1]:
                isRedudntand = True
                break
        if not isRedudntand:
            outList.append(checkingPos)
    

def getFormatedPossitions(formatedPos,impossiblePos):


    preStripingFOrmated=[]


    strippedPos = []
    
    deleteInclusion(impossiblePos,strippedPos)


    for idx in range(len(strippedPos)):
        temp = strippedPos[idx+1:]
       
        formPos = [strippedPos[idx][0],strippedPos[idx][1]]
      

        for otherPos in temp:        
            if otherPos[0] > formPos[0] and otherPos[0] < formPos[1] and otherPos[1]>formPos[1]:
         
                formPos[1] = otherPos[0]

            if otherPos[1] < formPos[1] and otherPos[1]>formPos[0] and otherPos[0]<formPos[0]:
       
                formPos[0] = otherPos[1]

   
        preStripingFOrmated.append(formPos)


    #deletes duplicates
    additionalyStripped = []
    for idx in range(len(preStripingFOrmated)):
        tempForRedundance = preStripingFOrmated[idx+1:]
        if preStripingFOrmated[idx] in tempForRedundance:
            continue
        additionalyStripped.append(preStripingFOrmated[idx])

    deleteInclusion(additionalyStripped,formatedPos)



    formatedPos.sort(key= lambda x: x[0])
    for i in range(len(formatedPos)-1):
        if formatedPos[i][1] == formatedPos[i+1][0]:
            formatedPos[i][1]-= 1

def getSensors(sensors,sneakyBecons = set(),row = 0):
    with open("day15/data.txt","r") as  file:
        for line in file:
            line = line.strip("\n")
            sensorPos = line.replace("Sensor at","").replace("x=","").replace("y=","").split(": closest beacon is at ")[0].split(',')
            beaconPos = line.replace("x=","").replace("y=","").split(": closest beacon is at ")[1].split(",")  
          
            sensorPos = [int(sensorPos[0]),int(sensorPos[1])] 
            beaconPos = [int(beaconPos[0]),int(beaconPos[1])] 

            if beaconPos[1] == row:
                sneakyBecons.add(beaconPos[0])
            distance = abs(sensorPos[0]-beaconPos[0]) + abs(sensorPos[1]-beaconPos[1])
            sensors.append(sensor(sensorPos,distance))


def task1():
    sensors = []
    sneakyBeacons = set()
    row = 2000000
    getSensors(sensors,sneakyBeacons,row)

    impossiblePos = []
    
    for s in sensors:
        maxDist =s.dist - abs(s.pos[1] - row)
        if maxDist < 0:
            continue
        impossiblePos.append([s.pos[0]-maxDist,s.pos[0]+maxDist])

    formatedPos = []
    getFormatedPossitions(formatedPos,impossiblePos)
    sum = 0
    for pos in formatedPos:
        sum += pos[1]-pos[0]+1
    for b in sneakyBeacons:
        for pos in formatedPos:
            if b >= pos[0] and b<=pos[1]:
                sum -=1
    print(sum)


def task2():
    sensors = []

    getSensors(sensors)

    found = False
    for row in range(4000000):
        impossiblePos = []
    
        for s in sensors:
            maxDist =s.dist - abs(s.pos[1] - row)
            if maxDist < 0:
                continue
            impossiblePos.append([s.pos[0]-maxDist,s.pos[0]+maxDist])

        formatedPos = []
        getFormatedPossitions(formatedPos,impossiblePos)
        if formatedPos[0][0]>0:
            #print(f"\nIn {row} row signal starts at {formatedPos[0][0]}")
            break
        if formatedPos[-1][1]<4000000:
            #print(f"\nIn {row} row signal ends at {formatedPos[-1][1]}")
            break

        for i in range(len(formatedPos)-1):
            if formatedPos[i][1] +1 != formatedPos[i+1][0]:
                print(formatedPos,i)
                #print(f"\nthere is a break at {row} row in possition {formatedPos[i][1]+1}")
                print((formatedPos[i][1]+1)*4000000+ row)
                found = True
                break
        if found:
            break
        print(f"\r {row} out of 4000000",end="")
        


  

  

if __name__ == "__main__":
    task1()
    task2()