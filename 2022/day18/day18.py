
def openSides(droplet,x,y,z,maxX,maxY,maxZ):

    possibilieties = [
        (0,0,1),
        (0,0,-1),
        (0,1,0),
        (0,-1,0),
        (1,0,0),
        (-1,0,0),
    ]
    res = 0
    for posibility in possibilieties:
        newCords = (x+posibility[0],y+posibility[1],z+posibility[2])
        if newCords[0]<0 or newCords[1]<0 or newCords[2]<0 or newCords[0]>=maxX or newCords[1]>=maxY or newCords[2]>=maxZ:
            res +=1
        elif droplet[newCords[1]][newCords[0]][newCords[2]] == 0:
            res +=1

    return res

        
def isInside(droplet,x,y,z,maxX,maxY,maxZ):
    possibilieties = [
        (0,0,1),
        (0,0,-1),
        (0,1,0),
        (0,-1,0),
        (1,0,0),
        (-1,0,0),
    ]
    queue = set([(x,y,z)])
    beenTo = []
    while len(queue)>0:
        currNode = queue.pop()   
        for posibility in possibilieties:
            newCords = (currNode[0]+posibility[0],currNode[1]+posibility[1],currNode[2]+posibility[2])
            if newCords[0]<0 or newCords[1]<0 or newCords[2]<0 or newCords[0]>=maxX or newCords[1]>=maxY or newCords[2]>=maxZ:
                return 0
            elif droplet[newCords[1]][newCords[0]][newCords[2]] == 0:
                if not (newCords[0],newCords[1],newCords[2]) in beenTo:
                    queue.add(newCords)
        beenTo.append(currNode)
    return 1  
   



def task1():
    with open("day18/data.txt","r") as file:
        xMax = 0
        yMax = 0
        zMax = 0
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            cords = line.split(",")
            cords = [int(cords[0]),int(cords[1]),int(cords[2])]
            if cords[0]>xMax:
                xMax = cords[0]
            if cords[1] > yMax:
                yMax = cords[1]
            if cords[2] > zMax:
                zMax = cords[2]
        droplet = [[[0 for _ in range(zMax)]for _ in range(xMax)] for _ in range(yMax)]

        for line in lines:
            line = line.strip("\n")
            cords = line.split(",")
            cords = [int(cords[0]),int(cords[1]),int(cords[2])]
            droplet[cords[1]-1][cords[0]-1][cords[2]-1] = 1

    surf = 0
    for x in range(xMax):
        for y in range(yMax):
            for z in range(zMax):
                if droplet[y][x][z] == 1:
                    surf+=openSides(droplet,x,y,z,xMax,yMax,zMax)
    print(surf)

def task2():
    with open("day18/data.txt","r") as file:
        xMax = 0
        yMax = 0
        zMax = 0
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            cords = line.split(",")
            cords = [int(cords[0]),int(cords[1]),int(cords[2])]
            if cords[0]>xMax:
                xMax = cords[0]
            if cords[1] > yMax:
                yMax = cords[1]
            if cords[2] > zMax:
                zMax = cords[2]
        droplet = [[[0 for _ in range(zMax)]for _ in range(xMax)] for _ in range(yMax)]

        for line in lines:
            line = line.strip("\n")
            cords = line.split(",")
            cords = [int(cords[0]),int(cords[1]),int(cords[2])]
            droplet[cords[1]-1][cords[0]-1][cords[2]-1] = 1
    for x in range(xMax):
        for y in range(yMax):
            for z in range(zMax):
                if droplet[y][x][z] == 0:
                    droplet[y][x][z] = isInside(droplet,x,y,z,xMax,yMax,zMax)


    surf = 0
    for x in range(xMax):
        for y in range(yMax):
            for z in range(zMax):
                if droplet[y][x][z] == 1:
                    surf+=openSides(droplet,x,y,z,xMax,yMax,zMax)
    print(surf)



if __name__ == "__main__":
    task1()
    task2()