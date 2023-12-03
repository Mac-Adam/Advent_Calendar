

class Blizzard:
    def __init__(self,pos,dir):
        self.pos = pos
        self.dir = dir

    def move(self,size):
        self.pos[0]+= self.dir[0]
        self.pos[1]+= self.dir[1]
        if self.pos[0] < 1:
            self.pos[0] = size[0]-2
        if self.pos[0] > size[0]-2:
            self.pos[0] = 1
        if self.pos[1] < 1:
            self.pos[1] = size[1]-2
        if self.pos[1] > size[1]-2:
            self.pos[1] = 1
    
def getBlizzards(blizards):
    ##EDIT START NODE IN INPUT AS S AND END NODE AS E
    
    with open("day24/data.txt",'r') as file:
        lookup = {
            "^":(0,-1),
            "v":(0,1),
            '>':(1,0),
            '<':(-1,0)
        }
        for y,line in enumerate(file.readlines()):
            line = line.strip("\n")
            for x,char in enumerate(line):
                if char == "S":
                    start = (x,y)
                elif char == "E":
                    end = (x,y)
                elif char in lookup:
                    blizards.append(Blizzard([x,y],lookup[char]))
    return start,end,(x+1,y+1)

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def isValid(pos,mask,size,end,start):

    if pos == end:
        return True
    if pos == start:
        return True
    if pos[0] < 1:
    
        return False
    if pos[0] > size[0]-2:
    
        return False
    if pos[1] < 1:
    
        return False
    if pos[1] > size[1]-2:
    
        return False
    if mask[pos[1]][pos[0]]:
    
        return False
    return True

def generateMasks(masks,blizzards,size):
    for _ in range((size[1]-2)*(size[0]-2)):
        mask = [[0 for _ in range(size[0])]for _ in range(size[1])]
        for bliz in blizzards:

            mask[bliz.pos[1]][bliz.pos[0]] += 1
            bliz.move(size)
        masks.append(mask)

def shortestPath(start,end,masks,size,startMin = 0):
    queue = [(start,startMin)]
    moves = [
        (1,0),
        (-1,0),
        (0,-1),
        (0,1),
        (0,0)
    ]

    while queue[0][0] != end:
        currNode = queue.pop(0)
        for move in moves:
            newPos = (currNode[0][0]+move[0],currNode[0][1]+move[1])
            if isValid(newPos,masks[(currNode[1]+1)%((size[0]-2)*(size[1]-2))],size,end,start):
              
                if not (newPos,currNode[1]+1) in queue:
                    queue.append((newPos,currNode[1]+1))

        queue.sort(key = lambda x: x[1])
    return queue[0][1]


def task1(masks,size,start,end):
  
    print(shortestPath(start,end,masks,size))

def task2(masks,size,start,end):

       
    t = shortestPath(start,end,masks,size)
    t = shortestPath(end,start,masks,size,t)
    t = shortestPath(start,end,masks,size,t)
    print(t)

if __name__ == "__main__":
    blizzards = []
    start,end,size = getBlizzards(blizzards)
    masks = []
    generateMasks(masks,blizzards,size)
    task1(masks,size,start,end)
    task2(masks,size,start,end)
        