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

def chunkify(map,mesh):
    chunkSize = 50
    chunks = []
    for i in range(len(map)//chunkSize):
        meshRow = []
        chunksRow = []
        for j in range(len(map[0])//chunkSize):
            chunk = []
            if 0 in map[i*chunkSize][j*chunkSize:(j+1)*chunkSize]:
                meshRow.append(1)
            else:
                meshRow.append(0)
            
            for x in range(chunkSize):
                chunk.append(map[i*chunkSize+x][j*chunkSize:(j+1)*chunkSize])
            chunksRow.append(chunk)
        mesh.append(meshRow)
        chunks.append(chunksRow)
    return chunks




def rotateRight(chunk):
    size = len(chunk)
    newChunk = []
    for oldX in range(size):
        newRow = []
        for oldY in reversed(range(size)):
            newRow.append(chunk[oldY][oldX])
        newChunk.append(newRow)
    return newChunk

def rotateLeft(chunk):
    size = len(chunk)
    newChunk = []
    for oldX in reversed(range(size)):
        newRow = []
        for oldY in range(size):
            newRow.append(chunk[oldY][oldX])
        newChunk.append(newRow)
    return newChunk

def flipHorizontaly(chunk):
    newChunk = []
    for row in chunk:
       newChunk.append(row[::-1])
    return newChunk

def flipVerticaly(chunk):
    size = len(chunk)
    newChunk = []
    for oldY in reversed(range(size)):
        newRow = []
        for oldX in range(size):
            newRow.append(chunk[oldY][oldX])
        newChunk.append(newRow)
    return newChunk




def task2():
    chunkSize = 50
    map = []
    moves = []
    mesh = []
    getdata(map,moves)
    chunks = chunkify(map,mesh)
    for r in mesh:
        print(r)
    print()

    # strip = 2
    # pos=(0,11)
    # direction ='U'

    # strips = [
    #     flipVerticaly(chunks[1][0])+chunks[0][2]+ chunks[1][2]+chunks[2][2],
    #     rotateRight(chunks[1][0])+rotateRight(chunks[1][1])+rotateRight(chunks[1][2])+chunks[2][3],
    #     rotateRight(chunks[2][2]) + rotateRight(chunks[2][3]) + rotateLeft(chunks[0][2]) + chunks[1][1]
    #     ]
  
    # stripTranslation = {
    #     (0,0):(1,0,1),
    #     (0,1):(2,2,1),
    #     (0,2):(1,2,-1),
    #     (0,3):(2,0,-1),
    #     (1,0):(0,0,-1),
    #     (1,1):(2,3,1),
    #     (1,2):(0,2,1),
    #     (1,3):(2,1,-1),
    #     (2,0):(0,3,1),
    #     (2,1):(1,3,1),
    #     (2,2):(0,1,-1),
    #     (2,3):(1,1,-1)
    # }

    strip = 1
    pos=(0,150)
    direction ='U'

    strips = [
        chunks[0][1]+chunks[1][1]+ chunks[2][1]+rotateLeft(chunks[3][0]),
        rotateRight(chunks[2][0])+rotateRight(chunks[2][1])+rotateLeft(chunks[0][2])+rotateLeft(chunks[0][1]),
        chunks[2][0] + chunks[3][0] + chunks[0][2] + rotateLeft(chunks[1][1])
    ]
  
    stripTranslation = {
        (0,0):(1,3,1),
        (0,1):(2,3,1),
        (0,2):(1,1,-1),
        (0,3):(2,1,-1),
        (1,0):(2,0,1),
        (1,1):(0,2,1),
        (1,2):(2,2,-1),
        (1,3):(0,0,-1),
        (2,0):(1,0,-1),
        (2,1):(0,3,1),
        (2,2):(1,2,1),
        (2,3):(0,1,-1)
    }

    dirLookup = {
        'R':{
            (-1,'U'):'D',
            (1,'U'):'U',
            (-1,'D'):'U',
            (1,'D'):'D',
            },
        'L':{
            (1,'U'):'D',
            (-1,'U'):'U',
            (1,'D'):'U',
            (-1,'D'):'D',
            }
    }
    for move in moves:
        if move in dirLookup:
            chunkId = pos[1]//chunkSize
            chunkPos = pos[0],pos[1]%chunkSize
            afterMove = stripTranslation[(strip,chunkId)]
            strip = afterMove[0]
            newChunkId = afterMove[1]
            if afterMove[2] == -1:
                newChunkPos = chunkSize-chunkPos[1]-1,chunkPos[0]
            else:
                newChunkPos = chunkPos[1],chunkSize-chunkPos[0]-1
            direction = dirLookup[move][(afterMove[2],direction)]
            pos = newChunkPos[0],newChunkId*chunkSize+newChunkPos[1]
        else:
            pos = makeAMove(pos,direction,int(move),strips[strip])
        #print(move,pos,direction,strip)
        
    print(strip,pos,direction)

if __name__ == '__main__':
    task1()
    task2()
