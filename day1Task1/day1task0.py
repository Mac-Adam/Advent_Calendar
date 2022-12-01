
with open("C:/Users/adams/Documents/GitHub/Advent_Calendar/day1Task1/data.txt", "r") as file:
    lines = file.readlines()
    elves = [0]

    for line in lines:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1]+=int(line.strip("\n"))

    bigges = 0
    for e in elves:
        if e >=bigges:
            bigges = e
            
    print(bigges)