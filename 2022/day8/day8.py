
def isVisible(mask,tree):
    minHeigth = min(mask['l'],mask["r"],mask["u"],mask["d"])
    if tree> minHeigth:
        return True , minHeigth
    return False, minHeigth 
def getTask2Val(trees,y,x):
    gridSize = {
        'x': len(trees[0]),
        'y': len(trees)
        }
    thisTreeHeight = trees[y][x]
    #left
    l = 0
    for i in reversed(range(x)):
        l+=1
        if trees[y][i] >= thisTreeHeight:
            break
        
    r = 0
    #right
    for i in range(x+1,gridSize["x"]):
        r+=1
        if trees[y][i] >= thisTreeHeight:
            break
        
    u = 0
    #up
    for i in range(y+1,gridSize["y"]):
        u+=1
        if trees[i][x] >= thisTreeHeight:
            break
        
    d = 0
    #down
    for i in reversed(range(y)):
        d+=1
        if trees[i][x] >= thisTreeHeight:
            break
        
    return l*r*d*u
    
with open("day8/data.txt","r") as file:
    trees = []
    mask = []
    for line in file:
        line = line.strip("\n")
        row = [int(t) for t in line]
        maskRow = [{"u":-1,"d":-1,"l":-1,"r":-1} for _ in line] 
        trees.append(row)
        mask.append(maskRow)
    gridSize = {
        'x': len(trees[0]),
        'y': len(trees)
        }
    for y in range(gridSize["y"]):
        for x in range(gridSize['x']):
            if x == 0:
                continue
            mask[y][x]["l"] = max(mask[y][x-1]["l"],trees[y][x-1])
            mask[y][gridSize["x"]-1-x]["r"] = max(mask[y][gridSize["x"] - x]["r"],trees[y][gridSize["x"] - x])
    for x in range(gridSize["x"]):
        for y in range(gridSize['y']):
            if y == 0:
                continue
            mask[y][x]["u"] = max(mask[y-1][x]["u"],trees[y-1][x])
            mask[gridSize["y"]-1-y][x]["d"] = max(mask[gridSize["y"]-y][x]["d"],trees[gridSize["y"]-y][x])
    visibleTrees = 0
    #output = open("day8/output.txt","w")
    maxVal = 0
    for y in range(gridSize["y"]):
        for x in range(gridSize["x"]):
            val = getTask2Val(trees,x,y)
            if val >= maxVal:
                maxVal = val

    for y in range(gridSize["y"]):
        #line = ""
        for x in range(gridSize["x"]):
            (visibility,reqHeight) = isVisible(tree=trees[y][x],mask=mask[y][x])
            if visibility:             
                #line += "X"
                visibleTrees+=1
            #else:
                #line += str(trees[y][x])             
        #line += "\n"
        #output.write(line)
    #output.close()
    print(visibleTrees)
    print(maxVal)