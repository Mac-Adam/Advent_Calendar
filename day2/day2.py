with open("data.txt",'r') as file:
    lines = file.readlines()
    scoreDict = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3,
        "A" : 1,
        "B" : 2,
        "C" : 3,
    }
    score = 0
    for line in lines:
        line = line.strip("\n")
        (o,y) = line.split(" ")
        o,y = scoreDict[o] , scoreDict[y]
        score +=y
        
        if o == y:
            score +=3
        elif (y==1 and o == 3)or (y == 2 and o == 1) or (y == 3 and o ==2):
            score +=6

        
    print(score)
        