class Elf:

    def __init__(self,pos):
        self.pos = pos
        self.wants = None

def getElves(elves,map):
    with open('day23/data.txt','r') as file:
        onlyValid = []
        for y,line in enumerate(file):
            line = line.strip('\n')
            row = []
            for x,c in enumerate(line):
                if c == '#':
                    elves.append(Elf([x,y]))
                    row.append(True)
                else:
                    row.append(False)
            onlyValid.append(row)
        width = len(onlyValid[0])
        height = len(onlyValid)
        for _ in range(height):
            map.append([False]*3*width)
        for line in onlyValid:
            map.append([False]*width+line+[False]*width)
        for _ in range(height):
            map.append([False]*3*width)
        for elf in elves:
            elf.pos[0] += width
            elf.pos[1] += height

def validForMovement(pos,map):
    toCheck = [
        (1,1),
        (0,1),
        (-1,1),
        (1,0),
        (-1,0),
        (1,-1),
        (0,-1),
        (-1,-1),
        ]
    res = False
    for check in toCheck:
        res = res or map[pos[1]+check[1]][pos[0]+check[0]]
    return res

def checkMovement(pos,type,map):
    cheks = {
        'N':(
            (1,-1),
            (0,-1),
            (-1,-1)
            ),
        'S':(
            (1,1),
            (0,1),
            (-1,1)
            ),
        'W':(
            (-1,1),
            (-1,0),
            (-1,-1)
            ),
        'E':(
            (1,1),
            (1,0),
            (1,-1)
            ),
    }

    res = False
    for check in cheks[type]:
        res = res or map[pos[1]+check[1]][pos[0]+check[0]]
    return not res

def count(map):
    full = 0
    X = set()
    Y = set()
    for y,row in enumerate(map):
        for x,el in enumerate(row):
            if el:
                full+=1
                X.add(x)
                Y.add(y)
    return (max(Y)-min(Y)+1)*(max(X)-min(X)+1)-full





def task1():
    dirDecode = {
        'N':(0,-1),
        'S':(0,1),
        'W':(-1,0),
        'E':(1,0)
    }

    turn =[
        ['N','S','W','E'],
        ['S','W','E','N'],
        ['W','E','N','S'],
        ['E','N','S','W'],
    ]


    elves = []
    map = []
    getElves(elves,map)
    
    mask = [[0 for _ in map[0]]for _ in map]
    

    for i in range(10):
        wants = set()
        for elf in elves:
            if not validForMovement(elf.pos,map):
                continue
            for move in turn[i%4]:
                if checkMovement(elf.pos,move,map):
                    elf.wants = [elf.pos[0]+dirDecode[move][0],elf.pos[1]+dirDecode[move][1]]
                    break
        
        for elf1 in elves:
            for elf2 in elves:
                if elf1 != elf2 and elf1.wants == elf2.wants and elf1.wants != None:     
                    wants.add((elf1.wants[0],elf1.wants[1]))

       
        for elf in elves:   
            if elf.wants:
                
                if not (elf.wants[0],elf.wants[1]) in wants:
                    elf.pos = [elf.wants[0],elf.wants[1]]
                    elf.wants = None
              
   
        mask = [[0 for _ in map[0]]for _ in map]
        map =[[False for _ in mask[0]]for _ in mask]
       
        for elf in elves:
            map[elf.pos[1]][elf.pos[0]] =True
    print(count(map))
       
       
   
if __name__ == "__main__":
    task1()