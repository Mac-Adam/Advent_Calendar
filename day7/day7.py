import uuid
class directory:
   
    def __init__(self,name):
        self.name = name
        self.directories = []
        self.fileSizes = 0
        self.id = str(uuid.uuid4())
    def findChildByName(self,name):
        for dir in self.directories:
            if dir.name == name:
                return dir
    
    def addDir(self,name):
        for dir in self.directories:
            if dir.name == name:
                return
        newDir = directory(name)
        self.directories.append(newDir)
    def sumAll(self,dirSizes = dict()):
        dirSizes[self.name+self.id] = self.sumSizes()
        for dir in self.directories:
            dir.sumAll(dirSizes)
        return dirSizes
    def sumSizes(self):
        thisDirSize = self.fileSizes
        for dir in self.directories:
            thisDirSize+= dir.sumSizes()
        return thisDirSize

    def print(self,indentation=0):
        print("  "*indentation,self.name,self.fileSizes)
        for dir in self.directories:
            dir.print(indentation+1)

with open("day7/data.txt") as file:
    baseDir = directory("base")
    currDir = baseDir
    currPath = [baseDir]

    for line in file:
        line = line.strip("\n")
        # print("-"*30+"New Iteration"+ "-"*30)
        # print(f"Curr Dir Name: {currDir.name}")
        # print(line)

        if line.startswith("$"):
            if(line.split(" ")[1] == "ls"):
                continue
            elif(line.split(" ")[1] == "cd"):
                place = line.split(" ")[2]
                if place=="/":
                    currDir = baseDir
                    currPath = [baseDir]
                elif place=="..":
                    currPath.pop()
                    currDir = currPath[-1]
                else:
                    newDir = currDir.findChildByName(place)
                    currDir = newDir
                    currPath.append(newDir)
        elif line.startswith("dir"):
            dirname = line.split(" ")[1]
            currDir.directories.append(directory(dirname))
        else:
            size = int(line.split(" ")[0])
            currDir.fileSizes += size
        #baseDir.print()
    sizes = baseDir.sumAll()
    sum = 0
    for dir in sizes.items():
        print(dir)
    for dirSize in sizes.values():
        if dirSize <=100000:
            sum+= dirSize
    print(sum)

    sizesSorted = list(sizes.values())
    sizesSorted.sort()
    freeSpace = 70000000 - sizesSorted[-1]
    spaceNeeded = 30000000-freeSpace
    for size in sizesSorted:
        if size >= spaceNeeded:
            print(size)
            break
   
    
