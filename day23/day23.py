
def getElves(elves):
    with open('day23/data.txt','r') as file:
        for y,line in enumerate(file):
            line = line.strip('\n')
            for x,c in enumerate(line):
                if c == '#':
     
                    elves.add((x,y))           

def moveElves(elves,turn):
    moved = False
    checks = [
        [(-1,-1),(0,-1),(1,-1)],
        [(-1,1),(0,1),(1,1)],
        [(-1,1),(-1,0),(-1,-1)],
        [(1,1),(1,0),(1,-1)],
    ]
    ofsets = [
        (-1,-1),
        (0,-1), 
        (1,-1), 
        (1,1), 
        (0,1), 
        (-1,1), 
        (-1,0), 
        (1,0)
        ]

    proposals = dict()
    for elf in elves:
        if not any([(elf[0]+ofset[0],elf[1]+ofset[1]) in elves for ofset in ofsets]):
            continue
        for checkID in range(4):
            checkGroup = checks[(checkID+turn)%4]
            for check in checkGroup:
                if (elf[0]+check[0],elf[1]+check[1]) in elves:
                    break
            else:
                dir = checkGroup[1]
                newPos = (elf[0]+dir[0],elf[1]+dir[1])
                if newPos in proposals:
                    proposals[newPos].append(elf)
                else:
                    proposals[newPos] = [elf]
                break

    for place,elfy in proposals.items():
        if len(elfy) == 1:
            moved = True
            elves.remove(elfy[0])
            elves.add(place)
    return moved
            
def count(elves):
    minX = min(e[0] for e in elves)
    maxX = max(e[0] for e in elves)
    minY = min(e[1] for e in elves)
    maxY = max(e[1] for e in elves)
    return(maxX-minX +1)*(maxY-minY+1)-len(elves)





def task1():
    
    elves = set()
 

    getElves(elves)
    for i in range(10):
        moveElves(elves,i)
    print(count(elves))

   
def task2():
    elves = set()
 

    getElves(elves)
    i = 0
    while moveElves(elves,i):
        i+=1
        print(f"\r{i+1}",end="")
    
if __name__ == "__main__":
    task1()
    task2()