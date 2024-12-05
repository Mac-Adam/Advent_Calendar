
def inBounds(val,min,max):
    return min <= val <=max

def main():
    map = []
    with open("./in4.txt") as f:
         for line in f:
            line = line.strip()
            map.append(line)
    dirs = [(i,j) for i in range(-1,2) for j in range(-1,2) if not (i==j==0)]
    maxY = len(map)-1
    maxX = len(map[0])-1
    xmax = 'XMAS'
    res1 = 0
    res2 = 0
    xes = [(-1,-1),(-1,1),(1,1),(1,-1)]
    for (y, row) in enumerate(map):
        for (x, c) in enumerate(row):
            if c == 'X':
                for d in dirs:
                    for i in range(1,4):
                        new_idx_x = x+d[0]*i
                        new_idx_y = y+d[1]*i
                        if not inBounds(new_idx_x,0,maxX):
                            break
                        if not inBounds(new_idx_y,0,maxY):
                            break
                        if map[new_idx_y][new_idx_x] != xmax[i]:
                            break
                        
                    else:
                        res1 += 1
            elif c == 'A':
                Xmas = 'MSSM'
                for r in range(4):
                    for (i,d) in enumerate(xes):
                        
                        new_idx_x = x+d[0]
                        new_idx_y = y+d[1]
                        if not inBounds(new_idx_x,0,maxX):
                            break
                        if not inBounds(new_idx_y,0,maxY):
                            break
                        if map[new_idx_y][new_idx_x] != Xmas[(i+r)%4]:
                            break
                    else:
                        res2 +=1
    print(res1)
    print(res2)


if __name__ == "__main__":
    main()