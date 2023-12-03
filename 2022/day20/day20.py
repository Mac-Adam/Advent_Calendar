
def mix(data,id):
    val = data.pop(id)
 
    newId = (id+val[1])%len(data)
    
    if newId == 0:
        newId = len(data)
    data.insert(newId,val)

def getData(data,key=1):
    with open("day20/data.txt","r") as file:
        for id,line in enumerate(file):
            data.append((id,int(line)*key))
    
def getIdx(data,val):
    for id,x in enumerate(data):
        if x == val:
            return id

def decrypt(toMix,data):
    for x in data:
        mix(toMix,getIdx(toMix,x))
    return toMix

def getZeroIdx(data):
    for id,x in enumerate(data):
        if x[1] == 0:
            return id

def getRes(data):
    zeroId = getZeroIdx(data)
    id1 = ((zeroId+1000)%len(data))
    id2 = ((zeroId+2000)%len(data))
    id3 = ((zeroId+3000)%len(data))
   
    return data[id1][1] + data[id2][1] + data[id3][1]


def task1():
    data = []
    getData(data)
   
    data = decrypt(data[:],data)
 
    print(getRes(data))
    
def task2():
    data = []
    getData(data,811589153)
   
    res = data[:]
    for _ in range(10):
        res = decrypt(res,data)
    
    print(getRes(res))
    

if __name__ == "__main__":
    task1()
    task2()