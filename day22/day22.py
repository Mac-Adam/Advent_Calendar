def getdata(map,moves):
    with open("day22/data.txt",'r') as file:
        gettingMap = True
        for line in file:

            line = line.strip("\n")
            if line == '':
                gettingMap = False
            if not gettingMap:
                curr = ''
                for c in line:
                    directions = ['L','R']
                    if c in directions:
                        moves.append(curr)
                        moves.append(c)
                        curr = ''
                    else:
                        curr += c
                if curr != '':
                    moves.append(curr)
            else:
                row = []
                for c in line:
                    lookup = {
                        ' ':2,
                        '.':0,
                        '#':1
                    }    
                    row.append(lookup[c])
                map.append(row)
            width = 0
            for row in map:
                if len(row)>width:
                    width = len(row)
            for row in map:
                for _ in range(width-len(row)):
                    row.append(2)

def getStartingPos(map):
    for idx,n in enumerate(map[0]):
        if n != 2:
            return idx,0

def inRange(pos,map):
    if pos[0]<0:
        return False
    if pos[1]<0:
        return False
    if pos[1]>= len(map):
        return False
    if pos[0]>=len(map[pos[1]]):
        return False
   
    return True

def wrapAround(pos,dir,map):
    if dir =='R':
        for idx,val in enumerate(map[pos[1]]):
            if val == 1:
                return pos
            if val == 0:
                return idx,pos[1]
    if dir =='D':
        for idx,row in enumerate(map):
            if row[pos[0]] == 1:
                return pos
            if row[pos[0]] == 0:
                return pos[0],idx
    if dir == 'L':
        for idx in reversed(range(len(map[pos[1]]))):
            if map[pos[1]][idx] == 1:
                return pos
            if map[pos[1]][idx] == 0:
                return idx,pos[1]
    if dir == 'U':
        for idx in reversed(range(len(map))):
            if map[idx][pos[0]] == 1:
                return pos
            if map[idx][pos[0]] == 0:
                return pos[0],idx

def nextValidPos(pos,dir,map):
    lookup = {
        'R':(1,0),
        'L':(-1,0),
        'D':(0,1),
        'U':(0,-1),
    }
    desiredPos = pos[0]+lookup[dir][0],pos[1]+lookup[dir][1]
    if inRange(desiredPos,map):
        if map[desiredPos[1]][desiredPos[0]] == 1:
            return pos
        if map[desiredPos[1]][desiredPos[0]] == 0:
            return desiredPos
    return wrapAround(pos,dir,map)


def makeAMove(pos,direction,amount,map):
   
    for _ in range(amount):
       
        nextPos = nextValidPos(pos,direction,map)
        
        if nextPos == pos:
            return pos
        pos = nextPos
    return pos




def task1():
    map = []
    moves =[]
    getdata(map,moves)
    pos = getStartingPos(map)
    direction = 'R'
    dirLookUp={
        'L':{
            'L':'D',
            'R':'U',
            'U':'L',
            'D':'R',
        },
        'R':{
            'L':'U',
            'R':'D',
            'U':'R',
            'D':'L',
        }
    }
    for move in moves:
        if move in dirLookUp:
            direction = dirLookUp[move][direction]
        else:
            pos = makeAMove(pos,direction,int(move),map)
    scoreDir = {
        'R':0,
        'D':1,
        'L':2,
        'U':3
    }
    print(1000*(pos[1]+1)+4*(pos[0]+1)+scoreDir[direction])
if __name__ == '__main__':
    task1()
