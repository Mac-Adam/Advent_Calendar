with open("data.txt",'r') as file:
    lines = file.readlines()
    scoreDict = {
        ("A","X"):3, # r l -> s -> 0 + 3
        ("A","Y"):4, # r d -> r -> 3 + 1
        ("A","Z"):8, # r w -> p -> 6 + 2
        ("B","X"):1, # p l -> e -> 0 + 1
        ("B","Y"):5, # p d -> p -> 3 + 2
        ("B","Z"):9, # p w -> s -> 6 + 3
        ("C","X"):2, # s l -> p -> 0 + 2
        ("C","Y"):6, # s d -> s -> 3 + 3
        ("C","Z"):7, # s w -> r -> 6 + 1
    }
    score = 0
    for line in lines:
        line = line.strip("\n")
        (o,y) = line.split(" ")
        score +=scoreDict[o,y]
        
        
        
    print(score)
        