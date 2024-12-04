import re
debug = False

def main():
    part1()
    part2()
 
def part1():
    res = 0
    with open("./in2.txt") as f:
         for line in f:
            line = line.strip()
            lvls = line.split()
            lst = None
            dir = None
            for l in lvls:
                l = int(l)
                if lst is None:
                    lst = l
                    continue
                if  not 1 <= abs(lst - l) <= 3:
                    break
                if dir is None:
                    dir = l - lst
                    lst = l
                    continue
                if dir*(l-lst) < 0:
                    break
                lst = l
            else:

                res +=1
           
    print(res)

def is_fine(line,mistakes = 0,skip = 0):
    line = line.strip()
    lvls = line.split()
    lst = None
    dir = None
    if debug: print(lvls)
    flag = mistakes
    for l in lvls:
        if skip == 1:
            skip -= 1
            continue  
        skip -= 1
        l = int(l)
        if lst is None:
            lst = l
            if debug: print("pierwszy", l)
            continue
        if  not 1 <= abs(lst - l) <= 3:
            if debug: print("za duża różnica", l,lst)
            if flag:
                flag -= 1
                continue
            break
        if dir is None:
            if debug: print("nie ma dir", l,lst)
            dir = l - lst
            lst = l
            continue
        if dir*(l-lst) < 0:
            if debug: print("zły dir", l,lst,dir)
            if flag:
                flag -= 1
                continue
            break
        lst = l
    else:
        if debug: print('git')
        return 1
    return 0
    
def part2():
    res = 0
    with open("./in2.txt") as f:
         
         for line in f:
            n = len(line.strip().split())
            for i in range(n+1):
                if is_fine(line,skip=i):
                    res+=1
                    break

           
    print(res)
if __name__ == "__main__":
    main()