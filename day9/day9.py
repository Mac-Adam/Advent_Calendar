def updateTailPos(headX,headY,tailX,tailY):
    lookup = {
        (-2,0):(-1,0),
        (-2,1):(-1,0),
        (-2,-1):(-1,0),

        (2,0):(1,0),
        (2,1):(1,0),
        (2,-1):(1,0),

        (0,2):(0,1),
        (1,2):(0,1),
        (-1,2):(0,1),

        (0,-2):(0,-1),
        (1,-2):(0,-1),
        (-1,-2):(0,-1),

        (-2,-2):(-1,-1),
        (2,2):(1,1),
        (-2,2):(-1,1),
        (2,-2):(1,-1),
    }

    relativeX, relativeY = tailX-headX,tailY-headY
   
    if (relativeX,relativeY) in lookup:
        relativeX,relativeY = lookup[(relativeX,relativeY)]   
        return headX + relativeX, headY + relativeY

    return tailX,tailY

def move(headX,headY,direction):
    directionLookup = {
            "U": (0,1),
            "D": (0,-1),
            "L": (-1,0),
            "R": (1,0)
    }
    headX += directionLookup[direction][0]
    headY += directionLookup[direction][1]
    return headX,headY

def task2():
    with open("day9/data.txt") as file:
        beenTo = set()  
        knots = [(0,0) for _ in range(10)]

        for comand in file:
            direction = comand.split(" ")[0]
            steps = comand.split(" ")[1]

            for _ in range(int(steps)):
                knots[0] =  move(knots[0][0],knots[0][1],direction)

                for idx in range(len(knots)-1):
                    knots[idx+1] = updateTailPos(knots[idx][0],knots[idx][1],knots[idx+1][0],knots[idx+1][1])

                beenTo.add((knots[-1]))
        print(f"task2: {len(beenTo)}")



def task1():
    with open("day9/data.txt") as file:
        beenTo = set()
      
        headX = 0
        headY = 0
        tailX = 0
        tailY = 0

        for comand in file:
            direction = comand.split(" ")[0]
            steps = comand.split(" ")[1]

            for _ in range(int(steps)):
    
                headX, headY = move(headX,headY,direction)
                tailX,tailY = updateTailPos(headX,headY,tailX,tailY)
                beenTo.add((tailX,tailY))
             
        print(f"task1: {len(beenTo)}")



def main():
    task1()
    task2()


if __name__ == "__main__":
    main()