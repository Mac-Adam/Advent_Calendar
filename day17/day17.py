
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
        realH = 1

        jetIdx = 0
        hAterRocks = []

        cycles = []
        cycleH = dict()

        for rockIdx in range(iters):
            if not 0 in arena[currH-1] and currH !=1:
                if((rockIdx%5,jetIdx%len(jetPattern)) in cycles):

                    cycleData =cycleH[(rockIdx%5,jetIdx%len(jetPattern))]

                    cycleHeight = currH - cycleData[0]
                    cycleLen = rockIdx-cycleData[1]
                    cyclesFit = (iters-rockIdx)//(cycleLen)
                    left = (iters-rockIdx)%cycleLen
                
                    #print(f"Cycle of len {cycleLen} of height {cycleHeight} can fit {cyclesFit} will need to calc {left}")
                    print(f"This means H should be {currH+cycleHeight*cyclesFit + hAterRocks[cycleData[1]+left]}")
                    input()
                else:
                    cycles.append((rockIdx%5,jetIdx%len(jetPattern)))
                    cycleH[cycles[-1]] = (currH,rockIdx)


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
            hAterRocks.append(currH)

          
               

        print(currH-1)
    


if __name__ == "__main__":
    task1()