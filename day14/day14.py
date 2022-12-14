def signum(x):
    if x >0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def getData(data):
    
    for _ in range(500):
        data.append([0 for _ in range(1000)])
    with open("day14/test.txt") as file:
        for line in file:
            line = line.strip("\n")
            rockPossitions = line.split("->")
            formatedRockPossiton = []
            for r in rockPossitions:
                temp = r.split(",")
                formatedRockPossiton.append((int(temp[0]),int(temp[1])))
            #print(formatedRockPossiton)
            last = formatedRockPossiton[0]
            for rockPossition in formatedRockPossiton:
                if rockPossition[0] == last[0]:
                    for i in range(abs(rockPossition[1]-last[1])+1):
                        data[last[1] + i*signum(rockPossition[1]-last[1])][last[0]] = 1
                else:
                    for i in range(abs(rockPossition[0]-last[0])+1):
                        data[last[1]][last[0] + i*signum(rockPossition[0]-last[0])] = 1
                last = rockPossition
    for idx in reversed(range(len(data))):
        if 1 in data[idx]:
            data[idx+2] = [1 for _ in range(1000)]
            break
    

def task1():
    data =[]
    getData(data)

  
    sandSpawned = 0
    possibleMoves = [(0,1),(-1,1),(1,1)]
    while True:
        shouldEnd = False
        sandPos = [500,0]
        if data[0][500] == 2:
            break
        while True:
            if sandPos[1] >= 400:
                shouldEnd = True
                break
            moved = False
            for move in possibleMoves:
                if data[sandPos[1]+ move[1]][sandPos[0]+move[0]] == 0:
                    sandPos[0]+=move[0]
                    sandPos[1]+=move[1]
                    moved = True
                    break
            if not moved:
                data[sandPos[1]][sandPos[0]] = 2
                break

        if shouldEnd:
            break
        sandSpawned+=1
        
    print(sandSpawned)
    with open("day14/outp.txt","w") as outp:
        for l in data:
            line = ""
            for c in l:
                if c == 0:
                    line +='.'
                elif c ==2:
                    line+='o'
                else:
                    line += '#'
            outp.write(line+ "\n")
   

if __name__ == "__main__":
    task1()