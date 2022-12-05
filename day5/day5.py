
with open("day5/data.txt","r") as file:
    lines = file.readlines()
    cargoLines = []
    cargo = []
    moves = []
    cargoFinished = False

    for line in lines:
        if line == "\n":
            cargoFinished = True
            continue
        if(cargoFinished):
            moves.append(line.strip("\n"))
        else:
            cargoLines.append(line.strip("\n"))
       
    cargoLength = int(cargoLines[-1].strip("\n")[-2])

    cargo = ["" for _ in range(cargoLength)]

    for i in range(cargoLength):
        for cargoLine in cargoLines[:-1]:
            crate = cargoLine[1+i*4]
            if crate != " ":
                cargo[i]+=crate
    for x in range(len(cargo)):
        rev = ""
        for i in range(len(cargo[x])):
            rev+=cargo[x][len(cargo[x])-1-i]      
        cargo[x] = rev
    idx =0
    for move in moves:
        print(cargo)
        print(move)

        amount  = int(move.split("from")[0].strip("move"))
        fromTo = move.split("from")[1].split("to")
        fr = int(fromTo[0]) -1
        to = int(fromTo[1]) -1

        # for x in range(amount):

        #     cargo[to]+=cargo[fr][-1]
        #     cargo[fr] = cargo[fr][:-1]
        cargo[to]+= cargo[fr][-amount:]
        cargo[fr] = cargo[fr][:-amount]

    message = ""
    print(cargo)
    for stack in cargo:
        message+=stack[-1]

    print(message)

