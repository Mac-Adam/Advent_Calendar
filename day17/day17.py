import time
def isValidMove(arena,rock,rockPos,move):
    rockAfterMove = []
    for r in rock:
        rockAfterMove.append((r[0]+rockPos[0]+move[0],r[1]+rockPos[1]+move[1]))
    for pos in rockAfterMove:
      
        if pos[0]<0:
          
            return False
        if pos[0]>6:
         
            return False
        if pos[1]<0:

          
            return False
        if arena[pos[1]][pos[0]] != 0:
           
            return False
        
    return True


def task1():
    rocks = [
        ((0,0),(1,0),(2,0),(3,0)),
        ((0,1),(1,0),(1,1),(1,2),(2,1)),
        ((0,0),(1,0),(2,0),(2,1),(2,2)),
        ((0,0),(0,1),(0,2),(0,3)),
        ((0,0),(1,0),(0,1),(1,1)),
    ]


    startTime = time.time()
    with open("day17/data.txt") as file:
        jetMovementsDict = {
            ">":(1,0),
            '<':(-1,0)
        }
        iters = 1000000000000
        jetPattern = file.readline().strip("\n")
        arena = [[0 for _ in range(7)] for _ in range(20)] # make 100% sure it won't overflow
        arena[0] = [1,1,1,1,1,1,1]
        currH = 1
        jetIdx = 0



        for rockIdx in range(iters):
            rock = rocks[rockIdx%5]
            rockPos = [2,currH+3]
            while True:
                
                jetMovement =jetMovementsDict[jetPattern[jetIdx%len(jetPattern)]]
                if isValidMove(arena,rock,rockPos,jetMovement):
                
                    rockPos = [rockPos[0]+jetMovement[0],rockPos[1]+jetMovement[1]]
              
                jetIdx+=1

                if not isValidMove(arena,rock,rockPos,(0,-1)):  
                    for r in rock:
                        posToClaim = [r[0]+rockPos[0],r[1]+rockPos[1]]
                        arena[posToClaim[1]][posToClaim[0]] = 1
                    while 1 in arena[currH]:
                        currH +=1
                        arena.append([0 for _ in range(7)])
                    break
                    
                rockPos[1]-=1


            if rockIdx %10000 == 0:
                if rockIdx == 0:
                    continue
                timeSpent = time.time()-startTime

                print(f"\r {rockIdx} out of {iters} time spent: {timeSpent} estimated time left: {(timeSpent/rockIdx)*(iters-rockIdx)}")


               

        print(currH-1)
    


if __name__ == "__main__":
    task1()